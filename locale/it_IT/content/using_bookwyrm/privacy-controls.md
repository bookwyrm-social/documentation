---
Title: Controlli Sulla Privacy
Date: 26-05-2025
Order: 7
---

BookWyrm offre diversi livelli di privacy che permettono agli utenti di controllare quanto siano pubblici i propri contenuti e chi può vederli.
Desideri condividere le tue letture con l’intero internet, solo con i tuoi amici o mantenerle private?

BookWyrm prevede quattro livelli di privacy: Pubblico, Non in elenco, Visibile ai follower e Privato.
In sintesi: Pubblico è visibile a tutti,  Non in elenco è nascosto ma accessibile con il link, Solo follower è limitato ai tuoi follower, e Privato è visibile solo da te.
Questi livelli di privacy si comportano in modo diverso a seconda del tipo di contenuto su BookWyrm.

Su tutto il sito, il livello di privacy di un contenuto è indicato dall’icona che lo accompagna.
L’icona di un globo indica che il contenuto è Pubblico, un lucchetto aperto indica Non in elenco, un lucchetto chiuso corrisponde a Solo follower, e una busta rappresenta i contenuti Privati.

Note: Anyone can just follow you and then be able to see all things you marked Followers-only.
Se vuoi limitare questa funzione, accedi a Impostazioni - Modifica profilo - Privacy e attiva l’opzione “Approva manualmente i follower”.
Questo ti consente di esaminare attentamente le richieste di accesso, oppure di limitarle esclusivamente ai tuoi amici.

Other privacy settings are explained [at the bottom of this page](#privacy-related-settings).

## Stato

On Bookwyrm, [statuses](/posting-statuses.html) can be posted at four different privacy levels, which restrict who can see it and if it's promoted on public pages.
Ogni stato ha un proprio livello di privacy, quindi puoi scegliere quando renderlo Pubblico o Privato, oppure impostare un valore predefinito nelle impostazioni.
Nota che non può essere modificato una volta pubblicato.

### Public

L'opzione predefinita.

- Chiunque può vedere il tuo stato senza effettuare l'accesso.
- Il tuo stato apparirà su:
    - timeline pubbliche
    - pagine di scoperta.
    - its related book's page.
    - la timeline principale delle persone che ti seguono
- Il tuo stato può essere condiviso (boostato) nelle timeline principali di altre persone.

### Non in elenco

Esattamente come “Pubblico”, ma:

- Il tuo stato non apparirà nelle timeline pubbliche né nelle pagine di scoperta.

### Followers

- Solo le persone che ti seguono possono vedere il tuo stato nelle loro timeline o nella pagina del libro correlato.
- Il tuo stato non può essere condiviso (boostato).

### Private

- Your status can only be seen by you, anyone **mentioned** in it, and anyone previously involved in the conversation.
- This is the privacy level used in Direct Messages.

## Shelves

Shelves are Public by default, but you can edit them to make them only visible to your followers or just yourself.

### Public / Unlisted

- Per le scaffalature, non c’è differenza tra “Pubblico” e “Non in elenco”. L’opzione “Non in elenco” potrebbe essere rimossa in futuro.
- Chiunque può vedere queste scaffalature e tutti i libri che contengo.

### Followers

- Only people who follow you will see this shelf and the books on it.

### Private

- Only you will be able to see this shelf and the books on it.

### All books shelf

- The 'All books' shelf is a default shelf which displays books from all visible shelves to the user viewing it.

| User        | Libri sulle raccolte pubbliche | Books on Unlisted shelves | Books on Followers-only shelves | Books on Private shelves |
| ----------- | ------------------------------ | ------------------------- | ------------------------------- | ------------------------ |
| Anyone      | ✔                              | ✔                         |                                 |                          |
| Follows you | ✔                              | ✔                         | ✔                               |                          |
| Yourself    | ✔                              | ✔                         | ✔                               | ✔                        |

### Implications

- If you read a book, want to track it on Bookwyrm, but don't want anyone to know that you did, you'll need to put it on a new Private shelf, not a Public shelf.

## Liste

### Pubblico

- Chiunque può vedere la tua [Lista](/lists.html) senza effettuare l’accesso.
- La tua lista apparirà su:
    - la pagina Liste di scoperta (scheda Elenchi).
    - the pages of books that are in it, displayed on the side of the screen.
    - your profile.
- Anyone can 'save' (bookmark) your List.

### Unlisted

- There is currently no difference between Public and Unlisted for Lists.
    In the future, Unlisted will hide the List from the Lists discovery page and books pages.
    For details, see [#3265](https://github.com/bookwyrm-social/bookwyrm/issues/3265) on GitHub.

### Followers

- Only people who follow you can see your List on the aforementioned pages.

### Private

- Only you can see your List on the aforementioned pages.

## Groups

[Groups](/groups.html) have the same privacy settings as statuses and lists do, except they can't be Followers-only.
Group membership always requires an invitation from the group's owner, even if it is marked Public.
Note that currently, the Groups tab on a profile is only shown if the user viewing it is logged in (see [#3610](https://github.com/bookwyrm-social/bookwyrm/issues/3610)).

### Public

- Anyone can view the Group page, members and its Lists (except for private Lists)

- In futuro verrà mostrata in una pagina di scoperta dedicata ai Gruppi.

### Unlisted

- Anyone can view the group page, members and its Lists (except for private Lists)

### Private

- Only members of the group can view the group page, members and its Lists
- All the Groups Lists will also be private.

## Privacy related settings

### Manually approve followers

Found in `Settings - Edit Profile - Privacy`.

When enabled, you will get a notification when someone wants to follow you, and you'll be able to choose whether or not to accept it.
Useful if you want to check who they are or restrict your followers to only be your friends and people you know.

### Hide followers and following lists on profile

Found in `Settings - Edit Profile - Privacy`.

By default, anyone can view the list of people you follow and who follow you.
There are many reasons you might not want this, so Bookwyrm allows you to hide these lists.

### Show this account in suggested users

Found in `Settings - Edit Profile - Display`.

When enabled, your account may be suggested to other users and will be on the account directory.

