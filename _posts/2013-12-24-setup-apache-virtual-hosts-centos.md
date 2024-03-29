---
layout: post
title: Set Up Apache Virtual Hosts on CentOS 6
date: '2013-12-24T17:47:00.000+05:30'
author: Balvinder Rawat
tags:
  - centos6
  - apache
  - virtual host
imagefeature: apachevirtualhosts.png
modified_time: '2013-12-24T17:47:05.573+05:30'
thumbnail: >-
  http://1.bp.blogspot.com/-b4rAq0N4xzw/Url7KWx_7VI/AAAAAAAAAyQ/MpFcyAwQ52s/s72-c/apachevirtualhosts.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-4211693850535922778'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/12/setup-apache-virtual-hosts-centos.html'
---
[![](http://1.bp.blogspot.com/-b4rAq0N4xzw/Url7KWx_7VI/AAAAAAAAAyQ/MpFcyAwQ52s/s1600/apachevirtualhosts.png)][1]

**About Virtual Hosts**

* * *

Virtual Hosts are used to run more than one domain off of a single IP address. This is especially useful to people who need to run several sites off of one virtual private server. The sites display different information to the visitors, depending on with which the users accessed the site.There is no limit to the number of virtual hosts that can be added to a VPS.

  

  

  

**Set Up**

The steps in this tutorial require the user to have root privileges. You can see how to set that up in the[Initial Server Setup][2]in steps 3 and 4. Furthermore, if I reference the user in a step, I’ll use the name www. You can implement whatever username suits you.

  

Additionally, you need to have apache already installed and running on your virtual server 

If this is not the case, you can download it with this command:

  

_yum install httpd_

  

  

  

**Step One— Create a New Directory**

* * *

The first step in creating a virtual host is to a create a directory where we will keep the new website’s information.

  

This location will be your Document Root in the Apache virtual configuration file later on. By adding a -p to the line of code, the command automatically generates all the parents for the new directory.

  

_mkdir -p /var/www/example.com/public_html_

  

You will need to designate an actual DNS approved domain, or an IP address, to test that a virtual host is working. In this tutorial we will use example.com as a placeholder for a correct domain name.

  

However, should you want to use an unapproved domain name to test the process you will find information on how to make it work on your local computer in Step Six.

  

  

  

**Step Two—Grant Permissions**

* * *

We need to grant ownership of the directory to the user, instead of just keeping it on the root system.

_chown -R www:www /var/www/example.com/public_html_

  

Additionally, it is important to make sure that everyone will be able to read our new files.

  

_chmod 755 /var/www_

  

Now you are all done with permissions.

  

  

  

**Step Three— Create the Page**

* * *

We need to create a new file called index.html within our configurations directory.

_vi /var/www/example.com/public_html/index.html_

  

We can add some text to the file so we will have something to look at when the IP redirects to the virtual host.

  

_<html>_

_  <head>_

_    <title>www.example.com</title>_

_  </head>_

_  <body>_

_    <h1>Success: You Have Set Up a Virtual Host</h1>_

_  </body>_

_</html>_

  

Save and Exit

  

  

  

**Step Four—Turn on Virtual Hosts**

* * *

The next step is to enter into the apache configuration file itself.

_vi /etc/httpd/conf/httpd.conf_

  

There are a few lines to look for.

Make sure that your text matches what you see below.

  

_#Listen 12.34.56.78:80_

_Listen 80_

  

Scroll down to the very bottom of the document to the section called Virtual Hosts.

  

_NameVirtualHost *:80_

_#_

_\# NOTE: NameVirtualHost cannot be used without a port specifier_

_\# (e.g. :80) if mod_ssl is being used, due to the nature of the_

_\# SSL protocol._

_#   _

  

_#   _

_\# VirtualHost example:_

_\# Almost any Apache directive may go into a VirtualHost container._

_\# The first VirtualHost section is used for requests without a known_

_\# server name._

_#_

_<VirtualHost *:80>_

_     ServerAdmin webmaster@example.com_

_     DocumentRoot /var/www/example.com/public_html_

_     ServerName www.example.com_

_     ServerAlias example.com_

_     ErrorLog /var/www/example.com/error.log_

_     CustomLog /var/www/example.com/requests.log_

_</VirtualHost>_

  

The most important lines to focus on are the lines that say NameVirtualHost, Virtual Host, Document Root, and Server Name. Let’s take these one at a time.

  

\- Uncomment (remove the number sign) NameVirtualHost without making any changes. The star means that any IP address going through port 80 will be a virtual host. As your system probably only has one IP address this is not an issue—however, if you prefer, you can replace the star with your IP address.

  

\- You can leave the rest of the number marks in place until you reach the line <VirtualHost *:80> . Uncomment everything from there through <VirtualHost>.

  

\- Leave <VirtualHost *:80> as is—its details must match with those in the NameVirtual Host section. If you replaced the star with your IP address in that section, be sure to do the same here.

  

\- Document Root is key! For this section, write in the extension of the new directory created in Step One. If the document root is incorrect or absent you will not be able to set up the virtual host.

  

\- Server Name is another important piece of information, containing the virtual host’s domain name (eg. www.example.com). Make sure that you spell the domain out in full; we will put in any alternate possibilities in the next line.

  

\- ServerAlias is a new line in the config file that is not there by default. Adding it will allow you to list a few variants of the domain name, for example without the www in the front.

  

  

* * *

  

The rest of the lines in this section are not required to set up a virtual host. However, it is still helpful to know what they do.

  

\- Server admin asks for the webmaster’s email.

  

\- The Error Logs and Custom Logs keep track of any issues with the server. The error log covers issues that arise while maintaining the server, and the custom log tracks server requests. You can set up a custom location for these processes.

  

\- Make sure that <VirtualHost> is uncommented; then save and exit.

  

  

  

**Step Five—Restart Apache**

* * *

We’ve made a lot of the changes to the configuration. However, they will not take effect until Apache is restarted.

First stop all apache processes:

  

_apachectl -k stop_

  

Then start up apache once again.

  

_/etc/init.d/httpd start_

  

You may see the following error:

  

_Could not reliably determine the server's fully qualified domain name, using 127.0.0.1 for ServerName_

  

The message is just a warning, and you will be able to access your virtual host without any further issues.

  

  

  

**Optional Step Six—Setting Up the Local Hosts**

* * *

If you have pointed your domain name to your virtual private server’s IP address you can skip this step—you do not need to set up local hosts. Your virtual hosts should work. However, if want to try out your new virtual hosts without having to connect to an actual domain name, you can set up local hosts on your computer alone.

  

For this step, make sure you are on the computer itself, not your server. 

  

To proceed with this step you need to know your computer’s administrative password, otherwise you will be required to use an actual domain name to test the virtual hosts.

  

If you are on a Mac or Linux, access the root user (su) on the computer and open up your hosts file:

  

nano /etc/hosts

  

If you are on a Windows Computer, you can find the directions to alter the host file on the [Microsoft site][3]

  

You can add the local hosts details to this file, as seen in the example below. As long as that line is there, directing your browser toward, say, example.com will give you all the virtual host details for the corresponding IP address.

  

_\# Host Database_

_#_

_\# localhost is used to configure the loopback interface_

_\# when the system is booting.  Do not change this entry._

_##_

_127.0.0.1       localhost_

  

_#Virtual Hosts_

_12.34.56.789    www.example.com_

  

However, it may be a good idea to delete these made up addresses out of the local hosts folder when you are done to avoid any future confusion.

  

  

  

**Step Seven—RESULTS: See Your Virtual Host in Action**

* * *

Once you have finished setting up your virtual host, you can see how it looks online. Type your ip address into the browser (ie. http://12.34.56.789)

  

Good Job!

  

  

  

**Adding More Virtual Hosts**

* * *

To create additional virtual hosts, you can just repeat the process above, being careful to set up a new document root with the appropriate new domain name each time. Then just copy and paste the new Virtual Host information into the Apache Config file, as shown below

_<VirtualHost *:80>_

_     ServerAdmin webmaster@example.com_

_     DocumentRoot /var/www/example.com/public_html_

_     ServerName www.example.com_

_     ServerAlias example.com_

_     ErrorLog /etc/var/www/example.com/error.log_

_     CustomLog /var/www/example.com/requests.log_

_</VirtualHost>_

_<VirtualHost *:80>_

_     ServerAdmin webmaster@example.org_

_     DocumentRoot /var/www/example.org/public_html_

_     ServerName www.example.org_

_     ServerAlias example.org_

_     ErrorLog /var/www/example.org/error.log_

_     CustomLog /var/www/example.orgrequests.log_

_</VirtualHost>_

  

**See More:-**

  

Once you have set up your virtual hosts, you can proceed to[Create a SSL Certificate for your site][4]

  

[1]: http://1.bp.blogspot.com/-b4rAq0N4xzw/Url7KWx_7VI/AAAAAAAAAyQ/MpFcyAwQ52s/s1600/apachevirtualhosts.png
[2]: http://www.linuxtechtips.com/2013/12/steps-to-follow-after-linux-server-installation.html
[3]: http://support.microsoft.com/kb/923947
[4]: http://www.linuxtechtips.com/2013/12/create-ssl-certificate-for-apache-on-centos.html

