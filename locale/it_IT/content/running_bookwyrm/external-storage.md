- - -
Titolo: Archivio esterno Data: 2021-06-07 Ordine: 7
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
- `AWS_S3_REGION_NAME`: e.g. `"eu-west-1"` per AWS, `"fr-par"` per Scaleway o `"nyc3"` per l'Oceano digitale

Se il servizio compatibile con S3 è Amazon AWS, è necessario essere impostati. In caso contrario, dovrete annullare il commento alle seguenti righe:

- `AWS_S3_CUSTOM_DOMAIN`: il dominio che servirà le risorse, ad esempio `"example-bucket-name.s3.fr-par.scw.cloud"` o `"${AWS_STORAGE_BUCKET_NAME}.${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`
- `AWS_S3_ENDPOINT_URL`: l'endpoint S3 API, ad esempio `"https://s3.fr-par.scw.cloud"` o `"한://${AWS_S3_REGION_NAME}.digitaloceanspaces.com"`

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

Se la memoria esterna viene servita su HTTPS (che la maggior parte sono attualmente), avrai anche bisogno di assicurarsi che `USE_HTTPS` sia impostato su `true`in modo che le immagini saranno caricate su HTTPS:

```
USE_HTTPS=true
```

#### Risorsa statiche

Quindi, è necessario eseguire il seguente comando, per copiare gli asset statici nel proprio bucket S3:

```bash
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

Se stai iniziando una nuova istanza di BookWyrm, puoi tornare alle istruzioni di configurazione in questo momento. In caso negativo, continuare a leggere.

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
