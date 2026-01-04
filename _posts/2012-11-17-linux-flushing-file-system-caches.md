---
layout: post
title: Linux Flushing File System Caches
date: '2012-11-17T18:18:00.002+05:30'
author: Balvinder Rawat
tags:
  - file system cache
modified_time: '2014-01-07T12:54:41.445+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-33893767986000103'
blogger_orig_url: 'https://www.linuxtechtips.com/2012/11/linux-flushing-file-system-caches.html'
---


We may drop the file system caches on Linux to free up memory for applications. Kernels 2.6.16 and newer provide a mechanism via the /proc/ to make the kernel drop the page cache and/or inode and dentry caches on command. We can use this mechanism to free up the memory. However, this is a non-destructive operation that only free things that are completely unused and dirty objects will not be freed until written out to disk. Hence, we should flush these dirty objects to disk first. We can run “sync” to flush them out to disk. And the drop operations by the kernel will free more memory.

We can flush caches of the file systems by two steps:

Flush file system buffers
-------------------------

Call the sync command:

\# sync

Free pagecache, dentries and inodes
-----------------------------------

To use /proc/sys/vm/drop_caches, just echo a number to it.

To free pagecache:

\# echo 1 > /proc/sys/vm/drop_caches

To free dentries and inodes:

\# echo 2 > /proc/sys/vm/drop_caches

To free pagecache, dentries and inodes:

echo 3 > /proc/sys/vm/drop_caches

This is a non-destructive operation and will only free things that are completely unused. Dirty objects will continue to be in use until written out to disk and are not freeable. If you run "sync" first to flush them out to disk, these drop operations will tend to free more memory.

