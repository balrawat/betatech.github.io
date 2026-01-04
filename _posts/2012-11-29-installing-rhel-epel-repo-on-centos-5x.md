---
layout: post
title: Installing RHEL EPEL Repo on Centos 5.x or 6.x
date: '2012-11-29T16:33:00.003+05:30'
author: Balvinder Rawat
tags:
  - centos
  - additional repos
modified_time: '2014-01-07T12:54:34.380+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-1029079533370199136'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2012/11/installing-rhel-epel-repo-on-centos-5x.html
---
How to install RHEL EPEL repository on Centos 5.x or 6.x
--------------------------------------------------------

The following article will article CentOS 5.x-based or Centos 6.x-based  system using Fedora Epel repos, and the third party**remi**package repos. These package repositories are not officially supported by CentOS, but they provide much more current versions of popular applications like PHP or MYSQL.

### Install the extra repositories

The first step requires downloading some RPM files that contain the additional YUM repository definitions.

****Centos 5.x****

**wget https://dl.fedoraproject.org/pub/epel/5/i386/epel-release-5-4.noarch.rpm
wget https://rpms.famillecollet.com/enterprise/remi-release-5.rpm
sudo rpm -Uvh remi-release-5*.rpm epel-release-5*.rpm **

## Centos 6.x

**wget https://dl.fedoraproject.org/pub/epel/6/x86_64/epel-release-6-8.noarch.rpm
wget https://rpms.famillecollet.com/enterprise/remi-release-6.rpm
sudo rpm -Uvh remi-release-6*.rpm epel-release-6*.rpm**

Once installed you should see some additional repo definitions under the_/etc/yum.repos.d_directory.

**$ ls -1 /etc/yum.repos.d/epel* /etc/yum.repos.d/remi.repo
/etc/yum.repos.d/epel.repo
/etc/yum.repos.d/epel-testing.repo
/etc/yum.repos.d/remi.repo**

## Enable the remi repository

The remi repository provides a variety of up-to-date packages that are useful or are a requirement for many popular web-based services.  That means it generally is not a bad idea to enable the remi repositories by default.

First, open the_/etc/yum.repos.d/remi.repo_repository file using a text editor of your choice:

sudo vim /etc/yum.repos.d/remi.repo

Edit the**\[remi\]**portion of the file so that the_enabled_option is set to_1_.  This will enable the remi repository.

## name=Les RPM de remi pour Enterprise Linux $releasever - $basearch
#baseurl=https://rpms.famillecollet.com/enterprise/$releasever/remi/$basearch/
mirrorlist=https://rpms.famillecollet.com/enterprise/$releasever/remi/mirror
enabled=1
gpgcheck=1
gpgkey=file:///etc/pki/rpm-gpg/RPM-GPG-KEY-remi
failovermethod=priority

You will now have a larger array of yum repositories to install from.

_============_

_Credits:_

_============_

_This article is taken from https://www.rackspace.com/knowledge_center/article/installing-rhel-epel-repo-on-centos-5x-or-6x_

