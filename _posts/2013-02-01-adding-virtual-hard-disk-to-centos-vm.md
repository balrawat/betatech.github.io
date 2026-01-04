---
layout: post
title: Adding virtual hard disk to Centos VM on Vmware without reboot
date: '2013-02-01T17:49:00.003+05:30'
author: Balvinder Rawat
tags:
  - virtualbox
  - vmware
  - virtual machine
  - virtual hard disk
modified_time: '2014-01-07T12:52:25.245+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-3848310085301024157'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/02/adding-virtual-hard-disk-to-centos-vm.html
---


So you need to add an additional hard disk to your VM running the Centos/Redhat/Suse family of operating system, but its in production and you can not reboot it.

So how do you go about it?

Well, it is rather easy!

First, open the "edit settings" window, within the VM, either from the console menu, or by right clicking in the VM through the virtual infrastructure client. Add a hard disk and configure it with the size you require. Finally accept the changes and close the window. After a few seconds, the virtual infrastructure client will shown the reconfiguration being complete.

Now logon to the operating system of the VM, as the root user - or use sudo.

You will see that the VM does not see the new disk, i.e. running the command:

## 

## fdisk -l

## 

Shows only the existing disks, there is no sign of the new one.

What we need to do is, re-scan the SCSI bus, without rebooting the VM. To do this run the following command:


## echo "- - -" >/sys/class/scsi_host/host#/scan

## 

( make sure to note the spaces between "- - -" )

Where the # is replaced with the SCSI host value, usually 0

Now we re-run the command:


## fdisk -l


We can now see our additional disk and can carry on configuring it using the usual tools.

