# Assos Finder v1.01
### Recherche d'associations Françaises

- Permet de rechercher des associations Françaises par leurs noms, numéro de RNA ou numéro de Siret.
- Le nombre de résultats est limité à 500 (trop long au delà car 100 résultats sont renvoyés par page).
- Ajout de la foctionnalitée <Ctrl + C> pour copier la séléction souris.
- Ajout de la foctionnalitée <Ctrl + F> pour rechercher, dans le navigateur web, la séléction souris.
***
# Installation des dépendances
- <code>pip3 install -r requirements.txt</code> ou <code>pip3 install requests</code>
- Liste des modules utilisés:
```python
import tkinter as tk
from tkinter import IntVar, scrolledtext, ttk, StringVar
import requests
from sys import platform
import webbrowser
```
***
# License

 The MIT License (MIT)

Copyright © 2021 Pythony0

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the “Software”), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to 
the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
IN THE SOFTWARE.
***
# Note
- ![logo_api](./logo_api.png)
- Cette application utilise l'API ouverte : [https://api.gouv.fr/les-api/api_rna](https://api.gouv.fr/les-api/api_rna)
- Documentation de l'API : [https://entreprise.data.gouv.fr/api_doc/rna](https://entreprise.data.gouv.fr/api_doc/rna)
- ###### Cette application a été réalisée dans un but pédagogique


