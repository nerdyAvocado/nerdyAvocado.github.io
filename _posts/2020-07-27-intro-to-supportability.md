---
layout: post
title: "An Introduction to Software Supportability"
tags: Supportability
date: 2020-07-27
---

![gif of character building something on a Workbench in Animal Crossing](/assets/images/animal_crossing_build.gif)

My job as an L3 Engineer means I work on supporting, diagnosing problems with, and making bug-fixes for a product. Given that, I'm particularly invested in ensuring that our product is supportable and backed by a maintainable codebase - but what does that mean? 

*When there's a bug in your software, are you confident you'd be able to track down the cause and fix it?  
Is it easy to add new features to your code?    
Would you feel confident that you'd be able to restore service on your product if it failed in a critical deployment?    
Is there documentation covering all of the networking requirements for your product, and is the documentation customer-friendly?*

These are some questions that you could ask yourself if you were evaluating the supportability of your product - would you be able to answer them? Knowing what makes a product supportable is one of the things that you can use to build up a well-rounded insight into the lifecycle of a software product! At a code-level, a big part of supportability is having developers who produce maintainable code, so I've covered some basic points that you can apply to the code that you write.

## What is Software Supportability?

According to [Wikipedia](https://en.wikipedia.org/wiki/Serviceability_(computer)), Supportability is:

***"The ability of technical support personnel to install, configure and monitor computer products, identify exceptions or faults, debug or isolate faults to root cause analysis, and provide hardware or software maintenance in pursuit of solving a problem and restore the product into service".***

So that's the "dictionary definition", but what can make a product meet those requirements? And why is it important?

## My Job in an L3 Support Team

As some background, my job as the Product Owner in an L3 Support team means that I work on handling the technical, code-level support, and bug-fixing for one of my company's products once it's been deployed to the field. That means that on an average day, I might be answering questions from our Customer Care team about product functionality; working with the product's development team during the design stage for new features or enhancements, or diagnosing problems and bug-fixing.

Since our investigation and code fixes are targeted to specific areas, I've found that I gained a broad base of knowledge about my product, in a very short space of time. L3 engineers get to fix bugs in really varied parts of the product. For example, I've fixed bugs in Java code, Python code, and Bash scripts; I've investigated questions related to networking, fixed problems with Linux ssh config, and diagnosed database lock contention issues; and since my product is a management and configuration tool, I've had to become familiar with a range of APIs for integrating with the different things it can be used to manage.

Having to bounce from one area of the product to another very quickly - often in a matter of minutes when triaging incoming tickets - means that being able to ramp-up on things that I'm unfamiliar with is an important part of the job. Having a product that meets the definition of supportability makes this so much easier. Fixing bugs in unfamiliar bits of code is a lot simpler when the code is easy to follow and the functionality is well documented!

## What Makes a Product Supportable

Documentation is an excellent, and very accessible place to begin when thinking about the supportability of a product - it's easy to spot flaws in documentation no matter your experience. If it's confusing to you, or you can't find the documentation you are looking for, that means there's scope to improve it!

This is a very broad area, so there's a lot to consider, but we'll start with **internal documentation** - that is, documentation for people who are responsible for either the development of or the technical support of the product. This documentation should be easily accessible and searchable, maybe in some kind of company-wide knowledge base. You should have things that are more focussed on code-level detail, like a design doc for a new feature, or a high-level overview of the interactions between different components in an application. There should also be documentation aimed at people working in customer-facing support, which could include things like a clear set of instructions for things like commissioning a new deployment or enabling new features, or a set of steps for troubleshooting common problems.

The next thing to consider in this thread would be **customer-facing documentation**. This should be easy to access and search too and should cover all of the things that a customer might want to know about the product, from details for setting up firewalls around a server, to instructions for interacting with any UIs that they have access to. Remember that documentation aimed at customers will use different language than your internal documentation - you want it to be clear and concise, and not use any terminology that a customer wouldn't be familiar with. 

Being able to quickly identify and correct problems is a big part of supportability - that means that the product needs **good error and debug diagnostics for all it's components**. It's very important to have good default logging on errors, with useful diagnostics details included - for example, timestamps on all logs, stack traces for code errors, and heap dumps for memory problems. It should also be easy to enable targeted debug logging in the code.

What's less obvious with error logging is that the **logs need to persist for long enough to be useful** - that might mean using something like logrotate to ensure you keep a specified amount of log files without filling up disk space or zipping up historic logs to minimise disk usage. It also means eliminating rapid, repeated logs when hitting an error (using things like first and interval logging) to ensure that if an error starts being hit in the middle of the night, the logs haven't wrapped and eliminated the useful diagnostics that might have included at the point it started occurring by the time someone notices in the morning.

The final thing I'd highlight in a supportable product would be that it should have an **easy upgrade procedure**, that ideally a customer or end-user would be able to execute themselves, and that it should be **easy to deploy or spin-up a new instance** of the product - maybe that means there's some kind of automation or orchestration involved. Having this in a product means considering both the design of the upgrade procedures at the code-level implementation, and also ensuring the documentation of any procedures is clear and easy to follow. I can't stress enough how much pain you'll save yourself by having simple and well-documented procedures for initial deployment and set-up, upgrade procedures, and any common maintenance procedures!

## Maintainable Code

The most immediate supportability impact you can have when writing code for a product is to ensure that the code is maintainable. Maintainability can be defined as:

***"The ease with which a software system or component can be modified to correct faults, improve performance or other attributes, or adapt to a changed environment"***. 

In my experience, maintainable code is easy to read, provides a well-defined function, and is well documented.

The biggest problem I see in the code I've supported is over-engineering. People who write software are often very clever - but honestly, **most of the time, the simplest solution is the one you should be going with**. If you take away one thing from this, it's that you don't need to make your code fancy and wizzy and complicated. Over-engineered code is difficult to support because you have to reverse engineer what it's doing before you can even begin to think about fixing it.

The other way to improve the readability of your code is to **use Code Comments effectively**. You don't want to over-use code comments - your code itself should be readable, so comments should be used when you want to explain *why* you are doing something rather than what you are doing. 

Maintainable code doesn't just help with supporting the product - it helps developers adding new features too! When you go to add a new feature, or extend the functionality of your code, if it's too complicated, either in design or in implementation, then adding anything else into it will be exponentially more difficult.

The last thing to highlight would be that having dependencies that are well managed is important for ensuring that the product is supportable. The specific dependencies for each version of a product that is released should be recorded, and ideally archived somewhere to ensure that the exact release build can be rebuilt when required, even if the version of the dependency is no longer available from its initial source. Dependencies should be kept up-to-date and be easy to update - this ensures that it's easy to take bug fixes in the dependencies quickly and ideally with minimal effort from the team responsible for support.

## What Next?

Fundamentally, when you write some code to fix a bug, design a new feature or implement some new function, ask yourself - would you want to come back and work on the same thing in a year? If the answer is no, and you're the one who wrote the code, imagine how difficult it would be for someone else! That's the easiest way to start thinking about the impact you can have on the supportability of your codebase.

You can use the points above to start thinking about improving supportability and maintainability in your codebase, and if you want to read more, this article on [Developing Maintainable Software](https://software.ac.uk/resources/guides/developing-maintainable-software) is a good place to start.

