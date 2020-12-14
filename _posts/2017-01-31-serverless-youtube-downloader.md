---
layout: post
title:  "Youtube Downloader - Serverless"
date:   2020-12-14
desc: "I believe in serverless and I think this is the future."
keywords: "programming, python, serverless, aws, youtube, npm, js, code, frontend, backend"
categories: [programming, python, serverless, aws, youtube, npm, js, code, frontend, backend]
tags: [programming, python, serverless, aws, youtube, npm, js, code, frontend, backend]
icon: icon-nodejs
---

Before blabbering about the application that I made recently, I would like to shine some light on what serverless really is. **Serverless** is a cloud computing execution model in which the cloud provider (like google cloud/azure/amazon web services) runs the server, and dynamically manages the allocation of machine resources. In layman's term, it means that there are no servers running untill and unless there is a necessity for it to run.
<br><br>
<h2>Serverless, I choose you.... But, why?</h2>

I did it simply because I wanted to learn. Learning exiciting new stuffs and writing about them has become my niche these days. My motive aside, there are several good things that serverless brings to the table. The most important being the cost saving features. If you are a company that caters thousands, if not millions of users, then this might be a ground breaking thing but for me, this was not the main reason. 

I went with serverless because it auto-scales without additional work. While, it is fun to come up with system architecture where everything is implemented in house, it sometimes becomes tedious if you just want you go live and make things work. Some other points that I love about serverless are:

- it scales with demand automatically
  
- it significantly reduces server cost (70-90%), because you don’t pay for idle
  
- it eliminates server maintenance
  
- it frees up developer resources to take on projects that directly drive business value (versus spending that time on maintenance)

<br>
<h2>Let's talk about the application - How to use it?</h2>

You can simply head over to [Youtube Download - Bazra](http://d2ty6b2yjm83if.cloudfront.net/) to have a look for it yourself. The site is very simple (My 12 year old brother was able to figure out how to download the videos without guidance).

So, first thing first, right after you visit the site you will see a place to enter a link for the video you want to download from **YouTube**. If you are from a laptop/computer, you can simply copy the link from the top address bar and paste it in the site and hit enter (or click download). If you are from a mobile you can share the video and copy the link (either way, it works) and paste it into the site and download it.

Done! Your video will be downloaded. Simple, isn't it?

> *This is the first version release. After you click download the video will be downloaded in the highest resolution available.*

<br>
<h2>Technicalities - How it was build</h2>

I have used the following:

- [AWS (Amazon web services)](aws.amazon.com)
    
    I use AWS to host all my backend code. The core services I use are: Cloudfront (fast content delivery network (CDN)), S3 (to save videos and host this site), Lambda (backend code), Cloudwatch (for logs). *Let me know if you want to get started with AWS too. I can set up an account for you. I have couple hundred dollars lying passive here.*
  
- [Serverless Framework](http://serverless.com/)

    This is an awesome framework to which I should provide a `.yml` configuration file and it will setup all the infrastructure in any cloud provider (in my case AWS). There are plugins involved as well.

- [Angular 10](https://angular.io/)

    It is another amazing platform for building mobile and desktop web applications.

- [Python 3](https://www.python.org/)

    Programming language of my choice. I use packages like boto3, pytube etc.

- [Docker](https://www.docker.com/)

    This deserves a whole long blog post on itself. But, just for this application it is needed to bundle python dependencies to deploy it as lambda functions on aws.

If you are already familiar with these then you can hop to my github repository where all the code is present. If you are interested, I would love to have contributions.

> *Please text me, or get in touch through any medium if you would like to discuss more on it. I love tech gossips.*

[GITHUB: **Youtube Downloader - Bazra**](https://github.com/prameshbajra/serverless-works/tree/master/yt-bazra-download)

<br>
<h2>Future Plans</h2>

1. I will be updating this site next weekend with more features like video download based in resolution you select. Good news! The backend is already done. 

2. Then, I will also be adding an audio download feature where you can just give the youtube URL and audio file will be downloaded instead of video.

3. I will be adding a contributors page and a documentation page as well.

4. I have lot of interest in creating a browser extension as well, but let's see where this goes.

5. There might be ads later. Maybe after some user traffic? Also, I will be using the money to donate to some good cause. The infrastructure will be handled by be as long as it is under my budget. 

5. This is not yet decided but, I will be publishing the APIs for free and will provide a concise documentation.

<br><br>
> **As always, I would love to hear back. Feel free to drop suggestions and also let me know what I should add?**
> **My emails and messages are always open. And, there is a comment box below if in case you did not notice. :P **