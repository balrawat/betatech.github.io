---
layout: post
title: Setup VNC Server in Linux
date: '2013-10-28T12:21:00.000+05:30'
author: Balvinder Rawat
tags:
  - VNC
  - vncserver
  - remote vnc
modified_time: '2013-10-28T12:31:52.017+05:30'
thumbnail: >-
  https://1.bp.blogspot.com/-wZjMD6n9M7c/Um4L0GwsvII/AAAAAAAAAl0/DifpqNRZ2Go/s72-c/vnc1.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-4678944531279225185'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/10/setup-vnc-server-in-linux.html'
---
![](https://1.bp.blogspot.com/-wZjMD6n9M7c/Um4L0GwsvII/AAAAAAAAAl0/DifpqNRZ2Go/s320/vnc1.png)

This is how-to on setting up a VNC server on a Linux machine. 

Many times I've feel the need to VNC into the server & do the tasks. This is incredibly easy & can be done within few steps. We'll be setting up unencrypted VNC.

## Step 1: Installing Packages

There are a just a couple of packages to be dealt with. Those packages can be installed with a single command. Before you run the command, you must first "su" to root. This is done by entering the command _su _and then typing your root user password. Once you have root access, run the command:

`yum install vnc vnc-server`

Once the above command completes, you are ready to begin the configuration.

## Step 2: Configure Users

I will assume you already have either the users that will be allowed to VNC into the machine, or you only have one user that will be gaining access to the machine. Either way, the users will already have accounts on the server and will have logged in to confirm their passwords/accounts.

For each user that needs to gain access to the VNC server, you must set a VNC password for them. Let's say you've set up a user account called myvncuser and intend on logging in with only that user. To set the VNC password for the user, you must first _su_ to that user account. Issue the command:

_su myvncuser_

Now issue the command:

_vncpasswd_

You will then be prompted to enter (and confirm) the new password for the user. Once you've completed that action, you are done with user configuration.

## Step 3: Configure VNC

Now for the important pieces.The first phase of this step is to edit the` /etc/sysconfig/vncservers `file. At the end of that file, enter the following:

_VNCSERVERS="1:myvncuser"_

_VNCSERVERARGS\[1\]="-geometry 1600x1200"_

NOTE: You can set the geometry to whatever resolution you require.

In the above section, you can set up multiple users for connection. Say you had three users that needed access using different resolutions. To accomplish this, you could enter something like:

_VNCSERVERS="1:myvncuser1 2:myvncuser2 3:myvncuser3"_

_VNCSERVERARGS\[1\]="-geometry 1600x1200"_

_VNCSERVERARGS\[2\]="-geometry 800x600"_

_VNCSERVERARGS\[3\]="-geometry 640x480"_

## Step 4: Service Startup

Before you go any further, make sure the VNC server will start and stop cleanly. As the root user, issue the commands:

*   `service vncserver start`
*   `service vncserver stop`

If the VNC server started and stopped cleanly, set VNC up to start at boot with the command:

_chkconfig vncserver on_

## Step 5: Create xstartup scripts

You now need to go into each user that will be logging in with VNC and editing their`~/.vnc/xstartup` script. Within that script, you should find the following:


`#!/bin/sh`

```bash
\# Uncomment the following two lines for normal desktop:
```

```bash
\# unset SESSION_MANAGER
```

```bash
# exec /etc/X11/xinit/xinitrc
\[ -x /etc/vnc/xstartup \] && exec /etc/vnc/xstartup
```
`\[ -r $HOME/.Xresources \] && xrdb $HOME/.Xresources`

_xsetroot -solid grey_

_vncconfig -iconic &_

`xterm -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &`


_twm &_

Uncomment the following two lines (remove the "#" characters):

*   _unset SESSION_MANAGER_

*   `exec /etc/X11/xinit/xinitrc`

Save that file and you're ready to move on.

## Step 6: Edit Iptables

In order for the VNC connections to get through, you must allow them with iptables. To do this, open up the file` /etc/sysconfig/iptables` and add the line:

_-A INPUT -m state --state NEW -m tcp -p tcp -m multiport --dports 5901:5903,6001:6003 -j ACCEPT_

Save the file and restart iptables with the command:

`service iptables restart`


## Step 7: Start the VNC server

Issue the command:

`service vncserver start`

And the VNC server should start up nice and cleanly.

## Step 8: Test the connection

Move over to a machine that can display graphics (if your server does, you can test from there) and fire up your VNC client of choice and attempt to log in with the IP address of the server and port 5801.

There you go! You should now have a working VNC server on your Linux box

[1]: https://1.bp.blogspot.com/-wZjMD6n9M7c/Um4L0GwsvII/AAAAAAAAAl0/DifpqNRZ2Go/s1600/vnc1.png

