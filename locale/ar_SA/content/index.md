- - -
Title: Welcome Date: 2021-04-13
- - -

BookWyrm is a social network for tracking your reading, talking about books, writing reviews, and discovering what to read next. Federation allows BookWyrm users to join small, trusted communities that can connect with one another, and with other ActivityPub services like Mastodon and Pleroma.

## Features
The features are growing every month, and there is plenty of room for suggestions and ideas. افتح إشكالية [](https://github.com/bookwyrm-social/bookwyrm/issues) لجعل المحادثة مستمر، أو [ابحث عن إشكالية جيدة](https://github.com/bookwyrm-social/bookwyrm/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) لتقديم مساهمتك الأولى!

- Posting about books
    - Compose reviews, with or without ratings, which are aggregated in the book page
    - Compose other kinds of statuses about books, such as:
        - Comments on a book
        - Quotes or excerpts
    - Reply to statuses
    - View aggregate reviews of a book across connected BookWyrm instances
    - Differentiate local and federated reviews and rating in your activity feed
- Track reading activity
    - Shelve books on default "to-read," "currently reading," "stopped reading," and "read" shelves
    - Create custom shelves
    - Store started/stopped/finished reading dates, as well as progress updates along the way
    - Update followers about reading activity (optionally, and with granular privacy controls)
    - Create lists of books which can be open to submissions from anyone, curated, or only edited by the creator
    - Create groups with other BookWyrm users and collaborate with group-owned lists
- Federation with ActivityPub
    - Broadcast and receive user statuses and activity
    - Share book data between instances to create a networked database of metadata
    - Identify shared books across instances and aggregate related content
    - Follow and interact with users across BookWyrm instances
    - Inter-operate with non-BookWyrm ActivityPub services like Mastodon and GoToSocial
- Granular privacy controls
    - Private, followers-only, and public privacy levels for posting, shelves, and lists
    - خيار للمستخدمين للموافقة يدوياً على المتابعين
    - Allow blocking and flagging for moderation

## Using this documentation

### Navigation

Use the menu on the left-hand side to find the section you are looking for.

* _Using BookWyrm_ explains how to use BookWyrm as an ordinary user
* You will need the _Running BookWyrm_ section if you want to administer a BookWyrm instance (server)
* _Contributing_ explains how you can get involved in the project and contribute in various ways (you don't have to know how to code)
* _Codebase_ provides more information about key aspects of BookWyrm's code
* Consult the _Reference Guides_ if you need to know what a particular environment variable or `bw-dev` command does

You can also change the language and version.

### Translations

Documentation is written in English (US) by default. When we have at least 70% coverage for a language in [BookWyrm's translation project](https://translate.joinbookwyrm.com/) it will be added to the list of available languages. If you notice some parts of a translated version are in English, you can [help us to translate them](https://translate.joinbookwyrm.com/). This can happen as we make changes and additions to the documentation.

### Versioning

Since version `0.7.5`, each BookWyrm version has a matching version in the documentation. This allows you to check the documentation as it applies to your specific BookWyrm version. If you are using a patch version with no matching documentation (e.g. `0.8.1`), this is a bugfix-only version and you should use the documentation for the preceding version (e.g. `0.8.0`).

### Page table of contents

There is also a drop-down menu on each page that displays a table of contents. You can use this to navigate directly to a particular section heading. This can be useful for very long pages like the Reference Guides. The table of contents menu does not appear on the homepage.

### Smaller screens

On smaller screens the side menu is hidden. Use the "hamburger menu" at the top right of the screen to make it visible.