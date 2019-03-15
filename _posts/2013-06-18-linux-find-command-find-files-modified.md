---
layout: post
title: 'Linux Find Command: Find Files Modified On Specific Date'
date: '2013-06-18T14:24:00.001+05:30'
author: Balvinder Rawat
tags:
  - linux commands
modified_time: '2013-08-06T16:34:30.111+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-1626449491380433481'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/06/linux-find-command-find-files-modified.html
---
  
There are many situations in which we have to find out all files that have been modified on a specific date using find command under Linux.  
  
  
There are two ways to list files in given directory modified after given date of the current year. The latest version of GNU/find command use the following syntax:  
  
  

Syntax
------

GNU/find latest version:  
find /path/to/dir -newermt "date"  
find /path/to/dir -newermt "May 13"  
find /path/to/dir -newermt "yyyy-mm-dd"  
\## List all files modified on given date  
find /path/to/dir -newermt yyyy-mm-dd ! -newermt yyyy-mm-dd -ls  
\### print all *.sh ###  
find /path/to/dir -newermt "yyyy-mm-dd" -print -type f -iname "*.sh"

**The other way of doing this works on the versions of find before v4.3.3:**

touch -t 02010000 /tmp/timestamp  
find /usr -newer /tmp/timestamp

then we can remove the reference file:  
rm -f /tmp/stamp$$

  

To **find out all Shell Script files** (*.sh) in /home/linux/scripts that have been modified on 2013-05-01 (01/May/2013), enter:

find $HOME/scriptss -type f -name "*.sh" -newermt 2013-05-01 ! -newermt 2013-05-02 -print

Pass the -ls option to get **detailed file listing**:

find $HOME/scriptss -type f -name "*.sh" -newermt 2013-05-01 ! -newermt 2013-05-02 -ls

