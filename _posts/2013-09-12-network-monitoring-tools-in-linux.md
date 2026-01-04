---
layout: post
title: Network Monitoring tools in Linux
date: '2013-09-12T12:09:00.002+05:30'
author: Balvinder Rawat
tags:
  - network monitoring
modified_time: '2013-09-12T12:09:18.258+05:30'
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-3993273604776682102'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/09/network-monitoring-tools-in-linux.html'
---


Network monitoring tools are used to monitor the network, systems present on the network, various service running on the network, traffic etc.

**Ping:** Ping command is used to check if the system is in the network or not. To check if the host is operating.

e.g. ping ip_address

```bash
\[root@server1 ~\]# ping 172.26.128.132
```

_PING 172.26.128.132 (172.26.128.132) 56(84) bytes of data._

_64 bytes from 172.26.128.132: icmp_seq=0 ttl=58 time=3.27 ms_

_64 bytes from 172.26.128.132: icmp_seq=1 ttl=58 time=3.12 ms_

_64 bytes from 172.26.128.132: icmp_seq=2 ttl=58 time=1.92 ms_

_64 bytes from 172.26.128.132: icmp_seq=3 ttl=58 time=3.10 ms_

_64 bytes from 172.26.128.132: icmp_seq=4 ttl=58 time=2.14 ms_

_\-\-\- 172.26.128.132 ping statistics ---_

_5 packets transmitted, 5 received, 0% packet loss, time 4006ms_

`rtt min/avg/max/mdev = 1.922/2.715/3.279/0.564 ms, pipe 2`

```bash
\[root@server1 ~\]#
```

When the command is executed, it returns a detailed summary of the host. Packets sent, received, lost by estimating the round trip time.

**Traceroute:** the command is used to trace the path taken by the packet across a network. Tracing the path here means finding out the hosts visited by the packet to reach its destination. This information is useful in debugging. Roundtrip time in ms is shown for every visit to a host.

**Tcpdump:** commonly used to monitor network traffic. Tcdump captures and displays packet headers and matching them against criteria or all. It interprets Boolean operators and accepts host names, ip address, network names as arguments.

**Ntop:** Network top shows the network usage. It displays summary of network usage by machines on the network in a format as of UNIX top utility. It can also be run in web mode, which allows the display to be browsed with a web browser. It can display network traffic statistics, identify host etc. Interfaces are available to view such information.

