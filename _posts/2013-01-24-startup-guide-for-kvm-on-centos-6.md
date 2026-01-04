---
layout: post
title: Startup Guide for KVM on CentOS 6
date: '2013-01-24T17:17:00.000+05:30'
author: Balvinder Rawat
tags:
  - centos
  - linux
  - KVM
  - virtualization
modified_time: '2013-08-06T16:44:42.255+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-5234026909942508341'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/01/startup-guide-for-kvm-on-centos-6.html'
---
These instructions are very specific to CentOS 6.

For this I assume you have setup your server using the “Minimal” option when installing CentOS 6. You must also have the Virtualization features enabled for your CPU. This is done in your host’s BIOS.

Optionally you can skip the first section, Installing KVM, if you check all 4 “Virtualization” software categories during the install.

## Installing KVM

If you choose the “Minimal” option during CentOS 6 then this step is necessary. To get the full set of tools there are 4 software groups to install…

    Virtualization

    Virtualization Client

    Virtualization Platform

    Virtualization Tools

To install run

yum groupinstall “Virtualization*”

dejavu-lgc-sans-fonts is necessary or all the fonts in virt-manager will show as squares

yum install dejavu-lgc-sans-fonts

Once the install is finished verify that the KVM kernel module is loaded.

lsmod | grep kvm

You should see either kvm\_intel or kvm\_amd depending on your host’s CPU manufacturer.

At this point I chose to reboot the server. This allows services to be started and udev rules for KVM to be applied. This will also allow dbus to create the machine-id file, otherwise you would see something like the below when running virt-manager

## \# virt-manager

Xlib: extension “RANDR” missing on display “localhost:10.0″.

process 1869: D-Bus library appears to be incorrectly set up; failed to read machine uuid: Failed to open “/var/lib/dbus/machine-id”: No such file or directory

See the manual page for dbus-uuidgen to correct this issue.

D-Bus not built with -rdynamic so unable to print a backtrace

Aborted

If you receive that D-Bus error and would prefer not to restart then run this command to generate the necessary machine-id file

dbus-uuidgen > /var/lib/dbus/machine-id

## Final configuration steps

The server I run KVM on is headless, but I still like using virt-manager. So we must install the necessary tools to do X11 forwarding through SSH.

yum install xorg-x11-xauth

\# If you plan to use VNC to connect to the virtual machine’s console locally

yum install tigervnc

Now when you connect through SSH be sure to pass the -X flag to enable X11 forwarding.

**Optional:** Using an alternate location for VM images with SELinux

With SELinux enabled, special steps must be taken to change the default VM store from /var/lib/libvirt/images. My particular server I choose to keep all images and ISOs for VMs under /vmstore. The steps below give your new store the correct security context for SELinux.

\# this package is necessary to run semanage

yum install policycoreutils-python

semanage fcontext -a -t virt\_image\_t “/vmstore(/.*)?”

restorecon -R /vmstore

To activate this store you must open virt-manager, select your host, then do Edit-> Host Details. Under the Storage tab you can add your new storage volume.

Optional : Network Bridging for Virtual Machines

If you wish for your virtual machines to be accessible remotely then you must use network bridging to share your host’s network interface with the virtual machines. The setup requires linking one of your host’s physical interfaces with a bridge device. First copy your physical interface’s ifcfg file to create the new bridge device, named br0.

cp /etc/sysconfig/networking-scripts/ifcfg-eth0 /etc/sysconfig/networking-scripts/ifcfg-br0

Modify ifcfg-br0 to have the IP information in ifcfg-eth0 and remove, or comment out, that information in ifcfg-eth0. Below are examples of ifcfg-eth0 and ifcfg-br0. The highlighted lines are important.

/etc/sysconfig/networking-scripts/ifcfg-eth0

DEVICE=eth0

HWADDR=00:18:8B:58:07:3B

ONBOOT=yes

BRIDGE=br0

/etc/sysconfig/networking-scripts/ifcfg-br0

DEVICE=br0

TYPE=Bridge

BOOTPROTO=static

ONBOOT=yes

IPADDR=10.1.0.3

NETMASK=255.255.255.0

Once those two files are configured restart the network service

service network restart

Optional: Managing libvirt with standard user account

Beginning in CentOS 6 access to managing libvirt is handled by \[https://wiki.libvirt.org/page/SSHPolicyKitSetup PolicyKit\]. It’s always a good practice to do your daily administration tasks as some user besides root, and using PolicyKit you can give access to libvirt functions to a standard account.

First we create the necessary config file to define the access controls. The file must begin with a numeric value and have the .pkla extension.

vim /etc/polkit-1/localauthority/50-local.d/50-libvirt-remote-access.pkla

Here’s an example of the file I used to give access to a single user. Be sure to put your desired username in place of username on the highlighted line.

\[libvirt Management Access\]

Identity=unix-user:username

Action=org.libvirt.unix.manage

ResultAny=yes

ResultInactive=yes

ResultActive=yes

You can optionally replace Identity=unix-user:username with Identity=unix-group:groupname to allow access to a group of users.

Finally restart the libvirtd daemon to apply your changes.

/etc/init.d/libvirtd restart

## Creating the first virtual machine

You are now ready to create your virtual machines.

## Create the virtual disk

With the version of virt-manager shipped with CentOS 6 you cannot create qcow2 images from within the GUI. If you wish to create your new VM with a qcow2 format virtual disk you must do so from the command line, or see the next section for RPMs to upgrade virt-manager.

qemu-img create -f qcow2 CentOS-6.0-x86_64-Template.qcow2 20G

NOTE: Replace the filename “CentOS-6.0-x86_64-Template” with your desired name, and also replace “20G” with the desired max size of the virtual disk.

Now when creating your virtual machine select to use an existing virtual disk.

