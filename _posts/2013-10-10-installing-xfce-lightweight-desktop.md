---
layout: post
title: Installing XFCE ( Lightweight Desktop Environment ) on Centos/RHEL 6
date: '2013-10-10T11:39:00.000+05:30'
author: Balvinder Rawat
tags:
  - xfce
  - desktop environment
modified_time: '2013-10-10T11:39:46.691+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-7588588058849243130'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/10/installing-xfce-lightweight-desktop.html'
---
  

**What is XFCE**

  

Xfce is a lightweight desktop environment for UNIX-like operating systems. It aims to be fast and low on system resources, while still being visually appealing and user friendly.

Xfce embodies the traditional UNIX philosophy of modularity and re-usability. It consists of a number of components that provide the full functionality one can expect of a modern desktop environment. They are packaged separately and you can pick among the available packages to create the optimal personal working environment.

Another priority of Xfce is adherence to standards, specifically those defined at [freedesktop.org][1].

Xfce can be installed on several UNIX platforms. It is known to compile on Linux, NetBSD, FreeBSD, OpenBSD, Solaris, Cygwin and MacOS X, on x86, PPC, Sparc, Alpha...

  

Features
--------

Xfce contains a number of core components for the minimum tasks you'd expect from a desktop environment:

Window Manager

Manages the placement of windows on the screen, provides window decorations and manages workspaces or virtual desktops.

Desktop Manager

Sets the background image and provides a root window menu, desktop icons or minimized icons and a windows list.

Panel

Switch between opened windows, launch applications, switch workspaces and menu plugins to browse applications or directories.

Session Manager

Controls the login and power management of the desktop and allows you to store multiple login sessions.

Application Finder

Shows the applications installed on your system in categories, so you can quickly find and launch them.

File Manager

Provides the basic file management features and unique utilities like the bulk renamer.

Setting Manager

Tools to control the various settings of the desktop like keyboard shortcuts, appearance, display settings etcetera.

Beside the basic set of modules, Xfce also provides numerous additional applications and plugins so you can extend your desktop the way you like, for example a terminal emulator, text editor, sound mixer, application finder, image viewer, iCal based calendar and a CD and DVD burning application. You can read more about the modules of Xfce in the [projects][2] page.

  

Installing on Centos/RHEL 6:-
-----------------------------

  

*   Make sure your machine can connect to the internet
*   Download and install the epel repo:-

_wget http://download.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm  
rpm -ivh epel-release-6.8.noarch.rpm_

  
*    install all the xfce packages
  

  
_yum groupinstall Xfce_

  

  
*   The following command install some fonts needed for the graphical login process in CentOS, if they are not present, you will see squares instead in the login screen.
  

  

_yum install xorg-x11-fonts-Type1 xorg-x11-fonts-misc_

  

  
*   Logout & login again by selecting "xfce-session" as session from login screen.
  

  
  

[1]: http://freedesktop.org/
[2]: http://www.xfce.org/projects

