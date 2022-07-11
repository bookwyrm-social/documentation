- - -
Title: Stilleitfaden Date: 2021-10-20 Order: 4
- - -

## Pull-Anfragen

Also möchten Sie Code zu BookWyrm hinzufügen: Das klingt super! Wenn es ein offenes Problem gibt, das Sie beheben möchten, ist es hilfreich, das Problem zu kommentieren, damit die Arbeit nicht dupliziert wird. Versuchen Sie den Umfang der Pull-Anfragen klein zu halten und konzentrieren Sie sich auf ein einzelnes Thema. Auf diese Weise ist es einfacher zu überprüfen und wenn ein Teil Änderungen braucht, wird er die anderen Teile nicht aufhalten.

Wenn Sie sich nicht sicher sind, wie Sie etwas reparieren können, oder nicht in der Lage sind, es zu erledigen, ist das völlig okay, hinterlassen Sie nur einen Kommentar zu der Pull-Anfrage und wir werden es herausfinden 💖.

Pull-Anfragen müssen alle automatisierten Prüfungen bestehen, bevor sie übernommen werden können - dazu gehören Stil-Prüfungen, globale Linter, eine Sicherheitsprüfung und Unit-Tests.

## Linten

### Global

Wir verwenden [EditorConfig](https://editorconfig.org), um konsistente Einrückungen und Zeilenenden zu erhalten.

### Python

BookWyrm verwendet den [Black](https://github.com/psf/black) Code-Formatierer, um die Python Codebasis konsistent zu gestalten. Alle neuen Pull-Anfragen werden mit GitHub-Aktionen überprüft und Sie können Code-Stilprobleme automatisch beheben, indem Sie `./bw-dev black` ausführen

Code wird auch mit Pylint mittels GitHub-Aktionen überprüft. Pylint-Warnungen müssen bearbeitet werden, bevor Pull-Anfragen übernommen werden, aber es liegt im Ermessen, ob der Vorschlag verwendet werden oder die Warnung unterdrückt werden sollte. Um eine Warnung zu unterdrücken, fügen Sie einen Kommentar am Ende oder über der Zeile mit der Warnung hinzu: `# pylint: disable=Name-der-Warnung`

### Vorlagen (HTML)

Ihre Pull-Anfrage wird auch durch den [curlylint](https://www.curlylint.org)-Linter für Django-Templates überprüft.

### CSS

Wir verwenden [stylelint](https://stylelint.io), um alle CSS-Regeln zu überprüfen. Wie bei Pylint [kannst du styelint](https://stylelint.io/user-guide/ignore-code) für eine bestimmte Regel deaktivieren, aber du benötigst dafür eine gute Rechtfertigung.

### JavaScript

[ESLint](https://eslint.org) überprüft alle von Ihnen vorgenommenen JavaScript-Änderungen. Falls ESLint Ihr funktionierendes JavaScript nicht mag, überprüfen Sie die Linter-Meldung auf das genaue Problem.

## Inklusives Design

Bookwyrm hat zum Ziel, so umfassend und zugänglich wie möglich zu sein.

Überprüfen Sie die [Checkliste für inklusives Web Design](https://github.com/bookwyrm-social/bookwyrm/discussions/1354) bevor Sie Ihre Pull-Anforderung einreichen. Für Barrierefreiheit ist [A11Y-101](https://www.a11y-101.com/development) ebenfalls eine nützliche Quelle. Weitere Informationen darüber, wie Sie Ihre Seitenvorlagen mehrsprachig erstellen, finden Sie im [Abschnitt Übersetzungen](/translations.html).

Einige besondere Dinge, die Bookwyrm-Beitragende für nützlich erachtet haben, sind:

### Formulare

* Verwende nur `input[type="checkbox"]` oder `input[type="radio"]` in `<label>`
* Wenn Sie die Checkboxen und die Radiobuttons nicht innerhalb des `<label>`platzieren, sollte das `<label>` _nach_ dem Element platziert werden, auf das es sich bezieht

### Buttons und Links

* Verwenden Sie ein `<button>` Element für alles, was existiert, um eine JavaScript-Aktion auszulösen (z.B. ein Formular verstecken oder enthüllen) oder eine `POST`-Anfrage senden (z.B. ein Formular übermitteln)
* Verwenden Sie ein `<a>`-Element für alles, was eine `GET`-Anfrage auslöst. Normalerweise sollte ein Ankerelement (`<a>`) nicht als Button (`class="button"`) dargestellt werden, obwohl es einige Ausnahmen gibt, wie z. B. "Abbrechen"-Buttons. Falls Sie Zweifel haben, fragen Sie in Ihrer Pull-Anfrage um Rat
