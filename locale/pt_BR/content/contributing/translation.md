- - -
TItle: Traduções Date: 2021-10-20 Order: 2
- - -

## Colaborar com traduções

Você pode participar do projeto de tradução da BookWorm no [translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/).

## Linguagem neutra

As traduções da BookWyrm devem usar marcação de gênero neutra o máximo possível. Isso se aplica mesmo se a língua utiliza o masculino como gênero neutro padrão, ou se possui algo similiar a "ele/ela". Também é importante que as traduções sejam claras, concisas e legíveis em leitores de tela, e às vezes esses objetivos entram em conflito; não há uma solução perfeita para todos os problemas, e a solução depende do idioma.

Como elemento norteador, tente dar mais ênfase ao aspecto inclusivo e ao uso de palavras de gênero neutro do que se fiar à correção formal ou a guias de estilo oficiais. No Inglês, por exemplo, muitos guias de estilo formais exigem que se use um pronome singular "she" ou "he" para se referir a um indivíduo, mas na BookWyrm seria melhor utilizar o pronome singular neutro "they".

Se você não sabe como resolver algum problema de tradução, abra um [tópico de discussão](https://translate.joinbookwyrm.com/project/bookwyrm/discussions) para tratar de problemas mais amplos.

## Fazendo templates traduzíveis

A BookWyrm se utiliza da função de tradução do Django para fazer com que o conteúdo das páginas mude dependendo da língua da interface selecionada pelo usuário. A documentação do Django traz [uma ótima explicação](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code) de como ela funciona, mas aqui temos uma versão mais curta:

* todo texto no template deve incluir as tags de tradução de template
* adicione `{% load i18n %}` no início do arquivo de template pra ativar as traduções
* Se o bloco de texto for literal, você pode usar a tag `{% trans %}`
* Se o bloco de texto tiver variáveis, você deve usar o par de tags `{% blocktrans %}` e `{% endblocktrans %}`. Se você estiver usando espaços em brancos ou quebras de linha, use `trimmed` para removê-los automaticamente quando o arquivo de localização for gerado: `{% blocktrans trimmed %}`

### Exemplos

```html
<p>{% trans "Esta lista está vazia" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Adicionado por <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
