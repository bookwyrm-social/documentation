- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm hyödyntää [ActivityPub](http://activitypub.rocks/)-protokollaa käyttäjäaktivisuuden lähettämiseen ja vastaanottamiseen eri BookWyrm-instanssien ja muiden ActivityPub-sovellusten kanssa, kuten [Mastodon](https://joinmastodon.org/)-palveluiden. BookWyrm-palvelulla on kourallinen laajennettuja Activity-tyyppejä kirjatietojen käsittelyyn, mitkä eivät ole osa standardia, mutta mitä muut BookWyrm-instanssit pystyvät lukemaan.

## Activities and Objects

### Users and relationships
User relationship interactions follow the standard ActivityPub spec.

- `Follow`: request to receive statuses from a user, and view their statuses that have followers-only privacy
- `Accept`: approves a `Follow` and finalizes the relationship
- `Reject`: denies a `Follow`
- `Block`: prevent users from seeing one another's statuses, and prevents the blocked user from viewing the actor's profile
- `Update`: updates a user's profile and settings
- `Delete`: deactivates a user
- `Undo`: reverses a `Follow` or `Block`

### Statuses
#### Object types

- `Note`: On services like Mastodon, `Note`s are the primary type of status. They contain a message body, attachments, can mention users, and be replies to statuses of any type. Within BookWyrm, `Note`s can only be created as direct messages or as replies to other statuses.
- `Review`: A review is a status in response to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Comment`: A comment on a book mentions a book and has a message body.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book.


#### Activities

- `Create`: saves a new status in the database.

   **Note**: BookWyrm only accepts `Create` activities if they are:

   - Direct messages (i.e., `Note`s with the privacy level `direct`, which mention a local user),
   - Related to a book (of a custom status type that includes the field `inReplyToBook`),
   - Replies to existing statuses saved in the database
- `Delete`: Removes a status
- `Like`: Creates a favorite on the status
- `Announce`: Boosts the status into the actor's timeline
- `Undo`: Reverses a `Like` or `Announce`

### Collections
User's books and lists are represented by [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objects

- `Shelf`: A user's book collection. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Activities

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Add`: Adds a book to a shelf or list.
- `Remove`: Removes a book from a shelf or list.


## Alternative Serialization
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
