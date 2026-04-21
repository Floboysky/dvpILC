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

L'extraction du score pLDDT est faite à partir du script `select_plddt_CA.sh`, qui prend cette donnée directement à partir des fichiers CIF obtenus avec AlphaFold3. Son utilisation se fait automatiquement dans les fichiers `CA_bfactors_plddt.ipynb` et `conservation_nfil3.ipynb`, et doit être situé dans leur dossier parent.

- `CA_bfactors_plddt.ipynb` sert à comparer et à analyser graphiquement les scores de bfactors utilisée en cristallographie avec le score pLDDT utilisé par AlphaFold. Le fichier est divisé en deux parties, la première contenant les fonctions nécessaire au fonctionnement du code et la seconde pour générer les graphiques. Exemple de fichiers à mettre en input pour l'étude du pLDDT (ouput de AF3 dans `example_data/MeCP2_TBL1R/fold_mmecp2_mtbl1r`), et pour l'étude du bfactor (PDB:5NAF dans `example_data/MeCP2_TBL1R/Xp`). Les exemples de graphiques obtenus sont dans le dossier `example_data/MeCP2_TBL1R/Plots`.

- `conservation.ipynb` permet une analyse graphique qui regroupe dans une dataframe (`example_data/NFIL3/Results`) les résultats de probabilité de désordre, de fiabilité, de qualité d'alignement, et de pression de conservation pour chaque résidu d'une protéine spécifique:
    - L'input pour l'étude du désordre intrinsèque est un fichier JSON obtenu via le serveur d'AIUPred (`example_data/NFIL3/AIUPred`).
    - Pour la fiabilité (pLDDT), un output de AF3 à été pris en exemple (`example_data/NFIL3/fold_mnfil3`).
    - Les statistiques d'alignements sont obtenu à partir des fichiers d'output de l'outil Jalview après un alignement global de séquences protéiques. (`example_data/NFIL3/Jalview`):

        - Le fichier "jalview_files.json" via l'onglet "Files/Output to Textbox" pour les données de séquences.
        - Le fichier "jalview_annotation.csv" via l'onglet "Files/Export Annotations..." pour les données brut.

    - L'analyse de la pression de conservation à été obtenue via le programme EasyCodeML (`example_data/NFIL3/CodeML`). Pour fonctionner EasyCodeML à besoin au format FASTA de l'alignement protéique, de l'arbre phylogénétique de ceui-ci au format NWK (obtenu dans Jalview), et de la correspondance des séquences protéiques alignées avec les séquences génomiques au format PAML (obtenu avec le serveur PAL2NAL). Le script `clean_fasta.py` permet de nettoyer l'index des différentes séquences génomiques ainsi alignées avant leur utilisation dans EasyCodeML. Pour chaque site extrait d'EasyCodeML dans le model 8 (M8) obtenu avec l'option "Site Model", le script extrait l'estimation de omega, son incertitude ainsi que sa probalité d'être dans la classe n°1.

### Analyse des interactions protéine-protéine

Ce chapitre décrit les bonnes pratiques d'utilisation du code contenu dans le dossier `PPI`.

Comme pour le chapitre ["Analyse de la conservation"](#analyse-de-la-conservation), l'extraction du pLDDT est automatiquement faite avec l'aide du script `select_plddt_CA.sh`. Il est utilisé par le script `alphafold3_lis_contact.ipynb`, et doit être placé dans son dossier parent.

- `alphafold3_lis_contact.ipynb`: est un programme adapté de [Kim et al. 2024](http://biorxiv.org/lookup/doi/10.1101/2024.02.19.580970), pour l'analyse des scores de PAE, iPTM, LIS, cLIS et LIA d'un complexe de deux protéines obtenu par AlphaFold3. Un exemple de donnée d'input a été placé dans le dossier `example_data/NFIL3_TBL1R`. Ce programme est aussi capable de fournir un graphique des pLDDT des carbones alpha pour tous les résidus, ainsi que les graphiques des valeurs de LIS et cLIS pour les résidus positifs (valeur max et moyenne) de chaque chaine du complexe. La sortie du programme est un fichier CSV contenant les résidus avec au moins une valeur de LIS ou de cLIS positive pour chaque protéine.

### Données dans BioGRID

- `data_BioGRID.py`

### Scripts utiles dans PyMOL

- `helix_axis.py`

- `PyMOL_color.py`

## Citation

```bibtex

```
