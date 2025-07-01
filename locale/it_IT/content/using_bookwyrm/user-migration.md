---
Title: Trasferimento degli utenti e alias
Date: 06-01-2024
Order: 21
---

È possibile trasferire il proprio account tra differenti istanze BookWyrm e/o associare un _alias_tra un qualunque account ActivityPub e il proprio profilo BookWyrm.

## Esportazione dati dell'account

Puoi esportare i dati del tuo account in qualsiasi momento, tuttavia ci sarà un limite su quanto spessopuoi farlo, impostato dal vostro amministratore di istanza. Una volta avviata l’esportazione dei dati, il processo verrà eseguito in background. Ti verrà inviata una notifica quando il file sarà pronto per essere scaricato. I file di esportazione sono nel formato tar.gz.

I file di esportazione dell'account includono:

- Profilo utente e avatar
- Impostazioni avanzate
- Obiettivi
- Raccolte
- Cronologia
- Recensione di libri
- Stato
- Liste personali e liste salvate
- Utenti seguiti e bloccati

Le esportazioni _non _includono:

- Messaggi privati
- Risposte al tuo stato
- Gruppi
- Preferiti

## Alias

Un _alias_ indica al software ActivityPub che due account rappresentano e sono gestiti dalla stessa persona. Puoi assegnare qualsiasi account ActivityPub come alias del tuo account BookWyrm andando su Impostazioni - Alias.

Impostare un account come alias è un’operazione facilmente reversibile ed è necessaria per trasferire gli account.

## Trasferimento account

Puoi "spostare" un account da uno all'altro in Impostazioni - Sposta account. Spostare il tuo account avviserà tutti i tuoi follower e li indirizzerà a seguire il nuovo account (target) - inclusi i follower dai server non-BookWyrm. Se si desidera anche spostare i dati utente, vedere "Importazione dati account" qui sotto.

Il vecchio account (sorgente) sarà contrassegnato come spostato e non sarà individuabile o utilizzabile a meno che non annulli lo spostamento, che puoi fare in qualsiasi momento, tuttavia tutti i follower che hanno spostato i loro follower dal vecchio account al nuovo account non seguiranno più il tuo vecchio account.

_Devi_impostare il vecchio utente (sorgente) come alias del nuovo utente (target) nelle impostazioni dell'account di destinazione per il funzionamento di un `Sposta`.

## Importazione dati dell’account

Una volta ottenuto il file di esportazione, puoi importarlo in un’altra istanza di BookWyrm. Per farlo, devi prima impostare il nuovo account (target) come alias del vecchio account (sorgente), oppure spostare il vecchio account su quello nuovo.

È importante leggere le istruzioni nella pagina di importazione dell’account, poiché alcuni dati potrebbero essere sovrascritti se selezionati. Esiste anche un limite alla frequenza con cui puoi importare i dati utente.

- Vai a \`Impostazioni - Importa account BookWyrm
- Seleziona il tuo file di esportazione
- Deseleziona tutte le opzioni di dati che non vuoi importare
- Clicca Su 'Importa'

L’importazione verrà eseguita in background e riceverai una notifica al termine del processo.

Se importi dati da un account presente sullo stesso server, tutti i post (commenti, recensioni, citazioni) saranno riassegnati al nuovo utente.