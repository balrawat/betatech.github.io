---
layout: post
title: Crazy Commands
date: '2013-01-24T17:33:00.005+05:30'
author: Balvinder Rawat
tags:
  - linux
  - linux commands
  - commands
modified_time: '2013-03-13T12:12:56.084+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-5219313232086272496'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/01/crazy-commands.html'
---
  
Many of us who love to work on Linux enjoy the privilege of using a plethora of commands and tools. Here is our effort to introduce you to a few very simple- to-use, yet enormously effective commands. The intended audience may belong to all classes of Linux users and the only requirement is to have a basic acquaintance with Linux. Our article deals with bash shell and Linux version Fedora 9, kernel 2.6.25.  

1.  Often, commands on the console may span many lines, and encountering a type mistake at the beginning of the command would require you to use the slow way of punching the right/left arrow keys to traverse in the command string.  
      
    **Remedy:** Try Ctrl+e to move to the end of the command string and Ctrl+a to reach start. It’s the fastest way to edit a Linux command line. To delete a word in the command string, use Ctrl+w.
2.  Another wonder of a simple shell variable is `!$`. Let’s say you have to create a directory, go into it and then rename it. So the flow of commands would be:
    
    $ mkdir your_dir  
    $ mv your\_dir my\_dir  
    $ cd my_dir
    
      
    **Remedy:** Well, Linux has a shorter and quicker way:  
    
    $ mkdir your_dir  
    $ mv !$ my_dir  
    $ cd !$
    
      
    `!$` points to the last string in the command string. This is useful in various scenarios where the last word of command string is to be used in subsequent commands (almost with all Linux commands like `vi`, `tar`, `gzip`, etc).
3.  Do you want to know what an `ls` or a `date`command does internally? Just run the following code to get to know the basic block of any Linux command:
    
    $ strace -c /usr/bin/ls
    
      
    `strace` is a system call monitor command and provides information about system calls made by an application, including the call arguments and return value.
4.  What if you want to create a chain of directories and sub-directories, something like `/tmp/our/your/mine`?  
      
    **Remedy:**Try this:
    
    $ mkdir -p /tmp/our/your/mine
    
5.  One very interesting way to combine some related commands is with `&&`.
    
    $ cd dir_name && ls -alr && cd ..
    
6.  Now for some fun! Have you ever tried checking the vulnerability of your Linux system? Try a fork-bomb to evaluate this:
    
    $ :(){ :|: & };:
    
    It’s actually a shell function; look closely and it’s an unnamed function `:()` with the body enclosed in `{}`. The statement ‘`:|:`’ makes a call to the function itself and pipes the output to another function call—thus we are calling the function twice. `&` puts all processes in the background and hence you can’t kill any process. Finally ‘`;`’ completes the function definition and the last ‘`:`’ initiates a call to this unnamed function. So it recursively creates processes and eventually your system will hang. This is one of the most dangerous Linux commands and may cause your computer to crash!  
      
    **Remedy:** How to avoid a fork bomb? Of course, by limiting the process limit; you need to edit `/etc/security/limits.conf`. Edit the variable `nproc` to `user_name hard nproc 100`. You require root privileges to modify this file.
7.  One more dirty way to hack into the system is through continuous reboots, resulting in the total breakdown of a Linux machine. Here’s an option that you need root access for. Edit the file `/etc/inittab` and modify the line `id:5:initdefault:` to `id:6:initdefault:`. That’s all! Linux specifies various user modes and `6` is intended for reboot. Hence, your machine keeps on rebooting every time it checks for the default user mode.  
      
    **Remedy:** Modify your Grub configuration (the Linux bootloader) and boot in single user mode. Edit the file `/etc/inittab` and change the default user level to 5.

I hope you’ll have some fun trying out these commands, and that they bring you closer to Linux. Please do share your feedback and comments.  
  
  
_This Post has been taken from :_  
_http://www.linuxforu.com/teach-me/tips-tricks/crazy-commands/?phpMyAdmin=1d8b5f958924edce27dfa99df2ab8e99_

