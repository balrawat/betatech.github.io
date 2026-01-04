---
layout: post
title: AMD Radeon™ HD 7670M on Ubuntu 12.04
date: '2012-12-08T14:24:00.003+05:30'
author: Balvinder Rawat
tags:
  - ubuntu
  - graphics card
  - linux
  - AMD Radeon
modified_time: '2013-11-24T08:42:53.774+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-5076778965212841467'
blogger_orig_url: 'https://www.linuxtechtips.com/2012/12/amd-radeon-hd-7670m-on-ubuntu-1204.html'
---
(function(d, s, id) { var js, fjs = d.getElementsByTagName(s)\[0\]; if (d.getElementById(id)) return; js = d.createElement(s); js.id = id; js.src = "//connect.facebook.net/en_US/all.js#xfbml=1"; fjs.parentNode.insertBefore(js, fjs); }(document, 'script', 'facebook-jssdk'));  

> _**Update:  **__Recently I install kubuntu 13.10 and there is no problem with graphics. It just works  fine out of the box._

  

I've seen many blog posts on how to make AMD HD7670M work on Ubuntu 12.04, specially when its in switchable graphics board like Dell Inspiron 15R 5520. I tried many things to make it work so that I could use the [cinnamon][1] desktop on ubuntu & other things too.. But to my surprise even the drivers from AMD site didn't work.

  

Then I tried a combination of those blog posts I read & somehow I became successful in running the full graphics including compiz settings inside My Ubuntu Machine.

  

Following are the steps I followed & it worked...

  

1\. Create a backup of your xorg configuration file:

  

_**sudo cp /etc/X11/xorg.conf /etc/X11/xorg.conf.BAK**_

  

2\. Remove/purge current fglrx and fglrx-amdcccle :

  

_**sudo apt-get remove --purge fglrx***_

  

3\. Install the driver:

  

_**sudo apt-get install fglrx fglrx-amdcccle**_

  

4\. Install additional components for advanced graphics:

  

_**sudo apt-get install xvba-va-driver libva-glx1 libva-egl1 vainfo**_

  

5\. Generate a fresh xorg.conf:

  

_**sudo aticonfig --initial**_

  

6\. Reboot.

  

Take a deep breath....

  

The graphics should work now...

  

**In case you still have problem getting them to work, make sure you have following lines in the /etc/fstab**

  

_**tmpfs /dev/shm tmpfs defaults 0 0**_

  

__**none /sys/kernel/debug debugfs defaults 0 0**__

  

  

Hope it helps :)

  

[1]: https://cinnamon.linuxmint.com/

