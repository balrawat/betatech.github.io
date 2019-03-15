---
layout: post
title: Hardening the Linux server - Part 3
date: '2012-12-03T17:32:00.004+05:30'
author: Balvinder Rawat
tags:
  - firewall
  - security
  - hardening linux
  - linux
modified_time: '2013-08-06T16:50:24.855+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-2110279984730669968'
blogger_orig_url: 'https://www.linuxtechtips.com/2012/12/hardening-linux-server-part-3.html'
---
[<< Part 2][1]                                                                                                    [Part 4 >>][2]

**Hardening the Linux server - Part 3**

  

  

  

**Write firewall rules**

You can deny access to your server through your firewall. Ubuntu Server uses a firewall called Uncomplicated FireWall (UFW), which is actually a management tool for iptables. Iptables filters network packets based on a series of rules written by the system administrator. Iptables can be complicated for beginners, so UFW simplifies it. Using UFW can help you harden your server; but if you're truly interested in server security, learning how to write rules for iptables will let you fine-tune a server's security.

To get started with UFW, you need to install it. Follow these steps:

1.  From the command line, type sudo aptitude install ufw
2.  Press **Enter** and enter your password. Press **Enter** again to install the package.
3.  To enable the firewall, type the following: sudo ufw enable
4.  Press **Enter**. You see the message Firewall started and enabled on system startup. Now you can create rules for your firewall.

Remember how you changed the port for SSH earlier? To open the port through UFW by creating a rule, type the following at the command line:

**_# sudo ufw allow 65000_**

That command allows access over port 65000 and lets SSH traffic into your server.

To deny access over this port, use the following:

**_\# sudo ufw deny 65000_**

To allow or deny traffic specifically on TCP port 65000, use the following command:

**_# sudo ufw allow 65000/tcp_**

You can also allow or deny traffic according by the protocol it uses. For instance, to block all HTTP traffic, you can use this command:

**_# sudo ufw deny http_**

You can create more complicated rules to deny or allow a service based on its IP address. For instance, if your desktop had the IP address 192.168.1.30 and your server had an IP address of 192.168.1.5, you could allow only your computer's IP address the ability to establish an SSH connection:

**_# sudo ufw allow proto tcp from 192.168.1.30 to 192.1681.5 port 65000_**

To check which rules you're currently running with UFW, use

**_# sudo ufw status_**

You're presented with a list of rules you've written for your firewall. If you see a rule that you wish to delete, type

**_# sudo delete \[rule\]_**

  

[<< Part 2  ][3]                                                                                                              [ Part 4 >>][4]

  

[1]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-2.html
[2]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-4.html
[3]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-2.html
[4]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-4.html

