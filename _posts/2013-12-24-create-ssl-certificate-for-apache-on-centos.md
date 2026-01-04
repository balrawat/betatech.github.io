---
layout: post
title: Create a SSL Certificate for Apache on CentOS 6
date: '2013-12-24T17:33:00.000+05:30'
author: Balvinder Rawat
tags:
  - centos
  - ssl
  - ssl certificate
  - secure web server
  - https
imagefeature: https.png
modified_time: '2013-12-24T17:33:21.440+05:30'
thumbnail: >-
  https://4.bp.blogspot.com/--423qayIOoI/Url318RK0UI/AAAAAAAAAyA/1hJ7-8pAsE8/s72-c/https.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-8075590793322239754'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/create-ssl-certificate-for-apache-on-centos.html
---
[![](https://4.bp.blogspot.com/--423qayIOoI/Url318RK0UI/AAAAAAAAAyA/1hJ7-8pAsE8/s1600/https.png)][1]

**About Self-Signed Certificates**

* * *

A SSL certificate is a way to encrypt a site's information and create a more secure connection. Additionally, the certificate can show the virtual private server's identification information to site visitors. Certificate Authorities can issue SSL certificates that verify the virtual server's details while a self-signed certificate has no 3rd party corroboration.

**Step One—Install Mod SSL**

* * *

In order to set up the self signed certificate, we first have to be sure that Apache and Mod SSL are installed on our VPS. You can install both with one command:

_yum install mod_ssl_

  

  

  

**Step Two—Create a New Directory**

* * *

Next, we need to create a new directory where we will store the server key and certificate

_mkdir /etc/httpd/ssl_

  

  

  

**Step Three—Create a Self Signed Certificate**

* * *

When we request a new certificate, we can specify how long the certificate should remain valid by changing the 365 to the number of days we prefer. As it stands this certificate will expire after one year.

_openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/httpd/ssl/apache.key -out /etc/httpd/ssl/apache.crt_

  

With this command, we will be both creating the self-signed SSL certificate and the server key that protects it, and placing both of them into the new directory.

  

This command will prompt terminal to display a lists of fields that need to be filled in.

  

The most important line is "Common Name". Enter your official domain name here or, if you don't have one yet, your site's IP address.

  

You are about to be asked to enter information that will be incorporated

into your certificate request.

What you are about to enter is what is called a Distinguished Name or a DN.

There are quite a few fields but you can leave some blank

For some fields there will be a default value,

If you enter '.', the field will be left blank.

\-\-\-\-\-

_Country Name (2 letter code) \[AU\]:US_

_State or Province Name (full name) \[Some-State\]:New York_

_Locality Name (eg, city) \[\]:NYC_

_Organization Name (eg, company) \[Internet Widgits Pty Ltd\]:Awesome Inc_

_Organizational Unit Name (eg, section) \[\]:Dept of Merriment_

_Common Name (e.g. server FQDN or YOUR name) \[\]:example.com                 _

_Email Address \[\]:webmaster@awesomeinc.com_

  

  

  

**Step Four—Set Up the Certificate**

* * *

Now we have all of the required components of the finished certificate.The next thing to do is to set up the virtual hosts to display the new certificate.

  

Open up the SSL config file:

  

_ vi /etc/httpd/conf.d/ssl.conf_

  

Find the section that begins with <VirtualHost \_default\_:443> and make some quick changes.

  

Uncomment the DocumentRoot and ServerName line and replace example.com with your DNS approved domain name or server IP address (it should be the same as the common name on the certificate):

  

_ ServerName example.com:443_

  

Find the following three lines, and make sure that they match the extensions below:

  

_SSLEngine on_

_SSLCertificateFile /etc/httpd/ssl/apache.crt_

_SSLCertificateKeyFile /etc/httpd/ssl/apache.key_

Your virtual host is now all set up! Save and Exit out of the file.

  

  

  

**Step Five—Restart Apache**

* * *

You are done. Restarting the Apache server will reload it with all of your changes in place.

_ /etc/init.d/httpd restart_

  

In your browser, type _**https://youraddress**_ to view the new certificate.

  

[1]: https://4.bp.blogspot.com/--423qayIOoI/Url318RK0UI/AAAAAAAAAyA/1hJ7-8pAsE8/s1600/https.png

