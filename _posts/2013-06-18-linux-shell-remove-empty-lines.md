---
layout: post
title: 'Linux : Shell Remove Empty Lines'
date: '2013-06-18T14:30:00.006+05:30'
author: Balvinder Rawat
tags:
  - linux commands
modified_time: '2013-08-06T16:34:03.050+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-8180752214360949651'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/06/linux-shell-remove-empty-lines.html'
---

Many time we face situations where we have many empty lines in a file or script. Then how can we delete only those empty lines & make the file compact?

I tried following steps & they worked like charm. 
for deleting all empty lines from the file input.txt, run the following command:

## sed command

                sed '/^$/d' input.txt > output.txt
        OR
sed -i '/^$/d' input.txt

## awk command

                awk 'NF > 0' input.txt > output.txt

