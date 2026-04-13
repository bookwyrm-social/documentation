---
Title: RSS Feeds
Date: 2023-09-29
Order: 20
---

BookWyrm is an _open_ platform and generally it's ok to integrate your books and bookshelves in BookWyrm with other things. We provide some [RSS feeds](https://cyber.harvard.edu/rss/rss.html) to help you do that.

## RSS Locations

Currently, all RSS Feeds are relative to a someone's profile on their BookWyrm instance. So if your profile is at https://bookwyrm.social/user/mouse then all the rss feeds will be at a URL based on that.

### All Activity

This is everything someone posts that's publicly visible.

You can see all the _public_ activity of a user at their profile url /rss. So for user profile http://bookwyrm.social/user/mouse you can get an rss feed of all activity at http://bookwyrm.social/user/mouse/rss

BookWyrm is social - people quote books, chat with each other about books, etc. If you are looking for a more filtered view, the next locations might be useful.

### Reviews

To get an RSS feed of every Review someone posts, add `/rss-reviews` to the end of their profile url.

So for user profile http://bookwyrm.social/user/mouse you can get an rss feed of all Reviews at http://bookwyrm.social/user/mouse/rss-reviews

### Quotes

To get a feed of every Quote someone posts, add `/rss-quotes` to the end of their profile url.

So for user profile http://bookwyrm.social/user/mouse you can get an rss feed of all Quotes at http://bookwyrm.social/user/mouse/rss-quotes

### Comments

To get a feed of every Comment someone posts, add `/rss-comments` to the end of their profile url.

So for user profile http://bookwyrm.social/user/mouse you can get an rss feed of all Comments at http://bookwyrm.social/user/mouse/rss-comments

### Shelves

You might also want to get a feed of books being added to someone's bookshelves. You'll add `/rss` to the end of that bookshelf's url.

So for bookshelf https://bookwyrm.social/user/mouse/books/read you can get an RSS feed of all books added at https://bookwyrm.social/user/mouse/books/read/rss
