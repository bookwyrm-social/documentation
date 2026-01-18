- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm использует протокол [ActivityPub](http://activitypub.rocks/) для отправки и получения активности пользователей между другими узлами BookWyrm и прочими сайтами, использующими ActivityPub, например [Mastodon](https://joinmastodon.org/). Для работы с книгами в BookWyrm добавлен ряд расширенных действий, которые не являются частью стандарта, но понятны другим узлам BookWyrm.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Действия и объекты

### Пользователи и отношения
Взаимодействие между пользователями соответствует стандартной спецификации ActivityPub.

- `Подписк`а: запрос на получение обновлений пользователя и просмотра статусов, доступных только для подписчиков
- `Принять`: одобряет `подписк`у и устанавливает связь
- `Отклонить`: не разрешает `подписк`у
- `Блок`ировка: не позволяет пользователям видеть статусы друг друга, а также заблокированный не видит профиль заблокировавшего
- `Обновить`: обновляем настройки и профиль пользователя
- `Удалить`: удаляет пользователя
- `Отмена`: отменяет `Подписк`у или `Блок`ировку
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Статусы
#### Типы объектов

- `Note`: On services like Mastodon, `Note`s are the primary type of status. They contain a message body, attachments, can mention users, and be replies to statuses of any type. Within BookWyrm, `Note`s can only be created as direct messages or as replies to other statuses.
- `Review`: A review is a status in response to a book (indicated by the `inReplyToBook` field), which has a title, body, and numerical rating between 0 (not rated) and 5.
- `Comment`: A comment on a book mentions a book and has a message body.
- `Quotation`: A quote has a message body, an excerpt from a book, and mentions a book.

#### Действия

- `Создать`: сохраняет новый статус в базе данных.

    **Note**: BookWyrm only accepts `Create` activities if they are:

    - Direct messages (i.e., `Note`s with the privacy level `direct`, which mention a local user),
    - Related to a book (of a custom status type that includes the field `inReplyToBook`),
    - Replies to existing statuses saved in the database

- `Удалить`: Удаляет статус
- `Like`: Creates a favorite on the status
- `Announce`: Boosts the status into the actor's timeline
- `Undo`: Reverses a `Like` or `Announce`

### Collections
Книги и списки пользователя представлены [`Упорядоченной Коллекцией`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objects

- `Shelf`: A user's book collection. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Activities

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Добавить`: Добавляет книгу на полку или в список.
- `Убрать`: Убирает книгу с полки или из списка.

## Alternative Serialization
Поскольку BookWyrm использует пользовательские типы объектов (`Обзор`, `Комментарий`, `Цитаты`) которые не поддерживаются ActivityPub, статусы преобразуются в стандартные типы при получении или просмотре сторонними сервисами. `Отзыв` конвертируется в `Статью`, а `Комментарий` и `цитата` преобразуются в `заметку`, со ссылкой на книгу и прикрепленное изображение обложки.

This may change in future in favor of the more ActivityPub-compliant [extended Object types](https://www.w3.org/TR/activitystreams-core/#fig-following-is-an-example-object-that-uses-the-id-and-type-properties-to-express-the-global-identifier-and-object-type) listed alongside core ActivityPub types.

## Making ActivityPub-aware models

The way BookWyrm sends and receives ActivityPub objects can be confusing for developers who are new to BookWyrm. It is mostly controlled by:

* Functions and [data classes](https://docs.python.org/3/library/dataclasses.html) outlined in the [activitypub](https://github.com/bookwyrm-social/bookwyrm/tree/main/bookwyrm/activitypub) directory
* The [ActivitypubMixin](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L40) and its children for models that are serializable for ActivityPub requests

### Serializing data to and from ActivityPub JSON

BookWyrm needs to know how to _serialize_ the data from the model into an ActivityPub JSON-LD object.

The `/activitypub/base_activity.py` file provides the core functions that turn ActivityPub JSON-LD strings into usable Django model objects, and vice-versa. We do this by creating a data class in `bookwyrm/activitypub`, and defining how the model should be serialized by providing an `activity_serializer` value in the model, which points to the relevant data class. From `ActivityObject` we inherit `id` and `type`, and two _class methods_:

**`to_model`**

This method takes an ActivityPub JSON string and tries to turn it into a BookWyrm model object, finding an existing object wherever possible. This is how we process **incoming** ActivityPub objects.

**`serialize`**

This method takes a BookWyrm model object, and turns it into a valid ActivityPub JSON string using the dataclass definitions. This is how we process **outgoing** ActivityPub objects.

### Example - Users

A BookWyrm user [is defined in `models/user.py`](https://github.com/bookwyrm-social/bookwyrm/blob/main/bookwyrm/models/user.py):

```py
class User(OrderedCollectionPageMixin, AbstractUser):
    """a user who wants to read books"""
```
Notice that we are inheriting from ("subclassing") `OrderedCollectionPageMixin`. This in turn inherits from `ObjectMixin`, which inherits from `ActivitypubMixin`. This may seem convoluted, but this inheritence chain allows us to avoid duplicating code as our ActivityPub objects become more specific. `AbstractUser` is [a Django model intended to be subclassed](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#specifying-custom-user-model), giving us things like hashed password logins and permission levels "out of the box".

Because `User` inherits from [`ObjectMixin`](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L213), when we `save()` a `User` object we will send a `Create` activity (if this is the first time the user was saved) or an `Update` activity (if we're just saving a change – e.g. to the user description or avatar). Any other model you add to BookWyrm will have the same capability if it inherits from `ObjectMixin`.

For BookWyrm users, the `activity_serializer` is defined in the `User` model:

```py
activity_serializer = activitypub.Person
```

The data class definition for `activitypub.Person` is at `/activitypub/person.py`:

```py
@dataclass(init=False)
class Person(ActivityObject):
    """actor activitypub json"""

    preferredUsername: str
    inbox: str
    publicKey: PublicKey
    followers: str = None
    following: str = None
    outbox: str = None
    endpoints: Dict = None
    name: str = None
    summary: str = None
    icon: Image = None
    bookwyrmUser: bool = False
    manuallyApprovesFollowers: str = False
    discoverable: str = False
    hideFollows: str = False
    movedTo: str = None
    alsoKnownAs: dict[str] = None
    type: str = "Person"
```

You might notice that some of these fields are not a perfect match to the fields in the `User` model. If you have a field name in your model that needs to be called something different in the ActivityPub object (e.g. to comply with Python naming conventions in the model but JSON naming conventions in JSON string), you can define an `activitypub_field` in the model field definition:

```py
followers_url = fields.CharField(max_length=255, activitypub_field="followers")
```
