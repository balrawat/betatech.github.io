---
layout: post
title: Passwordless SSH logins
date: '2013-06-16T11:35:00.000+05:30'
author: Balvinder Rawat
tags:
  - SSH
modified_time: '2014-01-07T12:51:48.702+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-6123680090074943275'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/06/passwordless-ssh-logins.html'
---

There are a few cases where having passwordless access to a machine is quite convenient or necessary. I'm looking up for commands that I can just copy and paste to do it right quick. Below are the steps:-

## 1\. Generate key pair:-

       One of the login modes of SSH is to use a SSH key based authentication. A key pair is made up of both a private and a public key. The private key is kept on your local machine very securely while your public key is what you distribute to all the machines you want to log in to. There are a few flavors of keys you can generate, rsa1 (for SSH1), dsa (SSH2), or rsa (SSH2). Most linux admins like DSA. You can (and should) associate a password with your key pair, so that only you can use it even if someone else manages to gain access to your account. Password for key is not recommened when you want to use it for daily tasks or tasks that are done through cron jobs. If you have more than one key pair, using the same password for all key pairs will make them all active at the same time. You can also vary the number of bits used for the key. The more bits you use the harder it will be to crack, but I believe at a nominal performance drop. I was recommended to use 2048 bits. Very well, 2048 bit DSA key it is

ssh-keygen -t dsa -b 2048
\# Type in strong password or no password when you don't want any password prompt.

If for some reason you need an rsa key, you can just replace the type with the appropiate argument, -t rsa or -t rsa1.

NOTE: You need to make sure the permissions of the files in this directory are set to allow read/write for the user only (-rw------- or chmod 600 *). The most important files to do this for are the authorized_keys and private keys files. Sometimes logging in will silently fail if you don't have the permissions set correctly.


## 2\. Copy public key to remote machine:-

    Once you made your key pair, you should copy your public key to the remote machine and add it to the remote user's .ssh/authorized_keys file. There are several ways to do this. The easiest one is using the ssh-copy-id command:-

    ssh-copy-id -i ~/.ssh/id_rsa.pub remote-user@remote-host

You can also use below command:-

cat ~/.ssh/id\`dsa.pub | ssh user@remote.machine.com 'cat >> .ssh/authorized\`keys'

or you can manually transfer the pub file to remote machine & put it inside the authorized_keys of remote user.


## 3\.  Login to remote server:-

    As the public key is copied now. We can just login & check if its working:-

    ssh remote-user@remote-host

   It should take you to remote host without asking for password ( if you've not provided any password with key )


It is recommended that once you have the ability to log in remotely as root with keys, you should disable password-based logins via ssh by making sure the following line is in /etc/ssh/sshd_config:-

PermitRootLogin   without-password

