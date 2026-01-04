---
layout: post
title: Change Timezone in Linux in different ways
date: '2013-12-05T11:08:00.002+05:30'
author: Balvinder Rawat
tags:
  - timezone
  - set timezone in linux
modified_time: '2013-12-06T11:51:49.804+05:30'
thumbnail: >-
  https://2.bp.blogspot.com/-F0NMVHr_ZcA/UqARQNuwSxI/AAAAAAAAAvY/M1FEGXrVXd8/s72-c/timezone.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-8736389288405661849'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/change-timezone-in-linux-in-different.html
---
![](https://2.bp.blogspot.com/-F0NMVHr_ZcA/UqARQNuwSxI/AAAAAAAAAvY/M1FEGXrVXd8/s640/timezone.png)

There is some instance during the Linux installation that you did not bother to set the correct timezone for any reasons like sometimes you are just lazy to set it, you’re in a rush to finish what your boss want you to complete in that day, or you just don’t give a damn![:)](file:///C:\DOCUME~1\balwinsi\LOCALS~1\Temp\msohtmlclip1\01\clip_image001.gif)Seriously, timezone is a bit important especially if you have scheduled scripts that you intended to run.

Here are some ways to change your timezone depending on your Linux distribution:

for RHEL/CENTOS:

Assuming you have the default or current timezone as UTC and you would like to change it to Singapore timezone

\[root@linuxtechtips etc\]# ## date

Thu Sep 6 23:15:06 UTC 2012 

\[root@linuxtechtips etc\]# ## rm /etc/localtime

Note: All timezones can be found under the directory## /usr/share/zoneinfo

Link the Singapore file under the Asia to the /etc/localtime

#cd /etc

#ln -s /usr/share/zoneinfo/Asia/Singapore localtime

#date

Fri Sep 7 07:17:20 SGT 2012 

This localtime symbolic links can be overwritten when you execute tzdata-update which will based from /etc/sysconfig/clock settings configured

Example:

current date in Singapore time, you execute the tzdata-update, it will read the /etc/sysconfig/clock file

\[root@linuxtechtips etc\]# ## cat /etc/sysconfig/clock

ZONE="Asia/Seoul"

UTC=true

ARC=false

\[root@linuxtechtips etc\]# date

Fri Sep 7 07:26:12 SGT 2012

\[root@linuxtechtips etc\]# ## tzdata-update

\[root@linuxtechtips etc\]# date

Fri Sep 7 08:26:20 KST 2012

For Ubuntu/Debian, the above method will also work. But it also has some commands to make you life easier, see items 1 & 2

1\. A simple way to change your timezone is using the “tzconfig” command which will prompt you with a list of region and cities. It will a simple way to update the link /etc/localtime to point to the correct timezone in /usr/share/zoneinfo

\[root@linuxtechtips etc\]# ## tzconfig

2.Another way is using the command “dpkg-reconfigure tzdata”. It will be a menu-based type of configuration screen.

\[root@linuxtechtips etc\]# ## dpkg-reconfigure tzdata

3\. Another method which will work with other distribution as well is via the TZ environment variable

\[root@linuxtechtips ~\]# date

Fri Sep 7 07:46:09 SGT 2012

\[root@linuxtechtips ~\]# ## export TZ=Asia/Manila

\[root@linuxtechtips ~\]# date

Fri Sep 7 07:46:30 PHT 2012 

4\. Another way is via “tzselect” command

\[root@linuxtechtips ~\]# ## tzselect

[1]: https://2.bp.blogspot.com/-F0NMVHr_ZcA/UqARQNuwSxI/AAAAAAAAAvY/M1FEGXrVXd8/s1600/timezone.png

