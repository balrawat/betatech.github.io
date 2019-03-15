---
layout: post
title: How To Protect SSH with fail2ban on Linux Machines
date: '2013-12-11T16:29:00.000+05:30'
author: Balvinder Rawat
tags:
  - brute force protection
  - iptables
  - fail2ban
modified_time: '2014-01-07T12:45:52.025+05:30'
thumbnail: >-
  http://2.bp.blogspot.com/-6zPfAFP2WgI/UqhFCHqS6BI/AAAAAAAAAwM/Mtf7Oz4ELjc/s72-c/fail2ban.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-3690195495586961123'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/how-to-protect-ssh-with-fail2ban-on-linux.html
---
[![](http://2.bp.blogspot.com/-6zPfAFP2WgI/UqhFCHqS6BI/AAAAAAAAAwM/Mtf7Oz4ELjc/s400/fail2ban.png)][1]

**About Fail2Ban**

Servers do not exist in isolation and those linux servers with only the most basic SSH configuration can be vulnerable to brute force attacks. fail2ban provides a way to automatically protect linux servers from malicious behavior. The program works by scanning through log files and reacting to offending actions such as repeated failed login attempts.

  

  

Step One—Install Fail2Ban
-------------------------

* * *

On ubuntu/Debian

_\# apt-get install fail2ban_

On RHEL/Centos

We need [epel repo][2]to install fail2ban on RHEL/Centos based machines.

So, download the rpm:-

_\# wget [http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm][3]_

and, then install fail2ban

_\# yum install fail2ban_

  

  

  

  

Step Two—Copy the Configuration File
------------------------------------

* * *

The default fail2ban configuration file is location at /etc/fail2ban/jail.conf. The configuration work should not be done in that file, however, and we should instead make a local copy of it.

_\# cp /etc/fail2ban/jail.conf /etc/fail2ban/jail.local_

  

  

After the file is copied, you can make all of your changes within the new jail.local file. Many of possible services that may need protection are in the file already. Each is located in its own section, configured and turned off.

  

  

  

  

Step Three—Configure the Defaults in Jail.Local
-----------------------------------------------

* * *

Open up the the new fail2ban configuration file:

_\# vim /etc/fail2ban/jail.local_

  

  

The first section of defaults covers the basic rules that fail2ban will follow. If you want to set up more nuanced protection on your virtual server, you can customize the details in each section.

  

  

You can see the default section below.

  

_\[DEFAULT\]_

_\# "ignoreip" can be an IP address, a CIDR mask or a DNS host_

_ignoreip = 127.0.0.1/8_

_bantime  = 600_

_maxretry = 3_

_\# "backend" specifies the backend used to get files modification. Available_

_\# options are "gamin", "polling" and "auto"._

_\# yoh: For some reason Debian shipped python-gamin didn't work as expected_

_#      This issue left ToDo, so polling is default backend for now_

_backend = auto_

_#_

_\# Destination email address used solely for the interpolations in_

_\# jail.{conf,local} configuration files._

destemail = root@localhost

Write your personal IP address into the**ignoreip**line. You can separate each address with a space. IgnoreIP allows you white list certain IP addresses and make sure that they are not locked out. Including your address will guarantee that you do not accidentally ban yourself from your own server.

  

  

  

The next step is to decide on a**bantime**, the number of seconds that a host would be blocked from the VPS if they are found to be in violation of any of the rules. This is especially useful in the case of bots, that once banned, will simply move on to the next target. The default is set for 10 minutes—you may raise this to an hour (or higher) if you like.

  

**

**Maxretry**is the amount of incorrect login attempts that a host may have before they get banned for the length of the ban time.

**

  

You can leave the**backend**as auto.

  

**

**Destemail**is the email that alerts get sent to. If you have a mail server set up on your droplet, Fail2Ban can email you when it bans an IP address.

**

  

  

  

### Additional Details—Actions

The Actions section is located below the defaults. The beginning looks like this:

_#_

_\# ACTIONS_

_#_

_\# Default banning action (e.g. iptables, iptables-new,_

_\# iptables-multiport, shorewall, etc) It is used to define_

_\# action_* variables. Can be overridden globally or per_

_\# section within jail.local file_

_banaction = iptables-multiport_

_\# email action. Since 0.8.1 upstream fail2ban uses sendmail_

_\# MTA for the mailing. Change mta configuration parameter to mail_

_\# if you want to revert to conventional 'mail'._

_mta = sendmail_

_\# Default protocol_

_protocol = tcp_

_\[...\]_

  

  

**Banaction**describes the steps that fail2ban will take to ban a matching IP address. This is a shorter version of the file extension where the config if is located. The default ban action, "iptables-multiport", can be found at /etc/fail2ban/action.d/iptables-multiport.conf

  

  

****MTA**refers to email program that fail2ban will use to send emails to call attention to a malicious IP.**

  

You can change the**protocol**from TCP to UDP in this line as well, depending on which one you want fail2ban to monitor.

  

  

  

Step Four (Optional)—Configure the ssh-iptables Section in Jail.Local
---------------------------------------------------------------------

* * *

The SSH details section is just a little further down in the config, and it is already set up and turned on. Although you should not be required to make to make any changes within this section, you can find the details about each line below.

_\[ssh\]_

_enabled  = true_

_port     = ssh_

_filter   = sshd_

_logpath  = /var/log/auth.log_

_maxretry = 6_

  

  

**Enabled**simply refers to the fact that SSH protection is on. You can turn it off with the word "false".

  

  

The**port**designates the port that fail2ban monitors. If you have set up your virtual private server on a non-standard port, change the port to match the one you are using:

  

 eg. _port=30000_

  

  

The**filter**, set by default to sshd, refers to the config file containing the rules that fail2ban uses to find matches. sshd refers to the /etc/fail2ban/filter.d/sshd.conf.

  

  

****log path**refers to the log location that fail2ban will track.**

  

The**max retry**line within the SSH section has the same definition as the default option. However, if you have enabled multiple services and want to have specific values for each one, you can set the new max retry amount for SSH here.

  

  

  

Step Five—Restart Fail2Ban
--------------------------

* * *

After making any changes to the fail2ban config, always be sure to restart Fail2Ban:

_\# service fail2ban restart_

Make sure it starts automatically with each boot:

chkconfig fail2ban on

  

  

You can see the rules that fail2ban puts in effect within the IP table:

  

_\# iptables -L_

  

  

[1]: http://2.bp.blogspot.com/-6zPfAFP2WgI/UqhFCHqS6BI/AAAAAAAAAwM/Mtf7Oz4ELjc/s1600/fail2ban.png
[2]: http://www.linuxtechtips.com/2012/11/installing-rhel-epel-repo-on-centos-5x.html
[3]: http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm

