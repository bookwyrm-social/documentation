---
Title: Federatie
Date: 2026-01-18
Order: 2
---

## Federatie-instellingen

Administrators en moderators kunnen federatie volledig uitschakelen. This will prevent any further communication inwards or outwards, however existing data will be retained in the database. Disabling federation does not prevent connectors from importing books, however it will restrict all statuses (reviews, comments etc) to only users on your instance, or anything those users import manually (e.g. via a Goodreads CSV import).

To disable federation, go to `Admin > Federation > Federation Settings`.

## Federated Instances

At `Admin > Federation > Federated Instances` you can see all instances connected to yours via federation. This list may be quite long, as it will include every ActivityPub server that has sent or received a status or object. This list will show you the instance domain and software the instance is running.

You can click on the instance domain to find out more information about the instance including how many users have come from that instance. You can also block the instance completely from here.