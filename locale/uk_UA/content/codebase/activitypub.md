- - -
Title: ActivityPub Date: 2021-04-20 Order: 1
- - -

BookWyrm використовує [ActivityPub](http://activitypub.rocks/) протокол для надсилання та отримання діяльності користувача між іншими екземплярами BookWyrm та іншими службами, що реалізують ActivityPub, як [Mastodon](https://joinmastodon.org/). Для обробки даних книги, BookWyrm має декілька розширених типів діяльності, які не є частиною стандарту, але вони зрозумілі для інших екземплярів BookWyrm.

## Діяльність та об'єкти

### Користувачі та зв'язки
Користувацькі взаємодії слідують стандартній специфікації ActivityPub.

- `Follow`: запит на отримання статусів від користувача і перегляд їхніх статусів, що мають followers-only конфіденційність
- `Accept`: затверджує `Follow` запит і завершує формування зв'язку
- `Reject`: відмовляє `Follow` запит
- `Block`: не дає користувачам бачити статуси одне одного та не дозволяє заблокованому користувачу переглядати профіль персони
- `Update`: оновлює профіль користувача та налаштування
- `Delete`: деактивує користувача
- `Undo`: скасовує `Follow` або `Block`

### Статуси
#### Типи об'єктів

- `Note`: На службах, таких як Mastodon, `Note` - це основний тип статусу. Вони містять тіло повідомлення, вкладення, можуть згадувати користувачів та відповідати на статуси будь-якого типу. У додатку BookWyrm `Note` можна створювати лише як прямі повідомлення або відповідати на інші статуси.
- `Review`: A review is a status in response to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Comment`: коментар до книги, який згадує книгу і має тіло повідомлення.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book.


#### Activities (дії)

- `Create`: збереже новий статус в базі даних.

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

#### Activities (дії)

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Add`: Adds a book to a shelf or list.
- `Remove`: Removes a book from a shelf or list.


## Альтернативна серіалізація
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
