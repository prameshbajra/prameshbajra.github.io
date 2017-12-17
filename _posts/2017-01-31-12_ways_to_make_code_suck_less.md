---
layout: post
title:  "12 ways to make your code suck less"
date:   2017-12-16
desc: "Reading code is as important as writing it."
keywords: "code, principle, programming, programs "
categories: [code, principle, programming, programs]
tags: [code, principle, programming, programs ]
icon: icon-fire-alt
---

Personally, I think that code is more read than write. Take an example of any textbook, we read textbooks a lot more than we write. So putting it straight I say that reading code is equally important as writing code. Also, the code you write will be read by many fellow developers or many other contributors so as to make the product/project better. 

Here are 12 tips for you to write code that will help you and others as well.

**1. Use linters.**

Linters maintain code consistency. It helps in making code structure similar across all development teams such that there exist no confusion between developers. Linters also covers _code indentation, use of proper variables, best modern practices_ etc. I, being a JavaScript developer use linters like _ESLINT, JSLINT, JSHINT_ etc. Similar types of linters are available for python, java and pretty much all popular programming languages. These linters easily couples with you current code editors like _VSCode, Atom, Sublime text and other full featured IDEs like Intellij , PHPStorm, WebStrom_ etc.

**2. Favor high cohesion and low coupling.**

Simply, _cohesion_ just means _a piece of code that does only one thing_. This helps in reducing frequency of change in the software and it also gives low cyclomatic complexity which is very favorable. Changing or updating the code is also very easy if we do this. _Coupling_ refers to _a piece of code that depends or has some kind of relation with another part of code_. We should keep our code as independent as it could be. Favoring low coupling is best for development and it also make testing very easy.

**3. Schedule time to lower technical debt.**

This is a non-technical criteria to keep in mind when writing code. Writing poor quality code is not technical debt. If you are working on a solo project or a project that doesn’t have a deadline then you may skip this point but, if you are working for someone or some company then schedule your time and work on your part. Schedule time to plan, write code, test and reviews accordingly. If you do not do this then your project will definitely lack in some part.

**4. Program with intention.**

Always have a goal on what you are trying to accomplish by writing a program. Never follow “Heat and trial” approach. One of the best way to program with intention is to _write tests first_ and then write program that makes the test pass. This will be difficult at first but trust me, it’s worth it. What this approach does is that it forces you to move towards your goal. It will be like moving to a certain fixed destination that you are aware of.


**5. Avoid primitive obsession.**

“`It is better to reuse than to rewrite`” – always keep this in mind. Try not to rewrite the functions, classes or any snippets that is already available in the codebase. Those methods are highly efficient and also written by one of the best developers. If you think that your method can surpass those predefined methods then a rewrite would be considerable, but remember this is very unlikely. 

For example -

to sort an array in java you do not have to write a sorting algorithms everytime, you can just use `Arrays.sort(ArrayName)`.
 
This is concise, self explanatory, short and efficient. We should avoid writing code at lowest level possible.  Also, prefer to code in functional style rather than imperative style. 

_Note: Functional Programming > Imperative Programming._

**6. Always prefer clean code, not clever code.**

Writing clever code makes you feel good, and you are not alone. It gives you a moment of joy and confidence. There is a quote that goes by – “`Programs must be written for people to read and only incidentally for machine to execute`”. I want you to remember this quote next time you write any clever code. I want to focus on one main drawback by writing clever code. Well it’s clear that you won’t remember every line of code that you wrote. May be after couple of months you won’t even remember working on the project. So, by case if you have to change a piece of code or you perhaps want to add a feature then you have to go back and read the same clever code that you wrote months back. This code will definitely confuse you and take up a good portion of your time. To avoid these kind of scenarios we should avoid writing clever code.

**7. Apply Zinsser’s principle.**

_“Hard writing makes easy reading and easy writing makes hard reading”_ – `Zinsser’s Principle`. So to make this clear, take your time to code. Think about the clean and easy way to code such that it will be easier for others and future you to read it without getting stuck and wasting too much time.  I also would like to suggest everyone to leave a blank line after each function declaration, class definition or any transition relevance act. This makes reading code very easy and transitions and breaks are understood by everyone. 

**8. Comment why, not what.**

`A good code is like a good joke, it’s not worth it if you have to explain it`. Always only comment the logic behind the code. Try to write expressive self-documenting code. Comment why the code is there not what that code does.

For example:

   `i++;                //   post increment i value by one` 

these types of comments are stupid so please avoid these. 
Rather explain why is the increment done.


**9. Avoid long methods.**

When writing methods apply __SLAP__ (_Single level of abstraction principle_). You might have a slight guess why developers do not prefer long methods. I personally do not like long methods because they are hard to maintain, hard to debug, difficult to test and even harder to refactor. Long methods have high coupling and low cohesion, they are not suitable to reuse and long methods leads to duplication of code. They violate good coding principles. So, separate a method when you think it’s level of abstraction is complete.

**10. Follow naming conventions.**

This is a must follow rule for everyone (Especially in our college). Always name your methods, classes and variables meaningfully. Avoid naming variables as single letters. 

For example –
    
   `int a , b, c;`
 
Never do this. These variables do not explain what they do. They enhance the complexity of the program and creates more confusion. For classes, remember to name their initials in capital letters. For method and variable you can either follow _snake\_casing_ or _CamelCasing_.

**11. Use tactical code reviews.**

Code review is generally done in groups, like in a meeting. I call this a bad idea. Not everybody has similar views on the code you write. Some might like your code and some won’t. Reviewing this in groups will create diverse results making it harder to decide. What can be a better alternative is to invite a colleague or another developers from the same company and cross review the code. I mean you reviewing your colleague code and your colleague reviewing your code. This will save time and resource, as well as maintain a friendly environment.

**12. Reduce state and state mutations.**

Simple trick is to start writing functions before declaring variables. They somehow force you to know the nature of the variables and use them properly. Messing with the state is the root of man problems both in software and in politics.
