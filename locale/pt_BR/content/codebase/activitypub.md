- - -
Título: ActivityPub Data: 2021-04-20 Ordem: 1
- - -

BookWyrm usa o protocolo [ActivityPub](http://activitypub.rocks/) para enviar e receber as atividades dos usuários entre instâncias BookWyrm e outros serviços que utilizem o ActivityPub, como o [Mastodon](https://joinmastodon.org/). Para lidar com dados de livros, a BookWyrm tem uma série de tipos estendidos de "Atividade" que não são parte do padrão, mas são legíveis para instâncias BookWyrm.

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

- `Estante`: a coleção de livros de um usuário. Por padrão, todo usuário possui as estantes `"para ler"`, `"lendo"`, e `"lido"`, elas servem para companhar o andamento da leitura.
- `Lista`: uma coleção de livros que podem ter itens submetidos por outros usuários além do criador da lista.

#### Atividades

- `Criar`: salva uma estante ou uma lista no banco de dados.
- `Excluir`: exclui uma estante ou lista.
- `Adicionar`: adiciona um livro a uma estante ou lista.
- `Remover`: exclui um livro de uma estante ou lista.


## Serialização alternativa
Uma vez que a BookWyrm utiliza tipos de objetos especiais (`Resenha`, `Comentário`, `Citação`) que não são compatíveis com o ActivityPub, as publicações são transformadas em objetos do tipo padrão quando são enviadas ou visualizadas por serviços que não a BookWyrm. `Resenhas` são transformadas em `Artigo`, e `Comentários ` e `Citações ` são transformados em `Notas ` com um link para o livro e a imagem de capa no anexo.
