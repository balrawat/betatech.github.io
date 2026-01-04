---
layout: post
title: Hardening the Linux server - Part 5
date: '2012-12-03T17:35:00.001+05:30'
author: Balvinder Rawat
tags:
  - security
  - encryption
  - hardening linux
  - linux
modified_time: '2013-08-06T16:49:29.774+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-3343288754572511245'
blogger_orig_url: 'https://www.linuxtechtips.com/2012/12/hardening-linux-server-part-5.html'
---
[<< Part 4][1]

  

**Hardening the Linux server - Part 5**

**Encryption**

_Encryption_ is the process of taking data stored on a computer and scrambling it in a manner that makes it unreadable to anyone who doesn't possess the key to re-create the data in its original form. Data that has been encrypted can be stored on the local computer, stored on a network share, or transmitted to other users and computers.

It's possible to encrypt an entire hard disk or the partitions of the disk. This should be done at installation. You can also secure data through encryption by creating a directory and encrypting it. For example, if you've set up a file server, you may want to encrypt a directory that holds sensitive information.

Before you go forward with protecting your data, you need to install eCryptfs from the Ubuntu repositories by typing

  

**_# sudo aptitude install ecryptfs-utils_**

Press **Enter**, and type your root password.

  

**Encrypt a directory**

The next step is to create a directory to encrypt. The example uses a directory called secure, but you can name it anything you wish. Follow these steps:

1.  Enter the following command:

1.  **_\# mkdir ~/secure_**

3.  Just to keep others from snooping around, change the permissions to 700:

1.  **_# chmod 700 ~/secure_**

4.   Mount the new directory with the eCryptfs file system:

1.  **\# _sudo mount -t ecryptfs  ~/secure ~/secure_**

6.  You're asked a series of questions. Be sure you remember the answers, because you'll need them when you remount. The first question asks which type of key you'd like to use. Make your selection by typing the number that corresponds to your choice. Next, select the cipher you wish to use and the size of the key.
7.  Once you've answered all the questions, your directory is ready to add files and other subdirectories to. When you're ready to secure your directory, unmount it with 

1.  **_# sudo unmount ~/secure_**

  

  

**Additional security steps**

Now that you've created a solid foundation for hardening your server, you should take a few steps to further enhance the security measures you've put into place. These last few tips introduce some of the extra points to keep in mind when hardening your GNU/Linux server.

  

  

  

**Updates**

A production server should never have updates and patches installed unless they were first tested on a test, or development, server. Because a GUI may not be installed on your server, you have to download any updates and patches through the terminal. When you're ready to install updates, enter the command `sudo apt-get update` and then `sudo apt-get dist-upgrade`. In some cases, you need to restart your server.

  

  

  

**Malware**

Many system administrators find installing antivirus software on a server running GNU/Linux to be a waste of resources because no viruses in the wild can attack the GNU/Linux operating system. But any GNU/Linux administrator who is running SAMBA to share Windows files should definitely make sure an antivirus scanner like ClamAV is installed to make sure infected files don't spread throughout your system.

Although viruses don't pose as much of a threat to the GNU/Linux server, rootkits can cause you a headache. _Rootkits_ are tools that attackers use to gain root-level permissions to a system, capture passwords, intercept traffic, and create other vulnerabilities. To combat this threat, you should install tools such as RKHunter and chkrootkit on the server.

  

  

  

**Backup and recovery**

Servers that house gigabytes of information, corporate Web sites, or catalogs for directory services need to have a backup and recovery strategy in place. Most corporate networks can afford redundancy through multiple servers, and smaller networks can find peace of mind through virtualization and back-up and recovery software.

If you're planning to run backup and recovery software from the Ubuntu repositories, Sbackup is an excellent choice because it can be run from either the command line or a GUI. When backing up server data on a corporate network, it's important that your backup files be stored outside the server. Portable storage devices provide large amounts of storage space at extremely reasonable prices, and they're excellent options for storing backed-up files and directories.

  

  

  

**Passwords**

As the system administrator, you're required to set passwords for your server's root account and possibly other sensitive accounts in your organization such as MySQL databases or FTP connections. You can't force strong passwords for your users with Ubuntu Server, but you can be sure you train users on how to create a strong password.

  

**Network password policy**

  

If you're running directory services like OpenLDAP, you have the option to enforce strong passwords across your network with some of the configuration options available.

  

  

  

Make sure your users' passwords contain at least three of the following: an uppercase letter, a lowercase letter, a number, or a symbol. To further strengthen the password, make it a policy that all passwords are at least eight characters long.

One way to teach users to use strong passwords but keep them from writing down complex passwords on sticky notes is to have them use passphrases. Something like Myf@voritecolorisBlue! is much easier to remember than M$iuR78$, and both meet minimal complexity standards.

  

  

  

[<< Part 4][2]

  

[1]: https://www.linuxtechtips.com/2012/12/hardening-linux-server-part-4.html
[2]: https://www.linuxtechtips.com/2012/12/hardening-linux-server-part-4.html

