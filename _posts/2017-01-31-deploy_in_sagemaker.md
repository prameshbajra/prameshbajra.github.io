---
layout: post
title:  "Deploy your own custom trained object detection model in AWS Sagemaker"
date:   2019-12-13
desc: "Deployment of your own object detection model in sagemaker."
keywords: "deploy, aws, sagemaker, model, object detection, sdk, tensorflow"
categories: [aws, sagemaker, prediction, detection, tensorflow, numpy, data, images, code, programming, deployment, s3, cloudwatch]
tags: [aws, sagemaker, prediction, detection, tensorflow, numpy, data, images, code, programming, deployment, s3, cloudwatch]
icon: icon-fire-alt
---

The main motive of this blog is to help others deploy their custom models to sagemaker. Honestly speaking, I had to play around with this for 100+ hours in order to get this to work. At the time of writing this blog the sagemaker documentation is not consistent anywhere and lacks many tiny details. This method is not specific to object detection models and can be used to deploy any kind of models, be it custom/pretrained or downloaded from somewhere else.

Let's get started: <br><br>

## Prerequisites

In order to deploy your models to Sagemaker you need to make sure of some things before you start. Firstly, make sure that the folder structure is something like this:

```
model 
    |__ Some positive number that represents version (For eg: 1) 
            |__ saved_model.pb 
            |__ variables 
                    |__ (Non empty)
```

