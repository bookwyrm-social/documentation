---
Title: Federatie
Date: 2026-01-18
Order: 2
---

## Federatie-instellingen

To adjust these settings, go to `Admin > Federation > Federation Settings`. By default they are all disabled.

### Require signed GET requests

Instances with this setting enabled will reject all anonymous ActivityPub requests from federated instances. That is, all requests must use signed HTTP headers. BookWyrm has been signing `GET` requests for ActivityPub data since 2022, but without this setting your instance will not check incoming signatures. This will impact _all_ ActivityPub traffic. Whilst Mastodon and other major Fediverse systems also sign GET requests as a matter of course, this is not the case for all Fediverse software

This is roughly equivalent to Mastodon's 'secure mode' or `AUTHORIZED_FETCH`, though BookWyrm does not check JSON-LD signatures. You can find [a detailed explainer of AUTHORIZED_FETCH here](https://hub.sunny.garden/2023/06/28/what-does-authorized_fetch-actually-do/).

### Disable federation

Administrators en moderators kunnen federatie volledig uitschakelen. This will prevent any further communication inwards or outwards, however existing data will be retained in the database. Disabling federation does not prevent connectors from importing books, however it will restrict all statuses (reviews, comments etc) to only users on your instance, or anything those users import manually (e.g. via a Goodreads CSV import).

### Prevent unauthenticated views

Technically this setting is not related to federation, but it is also found in the "Federation settings" section of the admin interface.

_Prevent unauthenticated views_ requires viewers to log in for every page other than the absolute basics required to manage logins, invites, and essential instance information pages. It also hides the "recent books" from the homepage. Enabling this setting should ensure that only your instance's users can view pages on your instance such as the Directory, Lists, and user profile pages.

**Note:** User profiles for your instance's users on federated instances may still be viewable on those instances even with this setting enabled.

### Block incoming search

Enabling this setting will prevent any federated servers from being able to use your instance's search endpoint. It is equivalent to disabling all BookWyrm [Connectors](system.html#connectors), but in reverse. It is **strongly discouraged** to enable this setting, however administrators concerned about revealing which books are in the local database, or experiencing disruptive bot activity, may wish to do so. If enabled, this is likely to lead to more duplicate works and editions within the BookWyrm federation.

## Federated Instances

At `Admin > Federation > Federated Instances` you can see all instances connected to yours via federation. This list may be quite long, as it will include every ActivityPub server that has sent or received a status or object. This list will show you the instance domain and software the instance is running.

You can click on the instance domain to find out more information about the instance including how many users have come from that instance. You can also block the instance completely from here.