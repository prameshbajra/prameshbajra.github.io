---
layout: post
title:  "Deploy Node - Express Application as NPM packages"
date:   2019-06-29
desc: "Deploy Express application as npm packages and publish it to npm registry."
keywords: "javascript, npm, programming, registry, express, node, code, login, deploy, server, ejs"
categories: [javascript, npm, programming, registry, express, node, code, login, deploy, server, ejs]
tags: [javascript, npm, programming, registry, express, node, code, login, deploy, server, ejs]
icon: icon-nodejs
---

I recently came around this problem where I needed to deploy an express application as a npm package, but to my suprise
there were no article explaining how it's done. Weird right?

First of all, I am not sure why you would want to do this. For me this was just a play- around thing. Turns out, this is easy AF.

First, setup you express project. I did this like:

    express --ejs myApplication

If you are not sure what this is then please check out `express-generator`, you can install it by:

    npm i -g express-generator

Here's a reference for convienence. [Express generator](https://expressjs.com/en/starter/generator.html)

Just to make things clear beforehand we won't be changing anything in the application itself.
Most of the changes will be in the `package.json` file.

Your `package.json` file would look something like this at first:

    {
        "name": "package-name",
        "version": "0.0.1",
        "private": true,
        "scripts": {
            "start": "node ./bin/www"
        },
        "dependencies": {
            "Your dependancies here"
        }
    }

You should add some elements here such that your final `package.json` would look something like this:

    {
        "name": "package-name",
        "version": "0.0.1",
        "private": false,
        "main": "./bin/www",
        "scripts": {
            "start": "node ./bin/www"
        },
        "bin": {
            "package-name": "./bin/www"
        },
        "dependencies": {
            "Your dependancies here"
        }
    }


Watch out for the `"private": false` part if you are going to release you npm package as public.

We are pretty much done at this point.

Before publishing make sure that you have your account set up at : [NPM JS](https://npmjs.com)
and login from terminal.

You can login to npm from your command line using :

    npm login

After this you can simply:

    npm publish


If everything is good and god is on your side then you should be able to publish your package successfully.
Give it a try and let me know which app you published. I'd be happy to use it.

If there is any doubt along the way, please feel free to drop a mail or contact me through any means.





