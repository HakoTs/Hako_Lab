#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestionnaire de Réalisations - Hako LAB
Outil pour automatiser la gestion des projets et réalisations du site web
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os
import re
import json
from datetime import datetime

class GestionnaireRealisations:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestionnaire de Réalisations - Hako LAB")
        self.root.geometry("800x600")
        
        # Chemin du site web
        self.site_path = os.path.dirname(os.path.abspath(__file__))
        
        # Configuration
        self.config_file = os.path.join(self.site_path, "config_realisations.json")
        self.load_config()
        
        self.setup_ui()
        
    def load_config(self):
        """Charge la configuration depuis le fichier JSON"""
        default_config = {
            "projets": [],
            "realisations": [],
            "next_realisation_id": 2
        }
        
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    self.config = json.load(f)
            except:
                self.config = default_config
        else:
            self.config = default_config
            
    def save_config(self):
        """Sauvegarde la configuration dans le fichier JSON"""
        with open(self.config_file, 'w', encoding='utf-8') as f:
            json.dump(self.config, f, indent=2, ensure_ascii=False)
            
    def setup_ui(self):
        """Configure l'interface utilisateur"""
        # Notebook pour les onglets
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Onglet Projets
        self.projets_frame = ttk.Frame(notebook)
        notebook.add(self.projets_frame, text="Projets en cours")
        self.setup_projets_tab()
        
        # Onglet Réalisations
        self.realisations_frame = ttk.Frame(notebook)
        notebook.add(self.realisations_frame, text="Réalisations")
        self.setup_realisations_tab()
        
        # Onglet Nouveau Projet
        self.nouveau_frame = ttk.Frame(notebook)
        notebook.add(self.nouveau_frame, text="Nouveau Projet")
        self.setup_nouveau_tab()
        
    def setup_projets_tab(self):
        """Configure l'onglet des projets"""
        # Liste des projets
        ttk.Label(self.projets_frame, text="Projets en cours:", font=("Arial", 12, "bold")).pack(pady=10)
        
        self.projets_listbox = tk.Listbox(self.projets_frame, height=10)
        self.projets_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Boutons
        buttons_frame = ttk.Frame(self.projets_frame)
        buttons_frame.pack(pady=10)
        
        ttk.Button(buttons_frame, text="Transformer en Réalisation", 
                  command=self.transformer_en_realisation).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Supprimer Projet", 
                  command=self.supprimer_projet).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Actualiser", 
                  command=self.actualiser_listes).pack(side=tk.LEFT, padx=5)
        
    def setup_realisations_tab(self):
        """Configure l'onglet des réalisations"""
        ttk.Label(self.realisations_frame, text="Réalisations terminées:", font=("Arial", 12, "bold")).pack(pady=10)
        
        self.realisations_listbox = tk.Listbox(self.realisations_frame, height=10)
        self.realisations_listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Boutons
        buttons_frame = ttk.Frame(self.realisations_frame)
        buttons_frame.pack(pady=10)
        
        ttk.Button(buttons_frame, text="Modifier Réalisation", 
                  command=self.modifier_realisation).pack(side=tk.LEFT, padx=5)
        ttk.Button(buttons_frame, text="Supprimer Réalisation", 
                  command=self.supprimer_realisation).pack(side=tk.LEFT, padx=5)
        
    def setup_nouveau_tab(self):
        """Configure l'onglet nouveau projet"""
        ttk.Label(self.nouveau_frame, text="Ajouter un nouveau projet:", font=("Arial", 12, "bold")).pack(pady=10)
        
        # Formulaire
        form_frame = ttk.Frame(self.nouveau_frame)
        form_frame.pack(padx=20, pady=10, fill=tk.X)
        
        ttk.Label(form_frame, text="Nom du projet:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.nom_entry = ttk.Entry(form_frame, width=50)
        self.nom_entry.grid(row=0, column=1, pady=5, padx=10)
        
        ttk.Label(form_frame, text="Description courte:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.desc_entry = ttk.Entry(form_frame, width=50)
        self.desc_entry.grid(row=1, column=1, pady=5, padx=10)
        
        ttk.Button(form_frame, text="Ajouter Projet", 
                  command=self.ajouter_projet).grid(row=2, column=1, pady=20)
        
        self.actualiser_listes()
        
    def actualiser_listes(self):
        """Actualise les listes de projets et réalisations"""
        # Vider les listes
        self.projets_listbox.delete(0, tk.END)
        self.realisations_listbox.delete(0, tk.END)
        
        # Remplir la liste des projets
        for projet in self.config.get("projets", []):
            self.projets_listbox.insert(tk.END, f"{projet['nom']} - {projet['description']}")
            
        # Remplir la liste des réalisations
        for realisation in self.config.get("realisations", []):
            self.realisations_listbox.insert(tk.END, f"{realisation['nom']} - {realisation['description']}")
            
    def ajouter_projet(self):
        """Ajoute un nouveau projet"""
        nom = self.nom_entry.get().strip()
        desc = self.desc_entry.get().strip()
        
        if not nom:
            messagebox.showerror("Erreur", "Le nom du projet est obligatoire")
            return
            
        projet = {
            "nom": nom,
            "description": desc or "Nouveau projet",
            "date_creation": datetime.now().isoformat()
        }
        
        self.config.setdefault("projets", []).append(projet)
        self.save_config()
        
        # Vider les champs
        self.nom_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        
        self.actualiser_listes()
        messagebox.showinfo("Succès", f"Projet '{nom}' ajouté avec succès!")
        
    def transformer_en_realisation(self):
        """Transforme un projet en réalisation"""
        selection = self.projets_listbox.curselection()
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner un projet")
            return
            
        index = selection[0]
        projet = self.config["projets"][index]
        
        # Ouvrir la fenêtre de saisie des détails
        self.ouvrir_fenetre_realisation(projet, index)
        
    def ouvrir_fenetre_realisation(self, projet, projet_index):
        """Ouvre la fenêtre pour saisir les détails de la réalisation"""
        fenetre = tk.Toplevel(self.root)
        fenetre.title(f"Transformer '{projet['nom']}' en réalisation")
        fenetre.geometry("600x700")
        fenetre.grab_set()
        
        # Formulaire détaillé
        main_frame = ttk.Frame(fenetre)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Titre
        ttk.Label(main_frame, text="Détails de la réalisation", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Nom
        ttk.Label(main_frame, text="Nom de la réalisation:").pack(anchor=tk.W)
        nom_var = tk.StringVar(value=projet['nom'])
        ttk.Entry(main_frame, textvariable=nom_var, width=60).pack(fill=tk.X, pady=5)
        
        # Description
        ttk.Label(main_frame, text="Description détaillée:").pack(anchor=tk.W, pady=(10,0))
        desc_text = tk.Text(main_frame, height=4, width=60)
        desc_text.pack(fill=tk.X, pady=5)
        desc_text.insert(tk.END, projet.get('description', ''))
        
        # Technologies
        ttk.Label(main_frame, text="Technologies utilisées (séparées par des virgules):").pack(anchor=tk.W, pady=(10,0))
        tech_var = tk.StringVar(value="HTML, CSS, JavaScript")
        ttk.Entry(main_frame, textvariable=tech_var, width=60).pack(fill=tk.X, pady=5)
        
        # Fonctionnalités
        ttk.Label(main_frame, text="Fonctionnalités clés (une par ligne):").pack(anchor=tk.W, pady=(10,0))
        fonc_text = tk.Text(main_frame, height=4, width=60)
        fonc_text.pack(fill=tk.X, pady=5)
        
        # Détails techniques
        ttk.Label(main_frame, text="Détails techniques:").pack(anchor=tk.W, pady=(10,0))
        tech_details_text = tk.Text(main_frame, height=3, width=60)
        tech_details_text.pack(fill=tk.X, pady=5)
        
        # Résultats
        ttk.Label(main_frame, text="Résultats obtenus:").pack(anchor=tk.W, pady=(10,0))
        resultats_text = tk.Text(main_frame, height=3, width=60)
        resultats_text.pack(fill=tk.X, pady=5)
        
        # Lien projet
        ttk.Label(main_frame, text="Lien vers le projet (optionnel):").pack(anchor=tk.W, pady=(10,0))
        lien_var = tk.StringVar()
        ttk.Entry(main_frame, textvariable=lien_var, width=60).pack(fill=tk.X, pady=5)
        
        # Image
        ttk.Label(main_frame, text="Chemin vers l'image (optionnel):").pack(anchor=tk.W, pady=(10,0))
        image_frame = ttk.Frame(main_frame)
        image_frame.pack(fill=tk.X, pady=5)
        image_var = tk.StringVar()
        ttk.Entry(image_frame, textvariable=image_var, width=50).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(image_frame, text="Parcourir", 
                  command=lambda: self.choisir_image(image_var)).pack(side=tk.RIGHT, padx=(5,0))
        
        # Boutons
        buttons_frame = ttk.Frame(main_frame)
        buttons_frame.pack(pady=20)
        
        ttk.Button(buttons_frame, text="Créer la Réalisation", 
                  command=lambda: self.creer_realisation(
                      fenetre, projet, projet_index, nom_var.get(),
                      desc_text.get(1.0, tk.END).strip(),
                      tech_var.get(),
                      fonc_text.get(1.0, tk.END).strip(),
                      tech_details_text.get(1.0, tk.END).strip(),
                      resultats_text.get(1.0, tk.END).strip(),
                      lien_var.get(),
                      image_var.get()
                  )).pack(side=tk.LEFT, padx=5)
        
        ttk.Button(buttons_frame, text="Annuler", 
                  command=fenetre.destroy).pack(side=tk.LEFT, padx=5)
    
    def choisir_image(self, image_var):
        """Ouvre un dialogue pour choisir une image"""
        filename = filedialog.askopenfilename(
            title="Choisir une image",
            filetypes=[("Images", "*.jpg *.jpeg *.png *.gif *.bmp")]
        )
        if filename:
            image_var.set(filename)
    
    def creer_realisation(self, fenetre, projet, projet_index, nom, description, 
                         technologies, fonctionnalites, details_tech, resultats, lien, image):
        """Crée une nouvelle réalisation"""
        if not nom.strip():
            messagebox.showerror("Erreur", "Le nom est obligatoire")
            return
        
        # Générer l'ID de la réalisation
        realisation_id = self.config.get("next_realisation_id", 2)
        
        # Créer l'objet réalisation
        realisation = {
            "id": realisation_id,
            "nom": nom,
            "description": description,
            "technologies": [t.strip() for t in technologies.split(',') if t.strip()],
            "fonctionnalites": [f.strip() for f in fonctionnalites.split('\n') if f.strip()],
            "details_techniques": details_tech,
            "resultats": resultats,
            "lien": lien,
            "image": image,
            "date_creation": datetime.now().isoformat()
        }
        
        try:
            # Créer le fichier HTML de la réalisation
            self.creer_fichier_realisation(realisation)
            
            # Mettre à jour la page des réalisations
            self.mettre_a_jour_page_realisations(realisation)
            
            # Ajouter à la config et supprimer le projet
            self.config.setdefault("realisations", []).append(realisation)
            del self.config["projets"][projet_index]
            self.config["next_realisation_id"] = realisation_id + 1
            
            self.save_config()
            self.actualiser_listes()
            
            fenetre.destroy()
            messagebox.showinfo("Succès", f"Réalisation '{nom}' créée avec succès!")
            
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur lors de la création: {str(e)}")
    
    def creer_fichier_realisation(self, realisation):
        """Crée le fichier HTML de la réalisation"""
        template_path = os.path.join(self.site_path, "realisation1.html")
        nouveau_fichier = os.path.join(self.site_path, f"realisation{realisation['id']}.html")
        
        # Lire le template
        with open(template_path, 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        # Remplacer les placeholders
        contenu = contenu.replace("Réalisation [N°]", f"Réalisation {realisation['id']} - {realisation['nom']}")
        
        # Technologies
        tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in realisation['technologies']])
        contenu = re.sub(r'<span class="tech-tag">.*?</span>', '', contenu)
        contenu = contenu.replace('<!-- Modifier les tags techno ici -->', tech_tags)
        
        # Image
        if realisation['image']:
            contenu = contenu.replace('src="lien-vers-image.jpg"', f'src="{realisation["image"]}"')
            contenu = contenu.replace('alt="Capture de la réalisation"', f'alt="{realisation["nom"]}"')
        
        # Description
        contenu = contenu.replace(
            '[Insérez ici une description détaillée du projet. Parlez des objectifs, du contexte, des défis rencontrés et des solutions apportées.]',
            realisation['description']
        )
        
        # Fonctionnalités
        if realisation['fonctionnalites']:
            fonc_html = '\n'.join([f'        <li>{fonc}</li>' for fonc in realisation['fonctionnalites']])
            contenu = re.sub(r'<li>Fonctionnalité \d+</li>', '', contenu)
            contenu = contenu.replace('<!-- Modifier les fonctionnalités ici -->', fonc_html)
        
        # Détails techniques
        if realisation['details_techniques']:
            contenu = contenu.replace(
                '[Décrivez ici les aspects techniques intéressants, les technologies utilisées, les choix d\'architecture, etc.]',
                realisation['details_techniques']
            )
        
        # Résultats
        if realisation['resultats']:
            contenu = contenu.replace(
                '[Décrivez les résultats obtenus, les retours clients, les statistiques d\'utilisation si disponibles, etc.]',
                realisation['resultats']
            )
        
        # Lien
        if realisation['lien']:
            contenu = contenu.replace('href="#"', f'href="{realisation["lien"]}"')
        
        # Écrire le nouveau fichier
        with open(nouveau_fichier, 'w', encoding='utf-8') as f:
            f.write(contenu)
    
    def mettre_a_jour_page_realisations(self, realisation):
        """Met à jour la page des réalisations avec le nouveau lien"""
        realisations_path = os.path.join(self.site_path, "realisations.html")
        
        with open(realisations_path, 'r', encoding='utf-8') as f:
            contenu = f.read()
        
        # Ajouter le nouveau lien dans la liste
        nouveau_lien = f'        <li><a href="realisation{realisation["id"]}.html">{realisation["nom"]}</a></li>'
        
        # Trouver la position d'insertion (avant </ul>)
        pattern = r'(.*<ul>.*?)(\n\s*</ul>)'
        match = re.search(pattern, contenu, re.DOTALL)
        if match:
            avant = match.group(1)
            apres = match.group(2)
            contenu = avant + '\n' + nouveau_lien + apres
        
        # Mettre à jour le script JavaScript
        js_pattern = r'(const realisations = \[)(.*?)(\];)'
        js_match = re.search(js_pattern, contenu, re.DOTALL)
        if js_match:
            avant_js = js_match.group(1)
            contenu_js = js_match.group(2)
            apres_js = js_match.group(3)
            
            nouveau_item = f'"realisation{realisation["id"]}.html"'
            if contenu_js.strip():
                nouveau_contenu_js = contenu_js.rstrip() + ',\n        ' + nouveau_item
            else:
                nouveau_contenu_js = '\n        ' + nouveau_item + '\n      '
            
            contenu = avant_js + nouveau_contenu_js + apres_js
        
        with open(realisations_path, 'w', encoding='utf-8') as f:
            f.write(contenu)
    
    def supprimer_projet(self):
        """Supprime un projet sélectionné"""
        selection = self.projets_listbox.curselection()
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner un projet")
            return
        
        if messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer ce projet ?"):
            index = selection[0]
            del self.config["projets"][index]
            self.save_config()
            self.actualiser_listes()
    
    def modifier_realisation(self):
        """Modifie une réalisation existante"""
        selection = self.realisations_listbox.curselection()
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner une réalisation")
            return
        
        messagebox.showinfo("Info", "Fonctionnalité à venir dans une prochaine version")
    
    def supprimer_realisation(self):
        """Supprime une réalisation"""
        selection = self.realisations_listbox.curselection()
        if not selection:
            messagebox.showerror("Erreur", "Veuillez sélectionner une réalisation")
            return
        
        if messagebox.askyesno("Confirmation", "Êtes-vous sûr de vouloir supprimer cette réalisation ?"):
            index = selection[0]
            realisation = self.config["realisations"][index]
            
            # Supprimer le fichier HTML
            fichier_html = os.path.join(self.site_path, f"realisation{realisation['id']}.html")
            if os.path.exists(fichier_html):
                os.remove(fichier_html)
            
            # Supprimer de la config
            del self.config["realisations"][index]
            self.save_config()
            self.actualiser_listes()
            
            messagebox.showinfo("Succès", "Réalisation supprimée")
    
    def run(self):
        """Lance l'application"""
        self.root.mainloop()

if __name__ == "__main__":
    app = GestionnaireRealisations()
    app.run()
