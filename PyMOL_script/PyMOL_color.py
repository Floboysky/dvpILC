#!/usr/bin/env python3

import os
import json
import pandas as pd
from pymol import cmd


def color_by_residues(key, file, sele="all", grad="rainbow_rev"):
    """
    Colorie les résidus en fonction de valeurs contenues dans le fichier JSON d'ouput de Jalview ou le fichier CSV data_all.
    Can be used directly in PyMOL.
    
    Parameters:
        key: Clé dans le fichier contenant les valeurs à utiliser
        file: Chemin vers le fichier contenant les valeurs à utiliser
        sele: Sélection PyMOL à colorier (par défaut "all")
        grad: Liste des couleurs définissant le gradient (ex: "blue_white_red")
    """
    
    # Teste l'extension du fichier
    ext = os.path.splitext(file)[1].lower()
    
    if ext == ".json":
        # Charger le fichier JSON
        with open(file, 'r') as f:
            data = json.load(f)
            
        # Extraire les numéros de résidus et les valeurs associées
        nums = data["num"]
        values = data[key]
    
        # Désimbriquer les listes
        if isinstance(nums, list) and isinstance(nums[0], list):
            nums = nums[0]
        if isinstance(values, list) and isinstance(values[0], list):
            values = values[0]
            
    elif ext == ".csv":
        # Charger le fichier CSV
        data = pd.read_csv(file, sep=";", encoding="utf-8")
        
        # Extraire les colonnes
        nums = data["Position"].tolist()
        values = data[f"{key}"].tolist()
    
    else:
        raise ValueError("Format de fichier non supporté. Veuillez utiliser le fichier jalview_output.json ou data_all.csv.")
    
    # Trouver les valeurs minimales et maximales pour définir l'échelle du gradient
    min_val = min(values)
    max_val = max(values)
    if max_val == min_val:  # Éviter la division par zéro si toutes les valeurs sont identiques
        raise ValueError(f"Toutes les valeurs de '{key}' sont identiques, impossible de générer un gradient.")

    # Appliquer les couleurs aux résidus en fonction de la valeur clé
    for resi, val in zip(nums, values):
        cmd.alter(f"resi {resi} and {sele}", f"b = {val}")

    # Appliquer un gradient pré-défini à la sélection
    cmd.spectrum("b", grad, sele)


cmd.extend("color_by_residues", color_by_residues)
