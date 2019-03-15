---
layout: post
title: DNS Server Configuration on Linux
date: '2013-11-08T12:13:00.000+05:30'
author: Balvinder Rawat
tags:
  - dns
  - dns server
  - bind9
modified_time: '2013-11-08T12:17:49.331+05:30'
thumbnail: >-
  http://4.bp.blogspot.com/-bERkx9RU2hg/UnyJBwMVrLI/AAAAAAAAAn0/kVgaOwliJQA/s72-c/DNS3.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-3742909536503461890'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/11/dns-server-configuration-on-linux.html'
---
[![](http://4.bp.blogspot.com/-bERkx9RU2hg/UnyJBwMVrLI/AAAAAAAAAn0/kVgaOwliJQA/s1600/DNS3.png)][1]

  

This article is a quick configuration manual of a Linux DNS server using bind.I believe thatbind do not need much introduction, butbefore you proceed with the installation and configuration of bind nameserver make sure that bind DNS server is exactly what you want. Default setup and execution of bind on Debian or Ubuntu may take around 200MB of RAM with no zones added to the config file. Unless you reduce the memory usage of a bind via various bind "options" config settings, be prepared to have some spare RAM available just for this service. This fact is even more important if you pay for your own VPS server.

  

  

Another DNS nameservers available on a Linux systems are NSD ( Name Server Daemon) or djbdns ( tinydns ). Both are lightweight alternatives to bind9 DNS server and have less RAM requirements. Apparently are even faster.

In this article we will not go into details of what Domain Name Service ( DNS ) is nor how DNS works. Rather we simply concentrate in a simple configuration of a custom zone and config file for a given domain / host supporting www, mail services.

  

Sample scenario notes to help you ready this DNS bind howto:

· nameserver IP address 192.168.135.130

· sample domain / host: linuxtechtips.com

· authoritative nameservers for a linuxtechtips.com zone: ns1.linuxtechtips.com ( 192.168.0.10 ) and ns2.linuxtechtips.com ( 192.168.0.11 )

· www and mail services for linuxtechtips.com will point to: 192.168.0.10

1. bind9 nameserver installation

Unless you prefer to install bind from a source code the installation is rather simple. On a Debian or Ubuntu Linux server you can install a bind nameserver with a following command:

apt-get install bind9 dnsutils

CentOS or Fedora alternative:

yum install bind dnsutils

dnsutils is not compulsory package to run bind webserver, but we will use a dig command which is part of this package as a testing tool of your bind configuration.

2. Creating a DNS zone file

At this stage we will need to create a new zone file for a domain linuxtechtips.com. Navigate to /etc/bind/ directory execute following sequence of commands to navigate to zones/master/

cd /etc/bind

mkdir -p zones/master

cd zones/master/

/etc/bind/zones/master directory will contain a zone file for a linuxtechtips.com domain. If you prefer to use another directory to hold this file you are free to do so. The following zone file db.linuxtechtips.com will hold a DNS record to assist a nameserver resolve a fully qualified domain name to an IP address. Create and save **db.linuxtechtips.com** with a following content:

;

; BIND data file for linuxtechtips.com

;

$TTL    3h

@       IN      SOA     ns1.linuxtechtips.com. admin.linuxtechtips.com. (

                          1        ; Serial

                          3h       ; Refresh after 3 hours

                          1h       ; Retry after 1 hour

                          1w       ; Expire after 1 week

                          1h )     ; Negative caching TTL of 1 day

;

@       IN      NS      ns1.linuxtechtips.com.

@       IN      NS      ns2.linuxtechtips.com.

  

  

linuxtechtips.com.    IN      MX      10      mail.linuxtechtips.com.

linuxtechtips.com.    IN      A       192.168.0.10

ns1                     IN      A       192.168.0.10

ns2                     IN      A       192.168.0.11

www                     IN      CNAME   linuxtechtips.com.

mail                    IN      A       192.168.0.10

ftp                     IN      CNAME   linuxtechtips.com.

Here is just a quick review of some lines from the above bind DNS zone file:

· SOA Record: nameserver authoritative for a zone linuxtechtips.com is ns1.linuxtechtips.com and admin.linuxtechtips.com is an email address of a person responsible for this DNS zone.

· NS Records: two nameservers for a linuxtechtips.com zone are ns\[1,2\].linuxtechtips.com

· MX ( Mail Exchange): linuxtechtips.com mail exachange record. Number 10 means a preference for discarting a records A : A simply means address inanother words in linuxtechtips.com's zone a ns1 would ahve a A ( address ) 192.168.0.10.

· CNAME Record ( Canonical Name record ): restart the query using the canonical name instead of the original name

3. address-to-name mappings

At this stage the bind DNS server can resolve an IP address mapped to a linuxtechtips.com host. What we should do now is the teach our nameserver the other way around, which is, to resolve a host from an IP address. For this we are going to need yet another file and that is**db.192.168.0**with a following content:

PTR

;

; BIND reverse data file for 0.168.192.in-addr.arpa

;

$TTL    604800

0.168.192.in-addr.arpa.      IN      SOA     ns1.linuxtechtips.com. admin.linuxtechtips.com. (

                          1         ; Serial

                          3h       ; Refresh after 3 hours

                          1h       ; Retry after 1 hour

                          1w       ; Expire after 1 week

                          1h )     ; Negative caching TTL of 1 day

;

0.168.192.in-addr.arpa.       IN      NS      ns1.linuxtechtips.com.

0.168.192.in-addr.arpa.       IN      NS      ns2.linuxtechtips.com.

  

10.0.168.192.in-addr.arpa.   IN      PTR     linuxtechtips.com.

· PTR: a NDS record used for a mapping of an IP address to a host name.

4. Updating a BIND Configuration File

At this point we should have two files ready:

· /etc/bind/zones/master/db.linuxtechtips.com

· /etc/bind/zones/master/db.192.168.0

All we need to do now is to insert both zone file names into a bind's configuration file **named.conf.local. **To do that add following lines into this file:

zone "linuxtechtips.com" {

       type master;

       file "/etc/bind/zones/master/db.linuxtechtips.com";

};

  

zone "0.168.192.in-addr.arpa" {

       type master;

       file "/etc/bind/zones/master/db.192.168.0";

};

Last thing before we go ahead to check a configuration is to add and IP address af a stable DNS server to a named.conf.options file. This IP address is used in case that a local DNS server do not know the answer the a name resolution query. In IP address of a DNS server in many cases is provided by your Internet provider. Alternatively if you are google fan use 8.8.8.8 or 8.8.4.4.

Replace a following blog of text withing a named.conf.options file:

       // forwarders {

       //      0.0.0.0;

       // };

with new stable DNS server IP address

        forwarders {

              8.8.4.4;

         };

5. Checking bind's zone files and configuration

Before we attempt to start a bind nameserver with a new zone and configuration here are some tools to check if we have not done some typo or misconfiguration.

To check a configuration files run a following command:

named-checkconf

With this named-checkconf command the rule is: no news are good news. If no output had been produced your config files looks OK.

To check a DNS zone files we can use named-checkzone command:

named-checkzone linuxtechtips.com /etc/bind/zones/master/db.linuxtechtips.com

zone linuxtechtips.com/IN: loaded serial 1

OK

reverse zone file check:

named-checkzone 0.168.192.in-addr.arpa /etc/bind/zones/master/db.192.168.0

zone 0.168.192.in-addr.arpa/IN: loaded serial 2

OK

6. Start / restart bind nameserver

At this point nothing can stop us to run bind9 dns server:

 /etc/init.d/bind9 start

Starting domain name service...: bind9.

Alternatively, if your bind server is already running use a following command to to assist you with its restart:

/etc/init.d/bind9 restart

Stopping domain name service...: bind9.

Starting domain name service...: bind9.

7. Testing a bind server configuration

A dig command from dnsutils package will become handy to help us to test a new configuration of bind nameserver.

dig command can be used from any PC which has a network access the your DNS server but preferably your should start your testing from a localhost. In our this case the IP address of our name server is 192.168.135.130. First we will test host-to-IP resolution:

dig @192.168.135.130 www.linuxtechtips.com

  

; <<>\> DiG 9.6-ESV-R1 <<>> @192.168.135.130 www.linuxtechtips.com

; (1 server found)

;; global options: +cmd

;; Got answer:

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 60863

;; flags: qr aa rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 2, ADDITIONAL: 2

  

;; QUESTION SECTION:

;www.linuxtechtips.com.           IN      A

  

;; ANSWER SECTION:

www.linuxtechtips.com.    10800   IN      CNAME   linuxtechtips.com.

linuxtechtips.com.        10800   IN      A       192.168.0.10

  

;; AUTHORITY SECTION:

linuxtechtips.com.        10800   IN      NS      ns2.linuxtechtips.com.

linuxtechtips.com.        10800   IN      NS      ns1.linuxtechtips.com.

  

;; ADDITIONAL SECTION:

ns1.linuxtechtips.com.    10800   IN      A       192.168.0.10

ns2.linuxtechtips.com.    10800   IN      A       192.168.0.11

  

;; Query time: 0 msec

;; SERVER: 192.168.135.130#53(192.168.135.130)

;; WHEN: Thu Aug  5 18:50:48 2010

;; MSG SIZE  rcvd: 135

Next we test IP-to-host resolution:

dig @192.168.135.130 -x 192.168.0.10

  

; <<>\> DiG 9.6-ESV-R1 <<>> @192.168.135.130 -x 192.168.0.10

; (1 server found)

;; global options: +cmd

;; Got answer:

;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10810

;; flags: qr aa rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 2, ADDITIONAL: 2

  

;; QUESTION SECTION:

;10.0.168.192.in-addr.arpa.     IN      PTR

  

;; ANSWER SECTION:

10.0.168.192.in-addr.arpa. 604800 IN    PTR     linuxtechtips.com.

  

;; AUTHORITY SECTION:

0.168.192.in-addr.arpa. 604800  IN      NS      ns2.linuxtechtips.com.

0.168.192.in-addr.arpa. 604800  IN      NS      ns1.linuxtechtips.com.

  

;; ADDITIONAL SECTION:

ns1.linuxtechtips.com.    10800   IN      A       192.168.0.10

ns2.linuxtechtips.com.    10800   IN      A       192.168.0.11

  

;; Query time: 0 msec

;; SERVER: 192.168.135.130#53(192.168.135.130)

;; WHEN: Thu Aug  5 18:52:06 2010

;; MSG SIZE  rcvd: 140

Congratulations, you have just created and configured your own DNS zone using bind nameserver.

  

  

[1]: http://4.bp.blogspot.com/-bERkx9RU2hg/UnyJBwMVrLI/AAAAAAAAAn0/kVgaOwliJQA/s1600/DNS3.png

