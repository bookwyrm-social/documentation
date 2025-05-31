- - -
Title: 翻訳 Date: 2021-10-20 Order: 2
- - -

## 翻訳に貢献する

BookWyrmの翻訳プロジェクトには、[translate.joinbookwyrm.com](https://translate.joinbookwyrm.com/)から参加できます。

## ジェンダーニュートラルな言葉

BookWyrmの翻訳では、可能な限りジェンダーニュートラルな言葉を使用してください。 このルールは、ある言語が標準的に男性形を中立的なジェンダーとして使用している場合、または「彼/彼女」(he/she) のような表現を使用している場合にも当てはまります。 また、翻訳が明確かつ簡潔で、スクリーンリーダーで読めるものであることも重要です。こうした目標は衝突することもありますが、完全であらゆる場合に当てはまる答えや解決策は言語によって変わるでしょう。

指針として、形式的な正しさや公に認められたスタイルガイドよりも、包括的でジェンダーニュートラルな言葉を重視してください。 例えば、英語では多くの形式的なスタイルガイドが個人について言及する際に単数形の「she」や「he」の代名詞を使うことを要求していますが、BookWyrmではジェンダーニュートラルな単数形「they」を代わりに使用するほうがいいでしょう。

翻訳の問題に取り組むのに最善の方法が分からない場合は、翻訳にコメントしたり[議論の議題](https://translate.joinbookwyrm.com/project/bookwyrm/discussions)を設けて、広範な質問に対応しましょう。

## テンプレートを翻訳可能にする

BookWyrmは、Djangoの翻訳機能を活用して、ユーザーが選択した表示言語に応じてページコンテンツを変更できます。 Djangoのドキュメントでは、動作の仕組みについて[役に立つ説明](https://docs.djangoproject.com/en/3.2/topics/i18n/translation/#internationalization-in-template-code)が提供されていますが、ここでは短い要約をしておきます。

* すべてのテンプレートテキストは翻訳テンプレートタグがを含める必要がある。
* 翻訳を有効にするには、`{% load i18n %}`をテンプレートの先頭に追加する。
* テキストブロックがリテラルテキストの場合、テンプレートタグ`{% trans %}`を使用できる。
* テキストブロックに変数が含まれる場合、テンプレートタグ`{% blocktrans %}`と`{% endblocktrans %}`のペアを使う必要がある。 空白または改行を含む場合は、ロケールファイルが生成されるときにそれらを自動的に削除するために`trimmed`を使用します。例: `{% blocktrans trimmed %}`

### 例

```html
<p>{% trans "This list is currently empty" %}</p>

<p>
    {% blocktrans trimmed with username=item.user.display_name user_path=item.user.local_path %}
    Added by <a href="{{ user_path }}">{{ username }}</a>
    {% endblocktrans %}
</p>
```
