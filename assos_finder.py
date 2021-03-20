#!/usr/bin/python3
import tkinter as tk
from tkinter import IntVar, scrolledtext, ttk, StringVar
import requests
from sys import platform
import webbrowser

"""
RNA Croix Rouge: W9C1000188
RNA ATASLACK: W062008198
SIRET Secourisme: 48077929700013
"""
index = 0
index_page = 0
reponse = {}
liste_page = []


# Définition des fonctions
def champ_vide(*arg):
    if input_text.get() == "":
        bouton_chercher.config(state=tk.DISABLED)
        input_text.unbind("<Return>")
    else:
        bouton_chercher.config(state=tk.NORMAL)
        input_text.bind("<Return>", make_api)


def radio_selected():
    pass


def afficher():
    try:
        label_assos.config(text=reponse["association"]["titre"], fg="green")
        label_erreur.config(text="Nombre de résultats: " + str(len(reponse.keys())), fg="green")
        text = ""
        for el in reponse.items():
            for element in el[1].items():
                if element[1] is None:
                    pass
                else:
                    text += element[0].capitalize().replace("_", " ") + ":\n" + str(element[1]) + "\n\n"
        label_resultat.insert("1.0", text)
        label_resultat.config(state=tk.DISABLED)
    except TypeError:
        label_assos.config(text="Aucun résultat", fg="red")


def afficher_nom():
    global index_page
    try:
        if reponse["total_results"] == 1:
            bouton_precedent.config(state=tk.DISABLED)
            bouton_suivant.config(state=tk.DISABLED)
            index_page = 0
        elif index + index_page * 100 == 0:
            bouton_precedent.config(state=tk.DISABLED)
            bouton_suivant.config(state=tk.NORMAL)
        elif index + index_page * 100 + 1 == reponse["total_results"]:
            bouton_suivant.config(state=tk.DISABLED)
            bouton_precedent.config(state=tk.NORMAL)
        else:
            bouton_precedent.config(state=tk.NORMAL)
            bouton_suivant.config(state=tk.NORMAL)

        label_resultat.config(state=tk.NORMAL)
        label_resultat.delete("1.0", tk.END)

        if index_page == 0:
            if not reponse["association"][index]["titre_court"]:
                label_assos.config(text=reponse["association"][index]["titre"] + "\n" +
                                   str(index + 1) + "/" + str(reponse["total_results"]), fg="green")
            else:
                label_assos.config(text=reponse["association"][index]["titre_court"] + "\n" +
                                   str(index + 1) + "/" + str(reponse["total_results"]), fg="green")
            label_erreur.config(text="Nombre de résultats: " + str(reponse["total_results"]), fg="green")
            text = ""

            for element in reponse["association"][index].items():
                if element[1] is None:
                    pass
                else:
                    text += element[0].capitalize().replace("_", " ") + ":\n" + str(element[1]) + "\n\n"

            label_resultat.insert("1.0", text)
            label_resultat.config(state=tk.DISABLED)

        else:
            if not liste_page[index_page - 1]["association"][index]["titre_court"]:
                label_assos.config(text=liste_page[index_page - 1]["association"][index]["titre"] + "\n" +
                                   str(index_page * 100 + index + 1) + "/" +
                                   str(reponse["total_results"]), fg="green")
            else:
                label_assos.config(text=liste_page[index_page - 1]["association"][index]["titre_court"] + "\n" +
                                   str(index_page * 100 + index + 1) + "/" +
                                   str(reponse["total_results"]), fg="green")
            label_erreur.config(text="Nombre de résultats: " + str(reponse["total_results"]),
                                fg="green")
            text = ""

            for element in liste_page[index_page - 1]["association"][index].items():
                if element[1] is None:
                    pass
                else:
                    text += element[0].capitalize().replace("_", " ") + ":\n" + str(element[1]) + "\n\n"

            label_resultat.insert("1.0", text)
            label_resultat.config(state=tk.DISABLED)

    except TypeError:
        label_assos.config(text="Aucun résultat", fg="red")


def make_api(event):
    label_resultat.config(state=tk.NORMAL)
    label_resultat.delete("1.0", tk.END)

    if len(input_text.get()) == 0:
        label_erreur.config(text="Champ de recherche vide", fg="red")
    else:
        label_erreur.config(text="")
        url = "https://entreprise.data.gouv.fr/api/rna/v1/"

        if choix.get() == 1:
            url += "full_text/" + input_text.get()
            get_data(url)
            afficher_nom()

        elif choix.get() == 2:
            url += "id/" + input_text.get()
            get_data(url)
            afficher()

        elif choix.get() == 3:
            url += "siret/" + input_text.get()
            get_data(url)
            afficher()


def get_data(url):
    global reponse
    global liste_page
    global index
    global index_page
    index = 0
    index_page = 0
    liste_page = 0
    bouton_precedent.config(state=tk.DISABLED)
    bouton_suivant.config(state=tk.DISABLED)
    querystr = {"per_page": 100}
    try:
        reponse = requests.get(url, params=querystr)
        if reponse.status_code == 200:
            reponse = reponse.json()
            if "total_pages" in reponse.keys():
                page = reponse["total_pages"]
                if reponse["total_results"] > 500:
                    reponse["total_results"] = 500
                    page = 5
                liste_page = []
                for p in range(2, page + 1):
                    rep = requests.get(url, {"per_page": 100, "page": p})
                    rep = rep.json()
                    liste_page.append(rep)
        else:
            raise requests.exceptions.RequestException
    except requests.exceptions.RequestException:
        label_resultat.insert("1.0", "Aucun résultat pour cette recheche")
        label_assos.config(text="")
        label_resultat.config(state=tk.DISABLED)


def precedent():
    global index
    global index_page
    index -= 1
    if index < 0:
        index = 0
    if index % 100 == 0:
        index_page -= 1
        index = 99
    if index_page < 0:
        index_page = 0
        index = 0
    afficher_nom()


def suivant():
    global index
    global index_page
    index += 1
    if index % 100 == 0:
        index_page += 1
        index = 0
    afficher_nom()


def copier(*event):
    root.clipboard_clear()
    root.clipboard_append(input_text.selection_get())


# Définition de la police suvant le system
font = tuple()
font_family = ""
if platform == "linux" or platform == "linux2" or platform == "darwin":
    font = ("Quicksand", 14)
    font_family = "Quicksand"
elif platform == "win32":
    font = ("Cantarell", 14)
    font_family = "Cantarell"


# Définition de la fenetre principale
root = tk.Tk(className="Assos Finder")
root.wm_title("Assos Finder")
root.resizable(0, 0)

# Définition des layout
input_frame = tk.Frame(root)
separator = ttk.Separator(root, orient='horizontal')
output_frame = tk.Frame(root)
input_frame.pack(padx=10, pady=10)
separator.pack(fill='x')
output_frame.pack(padx=10, pady=10)

# Définition des widgets de input_frame
input_var = StringVar()
label_chercher = tk.Label(input_frame, text="Chercher par:", font=font)
choix = IntVar()
radio_nom = tk.Radiobutton(input_frame, text="Nom", variable=choix, value=1, command=radio_selected, font=font)
radio_rna = tk.Radiobutton(input_frame, text="RNA", variable=choix, value=2, command=radio_selected, font=font)
radio_siret = tk.Radiobutton(input_frame, text="Siret", variable=choix, value=3, command=radio_selected, font=font)
input_text = tk.Entry(input_frame, width=25, font=(font_family, 16), borderwidth=3, justify="center",
                      textvariable=input_var)
bouton_chercher = tk.Button(input_frame, text="Chercher", command=lambda: make_api("event"), font=font, borderwidth=3)
label_erreur = tk.Label(input_frame, text="", font=(font_family, 14), fg="red")

radio_nom.select()
input_text.focus_set()
input_var.trace_add("write", champ_vide)
bouton_chercher.config(state=tk.DISABLED)

# Placement des widgets de input_frame
label_chercher.grid(row=0, column=0)
radio_nom.grid(row=1, column=0)
radio_rna.grid(row=2, column=0)
radio_siret.grid(row=3, column=0)
bouton_chercher.grid(row=0, column=1, padx=(80, 0), ipadx=100)
input_text.grid(row=1, column=1, rowspan=3, padx=(80, 0))
label_erreur.grid(row=4, column=1, padx=(80, 0))

# Définition des widgets de output_frame
bouton_precedent = tk.Button(output_frame, text="Précédent", command=precedent, font=font, borderwidth=3)
bouton_suivant = tk.Button(output_frame, text="Suivant", command=suivant, font=font, borderwidth=3)
label_assos = tk.Label(output_frame, font=font,  wraplength=400)
label_resultat = tk.scrolledtext.ScrolledText(output_frame, font=font, width=50, height=20, wrap="word")

root.bind("<Control-c>", copier)

bouton_precedent.config(state=tk.DISABLED)
bouton_suivant.config(state=tk.DISABLED)

# Placement des widgets de output_frame
bouton_precedent.grid(row=0, column=0, padx=10, pady=(0, 10), ipadx=50)
bouton_suivant.grid(row=0, column=1, padx=10, pady=(0, 10), ipadx=60)
label_resultat.grid(row=2, column=0, columnspan=2)
label_assos.grid(row=1, column=0, columnspan=2)

root.bind("<Control-f>", lambda i: webbrowser.open("https://duckduckgo.com/?q=" + root.selection_get()))

# Main Loop
root.mainloop()
