- - -
Titolo: Aggiornare la tua istanza Data: 2022-11-17 Ordine: 3
- - -

Quando ci sono cambiamenti disponibili nel ramo di produzione, è possibile installare e farli funzionare sulla vostra istanza utilizzando il comando `. aggiornamento bw-dev`. Questo fa un certo numero di cose:

- `git pull` ottiene il codice aggiornato dal repository Git. Se si verificano conflitti, potrebbe essere necessario eseguire `git pull` separatamente e risolvere i conflitti prima di provare `. bw-dev aggiornamento` di nuovo script.
- `docker-compose build` ricostruisce le immagini, garantendo che i pacchetti corretti siano installati. Questo passaggio richiede molto tempo ed è necessario solo quando le dipendenze (compresi i requisiti pip `. xt` pacchetti) sono cambiate, in modo da poter commentare fuori se si desidera un percorso di aggiornamento più rapido e non dispiacere-commentare se necessario.
- `docker-compose run --rm web python manage.py migrate` esegue le migrazioni del database in Django utilizzando le immagini Docker appena create
- `docker-compose run --rm web python manage.py collectstatic --no-input` carica qualsiasi file statico aggiornato (come JavaScript e CSS)
- `docker-compose giù: docker-compose up -d` riavvierà tutti i contenitori docker e userà le immagini di nuova costruzione (attenzione: tempi di fermo durante il riavvio)

## Ricostruisci flussi attività

I feed di ogni utente sono memorizzati in Redis. Per ripopolare un flusso, utilizzare il comando gestione:

``` { .sh }
./bw-dev populate_streams
# O utilizza docker-compose direttamente
docker-compose run --rm web python manage.py populate_streams
```

Se qualcosa è andato terribilmente male, i dati del flusso possono essere cancellati.

``` { .sh }
docker-compose esegui --rm web python manage.py erase_stream
```
