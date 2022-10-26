# grumble-solver

Solver for the french game [grumble.fr](https://www.grumble.fr/)

Please don't mind the dirty code. That was more a proof of concept than anything serious. Nevertheless, feel free to improve the code if you feel like it (there's plenty of space for optimization!)

I only have tested on Linux, but this should work flawlessly on windows if you [install the `grep` command](https://gnuwin32.sourceforge.net/packages/grep.htm). (Yeah, code is nasty...)

### Requirements : 
- Python 3+
- Python module `numpy`

### Usage :

Put all letters in sequence, between quotes as first argument of `grumble.py`

Example usage : 
```bash
$ python3 grumble.py "eiiolasventrsjlc"

[...]
21 enjoliverai
21 enjolivâtes
22 javellisions
22 injectives
22 enjoliverais
22 enjoliverait
23 javelliserons
23 javelliseront
24 javelliserions
```

> Note : Credits to [hbenbel's github](https://github.com/hbenbel/French-Dictionary.git) for the french dictionary file `dictionnary.csv`