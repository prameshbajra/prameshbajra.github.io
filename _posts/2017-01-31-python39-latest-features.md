---
layout: post
title:  "Python 3.9 - Latest Features"
date:   2020-10-03
desc: "Python is coming up with some cool nifty features. Let's check out some of them here."
keywords: "code, python, features, programming"
categories: [code, python, features, programming]
tags: [code, python, features, programming]
icon: icon-fire-alt
---

Please allow me to start with a disclaimer: I am a big **JavaScipt** fan and I only keep track of the latest features for **JavaScript**. The language (*JS*) has added very handy features in recent years and I can't stop fan girling about them.

Ok then, with that out of the way. Let's talk **python** today. This is my first time looking and using the latest features provided by any programming language other than **JavaScript** and honestly, I am very impressed.
<br><br>
<h2>Let's jump right in</h2>
<br>
To make things easier I will be ignoring all the other additions that I did not find very interesting. I mean, I will only mention those latest features which I think will be worth mentioning and will be of some use to us developers.


1. <b>The union operator for dictionaries (| and |=)</b>

    In earlier versions, to merge 2 dictionaries you would do something like:

    ```python
    python = {2000: "2.0.1", 2008: "2.6.9", 2010: "2.7.18"}
    python3 = {2008: "3.0.1", 2009: "3.1.5", 2016: "3.6.12", 2020: "3.9.0"}

    ##merging two dictionaries
    {**python, **python3}

    # or
    python.update(python3)
    ```

    But, now you can simply do

    ```python
    ##merging two dictionaries
    python | python3

    # and update dictionary
    python |= python3
    ```

    both of the above code will update *python* dictionary to

    ```json
    {
        2000: "2.0.1",
        2008: "3.0.1",
        2010: "2.7.18",
        2009: "3.1.5",
        2016: "3.6.12", 
        2020: "3.9.0"
    }
    ```

    Pretty sleek, don't you think?
   
   
2. <b>removeprefix() and removesuffix() FINALLY !!!</b>
   
   I do not know about you, but this is a must have for me. I personally, have to work with many file operations where saving a file with new name is a common job. 

   In Python 3.9, there are two new string methods that solve this exact use case. You can use .removeprefix() and .removesuffix() to remove the beginning or end of a string, respectively:

   ```python
   # In older python code:
   document_file_name = "pramesh.pdf"
   json_file_name = f"{document_file_name.split(".")[0]}.json"

   # In python 3.9, I can just do:
   document_file_name = "pramesh.pdf"
   json_file_name = f"{document_file_name.removesuffix(".pdf")}.json"
   ```

   Much clear, isn't it?

3. <b>math.gcd() and math.lcm() now works with list of numbers.</b>

    Earlier, you could do this

    ```python
    import math
    # This worked ...
    print(math.gcd(49, 14)) # 7

    # But this did not ...
    print(math.gcd(273, 1729, 6048)) # 7
    ```

    Now, wahh laaa!! The second one works too. And, same thing applies to LCM as well. You will now be able to use these functions as

    ```python
    print(math.gcd(273, 1729, 6048)) # 7
    ```


4. <b>zoneinfo</b>

    The zoneinfo module brings support for the IANA time zone database to the standard library. It adds zoneinfo.ZoneInfo, a concrete datetime.tzinfo implementation backed by the system’s time zone data.

    ```python
    >>> from zoneinfo import ZoneInfo
    >>> from datetime import datetime, timedelta

    >>> # Daylight saving time
    >>> dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
    >>> print(dt)
    2020-10-31 12:00:00-07:00
    >>> dt.tzname()
    'PDT'

    >>> # Standard time
    >>> dt += timedelta(days=7)
    >>> print(dt)
    2020-11-07 12:00:00-08:00
    >>> print(dt.tzname())
    PST
    ```
<br>

These were some of the cool features that I liked in this new version of **Python**. There are many others too. Please refer to [RELEASE NOTES](https://docs.python.org/3/whatsnew/3.9.html) if you want to dig deeper and have a look for yourself.
<br><br>
<h2>What's next?</h2>
<br>
I just wanted to point out some minor things here that needs to be kept in mind when working with **Python**. 

**Python 2** has been unsupported from the Python Community for a while now. **Python 3.9** is the last version providing those Python 2 backward compatibility layers, to give more time to Python projects maintainers to organize the removal of the Python 2 support and add support for Python 3.9. So, from next version onwards buckle up for some breaking things.

**Python 3.9** uses a new parser, based on PEG instead of LL(1). The new parser’s performance is roughly comparable to that of the old parser, but the PEG formalism is more flexible than LL(1) when it comes to designing new language features. We’ll start using this flexibility in Python 3.10 and later. The ast module uses the new parser and produces the same AST as the old parser. In **Python 3.10**, the old parser will be deleted and so will all functionality that depends on it (primarily the parser module, which has long been deprecated). In Python 3.9 only, you can switch back to the LL(1) parser using a command line switch (-X oldparser) or an environment variable (PYTHONOLDPARSER=1).

Fingers crossed for Python 3.10 now.
<hr>
<br>
**As usual, feel free to drop a message if you want to get in touch. I am always ready to talk tech.**