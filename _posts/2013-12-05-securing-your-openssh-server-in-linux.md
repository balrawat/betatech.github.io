---
layout: post
title: Securing your OpenSSH server in Linux
date: '2013-12-05T10:33:00.001+05:30'
author: Balvinder Rawat
tags:
  - secure ssh
  - SSH
modified_time: '2013-12-05T10:33:45.217+05:30'
thumbnail: >-
  https://1.bp.blogspot.com/-GD8eXr1qbkM/UqAI4RFbJSI/AAAAAAAAAus/IguRSPH1dsQ/s72-c/ssh.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-6483259583342610426'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/securing-your-openssh-server-in-linux.html
---
![](https://1.bp.blogspot.com/-GD8eXr1qbkM/UqAI4RFbJSI/AAAAAAAAAus/IguRSPH1dsQ/s640/ssh.png)

Secure Shell (SSH) is a program used to secure communication between two entities, often used as a replacement for Telnet and the Berkeley protocols such as remote shell (RSH) and remote login (Rlogin). SSH is also used as a secure remote copy utility, replacing traditional protocols such as the File Transfer Protocol (FTP) and Remote Copy Protocol (RCP).

For this tutorial, we are going to demonstrate steps on securing your **OpenSSH Server **which is a free version of the SSH protocol suite.

Note: Steps 1-9 can be done by  tweaking your sshd_config and do ssh service restart after changes to take effect.

### 1. Use SSH Protocol 2

Use SSH version 2 (SSH2) only as it offers more performance, flexibility and security than SSH1.

- To verify what SSH protocol version you are running, check your /etc/ssh/sshd_config and look for the line “Protocol”,

\[root@linuxtechtips ~\]# vi /etc/ssh/sshd_config

Protocol 2

\[root@linuxtechtips ~\]# /etc/init.d/sshd restart

Stopping sshd: \[  OK  \]

Starting sshd: \[  OK  \]

### 2. Disable direct root SSH logins

- Disable direct logging in as root via ssh. This is like inviting hackers to brute force your root password.

It’s recommend to login as a normal user and then after that, just use su or sudo if want to execute priviledge commands.

PermitRootLogin no

### 3. Enable a SSH warning banner

You can display a warning banner before login to require acknowledgment of the contents. This can be done by defining under sshd_config

a. Create a Banner on any location. e.g. /etc/linuxtechtips

\[root@linuxtechtips~\]# vi /etc/linuxtechtips

###############################################################

AUTHORIZED USERS ONLY

All login attempts will be logged!!!

###############################################################

b. Edit /etc/ssh/sshd_config. Locate the line containing “Banner”, uncomment and specify the file location

vi /etc/ssh/sshd_config

\# no default banner path

Banner /etc/linuxtechtips

c. Restart ssh service

\[root@linuxtechtips~\]# service sshd restart

Stopping sshd: \[  OK  \]

Starting sshd: \[  OK  \]

d. Test:

@ssh client

login as: darwin

###############################################################

AUTHORIZED USERS ONLY

All login attempts will be logged!!!

###############################################################

darwin@10.0.2.100′s password:

Last login: Fri Oct 19 18:19:12 2012 from 10.0.2.2

### 4. Disable empty passwords

To disable empty password, edit /etc/ssh/sshd_config and make sure this line below is uncommented

PermitEmptyPasswords no

### 5. Disable Host-based authentication

It is not recommended that hosts always agreed to trust one another

HostbasedAuthentication no

### 6. Configure Idle Timeout

Let say you want the system to log out users after 15 mins of idling. Then you can set this:

\[root@linuxtechtips~\]# vi /etc/ssh/sshd_config

ClientAliveInterval 300

ClientAliveCountMax 3

where:

This will give a timeout of 15 minutes (300 secs X 3)

ClientAliveInterval – timeout in seconds.

ClientAliveCountMax – total number of checkalive message sent by the ssh server without getting any response from the ssh client

Also,  you can do this 15 minute timeout:

ClientAliveInterval 900

ClientAliveCountMax 0

Additional Tip: This is slightly different with “TMOUT” variable that will terminate the shell if no activity for N seconds

\# export TMOUT=N

\[root@linuxtechtips~\]# export TMOUT=60

### 7. Limit SSH LoginGraceTime

By default, sshd will allow a connected user that has not begun the authentication process for a period 2 minutes (120 secs) for a grace time. It’s recommended to shorten this time to protect from brute force attacks.

LoginGraceTime 30

### 8. Change ssh port number

The advantage of this is somehow protects your box against automated attacks or malicious scripts that is trying to get in via ssh default port 22.

Port 35286

### 9. Limit or Permit only specific users or groups to login

All users by default is allowed to access your box. But you have the options to allow or deny few users or groups. This can be done in either of this way.

#\[AllowUsers\]

AllowUsers darwin tux

OR

#\[DenyUsers\]

DenyUsers user1 user2

DenyGroups group1 group2 group3

### 10. Update OpenSSH & OS

Make sure your Linux system is running the latest version for OpenSSH. SSH package version depends on your Linux distribution & OS version. Your distro will use the best or stable version for any packages, so if you want to upgrade to another version, you can do this via source package installation. It can be downloaded on OpenSSH official site [https://www.openssh.com] https://www.openssh.com. Alternatively, you can do it by installing the latest rpm package or changing your repository, then use the yum.

For instance, if you are running CentOS 5.8 to check the current installed package and verify if there’s update, tr the following:

\[root@linuxtechtips~\]# cat /etc/issue

CentOS release 5.8 (Final)

Kernel \\r on an \\m

\[root@linuxtechtips~\]# rpm -qa | grep openssh

openssh-4.3p2-82.el5

openssh-clients-4.3p2-82.el5

openssh-server-4.3p2-82.el5

\[root@linuxtechtips~\]# ssh -V

OpenSSH_4.3p2, OpenSSL 0.9.8e-fips-rhel5 01 Jul 2008

\[root@linuxtechtips~\]# yum update openssh*

Loaded plugins: fastestmirror, security

Determining fastest mirrors

\* base: mirror.nus.edu.sg

\* extras: mirror.nus.edu.sg

\* updates: mirror.nus.edu.sg

base                                                     | 1.1 kB     00:00

extras                                                   | 1.9 kB     00:00

extras/primary_db                                        | 171 kB     00:00

updates                                                  | 1.9 kB     00:00

updates/primary_db                                       | 828 kB     00:01

Skipping security plugin, no data

Setting up Update Process

No Packages marked for Update

### 11. Enforce access controls list by using TCP wrappers

TCP wrappers is used to restrict access to TCP services based on IP, hostname, network address etc. It supports SSH via the libwrap library. To check if your sshd is

dynamically linked against libwrap:

\[root@linuxtechtips~\]# which sshd

/usr/sbin/sshd

\[root@linuxtechtips~\]# ldd /usr/sbin/sshd | grep libwrap

libwrap.so.0 => /lib/libwrap.so.0 (0×00978000)

@/etc/syslog.conf

\# The authpriv file has restricted access.

authpriv.*                                              /var/log/secure

Configuration Files of TCP Wrapper

a. /etc/hosts.allow

b. /etc/hosts.deny

The file names are quite self-explanatory.

Access will be allowed when it matches an entry in the /etc/hosts.allow file

Access will be denied when it matches an entry in the /etc/hosts.deny file

But take note of the rules or points to consider

- access rules in hosts.allow are applied first

- rules in each file are read from the top down, so take note the order of rules

- changes in hosts.allow or hosts.deny will take effect immediately, no need to restart any services.

- access to service is permitted if no rules are found in either file

- use ‘#’ character to insert comments

- it uses this format

tcp\`service : client\`list \[ : shell_command \]

where:

tcp_server – daemon process names

client_list – IP, hostnames, patterns, wildcards matching the client address or hostname

There are several patterns that you can use under client_list which we will not covering on this topic. But the recommended setting will be:

Deny anything not explicitly allowed and only Allow certain services.

\[root@linuxtechtips~\]# cat /etc/hosts.allow

#

\# hosts.allow   This file describes the names of the hosts which are

#               allowed to use the local INET services, as decided

#               by the ‘/usr/sbin/tcpd’ server.

#

ALL: ALL

\[root@linuxtechtips~\]# cat /etc/hosts.allow

#

\# hosts.allow   This file describes the names of the hosts which are

#               allowed to use the local INET services, as decided

#               by the ‘/usr/sbin/tcpd’ server.

#

sshd : linuxtechtipstutorials.com : allow

sshd: 192.168.0.192/255.255.255.240 : allow

sshd : 192.168.0.100 : allow

### 12. Configure iptables for added SSH security

It’s good to have your servers protected by hardwares or appliances such as security appliances, PIX, ASA etc. that will added more protection such as limiting TCP connections esp. on preventing dictionary attacks.

If you don’t have this, it’s a good thing this can be done also from your Linux server using iptables.

Sample iptables  to allow only specified host:

iptables -A INPUT -p tcp -m state –state NEW –source 172.16.0.101 –dport 35286 -j ACCEPT

Another example iptables rule:

iptables -N RULE1

iptables -A INPUT -p tcp –dport 35286 -m state –state NEW -j RULE1

iptables -A RULE1 -m recent –set –name SSH

iptables -A RULE1 -m recent –update –seconds 60 –hitcount 4 –name SSH -j DROP

where:

Line1: create a new chaing RULE1

Line2/3: allow incoming SSH connection on ssh port 35286 and it will pass through this chain

Line4: source IP should not be more than 3 attempts within 60 seconds, else packets will be dropped from that source IP

### 13. Use Strong Passwords

As system administrator, you can set a criteria for users to have a strong passwords. To enforce password complexity on  your Linux boxes via  PAM (the “pluggable authentication module”)

\[root@linuxtechtips~\]# cat /etc/pam.d/system-auth | grep password

password    requisite     pam\_cracklib.so try\_first_pass retry=3

password    sufficient    pam\_unix.so md5 shadow nullok try\_first\_pass use\_authtok

password    required      pam_deny.so

Change to something like this:

password requisite pam\_cracklib.so try\_first_pass retry=3 minlength=12 lcredit=1 ucredit=1 dcredit=1 ocredit=1 difok=4

where:

try\_first\_pass = sets the number of times a user can attempt to set a good password before it aborts

minlen = measure of complexity related to the password length

lcredit = minimum number of required lowercase letters

ucredit = minimum number of required uppercase letters

dcredit = minimum number of required digits

ocredit = minimum number of required other characters

difok = sets the number of characters that must be different from the previous passwords

Alternatively, you can use /etc/login.defs to set parameters such as password expiration, etc.

@/etc/login.defs

\# Password aging controls:

#

#       PASS\_MAX\_DAYS   Maximum number of days a password may be used.

#       PASS\_MIN\_DAYS   Minimum number of days allowed between password changes.

#       PASS\_MIN\_LEN    Minimum acceptable password length.

#       PASS\_WARN\_AGE   Number of days warning given before a password expires.

#

PASS\_MAX\_DAYS   99999

PASS\_MIN\_DAYS   0

PASS\_MIN\_LEN    5

### 14. Use Private/Public Keys for SSH authentication

If you decided not to do password authenticaton instead using of keys, then you can follow this [tutorial] tutorial.

### 15. Patch OpenSSH to latest security fix

As long as you have the latest updates or patches installed on your Linux distribution, that should be enough to tell that you are fully patched.

To check the changelog for the openssh rpm, use the command below. It will show you various patches

\[root@linuxtechtips~\]# rpm -q –changelog openssh | more

\* Wed Jan 04 2012 Petr Lautrbach <plautrba@redhat.com> 4.3p2-82

- improve RNG seeding from /dev/random (#681291,#708056)

\* Fri Dec 02 2011 Petr Lautrbach <plautrba@redhat.com> 4.3p2-81

- make ssh(1)’s ConnectTimeout option apply to both the TCP connection and

SSH banner exchange (#750725)

[1]: https://1.bp.blogspot.com/-GD8eXr1qbkM/UqAI4RFbJSI/AAAAAAAAAus/IguRSPH1dsQ/s1600/ssh.png
[2]: https://www.openssh.com/ "OpenSSH"
[3]: https://freelinuxtutorials.com/tutorials/ssh-authentication-via-public-private-keys "SSH authentication via private public keys"

