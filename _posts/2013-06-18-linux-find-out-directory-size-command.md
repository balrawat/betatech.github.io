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
`\[root@myserver ~\]# du -sh /usr/*`
`71M     /usr/bin`
`8.0K    /usr/etc`
`8.0K    /usr/games`
`87M     /usr/include`
`122M    /usr/java`
`1.8M    /usr/kerberos`
`535M    /usr/lib`
`199M    /usr/lib64`
`12M     /usr/libexec`
`212M    /usr/local`
`17M     /usr/sbin`
`563M    /usr/share`
`57M     /usr/src`
`4.0K    /usr/tmp`
`48M     /usr/X11R6`

