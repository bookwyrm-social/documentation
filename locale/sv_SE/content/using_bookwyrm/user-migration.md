---
Title: User Migration and Aliases
Date: 2024-01-06
Order: 21
---

You can migrate your account between BookWyrm instances, and/or set up an _alias_ between any ActivityPub account and your BookWyrm acccount.

## Exportera kontodata

You can export your account data at any time, however there will be a limit on how often you can do this, set by your instance admin. When you create an export file a process will run in the background and you will be notified when it is completed and ready for download. Export files are in `tar.gz` format.

Account export files include:

- Användarprofil och avatar
- Most user settings
- Reading goals
- Shelves
- Reading history
- Book reviews
- Statusar
- Your own lists and saved lists
- Which users you follow and block

Exports do _not_ include:

- Direct messages
- Replies to your statuses
- Grupper
- Favoriter

## Aliases

An _alias_ indicates to ActivityPub software that two accounts represent and are controlled by the same person. You can assign any ActivityPub account as an alias of your BookWyrm account by navigating to `Settings - Aliases`.

Setting an account as an alias is easily reversible, and is required to migrate accounts.

## Flytta ett konto

You can "move" an account from one to another at `Settings - Move Account`. Moving your account will notify all your followers and direct them to follow the new (target) account - including followers from non-BookWyrm servers. If you also want to move your user data, see "Importing account data" below.

Your old (origin) account will be marked as moved and will not be discoverable or usable unless you undo the move, which you can do at any time, however any followers who have migrated their follow from the old account to the new account will no longer be following your old account.

You _must_ set the old (source) user as an alias of the new (target) user in the settings of the target account for a `Move` to work.

## Importera kontodata

Once you have an export file you can import it into another BookWyrm instance. To do so, you must first set the new (target) account as an alias of the old (source) account, or `Move` the old account to the new one.

It is important to read the instructions on the account import page as some data will be overwritten if selected. There is also a limit on how often you can import user data.

- Go to `Settings - Import BookWyrm Account`
- Välj din exportfil
- Untick any data options you do not wish to import
- Klicka 'Importera'

Your import will run in the background and you will be notified when it is completed.

If you import data from an account on the same server, all posts (comments, reviews, quotations) will be re-assigned to the new user.