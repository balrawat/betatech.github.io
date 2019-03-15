---
layout: post
title: 'Linux: Find Out Directory Size Command'
date: '2013-06-18T16:04:00.001+05:30'
author: Balvinder Rawat
tags:
  - linux commands
modified_time: '2013-08-06T16:33:29.381+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-8160221597441908749'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/06/linux-find-out-directory-size-command.html
---
  
  
To get the size of a Directory in Linux, use du command. du command is used to find the file space usage & summarize disk usage of each file/directory.  
  
To find the size of /usr directory:  
  
  du /usr  
OR  
  
 Pass -s option to see the total disk space summary & -h option for human readable format.  
  
  du -sh /usr  
  
  
We can also list the contents of the directory (whether file or directory) with size:-  
  
du -sh /usr/*  
  
Sample output:  
_\[root@myserver ~\]# du -sh /usr/*_  
_71M     /usr/bin_  
_8.0K    /usr/etc_  
_8.0K    /usr/games_  
_87M     /usr/include_  
_122M    /usr/java_  
_1.8M    /usr/kerberos_  
_535M    /usr/lib_  
_199M    /usr/lib64_  
_12M     /usr/libexec_  
_212M    /usr/local_  
_17M     /usr/sbin_  
_563M    /usr/share_  
_57M     /usr/src_  
_4.0K    /usr/tmp_  
_48M     /usr/X11R6_

