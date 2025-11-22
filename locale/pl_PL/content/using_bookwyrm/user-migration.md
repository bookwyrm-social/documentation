---
Title: Migracja użytkowników i aliasy
Date: 2024-01-06
Order: 21
---

Możesz przenosić swoje konto między instancjami BookWyrm i/lub ustawić _alias_ między dowolnym kontem ActivityPub i swoim kontem BookWyrm.

## Eksportowanie danych konta

Możesz eksportować dane swojego konta w dowolnym momencie, ale administrator instancji może ustawić limit częstotliwości wykonywania tego zadania. Podczas tworzenia pliku eksportu w tle zostanie uruchomiony proces i otrzymasz powiadomienie, gdy zostanie zakończony, a plik będzie gotowy do pobrania. Pliki eksportu mają format „tar.gz”.

Pliki eksportu konta zawierają:

- Profil i obraz użytkownika
- Większość ustawień użytkownika
- Cele czytania
- Półki
- Historię czytania
- Recenzje książek
- Statusy
- Twoje własne listy i zapisane listy
- Obserwowanych i zablokowanych użytkowników

Eksporty _nie_ zawierają:

- Wiadomości bezpośrednich
- Odpowiedzi na Twoje statusy
- Grup
- Ulubionych

## Aliasy

_Alias_ wskazuje oprogramowaniu ActivityPub, że dwa konta reprezentują tę samą osobę i należą do niej. Możesz przypisać dowolne konto ActivityPub jako alias swojego konta BookWyrm, przechodząc do „Ustawienia - Aliasy”.

Setting an account as an alias is easily reversible, and is required to migrate accounts.

## Moving an account

You can "move" an account from one to another at `Settings - Move Account`. Moving your account will notify all your followers and direct them to follow the new (target) account - including followers from non-BookWyrm servers. If you also want to move your user data, see "Importing account data" below.

Your old (origin) account will be marked as moved and will not be discoverable or usable unless you undo the move, which you can do at any time, however any followers who have migrated their follow from the old account to the new account will no longer be following your old account.

You _must_ set the old (source) user as an alias of the new (target) user in the settings of the target account for a `Move` to work.

## Importing account data

Once you have an export file you can import it into another BookWyrm instance. To do so, you must first set the new (target) account as an alias of the old (source) account, or `Move` the old account to the new one.

It is important to read the instructions on the account import page as some data will be overwritten if selected. There is also a limit on how often you can import user data.

- Go to `Settings - Import BookWyrm Account`
- Select your export file
- Untick any data options you do not wish to import
- Click 'Import'

Your import will run in the background and you will be notified when it is completed.

If you import data from an account on the same server, all posts (comments, reviews, quotations) will be re-assigned to the new user.