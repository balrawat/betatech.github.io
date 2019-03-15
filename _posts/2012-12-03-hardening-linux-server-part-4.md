---
layout: post
title: Hardening the Linux server - Part 4
date: '2012-12-03T17:34:00.003+05:30'
author: Balvinder Rawat
tags:
  - security
  - encryption
  - hardening linux
  - linux
  - monitoring
modified_time: '2013-08-06T16:48:52.336+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-2971124724154376978'
blogger_orig_url: 'https://www.linuxtechtips.com/2012/12/hardening-linux-server-part-4.html'
---
[<< Part 3][1]                                                                                 [Part 5 >>][2]

**Hardening the Linux server - Part 4**
---------------------------------------

**Monitor your system**
-----------------------

There is a saying in computer security circles that the only way to truly secure a computer is to completely disconnect it and lock it in a box. Not too practical, but the underlying message is that if an attacker really wants into a system, odds are they will find a way in. After you take steps toward intrusion prevention, you need to set up a monitoring system to detect whether an attack against your server has taken place. Then, if you're alerted to an attack, you're better prepared to deal with it early on.

The following sections walk you through the steps of installing and configuring two programs that help to detect intrusions. Tripwire alerts you to unauthorized activity that takes place with system files on your server, and Logwatch is a tool that can be used to create reports for you to analyze.

  

  

**Tripwire**

  

  

  

Tripwire is a program that sets up a baseline of normal system binaries for your computer. It then reports any anomalies against this baseline through an e-mail alert or through a log. Essentially, if the system binaries have changed, you'll know about it. If a legitimate installation causes such a change, no problem. But if the binaries are altered as a result of a Trojan horse or rootkit being installed, you have a starting point from which to research the attack and fix the problems.

To install and configure Tripwire through the command line, follow these steps:

1.  Enter the following command:

1.  **_\# sudo aptitude install tripwire_**

2.  You can run the database initialization by typing Press **Enter** and type your password, and Tripwire downloads and installs.
3.  This screen informs users of Debian-based systems about a potential scenario in which an attacker could obtain the passphrase used with Tripwire while it's unencrypted. Advanced users may opt to stop here and create the site key and configuration files on their own. Beginners should select **OK** and move forward.
4.  The next screen asks if you wish to create your passphrase during installation. Select **Yes**, and press **Enter**.
5.  The next screen informs you about how Tripwire works. The program creates a text file that stores an encrypted database of the systems configuration. This text file is the baseline. If any changes are made to the system configuration, Tripwire sees the change and creates an alert. In order for you to make legitimate changes to the system, you create a passphrase. Select **Yes** and press **Enter** to begin building the configuration file.
6.  The following screen explains the same thing, but this time you're building the Tripwire policy file. Again, select **Yes** and press **Enter**.
7.  Once the files are built, you're prompted to enter the site-key passphrase. You need to remember this passphrase. Select **OK**, and then press **Enter**. You're prompted to enter your passphrase again on the next screen.
8.  You're brought to the local passphrase screen. This passphrase is required for the local files on the server. Enter your local passphrase, select **OK**, and then press **Enter**. You need to re-enter this passphrase again as well.
9.  Now that Tripwire has been installed, you're told the location of the database and the binaries. With **OK** selected, press **Enter** again to complete the configuration process.

  

**_# sudo tripwire --init_**

Press **Enter**. You're asked to provide the local passphrase you created during the Tripwire installation. Provide the passphrase and again press **Enter**. Now, Tripwire has created the baseline snapshot of your file system. This baseline will be used to check for changes to critical files. If such a change is detected, an alert will be sent.

You can check run an integrity check at any time by following these steps:

1.  Type

1.  **_\# sudo tripwire --check _**

2.  Press **Enter**. You're provided with a report that is saved in the reports directory. To view this report, use the twprint command:

1.  **_\# sudo twprint --print-report -r\ _**

4.  Press **Enter**, and type the sudo password. You're given a different type of prompt that looks like this:

1.  **_\#    >_**

6.  At this prompt, type the location and filename of the report you wish to print:

1.  **_# \> /var/lib/tripwire/report/<server name>-YYYYMMDD-HHMMSS.twr| less_**

7.  As your skills advance, you can look to twadmin to further fine-tune the capabilities of Tripwire. You can also set a cron job to e-mail you a copy of this report each day or configure Tripwire to e-mail you if an anomaly is reported.
    
    If you don't know the exact time you ran your report, navigate to the directory /var/lib/tripwire/reports to see the complete filename.
    

  

**Logwatch**

  

Logwatch is a great tool for monitoring your system's log files. This program requires a working mail server on your network to e-mail the logs to you. If you wish to change the .conf file, you need to open /usr/share/logwatch/default.conf/logwatch.conf and look for the line that reads MailTo. Change user.name.domain.tld to your e-mail address.

You can install Logwatch with this command:

  

**_# sudo aptitude install logwatch_**

To e-mail the logs to yourself, type

  

**_# logwatch --mailto email@youraddress.com --range All_**

Pressing **Enter** sends a copy of the report to the e-mail address specified. If you aren't running a mail server on your network but would still like to see a Logwatch report, the following command provides it on your screen:

  

**_# logwatch --range All --archives --detail Med_**

The output spans several screens; press **Shift-Page Up** to move to the beginning of the report.

  

**Users and groups**

GNU/Linux handles groups and permissions differently than the Microsoft® Windows® operating system does. You can organize users into groups for easy administration, but you also need to provide access to files and folders through permissions. No blanket "power user" gives users access to almost everything on a computer or network. The GNU/Linux system was designed to be more secure; it works off a _3x3_ system for granting permissions:

  

**Don't run as root**

Anyone who knows anything about GNU/Linux security will tell you never, never, never to run anything as the root user. Logging in as administrator in a Windows network is common, but doing so is discouraged in the GNU/Linux community. This is why whenever you need to run something as root, you use the sudo command. Any system administrator can use the sudo command if you give them the password. To see how and when the sudo password is being used, check out /var/log/messages. Because you're looking for all uses of sudo, use the `grep` command to find them.

*   **File permissions** \-\- Read (r), write (w), and execute (x). Each of these permissions is also given a number: read = 4, write = 2, and execute = 1.
*   **Directory-level permissions** \-\- Enter, which gives permission to enter the directory; show, which gives permission to see the contents of the directory; and write, which gives permission to create a new file or subdirectory.
*   **How permissions are assigned** \-\- Permissions are assigned in three ways: by user level, group level, and other level. The user level defines the user who created the file or directory, the group level defines the group the user is in, and the other level is for any user outside of the user's group.

The user permissions are granted first: for example, r/w/x means the user can read, write, and execute the file or files in the folder. You can apply the number value to each permission. Thus if a user can read, write, and execute, you add the corresponding numbers 4, 2, and 1, for a total of 7. Next come the group permissions. For instance, the other members of the user's group may be able to read and execute, but not write. Adding up the corresponding values gives you 5. Those in the others category can only read the files, so their numerical value is 4. Thus, the permissions for the file or folder are 754.

When permissions are set to 777, everyone is given the ability to read write and execute. The `chmod` command changes permissions for files and directories. If you wish to change ownership of a user, use the `chown` command. To change group ownership of a file or directory, use the `chgrp` command.

  

  

  

[<< Part 3     ][3]                                                                                                            [Part 5 >>][4]

  

[1]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-3.html
[2]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-5.html
[3]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-3.html
[4]: http://www.linuxtechtips.com/2012/12/hardening-linux-server-part-5.html

