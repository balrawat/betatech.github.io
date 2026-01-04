---
layout: post
title: Process and Job control in Linux/Unix
date: '2013-11-27T18:44:00.001+05:30'
author: Balvinder Rawat
tags:
  - process control
  - Job control
modified_time: '2013-11-29T11:58:05.422+05:30'
thumbnail: >-
  https://1.bp.blogspot.com/-tw425JghJnA/UpXvXV76GjI/AAAAAAAAAtg/to6uV0fJ2bo/s72-c/job.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-1918029373346486506'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/11/process-and-job-control-in-linuxunix.html
---


![](https://1.bp.blogspot.com/-tw425JghJnA/UpXvXV76GjI/AAAAAAAAAtg/to6uV0fJ2bo/s400/job.png)

** Processes and Jobs**
-----------------------

A process is an executing program identified by a unique PID (process identifier). To see information about your processes, with their associated PID and status, type

## % ps

A process may be in the foreground, in the background, or be suspended. In general the shell does not return the UNIX prompt until the current process has finished executing.

Some processes take a long time to run and hold up the terminal. Backgrounding a long process has the effect that the UNIX prompt is returned immediately, and other tasks can be carried out while the original process continues executing.

### Running background processes

To background a process, type an**&**at the end of the command line. For example, the command**sleep**waits a given number of seconds before continuing. Type

## % sleep 10

This will wait 10 seconds before returning the command prompt %. Until the command prompt is returned, you can do nothing except wait.

To run sleep in the background, type

## % sleep 10 &

## \[1\] 6259

The**&**runs the job in the background and returns the prompt straight away, allowing you do run other programs while waiting for that one to finish.

The first line in the above example is typed in by the user; the next line, indicating job number and PID, is returned by the machine. The user is be notified of a job number (numbered from 1) enclosed in square brackets, together with a PID and is notified when a background process is finished. Backgrounding is useful for jobs which will take a long time to complete.

### Backgrounding a current foreground process

At the prompt, type

## % sleep 1000

You can suspend the process running in the foreground by typing**^Z**, i.e.hold down the \[**Ctrl**\] key and type \[**z**\]. Then to put it in the background, type

## % bg

Note: do not background programs that require user interaction e.g. vi

** Listing suspended and background processes**
-----------------------------------------------

When a process is running, backgrounded or suspended, it will be entered onto a list along with a job number. To examine this list, type

## % jobs

An example of a job list could be

## \[1\] Suspended sleep 1000

****\[2\] Running netscape****

****\[3\] Running matlab****

To restart (foreground) a suspended processes, type

## % fg %_jobnumber_

For example, to restart sleep 1000, type

## % fg %1

Typing**fg**with no job number foregrounds the last suspended process.

** Killing a process**
----------------------

### kill (terminate or signal a process)

It is sometimes necessary to kill a process (for example, when an executing program is in an infinite loop)

To kill a job running in the foreground, type**^C**(control c). For example, run

## % sleep 100

****^C****

To kill a suspended or background process, type

## % kill %_jobnumber_

For example, run

## % sleep 100 &

****% jobs****

If it is job number 4, type

## % kill %4

To check whether this has worked, examine the job list again to see if the process has been removed.

### ps (process status)

Alternatively, processes can be killed by finding their process numbers (PIDs) and using killPID_number

## % sleep 1000 &

****% ps****

## PID TT S TIME COMMAND

****20077 pts/5 S 0:05 sleep 1000****

****21563 pts/5 T 0:00 netscape**## 


## 21873 pts/5 S 0:25 nedit

**

To kill off the process**sleep 1000**, type

## % kill 20077

and then type**ps**again to see if it has been removed from the list.

If a process refuses to be killed, uses the**-9**option, i.e. type

## % kill -9 20077

Note: It is not possible to kill off other users' processes !!!

**Summary**
-----------

<table border="1" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="border: 1pt outset rgb(102, 102, 102); margin-left: 6.75pt; margin-right: 6.75pt; text-align: left;"><tbody><tr><td style="background: #ECE9D8; border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Command<o:p></o:p></span></span></b></div></td><td style="background: #ECE9D8; border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; text-align: center;"><b><span style="color: #444444;"><span style="font-family: Verdana, sans-serif;">Meaning<o:p></o:p></span></span></b></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">ls -lag<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">list access rights for all files</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">chmod [<var>options</var>]<span class="apple-converted-space">&nbsp;</span><var>file</var><o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">change access rights for named file</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><var><b>command</b></var><span class="apple-converted-space"><b>&nbsp;</b></span><b>&amp;<o:p></o:p></b></span></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">run command in background</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">^C<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">kill the job running in the foreground</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">^Z<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">suspend the job running in the foreground</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">bg<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">background the suspended job</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">jobs<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">list current jobs</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">fg %1<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">foreground job number 1</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">kill %1<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">kill job number 1</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">ps<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">list current processes</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr><tr><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><b><span style="font-family: Verdana, sans-serif;">kill 26152<o:p></o:p></span></b></div></td><td style="border: inset #666666 1.0pt; mso-border-alt: inset #666666 .75pt; padding: 3.75pt 3.75pt 3.75pt 3.75pt;"><div class="MsoNormal" style="line-height: 19.2pt; mso-element-anchor-horizontal: margin; mso-element-frame-hspace: 9.0pt; mso-element-left: center; mso-element-top: 28.5pt; mso-element-wrap: around; mso-element: frame; mso-height-rule: exactly;"><span style="font-family: Verdana, sans-serif;"><span style="color: #444444;">kill process number 26152</span><span style="color: #444444;"><o:p></o:p></span></span></div></td></tr></tbody></table>

[1]: https://1.bp.blogspot.com/-tw425JghJnA/UpXvXV76GjI/AAAAAAAAAtg/to6uV0fJ2bo/s1600/job.png

