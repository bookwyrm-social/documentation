---
Title: Privacy Controls
Date: 2025-05-26
Order: 2
---

Bookwyrm has different privacy levels which let users control how public something is and who it is visible to.
Do you want to share your reading with the internet, just your friends, or do you want to keep it private?

There are four privacy levels: Public, Unlisted, Followers, and Private.
Broadly speaking, Public is visible to anyone; Unlisted hides it from discovery pages; Followers is only visible to people who follow you; and Private is only visible to you.
There are some slight differences in how these apply to different things in Bookwyrm.

Throughout the website, you can check what something's privacy level is by the icon next to it.
Public is a globe, Unlisted is an open lock, Followers is a closed lock, and Private is an envelope.

Note: Anyone can just follow you and then be able to see all things you marked Followers-only.
To limit this, go to `Settings - Edit Profile - Privacy` and enable 'Manually approve followers'.
This allows you to vet follow requests, or limit them just to your friends.

Other privacy settings are explained at the bottom of this page. [Click here](#privacy-related-settings) to scroll down to them.

--- 

## Statuses

On Bookwyrm, [statuses](/posting-statuses.html) can be posted at four different privacy levels, which restrict who can see it and if it's promoted on public pages.
Each status has its own privacy level, so you can choose when to make it Public or Private, or set a default in settings.
Note that it cannot be changed once it's published.

### Public

The default option.

- Anyone can see your status without logging in.
- Your status will appear on:
	- public timelines
	- discovery pages.
	- it's related book's page.
	- the home timeline of people who follow you
- Your status can be **boosted** into other people's home timelines.

### Unlisted

The exact same as Public, but:

- Your status will **not** appear in public timelines or discover pages.

### Followers

- Only people who follow you can see your status in their timelines or related book's page.
- Your status cannot be boosted.

### Private

- Your status can only be seen by you, and anyone **mentioned** in it.
- This is the privacy level used in Direct Messages.

---

## Shelves

Shelves are Public by default, but you can edit them to make them only visible to your followers or just yourself.

### Public / Unlisted

- There is no difference between Public and Unlisted for Shelves. The Unlisted option may be removed in the future.
- Anyone can see these shelves and all the books on them.

### Followers

- Only people who follow you will see this shelf and the books on it.

### Private

- Only you will be able to see this shelf and the books on it.

### All books shelf

- The 'All books' shelf is a default shelf which displays books from all visible shelves to the user viewing it. 

| User        | Books on Public shelves | Books on Unlisted shelves | Books on Followers-only shelves | Books on Private shelves |
|-------------|-------------------------|---------------------------|---------------------------------|--------------------------|
| Anyone      | ✔                       | ✔                         |                                 |                          |
| Follows you | ✔                       | ✔                         | ✔                               |                          |
| Yourself    | ✔                       | ✔                         | ✔                               | ✔                        |

### Implications

- If you read a book, want to track it on Bookwyrm, but don't want anyone to know that you did, you'll need to put it on a new Private shelf, not a Public shelf.

---

## Lists

### Public

- Anyone can see your [List](/lists.html) without logging in.
- Your List will appear on:
	- the Lists discovery page (Lists tab).
	- the pages of books that are in it, displayed on the side of the screen.
	- your profile.
- Anyone can 'save' (bookmark) your List. 

### Unlisted

- There is currently no difference between Public and Unlisted for Lists. 
In the future, Unlisted will hide the List from the Lists discovery page and books pages. 
For details, see [#3265](https://github.com/bookwyrm-social/bookwyrm/issues/3265) on GitHub.

### Followers

- Only people who follow you can see your List on the aforementioned pages.

### Private

- Only you can see your List on the aforementioned pages.

---

## Groups

[Groups](/groups.html) have the same privacy settings as statuses and lists do, except they can't be Followers-only.
Group membership always requires an invitation from the group's owner, even if it is marked Public.

### Public

- Anyone can view the Group page, members and its Lists (except for private Lists)

- In the future it will be displayed on a Groups discovery page.

### Unlisted

- Anyone can view the group page, members and its Lists (except for private Lists)

### Private

- Only members of the group can view the group page, members and its Lists

- All the Groups statuses and Lists will also be private.  

---

## Privacy related settings

### Manually approve followers

Found in `Settings - Edit Profile - Privacy`. 

When enabled, you will get a notification when someone wants to follow you, and you'll be able to choose whether or not to accept it.
Useful if you want to check who they are or restrict your followers to only be your friends and people you know.

### Hide followers and following lists on profile

Found in `Settings - Edit Profile - Privacy`. 

By default, anyone can view the list of people you follow and who follow you.
There are many reasons you might not want this, so Bookwyrm allows you to hide these lists.

### Show this account in suggested users 

Found in `Settings - Edit Profile - Display`.

When enabled, your account may be suggested to other users and will be on the account directory.

