
// based on: http://tympanus.net/Development/ArticleIntroEffects/index3.html

(function() {

    if ($('.post-template:not(.page)').length) {

        // detect if IE : from http://stackoverflow.com/a/16657946      
        var ie = (function(){
            var undef,rv = -1; // Return value assumes failure.
            var ua = window.navigator.userAgent;
            var msie = ua.indexOf('MSIE ');
            var trident = ua.indexOf('Trident/');

            if (msie > 0) {
                // IE 10 or older => return version number
                rv = parseInt(ua.substring(msie + 5, ua.indexOf('.', msie)), 10);
            } else if (trident > 0) {
                // IE 11 (or newer) => return version number
                var rvNum = ua.indexOf('rv:');
                rv = parseInt(ua.substring(rvNum + 3, ua.indexOf('.', rvNum)), 10);
            }

            return ((rv > -1) ? rv : undef);
        }());


        // disable/enable scroll (mousewheel and keys) from http://stackoverflow.com/a/4770179                  
        // left: 37, up: 38, right: 39, down: 40,
        // spacebar: 32, pageup: 33, pagedown: 34, end: 35, home: 36
        var keys = [32, 37, 38, 39, 40], wheelIter = 0;

        function preventDefault(e) {
            e = e || window.event;
            if (e.preventDefault)
            e.preventDefault();
            e.returnValue = false;  
        }

        function keydown(e) {
            for (var i = keys.length; i--;) {
                if (e.keyCode === keys[i]) {
                    preventDefault(e);
                    return;
                }
            }
        }

        function touchmove(e) {
            preventDefault(e);
        }

        function wheel(e) {
            // for IE 
            //if( ie ) {
                //preventDefault(e);
            //}
        }

        function disable_scroll() {
            window.onmousewheel = document.onmousewheel = wheel;
            document.onkeydown = keydown;
            document.body.ontouchmove = touchmove;
        }

        function enable_scroll() {
            window.onmousewheel = document.onmousewheel = document.onkeydown = document.body.ontouchmove = null;  
        }

        var docElem = window.document.documentElement,
            scrollVal,
            isRevealed, 
            noscroll,
            isAnimating,
            container = document.getElementById( 'notepad-post-container' ) || document.getElementById( 'main-content' ) || document,
            trigger = container.querySelector( 'button.trigger' );

        function scrollY() {
            return window.pageYOffset || docElem.scrollTop;
        }

        function scrollPage() {
            scrollVal = scrollY();
            
            if( noscroll && !ie ) {
                if( scrollVal < 0 ) return false;
                // keep it that way
                window.scrollTo( 0, 0 );
            }

            if( $(container).hasClass('notrans')) {
                $(container).removeClass('notrans');
                return false;
            }

            if( isAnimating ) {
                return false;
            }
            
            if( scrollVal <= 0 && isRevealed ) {
                toggle(0);
            }
            else if( scrollVal > 0 && !isRevealed ){
                toggle(1);
            }
        }

        function toggle( reveal ) {
            isAnimating = true;
            
            if( reveal ) {
                $(container).addClass('modify');
            }
            else {
                noscroll = true;
                disable_scroll();
                $(container).removeClass('modify');
            }

            // simulating the end of the transition:
            setTimeout( function() {
                isRevealed = !isRevealed;
                isAnimating = false;
                if( reveal ) {
                    noscroll = false;
                    enable_scroll();
                }
                if (typeof BackgroundCheck !== 'undefined' && BackgroundCheck.refresh) {
                    BackgroundCheck.refresh();
                }
            }, 600 );
        }

        // refreshing the page...
        var pageScroll = scrollY();
        noscroll = pageScroll === 0;

        if( pageScroll ) {
            isRevealed = true;
            $(container).addClass('notrans');
            $(container).addClass('modify');
            enable_scroll();
        } else {
            // Only disable scroll if we have a trigger button and container
            if (trigger && container && container !== document) {
                disable_scroll();
            } else {
                // No trigger button or container not found - auto-reveal content
                isRevealed = true;
                $(container).addClass('modify');
                enable_scroll();
            }
        }
        
        // Auto-reveal after a short delay if content is still hidden
        setTimeout(function() {
            if (!isRevealed && container && container !== document) {
                toggle(1);
            }
        }, 500);

        window.addEventListener( 'scroll', scrollPage );

        if (trigger) {
            trigger.addEventListener( 'click', function() { toggle( 1 ); } );
        }
    
    }

})();