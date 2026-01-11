---
Title: Documentação
Date: 2025-04-09
Order: 4
---

A documentação que você está lendo agora é mantida pela comunidade BookWyrm. Qualquer um pode contribuir com a documentação.

## Sugerindo melhorias

Você pode relatar **erros**, sugerir **melhorias**, ou solicitar uma **adição** à documentação [criando um issue](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-an-issue) no [repositório da documentação](https://github.com/bookwyrm-social/documentation).

## Como a documentação é feita

A documentação [possui seu próprio repositório GitHub](https://github.com/bookwyrm-social/documentation). A documentação é escrita em Markdown e usamos [Jinja](https://jinja.palletsprojects.com/en/stable) e Python para a converter em HTML. Um plugin Jinja é usado com Crowdin para criar traduções. Todos os arquivos fonte devem ser escritos em Inglês (US).

Todos os arquivos fonte são salvos no diretório `content`. Cada seção tem um diretório dentro dele, com cada página sendo um único arquivo markdown.

## Editando ou criando uma página da de documentação

Para criar ou editar uma nova página, você vai precisar de:

1. clonar [o repositório do GitHub](https://github.com/bookwyrm-social/documentation)
2. fazer suas mudanças no diretório `content` - seja editando uma página markdown existente, ou criando uma nova
3. criar um novo Pull Request
4. responder a quaisquer revisões com as edições necessárias
5. comemorar ao ver suas atualizações instantaneamente publicadas quando seu pull request for aceito e aplicado

Se você nunca usou git ou GitHub antes, isso tudo pode soar um tanto desafiador, mas, vamos simplificar:

### Clonar o repositório

1. Certifique-se de que você tem [uma conta GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).
2. Crie um "clone" ou "fork" do repositório da Documentação:

   - Na **interface web**, clique em "Fork", no topo da [esta página](https://github.com/bookwyrm-social/documentation)
   - Se estiver usando o **GitHub Desktop**, siga [essas instruções](https://docs.github.com/en/desktop/adding-and-cloning-repositories/cloning-and-forking-repositories-from-github-desktop)
   - Se você estiver usando a linha de comando, execute:

   `git clone https://github.com/bookwyrm-social/documentation.git`

### Crie um novo branch e faça suas edições

Para fazer alterações:

1. [Crie um novo branch](https://docs.github.com/en/issues/tracking-your-work-with-issues/using-issues/creating-a-branch-for-an-issue) no seu fork
2. Faça suas edições no diretório `content` e faça um **commit** das suas alterações:
   - [Interface GitHub web](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)
   - [GitHub Desktop](https://docs.github.com/en/desktop/making-changes-in-a-branch/committing-and-reviewing-changes-to-your-project-in-github-desktop)
   - Na linha de comando, salve suas alterações nos arquivos e execute `git commit`

A esse ponto, você deve querer ver como suas mudanças serão mostradas quando publicadas. Veja [Criando documentação localmente](#building-docs-locally) abaixo, para instruções sobre como pré-visualizar suas alterações.

### Criando um pull request

Assim que concluir suas alterações, [faça um pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) ao repositório da documentação.

Seu pull request será revisado e uma das três coisas vai acontecer:

1. Ele será **incorporado** sem alterações
2. Você será solicitado a fazer **alterações**
3. Ele será **rejeitado** e fechado

### Responder a revisões

Se pedirem para fazer alterações, você pode fazê-las localmente e fazer `push` das suas mudanças locais para seu fork/clone no Github. Isso aparecerá automaticamente na sua pull request. Avise o revisor quando terminar suas atualizações para que ele possa fazer outra revisão e, com sorte, aceitar suas mudanças.

Todas as contribuições são bem-vindas. Seria incomum que uma contribuição para a documentação fosse rejeitada imediatamente. Isso só aconteceria se seu pull request apresentasse informações erradas ou que são enganosas, sem chance de melhorias, ou se for declarado como fora de escopo.

### Suas alterações são publicadas

Quando seu pull request é incorporado, [a documentação](https://docs.joinbookwyrm.com/) é atualizada automaticamente. Pode ser necessário recarregar a página ou usar o "modo anônimo" para ver as mudanças em seu navegador.

## Novas páginas

Se estiver adicionando uma nova página, você precisará adicionar alguns metadados, e pode precisar ajustar outras páginas.

No topo de cada arquivo markdown está o "frontmatter" em formato `toml`:

```toml
Título: Documentação
Data: 2025-04-09
Ordem: 4
```

Esse exemplo mostra que a página é chamada "Documentação", deve ser a quarta página dentro de sua seção (neste caso, `Contribuindo`), e que a última atualização foi em 9 de Abril de 2025. Se você adicionar uma página em qualquer lugar que não seja no fim de uma seção, você vai precisar ajustar a ordem das outras páginas que aparecerem abaixo de sua nova página.

Esta seção está contida entre um par de traços triplos (`---`). Em markdown, traços triplos podem ser usados para indicar uma linha horizontal, no entanto, o parser de documentos do BookWyrm pode ficar confuso com isso. Se você precisar de uma linha horizontal, insira-a como código HTML diretamente com linhas vazias, acima e abaixo

```html
<0/>
```

## Criando documentação localmente

Você pode querer ver como suas alterações serão mostradas antes de enviar um pull request. O repositório da documentação inclui um script de desenvolvimento igual ao do repositório de código principal, com o mesmo nome: `bw-dev`. Você pode usar isso para testar como suas alterações serão mostradas.

Diferente do projeto principal, a documentação não é executada em um contêiner Docker. Se você quiser compilar o site da documentação localmente, você vai precisar instalar as dependências. É recomendado [usar um ambiente virtual](https://docs.python.org/3/library/venv.html):

```py
python -m venv /path/to/new/virtual/environment
source <command>/bin/activate
pip install -r requirements.txt
```

Você pode ver alguns comandos disponíveis ao executar `./bw-dev <venv>`. Os que você provavelmente quer, são:

### site:compile

Isso irá compilar arquivos markdown em arquivos html usando o script `generate.py`.

Quando você executar `site:compile`, irá gerar um grande número de arquivos no diretório `site`. Não os marque ou inclua em seu pull request: eles serão gerados novamente, no servidor da documentação, quando seu pull request for incorporado.

### site:serve

Isso roda um servidor local em `http://[::1]:8080/` para que você possa ver como a documentação será apresentada.

### black

Isso irá executar o comando `black` para analisar seus arquivos e evitar erros usando nossas verificações automatizadas. É improvável que você vá precisar disso se estiver apenas atualizando os arquivos fonte da documentação em `content`.

## Notas para mantenedores da documentação

### Traduções

Mantenha traduções alinhadas atualizando regularmente do Crowdin:

1. Traduções são atualizadas no Crowdin
2. Crowdin faz push de novas atualizações para o l10n_main assim que elas estiverem disponíveis
3. No seu fork, faça `pull` tanto do `main`, quanto do `l10n_main` , para eles estarem atualizados em seu repositório local
4. Crie um fork a partir do `main` (p. ex. chamado `update_locales`) e mude pare ele
5. faça merge do diretório `locale` do  `l10n_main` no seu fork: `git checkout l10n_main -- locale`
6. faça ajustes, se necessário
7. faça push do seu branch local para o seu branch remoto e faça um pull request
8. faça pull do PR para `main`
9. Agora há um novo arquivo de referência em en_US
10. Usando as alterações no novo arquivo de referência, as traduções são atualizadas no Crowdin...

Idiomas para o menu dropdown de idiomas, estão listados em `i18n.py`. Geralmente, esperamos que um idioma atinja 70% de cobertura no Crowdin antes de adicioná-lo à lista, para evitar deixar muito conteúdo sem tradução.

### Atualizando quando uma nova versão for lançada

Quando uma nova versão do BookWyrm é lançada, precisamos criar uma versão da documentação.

1. Adicione uma nova branch com o nome igual à nova tag de versão no BookWyrm. p. ex.: `v0.8.0`.

2. Adicione o nome da branch na lista de versões em `generate.py` na branch `main` da documentação

3. Faça checkout das outras versões e faça merge do arquivo de geração atualizado nelas para que todas tenham a nova branch listada: `git checkout main generate.py`. Em seguida, faça commit desta alteração, crie uma PR para fazer merge desta mudança na branch da versão na documentação, e faça merge dela. Isso garantirá que todas as páginas de todas as versões da documentação estarão listadas no menu dropdown.

4. Faça merge na branch main por último - apenas merges na main acionam a ação do GitHub de deploy no servidor da documentação. Se você fizer isso primeiro, as mudanças nas outras branches não terão efeito.