---
layout: post
title: How wildcards work in Linux and Unix
date: '2013-11-27T18:26:00.002+05:30'
author: Balvinder Rawat
tags:
  - wildcard
  - shell scripting
modified_time: '2013-11-29T13:31:52.766+05:30'
thumbnail: >-
  http://4.bp.blogspot.com/-ORU9e-qu274/UpXroIkDMNI/AAAAAAAAAtM/WE-H5lA01E0/s72-c/wildcards-300x168.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-2142506593002609686'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/11/how-wildcards-work-in-linux-and-unix.html
---
[![](http://4.bp.blogspot.com/-ORU9e-qu274/UpXroIkDMNI/AAAAAAAAAtM/WE-H5lA01E0/s400/wildcards-300x168.png)][1]

**Wildcards**
-------------

### The * wildcard

The character*****is called a wildcard, and will match against none or more character(s) in a file (or directory) name. For example, in your**unixstuff**directory, type

**% ls list***

This will list all files in the current directory starting with**list....**

Try typing

**% ls *list**

This will list all files in the current directory ending with**....list**

### The ? wildcard

The character**?**will match exactly one character.

  

So**?ouse**will match files like**house**and**mouse**, but not**grouse**.

Try typing

  

**% ls ?list**

  

** Filename conventions**
-------------------------

We should note here that a directory is merely a special type of file. So the rules and conventions for naming files apply also to directories.

In naming files, characters with special meanings such as**/ \* & %**, should be avoided. Also, avoid using spaces within names. The safest way to name a file is to use only alphanumeric characters, that is, letters and numbers, together with _ (underscore) and . (dot).

<table border="1" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="border: 1pt outset rgb(153, 153, 153); text-align: justify;"><tbody><tr><td style="background: #ECE9D8; border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Good filenames<o:p></o:p></span></span></b></div></td><td style="background: #ECE9D8; border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Bad filenames<o:p></o:p></span></span></b></div></td></tr><tr><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">project.txt<o:p></o:p></span></span></div></td><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">project<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">my_big_program.c<o:p></o:p></span></span></div></td><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">my big program.c<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">fred_dave.doc<o:p></o:p></span></span></div></td><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">fred &amp; dave.doc<o:p></o:p></span></span></div></td></tr></tbody></table>

File names conventionally start with a lower-case letter, and may end with a dot followed by a group of letters indicating the contents of the file. For example, all files consisting of C code may be named with the ending**.c**, for example,**prog1.c**. Then in order to list all files containing C code in your home directory, you need only type**ls *.c**in that directory.

** Getting Help**
-----------------

### On-line Manuals

There are on-line manuals which gives information about most commands. The manual pages tell you which options a particular command can take, and how each option modifies the behaviour of the command. Type**man _command_**to read the manual page for a particular command.

For example, to find out more about the**wc**(word count) command, type

**% man wc**

Alternatively

**% whatis wc**

gives a one-line description of the command, but omits any information about options etc.

### Apropos

When you are not sure of the exact name of a command,

**% apropos keyword**

will give you the commands with keyword in their manual page header. For example, try typing

**% apropos copy**

**Summary**
-----------

  

<table border="1" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="border: 1pt outset rgb(153, 153, 153); text-align: justify;"><tbody><tr><td style="background: #ECE9D8; border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Command<o:p></o:p></span></span></b></div></td><td style="background: #ECE9D8; border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Meaning<o:p></o:p></span></span></b></div></td></tr><tr><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><b><span style="font-family: Verdana, sans-serif;">*<o:p></o:p></span></b></div></td><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">match any number of characters</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><b><span style="font-family: Verdana, sans-serif;">?<o:p></o:p></span></b></div></td><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">match one character</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><b><span style="font-family: Verdana, sans-serif;">man<span class="apple-converted-space">&nbsp;</span><var>command</var><o:p></o:p></span></b></div></td><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">read the online manual page for a command</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><b><span style="font-family: Verdana, sans-serif;">whatis<span class="apple-converted-space">&nbsp;</span><var>command</var><o:p></o:p></span></b></div></td><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">brief description of a command</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><b><span style="font-family: Verdana, sans-serif;">apropos<span class="apple-converted-space">&nbsp;</span><var>keyword</var><o:p></o:p></span></b></div></td><td style="border: inset #999999 1.0pt; mso-border-alt: inset #999999 .75pt; padding: 3.0pt 3.0pt 3.0pt 3.0pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">match commands with keyword in their man pages</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr></tbody></table>

  

  

  

[1]: http://4.bp.blogspot.com/-ORU9e-qu274/UpXroIkDMNI/AAAAAAAAAtM/WE-H5lA01E0/s1600/wildcards-300x168.png

