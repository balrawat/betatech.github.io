---
layout: post
title: Linux Commands Directory
date: '2013-01-28T10:57:00.005+05:30'
author: Balvinder Rawat
tags:
  - linux
  - linux commands
  - commands
modified_time: '2013-03-13T12:12:40.042+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-323187086143733983'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/01/linux-commands-directory.html'
---
Why Bother?
===========

Why do you need to learn the command line anyway? Well, let me tell you a story. A few years ago we had a problem where I used to work. There was a shared drive on one of our file servers that kept getting full. I won't mention that this legacy operating system did not support user quotas; that's another story. But the server kept getting full and it stopped people from working. One of our software engineers spent the better part of a day writing a C++ program that would look through all the user's directories and add up the space they were using and make a listing of the results. Since I was forced to use the legacy OS while I was on the job, I installed [a Linux-like command line environment for it.] a Linux-like command line environment for it. When I heard about the problem, I realized I could do all the work this engineer had done with this single line:

du -s * | sort -nr > $HOME/user\_space\_report.txt

Graphical user interfaces (GUIs) are helpful for many tasks, but they are not good for all tasks. I have long felt that most computers today are not powered by electricity. They instead seem to be powered by the "pumping" motion of the mouse! Computers were supposed to free us from manual labor, but how many times have you performed some task you felt sure the computer should be able to do but you ended up doing the work yourself by tediously working the mouse? Pointing and clicking, pointing and clicking.
I once heard an author say that when you are a child you use a computer by looking at the pictures. When you grow up, you learn to read and write.

Here is a complete linux command reference:

[Linux Command Directory] Linux Command Directory

[1]: https://www.cygwin.com/
[2]: https://oreilly.com/linux/command-directory/

