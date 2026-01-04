---
layout: post
title: How To Install Joomla on a linux Server Running Ubuntu
date: '2013-12-11T18:47:00.002+05:30'
author: Balvinder Rawat
tags:
  - lampp
  - joomla
  - apache
modified_time: '2013-12-11T18:47:56.863+05:30'
thumbnail: >-
  https://1.bp.blogspot.com/-DWK0XXQbCU4/Uqhlw8CTytI/AAAAAAAAAxA/7vqklV6UrRY/s72-c/joomla_on_ubuntu.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-3146657468563563069'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/how-to-install-joomla-on-ubuntu-linux.html
---
![](https://1.bp.blogspot.com/-DWK0XXQbCU4/Uqhlw8CTytI/AAAAAAAAAxA/7vqklV6UrRY/s640/joomla_on_ubuntu.png)

### About Joomla

* * *

Joomla is a free and open source content management that uses a PHP and a backend database, such as MySQL. It offers a wide variety of features that make it an incredibly flexible content management system right out of the box. It was created in 2005 and is currently the 2nd most popular content management site online. It now has over 10,000 addons to customize its functionality.

Setup
-----

* * *

The steps in this tutorial require the user to have root privileges on their linux server. You can see how to set that up in steps 3 and 4 of [the Initial Server Setup] the Initial Server Setup

Before working with Joomla, you need to have LAMP installed on your linux server. If you don't have the Linux, Apache, MySQL, PHP stack on your linux server, you can find the tutorial for setting it up here:[How to Install LAMP on Ubuntu] How to Install LAMP on Ubuntu.

Once you have the user and required software, you can start installing Joomla!

Step One—Download Joomla
------------------------

* * *

To start, create a directory where you will keep your Joomla files temporarily:

`# mkdir temp`

Switch into the directory:

`# cd temp`

Then you can go ahead and download the most recent version of Joomla straight from their [website] website. Currently, the latest version is 2.5.7.

`# wget https://joomlacode.org/gf/download/frsrelease/17410/76021/Joomla\`2.5.7-Stable-Full\_Package.tar.gz_

This command will download the zipped Joomla package straight to your user's home directory on the linux server. You can untar it with the following command, moving it straight into the default apache directory, /var/www :

`# sudo tar zxvf Joomla\`2.5.7-Stable-Full\`Package.tar.gz  -C /var/www`

## Step Two—Configure the Settings

Once the Joomla files are in the web directory, we alter a couple of permissions to give access to the Joomla installer. First create a Joomla configuration file and make it temporarily world-writeable:

```bash
# sudo touch /var/www/configuration.php
# sudo chmod 777 /var/www/configuration.php
```
After the installation is complete, we will change the permissions back down to 755, which will make it only writeable by the owner.

## Step Three—Create the Joomla Database and User

Now we need to switch gears for a moment and create a new MySQL directory for Joomla.

Go ahead and log into the MySQL Shell:

```bash
\# mysql -u root -p
```

Login using your MySQL root password. We then need to create the Joomla database, a user in that database, and give that user a new password. Keep in mind that all MySQL commands must end with semi-colon.

First, let's make the database (I'm calling mine Joomla for simplicity's sake—for a real server, however, this name is not very secure). Feel free to give it whatever name you choose:

_CREATE DATABASE joomla;_

_Query OK, 1 row affected (0.00 sec)_

Then we need to create the new user. You can replace the database, name, and password, with whatever you prefer:

_CREATE USER juser@localhost;_

_Query OK, 0 rows affected (0.00 sec)_

Set the password for your new user:

_SET PASSWORD FOR juser@localhost= PASSWORD("password");_

_Query OK, 0 rows affected (0.00 sec)_

Finish up by granting all privileges to the new user. Without this command, the Joomla installer will be able to harness the new mysql user to create the required tables:

_GRANT ALL PRIVILEGES ON joomla.* TO juser@localhost IDENTIFIED BY 'password';_

_Query OK, 0 rows affected (0.00 sec)_

Then refresh MySQL:

_FLUSH PRIVILEGES;_

_Query OK, 0 rows affected (0.00 sec)_

Exit out of the MySQL shell:

_exit_

Restart apache:

`# sudo service apache2 restart`

## Step Four—Access the Joomla Installer

Once you have placed the Joomla files in the correct location on your linux server, assigned the proper permissions, and set up the MySQL database and username, you can complete the remaining steps in your browser.

Access the Joomla installer going to your domain name or IP address. (eg. Example.com)

Once you have finished going through the installer, delete the installation folder per Joomla’s instructions and change the permissions on the config file:

```bash
# sudo rm -rf /var/www/installation/
# sudo chmod 755 /var/www/configuration.php
```
Visit your domain or IP address to see your new Joomla page

[1]: https://1.bp.blogspot.com/-DWK0XXQbCU4/Uqhlw8CTytI/AAAAAAAAAxA/7vqklV6UrRY/s1600/joomla_on_ubuntu.png
[2]: https://www.linuxtechtips.com/2013/12/steps-to-follow-after-linux-server-installation.html
[3]: https://www.linuxtechtips.com/2013/12/how-to-install-linux-apache-mysql-php.html
[4]: https://joomlacode.org/gf/project/joomla/frs/?action=FrsReleaseBrowse&frs_package_id=6490

