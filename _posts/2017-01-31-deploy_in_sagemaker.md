---
layout: post
title:  "Deploy your own custom trained object detection model in AWS Sagemaker"
date:   2019-10-13
description: "Deployment of your own object detection model in sagemaker."
keywords: "deploy, aws, sagemaker, model, object detection, sdk, tensorflow"
categories: [aws, sagemaker, prediction, detection, tensorflow, numpy, data, images, code, programming, deployment, s3, cloudwatch]
tags: [aws, sagemaker, prediction, detection, tensorflow, numpy, data, images, code, programming, deployment, s3, cloudwatch]
icon: icon-fire-alt
---

The main motive of this blog is to help others deploy their custom models to **Sagemaker**. Honestly speaking, I had to play around with this for 100+ hours in order to get this to work. At the time of writing this blog the sagemaker documentation is not consistent anywhere and lacks many tiny details. This method is not specific to object detection models and can be used to deploy any kind of models, be it custom/pretrained or downloaded from somewhere else.

Let's get started: <br><br>

## Prerequisites

Before reading this the reader is expected to have a general idea for generating model from tensorflow. You will need to that this part comes only after your model is successfully trained and the models are generated.

In order to deploy your models to **Sagemaker** you need to make sure of some things before you start. Firstly, make sure that the folder structure is something like this:

```
some_name 
    |__ Some positive number that represents version (For eg: 1) 
            |__ saved_model.pb 
            |__ variables 
                    |__ (Non empty)
```

Keep in mind that the **variables** folder should not be empty. The **variables** folder in most of the case are empty because the original tensorflow object detection tutorial exports a frozen graph instead of unfrozen one. Here, frozen means that all the variables are frozen (i.e. made constants). Because of this reason the **variables** folder is empty. We will have to export an unfrozen graph. Follow my [another blog](https://prameshbajra.github.io/aws/sagemaker/prediction/detection/tensorflow/tensorflow-serving/numpy/data/images/code/programming/deployment/s3/cloudwatch/2019/12/14/export-unfrozen-graph-tensorflow-object-detection.html) in order to export an unfrozen graph.

After you have the above folder structure you can compress it into a `some_name.tar.gz` format. Notice that we have a positive numbered folder inside `model` directory. Your `model` folder can have multiple positive numbered folders. These will be treated as versions and Sagemaker will choose the highest version (i.e. highest positive number inside model directory) to deploy. 
<br><br>
## Setup model for Sagemaker

After the prerequisites are done, you can proceed by uploading your `some_name.tar.gz` into **S3**. You can do it manually too. Just in case you want to upload it by using code here is the way to do it.

```python
from sagemaker.session import Session

model_data = Session().upload_data(path='<PATH TO some_name.tar.gz>', key_prefix='model')
print(model_data)
```

This will print the **S3** path to **some_name.tar.gz**. Make sure to copy it.
<br><br>
## Initialize the model

Sagemaker SDK is very powerful and amazing. You can use one line code to create a model, it's respective endpoint configuration and endpoint. The model can be initialized by using the code below:

```python
from sagemaker.tensorflow.serving import Model

# Use an env argument to set the name of the default model.
# This is optional, but recommended when you deploy multiple models
# so that requests that don't include a model name are sent to a
# predictable model.
env = {'SAGEMAKER_TFS_DEFAULT_MODEL_NAME': 'some_name'}
# set specific role
sagemaker_role = "YOUR ROLE NAME FOR SAGEMAKER"

model = Model(
    model_data=
    '<Paste the S3 path to some_name.tar.gz>',
    role=sagemaker_role,
    framework_version="1.14",
    env=env)
```

Another thing to keep in mind here. The **framework_version** that you provide when initializing the model above must be same as the version of tensorflow that was used to train the model. So, make sure to do some saerching on the trained version before using any random version for deployment.
<br><br>
## Deploy the model

Use the code below to deploy the model. **Sagemaker** will do the heavy lifting for you from here on and create an endpoint that will be ready to take in inputs and return your predictions. `The model.deploy()` method will return a **predict** object that can take in inputs and give out predictions.

```python
# This will take some time ... Grab a coffee, take a break ...
predictor = model.deploy(initial_instance_count=1,
                         instance_type='ml.t2.medium')
```
Based on you requirements you can increase the `initial_instance_count` and change the `instance_type` to a more powerful instance. You can even set a `accelarator_type` too by simply adding a parameter to `model.deploy()` function. Eg: `predictor = model.deploy(initial_instance_count=1, instance_type='ml.c5.xlarge', accelerator_type='ml.eia1.medium')` 
<br><br>
## Get predict from endpoint

From the predictor object you can get the **endpoint_name** that the model has been deployed to. This method is necessary because every time you will call `predict()` it is not feasible to deploy the model. What you can do is get the predictor object from the endpoint. You can do this by :

```python
from sagemaker.tensorflow.serving import Predictor

predictor = Predictor(endpoint_name = "<Your endpoint name>")
```

There are other ways to do this too. You can use `RealtimePredictor` that sagemaker provides. I won't be including that here as that would make this a long post.
<br><br>
## Testing is must

We are on the final stage now. We need to get the prediction done. But wait, sagemaker endpoint only accepts json/csv format (Not sure why). We have to pass image to this. We can do this by :

```python
import cv2
import numpy as np

headers = {"content-type": "application/json"}
image_content = cv2.imread("<Path to your image>",
                           1).astype('uint8').tolist()
body = {"instances": [{"inputs": image_content}]}

results = predictor.predict(body)

print(results)
```

This will get you some output in **dict** format having elements like **detection_classes**, **detection_boxes** etc. This output  that you get here is similar to the one you get when you run object detection in tensorflow. You will have to arrange or even write up some code in order to get the co-ordinates for detections done.

Feel free to ping me anywhere in social media if you get stuck somewhere or in case you have some questions.



