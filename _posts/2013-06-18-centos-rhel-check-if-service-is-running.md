---
layout: post
title: 'CentOS | RHEL: Check If A Service Is Running Or Not'
date: '2013-06-18T16:11:00.005+05:30'
author: Balvinder Rawat
tags: null
modified_time: '2013-08-06T16:32:55.729+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-5593268503842869314'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/06/centos-rhel-check-if-service-is-running.html
---
  
We can use service command to get the status of services running on the system. It runs a System V init script in as predictable environment as possible, removing most environment variables and with current working directory set to /.  
  
Syntax is:  
  
service <service-name> status  
  
OR  
  
/etc/init.d/<service-name> status  
  
Example:  
  
Find, out if a service called httpd (Apache Web Server) is running on CentOS OR RHEL. Open a terminal or login using ssh, enter:  
  
  #  service httpd status  
  
Sample outputs:  
  
\[root@myserver ~\]# service httpd status  
  
httpd (pid  21585) is running...  

  

### Find out status of all services

The service --status-all command runs all init scripts, in alphabetical order, with the status command:

 #  service --status-all

Sample output:-

  
  
\[root@myserver ~\]# service --status-all  
  
anacron is stopped  
  
atd is stopped  
  
auditd is stopped  
  
cpuspeed is stopped  
  
crond (pid 3442) is running...  
  
cupsd (pid 5004) is running...  
  
gpm (pid 3316) is running...  
  
hald is stopped  
  
httpd is stopped  
  
ipmi_msghandler module not loaded.  
  
ipmi_si module not loaded.  
  
ipmi_devintf module not loaded.  
  
/dev/ipmi0 does not exist.  
  
Firewall is stopped.  
  
irqbalance (pid 3031) is running...  
  
Usage: jboss {start|stop|restart}  
  
Usage: jboss {start|stop|restart}  
  
mdmpd is stopped  
  
dbus-daemon-1 is stopped  
  
/etc/init.d/microcode_ctl: reading microcode status is not yet supported  
  
Server address not specified in /etc/sysconfig/netdump  
  
netplugd is stopped  
  
Configured devices:  
  
lo eth0  
  
Currently active devices:  
  
lo eth0  
  
NetworkManager is stopped  
  
nscd is stopped  
  
ntpd (pid 3117) is running...  
  
rhnsd (pid 3498) is running...  
  
saslauthd is stopped  
  
sendmail (pid 3145 3135) is running...  
  
smartd is stopped  
  
snmpd (pid 5035) is running...  
  
snmptrapd is stopped  
  
sshd (pid 32692 32690 31125 31123 31007 31005 28859 28828 27800 27797 25769 25763 24868 24865 24453 24451 23420 23417 22077 22072 21991 21989 21578 21576 21185 21183 20987 20984 20757 20755 20665 20661 19843 19837 18508 18490 18447 18445 15355 15349 15268 15266 11588 11580 11106 11104 8560 8557 8494 8428 8426 8425 8408 7597 7591 7450 7448 6677 6671 5249 5233 4776 4772 4570 4563 3084 2807 2805 2307 2305 1909 1907 1548 1545) is running...  
  
syslogd (pid 3014) is running...  
  
klogd (pid 3018) is running...  
  
vsftpd is stopped  
  
winbindd is stopped  
  
wpa_supplicant is stopped  
  
xfs (pid 3463) is running...  
  
xinetd (pid 4898) is running...

  

  

ps or pgrep command
-------------------

You can use ps or pgrep command as follows to find out if service is running or not on RHEL/Centos:

 #  ps aux | grep 'serviceName'

 # ps aux | grep 'httpd'

