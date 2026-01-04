---
layout: post
title: "Bastion Servers: Jump Hosts"
date: 2026-01-04
description: "A quick look at bastion servers."
keywords: "bastion server, jump host, api gateway, load balancer, cloud security, infrastructure access"
categories: [cloud, security, infrastructure, networking]
tags: [bastion servers, jump host, api gateway, load balancer, cloud, security]
---

I was recently talking to my friend, and we were discussing a couple of things about system architectures and cloud in general. 
He then uttered a heavy word "bastion servers" in the conversation, and I realized I didn’t actually know what that was. He did a 
super good job explaining it, but I wanted to solidify my understanding further.

So today, I looked it up and thought I’d share what a bastion server is—and what I was initially confusing it with.

<br>

# 🛡️ Bastion Server (a.k.a. Jump Host) <br><br>

What is a "Bastion"?

A "bastion" is basically a fortified stronghold or a defensive position used to protect a larger area. Something like this.

<img src="/static/assets/img/blog/bastion/bastion.jpg" width="40%"
alt="Bastion fortress image">

<br>

In the context of IT and cloud computing, a bastion server is a secure entry point for administrators/developers to access internal systems.

Instead of exposing all your servers to the internet, you expose one highly secured machine. Admins/developers first connect to this bastion (usually via SSH or RDP), and from there, they “jump” into private servers that are otherwise unreachable from outside. Think of it as a fortified entry point that admins must pass through to access internal servers. Instead of exposing your entire network to the internet, you expose just this one server. From there, admins can "jump" into the internal systems safely. It's all about providing a controlled and logged way for humans to do administrative work without opening up your entire environment.

**Key points:**

- Used mainly by humans (admins, SREs, developers)

- Focused on secure access, not traffic routing

- Heavily hardened and audited

- Common in cloud setups with private subnets

**Important:** Think of it as a security checkpoint, not a traffic manager.

<br>

# 🚪 API Gateway <br><br>

This is where my confusion initially came from.

An API gateway is an entry point for application traffic, not admin access. In many microservice architectures, all services are accessible only through the API gateway.

**What it typically does:**

- Authentication & authorization (users, roles, tokens)

- Routing requests to the correct microservice

- Rate limiting, logging, versioning, etc.

<br>

Even though both a bastion server and an API gateway act as “gatekeepers,” they protect very different things:

Bastion → protects infrastructure access

API Gateway → protects application APIs

<br>

# ⚖️ Load Balancer <br><br>

A load balancer has yet another job:

- Distribute incoming traffic across multiple servers

- Improve availability and reliability

- Prevent any single server from being overwhelmed

It doesn’t care who the user is (that’s auth), and it doesn’t care how admins log in. It just spreads traffic efficiently.

<br>

# 🧠 Simple Mental Model <br><br>

Bastion Server → “How do admins get into private servers safely?”

API Gateway → “How do users access my APIs securely?”

Load Balancer → “How do I spread traffic across servers?”

<br>

Each solves a different problem, and they often coexist in the same architecture.

This was a great reminder for me that similar-sounding components can have very different responsibilities. 

Hope this helps someone else who might be mixing these up too 🙂

