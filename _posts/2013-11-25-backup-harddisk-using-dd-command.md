---
layout: post
title: 'Backup Harddisk Using the dd Command '
date: '2013-11-25T15:45:00.002+05:30'
author: Balvinder Rawat
tags:
  - dd
  - copy drive
modified_time: '2013-11-25T15:46:02.192+05:30'
thumbnail: >-
  https://3.bp.blogspot.com/-Gt36s1Jh0r0/UpMjHvBDfHI/AAAAAAAAAsA/CkppsNPabkk/s72-c/dd.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-301842551935014901'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/11/backup-harddisk-using-dd-command.html'
---
![](https://3.bp.blogspot.com/-Gt36s1Jh0r0/UpMjHvBDfHI/AAAAAAAAAsA/CkppsNPabkk/s1600/dd.png)

## Overview

The dd command is a useful tool for copying one entire hard drive to another. This can be helpful if you want to move your entire computer system to a new hard drive. The trick is making sure you know which drive you are copying from and which drive you are copying to. There is no recovering your data if you accidentally copy an empty drive to your system drive. It will overwrite all your information.

## The Process

Here are some commands and tools that you will want to use:

*   **df -h**  (this will show you your drives and the disk free space)
*   **dd if=/dev/sdb of=/dev/sdc** (important: sdb and sdc are examples you will need to know what your specific drives are )


We can also use dd to create image backup of a hard disk

Instead of taking a backup of the hard disk, you can create an image file of the hard disk and save it in other storage devices.There are many advantages to backing up your data to a disk image, one being the ease of use. This method is typically faster than other types of backups, enabling you to quickly restore data following an unexpected catastrophe.

  ## \# dd if=/dev/hda of=~/hdadisk.img

The above creates the image of a harddisk /dev/hda

### ## Restore:

To restore a hard disk with the image file of an another hard disk, use the following dd command example.

## \# dd if=hdadisk.img of=/dev/hdb

The image file hdadisk.img file, is the image of a /dev/hda, so the above command will restore the image of /dev/hda to /dev/hdb.

### ## Backup a Partition

You can use the device name of a partition in the input file, and in the output either you can specify your target path or image file as shown in the dd command example below.

##   # dd if=/dev/hda1 of=~/partition1.img

### ## CDROM Backup

dd command allows you to create an iso file from a source file. So we can insert the CD and enter dd command to create an iso file of a CD content.

# ## dd if=/dev/cdrom of=tgsservice.iso bs=2048

dd command reads one block of input and process it and writes it into an output file. You can specify the block size for input and output file. In the above dd command example, the parameter “bs” specifies the block size for the both the input and output file. So dd uses 2048bytes as a block size in the above command.

**Note:** If CD is auto mounted, before creating an iso image using dd command, its always good if you unmount the CD device to avoid any unnecessary access to the CD ROM.

[1]: https://3.bp.blogspot.com/-Gt36s1Jh0r0/UpMjHvBDfHI/AAAAAAAAAsA/CkppsNPabkk/s1600/dd.png

