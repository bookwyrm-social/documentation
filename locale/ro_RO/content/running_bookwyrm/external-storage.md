În mod implicit, BookWyrm folosește stocarea locală pentru modelele statice (favicon, avatarul de bază etc.) și media (avatarurile utilizatorilor, coperțile cărților etc.), dar puteți folosi un serviciu de stocare extern pentru a deservi aceste fișiere. BookWyrm folosește `django-storages` pentru a manipula stocarea externă, precum servicii S3 compatibile, Apache Libcloud sau SFTP.

## Servicii S3 compatibile

### Configurare

Creați o „găleată” la serviciul dvs. S3 compatibil împreună cu ID-ul unei chei de acces și o cheie de acces secretă. Acestea pot fi auto-găzduite, precum [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) sau [MinIO](https://min.io/) (GNU AGPL v3.0) sau comerciale ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

Acest ghid a fost testat cu Scaleway Object Storage. Dacă folosiți un alt serviciu, vă rugăm partajați experiența dvs. (în special dacă a trebuit să urmați pași diferiți) completând un tichet pe depozitul [BookWyrm Documentation](https://github.com/bookwyrm-social/documentation).

### Ce vă așteaptă

Dacă începeți o nouă instanță BookWyrm, procesul va fi:

- Configurarea serviciul dvs. extern de stocare
- Activatul stocării externii pe BookWyrm
- Porniți instanța BookWyrm
- Actualizați conectorul instanței

Dacă ați început deja o instanță și imaginile au fost încărcate în stocarea internă, procesul va fi:

- Configurați serviciul dvs. extern de stocare
- Copiați fișierele media locale pe stocarea externă
- Activați stocarea externă pe BookWyrm
- Reporniți instanța BookWyrm
- Actualizați conectorul instanței

### Setări BookWyrm

Editați fișierul dvs. `.env` decomentând următoarele linii:

- `AWS_ACCESS_KEY_ID`: ID-ul cheie de acces al dvs.
- `AWS_SECRET_ACCESS_KEY`: cheia de acces secretă a dvs.
- `AWS_STORAGE_BUCKET_NAME`: numele „găleții” dvs.
- `AWS_S3_REGION_NAME`: de ex. `"eu-west-1"` pentru AWS, `"fr-par"` pentru Scaleway sau `"nyc3"` pentru Digital Ocean

Dacă serviciul dvs. S3 compatibil este Amazon AWS, ar trebui să fie deja setat. Dacă nu, va trebui să decomentați următoarele linii:

- `AWS_S3_CUSTOM_DOMAIN`: domeniul care va deservi modelele, de ex. `"example-bucket-name.s3.fr-par.scw.cloud"` sau `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
- `AWS_S3_ENDPOINT_URL`: punctul final al API-ului S3 (S3 API endpoint), de ex. `"https://s3.fr-par.scw.cloud"` sau `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`

### Copiați fișierele media locale pe stocarea externă

Dacă instanța dvs. BookWyrm rulează deja și fișierele media au fost încărcate (avatare de utilizator, coperți de cărți…), va trebui să migrați fișierele media încărcate pe „găleata” (bucket) dvs.

Această sarcină este realizată de comanda:

```bash
./bw-dev copy_media_to_s3
```

### Activați stocarea externă pentru BookWyrm

Pentru a activa stocarea externă S3 compatibiliă, va trebui să editați fișierul dvs. `.env` schimbând valoarea proprietății pentru `USE_S3` din `false` în `true`:

```
USE_S3=true
```

Dacă stocarea externă a dvs. este deservită prin HTTPS (cel mai des în prezent), veți avea nevoie de asemenea să vă asigurați că `USE_HTTPS` este setat la `true`, în așa fel încât imaginile vor fi încărcate prin HTTPS:

```
USE_HTTPS=true
```

#### Modele statice

Apoi, veți avea nevoie să rulați următoarea comandă pentru a copia modelele statice către „găleata” dvs. S3:

```bash
./bw-dev collectstatic
```

#### Setări CORS

Odată ce modelele statice au fost colectate, veți avea nevoie să configurați CORS pentru găleata dvs.

Unele servicii precum Digital Ocean oferă o interfață de configurare, vedeți [Digital Ocean doc: How to Configure CORS](https://docs.digitalocean.com/products/spaces/how-to/configure-cors/).

Dacă serviciul dvs. nu oferă o interfață, încă puteți configura CORS în linia de comandă.

Creați un fișier numit `cors.json` cu conținutul următor:

```json
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://MY_DOMAIN_NAME", "https://www.MY_DOMAIN_NAME"],
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "HEAD", "POST", "PUT", "DELETE"],
      "MaxAgeSeconds": 3000,
      "ExposeHeaders": ["Etag"]
    }
  ]
}
```

Înlocuiți `MY_DOMAIN_NAME` cu numele domeniului/domeniilor ale instanței dvs.

Apoi rulați următoarea comandă:

```bash
./bw-dev set_cors_to_s3 cors.json
```

Dacă nu afișează nimic este de bine.

Dacă începeți o instanță nouă BookWyrm, puteți reveni la instrucțiunile de configurare acum. Dacă nu, continuați să citiți.

### Reporniți instanța dvs.

Odată ce migrarea fișierelor media a fost făcută și modelele statice colectate, puteți încărca noua configurare `.env` și reporni instanța cu:

```bash
./bw-dev up -d
```

Dacă totul decurge cum trebuie, stocarea dvs. a fost schimbată fără timp de oprire. Dacă unele fonturi lipsesc (și consola JS a navigatorului dvs. vă arată alerte CORS), atunci ceva a mers greșit [here](#cors-settings). În acest caz, ar fi bine să verificați antetele unei cereri HTTP cu un fișier al „găleții” dvs:

```bash
curl -X OPTIONS -H 'Origin: http://MY_DOMAIN_NAME' http://BUCKET_URL/static/images/logo-small.png -H "Access-Control-Request-Method: GET"
```

Înlocuiți `MY_DOMAIN_NAME` cu numele domeniului instanței dvs., `BUCKET_URL` cu URL-ul pentru găleata dvs. Puteți înlocui calea fișierului co orice altă cale validă pentru găleata dvs.

Dacă vedeți vrun mesaj, în special un mesaj începând cu `<Error><Code>CORSForbidden</Code>`, nu a funcționat. Dacă nu vedeți niciun mesaj, atunci a mers.

Pentru o instanță activă, s-ar putea să fie câteva fișiere care au fost create local în timpul migrării fișierelor pe stocarea externă. Reporniți aplicația pentru a folosi stocarea externă. Pentru a vă asigura că orice fișier rămas este încărcat pe stocarea externă după schimbare, puteți folosi comanda următoare, care va încărca numai fișierele care nu sunt prezente pe stocarea externă:

```bash
./bw-dev sync_media_to_s3
```

### Actualizați conectorul instanței

*Notă: puteți sări acest pas dacă rulați o versiune actualizată de BookWyrm. În septembrie 2021, „conectorul de raft” a fost înlăturat în [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413)*

Pentru ca URL-ul corect să fie utilizat la afișarea rezultatelor de căutare pentru cărțile locale, va trebui să modificați valoarea pentru URL de bază a imaginilor de copertă.

Datele conectorului pot fi accesate cu interfața de admin Django, situată la URL-ul `http://MY_DOMAIN_NAME/admin`. Conectorul pentru propria voastră instanță este prima intrare în baza de date, deci puteți să-l accesați prin acest URL: `https://MY_DOMAIN_NAME/admin/bookwyrm/connector/1/change/`.

Câmpul _Covers url_ este definit în mod implicat ca `https://MY_DOMAIN_NAME/images`. Trebuie să-l schimbați cu `https://S3_STORAGE_URL/images`. Apoi, apăsați butonul _Save_. Voilà!

Va trebui să actualizați valoarea pentru _Covers url_ de fiecare dată când schimbați URL-ul pentru stocarea dvs.
