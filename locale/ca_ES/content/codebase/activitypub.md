- - -
Títol: ActivityPub Data: 21-04-2025 Ordre: 1
- - -

BookWyrm utiltza el protocol [ActivityPub](http://activitypub.rocks/) per enviar i rebre activitat d'usuari entre diferents instàncies de BookWyrm i altres serveis que implementen ActivityPub, com [Mastodon](https://joinmastodon.org/). Per manegar les dades d'un llibre, BookWyrm té molts tipus d'activitats que no formen parts de l'estàndard, però que altres instàncies de BookWyrm poden llegir.

Per veure les dades ActivityPub d'una entitat a BookWyrm (usuari, llibre, llista, etc.) pots afegir `.json` al final de l'URL. per exemple. `https://www.example.com/user/sam.json` i veure el resultat JSON al teu navegador o a través d'una petició http (per exemple, utilitzant `curl`).

## Activitats i Objectes

### Usuaris i relacions
Les interaccions entre usuaris segueixen les especificacions estandars d'ActivityPub.

- `Segueix`: sol·licita rebre les entrades d'un usuari i veure aquelles que només són accessibles per part dels seguidors
- `Accepta`: aprova un `Segueix` i finalitza la sol·licitud
- `Refusa`: denega un `Segueix`
- `Bloqueja`: impossibilita als usuaris que es vegin mútuament les entrades i l'accés de la persona bloquejada al perfil de qui l'ha bloquejat
- `Actualitza`: actualitza el perfil i configuració de l'usuari
- `Elimina`: desactiva l'usuari
- `Desfés`: desfà un `Segueix` o `Bloqueja`
- `Moure`: informa que un usuari ha canviat el seu ID i s'ha mogut a un nou servidor. La majoria del software que utilitza ActivityPub "seguirà" a l'usuari a la nova identitat. BookWyrm envia una notificació als seguidors i demana de confirmar que volen seguir l'usuari en la seva nova identitat.

### Estats
#### Tipus d'objecte

- `Nota`: En serveis com Mastodon, les `Notes` són el tipus principal d'estat. Contenen un cos del missatge, adjunts, poden fer menció a usuaris i, ser respostes altres tipus d'estat. Dins de BookWyrm, les `Notes` només poden ser creades com a missatges directes o com a respostes a altres estats.
- `Ressenya`: Una ressenya és un estat en resposta a un llibre (indicat pel camp `inReplyToBook`), el qual conté títol, cos i, una valoració numèrica entre 0 (no valorat) i 5.
- `Comentari`: Un comentari en un llibre fa referència a un llibre i té un cos del missatge.
- `Cita`: Una cita té un cos del missatge, un extracte d'un llibre i, menciona un llibre.

#### Activitats

- `Crear`: guarda un nou estat a la base de dades.

    **Nota**: BookWyrm nomès accepta activitats de `Crear` si són:

    - Missatges directes (per exemple `Notes` amb el nivell de privacitat `directe`, el qual menciona a un usuari local),
    - Relacionat amb un llibre (amb un estat personalitzat que inclogui el camp `inReplyToBook`),
    - Respostes a estats ja existents guardats a la base de dades

- `Eliminar`: Elimina un estat
- `M'agrada`: Crea un favorit a l'estat
- `Anunci`: Destaca l'estat a la línia de temps de l'actor
- `Desfer`: Desfà un `M'agrada` o un `Anunci`

### Col·leccions
Els llibres i llistats de l'usuari son representats per [`OrderedCollection`](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-orderedcollection)

#### Objectes

- `Prestatge`: Una col·lecció de llibres d'un usuari. Per defecte, tots els usuaris tenen un prestatge `per-llegir`, `llegint`, `lectura aturada` i `llegit` els quals són emprats per fer un seguiment de la seva activitat de lectura.
- `Llista`: Una col·lecció de llibres que pot contenir contribucions realitzades per altres usuaris a més a més de qui ha creat la llista.

#### Activitats

- `Create`: Afegeix un prestatge o llista a la base de dades.
- `Delete`: Elimina un prestatge o llista.
- `Add`: Afegeix un llibre al prestatge o llista.
- `Remove`: Elimina un llibre del prestatge o llista.

## Serialitzacions alternatives
Degut a que BookWyrm fa ús de tipus d'objectes personalitzats (`Ressenya`, `Comentari`, `Cita`) que no són reconeguts per l'ActiityPub, els estats són transformats a tipus estàndard quan s'envien o són llegits per serveis que no són BookWyrm. `Ressenyes` són convertides en `Article`s i, `Comentari`s i `Cites` són transformats en `Notes`, amb un enllaç al llibre i a la imatge de portada adjunta.

Això podria canviar en un futur a favor del [extended Object types](https://www.w3.org/TR/activitystreams-core/#fig-following-is-an-example-object-that-uses-the-id-and-type-properties-to-express-the-global-identifier-and-object-type) més conforme amb ActivityPub, llistat amb els principals tipus a ActivityPub.

## Creant models ActivityPub

El mode que BookWyrm envia i rep objectes ActivityPub pot ser confús per als desenvolupadors que són nous a BookWyrm. Està principalment controlat per:

* Funcions i [classes de dades](https://docs.python.org/3/library/dataclasses.html) esbossades al directori d'[activitypub](https://github.com/bookwyrm-social/bookwyrm/tree/main/bookwyrm/activitypub)
* L'[ActivitypubMixin](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L40) i els seus fills de models que són serialitzables per les peticions d'ActivityPub

### Serialitzar dades a i des de ActivityPub JSON

BookWyrm necessita saber com _serialitzar_ les dades des del model fins a un objecte ActivityPub JSON-LD.

L'arxiu `/activitypub/base_activity.py` proporciona les funcions principals que converteixen les cadenes JSON-LD d'ActivityPub en objectes de model Django utilitzables, i viceversa. Aconseguim això creant una classe de dades a `bookwyrm/activitypub`, i definint com el model ha de ser serialitzat, proporcionant un valor `activity_serializer` en el model, que apunta a la classe de dades adient. Des de `ActivityObject` s'hereda `id` i `type`, i dues _mètodes de classe_:

**`to_model`**

Aquest mètode rep una cadena JSON ActivityPub i prova de transformar-la en un objecte ActivityPub, trobant un objecte existent sempre que sigui possible. Així és com processem els objectes ActivityPub **entrants**.

**`serialize`**

Aquest mètode rep un objecte ActivityPub, i el transforma en una cadena vàlida ActivityPub JSON utilitzant les definicions dataclass. Així és com es processen els objectes ActivityPub **sortints**.

### Exemple - Usuaris

Un usuari BookWyrm [és definit a `models/user.py`](https://github.com/bookwyrm-social/bookwyrm/blob/main/bookwyrm/models/user.py):

```py
class User(OrderedCollectionPageMixin, AbstractUser):
    """a user who wants to read books"""
```
Observa que estem heretant de ("subclassing") `OrderedCollectionPageMixin`. La que, al seu torn, hereta de `ObjectMixin`, que hereta de `AvtivitypubMixin`. Això pot semblar complicat, però aquesta cadena d'herències ens permet evitar duplicar el codi a mesura que els nostres objectes ActivityPub es tornen més específics. `AbstractUser` és [un model Django destinat a ser utilitzat a una subclase](https://docs.djangoproject.com/en/5.1/topics/auth/customizing/#specifying-custom-user-model), donant-nos coses com autenticacions amb paraules de pas no visibles i nivells de permís "fora de la caixa".

Com `User` hereva de [`ObjectMixin`](https://github.com/bookwyrm-social/bookwyrm/blob/c458cdcb992a36f3c4a06752499461c3dd991e07/bookwyrm/models/activitypub_mixin.py#L213), quan `save()` un objecte `User` enviarem una activitat `Create()` (si és la primera vegada que l'usuari és guardat) o una activitat `Update` (si estem guardant un canvi - per exemple a la descripció d'usuari o l'avatar). Qualsevol altre model que afegeixis a BookWyrm tindrà la mateixa capacitat si hereta de `ObjectMixin`.

Per als usuaris de BookWyrm, la `activity_serializer` és definida al model `User`:

```py
activity_serializer = activitypub.Person
```

La definició de les dades de la classe `activitypub.Person` és a `/activitypub/person.py`:

```py
@dataclass(init=False)
class Person(ActivityObject):
    """actor activitypub json"""

    preferredUsername: str
    inbox: str
    publicKey: PublicKey
    followers: str = None
    following: str = None
    outbox: str = None
    endpoints: Dict = None
    name: str = None
    summary: str = None
    icon: Image = None
    bookwyrmUser: bool = False
    manuallyApprovesFollowers: str = False
    discoverable: str = False
    hideFollows: str = False
    movedTo: str = None
    alsoKnownAs: dict[str] = None
    type: str = "Person"
```

Potser hauràs observat que alguns dels camps no són exactament iguals que els camps del model `User`. Si tens un nom d'un camp al teu model que cal anomenar d'una manera diferent l'objecte ActivityPub (per exemple, per complir amb les convencions de nom de Python al model i a les convencions de nom JSON a una cadena JSON), pots definir un `activitypub_field` a les definicions de camps del model:

```py
followers_url = fields.CharField(max_length=255, activitypub_field="followers")
```
