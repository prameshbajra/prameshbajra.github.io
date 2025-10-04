---
layout: post
title:  "Deploy WhisperAI, FFMpeg and OpenAI in AWS Lambda using Docker Container"
date:   2023-05-22
description: "Deploy WhisperAI, FFMpeg and OpenAI into AWS Lambda Containers"
keywords: "ai, code, aws, docker, lambda, containers, ffmpeg"
categories: [ai, code, aws, docker, lambda, containers, ffmpeg]
tags: [ai, code, aws, docker, lambda, containers, ffmpeg]
icon: icon-antenna
---

Let's talk about working with AI, Docker and AWS Lambda. Sounds exciting, right? Maybe? 

But let me slide in a quick disclaimer: AWS Lambda might not be your first choice for AI tasks. 

These AI tasks are resource-intensive and sometimes prefer their tasks to be run on a GPU. But hey, who doesn't like a bit of challenge and fun?

As we start with this journey, let's keep few points in our mind:

1. Lambda functions can run for a 15-minute run, MAX. Default is 3 seconds. You might want to configure that.

2. When it comes to using docker containers as lambda functions, they have a "10GB max" size limit. No more. I tried ! :/

3. As of this date, Lambda doesn't support GPU, so remember this when you're tinkering around.


Alright, gear up, let's dive in.
<br><br>

First off, ensure you have docker running on your trusty laptop/PC.

You'll need three major files to get this show going:

A **handler.py** file - *our command center* - looking something like this:

```python
import os
import time
import boto3
import openai
import whisper

start = time.time()
# Load the model outside for a warm lambda executions... Seriously !! This helps !!
model = whisper.load_model("base", download_root='/tmp/')
end = time.time()
print("Time it took Whisper Model to load: ", end - start)

session = boto3.session.Session()
s3_client = boto3.client('s3')
# Security 101: Always keep your secrets ... You know .. SECRETS !! ...
client = session.client(service_name='secretsmanager', region_name='<YOUR_AWS_REGION>')
openai.api_key = client.get_secret_value(
    SecretId='<SECRETIDHERE_SHHH!!>')['SecretString']


def handler(event, context):
    # To run your lambda on a batch, consider iterating the records...
    # My lambda executes when a file is uploaded to a S3 bucket... Tweak this according to your needs ...
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    print("Commencing download: ", bucket, key)
    download_path = os.path.join('/tmp', os.path.basename(key))
    s3_client.download_file(bucket, key, download_path)
    print("Done downloading. Wow internet!")
    start = time.time()
    result = model.transcribe(download_path)
    end = time.time()
    print("Transcription time: ", end - start)
    return {
        "statusCode": 200,
        "result": result,
    }
```
<br>

The **requirements.txt** file - tending to the dependencies:
```text
boto3==1.26.137
openai==0.27.7
openai-whisper==20230314
```
<br>

And last but not least, the **Dockerfile** - our docker container creator, soon-to-be Lambda function core:
```Dockerfile
FROM public.ecr.aws/lambda/python:3.10-arm64

RUN yum -y update && \
    yum -y install tar gzip xz && \
    yum clean all && \
    rm -rf /var/cache/yum

RUN curl https://johnvansickle.com/ffmpeg/releases/ffmpeg-release-arm64-static.tar.xz -o ffmpeg.tar.xz && \
    tar -xf ffmpeg.tar.xz && \
    mv ffmpeg-*-static/ffmpeg /usr/local/bin/ && \
    rm -r ffmpeg.tar.xz ffmpeg-*-static

COPY requirements.txt  .
RUN pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Copy function code
COPY handler.py ${LAMBDA_TASK_ROOT}

# Set the CMD to your handler 
CMD [ "handler.handler" ]
```
<br>
Customize these files to meet your requirements, and voila! You're ready to launch your code into the AWS Lambda.
<br><br>

## Unleash the Deployment !!

Kick things off by building the docker image:
```shell
docker build -t image-name .   
```

To check if your creation is functioning as expected, put it through a local test run:
```shell
docker run -p 9000:8080 image-name 
```

And hope it works:
```shell
curl -XPOST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{}'
```

At this point, your terminal should return you with an output. 

Your docker image, now ready and waiting, needs to be uploaded to ECR (Elastic Container Registry) for its Lambda adventure.

To do this, you'll need an ECR repository. If you have one, use it by all means. If not, create an ECR repo with this command:
```shell
aws ecr create-repository --repository-name docker-image-ecr-repository --region <YOUR_AWS_REGION> --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
```

Your terminal will reward you with a response like this. COPY that `repositoryUri`. We'll need it to upload our docker image to the repository:
```json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:<YOUR_AWS_REGION>:XXXXXXXXXX:repository/docker-image",
        "registryId": "XXXXXXXXXX",
        "repositoryName": "docker-image",
        "repositoryUri": "XXXXXXXXXX.dkr.ecr.<YOUR_AWS_REGION>.amazonaws.com/docker-image",
        "createdAt": "2023-03-09T10:39:01+00:00",
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": true
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
```

But wait, there's more! Before you can upload the images to the repository, you need to prove your identity. Authenticate by executing this:
```shell
aws ecr get-login-password --region <YOUR_AWS_REGION> | docker login --username AWS --password-stdin <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_AWS_REGION>.amazonaws.com
```

Just one more teeny step. To guide it to the right ECR repository, you need to tag your docker image with the repository name, like so:
```shell
docker tag docker-image:latest <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_AWS_REGION>.amazonaws.com/docker-image-ecr-repository:latest
```

Trust me !! this is the final step! Now it's time to push the image.
```shell
docker push <YOUR_AWS_ACCOUNT_ID>.dkr.ecr.<YOUR_AWS_REGION>.amazonaws.com/docker-image-ecr-repository:latest
```

With your image now in ECR you are ready to deploy it to AWS Lambda. Here, you have a lots of choices. You can create lambda functions from the console or from tools like AWS SAM, CDK, Terraform, and more.

As always, if you hit any roadblocks or need some guidance, don't hesitate to give me a shout. 

**Happy Coding!**








