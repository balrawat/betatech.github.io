---
layout: post
title: Redirection in Linux and Unix
date: '2013-11-27T18:19:00.001+05:30'
author: Balvinder Rawat
tags:
  - redirection
modified_time: '2013-12-01T13:03:03.388+05:30'
thumbnail: >-
  http://2.bp.blogspot.com/--qut1SkmLZk/UpXqAVXotuI/AAAAAAAAAs8/e4_l533GQEw/s72-c/redirection.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-5112578020112203820'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/11/redirection-in-linux-and-unix.html'
---
[![](http://2.bp.blogspot.com/--qut1SkmLZk/UpXqAVXotuI/AAAAAAAAAs8/e4_l533GQEw/s1600/redirection.png)][1]

** Redirection  **
------------------

Most processes initiated by UNIX commands write to the standard output (that is, they write to the terminal screen), and many take their input from the standard input (that is, they read it from the keyboard). There is also the standard error, where processes write their error messages, by default, to the terminal screen.

We have already seen one use of the**cat**command to write the contents of a file to the screen.

Now type**cat**without specifying a file to read

**% cat**

Then type a few words on the keyboard and press the \[**Return**\] key.

Finally hold the \[**Ctrl**\] key down and press \[**d**\] (written as**^D**for short) to end the input.

What has happened?

If you run the**cat**command without specifing a file to read, it reads the standard input (the keyboard), and on receiving the 'end of file' (**^D**), copies it to the standard output (the screen).

In UNIX, we can redirect both the input and the output of commands.

** Redirecting the Output  **
-----------------------------

We use the > symbol to redirect the output of a command. For example, to create a file called**list1**containing a list of fruit, type  

**% cat > list1**

Then type in the names of some fruit. Press \[**Return**\] after each one.

**pear**

**

**banana**

**apple**

**^D {this means press \[Ctrl\] and \[d\] to stop}**

**  

What happens is the cat command reads the standard input (the keyboard) and the > redirects the output, which normally goes to the screen, into a file called**list1**

To read the contents of the file, type

**% cat list1**

### For Practice

Using the above method, create another file called**list2**containing the following fruit: orange, plum, mango, grapefruit. Read the contents of**list2**

  

### Appending to a file

The form >> appends standard output to a file. So to add more items to the file**list1**, type

**% cat >> list1**

Then type in the names of more fruit

**peach**

**

**grape**

**orange**

**^D (Control D to stop)**

**  

To read the contents of the file, type

**% cat list1**

You should now have two files. One contains six fruit, the other contains four fruit.

We will now use the cat command to join (concatenate)**list1**and**list2**into a new file called**biglist**. Type

**% cat list1 list2 > biglist**

What this is doing is reading the contents of**list1**and**list2**in turn, then outputing the text to the file**biglist**

To read the contents of the new file, type

**% cat biglist**

** Redirecting the Input  **
----------------------------

We use the < symbol to redirect the input of a command.

The command sort alphabetically or numerically sorts a list. Type

**% sort**

Then type in the names of some animals. Press \[Return\] after each one.

**dog**

**

**cat**

**bird**

**ape**

**^D (control d to stop)**

**  

The output will be

**ape**

**

**bird**

**cat**

**dog**

**  

Using < you can redirect the input to come from a file rather than the keyboard. For example, to sort the list of fruit, type

**% sort < biglist**

and the sorted list will be output to the screen.

To output the sorted list to a file, type,

**% sort < biglist > slist**

Use cat to read the contents of the file**slist**

** Pipes**
----------

To see who is on the system with you, type

**% who**

One method to get a sorted list of names is to type,

**% who > names.txt**

**

**% sort < names.txt**

**  

This is a bit slow and you have to remember to remove the temporary file called names when you have finished. What you really want to do is connect the output of the who command directly to the input of the sort command. This is exactly what pipes do. The symbol for a pipe is the vertical bar |

For example, typing

**% who | sort**

will give the same result as above, but quicker and cleaner.

To find out how many users are logged on, type

**% who | wc -l**

### For Practice

Using pipes, display all lines of**list1**and**list2**containing the letter 'p', and sort the result.

  

**Summary**
-----------

  

<table border="1" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="text-align: justify;"><tbody><tr><td style="background: #ECE9D8; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Command<o:p></o:p></span></span></b></div></td><td style="background: #ECE9D8; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Meaning<o:p></o:p></span></span></b></div></td></tr><tr><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><var><b>command</b></var><span class="apple-converted-space"><b>&nbsp;</b></span><b>&gt;<span class="apple-converted-space">&nbsp;</span><var>file</var><o:p></o:p></b></span></div></td><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">redirect standard output to a file</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><var><b>command</b></var><span class="apple-converted-space"><b>&nbsp;</b></span><b>&gt;&gt;<span class="apple-converted-space">&nbsp;</span><var>file</var><o:p></o:p></b></span></div></td><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">append standard output to a file</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><var><b>command</b></var><span class="apple-converted-space"><b>&nbsp;</b></span><b>&lt;<span class="apple-converted-space">&nbsp;</span><var>file</var><o:p></o:p></b></span></div></td><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">redirect standard input from a file</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><var><b>command1</b></var><span class="apple-converted-space"><b>&nbsp;</b></span><b>|<span class="apple-converted-space">&nbsp;</span><var>command2</var><o:p></o:p></b></span></div></td><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">pipe the output of command1 to the input of command2</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><b><span style="font-family: Verdana, sans-serif;">cat<span class="apple-converted-space">&nbsp;</span><var>file1 file2</var><span class="apple-converted-space">&nbsp;</span>&gt;<span class="apple-converted-space">&nbsp;</span><var>file0</var><o:p></o:p></span></b></div></td><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">concatenate file1 and file2 to file0</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><b><span style="font-family: Verdana, sans-serif;">sort<o:p></o:p></span></b></div></td><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">sort data</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><b><span style="font-family: Verdana, sans-serif;">who<o:p></o:p></span></b></div></td><td style="padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">list users currently logged in</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr></tbody></table>

  

  

  

[1]: http://2.bp.blogspot.com/--qut1SkmLZk/UpXqAVXotuI/AAAAAAAAAs8/e4_l533GQEw/s1600/redirection.png

