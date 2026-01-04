---
layout: post
title: How to install NTOP on CentOS 5.5 64bits
date: '2013-01-24T17:19:00.001+05:30'
author: Balvinder Rawat
tags:
  - ntop
  - centos
  - linux
  - network monitoring
modified_time: '2013-08-06T16:43:35.804+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-4444424772863505716'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/01/how-to-install-ntop-on-centos-55-64bits.html
---
Quick and easisest way:

wget [http://apt.sw.be/redhat/el5/en/x86\`64/rpmforge/RPMS//rpmforge-release-0.3.6-1.el5.rf.x86\`64.rpm] http://apt.sw.be/redhat/el5/en/x86\`64/rpmforge/RPMS//rpmforge-release-0.3.6-1.el5.rf.x86\`64.rpm

rpm -Uvh rpmforge-release-0.3.6-1.el5.rf.x86_64.rpm

yum install ntop

\# Get yum ready

yum clean all

yum update

\# Install Development Tools

yum groupinstall “Development Tools”

\# Install more ntop Dependencies

yum install libpcap-devel libpcap

\# Install RDD tools dependencies

yum install cairo-devel libxml2-devel pango-devel pango libpng-devel freetype freetype-devel libart_lgpl-devel

\# Download, compile and install RDDTools

wget [https://oss.oetiker.ch/rrdtool/pub/rrdtool-1.4.5.tar.gz] https://oss.oetiker.ch/rrdtool/pub/rrdtool-1.4.5.tar.gz

tar xvzf rrdtool-1.4.5.tar.gz

cd rrdtool-1.4.5

./configure

make

make install

\# Download, compile and Install GeopIP

wget [https://geolite.maxmind.com/download/geoip/api/c/GeoIP.tar.gz] https://geolite.maxmind.com/download/geoip/api/c/GeoIP.tar.gz

tar xvzf GeoIP.tar.gz

cd GeoIP-1.4.6/

./configure

./make

./make install

NOTE: config at: /usr/local/etc/GeoIP.conf

#Download, compile and install nTop 4.0.1

wget [https://cdnetworks-us-1.dl.sourceforge.net/project/ntop/ntop/ntop-4.0.1/ntop-4.0.1.tar.gz] https://cdnetworks-us-1.dl.sourceforge.net/project/ntop/ntop/ntop-4.0.1/ntop-4.0.1.tar.gz

tar xvzf ntop4.0.1.tar.gz

cd ntop-4.0.1/

autoconf

./configure –with-rrd-home=/opt/rrdtool-1.4.4/

make

make install

\# Add ntop user and directory permissions.

useradd -M -s /sbin/nologin -r ntop

chown -R ntop:root /usr/local/var/ntop/

chown -R ntop:ntop /usr/local/share/ntop/

\# Set ntop password

ntop -A

\# To start ntop on boot

nano /etc/rc.local # and add: /usr/local/bin/ntop -i “eth0,eth1″ -d -L -u ntop -P /usr/local/

you have multiple interface (eth0, eth1 and so on), start ntop as follows:

\# To start ntop

/usr/bin/ntop -i “eth0″ -d -L -u ntop -P /var/ntop –skip-version-check –use-syslog=daemon

htpasswd -c /etc/httpd/.htpasswd segredes

Where,

\* -i “eth0,eth1″ : Specifies the network interface or interfaces to be used by ntop for network monitoring. Here you are monitoring eth0 and eth1.

\* -d : Run ntop as a daemon.

\* -L : Send all log messages to the system log (/var/log/messages) instead of screen.

\* -u ntop : Start ntop as ntop user

\* -P /usr/local/var/ntop : Specify where ntop stores database files. You may need to backup database as part of your disaster recovery program.

\* –skip-version-check : By default, ntop accesses a remote file to periodically check if the most current version is running. This option disables that check.

\* –use-syslog=daemon : Use syslog daemon.

By default ntop listen on 3000 port. You can view ntop stats by visiting following url:

[https://localhost:3000/] https://localhost:3000/

[1]: http://apt.sw.be/redhat/el5/en/x86`64/rpmforge/RPMS//rpmforge-release-0.3.6-1.el5.rf.x86`64.rpm
[2]: https://oss.oetiker.ch/rrdtool/pub/rrdtool-1.4.5.tar.gz
[3]: https://geolite.maxmind.com/download/geoip/api/c/GeoIP.tar.gz
[4]: https://cdnetworks-us-1.dl.sourceforge.net/project/ntop/ntop/ntop-4.0.1/ntop-4.0.1.tar.gz
[5]: https://localhost:3000/

