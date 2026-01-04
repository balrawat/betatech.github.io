---
layout: post
title: How to encrypt a partition with Cryptoloop
date: '2013-11-20T10:31:00.000+05:30'
author: Balvinder Rawat
tags:
  - encryption
  - cryptoloop
modified_time: '2013-11-20T10:31:19.684+05:30'
thumbnail: >-
  https://4.bp.blogspot.com/--_13QzBVEG4/Uom95pGEq7I/AAAAAAAAApI/9AfGJaQ4U4s/s72-c/loop.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-8463814954141109069'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/11/how-to-encrypt-partition-with-cryptoloop.html
---
![](https://4.bp.blogspot.com/--_13QzBVEG4/Uom95pGEq7I/AAAAAAAAApI/9AfGJaQ4U4s/s1600/loop.png)

===

1. Introduction
===============

This article will describe how to encrypt entire partition with a Cryptoloop. Cryptoloop is a disk encryption module for Linux. It was first introduced in the 2.5.x kernel series. Cryptoloop has an ability to create an encrypted file system on a single partition or within a regular file, which can later simply be mounted by the mount command. Cryptoloop uses so called loopback device, which needs to be called with any file system request. Currently there are many alternatives for Cryptoloop usage and the most common is Loop-AES. This article will explain a simple usage of the cryptoloop module for partition encryption and mounting within a Linux Operating system.

2. Prerequisites
================

As it was already mentioned the cryptoloop module was introduced to Linux with the 2.5 kernel series. Therefore, the chances are that this module is already available on your system. To confirm that the cryptoloop module is available on your system run:


\# lsmod | grep cryptoloop

cryptoloop             12671  1

If no output has been produced that means that the module is unavailable and you will need to load it with:

\# modprobe cryptoloop

Another tool, which we are going to need is**losetup,**which should be already a variable on your system.

3. Setting up a loopback device
===============================

Cryptoloop can be used to create an encrypted filesystem within the entire partition or single file. The procedure is the same for both of them. The only difference is the supplied argument either to be a path to a regular file or to block the device. As an example in this tutorial we will encrypt a block device /dev/sdb1.

First, we can make sure to overwrite entire partition with some random data. This step is optional but recommended.

**WARNING:**note that the below command will physically erase any data you may already have on your partition:

\# dd if=/dev/urandom of=/dev/sdb1 bs=1M

Disregard any possible error message about a full disk space.

In the next step we need to choose a type of encryption. A list of encryption algorithm available on your system can be seen by the following command:

 # cat /proc/crypto

We will use AES encryption algorithm. In the next step we use the losetup utility to attach our /dev/sdb1 block device to the system's loopback device /dev/loop0.


\# losetup -e aes -k 256 /dev/loop0 /dev/sdb1

Password:

You will be prompted to enter a password, which will be used to mount and unmount your partition. Choose a strong password right from the beginning as there is no easy way to change this password later.

4. Create a filesystem
======================

At this point we should have our /dev/sdb1 partition attached to /dev/loop0 with AES 256 bit encryption. Next we use the /dev/loop0 device to create a filesystem. Feel free to use any type of filesystem you deem it to be worthy. I will use ext4:

\# mkfs.ext4 /dev/loop0

5. Mounting Loopback device
===========================

To mount a loopback device in this case is as simple as mounting any other block devices. First, we need to create a mount point:

\# mkdir /mnt/cryptoloop

Once ready, we use the mount command to mount /dev/loop0 as ext4 filesystem:

\# mount -t ext4 /dev/loop0 /mnt/cryptoloop/

At this point we are able to navigate to /mnt/cryptoloop/  and store some data. For example, let's create a new file foo.txt:

\# echo LinuxTechTips.com > foo.txt

Once you finish using your new encypted filesystem you simply unmount it and detach it from a loopback device:


\# umount /mnt/cryptoloop/

\# losetup -d /dev/loop0

After executing the above commands your data ( foo.txt ) will no longer be available.

6. Cryptoloop permanent mount
=============================

Once the new /dev/sdb1 file-system was created and encrypted with use of cryptoloop and the loopback device we can mount it again without use of the pseudo loopback device /dev/loop0.

\# mount -t ext4 /dev/sdb1 /mnt/cryptoloop/ -o encryption=aes

\# cd /mnt/cryptoloop/

\# cat foo.txt

LinuxTechTips.com

To be able to mount off our encrypted partition easily with the simple mount command we need to add the following line into the /etc/fstab file:

/dev/sdb1       /mnt/cryptoloop        ext4       noauto,encryption=aes

Now, we are able to mount this partition with:

\# mount -a

OR

\# mount /mnt/cryptoloop

7. Conclusion
=============

You can find many other crypto utilities available on your Linux system. One worth to mention in conjunction to cryptoloop is its successor dm-crypt. Cryptoloop is part of Linux Crypto API since the kernel version 2.6.

[1]: https://4.bp.blogspot.com/--_13QzBVEG4/Uom95pGEq7I/AAAAAAAAApI/9AfGJaQ4U4s/s1600/loop.png

