---
Title: Moderation
Date: 2021-04-18
Order: 3
---

## User actions

### Blocking
Users have the option to block other users on their own, without a moderator intervening. From the "Federated Servers" admin view, administrators can see how many users from an instance have been blocked by local users.

### Reports
Users can report statuses or users from the "more options" menu in the footer of posts and the follow/unfollow buttons for users. When a report is made, all users with admin permissions will receive a notification.

To manage reports, go to `Admin > Moderation > Reports`.

When a report is made, there are a few options how the moderator can respond.
- Send a direct message to the reported user.
- Delete the reported status.
- Deactivate the user. For local users, this will make them unable to log in, and their account will not be shown in the application. For remote users, the server will reject any incoming activities from this user, and they will not be shown in searches.

## Auto-moderation

Auto-moderation rules will create reports for any local user or status with fields matching the provided string. Users or statuses that have already been reported (regardless of whether the report was resolved) will not be flagged. To set up auto-moderation, go to `Admin > Moderation > Auto-Moderation Rules`.

## Instance-level moderation

### Manual instance blocks

Moderators can block entire instances. This will prevent any activities from coming in from that instance, and deactivate all accounts from that instance locally. To block an instance go to `Admin > Federated Instances` and find the instance you wish to block. See `Managing BookWyrm > Federation` for more information.

If the instance is un-blocked, all the users who were deactivated by the block will be re-activated.

### FediBlock lists

Moderators can also upload _FediBlock_ formatted blocklists to block servers in bulk. To do this, go to `Federation > Federated Instances` and click on "Add instance".

### Email and IP block lists

You can block signups from a given email domain at `Admin > Moderation > Email Blocklist`. When someone tries to register with an email from a domain in your email blocklist, no account will be created. The registration process will appear to have worked.

An IP block list will block all traffic from the IP address. Requests to any part of your instance from these IPs will receive a 404 response.

### Link Domains

Users can add a link to a book download for any book. Link domains must be approved before they are shown on book pages in order to avoid spam and malicious links. You can approve link domains at `Admin > Moderation > Link Domains`.

## Disabling federation
Administrators and moderators can disable federation completely. This will prevent any further communication inwards or outwards, however existing data will be retained in the database. Disabling federation does not prevent connectors from importing books, however it will restrict all statuses (reviews, comments etc) to only users on your instance, or anything those users import manually (e.g. via a Goodreads CSV import).

To disable federation, go to `Admin > Federation > Federation Settings`.

