---
Title: Föderation
Date: 2026-01-18
Order: 2
---

## Föderationseinstellungen

To adjust these settings, go to `Admin > Federation > Federation Settings`. By default they are all disabled.

### Require signed GET requests

Instances with this setting enabled will reject all anonymous ActivityPub requests from federated instances. That is, all requests must use signed HTTP headers. BookWyrm has been signing `GET` requests for ActivityPub data since 2022, but without this setting your instance will not check incoming signatures. This will impact _all_ ActivityPub traffic. Whilst Mastodon and other major Fediverse systems also sign GET requests as a matter of course, this is not the case for all Fediverse software

This is roughly equivalent to Mastodon's 'secure mode' or `AUTHORIZED_FETCH`, though BookWyrm does not check JSON-LD signatures. You can find [a detailed explainer of AUTHORIZED_FETCH here](https://hub.sunny.garden/2023/06/28/what-does-authorized_fetch-actually-do/).

### Disable federation

Administrator\*innen und Moderator\*innen können die Föderation komplett deaktivieren. Das wird die gesamte zukünftige eingehende und ausgehende Kommunikation unterbinden. Bestehende Daten bleiben allerdings in der Datenbank erhalten. Die Föderation zu deaktivieren hält die Konnektoren nicht davon ab, Bücher zu importieren, aber es beschränkt alle Beiträge (Rezensionen, Kommentare etc.) auf Nutzer\*innen deiner Instanz und das, was sie händisch importieren (z. B. von Goodreads durch einen CSV-Import).

### Prevent unauthenticated views

Technically this setting is not related to federation, but it is also found in the "Federation settings" section of the admin interface.

_Prevent unauthenticated views_ requires viewers to log in for every page other than the absolute basics required to manage logins, invites, and essential instance information pages. It also hides the "recent books" from the homepage. Enabling this setting should ensure that only your instance's users can view pages on your instance such as the Directory, Lists, and user profile pages.

**Note:** User profiles for your instance's users on federated instances may still be viewable on those instances even with this setting enabled.

### Block incoming search

Enabling this setting will prevent any federated servers from being able to use your instance's search endpoint. It is equivalent to disabling all BookWyrm [Connectors](system.html#connectors), but in reverse. It is **strongly discouraged** to enable this setting, however administrators concerned about revealing which books are in the local database, or experiencing disruptive bot activity, may wish to do so. If enabled, this is likely to lead to more duplicate works and editions within the BookWyrm federation.

## Föderierte Instanzen

Unter `Administration > Föderation > Föderierte Instanzen` siehst du alle Instanzen, die durch die Föderation mit deiner verbunden sind. Diese Liste kann recht lang werden, da sie jeden ActivityPub-Server enthält, der einen Beitrag oder ein Objekt mit deinem Server ausgetauscht hat. Die Liste wird dir die Domain der Instanz zeigen sowie die Software, die auf der Instanz läuft.

Du kannst auf die Instanz-Domain klicken, um weitere Informationen zur Instanz abzurufen, darunter die Anzahl der Nutzer\*innen, die von dieser Instanz kommen. Du kannst die Instanz von dieser Seite aus auch völlig blockieren.