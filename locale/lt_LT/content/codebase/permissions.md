- - -
Pavadinimas: Leidimai Data: 2021-04-18 Užsakymas: 2
- - -

Naudotojų prieiga prie įvairių funkcijų kontroliuojama per Django [integruotą autentifikacijos sistemą](https://docs.djangoproject.com/en/3.2/topics/auth/default/). Kai sukuriamas serveris, `initdb` scenarijus sukuria leidimų rinkinį, kuris priskiriamas prie grupių. Visi nauji nariai priskiriami prie `redaktoriaus` grupės, todėl jie gali redaguoti knygos metaduomenis.

Serverio administratorius turi `supernaudotojo` teisę, kurios dėka gaunama prieiga prie Django administratoriaus (`/admin`) ir nariui suteikiami visi leidimai.

## Leidimai ir grupės
Šioje lentelėje rodomos keturios grupės (administratoriaus, moderatoriaus, redaktoriaus ir nario) bei kokius leidimus turi tos grupės naudotojas:

|                        | administratorius | moderatorius | editor | user |
| ---------------------- | ---------------- | ------------ | ------ | ---- |
| edit instance settings | ✔️               | -            | -      | -    |
| change user level      | ✔️               | -            | -      | -    |
| manage federation      | ✔️               | ✔️           | -      | -    |
| issue invites          | ✔️               | ✔️           | -      | -    |
| deactivate users       | ✔️               | ✔️           | -      | -    |
| delete posts           | ✔️               | ✔️           | -      | -    |
| edit books             | ✔️               | ✔️           | ✔️     | -    |
 upload covers            |  ✔️    |     ✔️       |   ✔️     |  ✔️
