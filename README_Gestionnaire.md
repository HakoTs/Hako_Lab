# Gestionnaire de Réalisations - Hako LAB

## Description
Cet outil vous permet de gérer facilement vos projets et réalisations sur votre site web sans avoir à toucher au code HTML.

## Fonctionnalités

### 📋 Gestion des Projets
- **Ajouter un nouveau projet** : Créez facilement de nouveaux projets avec nom et description
- **Voir tous vos projets en cours** : Liste claire de tous vos projets inachevés
- **Supprimer un projet** : Supprimez les projets que vous ne voulez plus

### ✅ Transformation en Réalisations
- **Transformer un projet en réalisation** : Interface simple pour remplir tous les détails
- **Remplissage automatique des templates HTML** : L'outil génère automatiquement les pages
- **Mise à jour automatique de la page réalisations** : Ajoute automatiquement les liens

### 🎯 Gestion des Réalisations
- **Voir toutes vos réalisations** : Liste de toutes vos réalisations terminées
- **Supprimer une réalisation** : Supprime le fichier HTML et met à jour les liens

## Comment utiliser

### 1. Lancer l'application
```bash
python gestionnaire_realisations.py
```

### 2. Ajouter un nouveau projet
1. Allez dans l'onglet "Nouveau Projet"
2. Entrez le nom et la description
3. Cliquez sur "Ajouter Projet"

### 3. Transformer un projet en réalisation
1. Allez dans l'onglet "Projets en cours"
2. Sélectionnez le projet à transformer
3. Cliquez sur "Transformer en Réalisation"
4. Remplissez le formulaire détaillé :
   - **Nom** : Nom final de la réalisation
   - **Description détaillée** : Description complète du projet
   - **Technologies** : Liste des technologies utilisées (séparées par des virgules)
   - **Fonctionnalités** : Liste des fonctionnalités principales (une par ligne)
   - **Détails techniques** : Aspects techniques intéressants
   - **Résultats** : Résultats obtenus, retours clients, etc.
   - **Lien** : Lien vers le projet en ligne (optionnel)
   - **Image** : Capture d'écran ou image du projet (optionnel)
5. Cliquez sur "Créer la Réalisation"

### 4. Gérer vos réalisations
- Allez dans l'onglet "Réalisations" pour voir toutes vos réalisations
- Vous pouvez supprimer une réalisation si nécessaire

## Ce que fait l'outil automatiquement

### ✨ Création automatique des fichiers
- Crée un nouveau fichier `realisationX.html` basé sur votre template
- Remplace automatiquement tous les placeholders avec vos informations
- Met à jour la page `realisations.html` avec le nouveau lien
- Met à jour le script JavaScript pour la fonction "réalisation aléatoire"

### 🔄 Gestion des données
- Sauvegarde toutes vos informations dans `config_realisations.json`
- Garde une trace de tous vos projets et réalisations
- Génère automatiquement les IDs uniques pour chaque réalisation

## Structure des fichiers

```
votre-site/
├── gestionnaire_realisations.py    # L'application principale
├── config_realisations.json        # Fichier de configuration (créé automatiquement)
├── realisations.html              # Page principale des réalisations (mise à jour automatiquement)
├── realisation1.html              # Template de base
├── realisation2.html              # Nouvelles réalisations créées automatiquement
├── realisation3.html              # ...
└── README_Gestionnaire.md         # Ce fichier
```

## Avantages

✅ **Aucun code à toucher** : Interface graphique simple
✅ **Automatisation complète** : Génération automatique des pages HTML
✅ **Sauvegarde des données** : Toutes vos informations sont conservées
✅ **Interface intuitive** : Formulaires clairs et boutons simples
✅ **Gestion des erreurs** : Messages d'erreur clairs en cas de problème

## Prérequis

- Python 3.6 ou plus récent
- Modules inclus : `tkinter`, `json`, `os`, `re`, `datetime`

## Support

Si vous rencontrez des problèmes :
1. Vérifiez que tous vos fichiers HTML sont dans le même dossier
2. Assurez-vous que `realisation1.html` existe (utilisé comme template)
3. Vérifiez les permissions d'écriture dans le dossier

---

**Note** : Cet outil a été conçu spécifiquement pour votre site web Hako LAB. Il utilise la structure et les templates existants de votre site.
