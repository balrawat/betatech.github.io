---
layout: post
title: Active vs Passive FTP
date: '2013-02-24T15:46:00.002+05:30'
author: Balvinder Rawat
tags:
  - active ftp
  - passive ftp
  - windows
  - ftp
  - ftp modes
modified_time: '2014-01-07T12:52:15.569+05:30'
thumbnail: >-
  https://4.bp.blogspot.com/-b4CsQvy4MM4/USnklu9foBI/AAAAAAAAASc/RZddGj_zT7c/s72-c/1.png
blogger_id: 'tag:blogger.com,1999:blog-6814921223515313000.post-6302645972960415183'
blogger_orig_url: 'https://www.linuxtechtips.com/2013/02/active-vs-passive-ftp.html'
---
  

When a client experiences problems when connecting to your FTP server, one thing you might want to look into is whether you've set your FTP data transfer mode to either active or passive. 

Active and passive are two possible modes that an FTP connection can operate on. Taking into consideration the network configurations and security controls in place, you should choose one mode over the other.

But before we discuss which mode is best for what scenario, let's first talk about the basics of these two modes, which can best be explained if we start our discussion with the two channels an FTP session normally has.

#### **FTP command channel and data channel**

A typical FTP session operates using two channels: a command (or control) channel and a data channel. As their names imply, the command channel is used for transmitting commands as well as replies to those commands, while the data channel is used for transferring data. 

Unless you configure your FTP server differently, you will normally set your command channel to use port 21. The port you'll use for the data channel, on the other hand, can differ depending on which data transfer mode you choose. If you choose active mode, then the data channel will normally be port 20. But if you choose passive mode, then the port that will be used will be a random port. 

[![](https://4.bp.blogspot.com/-b4CsQvy4MM4/USnklu9foBI/AAAAAAAAASc/RZddGj_zT7c/s1600/1.png)][1]

  

Note that the ports we are referring to here up to this point are only the ports on the server side. We'll include client-side ports in our discussion in a short while.

#### **Active mode FTP**

Among the two modes, Active mode is the older one. It was the mode introduced in the early days of computing when mainframes were more common and attacks to information security were not as prevalent. 

Here's a simplified explanation on how an active mode connection is carried out, summarized in two steps. Some relevant steps (e.g. ACK replies) have been omitted to simplify things.

1.  A user connects from a random port on a file transfer client to port 21 on the server. It sends the PORT command, specifying what client-side port the server should connect to. This port will be used later on for the data channel and is different from the port used in this step for the command channel.
2.  The server connects from port 20 to the client port designated for the data channel. Once connection is established, file transfers are then made through these client and server ports.

[![](https://4.bp.blogspot.com/-qZK35NAxm94/USnkluioQeI/AAAAAAAAASY/Yp9BwRDaMD0/s1600/2.png)][2]

#### **Passive mode FTP**

In passive mode, the client still initiates a command channel connection to the server. However, instead of sending the PORT command, it sends the PASV command, which is basically a request for a server port to connect to for data transmission. When the FTP server replies, it indicates what port number it has opened for the ensuing data transfer. 

Here's how passive mode works in a nutshell:

1.  The client connects from a random port to port 21 on the server and issues the PASV command. The server replies, indicating which (random) port it has opened for data transfer. 
2.  The client connects from another random port to the random port specified in the server's response. Once connection is established, data transfers are made through these client and server ports.

[![](https://4.bp.blogspot.com/-XPrUgtQipJ8/USnkl0KTCqI/AAAAAAAAASg/0Sy6KaN70Ew/s1600/3.png)][3]

  

  

#### **Active mode vs Passive mode - which is more suitable for you?**

There's a reason why I opted to simplify those two diagrams above. I wanted to focus on the main difference between active mode and passive mode FTP data transfers. If you compare those two diagrams, one of the things that should really stand out are the opposing directions at which the **second** arrows (which also represent the data channels) are pointing to.

In this section, we'll focus on those second arrows and the ports associated with them.

In the active mode, the second arrow is pointing to the client. Meaning, the client initially specifies which client-side port it has opened up for the data channel, and **the server initiates the connection**. 

By contrast, in the passive mode, the second arrow is pointing to the server. Here, the server specifies which server-side port the client should connect to and **the client initiates the connection**.

There shouldn't be any problem had there not been any firewalls in existence. But threats to information security are on the rise and hence the presence of firewalls is almost always a given. In most cases, clients are located behind a firewall or a NAT (which basically functions like a firewall). In such cases, only a select number of **predefined**ports are going to be accessible from the outside. 

Remember that in an active mode configuration, the server will attempt to connect to a **random**client-side port. So chances are, that port wouldn't be one of those predefined ports. As a result, an attempt to connect to it will be blocked by the firewall and no connection will be established.

[![](https://2.bp.blogspot.com/-i7wKZMOByq4/USnkmWUXEAI/AAAAAAAAASo/fKipRKFiTsY/s1600/4.png)][4]

  

  

  

In this particular scenario, a passive configuration will not pose a problem. That's because the client will be the one initiating the connection, something that a client-side firewall won't have any problem with.

  

  

[![](https://1.bp.blogspot.com/--8frrShuXRY/USnkmlQ4irI/AAAAAAAAASw/T5kfaA8hojM/s1600/5.png)][5]

Of course, it's possible for the server side to have a firewall too. However, since the server is expected to receive a greater number of connection requests compared to a client, then it would be but logical for the server admin to adapt to the situation and open up a selection of ports to satisfy passive mode configurations.

#### **Security considerations when setting up passive FTP**

As explained earlier, if you're administering an FTP server, it would be best for you to configure your server to support passive mode FTP. However, you should bear in mind that in doing so, you would be making your system more vulnerable to attacks. Remember that, in passive mode, clients are supposed to connect to random server ports.

Thus, to support this mode, not only should your server have to have multiple ports available, your firewall should also allow connections to all those ports to pass through!

But then the more open ports you have, the more there will be to exploit. To mitigate the risks, a good solution would be to specify a range of ports on your server and then to allow only that range of ports on your firewall.

#### **Where to set up passive port range in FILEZILLA FTP Server**

  

For those of you who are already using FILEZILLA FTP Server, you can specify a range of ports for your passive mode FTP connections by going to **Edit > Settings** \> **Passive mode settings** in your FILEZILLA Server Interface. Because low ports (particularly those < 1024) are reserved, choose a high port range (i.e. large numbers). For example, from 5000 to 6000. For better security, don't just copy the example. Use your own!

  

  

[![](https://3.bp.blogspot.com/-IH6imBiPOHI/USnobk0JhwI/AAAAAAAAATM/pvvh9rm_yIE/s1600/Capture.JPG)][6]

  

  

  

In the event that the IP address your server uses in responding to requests for passive connections is not routable via the Internet, you'll need to enter your public IP address in the **Passive IP** field. 

[1]: https://4.bp.blogspot.com/-b4CsQvy4MM4/USnklu9foBI/AAAAAAAAASc/RZddGj_zT7c/s1600/1.png
[2]: https://4.bp.blogspot.com/-qZK35NAxm94/USnkluioQeI/AAAAAAAAASY/Yp9BwRDaMD0/s1600/2.png
[3]: https://4.bp.blogspot.com/-XPrUgtQipJ8/USnkl0KTCqI/AAAAAAAAASg/0Sy6KaN70Ew/s1600/3.png
[4]: https://2.bp.blogspot.com/-i7wKZMOByq4/USnkmWUXEAI/AAAAAAAAASo/fKipRKFiTsY/s1600/4.png
[5]: https://1.bp.blogspot.com/--8frrShuXRY/USnkmlQ4irI/AAAAAAAAASw/T5kfaA8hojM/s1600/5.png
[6]: https://3.bp.blogspot.com/-IH6imBiPOHI/USnobk0JhwI/AAAAAAAAATM/pvvh9rm_yIE/s1600/Capture.JPG

