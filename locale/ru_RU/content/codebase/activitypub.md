- - -
Название: Статус сообщения Дата: 2021-04-30 Заказ: 1
- - -

BookWyrm использует протокол [ActivityPub](http://activitypub.rocks/) для отправки и получения активности пользователей между другими узлами BookWyrm и прочими сайтами, использующими ActivityPub, например [Mastodon](https://joinmastodon.org/). Для работы с книгами в BookWyrm добавлен ряд расширенных действий, которые не являются частью стандарта, но понятны другим узлам BookWyrm.

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
- `Delete`: Removes a status
- `Like`: Creates a favorite on the status
- `Announce`: Boosts the status into the actor's timeline
- `Undo`: Reverses a `Like` or `Announce`

### Collections
Книги и списки пользователя представлены [`Упорядоченной Коллекцией`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objects

- `Shelf`: A user's book collection. By default, every user has a `to-read`, `reading`, and `read` shelf which are used to track reading progress.
- `List`: A collection of books that may have items contributed by users other than the one who created the list.

#### Activities

- `Create`: Adds a shelf or list to the database.
- `Delete`: Removes a shelf or list.
- `Добавить`: Добавляет книгу на полку или в список.
- `Убрать`: Убирает книгу с полки или из списка.


## Alternative Serialization
Поскольку BookWyrm использует пользовательские типы объектов (`Обзор`, `Комментарий`, `Цитаты`) которые не поддерживаются ActivityPub, статусы преобразуются в стандартные типы при получении или просмотре сторонними сервисами. `Отзыв` конвертируется в `Статью`, а `Комментарий` и `цитата` преобразуются в `заметку`, со ссылкой на книгу и прикрепленное изображение обложки.
