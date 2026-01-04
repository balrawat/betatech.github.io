---
layout: post
title: Working with Regular Expressions
date: '2013-12-10T12:52:00.000+05:30'
author: Balvinder Rawat
tags:
  - regex
  - regular expressions
  - shell
modified_time: '2013-12-10T12:54:12.635+05:30'
thumbnail: >-
  https://1.bp.blogspot.com/-TSttgbtVw3A/UqbA2X7aGcI/AAAAAAAAAvs/Y-GsqsP_hUA/s72-c/regex.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-3977219890417873051'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/12/working-with-regular-expressions.html'
---
![](https://1.bp.blogspot.com/-TSttgbtVw3A/UqbA2X7aGcI/AAAAAAAAAvs/Y-GsqsP_hUA/s640/regex.png)

## Introduction

Regular expressions are a way of manipulating text by using character strings and metacharacters. They are often used by programmers, but can also be used in shell commands and in some programs (e.g. vi and other text editors). The examples that follow are mainly based upon the regular expression format used by perl. They are also the same as those available in PHP using the preg regular expression functions. Some programs / languages may use different syntax or meta-characters but the general concept is the same.

## Getting started

Regular expressions can initially be compared with wild-characters that you may already be familiar with, but regular expressions are much more powerful. For example most people are familiar with the ? and * when used on the command line to mean: match any single character, and match any number of characters, respectively.

To match a using a regular expression the expression is first contained within forward slashes. For example:

/Linux/ would match on the word Linux, which could occur anywhere in the string being tested.

Note that whilst the use of forward slashes is most common it is often possible to replace these with any other single character. This is useful if using a path name or url that contains slashes that would otherwise need to be escaped.

## Replacing characters or strings

Regular Expressions are often used to find and replace text so the example:

s/Linux/UNIX/

would replace the word Linux with UNIX (useful if you wanted to convert some documentation to a more generic UNIX reference rather than restricting to Linux. The "s" means substitute, in the match earlier there is an implied "m" character meaning match. Depending upon the program / language being used you may or may not need to include the "s" or "m" characters.

## Modifiers and special characters

There are also a number of modifiers that can be added to the end of the regular expression. The two most common are:

**g##  which means match globally, ie. replace all occurrences in the string rather than stopping after the first one (which is probably what we really wanted for the ealier example).


**i##  means ignore case (or perform a case-insensitive match).


So our earlier example could become:

s/Linux/UNIX/gi

to replace for all occurrences regardless of case.

The above examples are nothing more than a basic find and replace, but the real power of regular expressions is when you include meta-characters and other special commands. Some metacharacters are:

**\**Escape the character following it (ie. ignore special properties of the following character)

**.##  Match any single character except new line


**^** Match at the beginning of the string, or if the first character in square brackets matches elements not in the list

****

**$** Match at the end of the string

****

***** Match the preceding element 0 or more times

****

**?** Match the preceding element 0 or 1 time

****

**{...}** Range of occurrences for the preceding element

****

**\[...\]** Match any of the characters between the brackets

****

**(...)** Groups regular expressions often leaves values in $x - where x is the number of the bracket pair (staring at 1)

****

**|##  Matches either the preceding or following character/expression


There are also some escape sequences / character classes that can be used:

**\\n**Newline

**\\r##  Carriage return


**\\t** Tab

****

**\\f** Formfeed

****

**\\d** Match a digit e.g. \[0-9\]

****

**\\D** Match a non-digit e.g. \[^0-9\]

****

**\\w** Match a word character (alphanumeric) e.g. \[a-zA-Z_0-9\]

****

**\\W** Match a non-word character e.g. \[^a-zA-Z_0-9\]

****

**\\s** Match a whitespace character e.g. \[ \\t\\n\\r\\f\]

****

**\\S##  Match a non-whitespace character e.g. \[^ \\t\\n\\r\\f\]


When using square brackets, some characters can have different meanings depending on whether they are inside our outside the brackets. A period '.' outside the brackets will match on any character, but inside will only match on a period character.

## Examples

/\[df\]og/ Matches dog or fog

/^The/ Matches "The" if it is at the beginning of the string

/^The end$/ Matches "The end" if that is the entire string

/The\\s*end/ Matches "The end" and "The        end" but not "The - end"

/The.*end/ Matches "The end" as well as "The book will soon be coming to an end."

[1]: https://1.bp.blogspot.com/-TSttgbtVw3A/UqbA2X7aGcI/AAAAAAAAAvs/Y-GsqsP_hUA/s1600/regex.png

