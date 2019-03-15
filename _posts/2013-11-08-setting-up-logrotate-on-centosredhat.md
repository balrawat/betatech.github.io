---
layout: post
title: Setting Up Logrotate on Centos/RedHat Linux
date: '2013-11-08T11:43:00.000+05:30'
author: Balvinder Rawat
tags:
  - log
  - logrotate
modified_time: '2013-11-08T12:05:40.897+05:30'
thumbnail: >-
  http://2.bp.blogspot.com/-oxZJUs_4KkI/UnyAyly5xmI/AAAAAAAAAnE/DDmetiQHuCg/s72-c/log-rotate.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-3754462719174747917'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/11/setting-up-logrotate-on-centosredhat.html
---
[![](http://2.bp.blogspot.com/-oxZJUs_4KkI/UnyAyly5xmI/AAAAAAAAAnE/DDmetiQHuCg/s1600/log-rotate.png)][1]

**1. Introduction**

Logrotate is a utility designed for administrators who manage servers producing a high volume of log files to help them save some disk space as well as to avoid a potential risk making a system unresponsive due to the lack of disk space. Normally, a solution to avoid this kind of problem is to setup a separate partition or logical volume for a /var mount point. However, logrotate may also be a viable solution to this problem especially if it is too late to move all logs under different partition. In this article we will talk about usage and configuration of logrotate on RedHat / CentOS Linux server.

**2. What is Logrotate**

Logrotate provides an ability for a system administrator to systematically rotate and archive any log files produced by the system and thus reducing a operating system's disk space requirement. By default logrotate is invoked once a day using a cron scheduler from location /etc/cron.daily/

\# ls /etc/cron.daily/

  

cups **logrotate**  makewhatis.cron  mlocate.cron  prelink  readahead.cron  rhsmd  tmpwatch

**3. Configuring Logrotate**

Logrotate's configuration is done by editing two separate configuration files:

· /etc/logrotate.conf

· service specific configuration files stored in /etc/logrotate.d/.

The main logrotate.conf file contains a generic configuration. Here is a default logrotate configuration file logrotate.conf:

     1  weekly

     2  rotate 4

     3  create

     4  dateext

     5  include /etc/logrotate.d

     6  /var/log/wtmp {

     7      monthly

     8      create 0664 root utmp

     9          minsize 1M

    10      rotate 1

    11  }

· Line 1 - **weekly **configuration option ensures a weekly rotation of all log-files defined in main configuration file and in /etc/logrotate.d/ directory.

· Line 2 - **rotate 4** ensures that logrotate keeps a 4 weeks backup of all log files

· Line 3 - **create** option instructs logrotate to create new empty log files after each rotation

· Line 4 - **dateext** appends an extension to all rotated log files in form of date when each particular log file was processed by logrotate

· Line 5 - **include** all other configuration from directory /etc/logrotate.d

· Line 6 -  11 contains a specific service log rotate configuration

As opposed to logrotate.conf a directory **/etc/logrotate.d/** contains a specific service configuration files used by logrotate. In the next section we will create a sample skeleton logrotate configuration.

**3.1. Including new service logs to logrotate**

 In this section we will add new log file into a logrotate configuration. Let's say that we have a log file called:

/var/log/linuxtechtips.log

sitting in our /var/log directory that needs to be rotated on daily basis. First we need to create a new logrotate configuration file to accommodate for our new log file:

$ vi /etc/logrotate.d/linuxtechtips

Insert a following text into /etc/logrotate.d/linuxtechtips:

/var/log/linuxtechtips.log {

  

    missingok

    notifempty

 compress

 size 20k

    daily

    create 0600 root root

}

Here is a line by line explanation of the above logrotate configuration file:

**TIP: **If you wish to include multiple log files in a single configuration file use wildcard. For example /var/log/mylogs/*.log will instruct logrotate to rotate all log files located in /var/log/mylogs/ with extension .log.

· **missingok**\- do not output error if logfile is missing

· **notifempty**\- donot rotate log file if it is empty

· **compress**\- Old versions of log files are compressed with gzip(1) by default

· **size**\- Log file is rotated only if it grow bigger than 20k

· **daily**\- ensures daily rotation

· **create**\- creates a new log file wit permissions 600 where owner and group is root user

 The logrotate utility as quite versatile as it provides many more configuration options. Below, I will list few other configuration options for log rotate. To get a complete list, consult logrotate's manual page:

$ man logrotate

· **copy**  \- Make a copy of the log file, but don’t change the original at all.

· **mail <email@address>**\- When a log is rotated out-of-existence, it is mailed to address.

· **olddir <directory>**\- Logs are moved into <directory> for rotation.

· **postrotate/endscript**\- The lines between postrotate and endscript are executed after the log file is rotated.

**3.2. Testing a new Logrotate configuration**

Once you have created a new logrotate configuration file within /etc/logrotate.d:

\# cat /etc/logrotate.d/linuxtechtips 

  

/var/log/linuxtechtips.log {

    missingok

    notifempty

    compress

    size 20k

    daily

    create 0600 root root

}

create some sample log file ( if not existent ! ):

\# echo "rotate my log file" > /var/log/linuxtechtips.log

Once your log file is in place force logrotate to rotate all logs with -f option.

\# logrotate -f /etc/logrotate.conf

**Warning**: The above command will rotate all your logs defined in /etc/logrotate.d directory.

Now visit again your /var/log/directory and confirm that your log file was rotated and new log file was created:

\# cat /var/log/linuxtechtips.log

  

rotate my log file

\# logrotate -f /etc/logrotate.conf 

\# cat /var/log/linuxtechtips.log

file /var/log/linuxtechtips.log-20130409.gz 

/var/log/linuxtechtips.log-20130409.gz: gzip compressed data, from Unix, last modified: Tue Apr  9 12:43:50 2013

\# zcat /var/log/linuxtechtips.log-20130409.gz 

rotate my log file

As you can see the new empty log file linuxtechtips.log was created and old linuxtechtips.log file was compressed with gzip and renamed with date extension.

**TIP: **In order to see a content of your compressed log file you do not need to decompress it first. Use **zcat** or **zless** commands which will decompress your log file on fly.

**4. Conclusion**

As it was already mentioned previously, the best way to avoid your system being clogged by log files is to create a separate partition/logical volume for your /var/ or even better /var/log directory. However, even then logrotate can help you to save some disk space by compressing your log files. Logrotate may also help you to archive your log files for a future reference by creating an extra copy or by emailing you any newly rotated log files. For more information see logrotate's manual page:

$ man logrotate

  

  

[1]: http://2.bp.blogspot.com/-oxZJUs_4KkI/UnyAyly5xmI/AAAAAAAAAnE/DDmetiQHuCg/s1600/log-rotate.png

