---
layout: post
title:  "I wrote a SERVER that might be of use to YOU!!"
date:   2020-08-16
desc: "Share files with a powerful http server."
keywords: "nodejs, node, multer, code, server, file, network, http, express, ejs, code"
categories: [nodejs, node, multer, code, server, file, network, http, express, ejs, code]
tags: [nodejs, node, multer, code, server, file, network, http, express, ejs, code]
icon: icon-maven
---

## What is it?

It is like any other `http file server` but on **steroids**. Why?

Because it not only provides you the file sharing capabilities but also tags along other great features like *download as zip* and *upload to the server*.
<br><br>

## Is it a complete thing?

No, not really. In fact, this is nowhere close to done. I will be adding a vast array of features down the line. Please stay tuned.
<br><br>

## Why did I make this?

Duhhhh! Because I can. 

Kidding aside. In my daily office works, I need to move files back and forth between multiple computers/laptops connected under a same network. So, this makes my (and my collegues) life much simpler and easier.
<br><br>

## How to use it?

Ok, enough blabbering. Let's get started. You will need **Node** installed on your laptop/computer and both the system you want to transfer files to and from should be under the same network. Basically, it needs to be connected to the same wifi network. In case, you have not installed **Node**, you can do so from [this link](https://nodejs.org/en/).

Node will automatically install **npm (Node Package Manager)** for you from where you can install many other packages. It is like a market for node applications where you can pick stuffs and use it. 

So, 

1. Open a terminal/cmd/shell on your host machine (the machine from which you want to transfer the files to), and type:

        npm install -g see-my-files

    This will install the required things that you will need to run the application.

2. Then right after it you can simply do:

        see-my-files

    This will open up a server and give you a link. 

The link that just got printed after running the above command can be used in any other computer to open a file system. The link should look something like: `http://192.168.1.11:3300`. Note this link and on the other computer simply open a browser and navigate to this very link.

You will see something link this:

<img src="/static/assets/img/blog/see-my-files/see-my-files.png" width = "70%">

To **downlaod a file** simply **click** on the file. It will automatically be downloaded. To **download a folder** you can right click on it and press **download as zip**. To **upload something** to the source machine you can simply **drag the file to the folder icon**. The upload will be done automatically.

Well. That's it for this article. I really hope you find this useful.
<br><br>
As always, feel free to reach out to me if you need help.
<br><br>
## Are you a developer as well?

Feel free to contribute: [https://github.com/prameshbajra/see-my-files](https://github.com/prameshbajra/see-my-files)

