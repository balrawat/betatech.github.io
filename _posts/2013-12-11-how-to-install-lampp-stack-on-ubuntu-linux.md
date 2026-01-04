---
layout: post
title: 'How To Install Linux, Apache, MySQL, PHP (LAMP) stack on Ubuntu'
date: '2013-12-11T18:40:00.001+05:30'
author: Balvinder Rawat
tags:
  - mysql
  - lampp
  - apache
  - php
modified_time: '2013-12-11T18:40:33.457+05:30'
thumbnail: >-
  https://2.bp.blogspot.com/-8x6dugKaabk/UqhhKG12FII/AAAAAAAAAw0/HIjRekjE8II/s72-c/lampp.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-531155729873373933'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/how-to-install-lampp-stack-on-ubuntu-linux.html
---
[![](https://2.bp.blogspot.com/-8x6dugKaabk/UqhhKG12FII/AAAAAAAAAw0/HIjRekjE8II/s640/lampp.png)][1]

###   

### About LAMP

* * *

LAMP stack is a group of open source software used to get web servers up and running. The acronym stands for Linux, Apache, MySQL, and PHP. Since the linux server is already running Ubuntu, the linux part is taken care of. Here is how to install the rest.  
  

**Set Up**

The steps in this tutorial require the user to have root privileges on your linux server. You can see how to set that up in the[Initial Server Setup][2]in steps 3 and 4.  
  

**Step One—Install Apache**

* * *

Apache is a free open source software which runs over 50% of the world’s web servers.  
  
To install apache, open terminal and type in these commands:

_\# sudo apt-get update_

_\# sudo apt-get install apache2_

  
That’s it. To check if Apache is installed, direct your browser to your server’s IP address (eg. https://12.34.56.789). The page should display the words “It works!"  

**How to Find your Server’s IP address**

* * *

You can run the following command to reveal your server’s IP address.

_\# ifconfig eth0 | grep inet | awk '{ print $2 }'_

**Step Two—Install MySQL**

* * *

MySQL is a powerful database management system used for organizing and retrieving data  
  
To install MySQL, open terminal and type in these commands:  

_\# sudo apt-get install mysql-server libapache2-mod-auth-mysql php5-mysql_

  
During the installation, MySQL will ask you to set a root password. If you miss the chance to set the password while the program is installing, it is very easy to set the password later from within the MySQL shell.  
  
Once you have installed MySQL, we should activate it with this command:

_\# sudo mysql\_install\_db_

  
Finish up by running the MySQL set up script:

_\# sudo /usr/bin/mysql\_secure\_installation_

  
The prompt will ask you for your current root password.  
  
Type it in.

Enter current password for root (enter for none): 

OK, successfully used password, moving on...

  
Then the prompt will ask you if you want to change the root password. Go ahead and choose N and move on to the next steps.  
  
It’s easiest just to say Yes to all the options. At the end, MySQL will reload and implement the new changes.

_By default, a MySQL installation has an anonymous user, allowing anyone_

_to log into MySQL without having to have a user account created for_

_them.  This is intended only for testing, and to make the installation_

_go a bit smoother.  You should remove them before moving into a_

_production environment._

_Remove anonymous users? \[Y/n\] y_ 

_ ... Success!_

_Normally, root should only be allowed to connect from 'localhost'.  This_

_ensures that someone cannot guess at the root password from the network._

_Disallow root login remotely? \[Y/n\] y_

_... Success!_

_By default, MySQL comes with a database named 'test' that anyone can_

_access.  This is also intended only for testing, and should be removed_

_before moving into a production environment._

_Remove test database and access to it? \[Y/n\] y_

 _\- Dropping test database..._

 _... Success!_

 _\- Removing privileges on test database..._

 _... Success!_

_Reloading the privilege tables will ensure that all changes made so far_

_will take effect immediately._

_Reload privilege tables now? \[Y/n\] y_

 _... Success!_

_Cleaning up..._

Once you're done with that you can finish up by installing PHP.  
  

**Step Three—Install PHP**

* * *

PHP is an open source web scripting language that is widely use to build dynamic webpages.  
  
To install PHP, open terminal and type in this command.

_\# sudo apt-get install php5 libapache2-mod-php5 php5-mcrypt_

  
After you answer yes to the prompt twice, PHP will install itself.  
  
It may also be useful to add php to the directory index, to serve the relevant php index files:

_\# sudo nano /etc/apache2/mods-enabled/dir.conf_

  
Add index.php to the beginning of index files. The page should now look like this:

_<IfModule mod_dir.c>_

_          DirectoryIndex index.php index.html index.cgi index.pl index.php index.xhtml index.htm_

_</IfModule>_

PHP Modules
-----------

* * *

PHP also has a variety of useful libraries and modules that you can add onto your linux server. You can see the libraries that are available.

_apt-cache search php5-_

  
Terminal will then display the list of possible modules. The beginning looks like this:

_php5-cgi - server-side, HTML-embedded scripting language (CGI binary)_

_php5-cli - command-line interpreter for the php5 scripting language_

_php5-common - Common files for packages built from the php5 source_

_php5-curl - CURL module for php5_

_php5-dbg - Debug symbols for PHP5_

_php5-dev - Files for PHP5 module development_

_php5-gd - GD module for php5_

_php5-gmp - GMP module for php5_

_php5-ldap - LDAP module for php5_

_php5-mysql - MySQL module for php5_

_php5-odbc - ODBC module for php5_

_php5-pgsql - PostgreSQL module for php5_

_php5-pspell - pspell module for php5_

_php5-recode - recode module for php5_

_php5-snmp - SNMP module for php5_

_php5-sqlite - SQLite module for php5_

_php5-tidy - tidy module for php5_

_php5-xmlrpc - XML-RPC module for php5_

_php5-xsl - XSL module for php5_

_php5-adodb - Extension optimising the ADOdb database abstraction library_

_php5-auth-pam - A PHP5 extension for PAM authentication_

_\[...\]_

Once you decide to install the module, type:

_\# sudo apt-get install name of the module_

  
You can install multiple libraries at once by separating the name of each module with a space.  
  
Congratulations! You now have LAMP stack on your Linux Server!  

**Step Four—RESULTS: See PHP on your Server**

* * *

Although LAMP is installed, we can still take a look and see the components online by creating a quick php info page  
  
To set this up, first create a new file:

_\# sudo nano /var/www/info.php_

  
Add in the following line:

_<?php_

_phpinfo();_

_?>_

  
Then Save and Exit.  
  
Restart apache so that all of the changes take effect:

_\# sudo service apache2 restart_

  

  
Finish up by visiting your php info page (make sure you replace the example ip address with your correct one): https://12.34.56.789/info.php

  

  

  

[1]: https://2.bp.blogspot.com/-8x6dugKaabk/UqhhKG12FII/AAAAAAAAAw0/HIjRekjE8II/s1600/lampp.png
[2]: https://www.linuxtechtips.com/2013/12/steps-to-follow-after-linux-server-installation.html

