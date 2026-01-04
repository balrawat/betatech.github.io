---
layout: post
title: printf bash command
date: '2013-11-27T17:47:00.000+05:30'
author: Balvinder Rawat
tags:
  - printf
  - bash
modified_time: '2013-11-28T13:50:45.291+05:30'
thumbnail: >-
  https://4.bp.blogspot.com/-CpnudH_9ne0/UpXiolEQjNI/AAAAAAAAAsg/PR1VTevpSAU/s72-c/printf.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-2663289629123986703'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/11/printf-bash-command.html'
---
[![](https://4.bp.blogspot.com/-CpnudH_9ne0/UpXiolEQjNI/AAAAAAAAAsg/PR1VTevpSAU/s1600/printf.png)][1]

  

  

When writing a bash scripts most of us by default use echo command as means to print to standard output stream. echo is easy to use and mostly it fits our needs without any problem. However, with simplicity very often comes limitation. This is also the case with echo command. Formatting an echo command output can be a nightmare and very often impossible task to do.

The solution to this can be a good old friend of all C/C++ the “printf” tool. printf can be just as easily implemented into a bash script is it is used with C/C++ programs. This article describes some basics of printf along with practical examples:

  

**Syntax**

printf accepts a FORMAT string and arguments in a following general form:

**_\# printf_**

In format prinft can have format specifiers, escape sequences or ordinary characters. When it comes to arguments it is usually text we would like to print to standard output stream. Let’s start with something simple from a bash shell command line:

**_          # printf “hello printf”_**

**_          hello printf#_**

At this point we have supplied and argument “hello”. Not the different behaviour in comparison to echo command. No new line had been printed out as it it in case of when using default setting of echo command. To print a new line we need to supply printf with format string with escape sequence \\n ( new line ):

**_          # printf “%s\\n” “hello printf”_**

**_          hello printf_**

The format string is applied to each argument:

**_          # printf “%s\\n” "hello printf" "in" "bash script"_**

**_          hello printf_**

**_          in_**

**_          bash script_**

  

### 1\. Format specifiers

As you could have seen in the previous simple examples we have used %s as a format specifier. The most commonly used printf specifiers are %s, %b, %d, %x and %f . The specifiers are replaced by a corresponding arguments. See the following example:

**_          # printf "%s\\t%s\\n" "1" "2 3" "4" "5"_**

**_1        2 3_**

**_4        5_**

In the example above we have supplied two specifiers %s to print TAB ( \\t ) and NEWLINE ( \\n ) to be used a s part of printf format string to print along with each argument. First \\t is applied to argument “1” and \\n is applied to argument “2 3”. If there are more arguments than specifiers the format string is reused until all arguments had been depleted. Specifier %s means to print all argument in literal form.

  

### 2\. Examples

As we have now covered the very basics let’s see some more printf examples: Instead of %s specifiers we can use %b specifier which is essentially the same by it allows us to interpret escape sequences with an argument:

**_          # printf "%s\\n" "1" "2" "\\n3"_**

**_          1_**

**_          2_**

**_          \\n3_**

**_          # printf "%b\\n" "1" "2" "\\n3"_**

**_          1_**

**_          2_**

**_          #_**

When it comes to printing a integers we can use %d specifier:

**_          # printf "%d\\n" 255 0xff 0377 3.5_**

**_          255_**

**_          255_**

**_          255_**

**_          Bash: printf: 3.5: invalid number_**

**_          3_**

As you can see %d specifiers refuses to print anything than integers. To printf floating point numbers a %f specifier is our friend:

**_          # printf "%f\\n" 255 0xff 0377 3.5_**

**_          255.000000_**

**_          255.000000_**

**_          377.000000_**

**_          3.500000_**

The default behaviour of %f printf specifier is to print floating point numbers with 6 decimal places. To limit a decimal places to 1 we can specify a precision in a following manner:

**_          # printf "%.1f\\n" 255 0xff 0377 3.5_**

**_          255.0_**

**_          255.0_**

**_          377.0_**

**_          3.5_**

Formatting to three places with preceding with 0:

**_          for i in $( seq 1 10 ); do printf "%03d\\t" "$i"; done_**

**_          001    002    003    004    005    006    007    008    009    010_**

Simple table. Format names to 7 places nad max 7 characters and format floating point number to 9 places with 2 decimals. More complicated sample script using printf formatting to create a table with multiple items. Save as a script make executable and run:

**_          #/bin/bash_**

**_divider===============================_**

**_divider=$divider$divider_**

**_header="\\n %-10s %8s %10s %11s\\n"_**

**_format=" %-10s %08d %10s %11.2f\\n"_**

**_width=43_**

**_printf "$header" "ITEM NAME" "ITEM ID" "COLOR" "PRICE"_**

**_printf "%$width.${width}s\\n" "$divider"_**

**_printf "$format" \_**

**_Triangle 13  red 20 \_**

**_Oval 204449 "dark blue" 65.656 \_**

**_Square 3145 orange .7_**

  

Output:

**_$ ./table_**

  

**_ ITEM NAME   ITEM ID      COLOR       PRICE_**

**_===========================================_**

**_ Triangle   00000013        red       20.00_**

**_ Oval       00204449  dark blue       65.66_**

**_ Square     00003145     orange        0.70_**

  

[1]: https://4.bp.blogspot.com/-CpnudH_9ne0/UpXiolEQjNI/AAAAAAAAAsg/PR1VTevpSAU/s1600/printf.png

