- - -
Title: Style Guide Date: 2021-10-20 Order: 3
- - -

## Pull eskariak

BookWyrm-en kodean parte-hartzeko asmoa duzu, bikaina da! Arazo ireki bat konpondu nahi baduzu, hobe da iruzkin bat uztea elkarrizketan, lana bikoiztu ez dadin. Saiatu pull eskarien gaiari mugatzen, eta kontzentratu zure arreta gai bakar batean. Horrela, irakurgarriagoa izaten da eta zati batek aldaketak behar baditu, ez ditu beste aldeak atzeratzen.

Arazo bat nola konpondu ez badakizu edo konpontzeko prest ez bazaude, lasai egon. Nahikoa da pull eskaeran iruzkin bat egitea, eta txanda hartuko dugu 💖.

Pull eskaerek egiaztapen automatizatu guztiak egin behar dituzte bat egin baino lehen, hala nola estilo-egiaztapenak, Linters globalak, segurtasun-kontrola eta proba unitarioak.

There are several `./bw-dev` commands you may find helpful for linting and testing prior to pushing your pull request. See [Command Line Tool](cli.html) for all the options available.

## Linting-a

### Orokorra

[EditorConfig](https://editorconfig.org) erabiltzen dugu indentazio eta lerro koherenteak mantentzeko.

### Python

#### Formatting and linting

BookWyrm uses [ruff](https://docs.astral.sh/ruff) for both code linting (checking for errors) and formatting (ensuring code style is consistent). All new pull requests are checked with GitHub actions, and you can automatically fix code style problems by running `./bw-dev ruff`. For linting errors, you can try `./bw-dev ruff-fix` to automatically fix errors, though this may not always be possible.

Ruff linting warnings must be addressed before pull requests are merged, but it's a judgement call if the suggestion should be used, or the warning suppressed. See [the Ruff projects's documentation on suppressing warnings](https://docs.astral.sh/ruff/linter/#comments) using code comments.

The BookWyrm project previously used `Black` for formatting and `Pylint` for linting. You may notice artefacts such as pylint suppression comments in older code. We are still refining our linting rules so if something seems confusing or not quite right, don't hesitate to ask for advice.

#### Type checking

We are gradually rolling out [static type checking](https://en.wikipedia.org/wiki/Type_system) across the BookWyrm code base. This is a long term project. Whilst it is not compulsory to formally define types in new code, it is strongly recommended. This will help to avoid some more subtle bugs that may not be identified in tests.

We currently use [mypy](https://www.mypy-lang.org) as our static type checker. Find out more about how to use mypy at [the `mypy` project documentation](https://mypy.readthedocs.io/en/stable/).

### Txantiloiak (HTML)

Zure pull eskaria, [curlylint](https://www.curlylint.org) linter-rak egiaztatuko du Django txantiloietarako.

### CSS

[Stylelint](https://stylelint.io) erabiltzen dugu CSS arau guztiak egiaztatzeko. Pylint-ekin bezala, [stylelint desaktiba dezakezu](https://stylelint.io/user-guide/ignore-code) arau jakin baterako, baina horretarako justifikazio ona beharko duzu.

### JavaScript

[ESLint](https://eslint.org)ek egiaztatzen ditu JavaScript-ean egin aldaketa guztiak. ESLint-ek zure JavaScript kodea (funtzionatzen badu ere) gustuko ez badu, egiaztatu linter mezua arazo zehatz horretarako.

## Diseinu inklusiboa

Bookwyrm-ek ahalik eta inklusiboena eta eskuragarriena izan nahi du.

Kodearekin ekarpenak egiten dituzunean, egiaztatu [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354), pull eskari bat proposatu aurretik. Irisgarritasunari buruzko aholkuetarako, [A11Y-101](https://www.a11y-101.com/development) ere baliabide baliagarria da. For information on how to make your page templates multi-lingual, see the [Translations section](/translation.html).

Hona hemen Bookwyrm-eko kolaboratzaileek gogoan hartu behar dituzten elementu batzuk:

### Formularioak

* Soilik erabili `input[type="checkbox"]` edo `input[type="radio"]` honen barnean: `<label>`
* Kontrol-kaxarik eta irrati-botoirik ez baduzu ezartzen `<label>` barnean, `<label>`a dagokion elementuaren _ondoren_ jarri behar da

### Botoiak eta Estekak

* Erabili `<button>` elementu bat JavaScript ekintza bat aktibatzeko helburua duen orotarako (adibidez: formulario bat ezkutatu edo erakusteko) edo `POST` eskaria bat bidaltzeko (adibidez, formulario bat aurkezteko)
* Erabili `<a>` elementu bat `GET` eskaria eragiten duen gauza orotarako. Usaian, esteka batek (`<a>`) ez du botoi (`class="button"`) baten itxura izan behar, nahiz eta salbuespen batzuk dauden "Ezeztatu" botoiak bezala. Zalantzarik izanez gero, aholku bat eska ezazu zure pull eskarian

#### Translations

BookWyrm is an international project and aims to be inclusive of as many languages as possible. All user-facing messages and templates should follow the advice on [translations and gendered language](translation.html).