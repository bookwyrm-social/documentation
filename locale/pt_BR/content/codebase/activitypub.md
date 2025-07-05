- - -
Title: ActivityPub Date: 2025-04-21 Order: 1
- - -

BookWyrm usa o protocolo [ActivityPub](http://activitypub.rocks/) para enviar e receber as atividades dos usuários entre instâncias BookWyrm e outros serviços que utilizem o ActivityPub, como o [Mastodon](https://joinmastodon.org/). Para lidar com dados de livros, a BookWyrm tem uma série de tipos estendidos de "Atividade" que não são parte do padrão, mas são legíveis para instâncias BookWyrm.

To view the ActivityPub data for a BookWyrm entity (user, book, list, etc) you can usually add `.json` to the end of the URL. e.g. `https://www.example.com/user/sam.json` and see the JSON in your web browser or via an http request (e.g. using `curl`).

## Atividades e Objetos

### Usuários e relações
As interações de relação entre usuários seguem a especificação padrão do ActivityPub.

- `Seguir`: pedir para receber as publicações de um usuário e ver suas publicações privadas, apenas para seguidores
- `Aceitar`: aprova um pedido para `Seguir` e finaliza a relação
- `Rejeitar`: recusa um pedido para `Seguir`
- `Bloquear`: impede que usuários vejam as publicações uns dos outros, e impede que o usuário bloqueado visualize o perfil do agente
- `Atualizar`: atualize o perfil do usuário e suas configurações
- `Excluir`: desativa um usuário
- `Desfazer`: reverte um pedido de `Seguir` ou `Bloquear`
- `Move`: communicate that a user has changed their ID and has moved to a new server. Most ActivityPub software will "follow" the user to the new identity. BookWyrm sends a notification to followers and requires them to confirm they want to follow the user to their new identity.

### Publicações
#### Tipos de objetos

- `Nota`: em serviços como o Mastodon, a `Nota`s é o tipo primário de publicação. Elas contêm o corpo da mensagem, os anexos, podem mencionar usuários e também serem respostas a publicações de qualquer tipo. Na BookWyrm, uma `Nota`s só pode ser criada como uma mensagem direta ou como respostas a outras publicações.
- `Resenha`: É uma publicação em respota a um livro (indicado pelo campo `inReplyToBook`), o qual tem um título, corpo e uma avaliação numérica entre 0 (não avaliado) e 5.
- `Comentário`: Um comentário sobre um livro menciona um livro e tem o corpo da mensagem.
- `Citação`: Tem um corpo de mensagem, um excerto do livro e menciona um livro.

#### Atividades

- `Criar`: salva uma nova publicação no banco de dados.

    **Lembrete**: A BookWyrm só aceita atividades `Criar` se elas forem:

    - Mensagens diretas (ou seja, `Notas` com o nível de privacidade `direto`, que menciona um usuário local),
    - Relacionadas a um livro (de um tipo de publicação que possua o campo `inReplyToBook`),
    - Respostas a publicações já salvas no banco de dados

- `Excluir`: apaga uma publicação
- `Curtir`: Adiciona um favorito ao status
- `Compartilhar`: compartilha a publicação na linha do tempo do agente
- `Desfazer`: reverte um `Curtir` ou um `Compartilhar`

### Coleções
Os livros dos usuários e suas listas são representadas com [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objetos

- `Estante`: a coleção de livros de um usuário. By default, every user has a `to-read`, `reading`, `stop-reading` and `read` shelf which are used to track reading progress.
- `Lista`: uma coleção de livros que podem ter itens submetidos por outros usuários além do criador da lista.

#### Atividades

- `Criar`: salva uma estante ou uma lista no banco de dados.
- `Excluir`: exclui uma estante ou lista.
- `Adicionar`: adiciona um livro a uma estante ou lista.
- `Remover`: exclui um livro de uma estante ou lista.

## Serialização alternativa
Uma vez que a BookWyrm utiliza tipos de objetos especiais (`Resenha`, `Comentário`, `Citação`) que não são compatíveis com o ActivityPub, as publicações são transformadas em objetos do tipo padrão quando são enviadas ou visualizadas por serviços que não a BookWyrm. `Resenhas` são transformadas em `Artigo`, e `Comentários ` e `Citações ` são transformados em `Notas ` com um link para o livro e a imagem de capa no anexo.

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
