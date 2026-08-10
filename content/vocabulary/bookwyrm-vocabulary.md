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

## Extended Object book types

The basic BookWyrm types are all extensions of the core Activity Streams [Object](https://www.w3.org/ns/activitystreams#Object) type.

### Core book type properties

All types in this section ([Work](#work), [Edition](#edition), [Author](#author), [Series](#series)) have all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, all types in this section have the following properties:

* [openlibraryKey](#openlibrarykey): `String`
* [inventaireId](#inventaireid): `String`
* [finnaKey](#finnakey): `String`
* [librisKey](#libriskey): `String`
* [librarythingKey](#librarythingkey): `String`
* [goodreadsKey](#goodreadskey): `String`
* [bnfId](#bnfid): `String`
* [viaf](#viaf): `String`
* [wikidata](#wikidata): `String`
* [asin](#asin): `String`
* [aasin](#aasin): `String`
* [isfdb](#isfdb): `String`
* [lastEditedBy](#lasteditedby): `@id`

### Extended book type properties

In addition to the core properties above, [Work](#work) and [Edition](#edition) types have the following extended properties:

* [title](#title): `String`
* [sortTitle](#sorttitle): `String`
* [subtitle](#subtitle): `String`
* [description](#description): `String`
* [languages](#languages): `Array`
* [series](#series_1): `String`
* [seriesNumber](#seriesnumber): `String`
* [seriesBooks](#seriesbooks): `Array`
* [subjects](#subjects): `Array`
* [subjectPlaces](#subjectplaces): `Array`
* [authors](#authors): `Array`
* [firstPublishedDate](#firstpublisheddate): `String`
* [publishedDate](#publisheddate): `String`
* [fileLinks](#filelinks): `Array`
* [cover](#cover): `Document`

### Work
_Included in version 1.0 of the BookWyrm vocabulary_

A bibliographic work, which manifests in the form of one or more [Edition](#edition)s.

#### Properties

Inherits all the [Object](https://www.w3.org/ns/activitystreams#Object), [Core book type](#core-book-type-properties) and [Extended book type](#extended-book-type-properties) properties.

In addition, a `Work` has the following extended properties:

* [lccn](#lccn): `String`
* [editions](#editions): `Array`

#### Example

```json
{
    "@context": [
        "https://www.w3id.org/bookwyrm/ns",
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
_Included in version 1.0 of the BookWyrm vocabulary_

The manifestation of a [Work](#work) as a specific edition.

#### Properties

Inherits all the [Object](https://www.w3.org/ns/activitystreams#Object), [Core book type](#core-book-type-properties) and [Extended book type](#extended-book-type-properties) properties.

In addition, an `Edition` has the following extended properties:

* [work](#work_1): `@id`
* [isbn10](#isbn10): `String`
* [isbn13](#isbn13): `String`
* [oclcNumber](#oclcnumber): `String`
* [pages](#pages): `Number`
* [physicalFormat](#physicalformat): `String`
* [physicalFormatDetail](#physicalformatdetail): `String`
* [publishers](#publishers): `Array`
* [editionRank](#editionrank): `Number`

#### Example

```json
{
    "@context": [
        "https://www.w3id.org/bookwyrm/ns",
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
_Included in version 1.0 of the BookWyrm vocabulary_

A creator of a [Work](#work) or [Edition](#edition). This includes creative contributions such as editor, illustrator, or translator.

#### Properties

Inherits all the [Object](https://www.w3.org/ns/activitystreams#Object) and [Core book type](#core-book-type-properties) properties.

In addition, an `Author` has the following extended properties:

* [isni](#isni): `String`
* [gutenbergId](#gutenbergid): `String`
* [born](#born): `String`
* [died](#died): `String`
* [aliases](#aliases): `Array`
* [bio](#bio): `String`
* [wikipediaLink](#wikipedialink): `String`
* [website](#website): `String`

#### Example

```json
{
    "@context": [
        "https://www.w3id.org/bookwyrm/ns",
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
_Included in version 1.0 of the BookWyrm vocabulary_

A `ShelfItem` represents an [Edition](#edition) on a [Shelf](#shelf).

#### Properties

Inherits all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, a `ShelfItem` has the following properties:

* [book](#book): `@id`

#### Example

TODO

### ListItem
_Included in version 1.0 of the BookWyrm vocabulary_

A `ListItem` represents an [Edition](#edition) on a [BookList](#booklist).

#### Properties

Inherits all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, a `ListItem` has the following properties:

* [book](#book): `@id`
* [notes](#notes): `String`
* [approved](#approved): `Boolean`
* [order](#order): `Number`

#### Example

TODO

### SuggestionListItem
_Included in version 1.0 of the BookWyrm vocabulary_

A `SuggestionListItem` represents a suggested [Work](#work) on a [SuggestionList](#suggestionlist).

#### Properties

Inherits all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, a `SuggestionListItem` has the following properties:

* [book](#book): `@id`
* [notes](#notes): `String`

#### Example

TODO

### SeriesBook
_Included in version 1.0 of the BookWyrm vocabulary_

A `SeriesBook` represents the relationship of a [Work](#work) to a [Series](#series).

#### Properties

Inherits all the properties of [Object](https://www.w3.org/ns/activitystreams#Object).

In addition, a `SeriesBook` has the following properties:

* [book](#book): `@id`
* [series](#series_1): `@id`
* [seriesNumber](#seriesnumber): `String`

#### Example

TODO


## Extended Note Types

These type are all extensions of the Activity Streams [`Note`](https://www.w3.org/ns/activitystreams#Note) object type.

### GeneratedNote
_Included in version 1.0 of the BookWyrm vocabulary_

<DIV class="notification is-warning is-light has-text-centered">
This type is under review and may be removed in a future version of BookWyrm
</DIV>

An extended `Note` that is auto-generated by BookWyrm. For example, when a user adds a book to one of their shelves.

There is no other difference between this type and a [`Note`](https://www.w3.org/ns/activitystreams#Note).

### Comment
_Included in version 1.0 of the BookWyrm vocabulary_

An extended `Note` related to an [Edition](#edition).

#### Properties

Inherits all the properties of [`Note`](https://www.w3.org/ns/activitystreams#Note).

In addition, a `Comment` has the following extended properties:

* [inReplyToBook](#inreplytobook): `@id`
* [readingStatus](#readingstatus): `String`
* [progress](#progress): `int`
* [progressMode](#progressmode): `String`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        {"bw": "https://www.w3id.org/bookwyrm/ns/"}
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
_Included in version 1.0 of the BookWyrm vocabulary_

A quotation from an [Edition](#edition).

#### Properties

Inherits all the properties of [`Comment`](#comment).

In addition, a `Quotation` has the following extended properties:

* [quote    ](#quote): `String`
* [position](#position): `Number`
* [positionMode](#positionmode): `String`

### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        {"bw": "https://www.w3id.org/bookwyrm/ns/"}
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
_Included in version 1.0 of the BookWyrm vocabulary_

A star rating indicating the actor's impression of the quality of an [Edition](#edition). This is essentially a review without any text.

#### Properties

Inherits the properties of [Review](#review), however `content` and `name` are not used. Although this type inherits from `Review`, the advertised Activity Streams type is `Note` rather than `Activity`.

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        {"bw": "https://www.w3id.org/bookwyrm/ns/"}
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
_Included in version 1.0 of the BookWyrm vocabulary_

A written review of an [Edition](#edition).

#### Properties

Inherits all properties from [Article](https://www.w3.org/ns/activitystreams#Article).

In addition, a `Review` has the following extended properties:

* [rating](#rating_1): `Number`

#### Example

```json
{
    "@context": [
        "https://www.w3.org/ns/activitystreams",
        {"bw": "https://www.w3id.org/bookwyrm/ns/"}
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

Other than [Series](#series), these types make use of the `to` and `cc` properties of [`Object`](https://www.w3.org/ns/activitystreams#Object) to enable privacy controlled collections.

### Shelf
_Included in version 1.0 of the BookWyrm vocabulary_

<DIV class="notification is-warning is-light has-text-centered">
This type is under review and may be removed in a future version of BookWyrm
</DIV>

A `Shelf` is a collection of [Edition](#edition) objects. Shelves are used to indicate the reading status of an [Edition](#edition).

#### Properties

`Shelf` inherits all the [OrderedCollection extended properties](#orderedcollection-extended-properties).

#### Example

```json
{
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
    ],
    "@context": "https://www.w3.org/ns/activitystreams"
}
```

### BookList
_Included in version 1.0 of the BookWyrm vocabulary_

A `BookList` is a collection of [Edition](#edition) objects, grouped together by an [Actor](https://www.w3.org/ns/activitystreams#actor) for any arbitrary reason. Items in a `BookList` are defined in [ListItem](#listitem)

#### Properties

`BookList` inherits all the [OrderedCollection extended properties](#orderedcollection-extended-properties).

In addition, `BookList` has the following properties:

* [curation](#curation): `String`

#### Example

```json
{
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
    "curation": "curated",
    "@context": "https://www.w3.org/ns/activitystreams"
}
```

### SuggestionList
_Included in version 1.0 of the BookWyrm vocabulary_

A `SuggestionList` is a collection of [SuggestionListItem](#suggestionlistitem) objects that can be added to by any [Actor](https://www.w3.org/ns/activitystreams#actor). A `SuggestionList` represents suggested works that may be similar to a given [Work](#work) identified by the [book](#book) property.

#### Properties

`SuggestionList` inherits all the [OrderedCollection extended properties](#orderedcollection-extended-properties).

In addition, `SuggestionList` has the following properties:

* [book](#book): `@id`

#### Example

TODO

### Series
_Included in version 1.0 of the BookWyrm vocabulary_

A `Series` is a collection of [SeriesBook](#seriesbook) objects representing [Work](#work) objects in a formal series. An example of a series is "The Lord of the Rings" by J.R.R. Tolkien.

#### Properties

`Series` inherits all the [OrderedCollection extended properties](#orderedcollection-extended-properties) but does **not** use `to` or `cc` from [`Object`](https://www.w3.org/ns/activitystreams#Object) as there is no concept of "privacy" for `Series` objects.

* [alternativeNames](#alternativenames): `Array`

#### Example

TODO

## Properties

### aasin
_Included in version 1.0 of the BookWyrm vocabulary_

An [Amazon Standard Identification Number](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number) for an Audible audiobook. The same audiobook may have a different ASIN when sold by Amazon directly.

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [asin](#asin)

### aliases
_Included in version 1.0 of the BookWyrm vocabulary_

Alternative names an author may be known by.

Type: `Array` of `String`s

Used on: [Author](#author)

See also: [alternativeNames](#alternativenames)

### alternativeNames
_Included in version 1.0 of the BookWyrm vocabulary_

Alternative names a series may be known by.

Type: `Array` of `String`s

Used on: [Series](#series)

See also: [aliases](#aliases)

### approved
_Included in version 1.0 of the BookWyrm vocabulary_

Indicates whether a [ListItem](#listitem) has been approved for inclusion in a [BookList](#booklist). This is only relevant for lists where the value of [curation](#curation) is `curated`.

Type: `Boolean`

Used on: [ListItem](#listitem)

### asin
_Included in version 1.0 of the BookWyrm vocabulary_

An [Amazon Standard Identification Number](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [aasin](#aasin)

### authors
_Included in version 1.0 of the BookWyrm vocabulary_

The [Author](#author)s associated with a [Work](#work) or [Edition](#edition).

Type: `Array` of `@id`s

Used on: [Work](#work), [Edition](#edition)

### bio
_Included in version 1.0 of the BookWyrm vocabulary_

Biographical information about an [Author](#author).

Type: `String`

Used on: [Author](#author)

### bnfId
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier assigned by the Bibliothèque nationale de France (National library of France).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [gutenbergId](#gutenbergid), [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### book
_Included in version 1.0 of the BookWyrm vocabulary_

A book related to another object. This may represent either a [Work](#work) or an [Edition](#edition) depending on the object it is a property of.

Type: `@id`

Used on: [ListItem](#listitem), [SeriesBook](#seriesbook), [ShelfItem](#shelfitem), [SuggestionList](#suggestionlist), [SuggestionListItem](#suggestionlistitem)

See also: [editions](#editions), [work](#work_1)

### born
_Included in version 1.0 of the BookWyrm vocabulary_

The birth date of an [Author](#author) in the format `YYYY-MM-DD`. This represents a date but takes the form of a string.

Type: `String`

Used on: [Author](#author)

See also: [died](#died)

### cover
_Included in version 1.0 of the BookWyrm vocabulary_

The cover image for a book.

Type: [Document](https://www.w3.org/ns/activitystreams#Document)

Used on: [Work](#work), [Edition](#edition)

### curation
_Included in version 1.0 of the BookWyrm vocabulary_

The type of curation for a [BookList](#booklist). Possible values are:

* `closed`: only the [owner](#owner) may add items to the list
* `open`: any other [Actor](https://www.w3.org/ns/activitystreams#actor) may add to the list.
* `curated`: Any other [Actor](https://www.w3.org/ns/activitystreams#actor) may add to the list, however the item must be [approved](#approved) by the [owner](#owner).
* `group`: Any other member of the group may add to the list.

Type: `String`

Used on: [BookList](#booklist)

Note: BookWyrm Groups are not currently ActivityPub objects.

### description
_Included in version 1.0 of the BookWyrm vocabulary_

A brief description or blurb for a book.

Type: `String`

Used on: [Work](#work), [Edition](#edition)

Note: This is used rather than [summary](https://www.w3.org/ns/activitystreams#summary) because [summary](https://www.w3.org/ns/activitystreams#summary) is widely used within the fediverse (including BookWyrm) as a "content warning" property.

### died
_Included in version 1.0 of the BookWyrm vocabulary_

The date of death for an [Author](#author) in the format `YYYY-MM-DD`. This represents a date but takes the form of a string.

Type: `String`

Used on: [Author](#author)

See also: [born](#born)

### editionRank
_Included in version 1.0 of the BookWyrm vocabulary_

A preferential ranking for an [Edition](#edition) in comparison to other editions with the same parent work, based on the completeness of the [Edition](#edition) object's metadata. [Edition](#edition) objects with more complete will have a higher rank represented by a lower integer. This is used to determine which edition will be considered the "default".

Type: `Number`

Used on: [Edition](#edition)

See also: [order](#order)

### editions
_Included in version 1.0 of the BookWyrm vocabulary_

A list of [Edition](#edition) objects that derive from a [Work](#work).

Type: `Array` of `id`s

Used on: [Work](#work)

### fileLinks
_Included in version 1.0 of the BookWyrm vocabulary_

A list of URLs representing web locations for a digital copy of a book.

Type: `Array` of [URL](https://www.w3.org/TR/url) `String`s

Used on: [Work](#work), [Edition](#edition)

### finnaKey
_Included in version 1.0 of the BookWyrm vocabulary_

The `id` field for any record from the National Library of Finland's [Finna.fi](https://www.finna.fi/Content/about) catalogue.

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [bnfId](#bnfid), [goodreadsKey](#goodreadskey), [gutenbergId](#gutenbergid), [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### firstPublishedDate
_Included in version 1.0 of the BookWyrm vocabulary_

The first known publication date for a book in the format `YYYY-MM-DD`. This represents a date but takes the form of a string.

Type: `String`

Used on: [Work](#work), [Edition](#edition)

See also: [publishedDate](#publisheddate)

### goodreadsKey
_Included in version 1.0 of the BookWyrm vocabulary_

The unique identifier for any record from [GoodReads](https://www.goodreads.com/).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [gutenbergId](#gutenbergid), [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### gutenbergId
_Included in version 1.0 of the BookWyrm vocabulary_

The unique identifier for an author from [Project Gutenberg](https://gutenberg.org).

Type: `String`

Used on: [Author](#author)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### inReplyToBook
_Included in version 1.0 of the BookWyrm vocabulary_

Represents an [Edition](#edition) that is the subject of the content of an object. For example the book that is being reviewed.

Type: `@id`

Used on: [Comment](#comment), [Quotation](#quotation), [Rating](#rating), [Review](#review)

### inventaireId
_Included in version 1.0 of the BookWyrm vocabulary_

The unique identifier for any record from [Inventaire](https://inventaire.io).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

Note: Inventaire identifiers are [often, but not necessarily the same as wikidata ids](https://wiki.inventaire.io/wiki/Entities_data#Data_sources)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### isbn10
_Included in version 1.0 of the BookWyrm vocabulary_

An International Standard Book Number (ISBN). `isbn10` is the original 10-digit format for ISBNs.

Type: `String`

Used on: [Work](#work), [Edition](#edition)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### isbn13
_Included in version 1.0 of the BookWyrm vocabulary_

An International Standard Book Number (ISBN). `isbn13` is the modern 13-digit format for ISBNs.

Type: `String`

Used on: [Work](#work), [Edition](#edition)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### isfdb
_Included in version 1.0 of the BookWyrm vocabulary_

The unique identifier for a record in the [Internet Speculative Fiction Database](https://www.isfdb.org/).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### isni
_Included in version 1.0 of the BookWyrm vocabulary_

The [International Standard Name Identifier](https://isni.org/) for an author.

Type: `String`

Used on: [Author](#author)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [lccn](#lccn), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### languages
_Included in version 1.0 of the BookWyrm vocabulary_

A list of the languages in which a book has been published.

Type: `Array` of `String`s.

Used on: [Work](#work), [Edition](#edition)

Note: This is an uncontrolled field and may itself be written in multiple languages.

### lastEditedBy
_Included in version 1.0 of the BookWyrm vocabulary_

An [actor](https://www.w3.org/ns/activitystreams#actor) who last made changes to an object.

Type: `@id`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

### lccn
_Included in version 1.0 of the BookWyrm vocabulary_

The [Library of Congress Control Number](https://en.wikipedia.org/wiki/Library_of_Congress_Control_Number) for a work.

Type: `String`

Used on: [Work](#work)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingkey), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

### librarythingKey
_Included in version 1.0 of the BookWyrm vocabulary_

A unique identifier from [Library Thing](https://www.librarything.com/).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [lccn](#lccn), [librisKey](#libriskey), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)


### librisKey
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier from the Swedish libraries' union catalogue [Libris](https://libris.kb.se).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingkey), [lccn](#lccn), [oclcNumber](#oclcnumber), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)

Used on: [Author](#author), [Review](#review)

### notes
_Included in version 1.0 of the BookWyrm vocabulary_

A brief explanatory note.

Type: `String`

Used on: [ListItem](#listitem), [SuggestionListItem](#suggestionlistitem)

### oclcNumber
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier for an edition recorded in [OCLC](https://www.oclc.org)'s [WorldCat](https://search.worldcat.org/). This is formally known as the [OCLC Control Number](https://www.oclc.org/bibformats/en/fixedfield/oclc.html) and may be recorded in other systems, especially library catalogues.

Type: `String`

Used on: [Edition](#edition)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingkey), [lccn](#lccn), [librisKey](#libriskey), [openlibraryKey](openlibrarykey), [viaf](#viaf), [wikidata](#wikidata)


### openlibraryKey
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier for records from [Open Library](https://openlibrary.org/).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingkey), [lccn](#lccn), [librisKey](#libriskey), [oclcNumber](oclcnumber), [viaf](#viaf), [wikidata](#wikidata)

### order
_Included in version 1.0 of the BookWyrm vocabulary_

An item's place in a sequential order.

Type: `Number`

Used on: [ListItem](#listitem)

See also: [editionRank](#editionrank)

### owner
_Included in version 1.0 of the BookWyrm vocabulary_

The [Actor](https://www.w3.org/ns/activitystreams#actor) who created an object.

Type: `@id`

Used on: [BookList](#booklist), [Series](#series), [Shelf](#shelf), [SuggestionList](#suggestionlist)

### pages
_Included in version 1.0 of the BookWyrm vocabulary_

The number of pages in a book.

Type: `Number`

Used on: [Work](#work), [Edition](#edition)

### physicalFormat
_Included in version 1.0 of the BookWyrm vocabulary_

The physical format of a book. For example "Paperback". This is a controlled field in the BookWyrm user interface. Options are:

* `AudiobookFormat`
* `EBook`
* `GraphicNovel`
* `Hardcover`
* `Paperback`

Type: `String`

Used on: [Work](#work), [Edition](#edition)

### physicalFormatDetail
_Included in version 1.0 of the BookWyrm vocabulary_

More specific detail regarding the physical format of a book. For example "spiral bound". This is a free text field in the BookWyrm user interface.

Type: `String`

Used on: [Work](#work), [Edition](#edition)

### position
_Included in version 1.0 of the BookWyrm vocabulary_

The position within a book in which a quote appears.

Type: `Number`

Used on: [Quotation](#quotation)

See also: [progress](#progress)

### positionMode
_Included in version 1.0 of the BookWyrm vocabulary_

The measure that [position](#position) represents. This is a controlled field in the BookWyrm user interface. Options are:

* `PG` representing "pages"
* `PCT` representing "percentage"

Type: `String`

Used on: [Quotation](#quotation)

See also: [progressMode](#progressmode)

### progress
_Included in version 1.0 of the BookWyrm vocabulary_

How much of a book an [Actor](https://www.w3.org/ns/activitystreams#actor) has read.

Type: `Number`

Used on: [Comment](#comment)

See also: [position](position)

### progressMode
_Included in version 1.0 of the BookWyrm vocabulary_

The measure that [progress](#progress) represents. This is a controlled field in the BookWyrm user interface. Options are:

* `PG` representing "pages"
* `PCT` representing "percentage"

Type: `String`

Used on: [Comment](#comment)

See also: [PositionMode](#positionmode)

### publishedDate
_Included in version 1.0 of the BookWyrm vocabulary_

The publication date for a specific book in the format `YYYY-MM-DD`. This represents a date but takes the form of a string.

Type: `String`

Used on: [Work](#work), [Edition](#edition)

See also: [firstPublishedDate](#firstpublisheddate)

### publishers
_Included in version 1.0 of the BookWyrm vocabulary_

A list of publishers of a book.

Type: `Array` of `String`s

Used on: [Edition](#edition)

### quote
_Included in version 1.0 of the BookWyrm vocabulary_

The text of a quotation from a book.

Type: `String`

Used on: [Quotation](#quotation)

Note: [Quotation](#quotation) objects can be coerced into a [Note](https://www.w3.org/ns/activitystreams#Note). Applications that implement [FEP-044f quote-posts](https://w3id.org/fep/044f#quote) also have a `quote` property which references another [Note](https://www.w3.org/ns/activitystreams#Note) by its id. Care should be taken to ensure the `quote` property is handled correctly according to each context.

### rating
_Included in version 1.0 of the BookWyrm vocabulary_

A star rating indicating the [Actor](https://www.w3.org/ns/activitystreams#actor)'s impression of the quality of an [Edition](#edition).

Type: `Number`

Used on: [Rating](#rating), [Review](#review)

### readingStatus
_Included in version 1.0 of the BookWyrm vocabulary_

A status indicating an [Actor](https://www.w3.org/ns/activitystreams#actor)'s overall reading progress for an [Edition](#edition). This is a controlled field in the BookWyrm user interface. Options are:

* `to-read`
* `reading`
* `read`
* `stopped-reading`

Type: `String`

Used on: [Comment](#comment)

Note: Currently there is a strong relationship between [readingStatus](#readingstatus) and [ShelfItem](#shelfitem), and every BookWyrm user has a [Shelf](#shelf) with an identifier that matches the reading status options listed above. This may change in future.

See also: [ShelfItem](#shelfitem)

### series
_Included in version 1.0 of the BookWyrm vocabulary_

The name of a series of books, or the `@id` of a [Series](#series).

Type: `String` or `@id`

Used on: [Work](#work), [Edition](#edition), [SeriesBook](#seriesbook)

Note: When used on [Work](#work) or [Edition](#edition), `series` is a legacy property retained for backwards-compatibility. The correct way to identify [Series](#series) objects associated with a [Work](#work) is to dereference any associated [SeriesBook](#seriesbook) objects and their [series](#series_1) property.

### seriesBooks
_Included in version 1.0 of the BookWyrm vocabulary_

A list of [SeriesBook](#seriesbook) associated with a book.

Type: `Array` of `@id`s

Used on: [Work](#work)

Note: This property was formerly also used on [Edition](#edition). Some BookWyrm instances may still send [Edition](#edition) objects with the `seriesBook` property.

### seriesNumber
_Included in version 1.0 of the BookWyrm vocabulary_

The name of a series of books, or the `@id` of a [Series](#series).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [SeriesBook](#seriesbook)

Note: When used on [Work](#work) or [Edition](#edition), `seriesNumber` is a legacy property retained for backwards-compatibility. The correct way to identify the series number associated with a [Work](#work) is to dereference any associated [SeriesBook](#seriesbook) objects and their [seriesNumber](#seriesnumber) property.

### sortTitle
_Included in version 1.0 of the BookWyrm vocabulary_

A version of a book title used for the purposes of alphabetical sorting.

Type: `String`

Used on: [Work](#work), [Edition](#edition)

Note: This property does not currently handle multi-lingual sorting.

### subjectPlaces
_Included in version 1.0 of the BookWyrm vocabulary_

A list of geographic locations in which a book is set.

Type: `Array` of `String`s

Used on: [Work](#work), [Edition](#edition)

### subjects
_Included in version 1.0 of the BookWyrm vocabulary_

A list of topics a book is about.

Type: `Array` of `String`s

Used on: [Work](#work), [Edition](#edition)

### subtitle
_Included in version 1.0 of the BookWyrm vocabulary_

A secondary part of the title of a book. Same as [alternativeHeadline](https://schema.org/alternativeHeadline) or [subtitle](https://www.wikidata.org/wiki/Q1135389).

Type: `String`

Used on: [Work](#work), [Edition](#edition)

Note: this does *not* refer to an "alternative" title.

See also: [title](#title)

### title
_Included in version 1.0 of the BookWyrm vocabulary_

The title or name of a book.

Type: `String`

Used on: [Work](#work), [Edition](#edition)

See also: [subtitle](#subtitle)

### viaf
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier from the [The Virtual International Authority File](https://viaf.org)

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingkey), [lccn](#lccn), [librisKey](#libriskey), [oclcNumber](oclcnumber), [openlibraryKey](#openlibrarykey), [wikidata](#wikidata)

### website
_Included in version 1.0 of the BookWyrm vocabulary_

The personal website of an author.

Type: `String` representing a [URL](https://www.w3.org/TR/url)

Used on: [Author](#author)

### wikidata
_Included in version 1.0 of the BookWyrm vocabulary_

Unique identifier for a record from the [wikidata](https://www.wikidata.org).

Type: `String`

Used on: [Work](#work), [Edition](#edition), [Author](#author), [Series](#series)

See also: [bnfId](#bnfid), [finnaKey](#finnakey), [goodreadsKey](#goodreadskey), [GutenbergId](#gutenbergid) [inventaireId](#inventaireid), [isbn10](#isbn10), [isbn13](#isbn13), [isfdb](#isfdb), [isni](#isni), [librarythingKey](#librarythingkey), [lccn](#lccn), [librisKey](#libriskey), [oclcNumber](oclcnumber), [openlibraryKey](#openlibrarykey), [viaf](#viaf)

### wikipediaLink
_Included in version 1.0 of the BookWyrm vocabulary_

The URL of a Wikipedia page.

Type: `String` representing a [URL](https://www.w3.org/TR/url)

Used on: [Author](#author)

Note: As [Author](#author) also has a [wikidata](#wikidata) property which could be used to obtain Wikipedia URLs, this property may be removed in future.

### work
_Included in version 1.0 of the BookWyrm vocabulary_

The parent [Work](#work) of an [Edition](#edition).

Type: `@id`

Used on: [Edition](#edition)
