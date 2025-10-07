- - -
Title: External Storage Date: 2021-06-07 Order: 8
- - -

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
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` for AWS, `"fr-par"` for Scaleway, `"nyc3"` for Digital Ocean or `"cluster-id"` for Linode

Dacă serviciul dvs. S3 compatibil este Amazon AWS, ar trebui să fie deja setat. Dacă nu, va trebui să decomentați următoarele linii:

- `AWS_S3_CUSTOM_DOMAIN`: the domain that will serve the assets:
  - for Scaleway, e.g. `"example-bucket-name.s3.fr-par.scw.cloud"`
  - for Digital Ocean, e.g. `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
  - for Linode Object Storage, this should be set to the cluster domain, e.g. `"eu-central-1.linodeobjects.com"`
- `AWS_S3_ENDPOINT_URL`: the S3 API endpoint:
  - for Scaleway, e.g. `"https://s3.fr-par.scw.cloud"`
  - for Digital Ocean, e.g. `"https://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
  - For Linode Object Storage, set this to the cluster domain, e.g. `"https://eu-central-1.linodeobjects.com"`

For many S3 compatible services, the default `ACL` is `"public-read"`, and this is what BookWyrm defaults to. If you are using Backblaze (B2) you need to explicitly set the default ACL to be empty in your `.env` file:

```
AWS_DEFAULT_ACL=""
```

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

**Note** that after `v0.7.5` all traffic is assumed to be HTTPS, so you need to ensure that your external storage is also served over HTTPS.

#### Modele statice

Then, you will need to run the following commands to compile the themes and copy all static assets to your S3 bucket:

```bash
./bw-dev compile_themes
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

### Additional Step for Linode Object Storage Users

For Linode, you now need to make an alteration to the `.env` to ensure that the generated links to your storage objects are correct. If you miss this step, all the links to images and static files (like css) will be broken. To fix this, you need to now insert the bucket-name into the `AWS_S3_CUSTOM_DOMAIN`, for example if your `AWS_STORAGE_BUCKET_NAME` is `"my-bookwyrm-bucket"`, then set it to:

```
AWS_S3_CUSTOM_DOMAIN=my-bookwyrm-bucket.cluster-id.linodeobjects.com
```

*Note*: From this point on, any bw-dev copy or sync commands will place objects into an incorrect location in your object store, so if you need to use them, revert to the previous setting, run and re-enable.

### User export and import files

After `v0.7.5`, user export and import files are saved to local storage even if `USE_S3` is set to `true`. Generally it is safer to use local storage for these files, and keep your used storage under control by setting up the task to periodically delete old export and import files.

If you are running a large instance you may prefer to use S3 for these files as well. If so, you will need to set the environment variable `USE_S3_FOR_EXPORTS` to `true`.

### New Instance

If you are starting a new BookWyrm instance, you can go back to the setup instructions right now: [[Docker](install-prod.html)] [[Dockerless](install-prod-dockerless.html)]. Dacă nu, continuați să citiți.

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
