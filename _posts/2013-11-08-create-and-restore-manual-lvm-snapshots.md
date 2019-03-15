---
layout: post
title: Create and Restore manual LVM Snapshots
date: '2013-11-08T11:59:00.002+05:30'
author: Balvinder Rawat
tags:
  - lvm
  - snapshot
  - lvm snapshot
modified_time: '2013-11-08T12:01:21.261+05:30'
thumbnail: >-
  http://1.bp.blogspot.com/-cK8ZgtJZA00/UnyEyRENxlI/AAAAAAAAAnc/CKm6B9rdO7U/s72-c/LVM+snapshots.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-2506188966380852617'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/11/create-and-restore-manual-lvm-snapshots.html
---
[![](http://1.bp.blogspot.com/-cK8ZgtJZA00/UnyEyRENxlI/AAAAAAAAAnc/CKm6B9rdO7U/s1600/LVM+snapshots.png)][1]

**1. Introduction**

By creating a Logical Volume snapshots you are able to freeze a current state of any of your logical volumes. This means that you can very easily create a backup and once needed rollback to a original logical volume state. This method is very similar to what you already know from using Virtualization software such as Virtualbox or VMware where you can simply take a snapshot of entire virtual machine and revert back in case something went wrong etc. Therefore, using LVM snapshots allows you to take a control of your system's logical volumes whether it is your personal laptop or server. This tutorial is self-contained as no previous experience with Logical Volume Manager is required.

**2. Scenario**

In this article we will explain how to manually create and restore logical volume snapshots. Since we do not assume any previous experience with Logical Volume Manager we will start from a scratch using a dummy physical hard drive /dev/sdb with size of 1073 MB. Here are all steps in nutshell:

· 1First we will create two partitions on our /dev/sdb drive. These partitions will be of "8e Linux LVM" type and will be used to create a physical volumes

· 2Once both partitions are created we use pvcreate command to create physical volumes

· 3In this step we create a new Logical Volume Group and a single 300MB in size logical volume using ext4 filesystem

· 4Mount our new logical volume and create some sample data

· 5Take a snapshot and remove sample data

· 6Rollback logical volume snapshot

**3. Creating a Logical Volume**

**3.1.  Logical Volume Manager Basics**

**Here is a quick start definition of logical volume manager:**

Logical volume manager allows you to create a Logical group consisting of multiple physical volumes. Physical volumes can be entire hard-drives or separate partitions.  Physical volumes can reside on a single or multiple hard-drives, partitions , USBs, SAN's etc. To increase a Logical Volume size you can add additional physical volumes. Once you create Logical volume group you can then create multiple Logical volumes and at the same time completely disregard a physical volume layer. Logical volume group can be resized at any time by adding more physical volumes so new logical volumes can created or resized.

**3.2. Create a partitions**

First, we need to create a partitions and mark them as physical volumes.  Here is our physical disk we are going to work with:

\# fdisk -l /dev/sdb

  

  

Disk /dev/sdb: 1073 MB, 1073741824 bytes

255 heads, 63 sectors/track, 130 cylinders, total 2097152 sectors

Units = sectors of 1 * 512 = 512 bytes

Sector size (logical/physical): 512 bytes / 512 bytes

I/O size (minimum/optimal): 512 bytes / 512 bytes

Disk identifier: 0x335af99c

  

   Device Boot      Start         End      Blocks   Id  System

Let's create two primary partitions. Here we are using fdisk to do tis job. Feel free to use any other partitioning tool to do this job such as cfdisk, parted etc.

\# fdisk /dev/sdb

All command are highlighted in bold:

Command (m for help): **n**

Partition type:

   p   primary (0 primary, 0 extended, 4 free)

   e   extended

Select (default p): **p**

Partition number (1-4, default 1):

Using default value 1

First sector (2048-2097151, default 2048):

Using default value 2048

Last sector, +sectors or +size{K,M,G} (2048-2097151, default 2097151): **+400M**

  

Command (m for help): **n**

Partition type:

   p   primary (1 primary, 0 extended, 3 free)

   e   extended

Select (default p): **p**

Partition number (1-4, default 2): **2**

First sector (821248-2097151, default 821248):

Using default value 821248

Last sector, +sectors or +size{K,M,G} (821248-2097151, default 2097151): **+200M**

  

Command (m for help): **t**

Partition number (1-4): **1**

Hex code (type L to list codes): **8e**

Changed system type of partition 1 to 8e (Linux LVM)

  

Command (m for help): **t**

Partition number (1-4): **2**

Hex code (type L to list codes): **8e**

Changed system type of partition 2 to 8e (Linux LVM)

  

Command (m for help): **w**

The partition table has been altered!

  

Calling ioctl() to re-read partition table.

Syncing disks.

 If you followed the above steps, your new partition table on the disk /dev/sdb will now look similar to the one below:

\# fdisk -l /dev/sdb

  

Disk /dev/sdb: 1073 MB, 1073741824 bytes

255 heads, 63 sectors/track, 130 cylinders, total 2097152 sectors

Units = sectors of 1 * 512 = 512 bytes

Sector size (logical/physical): 512 bytes / 512 bytes

I/O size (minimum/optimal): 512 bytes / 512 bytes

Disk identifier: 0x335af99c

  

   Device Boot      Start         End      Blocks   Id  System

/dev/sdb1            2048      821247      409600   8e  Linux LVM

/dev/sdb2          821248     1230847      204800   8e  Linux LVM

**3.3. Create Physical Volumes**

At this point we mark both partitions as physical volumes. Please note that you do not have to follow the same pattern as in this tutorial. For example you could simply partition entire disk with a single partition instead of two. Use pvcreate to create physical volumes:

 # pvcreate /dev/sdb\[1-2\]

  

  Writing physical volume data to disk "/dev/sdb1"

  Physical volume "/dev/sdb1" successfully created

  Writing physical volume data to disk "/dev/sdb2"

  Physical volume "/dev/sdb2" successfully created

**3.4. Create Volume Group**

Now it is time to create a Volume Group. For this we use tool vgcreate. The new Volume Group will have a name "volume_group".

\# vgcreate volume_group /dev/sdb1 /dev/sdb2

  

  Volume group "volume_group" successfully created

After execution of the above command you will have a new volume group created named "volume_group". This new volume group will consist of two physical volumes:

· /dev/sdb1

· /dev/sdb2

You can see the stats of your new volume group using vgdisplay command:

\# vgdisplay 

  

  \-\-\- Volume group ---

  VG Name               volume_group

  System ID             

  Format                lvm2

  Metadata Areas        2

  Metadata Sequence No  1

  VG Access             read/write

  VG Status             resizable

  MAX LV                0

  Cur LV                0

  Open LV               0

  Max PV                0

  Cur PV                2

  Act PV                2

  VG Size               592.00 MiB

  PE Size               4.00 MiB

  Total PE              148

  Alloc PE / Size       0 / 0   

  Free  PE / Size       148 / 592.00 MiB

  VG UUID               37jef7-3q3E-FyZS-lMPG-5Jzi-djdO-BgPIPa

**3.5. Creating Logical Volumes**

If all went smoothly we can now finally create a logical volume.  The size of the logical volume must not exceed the size of your logical group. Let's create new logical volume called "volume1" of size 200 MB and format it with ext4 filesystem.

\# lvcreate -L 200 -n volume1 volume_group

  

  Logical volume "volume1" created

You can see a definition of your new logical volume using lvdisplay command. Take a note of the LV Path value as you will need it when creating a filesystem on your new h"volume1" logical volume.

\# lvdisplay

  

  \-\-\- Logical volume ---

 **LV Path                /dev/volume_group/volume1**

  LV Name                volume1

  VG Name                volume_group

  LV UUID                YcPtZH-mZ1J-OQQu-B4nj-MWo0-yC18-m77Vuz

  LV Write Access        read/write

  LV Creation host, time debian, 2013-05-08 12:53:17 +1000

  LV Status              available

  # open                 0

  LV Size                200.00 MiB

  Current LE             50

  Segments               1

  Allocation             inherit

  Read ahead sectors     auto

  \- currently set to     256

  Block device           254:0

Now you can create an ext4 filesystem on your logical volume:

\# mkfs.ext4 /dev/volume_group/volume1

**4. Logical Volume Snapshot**

Finally, we have come to the point where we can take a snapshot of our logical volume created in previous section. For this we will also need some sample data on our Logical Volume "volume1" so once we revert from the snapshot we can confirm entire process by comparing original data with data recovered from the snapshot.

**4.1. Understanding Snaphosts**

In order to understand how snapshots work we first need to understand what logical volume consists of and how data are stored. This concept is similar to well known symbolic links. When you create a symbolic link to a file you are not creating a copy of the actual file but instead you simply create only a reference to it. Logical volume stores data in a similar fashion and it consists of two essential parts:

· metadata pointers

· data block

When a snapshot is created Logical Volume Manager simply creates a copy of all Metadata pointers to a separate logical volume. Metadata do not consume much space and therefore your are able to create snapshot of let's say 2GB logical volume to 5MB snapshot volume. The snapshot volume only starts grow once you start altering data of the original logical volume. Which means, that every time you remove or edit file on the original logical volume a copy of that file ( data ) is created on snapshot volume. For a simple changes you may need to create a snapshot volume of around 5-10% of the logical volume original size. If you are prepared to make many changes on your original logical volume then you will need lot more than 10%. Let's get started:

**4.2. Sample Data**

First, create a new mount point directory for "volume1" and mount it :

\# mkdir /mnt/volume1

  

\# mount /dev/volume_group/volume1 /mnt/volume1

Enter "volume1" mount point and copy some sample data:

\# cd /mnt/volume1

  

\# cp -r /sbin/ .

\# du -s sbin/

8264    sbin/

Using previous commands we have copied entire /sbin directory into /mnt/volume1. The size of /mnt/volume1/sbin/ is currently 8264 KB.

 Creating a Snapshot

Now we are going to create a snapshot of logical volume "volume1". In the process Logical Volume Manager will create a new separate logical volume. This new logical volume will have size of 20MB and will be called "volume1_snapshot":

\# lvcreate -s -L 20M -n volume1\_snapshot /dev/volume\_group/volume1

  

  Logical volume "volume1_snapshot" created

Execute **lvs** command to confirm that new volume snapshot has been created:

\# lvs

  

  LV               VG           Attr     LSize   Pool Origin  Data%  Move Log Copy%  Convert

  volume1          volume_group owi-aos- 200.00m                                            

  volume1\_snapshot volume\_group swi-a-s-  20.00m      volume1   0.06

  

  

Now that the snapshot has been created we can start altering data on "volume1" for  example by removing the entire content:

  

\# cd /mnt/volume1

  

\# rm -fr 

\# rm -fr sbin/

After this operation you can consult again lvs command and see that Data% on the volume1_snap is now increased. If you want to, you can now mount your snapshot volume to confirm that the original data from "volume1" still exists.

**4.3. Revert Logical Volume Snapshot**

Before we revert our logical volume snapshot, let's first confirm that our /mnt/volume1/sbin data are still missing:

\# du -s /mnt/volume1/sbin

  

du: cannot access `/mnt/volume1/sbin': No such file or directory

Recovering a Logical Volume snapshots consists of two steps:

· scheduling a  snapshot recovery after next logical volume activation

· deactivate and activate logical volume

To schedule a snapshot rollback execute a following command:

\# lvconvert --merge /dev/volume\_group/volume1\_snapshot

  

  Can't merge over open origin volume

  Merging of snapshot volume1_snapshot will start next activation.

After execution of the above command the logical volume "volume1" will rollback once it is activated. Therefore, what needs to be done next is to re-activate "volume1". First, make sure that you unmount your "volume1"

\# umount /mnt/volume1

Deactivate and activate you volume:

\# lvchange -a n /dev/volume_group/volume1

  

\# lvchange -a y /dev/volume_group/volume1

As a last step mount again your logical volume "volume1" and confirm that data all has been recovered:

\# mount /dev/volume_group/volume1 /mnt/volume1

  

\# du -s /mnt/volume1/sbin

8264    /mnt/volume1/sbin

**5. Conclusion**

The above was a basic example of snapshot manipulation using Logical Volume Manager. The usefulness of logical volume snapshots is enormous and it will sure help you with your tasks whether you are system administrator or a developer. Although you can use the setup above to create a multiple snapshots for a backup recovery you also need to know the you backup will find its limits on within you Logical Volume Group therefore any low level physical volume problems may render your snapshot useless.

  

  

[1]: http://1.bp.blogspot.com/-cK8ZgtJZA00/UnyEyRENxlI/AAAAAAAAAnc/CKm6B9rdO7U/s1600/LVM+snapshots.png

