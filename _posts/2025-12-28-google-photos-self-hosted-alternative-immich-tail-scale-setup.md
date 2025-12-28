---
layout: post
title:  "Google Photos Self-Hosted Alternative: Immich + Tail Scale Setup."
date:   2025-12-28
description: "Self-hosted photo library on a home server using Immich and Tailscale"
keywords: "self-hosted, photos, immich, tailscale, home-server, homelab"
categories: [self-hosted, homelab, photos, immich, tailscale]
tags: [self-hosted, homelab, photos, immich, tailscale]
---

## Summary: 

In short, I did not want to pay for Google Photos storage. I had been wanting 
to self-host a Google Photos alternative for a long time now and the time finally 
came. So I picked up a BeeLink box, moved my photo library to Immich, and
set up Tailscale for secure access from anywhere.

I have been spending a lot of time on the new server recently, and this small project
is just perfect for something like this. Moving off Google Photos felt like the
perfect excuse to make the server useful in practice, not just in my head.

<br>
## Why this setup

I wanted a self-hosted photo library that feels modern, works flawlessly and I 
wanted it to be securely accessible from anywhere. The combo of Immich and 
Tailscale does exactly that.

<br>
## What Immich is for

Immich is an open-source, self-hosted alternative to Google Photos. It handles
photo uploads from your phone, organizes everything into a timeline, and gives
you albums and search without handing your library to a third party. For me,
at least for now, Immich might be the place where all my photos will live going forward.

This is how Immich looks like. Looks very familiar right? It's just google photos, but self-hosted.
<br><br>

<img src="/static/assets/img/blog/immich/immich-screenshots.png" width="95%"
alt="Immich web interface screenshot">

<br>
## Basic Immich setup

I do not want to bore you with the installation steps here as it literally is done by running couple of commands. 
Here is the short version that I followed. The official docs are here:
<a href="https://docs.immich.app/overview/quick-start" target="_blank">https://docs.immich.app/overview/quick-start</a>

<br>
## What Tailscale is for

Tailscale is for secure remote access. It creates a private network
between my devices so I can reach Immich from my phone or laptop when I am away
from home. It runs on top of WireGuard, handles device authentication, and keeps
traffic encrypted without me touching port forwarding.


<a href="https://tailscale.com/" target="_blank">https://tailscale.com/</a>

By the way, Tailscale is amazing and it does other amazing things as well. I sometimes wonder how it is free. 

<br>
## High-level setup

Here is the simple version of what I did:

- My home server runs Docker and hosts the Immich containers.
  
- Photos are stored on a dedicated disk attached to the server.

- Tailscale runs on the server and on my personal devices.

- I use the Tailscale IP (or MagicDNS) to open Immich when I am not on Wi-Fi.

<br>
## What I want to improve next

This is the first step, not the final step. I still want to set up backups for the photo storage to S3 deep archive or something similar.

If you are also building a home server, this setup is a great way to make it
feel instantly useful. I will keep iterating as I go.
