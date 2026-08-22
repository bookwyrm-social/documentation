---
Title: BookWyrm Vocabulary v1.0
Date: 2026-08-09
Order: 1
---

<DIV class="notification is-danger is-light">

<p><strong>Note:</strong> This vocabulary is a draft and may change.</p>
<p>BookWyrm servers do not currently send activities in the format shown in these examples, nor reference this vocabulary.</p>

</DIV>

BookWyrm uses the Core and Extended types and properties outlined in the [Activity Streams 2.0 Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary).

This page outlines a set of extended object types and properties for BookWyrm, where the Activity Streams Vocabulary is not sufficient for BookWyrm's needs.

The identifier for this vocabulary is `https://www.w3id.org/BookWyrm/ns`.

The Version 1.0 draft of this vocabulary was first published on 11 August 2026. Most types and properties were in use for several years prior to publication of the vocabulary, but not formally name-spaced.

## Extended Object book types

The basic BookWyrm types are all extensions of the core Activity Streams [Object](https://www.w3.org/ns/activitystreams#Object) type.

### Core book type properties

All types in this section ([Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)) have all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, all types in this section have the following properties:

* [openlibraryKey](#openlibraryKey): `String`
* [inventaireId](#inventaireId): `String`
* [finnaKey](#finnaKey): `String`
* [librisKey](#librisKey): `String`
* [librarythingKey](#librarythingKey): `String`
* [goodreadsKey](#goodreadsKey): `String`
* [bnfId](#bnfId): `String`
* [viaf](#viaf): `String`
* [wikidata](#wikidata): `String`
* [asin](#asin): `String`
* [aasin](#aasin): `String`
* [isfdb](#isfdb): `String`
* [lastEditedBy](#lastEditedBy): `@id`

### Extended book type properties

In addition to the core properties above, [Work](#Work) and [Edition](#Edition) types have the following extended properties:

* [title](#title): `String`
* [sortTitle](#sortTitle): `String`
* [subtitle](#subtitle): `String`
* [description](#description): `String`
* [languages](#languages): `Array`
* [series](#series): `String`
* [seriesNumber](#seriesNumber): `String`
* [seriesBooks](#seriesBooks): `Array`
* [subjects](#subjects): `Array`
* [subjectPlaces](#subjectPlaces): `Array`
* [authors](#authors): `Array`
* [firstPublishedDate](#firstPublishedDate): `String`
* [publishedDate](#publishedDate): `String`
* [fileLinks](#fileLinks): `Array`
* [cover](#cover): `Document`

### Work
`https://www.w3id.org/BookWyrm/ns#Work`

_Included in version 1.0 of the BookWyrm vocabulary_

A bibliographic work, which manifests in the form of one or more [Edition](#Edition)s.

#### Properties

Inherits all the [Object](https://www.w3.org/ns/activitystreams#Object), [Core book type](#Core-book-type-properties) and [Extended book type](#Extended-book-type-properties) properties.

In addition, a `Work` has the following extended properties:

* [lccn](#lccn): `String`
* [editions](#editions): `Array`

#### Example

```json
{
    "@context": [
        "https://www.w3id.org/BookWyrm/ns",
        "https://www.w3.org/ns/activitystreams",
    ],
    "id": "https://example.com/book/5988",
    "type": "Work",
    "authors": [
        "https://example.com/author/417"
    ],
    "first_published_date": null,
    "published_date": null,
    "title": "Piranesi",
    "sort_title": null,
    "subtitle": null,
    "description": "**From the *New York Times* bestselling author of *Jonathan Strange & Mr. Norrell*, an intoxicating, hypnotic new novel set in a dreamlike alternative reality.",
    "languages": [],
    "series": null,
    "series_number": null,
    "subjects": [
        "English literature"
    ],
    "subject_places": [],
    "openlibrary_key": "OL20893680W",
    "librarything_key": null,
    "goodreads_key": null,
    "attachment": [
        {
            "url": "https://example.com/images/covers/10226290-M.jpg",
            "type": "Image"
        }
    ],
    "lccn": null,
    "editions": [
        "https://example.com/book/5989"
    ]
}
```

### Edition
`https://www.w3id.org/BookWyrm/ns#Edition`

_Included in version 1.0 of the BookWyrm vocabulary_

The manifestation of a [Work](#Work) as a specific edition.

#### Properties

Inherits all the [Object](https://www.w3.org/ns/activitystreams#Object), [Core book type](#core-book-type-properties) and [Extended book type](#extended-book-type-properties) properties.

In addition, an `Edition` has the following extended properties:

* [work](#work): `@id`
* [isbn10](#isbn10): `String`
* [isbn13](#isbn13): `String`
* [oclcNumber](#oclcNumber): `String`
* [pages](#pages): `Number`
* [physicalFormat](#physicalFormat): `String`
* [physicalFormatDetail](#physicalFormatDetail): `String`
* [publishers](#publishers): `Array`
* [editionRank](#editionRank): `Number`

#### Example

```json
{
    "@context": [
        "https://www.w3id.org/BookWyrm/ns",
        "https://www.w3.org/ns/activitystreams",
    ],
    "id": "https://example.com/book/5989",
    "lastEditedBy": "https://example.net/users/rat",
    "type": "Edition",
    "authors": [
        "https://example.com/author/417"
    ],
    "first_published_date": null,
    "published_date": "2020-09-15T00:00:00+00:00",
    "title": "Piranesi",
    "sort_title": null,
    "subtitle": null,
    "description": "Piranesi's house is no ordinary building; its rooms are infinite, its corridors endless, its walls are lined with thousands upon thousands of statues, each one different from all the others.",
    "languages": [
        "English"
    ],
    "series": null,
    "series_number": null,
    "subjects": [],
    "subject_places": [],
    "openlibrary_key": "OL29486417M",
    "librarything_key": null,
    "goodreads_key": null,
    "isfdb": null,
    "attachment": [
        {
            "url": "https://example.com/images/covers/50202953._SX318_.jpg",
            "type": "Image"
        }
    ],
    "isbn_10": "1526622424",
    "isbn_13": "9781526622426",
    "oclc_number": null,
    "asin": null,
    "pages": 272,
    "physical_format": null,
    "publishers": [
        "Bloomsbury Publishing Plc"
    ],
    "work": "https://example.com/book/5988"
}
```

### Author
`https://www.w3id.org/BookWyrm/ns#Author`

_Included in version 1.0 of the BookWyrm vocabulary_

A creator of a [Work](#Work) or [Edition](#Edition). This includes creative contributions such as editor, illustrator, or translator.

#### Properties

Inherits all the [Object](https://www.w3.org/ns/activitystreams#Object) and [Core book type](#core-book-type-properties) properties.

In addition, an `Author` has the following extended properties:

* [isni](#isni): `String`
* [gutenbergId](#gutenbergId): `String`
* [born](#born): `String`
* [died](#died): `String`
* [aliases](#aliases): `Array`
* [bio](#bio): `String`
* [wikipediaLink](#wikipediaLink): `String`
* [website](#website): `String`

#### Example

```json
{
    "@context": [
        "https://www.w3id.org/BookWyrm/ns",
        "https://www.w3.org/ns/activitystreams",
    ],
    "id": "https://example.com/author/1",
    "type": "Author",
    "openlibraryKey": "OL9388A",
    "inventaireId": "wd:Q692",
    "librarythingKey": "shakespearewilliam",
    "goodreadsKey": "947",
    "bnfId": "119246079",
    "viaf": "96994048",
    "wikidata": "Q692",
    "asin": "B000APWKO4",
    "isfdb": "22499",
    "lastEditedBy": "https://example.com/user/avid_reader",
    "name": "William Shakespeare",
    "isni": "0000000121032683",
    "born": "1564-04-19",
    "died": "1616-04-22",
    "aliases": [],
    "bio": "<p>William Shakespeare was an English poet and playwright, widely regarded as the greatest writer in the English language and the world's pre-eminent dramatist.  He is often called England's national poet and the &quot;Bard of Avon&quot;.  His surviving works, including some collaborations, consist of 38 plays,[c]  154 sonnets, two long narrative poems, and several other poems. His plays have been translated into every major living language and are performed more often than those of any other playwright. He has invented over 1700 words and some of them are common, some of them are not. (<a href=\"https://en.wikipedia.org/wiki/William_Shakespeare\">Source</a>.)</p>\n<p>Looking for the '<a href=\"https://openlibrary.org/works/OL362289W/Plays\">First Folio</a>'?</p>",
    "wikipediaLink": "https://en.wikipedia.org/wiki/William_Shakespeare",
    "website": ""
}
```

## Extended Object collection item types

### ShelfItem
`https://www.w3id.org/BookWyrm/ns#ShelfItem`
_Included in version 1.0 of the BookWyrm vocabulary_

A `ShelfItem` represents an [Edition](#Edition) on a [Shelf](#Shelf).

#### Properties

Inherits all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, a `ShelfItem` has the following properties:

* [book](#book): `@id`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://www.w3id.org/BookWyrm/ns/"
    ],
    "id": "http://example.com/shelfbook/1",
    "type": "ShelfItem",
    "actor": "http://example.com/user/bookwyrm.instance.actor",
    "book": "http://example.com/book/2"
}
```

### ListItem
`https://www.w3id.org/BookWyrm/ns#ListItem`

_Included in version 1.0 of the BookWyrm vocabulary_

A `ListItem` represents an [Edition](#Edition) on a [BookList](#BookList).

#### Properties

Inherits all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, a `ListItem` has the following properties:

* [book](#book): `@id`
* [notes](#notes): `String`
* [approved](#approved): `Boolean`
* [order](#order): `Number`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://www.w3id.org/BookWyrm/ns/"
    ],
    "id": "http://example.com/shelfbook/1",
    "type": "ListItem",
    "actor": "http://example.com/user/bookwyrm.instance.actor",
    "book": "http://example.com/book/2",
    "notes": "I added this to the list because I like it",
    "approved": true,
    "order": 3
}
```

### SuggestionListItem
`https://www.w3id.org/BookWyrm/ns#SuggestionListItem`

_Included in version 1.0 of the BookWyrm vocabulary_

A `SuggestionListItem` represents a suggested [Work](#Work) on a [SuggestionList](#SuggestionList).

#### Properties

Inherits all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, a `SuggestionListItem` has the following properties:

* [book](#book): `@id`
* [notes](#notes): `String`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://www.w3id.org/BookWyrm/ns/"
    ],
    "id": "http://example.com/shelfbook/1",
    "type": "SuggestionListItem",
    "actor": "http://example.com/user/bookwyrm.instance.actor",
    "book": "http://example.com/book/2",
    "notes": "If you loved that you will love this"
}
```

### SeriesBook
`https://www.w3id.org/BookWyrm/ns#SeriesBook`

_Included in version 1.0 of the BookWyrm vocabulary_

A `SeriesBook` represents the relationship of a [Work](#Work) to a [Series](#Series).

#### Properties

Inherits all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, a `SeriesBook` has the following properties:

* [book](#book): `@id`
* [series](#series): `@id`
* [seriesNumber](#seriesNumber): `String`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://www.w3id.org/BookWyrm/ns/"
    ],
    "id": "http://example.com/seriesbook/1",
    "type": "SeriesBook",
    "actor": "http://example.com/user/bookwyrm.instance.actor",
    "book": "http://example.com/book/2",
    "series": "http://example.com/series/1",
    "seriesNumber": "99"
}
```

## Extended Note Types

These type are all extensions of the Activity Streams [`Note`](https://www.w3.org/ns/activitystreams#Note) object type.

### GeneratedNote
`https://www.w3id.org/BookWyrm/ns#GeneratedNote`

_Included in version 1.0 of the BookWyrm vocabulary_

<DIV class="notification is-warning is-light has-text-centered">
This type is under review and may be removed in a future version of BookWyrm
</DIV>

An extended `Note` that is auto-generated by BookWyrm. For example, when a user adds a book to one of their shelves.

There is no other difference between this type and a [`Note`](https://www.w3.org/ns/activitystreams#Note).

### Comment
`https://www.w3id.org/BookWyrm/ns#Comment`

_Included in version 1.0 of the BookWyrm vocabulary_

An extended `Note` related to an [Edition](#Edition).

#### Properties

Inherits all the properties of [`Note`](https://www.w3.org/ns/activitystreams#Note).

In addition, a `Comment` has the following extended properties:

* [inReplyToBook](#inReplyToBook): `@id`
* [readingStatus](#readingStatus): `String`
* [progress](#progress): `int`
* [progressMode](#progressMode): `String`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        {"bw": "https://www.w3id.org/BookWyrm/ns/"},
        { "Hashtag": "as:Hashtag" }
    ],
    "id": "https://example.net/user/library_lurker/comment/9",
    "type": ["bw:Comment", "Note"],
    "published": "2023-06-30T21:43:46.013132+00:00",
    "attributedTo": "https://example.net/user/library_lurker",
    "content": "<p>This is a very enjoyable book so far.</p>",
    "to": ["https://example.net/user/library_lurker/followers"],
    "cc": [],
    "replies": {
        "id": "https://example.net/user/library_lurker/comment/9/replies",
        "type": "OrderedCollection",
        "totalItems": 0,
        "first": "https://example.net/user/library_lurker/comment/9/replies?page=1",
        "last": "https://example.net/user/library_lurker/comment/9/replies?page=1",
        "@context": "https://www.w3.org/ns/activitystreams"
        },
    "summary": "Spoilers ahead!",
    "tag": [],
    "attachment": [],
    "sensitive": true,
    "bw:inReplyToBook": "https://example.net/book/1",
    "bw:readingStatus": "reading",
    "bw:progress": 25,
    "bw:progressMode": "PG"
}
```
### Quotation
`https://www.w3id.org/BookWyrm/ns#Quotation`

_Included in version 1.0 of the BookWyrm vocabulary_

A quotation from an [Edition](#Edition).

#### Properties

Inherits all the properties of [`Comment`](#comment).

In addition, a `Quotation` has the following extended properties:

* [quote](#quote): `String`
* [position](#position): `Number`
* [positionMode](#positionMode): `String`

### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        {"bw": "https://www.w3id.org/BookWyrm/ns/"},
        { "Hashtag": "as:Hashtag" }
    ],
    "id": "https://example.net/user/mouse/quotation/13",
    "url": "https://example.net/user/mouse/quotation/13",
    "inReplyTo": null,
    "published": "2020-05-10T02:38:31.150343+00:00",
    "attributedTo": "https://example.net/user/mouse",
    "to": [
        "https://www.w3.org/ns/activitystreams#Public"
        ],
    "cc": [
        "https://example.net/user/mouse/followers"
        ],
    "sensitive": false,
    "content": "I really like this quote",
    "type": ["bw:Quotation", "Note"],
    "replies": {
        "id": "https://example.net/user/mouse/quotation/13/replies",
        "type": "Collection",
        "first": {
            "type": "CollectionPage",
            "next": "https://example.net/user/mouse/quotation/13/replies?only_other_accounts=true&page=true",
            "partOf": "https://example.net/user/mouse/quotation/13/replies",
            "items": []
        }
    },
    "inReplyToBook": "https://example.net/book/1",
    "bw:quote": "To be or not to be, that is the question.",
    "bw:position": 50,
    "bw:positionMode": "PCT",
}
```

### Rating
`https://www.w3id.org/BookWyrm/ns#Rating`

_Included in version 1.0 of the BookWyrm vocabulary_

A star rating indicating the actor's impression of the quality of an [Edition](#Edition). This is essentially a review without any text.

#### Properties

Inherits the properties of [Review](#Review), however `content` and `name` are not used. Although this type inherits from `Review`, the advertised Activity Streams type is `Note` rather than `Activity`.

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        {"bw": "https://www.w3id.org/BookWyrm/ns/"},
        { "Hashtag": "as:Hashtag" }
    ],
    "id": "https://example.com/user/mouse/reviewrating/123",
    "type": ["bw:Rating", "Note"],
    "published": "2026-08-05T15:37:46.054716+00:00",
    "attributedTo": "https://example.com/user/mouse",
    "content": "rated <em><a href=\"https://example.com/book/36497\">The outsider</a></em>: 3 stars",
    "to": [
        "https://www.w3.org/ns/activitystreams#Public"
    ],
    "cc": [
        "https://example.com/user/mouse/followers"
    ],
    "replies": {
        "@context": ["https://www.w3.org/ns/activitystreams"],
        "id": "https://example.com/user/mouse/reviewrating/123/replies",
        "type": "OrderedCollection",
        "totalItems": 0,
        "first": "https://example.com/user/mouse/reviewrating/123/replies?page=1",
        "last": "https://example.com/user/mouse/reviewrating/123/replies?page=1",
    },
    "tag": [],
    "attachment": [
        {
            "type": "Document",
            "url": "https://example.com/images/previews/covers/_2EcfJ15.jpg",
            "name": "Stephen King: The outsider (AudiobookFormat, 2018)",
            "@context": [
                "https://www.w3.org/ns/activitystreams",
                { "Hashtag": "as:Hashtag" }
            ]
        }
    ],
    "sensitive": false,
    "bw:inReplyToBook": "https://example.com/book/36497",
    "bw:rating": 3.0,
    "bw:name": "Review of \"The outsider\" (3 stars): None"
}
```


## Extended Article types

These types inherit all properties from [Article](https://www.w3.org/ns/activitystreams#Article).

### Review
`https://www.w3id.org/BookWyrm/ns#Review`

_Included in version 1.0 of the BookWyrm vocabulary_

A written review of an [Edition](#Edition).

#### Properties

Inherits all properties from [Article](https://www.w3.org/ns/activitystreams#Article).

In addition, a `Review` has the following extended properties:

* [rating](#rating): `Number`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        {"bw": "https://www.w3id.org/BookWyrm/ns/"},
        { "Hashtag": "as:Hashtag" }
    ],
    "id": "https://example.net/user/library_lurker/review/2",
    "type": ["Review", "Article"],
    "published": "2023-06-30T21:43:46.013132+00:00",
    "attributedTo": "https://example.net/user/library_lurker",
    "content": "<p>This is an enjoyable book with great characters.</p>",
    "to": ["https://example.net/user/library_lurker/followers"],
    "cc": [],
    "replies": {
        "id": "https://example.net/user/library_lurker/review/2/replies",
        "type": "OrderedCollection",
        "totalItems": 0,
        "first": "https://example.net/user/library_lurker/review/2/replies?page=1",
        "last": "https://example.net/user/library_lurker/review/2/replies?page=1",
        "@context": "https://www.w3.org/ns/activitystreams"
        },
    "summary": "Spoilers ahead!",
    "tag": [],
    "attachment": [],
    "sensitive": true,
    "bw:inReplyToBook": "https://example.net/book/1",
    "bw:name": "What a cracking read",
    "bw:rating": 4.5
}
```

## Extended OrderedCollection types

These type are all based on the Activity Streams [`OrderedCollection`](https://www.w3.org/ns/activitystreams#OrderedCollection) core object types.

### OrderedCollection extended properties

Types in this group have all the properties of [`OrderedCollection`](https://www.w3.org/ns/activitystreams#OrderedCollection).

In addition, all extended `OrderedCollection` types have the following properties:

* [owner](#owner): `@id`

Other than [Series](#Series), these types make use of the `to` and `cc` properties of [`Object`](https://www.w3.org/ns/activitystreams#Object) to enable privacy controlled collections.

### Shelf
`https://www.w3id.org/BookWyrm/ns#Shelf`

_Included in version 1.0 of the BookWyrm vocabulary_

<DIV class="notification is-warning is-light has-text-centered">
This type is under review and may be removed in a future version of BookWyrm
</DIV>

A `Shelf` is a collection of [Edition](#Edition) objects. Shelves are used to indicate the reading status of an [Edition](#Edition).

#### Properties

`Shelf` inherits all the [OrderedCollection extended properties](#Orderedcollection-extended-properties).

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://www.w3id.org/BookWyrm/ns/"
    ],
    "id": "https://example.net/user/avid_reader/books/extraspecialbooks-5",
    "type": "Shelf",
    "totalItems": 0,
    "first": "https://example.net/user/avid_reader/books/extraspecialbooks-5?page=1",
    "last": "https://example.net/user/avid_reader/books/extraspecialbooks-5?page=1",
    "name": "Extra special books",
    "owner": "https://example.net/user/avid_reader",
    "to": [
        "https://www.w3.org/ns/activitystreams#Public"
    ],
    "cc": [
        "https://example.net/user/avid_reader/followers"
    ]
}
```

### BookList
`https://www.w3id.org/BookWyrm/ns#BookList`

_Included in version 1.0 of the BookWyrm vocabulary_

A `BookList` is a collection of [Edition](#Edition) objects, grouped together by an [Actor](https://www.w3.org/ns/activitystreams#actor) for any arbitrary reason. Items in a `BookList` are defined in [ListItem](#ListItem)

#### Properties

`BookList` inherits all the [OrderedCollection extended properties](#OrderedCollection-extended-properties).

In addition, `BookList` has the following properties:

* [curation](#curation): `String`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://www.w3id.org/BookWyrm/ns/"
    ],
    "id": "https://example.net/list/1",
    "type": "BookList",
    "totalItems": 0,
    "first": "https://example.net/list/1?page=1",
    "last": "https://example.net/list/1?page=1",
    "name": "My cool list",
    "owner": "https://example.net/user/avid_reader",
    "to": [
        "https://www.w3.org/ns/activitystreams#Public"
    ],
    "cc": [
        "https://example.net/user/avid_reader/followers"
    ],
    "summary": "A list of books I like.",
    "curation": "curated"
}
```

### SuggestionList
`https://www.w3id.org/BookWyrm/ns#SuggestionList`

_Included in version 1.0 of the BookWyrm vocabulary_

A `SuggestionList` is a collection of [SuggestionListItem](#SuggestionListItem) objects that can be added to by any [Actor](https://www.w3.org/ns/activitystreams#actor). A `SuggestionList` represents suggested works that may be similar to a given [Work](#Work) identified by the [book](#book) property.

#### Properties

`SuggestionList` inherits all the [OrderedCollection extended properties](#OrderedCollection-extended-properties).

In addition, `SuggestionList` has the following properties:

* [book](#book): `@id`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://www.w3id.org/BookWyrm/ns/"
    ],
    "id": "http://example.com/book/4/suggestions",
    "type": "SuggestionList",
    "totalItems": 1,
    "first": "http://example.com/book/4/suggestions?page=1",
    "last": "http://example.com/book/4/suggestions?page=1",
    "owner": "http://example.com/user/bookwyrm.instance.actor",
    "to": [
        "https://www.w3.org/ns/activitystreams#Public"
    ],
    "cc": [
        "http://example.com/user/bookwyrm.instance.actor/followers"
    ],
    "book": {
        ...
    }
}
```

### Series
`https://www.w3id.org/BookWyrm/ns#Series`

_Included in version 1.0 of the BookWyrm vocabulary_

A `Series` is a collection of [SeriesBook](#SeriesBook) objects representing [Work](#Work) objects in a formal series. An example of a series is "The Lord of the Rings" by J.R.R. Tolkien.

#### Properties

`Series` inherits all the [OrderedCollection extended properties](#OrderedCollection-extended-properties) but does **not** use `to` or `cc` from [`Object`](https://www.w3.org/ns/activitystreams#Object) as there is no concept of "privacy" for `Series` objects.

* [alternativeNames](#alternativeNames): `Array`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        "https://www.w3id.org/BookWyrm/ns/"
    ],
    "id": "http://example.com/series/1",
    "type": "Series",
    "totalItems": 1,
    "first": "http://example.com/series/1?page=1",
    "last": "http://example.com/series/1?page=1",
    "name": "An interesting series of books",
    "actor": "http://example.com/user/bookwyrm.instance.actor",
    "alternativeNames": []
}
```

## Properties

### aasin
`https://www.w3id.org/BookWyrm/ns#aasin`

_Included in version 1.0 of the BookWyrm vocabulary_

An [Amazon Standard Identification Number](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number) for an Audible audiobook. The same audiobook may have a different ASIN when sold by Amazon directly.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [asin](#asin)

### aliases
`https://www.w3id.org/BookWyrm/ns#aliases`

_Included in version 1.0 of the BookWyrm vocabulary_

Alternative names an author may be known by.

Type: `Array` of `String`s

Used on: [Author](#Author)

See also: [alternativeNames](#alternativeNames)

### alternativeNames
`https://www.w3id.org/BookWyrm/ns#alternativeNames`

_Included in version 1.0 of the BookWyrm vocabulary_

Alternative names a series may be known by.

Type: `Array` of `String`s

Used on: [Series](#Series)

See also: [aliases](#aliases)

### approved
`https://www.w3id.org/BookWyrm/ns#approved`

_Included in version 1.0 of the BookWyrm vocabulary_

Indicates whether a [ListItem](#ListItem) has been approved for inclusion in a [BookList](#BookList). This is only relevant for lists where the value of [curation](#curation) is `curated`.

Type: `Boolean`

Used on: [ListItem](#ListItem)

### asin
`https://www.w3id.org/BookWyrm/ns#asin`

_Included in version 1.0 of the BookWyrm vocabulary_

An [Amazon Standard Identification Number](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [aasin](#aasin)

### authors
`https://www.w3id.org/BookWyrm/ns#authors`

_Included in version 1.0 of the BookWyrm vocabulary_

The [Author](#Author)s associated with a [Work](#Work) or [Edition](#Edition).

Type: `Array` of `@id`s

Used on: [Work](#Work), [Edition](#Edition)

### bio
`https://www.w3id.org/BookWyrm/ns#bio`

_Included in version 1.0 of the BookWyrm vocabulary_

Biographical information about an [Author](#Author).

Type: `String`

Used on: [Author](#Author)

### bnfId
`https://www.w3id.org/BookWyrm/ns#bnfId`

_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier assigned by the Bibliothèque nationale de France (National library of France).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [gutenbergId](#gutenbergId), [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### book
`https://www.w3id.org/BookWyrm/ns#book`

_Included in version 1.0 of the BookWyrm vocabulary_

A book related to another object. This may represent either a [Work](#Work) or an [Edition](#Edition) depending on the object it is a property of.

Type: `@id`

Used on: [ListItem](#ListItem), [SeriesBook](#SeriesBook), [ShelfItem](#ShelfItem), [SuggestionList](#SuggestionList), [SuggestionListItem](#SuggestionListItem)

See also: [editions](#editions), [work](#work)

### born
`https://www.w3id.org/BookWyrm/ns#born`

_Included in version 1.0 of the BookWyrm vocabulary_

The birth date of an [Author](#Author) in the format `YYYY-MM-DD`. This represents a date but takes the form of a string.

Type: `String`

Used on: [Author](#Author)

See also: [died](#died)

### cover
`https://www.w3id.org/BookWyrm/ns#cover`

_Included in version 1.0 of the BookWyrm vocabulary_

The cover image for a book.

Type: [Document](https://www.w3.org/ns/activitystreams#Document)

Used on: [Work](#Work), [Edition](#Edition)

### curation
`https://www.w3id.org/BookWyrm/ns#curation`

_Included in version 1.0 of the BookWyrm vocabulary_

The type of curation for a [BookList](#BookList). Possible values are:

* `closed`: only the [owner](#owner) may add items to the list
* `open`: any other [Actor](https://www.w3.org/ns/activitystreams#actor) may add to the list.
* `curated`: Any other [Actor](https://www.w3.org/ns/activitystreams#actor) may add to the list, however the item must be [approved](#approved) by the [owner](#owner).
* `group`: Any other member of the group may add to the list.

Type: `String`

Used on: [BookList](#BookList)

Note: BookWyrm Groups are not currently ActivityPub objects.

### description
`https://www.w3id.org/BookWyrm/ns#description`

_Included in version 1.0 of the BookWyrm vocabulary_

A brief description or blurb for a book.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

Note: This is used rather than [summary](https://www.w3.org/ns/activitystreams#summary) because [summary](https://www.w3.org/ns/activitystreams#summary) is widely used within the fediverse (including BookWyrm) as a "content warning" property.

### died
`https://www.w3id.org/BookWyrm/ns#died`

_Included in version 1.0 of the BookWyrm vocabulary_

The date of death for an [Author](#Author) in the format `YYYY-MM-DD`. This represents a date but takes the form of a string.

Type: `String`

Used on: [Author](#Author)

See also: [born](#born)

### editionRank
`https://www.w3id.org/BookWyrm/ns#editionRank`

_Included in version 1.0 of the BookWyrm vocabulary_

A preferential ranking for an [Edition](#Edition) in comparison to other editions with the same parent work, based on the completeness of the [Edition](#Edition) object's metadata. [Edition](#Edition) objects with more complete will have a higher rank represented by a lower integer. This is used to determine which edition will be considered the "default".

Type: `Number`

Used on: [Edition](#Edition)

See also: [order](#order)

### editions
`https://www.w3id.org/BookWyrm/ns#editions`

_Included in version 1.0 of the BookWyrm vocabulary_

A list of [Edition](#Edition) objects that derive from a [Work](#Work).

Type: `Array` of `id`s

Used on: [Work](#Work)

### fileLinks
`https://www.w3id.org/BookWyrm/ns#fileLinks`

_Included in version 1.0 of the BookWyrm vocabulary_

A list of URLs representing web locations for a digital copy of a book.

Type: `Array` of [URL](https://www.w3.org/TR/url) `String`s

Used on: [Work](#Work), [Edition](#Edition)

### finnaKey
`https://www.w3id.org/BookWyrm/ns#finnaKey`

_Included in version 1.0 of the BookWyrm vocabulary_

The `id` field for any record from the National Library of Finland's [Finna.fi](https://www.finna.fi/Content/about) catalogue.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [bnfId](#bnfid), [goodreadsKey](#goodreadsKey), [gutenbergId](#gutenbergId), [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### firstPublishedDate
`https://www.w3id.org/BookWyrm/ns#firstPublishedDate`

_Included in version 1.0 of the BookWyrm vocabulary_

The first known publication date for a book in the format `YYYY-MM-DD`. This represents a date but takes the form of a string.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

See also: [publishedDate](#publishedDate)

### goodreadsKey
`https://www.w3id.org/BookWyrm/ns#goodreadsKey`

_Included in version 1.0 of the BookWyrm vocabulary_

The unique identifier for any record from [GoodReads](https://www.goodreads.com/).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [gutenbergId](#gutenbergId), [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### gutenbergId
`https://www.w3id.org/BookWyrm/ns#gutenbergId`

_Included in version 1.0 of the BookWyrm vocabulary_

The unique identifier for an author from [Project Gutenberg](https://gutenberg.org).

Type: `String`

Used on: [Author](#Author)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### inReplyToBook
`https://www.w3id.org/BookWyrm/ns#inReplyToBook`

_Included in version 1.0 of the BookWyrm vocabulary_

Represents an [Edition](#Edition) that is the subject of the content of an object. For example the book that is being reviewed.

Type: `@id`

Used on: [Comment](#Comment), [Quotation](#Quotation), [Rating](#Rating), [Review](#Review)

### inventaireId
`https://www.w3id.org/BookWyrm/ns#inventaireId`

_Included in version 1.0 of the BookWyrm vocabulary_

The unique identifier for any record from [Inventaire](https://inventaire.io).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

Note: Inventaire identifiers are [often, but not necessarily the same as wikidata ids](https://wiki.inventaire.io/wiki/Entities_data#Data_sources)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### isbn10
`https://www.w3id.org/BookWyrm/ns#isbn10`

_Included in version 1.0 of the BookWyrm vocabulary_

An International Standard Book Number (ISBN). `isbn10` is the original 10-digit format for ISBNs.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### isbn13
`https://www.w3id.org/BookWyrm/ns#isbn13`

_Included in version 1.0 of the BookWyrm vocabulary_

An International Standard Book Number (ISBN). `isbn13` is the modern 13-digit format for ISBNs.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### isfdb
`https://www.w3id.org/BookWyrm/ns#isfdb`

_Included in version 1.0 of the BookWyrm vocabulary_

The unique identifier for a record in the [Internet Speculative Fiction Database](https://www.isfdb.org/).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### isni
`https://www.w3id.org/BookWyrm/ns#isni`

_Included in version 1.0 of the BookWyrm vocabulary_

The [International Standard Name Identifier](https://isni.org/) for an author.

Type: `String`

Used on: [Author](#Author)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [lccn](#lccn), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### languages
`https://www.w3id.org/BookWyrm/ns#languages`

_Included in version 1.0 of the BookWyrm vocabulary_

A list of the languages in which a book has been published.

Type: `Array` of `String`s.

Used on: [Work](#Work), [Edition](#Edition)

Note: This is an uncontrolled field and may itself be written in multiple languages.

### lastEditedBy
`https://www.w3id.org/BookWyrm/ns#lastEditedBy`

_Included in version 1.0 of the BookWyrm vocabulary_

An [actor](https://www.w3.org/ns/activitystreams#actor) who last made changes to an object.

Type: `@id`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

### lccn
`https://www.w3id.org/BookWyrm/ns#lccn`

_Included in version 1.0 of the BookWyrm vocabulary_

The [Library of Congress Control Number](https://en.wikipedia.org/wiki/Library_of_Congress_Control_Number) for a work.

Type: `String`

Used on: [Work](#Work)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingKey), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### librarythingKey
`https://www.w3id.org/BookWyrm/ns#librarythingKey`

_Included in version 1.0 of the BookWyrm vocabulary_

A unique identifier from [Library Thing](https://www.librarything.com/).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

### librisKey
`https://www.w3id.org/BookWyrm/ns#librisKey`

_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier from the Swedish libraries' union catalogue [Libris](https://libris.kb.se).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingKey), [lccn](#lccn), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)

Used on: [Author](#Author), [Review](#Review)

### notes
`https://www.w3id.org/BookWyrm/ns#notes`

_Included in version 1.0 of the BookWyrm vocabulary_

A brief explanatory note.

Type: `String`

Used on: [ListItem](#ListItem), [SuggestionListItem](#SuggestionListItem)

### oclcNumber
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier for an edition recorded in [OCLC](https://www.oclc.org)'s [WorldCat](https://search.worldcat.org/). This is formally known as the [OCLC Control Number](https://www.oclc.org/bibformats/en/fixedfield/oclc.html) and may be recorded in other systems, especially library catalogues.

Type: `String`

Used on: [Edition](#Edition)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingKey), [lccn](#lccn), [librisKey](#librisKey), [openlibraryKey](#openlibraryKey), [viaf](#viaf), [wikidata](#wikidata)


### openlibraryKey
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier for records from [Open Library](https://openlibrary.org/).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingKey), [lccn](#lccn), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [viaf](#viaf), [wikidata](#wikidata)

### order
_Included in version 1.0 of the BookWyrm vocabulary_

An item's place in a sequential order.

Type: `Number`

Used on: [ListItem](#ListItem)

See also: [editionRank](#editionRank)

### owner
_Included in version 1.0 of the BookWyrm vocabulary_

The [Actor](https://www.w3.org/ns/activitystreams#actor) who created an object.

Type: `@id`

Used on: [BookList](#BookList), [Series](#Series), [Shelf](#Shelf), [SuggestionList](#SuggestionList)

### pages
_Included in version 1.0 of the BookWyrm vocabulary_

The number of pages in a book.

Type: `Number`

Used on: [Work](#Work), [Edition](#Edition)

### physicalFormat
_Included in version 1.0 of the BookWyrm vocabulary_

The physical format of a book. For example "Paperback". This is a controlled field in the BookWyrm user interface. Options are:

* `AudiobookFormat`
* `EBook`
* `GraphicNovel`
* `Hardcover`
* `Paperback`

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

### physicalFormatDetail
_Included in version 1.0 of the BookWyrm vocabulary_

More specific detail regarding the physical format of a book. For example "spiral bound". This is a free text field in the BookWyrm user interface.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

### position
_Included in version 1.0 of the BookWyrm vocabulary_

The position within a book in which a quote appears.

Type: `Number`

Used on: [Quotation](#Quotation)

See also: [progress](#progress)

### positionMode
_Included in version 1.0 of the BookWyrm vocabulary_

The measure that [position](#position) represents. This is a controlled field in the BookWyrm user interface. Options are:

* `PG` representing "pages"
* `PCT` representing "percentage"

Type: `String`

Used on: [Quotation](#Quotation)

See also: [progressMode](#progressmode)

### progress
_Included in version 1.0 of the BookWyrm vocabulary_

How much of a book an [Actor](https://www.w3.org/ns/activitystreams#actor) has read.

Type: `Number`

Used on: [Comment](#Comment)

See also: [position](position)

### progressMode
_Included in version 1.0 of the BookWyrm vocabulary_

The measure that [progress](#progress) represents. This is a controlled field in the BookWyrm user interface. Options are:

* `PG` representing "pages"
* `PCT` representing "percentage"

Type: `String`

Used on: [Comment](#Comment)

See also: [PositionMode](#positionmode)

### publishedDate
_Included in version 1.0 of the BookWyrm vocabulary_

The publication date for a specific book in the format `YYYY-MM-DD`. This represents a date but takes the form of a string.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

See also: [firstPublishedDate](#firstPublishedDate)

### publishers
_Included in version 1.0 of the BookWyrm vocabulary_

A list of publishers of a book.

Type: `Array` of `String`s

Used on: [Edition](#Edition)

### quote
_Included in version 1.0 of the BookWyrm vocabulary_

The text of a quotation from a book.

Type: `String`

Used on: [Quotation](#Quotation)

Note: [Quotation](#Quotation) objects can be coerced into a [Note](https://www.w3.org/ns/activitystreams#Note). Applications that implement [FEP-044f quote-posts](https://w3id.org/fep/044f#quote) also have a `quote` property which references another [Note](https://www.w3.org/ns/activitystreams#Note) by its id. Care should be taken to ensure the `quote` property is handled correctly according to each context.

### rating
_Included in version 1.0 of the BookWyrm vocabulary_

A star rating indicating the [Actor](https://www.w3.org/ns/activitystreams#actor)'s impression of the quality of an [Edition](#Edition).

Type: `Number`

Used on: [Rating](#Rating), [Review](#Review)

### readingStatus
_Included in version 1.0 of the BookWyrm vocabulary_

A status indicating an [Actor](https://www.w3.org/ns/activitystreams#actor)'s overall reading progress for an [Edition](#Edition). This is a controlled field in the BookWyrm user interface. Options are:

* `to-read`
* `reading`
* `read`
* `stopped-reading`

Type: `String`

Used on: [Comment](#Comment)

Note: Currently there is a strong relationship between [readingStatus](#readingstatus) and [ShelfItem](#ShelfItem), and every BookWyrm user has a [Shelf](#Shelf) with an identifier that matches the reading status options listed above. This may change in future.

See also: [ShelfItem](#ShelfItem)

### series
_Included in version 1.0 of the BookWyrm vocabulary_

The name of a series of books, or the `@id` of a [Series](#Series).

Type: `String` or `@id`

Used on: [Work](#Work), [Edition](#Edition), [SeriesBook](#SeriesBook)

Note: When used on [Work](#Work) or [Edition](#Edition), `series` is a legacy property retained for backwards-compatibility. The correct way to identify [Series](#Series) objects associated with a [Work](#Work) is to dereference any associated [SeriesBook](#SeriesBook) objects and their [series](#series) property.

### seriesBooks
_Included in version 1.0 of the BookWyrm vocabulary_

A list of [SeriesBook](#SeriesBook) associated with a book.

Type: `Array` of `@id`s

Used on: [Work](#Work)

Note: This property was formerly also used on [Edition](#Edition). Some BookWyrm instances may still send [Edition](#Edition) objects with the `seriesBooks` property, which will always be empty.

### seriesNumber
_Included in version 1.0 of the BookWyrm vocabulary_

The name of a series of books, or the `@id` of a [Series](#Series).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [SeriesBook](#SeriesBook)

Note: When used on [Work](#Work) or [Edition](#Edition), `seriesNumber` is a legacy property retained for backwards-compatibility. The correct way to identify the series number associated with a [Work](#Work) is to dereference any associated [SeriesBook](#SeriesBook) objects and their [seriesNumber](#seriesNumber) property.

### sortTitle
_Included in version 1.0 of the BookWyrm vocabulary_

A version of a book title used for the purposes of alphabetical sorting.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

Note: This property does not currently handle multi-lingual sorting.

### subjectPlaces
_Included in version 1.0 of the BookWyrm vocabulary_

A list of geographic locations in which a book is set.

Type: `Array` of `String`s

Used on: [Work](#Work), [Edition](#Edition)

### subjects
_Included in version 1.0 of the BookWyrm vocabulary_

A list of topics a book is about.

Type: `Array` of `String`s

Used on: [Work](#Work), [Edition](#Edition)

### subtitle
_Included in version 1.0 of the BookWyrm vocabulary_

A secondary part of the title of a book. Same as [alternativeHeadline](https://schema.org/alternativeHeadline) or [subtitle](https://www.wikidata.org/wiki/Q1135389).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

Note: this does *not* refer to an "alternative" title.

See also: [title](#title)

### title
_Included in version 1.0 of the BookWyrm vocabulary_

The title or name of a book.

Type: `String`

Used on: [Work](#Work), [Edition](#Edition)

See also: [subtitle](#subtitle)

### viaf
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier from the [The Virtual International Authority File](https://viaf.org)

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingKey), [lccn](#lccn), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [wikidata](#wikidata)

### website
_Included in version 1.0 of the BookWyrm vocabulary_

The personal website of an author.

Type: `String` representing a [URL](https://www.w3.org/TR/url)

Used on: [Author](#Author)

### wikidata
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier for a record from the [wikidata](https://www.wikidata.org).

Type: `String`

Used on: [Work](#Work), [Edition](#Edition), [Author](#Author), [Series](#Series)

See also: [bnfId](#bnfid), [finnaKey](#finnaKey), [goodreadsKey](#goodreadsKey), [GutenbergId](#GutenbergId) [inventaireId](#inventaireId), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingKey), [lccn](#lccn), [librisKey](#librisKey), [oclcNumber](#oclcNumber), [openlibraryKey](#openlibraryKey), [viaf](#viaf)

### wikipediaLink
_Included in version 1.0 of the BookWyrm vocabulary_

The URL of a Wikipedia page.

Type: `String` representing a [URL](https://www.w3.org/TR/url)

Used on: [Author](#Author)

Note: As [Author](#Author) also has a [wikidata](#wikidata) property which could be used to obtain Wikipedia URLs, this property may be removed in future.

### work
_Included in version 1.0 of the BookWyrm vocabulary_

The parent [Work](#Work) of an [Edition](#Edition).

Type: `@id`

Used on: [Edition](#Edition)
