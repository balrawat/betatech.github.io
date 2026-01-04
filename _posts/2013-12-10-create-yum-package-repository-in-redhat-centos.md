---
layout: post
title: Create a YUM Package Repository on Redhat/Centos
date: '2013-12-10T17:18:00.000+05:30'
author: Balvinder Rawat
tags:
  - yum repo
  - linux
  - yum
modified_time: '2013-12-13T14:00:39.826+05:30'
thumbnail: >-
  https://2.bp.blogspot.com/-NS293WxpQ5g/UoWxtFwisjI/AAAAAAAAAoo/nc9r_oUWGjI/s72-c/yum.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-5693118972823661278'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/12/create-yum-package-repository-in-redhat-centos.html
---
[![](https://2.bp.blogspot.com/-NS293WxpQ5g/UoWxtFwisjI/AAAAAAAAAoo/nc9r_oUWGjI/s1600/yum.png)][1]

**1. Introduction**

If your Redhat server is not connected to the official RHN repositories, you will need to configure your own private repository which you can later use to install packages. The procedure of creating a Redhat repository is quite simple task. In this article we will show you how to create a local file Redhat repository as well as remote HTTP repository.

**2. Using Official Redhat DVD as repository**

After default installation and without registering your server to official RHN repositories your are left without any chance to install new packages from redhat repository as your repository list will show 0 entries:

\# yum repolist

  

Loaded plugins: product-id, refresh-packagekit, security, subscription-manager

  

This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.

  

repolist: 0

At this point the easiest thing to do is to attach your Redhat installation DVD as a local repository. To do that, first make sure that your RHEL DVD is mounted:

\# mount | grep iso9660

  

/dev/sr0 on /media/RHEL\_6.4 x86\_64 Disc 1 type iso9660 (ro,nosuid,nodev,uhelper=udisks,uid=500,gid=500,iocharset=utf8,mode=0400,dmode=0500)

The directory which most interests us at the moment is "**/media/RHEL\_6.4 x86\_64 Disc 1/repodata**" as this is the directory which contains information about all packages found on this particular DVD disc.

Next we need to define our new repository pointing to "**/media/RHEL\_6.4 x86\_64 Disc 1/**" by creating a repository entry in /etc/yum.repos.d/. Create a new file called: /etc/yum.repos.d/RHEL\_6.4\_Disc.repo usingvi editorand insert a following text:

\[RHEL\_6.4\_Disc\]

  

name=RHEL\_6.4\_x86\_64\_Disc

  

baseurl="file:///media/RHEL\_6.4 x86\_64 Disc 1/"

  

gpgcheck=0

Once file was created your local Redhat DVD repository should be ready to use:

\# yum repolist

  

Loaded plugins: product-id, refresh-packagekit, security, subscription-manager

  

This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.

  

repo idrepo namestatus

  

RHEL\_6.4\_DiscRHEL\_6.4\_x86\_64\_Disc3,648

repolist: 3,648

**3. Creating a local file Redhat repository**

Normally having a Redhat DVD repository will be enough to get you started however, the only disadvantage is that you are not able to alter your repository in any way and thus not able to insert new/updated packages into it. The resolve this issue we can create a local file repository sitting somewhere on the filesystem. To aid us with this plan we will use a **createrepo** utility.

By default createrepo may not be installed on your system:

\# yum list installed | grep createrepo

  

#

No output indicates that this packages is currently not present in your system. If you have followed a previous section on how to attach RHEL official DVD as your system's repository, then to install **createrepo **package simply execute:

\# yum install createrepo

The above command will install **createrepo** utility along with all prerequisites. In case that you do not have your repository defined yet, you can install createrepo manually:

Using your mounted RedHat DVD first install prerequisites:

\# rpm -hiv /media/RHEL\_6.4\ x86\_64\ Disc\ 1/Packages/deltarpm-*

\# rpm -hiv /media/RHEL\_6.4\ x86\_64\ Disc\ 1/Packages/python-deltarpm-*

 followed by the installation of the actual createrepo package:

\# rpm -hiv /media/RHEL\_6.4\ x86\_64\ Disc\ 1/Packages/createrepo-*

If all went well you should be able to see createrepo package installed in your system:

\# yum list installed | grep createrepo

createrepo.noarch                        0.9.9-17.el6                          installed

At this stage we are ready to create our own Redhat local file repository. Create a new directory called **/rhel_repo:**

\# mkdir /rhel_repo

Next, copy all packages from your mounted RHEL DVD to your new directory:

\# cp /media/RHEL\_6.4\ x86\_64\ Disc\ 1/Packages/* /rhel_repo/

When copy is finished execute createrepo command with a single argument which is your new local repository directory name:

\# createrepo /rhel_repo/

Spawning worker 0 with 3648 pkgs

  

Workers Finished

  

Gathering worker results

  

  

  

Saving Primary metadata

Saving file lists metadata

Saving other metadata

Generating sqlite DBs

Sqlite DBs complete

You are also able to create Redhat repository on any debian-like Linux system such as Debian, Ubuntu or mint. The procedure is the same except that installation of createrepo utility will be: # apt-get install createrepo

As a last step we will create a new yum repository entry:

\# vi /etc/yum.repos.d/rhel_repo.rep

\[rhel_repo\]

  

name=RHEL\_6.4\_x86\_64\_Local

  

baseurl="file:///rhel_repo/"

  

gpgcheck=0

Your new repository should now be accessible:

\# yum repolist

  

Loaded plugins: product-id, refresh-packagekit, security, subscription-manager

  

This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.

  

rhel_repo| 2.9 kB00:00 ... 

  

rhel\_repo/primary\_db| 367 kB00:00 ... 

repo idrepo namestatus

RHEL\_6.4\_DiscRHEL\_6.4\_x86\_64\_Disc3,648

**

**rhel\_repo                    RHEL\_6.4\_x86\_64_Local                                              3,648**

**

**4. Creating a remote HTTP Redhat repository**

If you have multiple Redhat servers you may want to create a single Redhat repository accessible by all other servers on the network. For this you will need apache web server. Detailed installation and configuration of Apache web server is beyond the scope of this guide therefore, we assume that your **httpd** daemon ( Apache webserver ) is already configured. In order to make your new repository accessible via http configure your apache with /rhel_repo/ directory created in previous section as **document root directory** or simply copy entire directory to: /var/www/html/ ( default document root ).

Then create a new yum repository entry on your client system by creating a new repo configuration file:

vi /etc/yum.repos.d/rhel\_http\_repo.repo

with a following content, where my host is a IP address or hostname of your Redhat repository server:

\[rhel\_repo\_http\]

  

name=RHEL\_6.4\_x86\_64\_HTTP

  

baseurl="https://myhost/rhel_repo/"

  

gpgcheck=0

Confirm the correctness of your new repository by:

\# yum repolist

  

Loaded plugins: product-id, refresh-packagekit, security, subscription-manager

  

This system is not registered to Red Hat Subscription Management. You can use subscription-manager to register.

  

repo id repo namestatus

  

rhel\_repo\_http        RHEL\_6.4\_x86\_64\_HTTP 3,648

repolist: 3,648

**5. Conclusion**

Creating your own package repository gives you more options on how to manage packages on your Redhat system even without paid RHN subscription. When using a remote HTTP Redhat repository you may also want to configure GPGCHECK as part of your repository to make sure that no packages had been tampered to prior their installation.

  

  

  

[1]: https://2.bp.blogspot.com/-NS293WxpQ5g/UoWxtFwisjI/AAAAAAAAAoo/nc9r_oUWGjI/s1600/yum.png

