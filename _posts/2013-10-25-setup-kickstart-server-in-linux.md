---
layout: post
title: Setup Kickstart Server in Linux ( RHEL/CENTOS)
date: '2013-10-25T20:24:00.000+05:30'
author: Balvinder Rawat
tags:
  - pxe boot
  - installation
  - kickstart
modified_time: '2013-10-29T10:34:14.917+05:30'
thumbnail: >-
  https://1.bp.blogspot.com/-0RoFVlT_u_w/Um9BwZQbVOI/AAAAAAAAAmM/nechlJDH3J0/s72-c/netboot.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-8508964222255614522'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/10/setup-kickstart-server-in-linux.html'
---
[![](https://1.bp.blogspot.com/-0RoFVlT_u_w/Um9BwZQbVOI/AAAAAAAAAmM/nechlJDH3J0/s320/netboot.png)][1]

**What is Kickstart?**

  

Many system administrators would prefer to use an automated installation method to install Red Hat Enterprise Linux on their machines. To answer this need, Red Hat created the kickstart installation method. Using kickstart, a system administrator can create a single file containing the answers to all the questions that would normally be asked during a typical installation.

Kickstart files can be kept on a single server system and read by individual computers during the installation. This installation method can support the use of a single kickstart file to install Red Hat Enterprise Linux on multiple machines, making it ideal for network and system administrators.

Kickstart provides a way for users to automate a Red Hat Enterprise Linux installation.

All kickstart scriptlets and the log files of their execution are stored in the **/tmp** directory to assist with debugging installation failures.

  

**How to perform a Kickstart Installation?**

Kickstart installations can be performed using a local DVD, a local hard drive, or via NFS, FTP, HTTP, or HTTPS.

To use kickstart, you must:

· Create a kickstart file.

· Create a boot media with the kickstart file or make the kickstart file available on the network.

· Make the installation tree available.

· Start the kickstart installation.

  

To create a kickstart file, you can use **Kickstart Configurator.**

**Kickstart Configurator**is not installed by default on Red Hat Enterprise Linux 6. Run`**su - yum install system-config-kickstart**`or use your graphical package manager to install the software.

  

**Setup Kickstart Server in Linux**

  

1. Install tftp server and enable TFTP service

a. yum install tftp-server.

b. Enable TFTP server.

vi /etc/xinetd.d/tftp and change disable to 'no'

c. service xinetd restart  
  

2. Install syslinux if not already installed

yum install syslinux  
  

3. Copy needed files from syslinux to the tftpboot directory

cp /usr/lib/syslinux/pxelinux.0 /tftpboot

cp /usr/lib/syslinux/menu.c32 /tftpboot

cp /usr/lib/syslinux/memdisk /tftpboot

cp /usr/lib/syslinux/mboot.c32 /tftpboot

cp /usr/lib/syslinux/chain.c32 /tftpboot  
  

4. Create the directory for your PXE menus

mkdir /tftpboot/pxelinux.cfg  
  

5. For each "Release" and "ARCH" Copy vmlinuz and initrd.img from /images/pxeboot/ directory on "disc 1" of that $Release/$ARCH to /tftpboot/images/RHEL/$ARCH/$RELEASE

mkdir -p /tftpboot/images/RHEL/i386/5.

mkdir -p /tftpboot/images/RHEL/i386/5.8

mkdir -p /tftpboot/images/RHEL/x86_64/5.1

mkdir -p /tftpboot/images/RHEL/x86_64/5.8  
  

6. For RHEL 5.8 x86_64, do the following

mount /dev/cdrom /cdrom

cd /cdrom/images/pxeboot

cp vmlinuz initrd.img /tftpboot/images/RHEL/x86_64/5.8

Do the above for all releases and ARCH you want to kickstart from this server.  
  

7. Add this to your existing or new /etc/dhcpd.conf.  
  

8. Note: xxx.xxx.xxx.xxx is the IP address of your PXE server

allow booting;

allow bootp;

option option-128 code 128 = string;

option option-129 code 129 = text;

next-server xxx.xxx.xxx.xxx;

filename "/pxelinux.0";  
  

9. Restart DHCP service

  service dhcpd restart  
  

10. Create Simple or Multilevel PIXIE menu. Create a file called "default" in /tftpboot/pxelinux.cfg directory. A Sample file named "isolinux.cfg" is found on the boot installation media in "isolinux" directory. Copy this file as default and edit this file as per requirement. A sample default file is given bellow.

default menu.c32

prompt 0

timeout 300

ONTIMEOUT local

  

MENU TITLE PXE Menu

  

LABEL Pmajic

        MENU LABEL Pmajic

        kernel images/pmagic/bzImage

        append noapic initrd=images/pmagic/initrd.gz root=/dev/ram0 init=/linuxrc ramdisk_size=100000

  

label Dos Bootdisk

        MENU LABEL ^Dos bootdisk

        kernel memdisk

        append initrd=images/622c.img

  

LABEL RHEL 5 x86 eth0

        MENU LABEL RHEL 5 x86 eth0

        KERNEL images/RHEL/x86/5.8/vmlinuz

        APPEND initrd=images/RHEL/x86\_64/5.8/initrd.img ramdisk\_size=10000

               ks=nfs:xx.xx.xx.xxx:/ ksdevice=eth1

  

LABEL RHEL 5 x86_64  eth0

        MENU LABEL RHEL 5 x86_64  eth0

        KERNEL images/RHEL/x86_64/5.8/vmlinuz

        APPEND initrd=images/RHEL/x86\_64/5.8/initrd.img ramdisk\_size=10000

               ks=nfs:xx.xx.xx.xxx:/ ksdevice=eth1

  

11. Install the kickstart Configurator tool. This tool will be helpful to create the kickstart configuration file.

yum install system-config-kickstart  
  

12. Create the kickstart config file. This file can be created using kickstart Configuration Tool. A Sample file anaconda-ks.cfg based on current installation of a system is placed in /root directory. We can also use this /root/anaconda-ks-cfg as the configuration file. Copy this file to the location specified in the default file. Make sure the directory is NFS exported if you are using NFS for installing the OS.  
  

13. Modify the kickstart configuration file as per requirement. If you are using NFS for installation, Make sure to copy the ISO images of Linux disks to any NFS server and NFS export the directory. This server/directory details need to be specified in the jumpstart configuration file.  
  

14. After creating the KS configuration files and copying the ISO images, the installation can be started.

  

  

[1]: https://1.bp.blogspot.com/-0RoFVlT_u_w/Um9BwZQbVOI/AAAAAAAAAmM/nechlJDH3J0/s1600/netboot.png

