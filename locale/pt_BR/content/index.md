- - -
Título: Bem-vindo Data: 2021-04-13
- - -

A BookWyrm é uma rede social para acompanhar sua leitura, falar sobre livros, escrever resenhas e achar outro livro para ler em seguida. A federação permite que usuários da BookWyrm participem de comunidades pequenas e confiáveis que podem se conectar entre si, e também a outros serviços ActivityPub, como o Mastodon e o Pleroma.

## Funcionalidades
The features are growing every month, and there is plenty of room for suggestions and ideas. Open an [issue](https://github.com/bookwyrm-social/bookwyrm/issues) to get the conversation going, or [find a good first issue](https://github.com/bookwyrm-social/bookwyrm/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22) to make your first contribution!

- Fazendo publicações sobre livros
    - Escreva resenhas com ou sem nota que aparecerão na página do livro
    - Escreva outros tipos de publicações sobre livros, como:
        - Comentários sobre um livro
        - Citações ou resumos
    - Respostas a publicações
    - Veja as resenhas sobre um livro de várias instâncias BookWyrm conectadas
    - Diferencie resenhas locais e federadas e as notas na sua página de atividades
- Acompanhe sua leitura
    - Shelve books on default "to-read," "currently reading," "stopped reading," and "read" shelves
    - Crie prateleiras personalizadas
    - Store started/stopped/finished reading dates, as well as progress updates along the way
    - Envia aos seguidores as atividades de leitura (opcionalmente, e com privacidade de controle granular)
    - Crie listas de livros que podem ser abertas às submissões de outros usuários, aberta à submissão mas com processo de aprovação ou apenas organizada por quem a criou
    - Create groups with other BookWyrm users and collaborate with group-owned lists
- Federação com o ActivityPub
    - Envie e receba publicações de usuários e suas atividades
    - Compartilhe informações sobre livros entre instâncias para criar um banco de dados de metadados distribuído
    - Identifique livros compartilhados entre instâncias e agregue conteúdos relacionados
    - Siga e interaja com usuários entre diferentes instâncias BookWyrm
    - Inter-operate with non-BookWyrm ActivityPub services like Mastodon and GoToSocial
- Controle de privacidade granular
    - Níveis de privacidade privado, só para seguidores e público para publicações, estantes e listas
    - Opção para que usuários aprovem seguidores manualmente
    - Permite bloquear e sinalizar para a moderação

## Using this documentation

### Navigation

Use the menu on the left-hand side to find the section you are looking for.

* _Using BookWyrm_ explains how to use BookWyrm as an ordinary user
* You will need the _Running BookWyrm_ section if you want to administer a BookWyrm instance (server)
* _Contributing_ explains how you can get involved in the project and contribute in various ways (you don't have to know how to code)
* _Codebase_ provides more information about key aspects of BookWyrm's code
* Consult the _Reference Guides_ if you need to know what a particular environment variable or `bw-dev` command does

You can also change the language and version.

### Translations

Documentation is written in English (US) by default. When we have at least 70% coverage for a language in [BookWyrm's translation project](https://translate.joinbookwyrm.com/) it will be added to the list of available languages. If you notice some parts of a translated version are in English, you can [help us to translate them](https://translate.joinbookwyrm.com/). This can happen as we make changes and additions to the documentation.

### Versioning

Since version `0.7.5`, each BookWyrm version has a matching version in the documentation. This allows you to check the documentation as it applies to your specific BookWyrm version. If you are using a patch version with no matching documentation (e.g. `0.8.1`), this is a bugfix-only version and you should use the documentation for the preceding version (e.g. `0.8.0`).

### Page table of contents

There is also a drop-down menu on each page that displays a table of contents. You can use this to navigate directly to a particular section heading. This can be useful for very long pages like the Reference Guides. The table of contents menu does not appear on the homepage.

### Smaller screens

On smaller screens the side menu is hidden. Use the "hamburger menu" at the top right of the screen to make it visible.