# Level02

Se connecter en tant que `level02`:

    $ ssh 192.168.1.124 -p 4242 -l level02
    level02@192.168.1.124's password: f2av5il02puano7naaf6adaaf

---

> Méthode 1

    $> ls -la
    ----r--r-- 1 flag02  level02 8302 Aug 30  2015 level02.pcap

Download le fichier en local

    $> scp -P 4242 level02@192.168.1.124:~/level02.pcap .

On ouvre le fichier pcap dans Wireshark pour l'analyser

Clique sur l'option : Analyser flux TCP

On trouve : "ft_wandr...NDRel.L0L"

En regardant les paquets qui correspondent aux lettres, on voit que le point equivaut au caractere "7f" dans la table ASCII qui est "DEL"

On les enlève et on supprime les caracteres avant ces points

Mot de passe final : "ft_waNDReL0L"

----

> Méthode 2

Container Docker Kali linux avec en volume le fichier level02.pcap

    $> docker run --rm --privileged -v `pwd`:/Ressources -ti kalilinux/kali-rolling /bin/bash
    $> apt update && apt install python2 tshark -y
    $> cd /Ressources
    $> tshark -Tfields -e data -r level02.pcap | tr -d '\n' > data

    $> cat data
    fffd25fffc25fffb26fffd18fffd20fffd23fffd27fffd24fffe26fffb18fffb20fffb23fffb27fffc24fffa2001fff0fffa2301fff0fffa2701fff0fffa1801fff0fffa200033383430302c3338343030fff0fffa2300536f646143616e3a30fff0fffa270000444953504c415901536f646143616e3a30fff0fffa1800787465726dfff0fffb03fffd01fffd22fffd1ffffb05fffd21fffd03fffc01fffb22fffa220301000003620304020f05000007621c08020409421a0a027f0b02150f02111002131102ffff1202fffffff0fffb1ffffa1f00b10031fff0fffd05fffb21fffa220103fff0fffa220107fff0fffa2103fff0fffb01fffd00fffe22fffd01fffb00fffc22fffa220303e20304820f07e21c08820409c21a0a827f0b82150f82111082131182ffff1282fffffff00d0a4c696e757820322e362e33382d382d67656e657269632d70616520283a3a666666663a31302e312e312e322920287074732f3130290d0a0a010077777762756773206c6f67696e3a206c006c6500657600766500656c006c5800580d01000d0a50617373776f72643a2066745f77616e64727f7f7f4e4452656c7f4c304c0d000d0a01000d0a4c6f67696e20696e636f72726563740d0a77777762756773206c6f67696e3a20

    $> python2
    >>> "fffd25fffc25fffb26fffd18fffd20fffd23fffd27fffd24fffe26fffb18fffb20fffb23fffb27fffc24fffa2001fff0fffa2301fff0fffa2701fff0fffa1801fff0fffa200033383430302c3338343030fff0fffa2300536f646143616e3a30fff0fffa270000444953504c415901536f646143616e3a30fff0fffa1800787465726dfff0fffb03fffd01fffd22fffd1ffffb05fffd21fffd03fffc01fffb22fffa220301000003620304020f05000007621c08020409421a0a027f0b02150f02111002131102ffff1202fffffff0fffb1ffffa1f00b10031fff0fffd05fffb21fffa220103fff0fffa220107fff0fffa2103fff0fffb01fffd00fffe22fffd01fffb00fffc22fffa220303e20304820f07e21c08820409c21a0a827f0b82150f82111082131182ffff1282fffffff00d0a4c696e757820322e362e33382d382d67656e657269632d70616520283a3a666666663a31302e312e312e322920287074732f3130290d0a0a010077777762756773206c6f67696e3a206c006c6500657600766500656c006c5800580d01000d0a50617373776f72643a2066745f77616e64727f7f7f4e4452656c7f4c304c0d000d0a01000d0a4c6f67696e20696e636f72726563740d0a77777762756773206c6f67696e3a20".decode("hex")
    '[...]Password: ft_wandr\x7f\x7f\x7fNDRel\x7fL0L\r[...] '

    ...
    	ft_wandr\x7f\x7f\x7fNDRel\x7fL0L => ft_waNDReL0L       (flag02)
    ...

On a le mot de passe

Se connecter en tant que `flag02` et récuperer le flag.

    $ su flag02
    Password: ft_waNDReL0L
    $ getflag
    Check flag.Here is your token : kooda2puivaav1idi4f57q8iq