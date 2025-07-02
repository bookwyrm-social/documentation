---
Title: Controlli Sulla Privacy
Date: 26-05-2025
Order: 7
---

BookWyrm offre diversi livelli di privacy che permettono agli utenti di controllare quanto siano pubblici i propri contenuti e chi può vederli.
Desideri condividere le tue letture con l’intero internet, solo con i tuoi amici o mantenerle private?

BookWyrm prevede quattro livelli di privacy: Pubblico, Non in elenco, Visibile ai follower e Privato.
In sintesi: Pubblico è visibile a tutti, Non in elenco è nascosto ma accessibile con il link, Solo follower è limitato ai tuoi follower, e Privato è visibile solo da te.
Questi livelli di privacy si comportano in modo diverso a seconda del tipo di contenuto su BookWyrm.

Su tutto il sito, il livello di privacy di un contenuto è indicato dall’icona che lo accompagna.
L’icona di un globo indica che il contenuto è Pubblico, un lucchetto aperto indica Non in elenco, un lucchetto chiuso corrisponde a Solo follower, e una busta rappresenta i contenuti Privati.

Nota: Chiunque può iniziare a seguirti e, in questo modo, vedere tutti i contenuti che hai contrassegnato come “visibili solo ai follower”.
Se vuoi limitare questa funzione, accedi a Impostazioni - Modifica profilo - Privacy e attiva l’opzione “Approva manualmente i follower”.
Questo ti consente di esaminare attentamente le richieste di accesso, oppure di limitarle esclusivamente ai tuoi amici.

Altre impostazioni sulla privacy sono spiegate [in fondo a questa pagina](#privacy-related-settings).

## Stato

Su Bookwyrm, gli [stati](/posting-statuses.html) possono essere pubblicati con quattro diversi livelli di privacy, che limitano chi può vederli e se vengono messi in evidenza nelle pagine pubbliche.
Ogni stato ha un proprio livello di privacy, quindi puoi scegliere quando renderlo Pubblico o Privato, oppure impostare un valore predefinito nelle impostazioni.
Nota che non può essere modificato una volta pubblicato.

### Pubblico

L'opzione predefinita.

- Chiunque può vedere il tuo stato senza effettuare l'accesso.
- Il tuo stato apparirà su:
    - timeline pubbliche
    - pagine di scoperta.
    - la pagina del libro a cui è collegato.
    - la timeline principale delle persone che ti seguono
- Il tuo stato può essere condiviso (boostato) nelle timeline principali di altre persone.

### Non in elenco

Esattamente come “Pubblico”, ma:

- Il tuo stato non apparirà nelle timeline pubbliche né nelle pagine di scoperta.

### Follower

- Solo le persone che ti seguono possono vedere il tuo stato nelle loro timeline o nella pagina del libro correlato.
- Il tuo stato non può essere condiviso (boostato).

### Privato

- Il tuo stato può essere visto solo da te, dalle persone menzionate al suo interno e da chi ha già partecipato alla conversazione.
- Questo è il livello di privacy utilizzato nei Messaggi Privati.

## Raccolte

Le raccolte sono pubbliche di default, ma puoi modificarle per renderle visibili solo ai tuoi follower oppure solo a te stesso.

### Pubblico / Non Elencato

- Per le scaffalature, non c’è differenza tra “Pubblico” e “Non in elenco”. L’opzione “Non in elenco” potrebbe essere rimossa in futuro.
- Chiunque può vedere queste scaffalature e tutti i libri che contengo.

### Follower

- Solo le persone che ti seguono possono vedere questa raccolta e i libri che contiene.

### Privato

- Solo tu potrai vedere la raccolta e i libri che contiene.

### Raccolta di tutti i libri

- La raccolta “Tutti i libri” è uno scaffale predefinito che mostra i libri presenti in tutti gli scaffali visibili all’utente che li sta visualizzando.

| Utente       | Libri sulle raccolte pubbliche | Libri "Non in elenco" | Libri "Solo follower" | Libri "Privati" |
| ------------ | ------------------------------ | --------------------- | --------------------- | --------------- |
| Tutti        | ✔                              | ✔                     |                       |                 |
| Chi ti segue | ✔                              | ✔                     | ✔                     |                 |
| Te stesso    | ✔                              | ✔                     | ✔                     | ✔               |

### Implicazioni

- Se leggi un libro, vuoi tracciarlo su Bookwyrm ma non vuoi che nessuno lo sappia, dovrai aggiungerlo a una nuova raccolta **Privata**, e non a una raccolta **Pubblica**.

## Liste

### Pubblico

- Chiunque può vedere la tua [Lista](/lists.html) senza effettuare l’accesso.
- La tua lista apparirà su:
    - la pagina Liste di scoperta (scheda Elenchi).
    - le pagine che un libro contiene verranno visualizzate lateralmente sullo schermo.
    - profilo utente.
- Chiunque può 'salvare' (segnalibro) la tua lista.

### Non in elenco

- Attualmente non c’è alcuna differenza tra “Pubblico” e “Non in elenco” per le Liste.
    In futuro, l’opzione “Non in elenco” nasconderà nella Lista dalle pagine scoperte e dalle pagine dei libri.
    Per ulteriori dettagli, [#3265](https://github.com/bookwyrm-social/bookwyrm/issues/3265) vedi su GitHub.

### Follower

- Solo le persone che ti seguono possono vedere la tua lista sulle pagine sopra menzionate.

### Privato

- Solo tu puoi vedere la tua lista sulle pagine sopra menzionate.

## Gruppi

I [Gruppi](/groups.html) hanno le stesse impostazioni di privacy di stati e liste, tranne che non possono essere impostati come “Solo follower”.
L’iscrizione a un gruppo richiede sempre un invito da parte del proprietario del gruppo, anche se il gruppo è impostato come Pubblico.
Nota che, al momento, la scheda Gruppi in un profilo viene mostrata solo se l’utente che la visualizza ha effettuato l’accesso (vedi [#3610](https://github.com/bookwyrm-social/bookwyrm/issues/3610)).

### Pubblico

- Chiunque può vedere la pagina del Gruppo, i membri e le Liste associate (ad eccezione delle Liste private)

- In futuro verrà mostrata in una pagina di scoperta dedicata ai Gruppi.

### Non in elenco

- Chiunque può visualizzare la pagina del gruppo, i membri e le Liste associate (ad eccezione delle Liste private)

### Privato

- Solo i membri del gruppo possono visualizzare la pagina del gruppo, i membri e le Liste associate
- Tutte le Liste dei Gruppi saranno anch’esse private.

## Impostazioni relative alla privacy

### Approvare manualmente i follower

Si trova in 'Impostazioni-Modifica profilo-Privacy'.

Quando attivata, riceverai una notifica ogni volta che qualcuno vorrà seguirti e potrai scegliere se accettare o meno la richiesta.
Utile se vuoi controllare chi sono o limitare i tuoi follower solo ai tuoi amici e persone che conosci.

### Nascondi la lista di follower e seguiti sul profilo

Si trova in 'Impostazioni-Modifica profilo-Privacy'.

Di default, chiunque può vedere la lista delle persone che segui e dei tuoi follower.
Ci sono molti motivi per cui potresti non volerlo, quindi Bookwyrm ti permette di nascondere queste liste.

### Mostra questo account tra gli utenti suggeriti

Si trova in 'Impostazioni-Modifica profilo-Aspetto'.

Se attivata, il tuo account potrà essere suggerito ad altri utenti e comparirà nell’elenco degli account.

