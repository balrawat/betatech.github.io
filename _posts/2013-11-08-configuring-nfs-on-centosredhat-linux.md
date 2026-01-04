---
layout: post
title: Configuring NFS on Linux
date: '2013-11-08T11:51:00.001+05:30'
author: Balvinder Rawat
tags:
  - network fileserver
  - nfs
  - nfs server
modified_time: '2013-11-08T12:03:56.480+05:30'
thumbnail: >-
  https://3.bp.blogspot.com/-InZP20sz6Eg/UnyC4Le6YtI/AAAAAAAAAnQ/lHDFDlXTnxI/s72-c/nfs.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-8981667642659805114'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/11/configuring-nfs-on-centosredhat-linux.html
---
![](https://3.bp.blogspot.com/-InZP20sz6Eg/UnyC4Le6YtI/AAAAAAAAAnQ/lHDFDlXTnxI/s1600/nfs.png)

## 1. Introduction

The Network File System is certainly one of the most widely used network services. Network file system (NFS) is based on the [Remote procedure call] Remote procedure callwhich allows the client to automatically mount remote file systems and therefore transparently provide an access to it as if the file system is local.

## 2. Scenario

In this scenario we are going to export the file system from the an IP address 10.1.1.50 ( NFS server ) host and mount it on an a host with an IP address 10.1.1.55 ( NFS Client ). Both NFS server and NFS client will be running Ubuntu Linux.

## 3. Prerequisites

At this point, we assume that the NFS service daemon is already installed on your system, including portmap daemon on which NFS setup depends.

If you have not done so yet simply install nfs-common package on both NFS client and NFS server using using apt-get tool.

\# apt-get install nfs-common

The command above will fetch and install all support files common to NFS client and NFS server including portmap.

Additionally we need to install extra package on our NFS server side.

apt-get install nfs-kernel-server

This package is the actual NFS daemon listenning on both UDP and TCP 2049 ports.

Execute rpcinfo -p to check correctness of your NFS installation and to actually confirm that NFS server is indeed running and accepting calls on a port 2049:

\# rpcinfo -p | grep nfs

    100003    2   udp   2049  nfs

    100003    3   udp   2049  nfs

    100003    4   udp   2049  nfs

    100003    2   tcp   2049  nfs

    100003    3   tcp   2049  nfs

    100003    4   tcp   2049  nfs

Furthermore, before we start exporting and mounting NFS directories, your system needs to actually support network file system. To check whether your system supports NFS grep /proc/filesystems and search for nfs.

\# cat /proc/filesystems | grep nfs

nodev   nfs

nodev   nfs4

If you do not see any output it means that NFS is not supported or the NFS module have not been loaded into your kernel. To load NFS module execute:

\# modprobe nfs

When installed correctly, the NFS daemon should be now listening on both UDP and TCP 2049 port and portmap should be waiting for instructions on a port 111.

At this point you should have portmap listening on both NFS server and NFS client:

rpcinfo -p | grep portmap

    100000    2   tcp    111  portmapper

    100000    2   udp    111  portmapper

## 4. Server export file

All directories we want to share over the network using NFS need to be defined on the server side of this communication and more specifically they need to be defind with /etc/exports file. In the next section you will see most common NFS exports:

## 4.1. Most common exports options

Here are the most common NFS export techniques and options:

<table border="1" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="border-collapse: collapse; text-align: justify;"><tbody><tr><td style="padding: 0in 0in 0in 0in; width: 300.0pt;" width="400"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">/home/nfs/ 10.1.1.55(rw,sync)<o:p></o:p></span></span></div></td><td style="padding: 0in 0in 0in 0in;"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">export /home/nfs directory for host with an IP address 10.1.1.55 with read, write permissions, and synchronized mode<o:p></o:p></span></span></div></td></tr><tr><td style="padding: 0in 0in 0in 0in;"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">/home/nfs/ 10.1.1.0/24(ro,sync)<o:p></o:p></span></span></div></td><td style="padding: 0in 0in 0in 0in;"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">export /home/nfs directory for network 10.1.1.0 with netmask 255.255.255.0 with read only permissions and synchronized mode<o:p></o:p></span></span></div></td></tr><tr><td style="padding: 0in 0in 0in 0in; width: 300.0pt;" width="400"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">/home/nfs/ 10.1.1.55(rw,sync) 10.1.1.10(ro,sync)<o:p></o:p></span></span></div></td><td style="padding: 0in 0in 0in 0in;"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">export /home/nfs directory for host with IP 10.1.1.55with read, write permissions, synchronized mode, and also export /home/nfs directory for another host with an IP address 10.1.1.10 with read only permissions and synchronized mode<o:p></o:p></span></span></div></td></tr><tr><td style="padding: 0in 0in 0in 0in; width: 300.0pt;" width="400"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">/home/nfs/ 10.1.1.55(rw,sync,no_root_squash)<o:p></o:p></span></span></div></td><td style="padding: 0in 0in 0in 0in;"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">export /home/nfs directory for host with an IP address 10.1.1.55with read, write permissions, synchronized mode and the remote root user will be treated as a root and will be able to change any file and directory.<o:p></o:p></span></span></div></td></tr><tr><td style="padding: 0in 0in 0in 0in; width: 300.0pt;" width="400"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">/home/nfs/ *(ro,sync)<o:p></o:p></span></span></div></td><td style="padding: 0in 0in 0in 0in;"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">export /home/nfs directory for any host with read only permissions and synchronized mode<o:p></o:p></span></span></div></td></tr><tr><td style="padding: 0in 0in 0in 0in; width: 300.0pt;" width="400"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">/home/nfs/ *.linuxtechtips.com(ro,sync)<o:p></o:p></span></span></div></td><td style="padding: 0in 0in 0in 0in;"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">export /home/nfs directory for any host within linuxtechtips.com domain with a read only permission and synchronized mode<o:p></o:p></span></span></div></td></tr><tr><td style="padding: 0in 0in 0in 0in; width: 300.0pt;" width="400"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">/home/nfs/ foobar(rw,sync)<o:p></o:p></span></span></div></td><td style="padding: 0in 0in 0in 0in;"><div class="MsoNormal" style="margin: 7.5pt 0in;"><span style="font-size: 12pt;"><span style="font-family: Verdana, sans-serif;">export /home/nfs directory for hostname foobar with read, write permissions and synchronized mode<o:p></o:p></span></span></div></td></tr></tbody></table>

## 4.2. Edit exports file

Now that we have familiarized our selfs with some NFS's export options we can define our first NFS export. Open up your favorite text editor, for example, vim and edit /etc/exports file by adding a line /home/nfs/ *(ro,sync) which will export /home/nfs directory for any host with read only permissions. Instead of text editor you can simply insert your NFS export line into /etc/exports file using echo command:

\# echo '/home/nfs/ *(ro,sync)' > /etc/exports

\# tail -1 /etc/exports

/home/nfs/ *(ro,sync)

Be sure that the directory you are about to export by NFS exists. You can also create a file inside the /home/nfs directory which will help you troubleshoot once you mount /home/nfs/ remotely.

\# touch /home/nfs/nfs-test-file

**NOTE: **The default behavior of NFS kernel daemon is to include additional option to your export line which is "no\_subtree\_check". Be aware of this fact when you attempt to configure your NFS exports further.

## 4.3. Restart NFS daemon

Once you have edited /etc/exports file you need to restart your NFS daemon to apply any changes. Depending on your Linux distribution the restarting procedure of NFS may differ. Ubuntu and Debian users:

\# /etc/init.d/nfs-kernel-server restart

Redhat and Fedora users

\# /etc/init.d/nfs restart

If you later decide to add more NFS exports to the /etc/exports file, you will need to either restart NFS daemon or run command exportfs:

\# exportfs -ra

## 5. Mount remote file system on client

First we need to create a mount point:

\# mkdir /home/nfs_local

If you are sure that the NFS client and mount point are ready, you can run the mount command to mount exported NFS remote file system:

\# mount 10.1.1.50:/home/nfs /home/nfs_local

In case that you need to specify a filesystem type you can do this by:

\# mount -t nfs 10.1.1.50:/home/nfs /home/nfs_local

You may also get and an error message:

mount: mount to NFS server failed: timed out (retrying).

This may mean that your server supports higher NFS version and therefore you need to pass one extra argument to your nfs client mount command. In this example we use nfs version 3:

\# mount -t nfs -o nfsvers=3 10.1.1.50:/home/nfs /home/nfs_local

In any case now you should be able to access a remote /home/nfs directory locally on your NFS client.

\# ls /home/nfs_local/

nfs-test-file

\# cd /home/nfs_local/

\# ls

nfs-test-file

\# touch test

touch: cannot touch `test': Read-only file system

The above output proves that a remote NFS export is mounted and that we can access it by navigating to a local /home/nfs_local/ directory. Please notice that the touch command reports that the filesystem is mounted as read-only which was exactly our intention.

## 6. Configure automount

To make this completely transparent to end users, you can automount the NFS file system every time a user boots a Linux system, or you can also use PAM modules to mount once a user logs in with a proper username and password. In this situation just edit /etc/fstab to mount system automatically during a system boot. You can use your favorite editor and create new line like this within /etc/fstab:

10.1.1.50:/home/nfs /home/nfs_local/ nfs defaults 0 0

as before you also use echo command to do that:

\# echo "10.1.1.50:/home/nfs /home/nfs_local/ nfs defaults 0 0" >> /etc/fstab

\# tail -1 /etc/fstab

10.1.1.50:/home/nfs /home/nfs_local/ nfs defaults 0 0

## 7. Conclusion

The Network File System comes with tons of export options. What has been shown here, just barely scratches the surface of NFS. Please visit [Linux NFS-HOWTO] Linux NFS-HOWTOhosted by linux documentation project or [NFS homepage] NFS homepagefor more details.

## 8. Appendix A

Following section of this NFS tutorial is going to be devoted to RedHat and Fedora Linux systems which by default block all incoming traffic to a NFS server by engaging firewall using iptables rules. For this reason when the firewall is running on your NFS server, you might get this error when mounting NFS filesytem:

## mount.nfs: mount to NFS server '10.1.1.13' failed: System Error: No route to host.

This error message has nothing to do with your NFS  configuration, all what needs to be done is either turn off the firewall or add iptables rules to allow traffic on portmap port 111, nfs port 2049 and random ports for other nfs services.

There are two solutions to this problem: easy solution is to turn off the firewall completely and the right solution to add appropriate iptables rules.

## 8.1. Turn off firewall on Redhat like systems:

The easiest solution is to just turn off the firewall. This will automatically grant access to the nfs daemon to anyone. I would suggest this solution only for testing purposes of your NFS configuration. Enter the following command to stop firewall and clean up all iptables rules:

\# service iptables stop

Now when your NFS settings are correct you should be able to mount nfs filesystem from you client machine.

## 8.2. Add iptables rules to allow NFS communication

This is a more complex but right solution to the above problem. First we need to set static port for nfs services such as rquotad, mountd, statd, and lockd by editing /etc/sysconfig/nfs file. Add or uncomment following lines in your /etc/sysconfig/nfs file:

LOCKD_TCPPORT=32803

LOCKD_UDPPORT=32769

MOUNTD_PORT=892

STATD_PORT=662

Restart you NFSD daemon with following commands:

\# /etc/init.d/nfs restart

\# /etc/init.d/nfslock restart

Use rpcinfo command to confirm a validity of your new ports settings:

\# rpcinfo -p localhost

The output should be similar to the one below:

program vers proto port

100000 2 tcp 111 portmapper

100000 2 udp 111 portmapper

100011 1 udp 999 rquotad

100011 2 udp 999 rquotad

100011 1 tcp 1002 rquotad

100011 2 tcp 1002 rquotad

100003 2 udp 2049 nfs

100003 3 udp 2049 nfs

100003 4 udp 2049 nfs

100021 1 udp 32769 nlockmgr

100021 3 udp 32769 nlockmgr

100021 4 udp 32769 nlockmgr

100021 1 tcp 32803 nlockmgr

100021 3 tcp 32803 nlockmgr

100021 4 tcp 32803 nlockmgr

100003 2 tcp 2049 nfs

100003 3 tcp 2049 nfs

100003 4 tcp 2049 nfs

100005 1 udp 892 mountd

100005 1 tcp 892 mountd

100005 2 udp 892 mountd

100005 2 tcp 892 mountd

100005 3 udp 892 mountd

100005 3 tcp 892 mountd

100024 1 udp 662 status

100024 1 tcp 662 status

Save your current iptables rules into iptables-rules-orig.txt :

\# iptables-save > iptables-rules-orig.txt

Create file called iptables-nfs-rules.txt with the following content:

*filter

:INPUT ACCEPT \[0:0\]

:FORWARD ACCEPT \[0:0\]

:OUTPUT ACCEPT \[2:200\]

:RH-Firewall-1-INPUT - \[0:0\]

-A INPUT -j RH-Firewall-1-INPUT

-A FORWARD -j RH-Firewall-1-INPUT

-A RH-Firewall-1-INPUT -i lo -j ACCEPT

-A RH-Firewall-1-INPUT -p icmp -m icmp --icmp-type any -j ACCEPT

-A RH-Firewall-1-INPUT -p esp -j ACCEPT

-A RH-Firewall-1-INPUT -p ah -j ACCEPT

-A RH-Firewall-1-INPUT -d 224.0.0.251 -p udp -m udp --dport 5353 -j ACCEPT

-A RH-Firewall-1-INPUT -p udp -m udp --dport 631 -j ACCEPT

-A RH-Firewall-1-INPUT -p tcp -m tcp --dport 631 -j ACCEPT

-A RH-Firewall-1-INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT

-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport 2049 -j ACCEPT

-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport 22 -j ACCEPT

-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport 111 -j ACCEPT

-A RH-Firewall-1-INPUT -p udp -m state --state NEW -m udp --dport 111 -j ACCEPT

-A RH-Firewall-1-INPUT -p udp -m state --state NEW -m udp --dport 2049 -j ACCEPT

-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport 32769 -j ACCEPT

-A RH-Firewall-1-INPUT -p udp -m state --state NEW -m udp --dport 32769 -j ACCEPT

-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport 32803 -j ACCEPT

-A RH-Firewall-1-INPUT -p udp -m state --state NEW -m udp --dport 32803 -j ACCEPT

-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport 662 -j ACCEPT

-A RH-Firewall-1-INPUT -p udp -m state --state NEW -m udp --dport 662 -j ACCEPT

-A RH-Firewall-1-INPUT -p tcp -m state --state NEW -m tcp --dport 892 -j ACCEPT

-A RH-Firewall-1-INPUT -p udp -m state --state NEW -m udp --dport 892 -j ACCEPT

-A RH-Firewall-1-INPUT -j REJECT --reject-with icmp-host-prohibited

COMMIT

Apply new rules with iptables-restore, where the single argument will be an iptables-nfs-rules.txt file:

**NOTE:**this will create a new set of iptables rules. If you have already defined some iptables rules previously, you may want to edit iptables-rules-orig.txt  and use it with iptables-restore command instead.

\# iptables-restore iptables-nfs-rules.txt

Save these new rules, so you do not have to apply new rules for nfs daemon next time you restart your server:

\# service iptables save

Now your server is ready to accept client nfs requests. Optionally, you may restart iptables rules / firewall with the following command:

\# service iptables restart

[1]: https://3.bp.blogspot.com/-InZP20sz6Eg/UnyC4Le6YtI/AAAAAAAAAnQ/lHDFDlXTnxI/s1600/nfs.png
[2]: https://en.wikipedia.org/wiki/Remote_procedure_call
[3]: https://tldp.org/HOWTO/NFS-HOWTO/index.html
[4]: https://nfs.sourceforge.net/

