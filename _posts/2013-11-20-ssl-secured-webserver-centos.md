---
layout: post
title: Setting up an SSL secured Webserver with CentOS
date: '2013-11-20T10:31:00.001+05:30'
author: Balvinder Rawat
tags:
  - ssl
  - http
  - apache
  - https
modified_time: '2013-11-20T10:31:41.809+05:30'
thumbnail: >-
  http://4.bp.blogspot.com/-zmAUfh-AZJs/Uom_Z1RP5RI/AAAAAAAAApU/8qsZwX1JwBk/s72-c/https.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-7343155710483564998'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/11/ssl-secured-webserver-centos.html'
---
[![](http://4.bp.blogspot.com/-zmAUfh-AZJs/Uom_Z1RP5RI/AAAAAAAAApU/8qsZwX1JwBk/s1600/https.png)][1]

  

This guide will explain how to set up a site over https. The tutorial uses a self signed key so will work well for a personal website or testing purposes. This is provided as is so proceed at your own risk and take backups!

**1\. Getting the required software**

For an SSL encrypted web server you will need a few things. Depending on your install you may or may not have OpenSSL and mod_ssl, Apache's interface to OpenSSL.Use yum to get them if you need them.

yum install mod_ssl openssl

Yum will either tell you they are installed or will install them for you.

**2\. Generate a self-signed certificate**

Using OpenSSL we will generate a self-signed certificate. If you are using this on a production server you are probably likely to want a key from Trusted Certificate Authority, but if you are just using this on a personal site or for testing purposes a self-signed certificate is fine. To create the key you will need to be root so you can either su to root or use sudo in front of the commands

\# Generate private key

openssl genrsa -out ca.key 1024

  

\# Generate CSR

openssl req -new -key ca.key -out ca.csr

  

\# Generate Self Signed Key

openssl x509 -req -days 365 -in ca.csr -signkey ca.key -out ca.crt

  

\# Copy the files to the correct locations

cp ca.crt /etc/pki/tls/certs

cp ca.key /etc/pki/tls/private/ca.key

cp ca.csr /etc/pki/tls/private/ca.csr

<table border="0" cellpadding="0" cellspacing="0" class="MsoNormalTable" style="border-collapse: collapse; margin-left: 12pt; text-align: justify;"><tbody><tr><td style="background: #FFECEC; border-left: none; border: solid #E0B7B7 1.0pt; mso-border-bottom-alt: solid #E0B7B7 .75pt; mso-border-right-alt: solid #E0B7B7 .75pt; mso-border-top-alt: solid #E0B7B7 .75pt; padding: 12.0pt 12.0pt 12.0pt 6.0pt; width: 451.35pt;" width="602"><div class="MsoNormal" style="line-height: 18.0pt; mso-margin-bottom-alt: auto; mso-margin-top-alt: auto;"><span style="font-family: Verdana, sans-serif;"><b><span style="font-size: 12pt;">WARNING:</span></b><span style="font-size: 12pt;">&nbsp;Make sure that you&nbsp;<b>copy</b>&nbsp;the files and do not&nbsp;<b>move</b>&nbsp;them if you use SELinux. Apache will complain about missing certificate files otherwise, as it cannot read them because the certificate files do not have the right SELinux context.<o:p></o:p></span></span></div></td></tr></tbody></table>

If you have moved the files and not copied them, you can use the following command to correct the SELinux contexts on those files, as the correct context definitions for /etc/pki/* come with the bundled SELinux policy.

restorecon -RvF /etc/pki

Then we need to update the Apache SSL configuration file

vi +/SSLCertificateFile /etc/httpd/conf.d/ssl.conf

Change the paths to match where the Key file is stored. If you've used the method above it will be

SSLCertificateFile /etc/pki/tls/certs/ca.crt

Then set the correct path for the Certificate Key File a few lines below. If you've followed the instructions above it is:

SSLCertificateKeyFile /etc/pki/tls/private/ca.key

Quit and save the file and then restart Apache

/etc/init.d/httpd restart

All being well you should now be able to connect over https to your server and see a default Centos page. As the certificate is self signed browsers will generally ask you whether you want to accept the certificate. Firefox 3 won't let you connect at all but you can override this.

**3\. Setting up the virtual hosts**

Just as you set[VirtualHosts][2]for http on port 80 so you do for https on port 443. A typical[VirtualHost][3]for a site on port 80 looks like this

<VirtualHost *:80>

        <Directory /var/www/vhosts/yoursite.com/httpdocs>

        AllowOverride All

        </Directory>

        DocumentRoot /var/www/vhosts/yoursite.com/httpdocs

        ServerName yoursite.com

</VirtualHost>

To add a sister site on port 443 you need to add the following at the top of your file

NameVirtualHost *:443

and then a[VirtualHost][4]record something like this:

<VirtualHost *:443>

        SSLEngine on

        SSLCertificateFile /etc/pki/tls/certs/ca.crt

        SSLCertificateKeyFile /etc/pki/tls/private/ca.key

        <Directory /var/www/vhosts/yoursite.com/httpsdocs>

        AllowOverride All

        </Directory>

        DocumentRoot /var/www/vhosts/yoursite.com/httpsdocs

        ServerName yoursite.com

</VirtualHost>

Restart Apache again using

/etc/init.d/httpd restart

**4\. Configuring the firewall**

You should now have a site working over https using a self-signed certificate. If you can't connect you may need to open the port on your firewall. To do this amend your iptables rules:

iptables -A INPUT -p tcp --dport 443 -j ACCEPT

/sbin/service iptables save

iptables -L -v

  

  

[1]: http://4.bp.blogspot.com/-zmAUfh-AZJs/Uom_Z1RP5RI/AAAAAAAAApU/8qsZwX1JwBk/s1600/https.png
[2]: http://wiki.centos.org/VirtualHosts
[3]: http://wiki.centos.org/VirtualHost
[4]: http://wiki.centos.org/VirtualHost

