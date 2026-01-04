---
layout: post
title: Bash History without numbers...
date: '2012-12-07T20:53:00.005+05:30'
author: Balvinder Rawat
tags:
  - linux
  - bash history
  - linux commands
modified_time: '2013-03-13T12:15:51.529+05:30'
thumbnail: >-
  https://1.bp.blogspot.com/-FBD-1ESpJ-8/UMIJAKSMVsI/AAAAAAAAAKY/L9YTeh5vyP0/s72-c/bash1.PNG
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-1546345626668257916'
blogger_orig_url: 'https://www.linuxtechtips.com/2012/12/bash-history-without-numbers.html'
---
The bash _**history**_ command is very cool. I understand why it shows the line numbers, but sometimes we need only the commands & not the numbers e.g. when we need to copy & run the commands to another server or terminal then it gets quiet useful. When you run **_history_** , the output is similar to this:  

  
  
  
[![](https://1.bp.blogspot.com/-FBD-1ESpJ-8/UMIJAKSMVsI/AAAAAAAAAKY/L9YTeh5vyP0/s320/bash1.PNG)][1]  
  
  
  
  
  
  
  
  
  
  
  
  
Now try running **_history | cut -c 8-_** , you'll get the this:  
  
  

[![](https://3.bp.blogspot.com/-g-ZMZ_qafxI/UMIJATClpnI/AAAAAAAAAKk/KxNBF58rI4s/s320/bash2.PNG)][2]  
  
  
  
  
  
  
  
  
  
  
  
  
So this command is really useful in situations where you need to do repeated work on same or different servers & you don't have scripting knowledge. You can just copy & paste the commands.   
  
_Hope you enjoy reading this!_

[1]: https://1.bp.blogspot.com/-FBD-1ESpJ-8/UMIJAKSMVsI/AAAAAAAAAKY/L9YTeh5vyP0/s1600/bash1.PNG
[2]: https://3.bp.blogspot.com/-g-ZMZ_qafxI/UMIJATClpnI/AAAAAAAAAKk/KxNBF58rI4s/s1600/bash2.PNG

