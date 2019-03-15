---
layout: post
title: WebDAV server setup on Ubuntu Linux
date: '2013-11-18T12:38:00.000+05:30'
author: Balvinder Rawat
tags:
  - webdav
modified_time: '2013-11-18T12:38:19.081+05:30'
thumbnail: >-
  http://3.bp.blogspot.com/-87Bo082dbUc/Uom8XNFQRUI/AAAAAAAAAo8/s1M-XuBrPVU/s72-c/webdav.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-4324152554104798052'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/11/webdav-server-setup-ubuntu.html'
---
[![](http://3.bp.blogspot.com/-87Bo082dbUc/Uom8XNFQRUI/AAAAAAAAAo8/s1M-XuBrPVU/s1600/webdav.png)][1]

**1. Introduction**

This article will deal with installation and configuration of WebDAV server on Ubuntu Linux. WebDAV stands for Web Distributed Authoring and Versioning and allows connected users the edit and share data online via the HTTP protocol. This makes WebDAV a popular choice for developers when combined, for example, with Subversion or OpenLink Virtuoso. WebDAV is supported by number of clients ranging from davfs2, which makes it possible to mount the WebDAV's data storage to include into the local filesystem. This can be done with the mount command to various GUI applications with the native WebDAV support such as Nautilus, konqueror, etc. Futhermore, in this guide we will combine WebDAV with the Apache2 server.

**2. Scenario**

In this section I would like to describe a scenario used in this tutorial. WebDAV can be very flexible service, which allows for number of configuration settings and scenarios. In this WebDAV tutorial we will start with the simplest basic startup WedDAV configuration and from there we will build it up to fit more complex environment. You can think of WebDAV as a HTTP extension for your existing website configuration. Normally, you may already have your apache website up and running. Thus, in that case, all you need to do to in order to include the WevbDAV service is to:

1.create additional upload data directory to use by WebDAV

2.configure your existing apache2 virtual host file

However, in this guide we will start from scratch starting from apache2 installation, virtual host creation, etc. Therefore, feel free to skip to any section most appropriate to your configuration requirement.

In this guide we will configure:

·webdav.local - this will be a virtual host running on IP 10.1.1.61 server

·webdav.local/svn - this will be a WebDAV enabled directory

·/var/www/webdav - directory to host webdav.local's index file

·/var/www/webdav/svn - directory to host webdav.local/svn WebDAV's data storage

Edit your DNS settings accordingly or alter your client's /etc/hosts file to include the above host webdav.local resolution.

**3. Apache and WebDAV installation**

In this section we will simply install apache2 and enable WebDAV module. WebDAV module comes with apache2 installation, however, it is not enabled by default. All of this can be done with two simple commands:

$ sudo apt-get install apache2

By now your should be able to access your default website located at http://webdav.local. If all goes well disable the default page as we no longer have use for it:

$ sudo a2dissite default

  

$ sudo service apache2 reload

**4. Configure virtual host**

At this point we need to configure the virtual host with ServerName: webdav.local and the attached directory /var/www/webdav. To do so navigate to /etc/apache2/sites-available/:

$ cd /etc/apache2/sites-available/

and create a new site configuration file called webdav.local with the following content:

<VirtualHost *:80>

        ServerAdmin webmaster@localhost

  

        Servername webdav.local

  

  

        DocumentRoot /var/www/webdav

        <Directory />

                Options FollowSymLinks

                AllowOverride None

        </Directory>

        <Directory /var/www/webdav/>

                Options Indexes FollowSymLinks MultiViews

                AllowOverride None

                Order allow,deny

                allow from all

        </Directory>

</VirtualHost>

Once done we need to create an appropriate /var/www/webdav/ directory:

$ sudo mkdir /var/www/webdav

Change owner to apache:

$ sudo chown www-data.www-data /var/www/webdav

and enable out new site webdav.local

$ sudo a2ensite webdav.local

To test it we can create some simple index.html file:

$ sudo sh -c 'echo "Welcome from WebDAV.local" > /var/www/webdav/index.html'

and finally reload apache2 webserver:

$ sudo service apache2 reload

Now you should be able to navigate your browser to http://webdav.local and see the message: Welcome from WebDAV.local on your screen. This concludes the installation of the apache2 webserver with virtual host webdav.local

**5. WebDAV setup**

It is time to enable WebDAV's module with:

$ sudo a2enmod dav_fs

  

Considering dependency dav for dav_fs:

  

Enabling module dav.

Enabling module dav_fs.

and restart apache server:

$ sudo service apache2 restart

Now that everything is ready we can setup a basic WebDAV server. This can be easily done by creating an additional directory to hold WebDAV data:

**5.1. Basic Configuration**

$ sudo mkdir /var/www/webdav/svn

It is also important to make it writable by apache otherwise we get 403 Forbidden error:

$ sudo chown www-data.www-data /var/www/webdav/svn/

and enabling WebDAV for our new virtual host webdav.local. This can be done by adding the following lines into <VirtualHost> block:

Alias /svn /var/www/webdav/svn

  

<Location /svn>

  

    DAV On

</Location>

What the above meas is that WebDAV enabled directory /var/www/webdav/svn which will be accessible via http://webdav.local/svn. Do the above modification of your existing /etc/apache2/sites-available/webdav.local config file and restart your apache web server. Here is how the entire /etc/apache2/sites-available/webdav.local file looks like at this stage:

<VirtualHost *:80>

        ServerAdmin webmaster@localhost

  

        Servername webdav.local

  

  

        DocumentRoot /var/www/webdav

        <Directory />

                Options FollowSymLinks

                AllowOverride None

        </Directory>

        <Directory /var/www/webdav/>

                Options Indexes FollowSymLinks MultiViews

                AllowOverride None

                Order allow,deny

                allow from all

        </Directory>

  

Alias /svn /var/www/webdav/svn

<Location /svn>

    DAV On

</Location>

  

</VirtualHost>

It is time to test our configuration. One way to do this is to point our browser to http://webdav.local/svn or even better way is to use the cadaver tool. First install cadaver with:

$ sudo apt-get install cadaver

Create same data file with dd to be uploaded to your WebDAV directory and upload it:

$** dd if=/dev/zero of=mydata.dat bs=1M count=10**

  

10+0 records in

  

10+0 records out

10485760 bytes (10 MB) copied, 0.075726 s, 138 MB/s

$** cadaver http://webdav.local/svn**

dav:/svn/>** put mydata.dat**

Uploading mydata.dat to `/svn/mydata.dat':

Progress: \[=============================>\] 100.0% of 10485760 bytes succeeded.

dav:/svn/> **quit**

Connection to `webdav.local' closed.

Now you should have the basic WebDAV server configured and ready to use. In the next section we will add some basic user authentication.

**5.2. WebDAV with user authentication**

If you intend to deploy your WebDAV server on a remote host it is more than advisable to implement at least some basic authentication. Fortunately, this can be easily done using the **htpasswd** command and reconfiguring our existing /etc/apache2/sites-available/webdav.local config file.

First create a directory where you wish to store the webdav's password file. This is a location of your choice. In this tutorial I use  /usr/local/apache2/:

$ sudo mkdir /usr/local/apache2/

Then, use htpasswd to create a new password file against which all users will be authenticated. 

$ sudo htpasswd -c /usr/local/apache2/webdav.passwords lubos

If you need to add more users use the above syntax but omit -c option as it will overwrite your existing file.

  

Now that the authentication file is ready, we need to add authentication to our current /etc/apache2/sites-available/webdav.local config file. New changes are highlighted with the bold font:

  

<VirtualHost *:80>

        ServerAdmin webmaster@localhost

  

        Servername webdav.local

  

  

        DocumentRoot /var/www/webdav

        <Directory />

                Options FollowSymLinks

                AllowOverride None

        </Directory>

        <Directory /var/www/webdav/>

                Options Indexes FollowSymLinks MultiViews

                AllowOverride None

                Order allow,deny

                allow from all

        </Directory>

  

Alias /svn /var/www/webdav/svn

<Location /svn>

    DAV On

** AuthType Basic**

**

**        AuthName "webdav"**

****

**        AuthUserFile /usr/local/apache2/webdav.passwords**

****

**        Require valid-user**

**

</Location>

  

</VirtualHost>

From now on if you try to access your WebDAV server your will need to authenticate yourself first. Here is a WebDAV authentication example:

$ **cadaver http://webdav.local/svn**

  

Authentication required for webdav on server `webdav.local':

  

Username: lubos

Password: 

dav:/svn/> **ls**

Listing collection `/svn/': succeeded.

        mydata.dat                      10485760  Feb 20 14:45

dav:/svn/>

**5.3. Limiting WebDAV access**

Furthermore, it is advisable to limit WebDAV access to a limited number of users. For example, if we want to let only sinlge user "Lubos" access our WebDAV repository we can do so by adding  a <Limit> clause inside the <Location> directive such as:

    <Limit PUT POST DELETE PROPFIND PROPPATCH MKCOL COPY MOVE LOCK UNLOCK>

  

        AuthType Basic

  

        AuthName "webdav"

        AuthUserFile /usr/local/apache2/webdav.passwords

        Require user lubos

    </Limit>

Since the users can access and upload file to any WebDAV enabled directory it is also recommended to disallow .httaccess file. Therefore, add:

AllowOverride None

inside the <Location> directive.

**6. Mounting WebDAV enabled directory**

As it was already mentioned before WebDAV is supported by large number of clients. It is also possible to mount the WebDAV directory into a local system to act as a part of the filesystem. To do so we first need to install davfs2 as a root user:

\# apt-get install davfs2

then create a mount point:

\# mkdir /mnt/webdav

and finally mount it with a mount command:

  

  

# **mount.davfs http://webdav.local/svn /mnt/webdav/**

  

Please enter the username to authenticate with server

http://webdav.local/svn or hit enter for none.

  Username: **lubos**

Please enter the password to authenticate user lubos with server

http://webdav.local/svn or hit enter for none.

  Password:  

# **cd /mnt/webdav/**

# **ls**

lost+found  mydata.dat

# **touch linuxtechtips.com.txt**

# **sync**

**7. Conclusion**

This article described a basic configuration of WebDAV service using Apache2 webserver to get you started. There are few security issues to be considered so you need to do your homework and consult[Apache Module mod_dav][2]for more configuration settings and security enhancements to improve you configuration.

  

  

  

[1]: http://3.bp.blogspot.com/-87Bo082dbUc/Uom8XNFQRUI/AAAAAAAAAo8/s1M-XuBrPVU/s1600/webdav.png
[2]: http://httpd.apache.org/docs/2.2/mod/mod_dav.html "apache module mod_dav"

