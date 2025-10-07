- - -
Title: External Storage Date: 2021-06-07 Order: 8
- - -

Per impostazione predefinita, BookWyrm utilizza memoria locale per le risorse statiche (favicon, avatar predefinito, ecc., e i supporti (avatar utente, copertine di libri, ecc.), ma è possibile utilizzare un servizio di archiviazione esterno per servire questi file. BookWyrm utilizza `django-storages` per gestire l'archiviazione esterna, come servizi compatibili con S3, Apache Libcloud o SFTP.

## Servizi S3 Compatibili

### Configurazione

Crea un secchio al tuo servizio S3 compatibile, insieme ad un ID chiave di accesso e a una chiave di accesso segreto. Questi possono essere ospitati autonomamente, come [Ceph](https://ceph.io/en/) (LGPL 2.1/3.0) o [MinIO](https://min.io/) (GNU AGPL v3.), o commerciale ([Scaleway](https://www.scaleway.com/en/docs/object-storage-feature/), [Digital Ocean](https://www.digitalocean.com/community/tutorials/how-to-create-a-digitalocean-space-and-api-key)…).

Questa guida è stata testata contro l'archivio oggetti di Scaleway. Se utilizzi un altro servizio, per favore condividi la tua esperienza (specialmente se hai dovuto fare passi diversi) scrivendo sul repository [BookWyrm Documentation](https://github.com/bookwyrm-social/documentation).

### Cosa ti aspetta

Se stai iniziando una nuova istanza di BookWyrm, il processo sarà:

- Imposta il tuo servizio di archiviazione esterno
- Attiva memoria esterna su BookWyrm
- Avvia la tua istanza BookWyrm
- Aggiorna il connettore dell'istanza

Se hai già avviato la tua istanza e le immagini sono state caricate nell'archivio locale, il processo sarà:

- Configura il tuo servizio di archiviazione esterno
- Copia i file multimediali locali su memoria esterna
- Abilitare memoria esterna su BookWyrm
- Riavvia l'istanza di BookWyrm
- Aggiornare il connettore istanza

### Impostazioni BookWyrm

Modifica il tuo file `.env` senza commentare le righe seguenti:

- `AWS_ACCESS_KEY_ID`: ID della tua chiave di accesso
- `AWS_SECRET_ACCESS_KEY`: la chiave di accesso segreto
- `AWS_STORAGE_BUCKET_NAME`: nome del tuo bucket
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` for AWS, `"fr-par"` for Scaleway, `"nyc3"` for Digital Ocean or `"cluster-id"` for Linode

Se il servizio compatibile con S3 è Amazon AWS, è necessario essere impostati. In caso contrario, dovrete annullare il commento alle seguenti righe:

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

### Copia media locali su memoria esterna

Se l'istanza BookWyrm è già in esecuzione e i media sono stati caricati (avatar utente, copertine del libro…), dovrai migrare i media caricati sul tuo secco.

Questo compito è stato fatto con il comando:

```bash
./bw-dev copy_media_to_s3
```

### Attiva memoria esterna su BookWyrm

Per attivare la memoria esterna compatibile con S3, dovrai modificare la tua `. nv` file cambiando il valore della proprietà per `USE_S3` da `false` a `vero`:

```
USE_S3=true
```

**Note** that after `v0.7.5` all traffic is assumed to be HTTPS, so you need to ensure that your external storage is also served over HTTPS.

#### Risorsa statiche

Then, you will need to run the following commands to compile the themes and copy all static assets to your S3 bucket:

```bash
./bw-dev compile_themes
./bw-dev collectstatic
```

#### Impostazioni CORS

Una volta che gli asset statici sono stati raccolti, è necessario impostare il CORS per il vostro secco.

Alcuni servizi come Digital Ocean forniscono un'interfaccia per impostarla, vedi [Digital Ocean doc: Come configurare CORS](https://docs.digitalocean.com/products/spaces/how-to/configure-cors/).

Se il servizio non fornisce un'interfaccia, è comunque possibile configurare CORS con la riga di comando.

Creare un file chiamato `cors.json`con il seguente contenuto:

```json
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://MY_DOMAIN_NAME", "https://www. Y_DOMAIN_NAME"],
      "AllowedHeaders": ["*"],
      "AllowedMethods": ["GET", "HEAD", "POST", "PUT", "DELETE"],
      "MaxAgeSeconds": 3000,
      "ExposeHeaders": ["Etag"]
    }
  ]
}
```

Sostituire `MY_DOMAIN_NAME` con il nome di dominio della tua istanza.

Quindi, eseguire il comando seguente:

```bash
./bw-dev set_cors_to_s3 cors.jsonName
```

Nessuna uscita significa che dovrebbe essere buona.

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

If you are starting a new BookWyrm instance, you can go back to the setup instructions right now: [[Docker](install-prod.html)] [[Dockerless](install-prod-dockerless.html)]. In caso negativo, continuare a leggere.

### Riavviare l'istanza

Una volta che la migrazione dei media è stata fatta e gli asset statici sono raccolti, è possibile caricare la nuova `. configurazione nv` e riavvia l'istanza con:

```bash
./bw-dev su -d
```

Se tutto va bene, la tua memoria è stata cambiata senza tempi di inattività server. Se mancano alcuni tipi di carattere (e la console JS del tuo browser si illumina con avvisi sul CORS), qualcosa è andato storto [qui](#cors-settings). In questo caso potrebbe essere bene controllare le intestazioni di una richiesta HTTP contro un file sul vostro secchi:

```bash
curl -X OPTIONS -H 'Origine: http://MY_DOMAIN_NAME' http://BUCKET_URL/static/images/logo-small.png -H "Access-Control-Request-method: GET"
```

Sostituire `MY_DOMAIN_NAME` con il nome del dominio di istanza, `BUCKET_URL` con l'URL per il tuo secchio, è possibile sostituire il percorso del file con qualsiasi altro percorso valido sul tuo secco.

Se vedi un messaggio, soprattutto un messaggio che inizia con `<Error><Code>CORSForbidden</Code>`, non ha funzionato. Se non vedi alcun messaggio, ha funzionato.

Per un esempio attivo, ci può essere una manciata di file che sono stati creati localmente durante il tempo tra la migrazione dei file all'archivio esterno, e riavviare l'app in modo che usi la memoria esterna. Per garantire che tutti i file rimanenti siano caricati nella memoria esterna dopo il passaggio all'esterno, puoi usare il seguente comando, che caricherà solo i file che non sono già presenti nella memoria esterna:

```bash
./bw-dev sync_media_to_s3
```

### Aggiornando il connettore istanza

*Nota: È possibile saltare questo passo se si esegue una versione aggiornata di BookWyrm; nel settembre 2021 il "connettore di auto" è stato rimosso in [PR #1413](https://github.com/bookwyrm-social/bookwyrm/pull/1413)*

Affinché l'URL corretto possa essere utilizzato quando si visualizzano i risultati di ricerca locali di un libro dobbiamo modificare il valore per la base URL delle immagini di copertina.

I dati del connettore possono essere accessibili tramite l'interfaccia di amministrazione Django, situata all'url `http://MY_DOMAIN_NAME/admin`. Il connettore per la tua istanza è il primo record del database, quindi puoi accedere al connettore con questo URL: `https://MY_DOMAIN_NAME/admin/bookwyrm/connector/1/change/`.

Il campo _Covers url_ è definito per impostazione predefinita come `https://MY_DOMAIN_NAME/images`, devi modificarlo in `https://S3_STORAGE_URL/images`. Quindi, fare clic sul pulsante _Salva_ e voila<unk>!

Dovrai aggiornare il valore per _Copertina url_ ogni volta che cambi l'URL per la tua archiviazione.
