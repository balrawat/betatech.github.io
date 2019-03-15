---
layout: post
title: How to install Ubuntu Server 10.04 in Hyper-V
date: '2013-01-24T17:23:00.000+05:30'
author: Balvinder Rawat
tags:
  - ubuntu
  - virtual machine
  - linux
  - hyper-v
  - virtualization
modified_time: '2013-08-06T16:43:15.038+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-6741176544354261345'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/01/how-to-install-ubuntu-server-1004-in.html
---
  

Last July, Microsoft announced the drivers for Linux source code is available in the Hyper-V virtualization environment. In practice, the 2.6.32 of the Linux kernel version now contains drivers for synthetic Hyper-V, virtual machine including the VMBus, storage, and network components. In detail, it's hv\_vmbus, hv\_storvsc, hv\_blkvsc and hv\_netvsc modules. These modules are described in [this article][1].

  

Out configurations "officially supported", I tested the activation of these modules in new Ubuntu Server 10.04, provided recently with the 2.6.32 kernel. To do this I found [this article][2] which explains how to enable these modules, and which I inspire me thus far.

  

**Enabling modules**

  

Firstly it must ensure that the Hyper-V modules are loaded at startup. To do this, edit the file /etc/initramfs-tools/modules and add the following four lines:

  

hv_vmbus

hv_storvsc

hv_blkvsc

hv_netvsc

  

  

Then, update the initramfs image:

$ sudo update-initramfs - u

  

Finally, configure the network by changing the/etc/network/interfaces file to configure the network interface named **seth0**. Indeed, a synthetic NIC would be named **seth** n instead of **eth** n for "legacy" network adapter.

  

For example for a DHCP configuration, add the following to /etc/network/interfaces:

  

Auto eth0

iface eth0 inet dhcp

  

  

or, for a static IP address:

  

  

Auto eth0

iface eth0 inet static

address ip_address

netmask mask

Gateway address

  

  

It remains only to restart, and check the proper loading of drivers using the command:

$ lsmod | grep hv_ (lower case L) in lsmod

  

**Test procedure**

For my test I used Windows Server 2008 R2 Hyper-V, and 32-bit [Ubuntu Server 10.04][3] (ubuntu-10. 04 - server - i386 .iso).

Because I set up the VM with a synthetic network adapter, it is not detected the installation. This is not serious; it will be when it has made steps outlined previously after installation.

  

![Erreur : aucune carte réseau détectée](http://blogs.technet.com/blogfiles/pascals/WindowsLiveWriter/UbuntuServerdansHyperVaveclesdriversHype_E693/image_3.png "Error: no network  adapter detected")

  

On this error message, choose <Continue>.

Once the virtual machine installed and started, the steps outlined above are fairly simple to implement:

  

![initramfs](http://blogs.technet.com/blogfiles/pascals/WindowsLiveWriter/UbuntuServerdansHyperVaveclesdriversHype_E693/image_10.png "initramfs")

![interfaces](http://blogs.technet.com/blogfiles/pascals/WindowsLiveWriter/UbuntuServerdansHyperVaveclesdriversHype_E693/image_11.png "Interfaces")

  

After a reboot (sudo reboot), we have many assets on the network map seth0 synthetic, and other drivers loaded:

  

![Réseau et drivers Hyper-V](http://blogs.technet.com/blogfiles/pascals/WindowsLiveWriter/UbuntuServerdansHyperVaveclesdriversHype_E693/image_14.png "Network systems and Hyper-V")

  

That is what servers run Linux under Hyper-V with decent performance. Have to wait for integration into the Linux kernel the next features (multi-processors, clock synchronization and stop integrated), these features are currently available in the beta integration services 2.1, SUSE Linux Enterprise Server Red Hat Enterprise Linux.

[1]: http://blogs.technet.com/b/port25/archive/2009/07/22/introduction-to-the-linux-integration-components.aspx
[2]: http://blog.allanglesit.com/2010/05/ubuntu-and-hyper-v-the-paths-to-enlightenment/
[3]: http://www.ubuntu.com/download/server

