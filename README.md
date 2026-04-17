![header](ILC_dev.png)
Figure adaptée de [Harly et al. 2018](https://doi.org/10.1084/jem.20170832).

---

# Influence de NFIL3 dans le développement des ILC chez la souris.

Ce dépôt contient tous les scripts et les ressources utilisés dans le papier:

Ce code source permet la caractérisation des résidus fonctionnels, l'analyse de la relation structure-fonction, ainsi que l'étude de fiabilité des potentiels partenaires protéiques du facteur de transcription NFIL3. Afin de caractériser ses mécanismes d'actions dans le développement des ILC murins.

## Installation

### Prérequis

- conda 24.11.3
- pymol 3.1.4.1

### Étapes

Dans un terminal anaconda lancer les commandes suivantes:

```bash
git clone https://github.com/Floboysky/dvpILC.git
conda env create -f environment.yml
conda activate NFIL3_ILC
```

## Description et utilisation

Le dossier `example_data` contient des exemples de données qui peuvent être manipulées par le code source. Dans tous les codes présentés ci-dessous, toutes les variables `path` et `name` peuvent être changés par l'utilisateur si besoin.

### Analyse de la conservation

Ce chapitre décrit les bonnes pratique d'utilisation des codes contenus dans le dossier `Analysis`.

L'extraction du score pLDDT est faite à partir du script `select_plddt_CA.sh`, qui prend cette donnée directement à partir des fichiers CIF obtenus avec AlphaFold3. Son utilisation ce fait automatiquement dans les fichiers `CA_bfactors_plddt.ipynb` et `conservation_nfil3.ipynb`.

- `CA_bfactors_plddt.ipynb` sert à comparer et à analyser graphiquement les scores de bfactors utilisée en cristallographie avec le score pLDDT utilisé par AlphaFold. Le fichier est divisé en deux parties, la première contenant les fonctions nécessaire au fonctionnement du code et la seconde pour générer les graphiques. Exemple de fichiers en input `example_data/MeCP2_TBL1R/fold_mmecp2_mtbl1r` (ouput de AF3) pour l'étude du pLDDT, et `example_data/MeCP2_TBL1R/Xp` pour l'étude du bfactor (PDB: 5NAF). Les exemples de fichiers output du programme sont dans le dossier `example_data/MeCP2_TBL1R/Plots`.

- `conservation.ipynb` permet une analyse graphique qui regroupe dans une dataframe (`example_data/NFIL3/Results`) les résultats de probabilité de désordre, de fiabilité, de qualité d'alignement, et de pression de conservation pour chaque résidu d'une protéine spécifique:
    - L'input pour l'étude du désordre intrinsèque est un fichier JSON obtenu via le serveur d'AIUPred (`example_data/NFIL3/AIUPred`).
    - Pour la fiabilité (pLDDT) un output de AF3 à été pris en exemple (`example_data/NFIL3/fold_mnfil3`).
    - Les statistiques d'alignement sont obtenu à partir des fichiers d'output de l'outil Jalview après un alignement global de séquences protéique. (`example_data/NFIL3/Jalview`):

        - Le fichier "jalview_files.json" via l'onglet "Files/Output to Textbox" pour les données de séquences.
        - Le fichier "jalview_annotation.csv" via l'onglet "Files/Export Annotations..." pour les données brut.

    - L'analyse de la pression de conservation à été obtenue via le programme EasyCodeML (`example_data/NFIL3/CodeML`). Pour fonctionner EasyCodeML à besoin d'un arbre phylogénétique (qui peut être obtenu via l'alignement Jalview) au format NWK, et de la correspondance des séquences protéiques alignées avec les séquences génomiques au format PAML obtenu avec le serveur PAL2NAL. Le script `clean_fasta.py` permet de nettoyer l'index des différentes séquences génomiques ainsi alignées avant leur utilisation dans EasyCodeML. Une fois fait, le script extrait les valeurs de "Postmean w" et la probalité de chaque résidu d'être dans la classe n°1 ("BEB class1").

### Analyse des interactions protéine-protéine

Ce chapitre décrit les bonnes pratique d'utilisation du code contenu dans le dossier `PPI`.

Comme pour le chapitre ["Analyse de la conservation"](#analyse-de-la-conservation), l'extraction du pLDDT est faite automatiquement avec l'aide du script `select_plddt_CA.sh`.

- `alphafold3_lis_contact.ipynb`

### Données dans BioGRID

- `data_BioGRID.py`

### Scripts utiles dans PyMOL

- `helix_axis.py`

- `PyMOL_color.py`

## Citation

```bibtex

```
