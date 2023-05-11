---
Title: Management Commands
Date: 2023-04-26
Order: 11
---

In the `bookwyrm/management/commands` directory there are some commands to manipulate the instance’s database. Some of them are documented here.

## Merging objects

Quite often an instance will end up with duplicate books and authors or editions that appear as separate books when they are actually just different editions of the same work. This can happen because of importing editions that don’t have shared identifiers or from user mistakes. Sadly there’s no user interface to correct this for the time being, but in cases where the books are important for your instance you can use these management commands to fix some of the problems if you are using at least version 0.6.2.

Please take extra care when using these commands because if you make a mistake there’s no way to undo it.

### Merging editions

If an edition of a book appears twice in the database and you are sure they are actually both referring to same edition, you can combine them into one with a command like this:

```
./bw-dev runweb python manage.py merge_editions --canonical=27 --other=38
```

This will copy any missing information from edition 38 (the “other” edition) over to edition 27 (the “canonical” edition) and then delete the other edition. If any field of information is in both editions then the data from the canonical edition will be kept. If the other edition is in any lists or has any comments or reviews etc then these will all be updated to point to the canonical edition instead.

You can find the numbers to use in the command by visiting the page for a book and looking at the number in the URL.

### Merging authors

Similarly if an author is duplicated, you can combine the two authors into one with a command like this:

```
./bw-dev runweb python manage.py merge_authors --canonical=7 --other=46
```

As for the editions, any extra information from the other author will be copied over to the canonical author and then the other author will be deleted. Any books written by the other author will be changed to be written by the canonical author. You can find the numbers to use in the command by visiting the page for an author and looking at the number in the URL.
