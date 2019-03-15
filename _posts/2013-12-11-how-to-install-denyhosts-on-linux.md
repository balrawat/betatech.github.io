---
layout: post
title: How To Install DenyHosts on Linux
date: '2013-12-11T16:41:00.002+05:30'
author: Balvinder Rawat
tags:
  - brute force protection
  - denyhosts
  - SSH
modified_time: '2013-12-11T16:41:47.918+05:30'
thumbnail: >-
  http://4.bp.blogspot.com/-lqyHtF9bBvM/UqhIVsscNSI/AAAAAAAAAwY/8zi9JsnGu1M/s72-c/DenyHosts.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-4413577211053553078'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/12/how-to-install-denyhosts-on-linux.html'
---
[![](http://4.bp.blogspot.com/-lqyHtF9bBvM/UqhIVsscNSI/AAAAAAAAAwY/8zi9JsnGu1M/s400/DenyHosts.png)][1]

### About DenyHosts

* * *

DenyHosts is a security tool written in python that monitors server access logs to prevent brute force attacks on a linux server. The program works by banning IP addresses that exceed a certain number of failed login attempts.  
  

Step One—Install Deny Hosts
---------------------------

* * *

DenyHosts is very easy to install on Ubuntu

_\#  apt-get install denyhosts_

On RHEL/Centos:

We need[epel repo][2]to install fail2ban on RHEL/Centos based machines.

So, download the rpm:-

_\# wget[http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm][3]_

and, then install

_\# yum install denyhosts_

Once the program has finished downloading, denyhosts is installed and configured on your linux server.  
  
  

Step Two—Whitelist IP Addresses
-------------------------------

* * *

After you install DenyHosts, make sure to whitelist your own IP address. Skipping this step will put you at risk of locking yourself out of your own machine.  
  
Open up the list of allowed hosts allowed on your server:

vim /etc/hosts.allow

  
Under the description, add in any IP addresses that cannot afford to be banned from the server; you can write each one on a separate line, using this format:

_\# sshd: 12.34.45.678_

  
After making any changes, be sure to restart DenyHosts so that the new settings take effect on your linux server:

_\# /etc/init.d/denyhosts restart_

  

**Step Three—(Optional) Configure DenyHosts**

* * *

DenyHosts is ready use as soon as the installation is over.  
  
However if you want to customize the behavior of DenyHosts on your server, you can make the changes within the DenyHost configuration file:

_\# vim /etc/denyhosts.conf_

  

[1]: http://4.bp.blogspot.com/-lqyHtF9bBvM/UqhIVsscNSI/AAAAAAAAAwY/8zi9JsnGu1M/s1600/DenyHosts.png
[2]: http://www.linuxtechtips.com/2012/11/installing-rhel-epel-repo-on-centos-5x.html
[3]: http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

