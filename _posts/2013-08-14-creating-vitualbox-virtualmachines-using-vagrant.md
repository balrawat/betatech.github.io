---
layout: post
title: Using Vagrant to create virtual machines with Virtual Box
date: '2013-08-14T16:31:00.002+05:30'
author: Balvinder Rawat
tags:
  - virtualbox
  - virtual machine
  - vagrant
  - virtualization
modified_time: '2013-08-14T16:35:18.105+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-7022536017623818459'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/08/creating-vitualbox-virtualmachines-using-vagrant.html
---
  
I'm a Linux System Admin & I play with lots of virtual machines to try & test various software & services. I use Virtual Box for creating virtual machine. Everything works fine except the part of installing same virtual machine again & again which takes a lot of time installing & configuring it.

  

Recently I came across a tool called Vagrant which can automate that process or at least can make it easy for us to make a base image & then create virtual machines from that image without any worry.

  
**Now the real work:-**  
  
Make sure you've Virtual Box installed on your machine, if not already done, download from [https://www.virtualbox.org/wiki/Downloads][1] & install it. Its available for almost all popular platforms.  
  
Download Vagrant from [http://downloads.vagrantup.com/][2] & install it.  
  

Binary packages available for MAC, Windows, debian & RPM based systems.

  

I used Centos 6 heavily so I installed Centos 6. Location specific mirrors for Centos are available at [http://isoredirect.centos.org/centos/6/isos/x86_64/][3] . Make sure you have Centos6 CD/DVD downloaded.

  
Now create a virtual machine for you work in Virtual Box. Those who are new to it can check help here [http://www.virtualbox.org/manual/ch01.html][4]  
  

Create a new VM by providing information like CPUs & RAM & HDD etc.

  

Now when machine is up & running. Enable the default network interface (eth0) with DHCP.

  

_**vi /etc/sysconfig/network-scripts/ifcfg-eth0**_

set ONBOOT='yes' and BOOTPROTO=dhcp

  

Start the network service:-

  

_**service network restart**_

  

make sure your system is up to date:-

  

**_yum update_**

  

make sure you've kernel packages to allow installation of Guest Additions:-

  

**_yum install gcc make kernel-devel kernel-headers perl_**

  

Now shutdown the VM & run following command in your host system:-

  

Go to the virtual box installation directory.

I've Windows XP as host:

So I run the command:-

**_"C:\\Program Files\\Oracle\\VirtualBox\\VBoxManage.exe modifyvm "vagrant-centos6" --natpf1 "guestssh,tcp,,2222,,22"_**

  

where "vagrant-centos6" is the name of virtual machine, change it to your VM name.

  
This will open SSH port on locahost to the new VM. This can also be done through Virtual Box GUI.  
  
Start the VM & install the Guest additions.  
  

After installation of guest additions, just logoff & login to make sure its working.

  

Now create the vagrant user:-

  

**_groupadd  admin_**

**_useradd -G admin -p $(openssl passwd -1 vagrant) vagrant_**

  

Install & configure sudo for vagrant user to have passwordless sudo access:-

  
**_yum install sudo_**  
  
**_visudo_**  
  
& add the following lines to end of the file:-  
  

**_%admin ALL=NOPASSWD: ALL_**

  

Now su to vagrant user:-

  

su - vagrant

  

Create a ssh-key-pair

  

ssh-keygen -t dsa

  

Press enter for blank passphrase.

  
Now run :-  
  
**_cd .ssh_**  
  

**_cat id\_dsa.pub >> authorized\_keys_**

**_chmod 0755 /home/vagrant/.ssh_**

**_chmod 0644 /home/vagrant/.ssh/authorized_keys_**

  

**Make sure to have the private key with you in your host system. Private key is present at /home/vagrant/.ssh/id_dsa**

  
Now you can make any modification like installation softwares etc on the VM.  
  

Finally shut down the VM.

  

On the host machine, open the Command prompt. Navigate to the directory where the VM is placed, in my case its D:\\VM

  
Now run the commands:-  
  
**_vagrant package --output centos6.box --base vagrant-centos6_**  
  

here make sure to replace vagrant-centos6 with your machine name

also centos6.box can be any name you like.

  

**_vagrant box add centos6 centos6.box_**

  

here centos6 can be any name you like.

  

**_vagrant box list_** ## this will show the new box

  

Now you can create new VM really quick by running following commands:-

  

**_mkdir "NEW_VM"_**

**_cd "NEW_VM"_**

_**vagrant init centos6** \## centos6 here should match the one in vagrant box list._

**_vagrant up_**

  

& 

  

**_vagrant ssh  ## this will create the SSH session to VM (for linux hosts)_**

  

For windows hosts, use putty client & the key private key you saved earlier in this tutorial, to login into the VM through vagrant user.

  

[1]: https://www.virtualbox.org/wiki/Downloads
[2]: http://downloads.vagrantup.com/
[3]: http://isoredirect.centos.org/centos/6/isos/x86_64/
[4]: http://www.virtualbox.org/manual/ch01.html

