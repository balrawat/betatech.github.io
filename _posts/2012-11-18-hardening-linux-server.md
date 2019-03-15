---
layout: post
title: Hardening the Linux server - Part 1
date: '2012-11-18T13:36:00.000+05:30'
author: Balvinder Rawat
tags:
  - security
  - hardening linux
  - linux
modified_time: '2013-08-06T16:54:57.872+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-5649246183215613968'
blogger_orig_url: 'https://www.linuxtechtips.com/2012/11/hardening-linux-server.html'
---
[Part 2 >>][1]

  

**Hardening the Linux server - Part 1**

_An introduction to GNU/Linux server security_

  

**Summary:**  Servers—whether used for testing or production—are primary targets for attackers. By taking the proper steps, you can turn a vulnerable box into a hardened server and help thwart outside attackers. Learn how to secure SSH sessions, configure firewall rules, and set up intrusion detection to alert you to any possible attacks on your GNU/Linux® server. Once you've gained a solid foundation in the basics of securing your server, you can build on this knowledge to further harden your systems.

  

**Objectives**

In this tutorial, you learn about basic concepts in security administration, including how to secure Secure Shell (SSH) remote logins, create firewall rules, and watch logs for possible attacks.

  

**System requirements**

To run the examples in this tutorial, you need to install [Ubuntu Server Edition][2] on a computer or a virtual machine, such as [Sun VirtualBox][3]. You also need an Internet connection to download specific software packages used in the tutorial.

  

  

**Introduction**

To understand the basics of hardening a server running GNU/Linux as the operating system, you need to be aware that although many core _concepts_of security apply to both the desktop operating system and the server operating system, the _ways_ they're secured are completely different.

  

**The Principle of Least Privilege**

A truly secure network makes sure that the Principle of Least Privilege is applied across the enterprise, not just to the servers. The roles taken on by servers and desktops also mandate how the operating system, and the computer itself, should be secured. The desktop may be an attractive target for a script kiddie whose attacks are often thwarted by updated software and malware scanners, but a data center hosting user accounts or credit-card information is a much more attractive target for the skilled attacker who can exploit weaknesses without detection in an environment that hasn't been hardened.

  

  

  

Securing a server is much different than securing a desktop computer for a variety of reasons. By default, a desktop operating system is installed to provide the user with an environment that can be run out of the box. Desktop operating systems are sold on the premise that they require minimal configuration and come loaded with as many applications as possible to get the user up and running. Conversely, a server's operating system should abide by the Principle of Least Privilege, which states that it should have only the services, software, and permissions necessary to perform the tasks it's responsible for.

  

  

**Revisiting the immutable laws of security**

In November 2000, Scott Culp of Microsoft drafted what he called the _10 Immutable Laws of Security_. There are two versions of these laws: one for users and one for system administrators. Over the years, these laws have been both revised and despised by people in the security industry. Despite some criticism, the 10 laws for administrators can serve as an excellent foundation for hardening any system if applied correctly.

First, the following law applies to general security practices: Security only works if the secure way also happens to be the easy way. This is the most important law for any system administrator. If a security policy is so tight that people can't perform their job tasks, they're going to find ways to circumvent the security put in place, sometimes creating a greater vulnerability than the policy was put in place to prevent. The best example relates to passwords. Strong passwords should be part of any security policy, but sometimes policies go too far. Requiring users to remember a password that is 15 characters long and that consists of uppercase letters, lowercase letters, numbers, and symbols is asking for a high percentage of users to write their password on a post-it note and attach it to their monitor.

Four of Culp's laws apply directly to the material covered in this tutorial:

*   **If you don't keep up with security fixes, your network won't be yours for long.** Attackers find vulnerabilities every day. As a system administrator. you need to make sure your system is updated. But this brings you to a difference between hardening a desktop and hardening a server. Generally, updates to the GNU/Linux desktop should be installed when they're published. When you're dealing with the server, you should test it in a research or development server environment before applying the fix to your production server, to make sure the patch doesn't interfere with the operations of the server or the users.
*   **Eternal vigilance is the price of security.** In an effort to make sure your GNU/Linux server is secured, you must constantly check logs, apply security patches, and follow up on alerts. Vigilance is what keeps your system secure.
*   **Security isn't about risk avoidance; it's about risk management.** Things happen. There may be a malware outbreak, or your Web site may be attacked. It may be something completely out of your control, such as a natural disaster. At one time or another, the security of your system will be tested. Make sure you've done everything you can to protect your system, and deal with the threat in a way that keeps your server and its resources available to the users who count on it.
*   **Technology isn't a panacea.** If there is one law that everyone who deals with technology should know, it's this one. Simply throwing more technology at the security problem won't solve it. Vigilance on the part of the system administrator, buy-in on the part of management, and acceptance on the part of users must all be in place for a security policy to work effectively.

[Part 2 >>][4]

[1]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-2.html
[2]: http://www.ubuntu.com/getubuntu/download
[3]: http://www.virtualbox.org/
[4]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-2.html

