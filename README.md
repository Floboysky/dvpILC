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

Dans tous les codes présentés ci-dessous, toutes les variables `path` et `name` peuvent être changés par l'utilisateur si besoin.

### Analyse de la conservation

Ce chapitre décrit les bonnes pratique d'utilisation des codes contenus dans le dossier `Analysis`.
L'extraction du score pLDDT est faite içi à partir du code `select_plddt_CA.sh`, qui prend cette donnée directement à partir des fichiers CIF obtenus avec AlphaFold3. L'utilisation de ce script se fait automatiquement dans les fichiers `CA_bfactors_plddt.ipynb` et `conservation_nfil3.ipynb`.

- `CA_bfactors_plddt.ipynb` sert à comparer et à analyser graphiquement les scores de bfactors utilisée en cristallographie avec le score pLDDT utilisé par AlphaFold. Le fichier est divisé en deux parties, la première contenant les fonctions nécessaire au fonctionnement du code et l'autre pour générer les graphiques.

- `conservation_nfil3.ipynb` permet une analyse graphique qui regroupe dans une dataframe les résultats de désordre (AIUPred), de fiabilité (pLDDT), de qualité d'alignement (Jalview), et de pression de conservation (rapport omega) pour une protéine donnée.

- `clean_fasta.py` est le code permettant de nettoyer l'index des différentes séquences génomiques générés par PAL2NAL, pour une utilisation dans EasyCodeML, afin d'étudier la pression de conservation subie par chaque résidu d'une protéine au cours de l'évolution.

### Analyse des interactions protéine-protéine



### Scripts utiles dans PyMOL



## Citation

```bibtex

```
