---
layout: post
title: Steps to follow after Linux Server installation
date: '2013-12-11T18:17:00.000+05:30'
author: Balvinder Rawat
tags:
  - initial steps
  - linux installation
modified_time: '2013-12-11T18:17:51.769+05:30'
thumbnail: >-
  https://2.bp.blogspot.com/-YCJ4eEEdL3A/UqhND5h8e2I/AAAAAAAAAwk/m5Q44HcUfgs/s72-c/linux-server.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-7868308695725574731'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/steps-to-follow-after-linux-server-installation.html
---
[![](https://2.bp.blogspot.com/-YCJ4eEEdL3A/UqhND5h8e2I/AAAAAAAAAwk/m5Q44HcUfgs/s400/linux-server.png)][1]

The Basics
==========

* * *

When you first begin to access your fresh new server, there are a few early steps you should take to make it more secure. Some of the first tasks required on a linux server can include setting up a new user, providing them with the proper privileges, and configuring SSH.  
  

**Step One—Root Login**

* * *

Once you know your IP address and root password, login as the main user, root.  
  
It is not encouraged to use root on a linux server on a regular basis, and this tutorial will help you set up an alternative user to login with permanently.

_\# ssh root@123.45.67.890_

  
The terminal will show:

_The authenticity of host '69.55.55.20 (69.55.55.20)' can't be established._

_ECDSA key fingerprint is 79:95:46:1a:ab:37:11:8e:86:54:36:38:bb:3c:fa:c0._

_Are you sure you want to continue connecting (yes/no)?_

  
Go ahead and type yes, and then enter your root password.  
  
  

Step Two—Change Your Password
-----------------------------

* * *

Currently your root password is the default one that was sent to you when you registered your droplet. The first thing to do is change it to one of your choice.

_\# passwd_

**Step Three— Create a New User**

* * *

After you have logged in and changed your password, you will not need to login again as root. In this step we will make a new user and give them all of the root capabilities.  
  
You can choose any name for your user. Here I’ve suggested adminuser

_\# adduser **adminuser**_

  
After you set the password, you do not need to enter any further information about the new user. You can leave all the lines blank if you wish  
  

**Step Four— Root Privileges**

* * *

As of yet, only root has all of the administrative capabilities. We are going to give the new user the root privileges.  
  
When you perform any root tasks with the new user, you will need to use the phrase “sudo” before the command. This is a helpful command for 2 reasons: 

  

1) it prevents the user making any system-destroying mistakes 

2) it stores all the commands run with sudo to the file ‘/var/log/secure' which can be reviewed later if needed.  
  
Let’s go ahead and edit the sudo configuration. This can be done through the default editor, which in Ubuntu is called ‘nano’

_\# visudo_

  
Find the section called user privilege specification.  
  
It will look like this:

_\# User privilege specification_

_root    ALL=(ALL:ALL) ALL_

  
Under there, add the following line, granting all the permissions to your new user:

_**adminuser**    ALL=(ALL:ALL) ALL_

  
Type ‘cntrl x’ to exit the file.  
  
Press Y to save; press enter, and the file will save in the proper place.  
  

**Step Five— Configure SSH (OPTIONAL)**

* * *

Now it’s time to make the server more secure.**These steps are optional. Please keep in mind that changing the port and restricting root login may make logging in more difficult in the future.**If you misplace this information, it could be nearly impossible.  
  
Open the configuration file

_\# vim /etc/ssh/sshd_config_

  
Find the following sections and change the information where applicable:

_Port 25000_

_Protocol 2_

_PermitRootLogin no_

  
We’ll take these one by one.  
  
Port: Although port 22 is the default, you can change this to any number between 1025 and 65536. In this example, I am using port 25000. Make sure you make a note of the new port number. You will need it to log in in the future. This change will make it more difficult for unauthorized people to log in.  
  
PermitRootLogin: change this from yes to no to stop future root login. You will now only be logging on as the new user.  
  
Add these lines to the bottom of the document,_replacing \*adminuser\* in the AllowUsers line with your username. (AllowUsers will limit login to_**_only_**_the users on that line. To avoid this, skip this line)_:

_UseDNS no_

_AllowUsers **adminuser**_

  

  
Save and Exit

  

[1]: https://2.bp.blogspot.com/-YCJ4eEEdL3A/UqhND5h8e2I/AAAAAAAAAwk/m5Q44HcUfgs/s1600/linux-server.png

