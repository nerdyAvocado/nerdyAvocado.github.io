---
layout: default
title: "Three Documentation Tips for Making Your Code Supportable"
date:
---

So you're a developer, and you've just shipped out the latest feature for your product. It's been code reviewed and tested, and you're ready to move on to the next bit of work. But what happens when an end-user tries out your new feature...

Bugs are inevitable. No product is perfect - there's always something that an end-user finds a problem with. A missed use-case, a fault with an edge-case you hadn't considered, or even just a coding bug - it happens to everyone. When things like this are found in testing, the developers can quickly fix things up because they've just been working in that area of the product - they're familiar with it, and likely just worked on whatever bit of code contains the flaw. But what happens when an end-user finds the bug a year later? 5 years later? A decade later? The oldest bug I've ever fixed was caused by a missing bit of logic in some code originally implemented in 2002!

Some companies run with a set up where the development team are responsible for the technical-level support of their product. In contrast to that, I work in a team where we're purely responsible for supporting customer deployments (no development for us!), but when it comes to investigating and fixing these bugs the context is often the same. It's unlikely that the person who implemented the faulty functionality 5 years ago is still on your team - and if they are, I can guarantee you that they won't remember much about it!

This is when the work almost becomes like archeology - digging through old specs and code commits trying to work out what the original thought process behind the implementation was. Below I've covered the three types of documentation that I find most useful when debugging these kinds of issues, and how you can use them to make any investigations eaiser for whoever works on your code in the future. 

### Functional Specifications

A FUNCTIONAL SPECIFICATION should cover a high-level design of the features you are implementing.

In an ideal world, you would know exactly what the behaviour of the broken functionality should be. But in reality, often it's a bit of obscure function that's rarely used or worked on, or you just haven't seen it before at all. When an end-user is complaining that a feature is broken, they know what <em>they</em> want it to do - but is that what was originally intended? Is there really a bug, or is the function actually working as designed? Maybe there is a fault with the feature, but what the end-user is asking for isn't the correct behaviour either!

That's the point that having some kind of FUNCTIONAL SPECIFICATION becomes important. How this is implemented for your project or company will obviously be different, but what you want to have for every bit of functional design you do, be it a new feature or a modification/extension to an existing feature, is something that documents the high-level overview of the design - i.e. what it should actually do. How does the new functionality interact with existing features? How should it appear to the end-user? What problem is it trying to solve, or what use-case is it fulfilling?

Not only should this document exist, but it also needs to be easy to find and understand. You should always remember that the your functional specification serves a purpose beyond the point of initial development. Some companies keep these in a specific archive, others might attach them to the tickets used to track the development work. Whatever you do, it should be consistent to avoid any confusion over missing specs later on!

Any assumed knowledge should be defined too - if you're referencing another spec, link out to it! Define any base knowledge that a reader would be required to have to understand your design, be it another part of the products functionality, or any technologies being discussed, such as framworks or external libraries. I'd recommend having a dedicated section for this at the start of your design - it makes it much easier to find all the pre-requisites before starting to read the rest of the document.

### Helpful Commit Messages

COMMIT MESSAGES should give a short description and context for your changes.

So now you know there's a fault with the functionality, and you have a good idea of what it actually should be doing. Now you need to figure out what code actually relates to this feature, to have an idea of where to start looking for the fault. How you do this will vary - maybe you just know where the code is! But what if you don't "just know" exactly where in the code to look? The product I work on has always had tickets linked in every code commit, and these tickets are linked to the high-level designs for any relevant work they are implementing. For example, that might mean linking to the JIRA ticket you're working on in your git COMMIT MESSAGE.

Having helpful COMMIT MESSAGES is often overlooked. Nothing hurts my soul more than a commit message that simply reads "Design implemented" - what design?!? What did you <em>do</em>?!? It can be easy to slack on writing good commit messages, especially if you're working on something yourself, but these commit messages aren't for you. Instead, they're a vital form of documentation. When you're looking through a blame or a changelog of a file, you want to be able to easily work out when, what and why a change was made - that's where having good COMMIT MESSAGES comes in.

###  Code Comments

CODE COMMENTS should describe <em>why</em> you're doing something, rather than what you're doing.

Once you've found the relevant code, you need to identify the fault. That generally requires understanding the logic the code is implementing through reading the code. 

Another developer should be able to work out what your code is doing, but they might not know why you've done it that way. Are you using a semi-colon as a delimiter because the text strings you're collating might have commas in them? Comment that! Are you explicitly handling the case where a database value is null in a specific way to ensure back-compatability? Comment that so that nobody accidentally removes it in any "tidying up" refactoring!

Any developers looking at the code in the future (including Future You!) need to have context for any unusual or un-obvious implementation choices that were made. While you might do this with some kind of low-level, implementation design document for more complicated work, individual or one-off design decisions can be just as easily recorded in the code itself. Your code comments code should be as concise and easy to understand as possible - think of them as just as important as the functional code you write. Learning how to write effective code comments is a skill that requires active learning and practice, just the same as learning any other new technical skill.

Have a read through some code that you've written before - the older, the better. Do you still understand it? Are there any code comments you find particularly useful? Or anything that you think should have been commented, that wasn't?

### 5 Minute Supportability Documentation Checklist

Whenever you work on a change, you can use the following checklist as a starting point for considering if you have documentation in place to make your new feature supportable. This might require some concious effort at first, at various points in the development cycle, but hopefully it will make you think more about supportability. Eventually you'll be writing supportable code without thinking about it!

- Do you have a high-level design doc?
	- Is it easy to find?
	- Does it cover all of the functionality you've implemented?
	- Is it easy to understand?
	- Does it contain references where needed?
- Have you written good commit messages?
	- Where applicable, do they reference the ticket you were working on?
	- Do they contain a quick description of the changes you've made?
- Have you added code comments?
	- Do they cover any unobvious or unusual decisions you've made?

This is just the beginning of the supportability and internal documentation considerations - as mentioned above, you could also have a low-level, implementation level design for your feature or maybe you . This also only covers internal documentation - writing documentation for end-users is a whole other area to consider! If you want to read more in this area, I'd recommend reading Stephanie Morillo's article [The What, Why, and How of Internal Documentation](https://www.stephaniemorillo.co/post/the-what-why-and-how-of-internal-documentation) for more on different kinds of internal documentation.
