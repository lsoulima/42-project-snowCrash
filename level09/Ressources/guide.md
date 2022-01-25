# Level09

Se connecter en tant que `level09`:

    $ ssh 192.168.1.124 -p 4242 -l level09
    password: 25749xKZ8L7DkSCwJkT9dyv6f

---

Premiere étape de recherche

    $ ls -la
    -rwsr-sr-x 1 flag09  level09 7640 Mar  5  2016 level09
    ----r--r-- 1 flag09  level09   26 Mar  5  2016 token

On trouve un binaire setuid et un fichier token

    $ ./level09
    You need to provied only one arg.

    $ ./level09 token
    tpmhr

    $ ./level09 abcdefghij
    acegikmoqs

Le programme fait un hash sur le parametre

    $ cat token
    f4kmm6p|=�p�n��DB�Du{��

Le token a surement été fait avec ce programme de hash

    $ ./level09 $(cat token)
    f5mpq;v�E��{�{��TS�W�����

Rien de bien intéressant...

Étudions un peu mieux le programme de hash

    $ ./level09 1
    1

    $ ./level09 11
    12

    $ ./level09 111
    123

    $ ./level09 1111
    1234

    $ ./level09 11111
    12345

Le programme décale chaque caractere par son index et l'affiche. On va donc devoir faire l'inverse avec notre token

Pour rendre le token lisible il nous suffit alors de faire l'inverse du binaire level09 avec un script `flag09` en C ce sera plus simple:

```c
#include <unistd.h>

int main(int ac, char** av) {
	char* s = av[1];

	int i = 0;
	while (s[i] != 0) {
		char tmp = s[i] - i;
		write(1, &tmp, 1);
		i++;
	}
	write(1, "\n", 1);
	return 0;
}
```

    $ scp -P 4242 flag09.c level09@192.168.1.124:/tmp
    $ gcc /tmp/flag09.c -o /tmp/flag09
    $ /tmp/flag09 `cat token`
    f3iji1ju5yuevaus41q1afiuq
    $ su flag09
    Password:
    Don't forget to launch getflag !
    $ getflag
    Check flag.Here is your token : s5cAJpM8ev6XHw998pRWG728z
