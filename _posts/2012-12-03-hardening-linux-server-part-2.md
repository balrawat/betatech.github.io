---
layout: post
title: Hardening the Linux server - Part 2
date: '2012-12-03T17:32:00.000+05:30'
author: Balvinder Rawat
tags:
  - security
  - hardening linux
  - installation
  - linux
modified_time: '2013-08-06T16:51:24.865+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-4677088127276784267'
blogger_orig_url: 'https://www.linuxtechtips.com/2012/12/hardening-linux-server-part-2.html'
---
[<< Part 1][1]                                                                                                     [Part 3 >>][2]

  

**Hardening the Linux server - Part 2**

  

  

  

**Plan the server installation**

  

The first step in hardening a GNU/Linux server is determining the server's function. What you use your server for determines what services need to be installed on the server. For example, if the server in question is used as a Web server, you should install LAMP services. On the other hand, if the server is used for directory services, Linux Apache MySQL PHP/Perl/Python (LAMP) has no business being installed on this machine. The only applications and services that should be permitted to run on your server are those that are required for the task the server is meant to perform. Nothing extra should be installed, for two reasons:

*   Installing extra software or running extra services means there is one more door you have to lock. For example, If you're running Lightweight Directory Access Protocol (LDAP) on a server for directory services, you need to make sure that both the operating system and LDAP are up to date with their security fixes and patches so that any known vulnerabilities are plugged. If LAMP were installed on this server, it would require updates and attention, even if it wasn't being used. Its mere existence on the server would provide an attacker another avenue into your system. Likewise, any other software installed on this server must be updated, patched, and monitored to make sure it doesn't provide a vulnerability that an attacker can exploit.
*   Installing extra software on a server means someone will be tempted to use that server for something other than its intended use. Not only does using the server for other tasks take resources away from it performing its main task, it exposes the server to threats it would not likely see without the software installed on it.

Among other things, you must decide whether to install a graphical user interface. For years, GNU/Linux admins have held a certain pride in being able to completely administer their networks and servers from a command-line interface. But in recent years, some system administrators have begun administering their GNU/Linux servers through a GUI. The choice to install a GUI such as the X Window System has sparked debate on various forums. On one hand, defenders of the command-line interface bring up the fact that the GUI can tax a system's resources and, because it's an extra service that isn't necessary, provide attackers with additional vulnerabilities. This side also points out that commands can be entered quickly through the command line without the need to search through menus and folders when performing a task.

On the other side of the debate, those who support a GUI environment argue that the GUI process can be killed when no longer in use to save resources and prevent any vulnerabilities from being exploited. They also argue that the GUI makes certain tasks, such as working with a database, much easier for the administrator.

  

**GUI login**

Some people who rely on a GUI like Gnome or KDE may be inclined to install a graphical login such as GDM. This isn't necessary because you can log in from the command-line interface just as easily as you would through a GUI-based login screen. The only difference is that you have to use the `sudo startx` command if you need to administer your server through a GUI.

  

  

  

Installing a GUI on your server is entirely a personal choice. Everything in this tutorial is done through the command line; but should you wish to install a GUI, the following instructions show you how to install Gnome as a desktop GUI:

  

1.  Once logged into your system, you should be at the command prompt. To install the Gnome core, type the following: `sudo aptitude install x-window-system-core gnome-core`
2.  Press **Enter**. You're asked for the sudo password. Type it, and then press **Enter** again. You're informed about what is being installed.
3.  To continue with the installation, type `Y` and then press **Enter**. Doing so installs a scaled-down version of Gnome that keeps the features of the desktop environment to a minimum and saves system resources. To install the full-featured version of Gnome, enter `sudo aptitude install x-window-system-core gnome`
4.  After you press **Enter**, you're asked to go through the same process as earlier. Follow along until Gnome is installed on your system.
5.  When either package is finished installing, you're still at the command prompt. To open Gnome, type the following: `sudo startx`

  

  

**Securing SSH**

SSH provides a user with a connection to a remote computer. As a replacement for Remote Shell (RSH) and Telnet, SSH is commonly used by system administrators to log in to their servers from a remote computer to perform maintenance and administrative tasks. Even though SSH provides a much greater level of security than the protocols that it replaced, you can do some things to make it more secure.

  

  

  

**Security by obscurity**

  

One of the most common methods for hardening SSH is to change the port number that is used to access it. The theory is that an attacker using the default port or TCP 22 to establish a connection will be denied access because the service is running on a secure port.

This method of securing SSH is the center of multiple forum debates. Changing the port number won't prevent the SSH port from being found by an attacker with a port scanner who takes the time to scan all of the ports on your server; and for this reason, many system administrators don't bother changing the port. But this approach does prevent script kiddies from attacking SSH with automated tools dedicated to finding open TCP 22 ports, and impatient attackers may grow weary of scanning your server if they don't find SSH running in the first range of ports they scan.

To change the SSH port address, you need to first install SSH on your server. Type

  

  

  

_\# **sudo aptitude install openssh-server**_

  
  

  

  

Press **Enter** and type your password. This command installs openssh to use for remote logins to your server.

  

Once you have an SSH file to configure, you should copy the file in case something happens when configuring. You can always revert back to the original. Follow these steps:

1.  At the command line, type `sudo cp /etc/ssh/sshd_config /ete/ssh/sshd_config.back`
2.  Press **Enter** and provide your password to complete the backup of this file.

**Install emacs**

To install emacs, use `sudo aptitude install emacs `Now, you need to locate the portion of the file where the port number is set. Once you've found this (the default is port 22), you can change it to an arbitrary number. There are more than 65,000 ports; choose something at the upper end of the scale, but a number you'll remember. Remember, skilled attackers know how people think. Changing the port number to 22222 or 22022 is a common mistakechoose a number that isn't easily guessed.

  

  

  

Now, you need to change the permissions for the sshd_config file so you can change it:

  

1.  Type `sudo chmod 644 /etc/ssh/sshd_config`
2.  Press **Enter**. Now you can use a text editor like emacs or vi to change the file: `emacs /etc/ssh/sshd_config`

Leave emacs or vi open as you make more changes to this file.

  

  

  

**Root login permissions**

  

The root user in all Ubuntu distributions is disabled, but you can activate this account. If you're using SSH, you should deny the root account permission to log in to the server remotely in the event that you or an attacker has activated this account. While you have the editor open, scroll down to the line that reads `PermitRootLogin`. The default is yes.

  

  

  

**Whitelist users**

  

Another step you can take to harden SSH on your server is to allow only certain users to use this service. This process is known as _whitelisting_. To create a whitelist, you first need the usernames of the people who will be allowed to use SSH to remotely access the server. Then, follow these steps

1.  Add this line to your sshd_config file: 

\# Allow only certain users

\# AllowUsers username username username

3.  There are many other ways to further secure SSH that are for more advanced users. When you've had more experience working with GNU/Linux and SSH, you should consider taking these steps.Substitute usernames from your list in place of the word _username_. Alternately, you can allow groups access to SSH logins by using `# Allow only certain groups AllowGroups group group `Again, substitute your user groups for the word _group_ in the example.

2.  Save your configuration file, and exit your editor. You need to restart SSH in order for the changes to take effect. You don't need to shut down your computer -- just type `sudo service ssh restart`
3.  Press **Enter** and provide your password. The service restarts and tells you `[OK]`.

  

[<< Part 1][3]                                                                                                                 [Part 3 >>][4]

[1]: http://www.linuxtechtips.com/2012/11/hardening-linux-server.html
[2]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-3.html
[3]: http://www.linuxtechtips.com/2012/11/hardening-linux-server.html
[4]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-3.html

