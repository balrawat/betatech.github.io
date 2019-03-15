---
layout: post
title: Working with Apache mod_rewrite module
date: '2013-12-10T13:13:00.000+05:30'
author: Balvinder Rawat
tags:
  - mod_rewrite
  - url rewriting
  - apache
modified_time: '2013-12-10T13:13:13.266+05:30'
thumbnail: >-
  http://2.bp.blogspot.com/-DASzpcLHH_U/UqbFGNwOaWI/AAAAAAAAAv4/UmIqIVEA6No/s72-c/mod_rewrite.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-4551079773210108364'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/working-with-apache-mod-rewrite-module.html
---
[![](http://2.bp.blogspot.com/-DASzpcLHH_U/UqbFGNwOaWI/AAAAAAAAAv4/UmIqIVEA6No/s640/mod_rewrite.png)][1]

**Introduction**

This is a guide to the Apache mod_rewrite module. This is a module included with the Apache web-server which provides the ability to manipulate URLs prior to determining the appropriate file or handing off to a script. This is commonly used when a visitor goes to a certain web address, but the server returns a different document to the one implied by the page address.

If you've ever wanted to be able to offer different URL's for the same file, or even direct to a different website all together then mod\_rewrite can help. It offers more functionality than the mod\_alias module which can be used to perform some basic mapping between URL's and filenames.

Documentation is available with the module, but it can be difficult to understand at first. This guide for mod_rewrite provides some simple examples to get an idea of what can be achieved.

Some of the examples shown here could be performed using the simpler mod\_alias, but understanding mod\_rewrite will allow better future proofing if additional flexibility is needed in future. This guide only covers some basic concepts. After reading this and experimenting with your own server you should then read the [Apache mod_rewrite documentation][2] to understand what is actually happening. \[The link is for Apache version 2.0\].

**mod_rewrite and regular expressions**

Regular expressions are a way of manipulating text by using character strings and metacharacters. The Apache mod_rewrite module uses regular expressions extensively, so it's well worth learning a little about regular expressions.

If however the talk of regular expressions sends a cold shiver down your spine then it is still possible to create some rewrite rules (and examples are provided) without really understanding regular expressions. But you will only have limited functionality and will not be using the full power of the mod_rewrite module.

You can view the [Beginner programming guide to regular expressions on LinuxTechTips][3]. The regular expression meta-characters are similar to those used by the perl language.

**Getting started with mod_rewrite**

The rewrite rules can be either in the server configuration files, or in the .htaccess files on a per folder basis. To add the RewriteRules to the server configuration files (eg. httpd.conf) will require root (administrator) access to the web server.

If you don't have root access (eg. on a hosted web server) then these will need to be added to the .htaccess file instead. The .htaccess file is normally located in the root directory of the server (eg. public\_html directory), although it could be installed in a lower subdirectory to only apply to that directory and below. If using the mod\_rewrite in the .htaccess then you should normally omit the first '/' in the rules.

If you are not using virtual hosts then you can add the entries within the <Directory /> section of the server config file. On Ubuntu this will normally be in the appropriate file within the /etc/apache2/sites-enabled directory. On other distributions this could instead be in: httpd.conf; httpd2.conf; or commonhttpd.conf which in the /etc/httpd/conf directory, or the appropriate vhosts.conf.

The first entry is needed to turn the rewrite engine on. The entry should be:

  

RewriteEngine on

  

followed by one or more RewriteRule entries:

  

RewriteRule _Pattern Substitution_

  

Some examples of this are shown below.

**Redirect one page to another**

As a basic example the following is a typical virtual hosts entry:

<VirtualHost *:80>

  

ServerName www.linuxtechtips.com

  

DocumentRoot /var/www/html

  

  

  

RewriteEngine on

  

RewriteRule ^/index\\.html$ /index.php \[L\]

  

<VirtualHost>

This example is for the virtual host www.linuxtechtips.com. The first few lines are the normal definitions for the virtual host. Next is the RewriteEngine directive to enable the rewrite rules, followed by any Rewrite Rules. In this example there is just one rewrite rule, but there could be more by having multiple RewriteRule entries, but the RewriteEngine entry only needs to be included once.

If this was included in the .htaccess file it would instead be written as

RewriteEngine on

  

RewriteRule ^index\\.html$ /index.php \[L\]

(note the lack of / at the beginning of the regular expression).

**Structure of a Rewrite Rule**

The Rewrite example can be read as follows:

RewriteRule ^/index\\.html$ /index.php \[L\]

·         **^/index\\.html$** The pattern to find

·         **/index.php** What to substitute the entry with

·         **\[L\]** Options that control how this works

This example is used because the index.html file has now been replaced with a PHP file index.php. This is a something that I did with my website when I wanted to add some dynamic updates to the index page. So anyone that tried to access http://www.linuxtechtips.com/index.html , will get the resulting page [http://www.linuxtechtips.com/index.php][4]

The pattern matched is the string ^/index\\.html$, which works as follows:

·         **^** Pattern must be begin with the following expression. In this example it means that the file must be /index.html and not /info/index.html or any other combination.

·         **/index\\.html** The string to be matched must be /index.html. The \\. means that it must be an explicit period character, without the \ then the period is used as a special regular expressions character to mean any charactor.

·         **$** Whilst not strictly required in this example the dollar indicates that this must also be at the end of the string. So it will not match anything after index.html.

If the pattern is matched then the file /index.php will be returned.

**RewriteRule Options**

The **\[L\]** option indicates that this if the match is successful then this is the Last substitution it should try. So if the file was index.html, after this rule has been successfully applied any subsequent RewriteRule directives will be ignored. Again this is not required for this example, but it is a good habit to always include \[L\] unless you want subsequent rules to be applied (the flexibility of being able to apply subsequent RewriteRules to the modified URL is one of the powerful features of this module).

The user viewing the pages will not know that this rewriting of the URL has occurred. As far as they see they will be getting the entry index.html. The next example will introduce another option for a force redirect.

**Change the browser url using Force Redirect**

The force redirect returns a different page as per the first example, but is normally used when a file has permanently changed location and you would like future visitors to go straight to the new url.

RewriteRule ^/info.html$ /info/index.html \[R,L\]

This is a simple rules that replaces a file called /info.html with a info directory, returning the index.html page within that directory. Note that I have not included a '\\' before the '.' character in this example. This means that particular character. For example it would also match /info-html, although it is unlikely that there would any other files that would be matched by mistake.

When this rule is applied then Apache will return a external redirect (302 moved temporarily) to the browser causing it to update its location bar and causing it to request the new page. This way the user can see that the page location has changed and if copying the url will get the new url.

There is another reason that this rule may need to be a force redirect. The new page returned is in a different directory to the old file, so if it uses relative urls (eg. images) then if the force redirect option was note selected then any relative paths would be applied against the / directory instead of the /info directory.

**Rewrite multiple pages**

In the previous examples we have replaced one file with another. The real power of the RewriteRule is when a single entry can match multiple different URLs. The next example shows how you can convert a user friendly URL so that it can be used for a script.

RewriteRule ^/linux/(.*) /linux.php?page=$1 \[L\]

This example is a little more complex in that we are actually using the regular expression to copy part of the pattern into the substitution. This is similar to a rewrite rule that I have on this site for the tutorial pages (eg this page).

Part of the pattern in brackets which is the part we want to copy over to the substitution. Anything (.*) below the linux directory is matched and instead used as a parameter for the linx.php page. So for example if we had /linux/apache-mod\_rewrite (this page) then it would be transposed to /linux.php?page=apache-mod\_rewite . If you had more sections then each bracket in the match will have a corresponding variable that can be used in the substitution. ie. the second bracket would be $2, the third $3 etc.

In this case I have already taken into consideration the effect of using a different directory, so it is not necessary to use the force redirect option.

**Managing Rewrite Rules**

Rewrite rules are processed in the order they are listed until the end or a match with a \[L\] is applied. This can be the source of some unexpected results if one rewrite rule is applied on top of a url that has already had a rewrite applied to it.

The rewrite rules can be included in either the http config files (e.g. httpd.conf or Vhosts.conf), or if allowed in .htaccess files.

Another way of including entries into the web server configuration files is to use the include statement. This allows the rewrite rules to be stored in a separate file to make it easier to manage. For example if you wanted to create a file with static filenames that are used in publicity materials etc. then this can included in the Vhosts.conf file using the entry:

  

Include /etc/httpd/conf/staticlinks.conf

  

**Adding Conditional rules - RewriteCond**

The RewriteCond adds a condition that must be matched to allow the subsequent RewriteRule to be applied. This adds a great deal of flexibility to mod_rewrite allowing different pages to be served depending upon various different variables such as the IP address of the visitor, the webbrowser they are running or even the day of the week that they are visiting.

**The Query String – after the question mark**

One thing that can trip up the unwary (including me when I first came across this) is that the RewriteRules mentioned earlier only work on the URL prior to any question marks '?'. Although, confusingly, you can change the values after the question mark in the RewriteRule in the substitution string. The reason for this is because the RewriteRule match only works on the hierarchical part of the incoming URL. The part after the ? is referred to as the query string and that is accessed differently.

The query string is accessed through the RewriteCond rule. To use RewriteCond rules needs a minimum of two lines; a RewriteCond and a RewriteRule. The RewriteCond is a condition under which the subsequent RewriteRule is applied. If you are familiar with programming then the RewriteCond acts like a an If Statement to determine if the RewriteRule is applied.

This next example uses the RewriteCond to only match if there is no query string:

RewriteCond %{QUERY_STRING} =""

  

RewriteRule ^photos/?$ /gallery.php?action=index \[L\]

In this case the RewriteCond just checks to see if there is any query string or not. If there is no query string (ie. it matches an empty string) then it applies the following rule which displays the photo gallery index page.

  

ie. going to page /photos will redirect to /gallery.php?action=index

  

The /? means that it will match either /photos or /photos/

  

The next example looks for a certain string in the query string and then uses that in the RewriteRule.

RewriteCond %{QUERY_STRING} ^(.\*album=.\*)$

  

RewriteRule ^photos/?$ /gallery.php?%1 \[L\]

In this case it looks for an album= section in the query string. Assuming this is included it then appends that to the Rewrite substitution. Note that %1 is used as opposed to $1 which is used if we were using a match from the RewriteRule expression. .* is used before and after the album to copy the entire query string over to the RewriteRule. In this case anything after the album parameter will also be included, but this could be changed to only match that section by using \\w instead of '.' and moving the brackets appropriately. If the brackets were placed around the parameter instead of the entire string then it will only put that part of the string into the RewriteRule substitution.

For example:

RewriteCond %{QUERY_STRING} ^album=(\\w*)$

  

RewriteRule ^photos/?$ /gallery.php?category=%1 \[L\]

which will result in the album parameter being used as category instead.

**Match on IP address**

Another useful feature of the RewriteCond is to match on IP address. The next example will redirect all visitors to the offline.html file unless they are coming from IP address 192.168.3.5. An example of where you may want to do this is when performing an upgrade to the website where other visitors are sent to an "upgrade in progress" page, but allowing the administrator access to the page to test it before going live.

Warning: Don't use this rule as it is – see the improved version afterwards.

\# Rewrite on IP address example - do not use on a real site

  

RewriteCond %{REMOTE_HOST} !^192\\.168\\.3\\.5

  

RewriteRule .* /offline.html \[R=302,L\]

The IP address of the visitor is accessible as %{REMOTE_HOST} and in this case I match on not (!) 192.168.3.5

I've also used the 302 rewrite rule which is a http temporary redirect.

The problem with the rule above is that it will also match on the offline.html file creating a loop. It is however possible to chain multiple RewriteCond rules together and the following gets around that by only Rewriteing in the request is not for the offline.html file.

\# Rewrite on IP address example - improved version

  

RewriteCond %{REMOTE_HOST} !^77\\.103\\.252\\.244

  

RewriteCond %{REQUEST_URI} !/offline\\.html$

  

RewriteRule .* /offline.html \[R=302,L\]

**Conclusion**

From the few examples above it is easy to see just how versatile mod_rewrite can be. It can manipulate the request in just about anyway you can think of. This is useful when trying to provide user friendly URLs, files being moved, or a temporary maintenance mode.

  

  

The combination of RewriteCond and RewriteRule can be used to do lots more, but hopefully this has provided enough information to get started.

  

[1]: http://2.bp.blogspot.com/-DASzpcLHH_U/UqbFGNwOaWI/AAAAAAAAAv4/UmIqIVEA6No/s1600/mod_rewrite.png
[2]: http://httpd.apache.org/docs-2.0/mod/mod_rewrite.html
[3]: http://www.linuxtechtips.com/2013/12/working-with-regular-expressions.html
[4]: http://www.linuxtechtips.com/index.php

