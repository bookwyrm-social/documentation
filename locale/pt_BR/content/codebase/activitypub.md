Título: ActivityPub Data: 20/04/2021 Ordem: 1

BookWyrm usa o protocolo [ActivityPub](http://activitypub.rocks/) para enviar e receber as atividades dos usuários entre instâncias BookWyrm e outros serviços que utilizem o ActivityPub, como o [Mastodon](https://joinmastodon.org/). Para lidar com dados de livros, a BookWyrm tem uma série de tipos estendidos de Atividade (Activity) que não são parte do padrão, mas são legíveis para instâncias BookWyrm.

## Atividades e Objetos

### Usuários e relações
As interações de relação entre usuários seguem a especificação padrão do ActivityPub.

- `Seguir (Follow)`: pedir para receber as publicações de um usuário e ver suas publicações privadas, apenas para seguidores
- `Aceitar (Accept)`: aprova um pedido para `Seguir` e finaliza a relação
- `Rejeitar (Reject)`: recusa um pedido para `Seguir`
- `Bloquear (Block)`: impede que usuários vejam as publicações uns dos outros, e impede que o usuário bloqueado visualize o perfil do agente
- `Atualizar (Update)`: atualize o perfil do usuário e suas configurações
- `Excluir (Delete)`: desativa um usuário
- `Desfazer (Undo)`: reverte um pedido de `Seguir` ou `Bloquear`

### Publicações
#### Tipos de objetos

- `Nota (Note)`: em serviços como o Mastodon, a `Nota`s é o tipo primário de publicação. Elas contêm o corpo da mensagem, os anexos, podem mencionar usuários e também serem respostas a publicações de qualquer tipo. Na BookWyrm, uma `Nota`s só pode ser criada como uma mensagem direta ou como respostas a outras publicações.
- `Resenha (Review)`: Uma resenha é uma publicação em resposta a um livro (indicada pelo campo `inReplyToBook`) que tem um título, corpo e uma avaliação entre 0 (não avaliado) e 5.
- `Comentário (Comment)`: Um comentário sobre um livro menciona um livro e tem o corpo da mensagem.
- `Citação (Quotation)`: Uma citação tem o corpo da mensagem, um excerto do livro e menciona um livro.


#### Atividades (Activities)

- `Criar (Create)`: salva uma nova publicação no banco de dados.

   **Lembrete**: A BookWyrm só aceita atividades `Criar (Create)` se elas forem:

   - Mensagens diretas (ou seja, `Nota`s com o nível de privacidade `direto (direct)`, que menciona um usuário local),
   - Relacionadas a um livro (de um tipo de publicação que possua o campo `inReplyToBook`),
   - Respostas a publicações já salvas no banco de dados
- `Excluir (Delete)`: apaga uma publicação
- `Curtir (Like)`: Adiciona um favorito ao status
- `Compartilhar (Announce)`: compartilha a publicação na linha do tempo do agente
- `Desfazer (Undo)`: reverte um `Curtir (Like)` ou um `Compartilhar (Announce)`

### Coleções
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
