---
layout: post
title: How to keep a script running even after logging out of the system
date: '2013-09-07T16:16:00.000+05:30'
author: Balvinder Rawat
tags:
  - linux commands
  - shell
modified_time: '2013-09-07T16:17:47.802+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-571938648088808142'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/09/how-to-keep-script-running-after-logout.html
---
There are times when we need to do some job or run some script which takes a lot of time. During this the connection can get aborted which results in the job getting killed. There is simple solution for this, Use NOHUP.

The command syntax is easy:-

nohup <command>  &

here  <command> is the command or script you're running. An & is need to put the command in the background as nohup doesn't do this itself.

For example, when you log-in to the remote server using ssh.

\# ssh user@remoteserver

now you want to run a backup script rsync_script.sh  which takes a long time, then you can run,

\# nohup rsync_script.sh &

you can now logout from the terminal & the script will continue to run until its completed.

