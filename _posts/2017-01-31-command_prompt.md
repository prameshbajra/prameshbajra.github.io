---
layout: post
title:  "Pimp Your Command Prompt/Cmd in Windows"
date:   2017-08-25
desc: "Make your CMD stand out and add some features to it to make life easier. "
keywords: "windows, prompt, cmd, clink "
categories: [windows , cmd, command prompt, clink]
tags: [windows , cmd , clink, command prompt, programming , code ]
icon: icon-google-developers
---

Bored with plain old command prompt? You're in the right place then. Welcome.

Let's start by changing the format of your current CMD. Follow along and please do ask if you get stuck somewhere.<br><br>

1. Open your __CMD / Command Prompt__ , copy this > `setx prompt $$ $C$P $L--$G $D$F$_$C$$$F -$G ` and paste it. Then press enter. (You might have to restart your __CMD / Command Prompt__) 

2. Your __CMD__ should now look something like 
     
    > `$ (C:\Windows\Temp <--> 2017-08-03)`
    >
    >  `($) -> █`
 
    <br>
    If you do not like this format then you can customize it yourself. Enter `prompt /?` and see the formatting options.
    For your convienence they are mention below:
    <br>
    Start with `setx prompt ` then make your own format as above.
    <br>
    <pre>
    - $A       &           (Ampersand) 
    - $B       |           (pipe) 
    - $C       (           (Left parenthesis) 
    - $D                    Current date 
    - $E                    Escape code  (ASCII code 27) 
    - $F       )           (Right parenthesis) 
    - $G       >           (greater-than sign) 
    - $H       Backspace   (erases previous character) 
    - $L       <           (less-than sign) 
    - $M       Display the remote name for Network drives
    - $N       Current drive 
    - $P       Current drive and path 
    - $Q       =           (equal sign) 
    - $S                    (space) 
    - $T       Current time 
    - $V       Windows NT version number 
    - $_       Carriage return and linefeed 
    - $$       $           (dollar sign)
    - $+       Will display plus signs (+) one for each level of the PUSHD directory stack
    </pre>

3. I'm guessing you haven't changed the font and color yet. In case you have or you like the default one skip this step. Right click on the title bar and go to **properties** , select **Font** tab and choose any font of your liking. Then go to **Colors** and choose your preferable color for screen text and screen background. After you're done press **OK**.
<br>

Very simple, Isn't it?   
Now let's add a feature that __preserves history between sessions__ and __tab on completion__.
This is very simple just download [Clink](http://mridgers.github.io/clink/) and install it. 
<br>
<br>
### Annnnnd!! You're done. Congratulations!