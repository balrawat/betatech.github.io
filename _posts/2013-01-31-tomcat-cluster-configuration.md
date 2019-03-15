---
layout: post
title: Tomcat Cluster Configuration
date: '2013-01-31T16:39:00.003+05:30'
author: Balvinder Rawat
tags:
  - windows
  - tomcat cluster
  - apache
  - tomcat cluster configuration
  - tomcat
modified_time: '2014-01-07T12:52:46.525+05:30'
thumbnail: >-
  http://4.bp.blogspot.com/-NChdPh4didE/Uo9VGNcsdZI/AAAAAAAAArI/rfF-JyOxg14/s72-c/tomcat-load-balancing.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-7562630654014742159'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/01/tomcat-cluster-configuration.html'
---
![](http://4.bp.blogspot.com/-NChdPh4didE/Uo9VGNcsdZI/AAAAAAAAArI/rfF-JyOxg14/s1600/tomcat-load-balancing.png)

  
Just because Tomcat is a lightweight container with a small footprint doesn't mean it isn't ready to deliver big performance under real-world loads. Tomcat's built-in support for clustering, load balancing, and session persistence means that you can add more power to your network as you need it, allowing your site to scale with your user base.

In this article, we'll go over the basic concepts behind clustered architecture, such as load balancing and session persistance, look at some different ways to approach these problems, and then show you how easy it is to set up your own Apache Tomcat clusters.

  

How Clustering Works
--------------------

Although clustering is most frequently talked about in relation to scalability, most modern clustering solutions actually attack a number of related issues in addition to simply providing more CPUs to serve requests. A typical clustering solution aims to provide not only scalability, but also high availability and load balancing. Before we move on, let's briefly clarify each of these terms:

  

### Scalability

Scalability and clustering are not the same thing. Rather, clustering is a method of achieving scalability. Scalability has to do with the ability of a server to efficiently process multiple concurrent requests simultaneously, with the stated goal that the time it takes to process an ever increasing number of simultaneous requests should be as close to the time it took to process the initial request as possible.

Clustering aims to provide scalability by spreading work out over a greater number of workers. Other methods of improving scalability are improving the hardware of the machines processing the requests, streamlining the data, caching frequent operations, and more.

  

### Load Balancing

Load balancing is a group of technologies aimed at distributing request load across a group of servers. Load balancing is a key component of a clustering solution, as it provides several services required to achieve the other goals of clustering.

To enable scalability, a load balancing implementation attempts to route requests to the server with the least amount of current load, for faster processing. To enable high-availability, which we will define next, a load balancing implementation must keep track of the status of its various servers, so that requests are never dropped.

Many load balancing solutions also take advantage of the fact that a server is now fronting the actual request processing software to provide an additional layer of security, ignoring and dropping malicious traffic before it can even reach the application servers.

Finally, the load balancing implementation makes the whole clustering structure functional by encapsulating the cluster within a virtual container, with one point of access. This means that the client attempting to access the web application served by the cluster never needs to know whether or not a cluster is being used.

  

### High Availability

High availability is a group of interrelated technologies and strategies with the aim of increasing the amount of time that the network is available to process requests. The most common of these techniques are failover, state replication, and load balancing.

Load balancing relates to high availability in two ways. First, it is a preventive measure; if a server never becomes overloaded, it will not fail. Secondly, it provides support to the failover mechanism by routing requests away from failed servers.

Failover refers to the ability of any server in the cluster to take over the work of any other server in the event that any server fails. Failover implementations can be divided into two categories - request-level and session-level.

Request-level failover is provided by the load balancer, and refers to the redirection of all subsequent requests after a server fails to a different server, to avoid any break in service.

Session-level failover, a more complicated proposition, involves replicating user sessions in such a way that in the event that a server goes down, another server or servers can take over the session information it was using, meaning that the user will not perceive any break in service. This is provided by using some form of session replication as a part of cluster.

One way to think about the structure of the cluster is as a sandwich - the load balancer is in front, distributing requests, the Tomcat servers are in the middle, serving requests, and the session replicator is in back, preserving the state data, in case anything goes wrong.

  

Setting up Clustering in Apache Tomcat
--------------------------------------

Let's get an example Tomcat cluster up and running. As Tomcat supports a few different options for load balancing and session persistance, we'll deal with these parts in separate sections, so we can dig a little deeper into the pros and cons of different set-ups.

Then, we'll put it all together, and walk you through setting up a simple Tomcat cluster with load balancing and session persistence from start to finish.

  

Load Balancing Options
----------------------

You can approach the problem of load balancing in a variety of ways, and Tomcat supports most of them with a little wrangling. The two most common ways to balance load across a group of servers are to use a dedicated load balancing appliance, or a software/server solution.

  

Load Balancing With An Appliance
--------------------------------

Load balancing network appliances are dedicated pieces of hardware that front a cluster and provide integrated load balancing capabilities. These devices use processors specifically designed for distributing high volumes of load efficiently, and also usually include a variety of compression, cacheing, and queueing options, as well as traffic shaping and security capabilities.

High end failover appliances can be very expensive, and can still represent a single point of failure for the network if scale continues to increase. Avoiding this problem brings the idea of HA load balancing into the equation, which uses such methods as hot spares to provide back-up.

While some users choose to utilize hardware load balancers with Tomcat clusters, other solutions are more common. For this reason, as well as the fact that each appliance vendor has slightly different set-up procedures for their devices, this article does not cover the configuration process for this approach. However, your vendor should be able to provide you with the proper documentation and support.

  

Load Balancing With a Server/Software Combination
-------------------------------------------------

The concept of the server/software approach to load balancing is basically the same as that of the appliance, but rather than using a dedicated device, it relies on a dedicated server or group of servers running one of a number of proxy solutions with load balancing capabilities.

  

Apache HTTPD and mod\_jk/mod\_proxy
-----------------------------------

The most popular server/software set-up for Tomcat clustering is to front a cluster of Tomcat servers with an Apache Web Server running either the mod\_JK or mod\_proxy connector module. These modules, which are also often used simply to provide basic interoperability between Apache Web Server and Tomcat, also each include built-in load balancing capabilities.

At one time, it was common practice to favor mod\_jk over mod\_proxy; this was because mod_jk was developed as part of the JK project, a Tomcat subproject aimed at improving connectivity between Tomcat and various web servers, and had support for AJP, an efficient protocol developed specifically for meta-data-rich communication between Apache Web Server and other types of servers.

The speed of AJP made this protocol preferable, and was a big vote on the side of mod\_jk. However, when mod\_proxy was refactored in Apache Web Server 2.2, it was vastly improved, and included new sub-modules offering support for AJP and load balancing features.Thus, the key differentiators between the two protocols are now the maturity of their load balancing features and the ease with which they can be configured.

As far as ease of configuration is concerned, mod_proxy is the clear winner. The module was developed alongside the Apache Web Server, and its configuration is very straightforward, only requiring a set of changes within Apache Web Server's main configuration file, httpd.conf.

By comparison, mod\_jk must be configured within httpd.conf, and then directed to an additional file called workers.properties, which defines all the available Tomcat servers as "workers", as well as a number of "virtual workers", processes that are responsible for the actual work of load balancing. This is often confusing, and can be a real source of frustration. On the other hand, mod\_proxy, being the more mature project, offers a much finer-grained level of control over the load balancing.

In terms of sophistication, mod\_jk wins hands down, and this makes it our recommended choice if you want real control over your load balancing. Although mod\_proxy and mod\_jk both include a web GUI, but mod\_jk's is much richer, offering a full page of information about each node, as well as a GUI tool for configuring hot load balancing properties, meaning that servers can be taken online and offline for updates one by one without interruption of service.

The load balancing algorithms used by mod\_jk are also more robust than mod\_proxy's, distributing load based on the number of HTTP sessions per server and each server's "lbfactor", a user-defined value used to incorporate the absolute performance potential of different servers into the equation.

As Apache HTTPD with mod_jk is far and away the most common clustering/load balancing solution used with Tomcat, this is the option we'll talk about later in this article.

  

Nginx, HAProxy, Wakamole and Spread
-----------------------------------

Although the official Apache documentation still recommends Apache HTTPD with Tomcat as the standard clustering solution, a growing number of alternative load balancing solutions have begun to gain traction.

These solutions focus around the combination of extremely lightweight, high-performance proxy solutions such as [Nginx][1] or [HAProxy][2], which provide load balancing, with [Wackamole][3] and [Spread][4], two interoperating open source technologies that provide distributed failover awareness via peer-to-peer messaging and floating IP addresses. With this set-up, it is possible to add multiple load balancer nodes to a cluster, which monitor one another's health, providing an additional layer of failover (Note: Tomcat provides some of this functionality natively via the Tribes component).

Both Nginx and HAProxy are fairly new technologies, with rapidly changing feature sets, so if you're thinking about integrating them into your clusters, it will be a good idea to run some benchmarks and compare their features during your discovery process.

Currently, HAProxy tends to be viewed as the more mature and stable project, but some people use a combination of HAProxy load balancing and Nginx reverse-proxying in an attempt to get the best of both worlds. Using Wakamole and Spread also requires some reading, as the peer to peer and floating IP techniques they employ can cause havoc on a shared network if not properly configured. However, according to those companies that have successfully integrated these solutions into their architectures ([Wordpress][5], for one), the work is worth it. You can find more information about setting up this kind of a system [here][6].

Other popular software-based load balancing solutions include [Zeus][7], [Pound][8], and [LVS][9].

  

Session Persistance
-------------------

The final piece of the clustering puzzle is session persistence - making sure that the information from an individual user's session is always available to them, even if the server currently hosting their session goes down, so that application state is maintained. There are a number of ways that session persistence can be factored into a cluster.

First of all, factoring the need to run in a clustered environment into the initial spec of an application can influence design decisions to a certain point. Non-complex state information that does not pose a security risk, such as the user's current tab, can be preserved on the client side via hidden fields, cookies, and URI-rewriting. These methods can be used effectively for a variety of data types, but are unsuitable for complex or security-sensitive operations.

Secondly, the majority of modern load balancers, including mod\_proxy and mod\_jk, support a feature called "session stickiness", which means that the load balancer remembers which cluster worker is storing the session information for each client's request, and proxies all concurrent requests from the same client to the same worker. While this ensures that state is maintained while all servers are working properly, if a server goes down for any reason, while the load balancer will begin directing requests to the remaining active servers, state data stored on the failed server will be lost.

Thus, a method of replicating the server-side session data must be provided to ensure that the cluster will truly never lose a transaction. There are several methods of doing this, which can be combined to create the best performing solution.

The simplest method of replicating session data within a cluster is to copy the data to at least one other worker. This "buddy system" method, in combination with some kind of health check or heartbeat function, allows the load balancer to detect when a server goes offline, and begin passing requests to its appropriate buddy worker.

Ideally, the client should perceive the service as uninterrupted. However, this method can introduce overhead under high loads - the load balancer must preserve increasing amounts of session-routing information, while the Tomcat workers take on database-like load in addition to their dynamic content processing load, which can create a bottleneck.

Load balancer bottleneck can be eliminated by using a multi-cast replication model, where each node of the cluster replicates its session data to every other node. For large environments, this can mean that the overall cluster is split into several smaller clusters using the DeltaManager component. However, small cluster set-ups without significant load should not experience these problems.

Other methods of achieving session persistence are to store the session information in a shared file system or JDBC-compliant database, or to use a cloud-based object cache system such as [Terracotta][10]. All of these methods carry an additional performance cost, as they require the additional step of writing and retrieving information to and from a database. However, as the overall goal of clustering is to improve availability, performance, and failover protection, this performance hit must be balanced against the other factors.

  

An Example Clustered Tomcat Configuration
-----------------------------------------

Tomcat provides fairly sophisticated clustering support, including several kinds of session replication, multicast or unicast heartbeat, cluster division, and more. Much of this configuration can be done right within the same XML configuration files as other Tomcat options, but there are some additional steps and options that can cause trouble.

To help you get started, we've created a step by step guide to [Tomcat Clustering][11], in which we walk you through everything you need to do to get a simple Tomcat cluster with session replication running behind Apache HTTPD. Check it out!

[1]: http://nginx.org/
[2]: http://haproxy.1wt.eu/
[3]: http://www.backhand.org/wackamole/
[4]: http://www.spread.org/
[5]: http://barry.wordpress.com/2008/04/28/load-balancer-update/
[6]: http://www.howtoforge.com/setting-up-a-high-availability-load-balancer-with-haproxy-wackamole-spread-on-debian-etch
[7]: http://www.zeus.com/products/load-balancer/
[8]: http://www.apsis.ch/pound/
[9]: http://www.linuxvirtualserver.org/
[10]: http://www.terracotta.org/
[11]: http://www.linuxtechtips.com/2013/01/tomcat-clustering.html

