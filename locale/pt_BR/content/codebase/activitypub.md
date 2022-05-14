> | Title: ActivityPub | Date: 2021-04-20 | Order: 1

BookWyrm uses the [ActivityPub](http://activitypub.rocks/) protocol to send and receive user activity between other BookWyrm instances and other services that implement ActivityPub, like [Mastodon](https://joinmastodon.org/). To handle book data, BookWyrm has a handful of extended Activity types which are not part of the standard, but are legible to other BookWyrm instances.

## Atividades e Objetos

### Usuários e relações
User relationship interactions follow the standard ActivityPub spec.

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

#### Objetos

- `Estante (Shelf)`: a coleção de livros de um usuário. Por padrão, todo usuário possui as estantes `to-read (para-ler)`, `reading (lendo)`, e `read (lido)`, elas servem para companhar o andamento da leitura.
- `Lista (List)`: uma coleção de livros que podem ter itens submetidos por outros usuários além do criador da lista.

#### Atividades (Activities)

- `Criar (Create)`: salva uma estante ou uma lista no banco de dados.
- `Excluir (Delete)`: exclui uma estante ou lista.
- `Adicionar (Add)`: adiciona um livro a uma estante ou lista.
- `Remover (Remove)`: exclui um livro de uma estante ou lista.


## Serialização alternativa
Because BookWyrm uses custom object types (`Review`, `Comment`, `Quotation`) that aren't supported by ActivityPub, statuses are transformed into standard types when sent to or viewed by non-BookWyrm services. `Review`s are converted into `Article`s, and `Comment`s and `Quotation`s are converted into `Note`s, with a link to the book and the cover image attached.
