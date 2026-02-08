---
Title: Kontoumzug und Aliase
Date: 2024-01-06
Order: 21
---

Du kannst mit deinem Konto zwischen BookWyrm-Instanzen umziehen und/oder _Aliase_ zwischen deinem ActivityPub-Konto und deinem BookWyrm-Konto definieren.

## Kontodaten exportieren

Du kannst deine Kontodaten jederzeit exportieren, allerdings legen die Administrator\*innen deiner Instanz eine Begrenzung fest, wie oft das möglich ist. Wenn du eine Exportdatei anlegst, wird ein Hintergrundprozess angestoßen. Du wirst benachrichtigt, wenn dieser Prozess beendet ist und dein Download bereitsteht. Exportdateien haben das Format `tar.gz`.

Exporte von Kontodaten beinhalten:

- Nutzer\*innenprofil und -avatar
- die meisten Einstellungen
- Leseziele
- Regale
- Lesehistorie
- Buchrezensionen
- Beiträge
- deine eigenen und von dir gespeicherte Listen
- welchen Nutzer\*innen du folgst und welche du blockiert hast

Exporte beinhalten _nicht_:

- Direktnachrichten
- Antworten auf deine Beiträge
- Gruppen
- Favoriten

## Aliase

Ein _Alias_ zeigt der ActivityPub-Software, dass zwei Konten dieselbe Person repräsentieren und von dieser kontrolliert werden. Du kannst ein ActivityPub-Konto als Alias für dein BookWyrm-Konto setzen, indem du zu `Einstellungen – Aliase` navigierst.

Ein Konto als Alias festzulegen lässt sich einfach rückgängig machen. Es wird benötigt, um Konten umzuziehen.

## Ein Konto umziehen

Du kannst von einem Konto zu einem anderen umziehen unter `Einstellungen – Account umziehen`. Wenn du umziehst, werden deine Follower\*innen benachrichtigt und zu deinem neuen (Ziel-)Konto umgeleitet – das umfasst auch Follower\*innen von Nicht-BookWyrm-Servern. Wenn du auch deine Nutzer\*innendaten umziehen möchtest, sieh dir "Kontodaten importieren" weiter unten an.

Dein altes (Herkunfts-)Konto wird als "umgezogen" markiert und wird nicht mehr entdeckt oder in Suchen gefunden werden können, sofern du den Umzug nicht rückgängig machst. Dies ist jederzeit möglich, aber alle Follower\*innen, die ihre Folge-Beziehung zum neuen Konto migriert haben, werden deinem alten Konto nicht länger folgen.

Du _musst_ in den Einstellungen das alte (Herkunfts-)Konto als Alias des neuen (Ziel-)Kontos festlegen, damit ein Umzug funktioniert.

## Kontodaten importieren

Sobald du eine Export-Datei hast, kannst du sie in eine andere BookWyrm-Instanz importieren. Dazu musst du zuerst das neue (Ziel-)Konto als Alias des alten (Herkunfts-)Kontos festlegen oder das alte Konto zum neuen umziehen.

Es ist wichtig, die Anleitung auf der Seite zum Kontoimport genau zu lesen, da manche Daten überschrieben werden, wenn dies nicht anders ausgewählt wird. Es gibt auch eine Begrenzung, wie oft du Kontodaten importieren kannst.

- Gehe zu `Einstellungen – BookWyrm-Konto importieren`
- Wähle deine Exportdatei
- Wähle jede Datenoption ab, die du nicht importieren möchtest
- Klicke auf "Importieren"

Der Import wird im Hintergrund ausgeführt und du erhältst eine Benachrichtigung, wenn er abgeschlossen ist.

Wenn du Daten von einem Konto auf demselben Server importierst, werden alle Beiträge (Kommentare, Rezensionen, Zitate) dem neuen Konto zugewiesen.