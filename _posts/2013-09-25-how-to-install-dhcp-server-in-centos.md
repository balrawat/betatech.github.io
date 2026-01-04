---
layout: post
title: How to install DHCP server in Centos and Redhat
date: '2013-09-25T10:49:00.003+05:30'
author: Balvinder Rawat
tags:
  - dhcp
  - linux
modified_time: '2013-09-25T11:03:08.211+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-7195729992109637040'
blogger_orig_url: >-
  https://www.linuxtechtips.com/2013/09/how-to-install-dhcp-server-in-centos.html
---


The **dhcp (Dynamic Host Configuration Protocol)**package contains an Internet Systems Consortium (ISC) DHCP server. DHCP is used to assign IP addresses and other stuff like gateway and DNS details automatically to the clients. we need a DHCP server configured for offering ipaddress to the clients when it is required. First, install the package as the superuser:

## \# yum install dhcp

Installing the dhcp package creates a file, **/etc/dhcp/dhcpd.conf,** which is merely an empty configuration file:

## cat /etc/dhcp/dhcpd.conf

#

\# DHCP Server Configuration file.

\#   see /usr/share/doc/dhcp*/dhcpd.conf.sample

The sample configuration file can be found at **/usr/share/doc/dhcp-<version>/dhcpd.conf.sample**. You should use this file to help you configure **/etc/dhcp/dhcpd.conf**, which is explained in detail below.

DHCP also uses the file `/var/lib/dhcpd/dhcpd.leases` to store the client lease database.

After installing dhcp server packages along with dependencies .Assign a static ip (eg: “192.168.0.254″) in the same DHCP range for the listening interface ( eg : “eth0″ ). Open`/etc/sysconfig/network-scripts/ifcfg-eth0` file and make the changes as per your requirement.

## Configuration File

The first step in configuring a DHCP server is to create the configuration file that stores the network information for the clients. Use this file to declare options and global options for client systems.

For every **subne**t which will be served, and for every subnet to which the DHCP server is connected, there must be one subnet declaration, which tells the DHCP daemon how to recognize that an address is on that subnet. A subnet declaration is required for each subnet even if no addresses will be dynamically allocated to that **subnet**.

In this example, there are global options for every DHCP client in the subnet and a range` declared. Clients are assigned an IP address within the range`.

subnet 192.168.1.0 netmask 255.255.255.0 {

        option routers                  192.168.1.254;

        option subnet-mask              255.255.255.0;

        option domain-search              "example.com";

        option domain-name-servers       192.168.1.1;

        option time-offset              -18000;     # Eastern Standard Time

range 192.168.1.10 192.168.1.100;

}

To configure a DHCP server that leases a dynamic IP address to a system within a subnet, modify Range parameter with your values. It declares a default lease time, maximum lease time, and network configuration values for the clients. This example assigns IP addresses in the range` 192.168.1.10 and 192.168.1.100 to client systems.

default-lease-time 600;

max-lease-time 7200;

option subnet-mask 255.255.255.0;

option broadcast-address 192.168.1.255;

option routers 192.168.1.254;

option domain-name-servers 192.168.1.1, 192.168.1.2;

option domain-search "example.com";

subnet 192.168.1.0 netmask 255.255.255.0 {

   range 192.168.1.10 192.168.1.100;

}

To assign an IP address to a client based on the MAC address of the network interface card, use the hardware ethernet parameter within a host declaration. As demonstrated below, the host apex declaration specifies that the network interface card with the MAC address 00:A0:78:8E:9E:AA always receives the IP address 192.168.1.4.

Note that you can also use the optional parameter host-name to assign a host name to the client.

host apex {

   option host-name "apex.example.com";

   hardware ethernet 00:A0:78:8E:9E:AA;

   fixed-address 192.168.1.4;

}

All subnets that share the same physical network should be declared within a `shared-network` declaration as shown below. Parameters within the `shared-network`, but outside the enclosed subnet` declarations, are considered to be global parameters. The name of the `shared-network` must be a descriptive title for the network, such as using the title 'test-lab' to describe all the subnets in a test lab environment.

shared-network name {

    option domain-search              "test.redhat.com";

    option domain-name-servers      ns1.redhat.com, ns2.redhat.com;

    option routers                  192.168.0.254;

    more parameters for EXAMPLE shared-network

    subnet 192.168.1.0 netmask 255.255.252.0 {

        parameters for subnet

        range 192.168.1.1 192.168.1.254;

    }

    subnet 192.168.2.0 netmask 255.255.252.0 {

        parameters for subnet

        range 192.168.2.1 192.168.2.254;

    }

}

As demonstrated below, the group` declaration is used to apply global parameters to a group of declarations. For example, shared networks, subnets, and hosts can be grouped.

group {

   option routers                  192.168.1.254;

   option subnet-mask              255.255.255.0;

   option domain-search              "example.com";

   option domain-name-servers       192.168.1.1;

   option time-offset              -18000;     # Eastern Standard Time

   host apex {

      option host-name "apex.example.com";

      hardware ethernet 00:A0:78:8E:9E:AA;

      fixed-address 192.168.1.4;

   }

   host raleigh {

      option host-name "raleigh.example.com";

      hardware ethernet 00:A1:DD:74:C3:F2;

      fixed-address 192.168.1.6;

   }

}

## Imp Notes:

When the DHCP server is started for the first time, it fails unless the **dhcpd.leases** file exists. Use the command touch **/var/lib/dhcpd/dhcpd.leases** to create the file if it does not exist.

If the same server is also running BIND as a DNS server, this step is not necessary, as starting the named service automatically checks for a **dhcpd.leases** file.

To start the DHCP service, use the command `/sbin/service dhcpd start`. To stop the DHCP server, use the command `/sbin/service dhcpd stop`.

By default, the DHCP service does not start at boot time. To configure the daemon to start automatically at boot time, use the command   ## chkconfig dhcpd on

If more than one network interface is attached to the system, but the DHCP server should only be started on one of the interfaces, configure the DHCP server to start only on that device. In `/etc/sysconfig/dhcpd`, add the name of the interface to the list of DHCPDARGS`:

## Configuring a DHCP Client

To configure a DHCP client manually, modify the **/etc/sysconfig/network** file to enable networking and the configuration file for each network device in the **/etc/sysconfig/network-scripts** directory. In this directory, each device should have a configuration file named **ifcfg-eth0**, where **eth0** is the network device name.

Make sure that the **/etc/sysconfig/network-scripts/ifcfg-eth0** file contains the following lines:

_DEVICE=eth0_

_BOOTPROTO=dhcp_

_ONBOOT=yes_

To use DHCP, set a configuration file for each device.

Other options for the network script include:

**DHCP_HOSTNAME** — Only use this option if the DHCP server requires the client to specify a hostname before receiving an IP address.

**PEERDNS**=**<answer>**, where **<answer>** is one of the following:

*   **yes** — Modify **/etc/resolv.conf** with information from the server. If using DHCP, then **yes** is the default.
*   **no** — Do not modify **/etc/resolv.conf**.

