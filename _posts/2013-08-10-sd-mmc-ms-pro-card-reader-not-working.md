---
layout: post
title: SD MMC MS-Pro card reader not working on DELL INSPIRON 15R 5520
date: '2013-08-10T22:50:00.000+05:30'
author: Balvinder Rawat
tags:
  - ubuntu
  - Ubuntu SD Card Reader
modified_time: '2013-08-10T22:52:22.973+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-1731733527182714002'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/08/sd-mmc-ms-pro-card-reader-not-working.html
---
Not sure how many of you've come across this, but for me this was unusual. Usually Ubuntu has great compatibility built out of the box. All the wifi,graphics etc are picked on boot. But when I inserted my SD card on its slot, it was not recognized & I'm running Ubuntu 12.04 LTS with 3.9.2 kernel. But it was simple google search & I found a simple solution for this problem:-

Create the file "sdhci-pci.conf" that contains one single line "options sdhci debug_quirks=0x40" in a directory "/etc/modprobe.d"

root@infra:/etc/modprobe.d# cat ./sdhci-pci.conf
options sdhci debug_quirks=0x40

and then reload the modules:

root@infra:/etc/modprobe.d# rmmod sdhci-pci
root@infra:/etc/modprobe.d# rmmod sdhci
root@infra:/etc/modprobe.d# modprobe sdhci-pci

(or reboot)

and plug-in the SD card now, it works...

I'm Happy again...

Hope it helps you too..

