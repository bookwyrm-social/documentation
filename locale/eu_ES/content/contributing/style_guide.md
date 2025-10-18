- - -
Izenburua: Estiloen gida Eguna: 2021-10-20 Ordena: 4
- - -

## Pull eskariak

BookWyrm-en kodean parte-hartzeko asmoa duzu, bikaina da! Arazo ireki bat konpondu nahi baduzu, hobe da iruzkin bat uztea elkarrizketan, lana bikoiztu ez dadin. Saiatu pull eskarien gaiari mugatzen, eta kontzentratu zure arreta gai bakar batean. Horrela, irakurgarriagoa izaten da eta zati batek aldaketak behar baditu, ez ditu beste aldeak atzeratzen.

Arazo bat nola konpondu ez badakizu edo konpontzeko prest ez bazaude, lasai egon. Nahikoa da pull eskaeran iruzkin bat egitea, eta txanda hartuko dugu 💖.

Pull eskaerek egiaztapen automatizatu guztiak egin behar dituzte bat egin baino lehen, hala nola estilo-egiaztapenak, Linters globalak, segurtasun-kontrola eta proba unitarioak.

## Linting-a

### Orokorra

[EditorConfig](https://editorconfig.org) erabiltzen dugu indentazio eta lerro koherenteak mantentzeko.

### Python

BookWyrm-ek [Black](https://github.com/psf/black) kodearen formatzailea erabiltzen du Python kodearen oinarriaren koherentzia mantentzeko. Pull eskaera berri guztiak GitHuben ekintzekin egiaztatzen dira, eta automatikoki konpon daitezke kode-estiloko arazoak `./bw-dev black` exekutatuz

Kodea Pylint-ekin ere egiaztatzen da GitHuben ekintza baten bidez. Pylint-en ohartarazpenei ekin behar zaie pull eskaerak bateratu baino lehen, baina zure iritziaren araberakoa da iradokizuna erabili edo oharra ezabatu behar den. Ohar bat ezabatzeko, gehitu iruzkin bat amaieran edo oharrak aipatzen diren aitzineko lerroan: `# pylint: disable=warning-name`

### Txantiloiak (HTML)

Zure pull eskaria, [curlylint](https://www.curlylint.org) linter-rak egiaztatuko du Django txantiloietarako.

### CSS

[Stylelint](https://stylelint.io) erabiltzen dugu CSS arau guztiak egiaztatzeko. Pylint-ekin bezala, [stylelint desaktiba dezakezu](https://stylelint.io/user-guide/ignore-code) arau jakin baterako, baina horretarako justifikazio ona beharko duzu.

### JavaScript

[ESLint](https://eslint.org)ek egiaztatzen ditu JavaScript-ean egin aldaketa guztiak. ESLint-ek zure JavaScript kodea (funtzionatzen badu ere) gustuko ez badu, egiaztatu linter mezua arazo zehatz horretarako.

## Diseinu inklusiboa

Bookwyrm-ek ahalik eta inklusiboena eta eskuragarriena izan nahi du.

Kodearekin ekarpenak egiten dituzunean, egiaztatu [Inclusive Web Design Checklist](https://github.com/bookwyrm-social/bookwyrm/discussions/1354), pull eskari bat proposatu aurretik. Irisgarritasunari buruzko aholkuetarako, [A11Y-101](https://www.a11y-101.com/development) ere baliabide baliagarria da. Zure orrialde txantiloiak eleaniztunak izateko moduari buruzko informazioa lortzeko, kontsultatu [Itzulpenak atala](/translations.html).

Hona hemen Bookwyrm-eko kolaboratzaileek gogoan hartu behar dituzten elementu batzuk:

### Formularioak

* Soilik erabili `input[type="checkbox"]` edo `input[type="radio"]` honen barnean: `<label>`
* Kontrol-kaxarik eta irrati-botoirik ez baduzu ezartzen `<label>` barnean, `<label>`a dagokion elementuaren _ondoren_ jarri behar da

### Botoiak eta Estekak

* Erabili `<button>` elementu bat JavaScript ekintza bat aktibatzeko helburua duen orotarako (adibidez: formulario bat ezkutatu edo erakusteko) edo `POST` eskaria bat bidaltzeko (adibidez, formulario bat aurkezteko)
* Erabili `<a>` elementu bat `GET` eskaria eragiten duen gauza orotarako. Usaian, esteka batek (`<a>`) ez du botoi (`class="button"`) baten itxura izan behar, nahiz eta salbuespen batzuk dauden "Ezeztatu" botoiak bezala. Zalantzarik izanez gero, aholku bat eska ezazu zure pull eskarian
