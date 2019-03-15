---
layout: post
title: 'Shell Script: Find Number Of Arguments Passed'
date: '2013-06-18T15:02:00.000+05:30'
author: Balvinder Rawat
tags:
  - shell scripting
modified_time: '2014-01-07T12:51:36.133+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-1960359858529303432'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/06/shell-script-find-number-of-arguments.html
---
  
Many times , when we create shell scripts we try to do repetitive tasks through functions. Some functions take arguments & we have to check the no. of arguments that are passed to it.  
  
Each bash shell function has the following set of shell variables:  

\[a\] All function parameters or arguments can be accessed via **$1, $2, $3,..., $N**.

\[b\] **$*** or **$@** holds all parameters or arguments passed to the function.

\[c\] **$#** holds the number of positional parameters passed to the function.

\[d\] An array variable called **FUNCNAME** ontains the names of all shell functions currently in the execution call stack.

Example
-------

Create a shell script as follows:

#!/bin/bash

\# Purpose: Demo bash function

\# -----------------------------

\## Define a function called test()

test(){

  echo "Function name:  ${FUNCNAME}"

  echo "The number of positional parameter : $#"

  echo "All parameters or arguments passed to the function: '$@'"

  echo

}

  

\## Call or invoke the function ##

\## Pass the parameters or arguments  ##

test linuxtechtips

test 1 2 3 4 5

test "this" "is" "a" "test"

  

**Run it as follows:**

$ chmod +x script.name.here

$ ./script.name.here

