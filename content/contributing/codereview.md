---
Title: Code Review
Date: 2023-01-11
Order: 7
---

You opened a pull request! Thank you so much. Here's what happens next. Long story short, another contributor will look over your code, try it out, and give feedback until it's ready to merge. Here's some more detail on the process:

## Automated Checks

BookWyrm uses a handful of [code validators](style_guide.html) that lint and validate code, and run the unit tests. All of these need to pass for your code to be ready to merge. There are usually hints about how you can fix any checks that don't pass, but if you aren't sure how to proceed, just comment on the issue and someone can help you out.

## Code Review

When your code is ready for review, a contributor will take a look at what you've written. They will be looking for a few things:

 - Is your proposed change in line with the project's goals?
 - Does your code work as expected?
 - Are there different or more efficient approaches you could have taken?
 - Are there edge cases you may have overlooked?
 - If you added any text, is it [correctly internationalized](translation.html)?
 - If you made UI changes, are they clearly navigable with a screen reader?

This is also a chance for other contributors to ask you questions about anything they don't understand or are curious about in your code.

## Merging

Once you and the reviewer feel good about your code, the reviewer will merge it. It won't be immediately available in production, but will go into the next release.
