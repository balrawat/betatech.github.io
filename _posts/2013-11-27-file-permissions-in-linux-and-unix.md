---
layout: post
title: File Permissions in Linux and Unix
date: '2013-11-27T18:34:00.004+05:30'
author: Balvinder Rawat
tags:
  - permissions
  - file system security
modified_time: '2013-11-27T18:47:00.514+05:30'
thumbnail: >-
  https://4.bp.blogspot.com/-PBLFYmYD_GM/UpXtaj1BlCI/AAAAAAAAAtU/7-YOQwdSvu8/s72-c/security.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-1373074920066184501'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/11/file-permissions-in-linux-and-unix.html'
---
** File system security (access rights)**
-----------------------------------------

In your**home**directory, type

## % ls -l (l for long listing!)

You will see that you now get lots of details about the contents of your directory, similar to the example below.

![](https://4.bp.blogspot.com/-PBLFYmYD_GM/UpXtaj1BlCI/AAAAAAAAAtU/7-YOQwdSvu8/s1600/security.png)

Each file (and directory) has associated access rights, which may be found by typing**ls -l**. Also,**ls -lg**gives additional information as to which group owns the file (beng95 in the following example):

## -rwxrw-r-- 1 ee51ab beng95 2450 Sept29 11:52 file1

In the left-hand column is a 10 symbol string consisting of the symbols d, r, w, x, -, and, occasionally, s or S. If d is present, it will be at the left hand end of the string, and indicates a directory: otherwise - will be the starting symbol of the string.

The 9 remaining symbols indicate the permissions, or access rights, and are taken as three groups of 3.

*   The left group of 3 gives the file permissions for the user that owns the file (or directory) (ee51ab in the above example);
*   the middle group gives the permissions for the group of people to whom the file (or directory) belongs (eebeng95 in the above example);
*   the rightmost group gives the permissions for all others.

The symbols r, w, etc., have slightly different meanings depending on whether they refer to a simple file or to a directory.

### Access rights on files.

*   r (or -), indicates read permission (or otherwise), that is, the presence or absence of permission to read and copy the file
*   w (or -), indicates write permission (or otherwise), that is, the permission (or otherwise) to change a file
*   x (or -), indicates execution permission (or otherwise), that is, the permission to execute a file, where appropriate

### Access rights on directories.

*   r allows users to list files in the directory;
*   w means that users may delete files from the directory or move files into it;
*   x means the right to access files in the directory. This implies that you may read files in the directory provided you have read permission on the individual files.

So, in order to read a file, you must have execute permission on the directory containing that file, and hence on any directory containing that directory as a subdirectory, and so on, up the tree.

### Some examples

<table border="1" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="border: 1pt outset rgb(102, 102, 102); text-align: justify;"><tbody><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">-rwxrwxrwx<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">a file that everyone can read, write and execute (and delete).<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">-rw-------<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">a file that only the owner can read and write - no-one else<span class="apple-converted-space">&nbsp;</span><br>can read or write and no-one has execution rights (e.g. your<span class="apple-converted-space">&nbsp;</span><br>mailbox file).<o:p></o:p></span></span></div></td></tr></tbody></table>

** Changing access rights**
---------------------------

### chmod (changing a file mode)

Only the owner of a file can use chmod to change the permissions of a file. The options of chmod are as follows

<table border="1" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="border: 1pt outset rgb(102, 102, 102); text-align: justify;"><tbody><tr><td style="background: #ECE9D8; border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Symbol<o:p></o:p></span></span></b></div></td><td style="background: #ECE9D8; border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Meaning<o:p></o:p></span></span></b></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">U<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">user<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">G<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">group<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">O<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">other<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">A<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">all<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">R<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">read<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">W<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">write (and delete)<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">X<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">execute (and access directory)<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">+<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">add permission<o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">-<o:p></o:p></span></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 2.25pt 2.25pt 2.25pt 2.25pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">take away permission<o:p></o:p></span></span></div></td></tr></tbody></table>

For example, to remove read write and execute permissions on the file**biglist**for the group and others, type

## % chmod go-rwx biglist

This will leave the other permissions unaffected.

To give read and write permissions on the file**biglist**to all,

## % chmod a+rw biglist

[1]: https://4.bp.blogspot.com/-PBLFYmYD_GM/UpXtaj1BlCI/AAAAAAAAAtU/7-YOQwdSvu8/s1600/security.png

