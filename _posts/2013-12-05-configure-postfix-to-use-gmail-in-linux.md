---
layout: post
title: Configure Postfix to use Gmail in RHEL/CentOS
date: '2013-12-05T17:14:00.002+05:30'
author: Balvinder Rawat
tags:
  - postfix relay
  - postfix
modified_time: '2013-12-05T17:14:56.840+05:30'
thumbnail: >-
  https://1.bp.blogspot.com/-nat9AcEDuFA/UqAPDw5sdlI/AAAAAAAAAvE/zrfTca78BSU/s72-c/postfix-gmail.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-6207264198744482713'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/configure-postfix-to-use-gmail-in-linux.html
---


![](https://1.bp.blogspot.com/-nat9AcEDuFA/UqAPDw5sdlI/AAAAAAAAAvE/zrfTca78BSU/s640/postfix-gmail.png)

Relaying to Gmail via smtp.gmail.com can be accomplished by configuring your Postfix with SASL authentication and TLS encryption.

The common errors you will encounter if sending from your postfix mail server failing to gmail.com domain but works in other domains are:

@/var/log/maillog

-Must issue a STARTTLS command first

- Certificate verification failed for gmail.com:unable to get local issuer certificate

-Authentication Required. Learn more at 530 5.5.1 https://mail.google.com/support/bin/answer.py?

How to fix?

Assuming you already installed Postfix and everything works fine except sending to gmail smtps, here are the steps to follow:

1\. Configure Postfix main configuration

a.vi /etc/postfix/main.cf

b. Add these lines:

smtp\_sasl\_security_options = noanonymous

relayhost = \[smtp.gmail.com\]:587

smtp\_use\_tls = yes

smtp\_tls\_CAfile = /etc/postfix/cacert.pem

smtp\_sasl\_auth_enable = yes

smtp\_sasl\_password_maps = hash:/etc/postfix/sasl/passwd

c. Save and exit

2\. Create /etc/postfix/sasl/passwd

a. Create a directory sasl under /etc/postfix and create a file passwd with contents below:

\[smtp.gmail.com\]:587 username@gmail.com:password

Save and exit

b. Change permission

#chmod 600 /etc/postfix/sasl/passwd

c. Create lookup table via postmap

#postmap /etc/postfix/sasl/passwd

Issuing that command will create passwd.db

3\. Generate your own CA certificate

a. Change directory to /etc/pki/tls/certs

#cd /etc/pki/tls/certs

b.Create a key and test certificate in one file

#make hostname.pem

You will something like

\[root@FLT certs\]# make hostname.pem

umask 77 ; \

PEM1=`/bin/mktemp /tmp/openssl.XXXXXX` ; \

PEM2=`/bin/mktemp /tmp/openssl.XXXXXX` ; \

/usr/bin/openssl req -utf8 -newkey rsa:1024 -keyout $PEM1 -nodes -x509 -days 365 -out $PEM2 -set_serial 0 ; \

cat $PEM1 >  hostname.pem ; \

echo “”    >> hostname.pem ; \

cat $PEM2 >> hostname.pem ; \

rm -f $PEM1 $PEM2

Generating a 1024 bit RSA private key

……………………….++++++

…..++++++

writing new private key to ‘/tmp/openssl.z12084′

—–

You are about to be asked to enter information that will be incorporated

into your certificate request.

What you are about to enter is what is called a Distinguished Name or a DN.

There are quite a few fields but you can leave some blank

For some fields there will be a default value,

If you enter ‘.’, the field will be left blank.

—–

Country Name (2 letter code) \[GB\]:

State or Province Name (full name) \[Berkshire\]:

Locality Name (eg, city) \[Newbury\]:

Organization Name (eg, company) \[My Company Ltd\]:

Organizational Unit Name (eg, section) \[\]:

Common Name (eg, your name or your server’s hostname) \[\]:

Email Address \[\]:

c. Fill-up the necessary information and copy the file on /etc/postfix as cacert.pem

#cp /etc/pki/tls/certs/hostname.pem /etc/postfix/cacert.pem

4\. Restart the postfix service

#service postfix restart

5\. Inspect now your postfix logs to see if it can send out mails now to gmail servers

A successful message states something like

May  3 17:35:00 FLT postfix/smtp\[28244\]: 0ABB61CE32A: to=<linuxtechtips-tutorials@gmail.com>, relay=smtp.gmail.com\[74.125.93.109\]:587, delay=5, delays=0.41/0.02/2.7/1.8, dsn=2.0.0, status=sent (250 2.0.0 OK 1272879300 8sm8902550qwj.38)

[1]: https://1.bp.blogspot.com/-nat9AcEDuFA/UqAPDw5sdlI/AAAAAAAAAvE/zrfTca78BSU/s1600/postfix-gmail.png

