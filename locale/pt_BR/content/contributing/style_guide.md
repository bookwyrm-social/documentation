- - -
Título: Guia de Estilo Data: 2021-10-20 Ordem: 4
- - -

## Pull requests

Então você quer contribuir com a BookWyrm? Show! Se houver algum problema aberto no repositório que você quer consertar, deixer um comentário para que o trabalho não seja feito mais de uma vez. Tente manter o escopo dos pull requests pequenos e focados em uma única questão. Assim é mais fácil revisar, e se alguma parte precisar ser alterada, isso não atrapalhará as outras partes.

Se você não sabe exatamente como consertar alguma coisa, ou se não consegue fazê-lo, está tudo bem! Só deixe um comentário no pull request e vamos descobrir 💖.

Os pull requests passam por todas as verificações automáticas antes de serem mesclados - isso inclui verificações de estilos, linters globais, uma verificação de segurança e testes unitários.

## Linting

### Global

Usamos o [EditorConfig](https://editorconfig.org) para manter uma identação e fins de linha consistentes.

### Python

A BookWyrm usa o formatador de código [Black](https://github.com/psf/black) pra manter o código Python com um estilo consistente. Todas as novas pull requests são verificadas com ações do GitHub, e você pode corrigir problemas nos códigos de estilo executando `./bw-dev black`

Os códigos também são chegados pelo Pylint usando GitHub Actions. Os avisos do Pylint devem ser analisados antes da pull request ser mesclada, mas é uma questão de escolha se a sugestão deve ser acatada ou o aviso, suprimido. Para suprimir o aviso, coloque um comentário no fim ou na linha acima do aviso: `# pylint: disable=warning-name`

### Templates (HTML)

Suas pull requests também vão ser verificadas pelo linter [curlylint](https://www.curlylint.org) dos templates do Django.

### CSS

Usamos o [stylelint](https://stylelint.io) para conferir todas as regras de CSS. Como no Pylint, [você pode disativar o stylelint](https://stylelint.io/user-guide/ignore-code) para alguma regra particular, mas você vai precisar de uma boa justificativa para fazê-lo.

### JavaScript

[ESLint](https://eslint.org) verifica todas as modificações em JavaScript que você fizer. Se o ESLint não gostar do seu JavaScript, dê uma olhada na mensagem do linter para ver qual é o problema.

## Design inclusivo

A BookWyrm quer ser o mais inclusiva e acessível possível.

Quando for contribuir com código, dê uma olhada na [Check list de web design inclusivo](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) antes de enviar o pull request. Para sugestões de acessibilidade, o [A11Y-101](https://www.a11y-101.com/development) também é uma fonte útil. Para saber como fazer seus templates serem compatíveis com vários idiomas, veja a [seção Traduções](/translations.html).

Algumas coisas que colaboradores da BookWyrm acharam boas de se lembrar:

### Formulários

* Só use `input[type="checkbox"]` ou `input[type="radio"]` dentro `<label>`
* Se você não colocar os botões de checkbox e radio dentro do `<label>`, o `<label>` deve ser colocado _depois_ do elemento ao que ele está relacionado

### Botões e links

* Use um elemento `<button>` para tudo que sirva para disparar uma ação de JavaScript (ex: esconder ou mostrar um formulário) ou enviar uma solicitação `POST` (ex: enviar um formulário)
* Use um elemento `<a>` para tudo que faça uma solicitação `GET`. Normalmente um elemento de âncora (`<a>`) não costuma ser estilizado como um botão (`class="button"`), mas há algumas exceções, como os botões de "Cancelar". Se tiver alguma dúvida, peça sugestões no seu pull request
