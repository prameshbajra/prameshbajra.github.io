---
layout: post
title:  "Make your shell pretty."
date:   2021-06-21
desc: "Your development environment should be clean and cool."
keywords: "code, windows, programming, shell, commandline, cli"
categories: [code, windows, programming, shell, commandline, cli]
tags: [code, windows, programming, shell, commandline, cli ]
icon: icon-fire-alt
---

Hey, I hope you are doing well. Before starting to blabber about the customization that we are going to make today, let me give you a sneak peek on what we are going to achieve at the end of this article.

<img src="/static/assets/img/blog/powershell/prettypowershell.png" width="95%">

It is a clean and nice looking terminal, isn't it? As a guy who works with code nearly all the time, this place should be very familiar to you. 

<br>

## Why would you want this?

Trust me, you do. It looks aesthetically pleasing and clean. If you are like me, then terminal shells like this will make you want to use it more, making you more productive.

<br>

## Shut up and get to the point. How do I get this installed?

Ok. Before we start I would strongly recommend you to download some of these fonts because windows default fonts sucks and, these are the ones that support the icons and ligratures really well.

<a href="https://www.nerdfonts.com/font-downloads" target="_blank"> DOWNLOAD NERD FONTS</a>

> Note: You do not need to download all these fonts. Just download the one you want and install it. All you will need to do is extract the `.zip` and double click on the font files to install it.

<br>

## Done? Good. Now,

The page that I am referring is <a href="https://ohmyposh.dev/docs/windows" target="_blank">here (oh-my-posh)</a>. Feel free to jump there if you are confident to install it. I will walk you through the installation steps anyways. I highly suggest you to use `Windows Terminal` as it is amazing and any further customization is a piece of cake.
You will need either `winget` (is an awesome package manager for windows, try it out if you have not yet!) or `scoop` (similar to winget, but older?).
I will be using `winget`, but the process is exactly the same for `scoop` too. For the future readers, you might want to see if your windows already has `winget` installed, as Microsoft will be shipping `winget` by default in all Windows machines soon.

Install `oh-my-posh`:

    winget install JanDeDobbeleer.OhMyPosh


Then, open your `Powershell` and follow the steps below (Remember, it has to be powershell or else it will not work).You will need to add a single line to a file here.

    notepad $PROFILE

and add the below line to the file. If you already have some text in that file then add this line to the bottom of the text. Also, remember to replace `[PATH]` with the path to that `json` file. It should be under `~\AppData\Local\Programs\oh-my-posh\themes\` for almost everyone.

    oh-my-posh --init --shell pwsh --config [PATH]/jandedobbeleer.omp.json | Invoke-Expression

now the final step is to reload the shell:
    
    . $PROFILE

and you're done.


By default there are a bunch of themes that this tool provides but I prefer to customize it further and make my own adjustments.
You can download my custom theme from <a href="https://gist.githubusercontent.com/prameshbajra/42dff56bbd229bad9ca8f5571d70c8cc/raw/dc145db13e2c86e57523290d71e0ee53d239b1be/pramesh.omp.json" target="_blank">here (prameshbajra github)</a>. Simply download this `json` and place it along with with `jsons` inside folder : `~\AppData\Local\Programs\oh-my-posh\themes\`.

You must also edit this line to:

    oh-my-posh --init --shell pwsh --config [PATH]/pramesh.omp.json | Invoke-Expression 

and do:

    . $PROFILE

You can have a look at the whole list of themes <a href="" target="_blank"> here</a>.

Enjoy your new theme. 

<br>

## Oh wait, one more thing,

The customizations you make here will also be applied in VSCode integrated terminal. So it is definitely a win-win.

<img src="/static/assets/img/blog/powershell/vscodepowershell.png" width="95%">

<br>

As always feel free to reach out if you have any queries. I love talking tech anytime. 

    
