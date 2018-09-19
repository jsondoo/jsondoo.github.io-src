Title: Paying Off Code Debt - SAP Co-op Report
Date: 2018-09-18 21:16
Category: Blog

## Introduction

For the past 8 months, I was an intern at SAP for a product called SAP Jam, a social collaboration app for companies and employees. I was part of the Messages epic, responsible for creating features and fixes for our messaging feature.

I learned many new things from development tools, new languages and frameworks, and agile development. But the most interesting thing I learned was why writing good software is so difficult.

One aspect of software development that I found particularly interesting is technical debt.

*Technical debt is a concept in software development that reflects the implied cost of additional rework caused by choosing an easy solution now instead of using a better approach that would take longer.  — Wikipedia*

In this post, I will touch on a few examples of technical debt and analyze them based on these metrics:

Impact — how much does it affect end-users and developers?

Fix cost — how much time, effort, and resources does it take to fix the issue?

I will also discuss possible causes and solutions to the technical debts.

## 1. “Code Rot”
“Code rot” is a technical debt that happens over time, where eventually, the code becomes unusable, faulty, or incomprehensible.

First, let's look at some front-end components that I worked with.

![Used with permission](https://i.imgur.com/fGg3Qh5.jpg)

My task was to refactor the code for these components so that they are rendered directly into the body of the DOM as a pop-out instead of being rendered inside a container.

But for some reason, these two components shared the same CSS, despite being two functionally and visually different components… This meant that if I made changes to the CSS for the reaction picker, I could possibly break the link tooltip component. This coupling made no sense (other than that they share the same white background and the positioning) and the obvious solution here was to separate the CSS for the two components before making any further changes.

### Causes

My guess is that it probably started off with simple, innocent CSS to be shared such as:

```css
.menu-component {
  background-color: white;
  z-index: 2;
  box-shadow: 0px 2px 5px rgba(0,0,0,0.2)
}
```

And later evolved to a huge mess as people added more and more attributes until it looked ‘right’.

### Analysis

1) Impact: 1/5

From the consumer’s perspective, there are no problems with the UI. For developers, there are lots of problems with the styling but no one would notice unless they had to actively work on the component (which was the case for me).

2) Fix Cost: 1/5

Separating out the CSS shouldn’t be too hard, although there were some questionable CSS attributes (scattered across multiple media queries) that took a bit more time to understand.

### Solution

The fix is fairly simple. Figure out which CSS attributes apply to which component and separate it.

```css
.link-toolbar {
  /* SCSS for the link toolbar */
}
.reaction-picker {
  /* SCSS for the reaction picker */
}
```

This is way cleaner and easier to maintain, and everyone is happy.


## 2. Outdated Tech Debt

When you’re a software developer, you need to be able to keep up with all the new technologies coming out, and also deal with libraries being deprecated over time.

When our team first started building Messages, we chose Inferno over React, since React had an undesirable license back then (see React 14’s BSD + patents license). Now that React 16 was released with a MIT license, I was assigned to migrate our code base for Messages from Inferno to React.

### Analysis

1) Impact: 4/5

React 16 would provide many benefits to developers such as greater support for libraries and testing tools, documentation, and better performance tools. Also, sooner we migrate, easier it will be since we would have less Inferno code to deal with.

2) Fix Cost: 2/5

Although Inferno and React are different front-end frameworks, the concepts and API are almost identical so the transition shouldn’t be too difficult. The main concern is ensuring that nothing breaks in the process of transitioning. To do this, the migration should be a beta feature that can be toggled for QA testing.

### Solution

This was an interesting task since there was a lot of incremental changes to be done to the code base. Most of the work was creating shims and working with webpack for an easy toggle between importing Inferno and React for testing. Then, I slowly worked through all the warnings, and resolved syntactical differences.

In the end, the migration gave us access to many awesome development tools such as React Hot Loader, React Developer Tools, and storybook for UI testing.

Interestingly, the full migration to React wasn’t the end of this technical debt. This leads to my next topic — deliberate technical debt.

## 3. Deliberate Technical Debt

Sometimes technical debt is created intentionally or left alone because its impact is minimal compared to the fix cost. And there are benefits to deliberate technical debt such as speeding up the development process to deliver features faster.

Below are some examples of deliberate technical debt we decided leave until later.

First, after the React migration, there were still a lot of places in directories, imports, and configs where we used the word Inferno. Renaming all of these to React without breaking anything would be a lot of effort for little value. It’s not just a simple find-and-replace since we need to think about renaming webpack chunks and fixing tests, so we decided to deliberately keep it as is for now.

Second, during the transition, I had to shim Inferno’s `linkEvent` function which did not exist in React.

```javascript
import React from ‘react’;
export const linkEvent = (params,event) => {
  if(React && React.linkEvent) {
    return React.linkEvent(params,event);
  } else {
     return (e) => event(params, e);
  }
}
```

The webpack configuration was set up so that `react` is an alias for either React or Inferno depending on the environment variables used to start the app allowing for an easy toggle.

After the migration, since `Inferno.linkEvent` didn’t exist anymore, we could replace all calls to the `linkEvent` shim with the appropriate callback.

The problem was that `linkEvent` was used in 100’s of places, and manually going through all instances and simplifying them with the appropriate callback would be a lot of work for little value. So we decided to just keep all calls to the shim.

Since future developers who are unaware of the React migration may be confused by this seemingly useless function, we decided that an acceptable solution for now is to just rename `linkEvent` to `OLD_linkEvent` (which only takes a few seconds to do). I also left a friendly comment in the shim saying `DO NOT USE` so that the technical debt doesn’t spread.

![This may or may not have happened.](https://cdn-images-1.medium.com/max/800/0*SlkxFS24hd31yUIe.png)

Software developers don’t want to do lot of work for little value. We want to do a lot of work for a lot of value. Note that deliberate technical debts usually have low impact and high fix cost, so it is okay to sit on these debts for some time.

## Conclusion

Technical debt is an unavoidable part of software development. There are many causes whether it be a new framework coming out, overlooked design specification, or deliberate.

Working through various technical debts taught me to always try to write code that is maintainable and readable. Before starting to code on a new component, I think about all the use cases and try to design it on paper before I work on the implementation. I document my code with comments if there are any ambiguities. Good software practices can help prevent technical debt.

Most importantly, I learned how to prioritize what needs to be fixed or refactored first, and decide what can be left alone until later, rather than trying to fix every small thing that comes up. Being able to analyze problems based on the severity of impact on customers and/or developers, and to estimate the time and effort of a task, will greatly benefit me as an aspiring software developer.


### Sources
[Riot games](https://engineering.riotgames.com/news/taxonomy-tech-debt)

[Types of debts](https://hackernoon.com/there-are-3-main-types-of-technical-debt-heres-how-to-manage-them-4a3328a4c50c)

[Original medium article by me](https://medium.com/@jsondoo/paying-off-code-debt-5820cbdd783b)