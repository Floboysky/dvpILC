![header](ILC_dev.png)
Figure adaptée de [Harly et al. 2018](https://doi.org/10.1084/jem.20170832).

---

# Influence de NFIL3 dans le développement des ILC chez la souris.

Code source utilisé dans le papier: 

## Description

Ce dépôt contient les scripts et les ressources utilisés pour générer les graphiques, et les hypothèses effectués dans l'article ci-dessus.

Il permet la caractérisation des domaines et résidus fonctionnels, l'analyse de la relation structure-fonction, ainsi que l'étude des potentiels partenaires protéiques du facteur de transcription NFIL3 dans le développement des ILC murins.

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

## Utilisation 

### Analyse de la conservation

Le score pLDDT est une mesure de confiance locale par résidus (Carbone alpha). Son étude est primordiale pour identifier les régions structurellement fiables et/ou flexible d'une protéine. Son extraction est faite à partir du code `select_plddt_CA.sh`, qui permet de prendre cette donnée directement à partir des fichiers CIF obtenus avec AlphaFold3. L'utilisation de ce scrpit se fait automatiquement dans les fichiers `CA_bfactors_plddt.ipynb` et `conservation_nfil3.ipynb`: 

- `CA_bfactors_plddt.ipynb` sert à comparer et afficher les scores de bfactors qui mesure le déplacement atomique utilisée en cristallographie avec le score pLDDT utilisé par AlphaFold. 

- `conservation_nfil3.ipynb` regroupe dans une dataframe les résultats de désordre (AIUPred), de fiabilité (AF3 pLDDT), de qualité d'alignement (Jalview), et de pression de conservation (rapport omega) pour une protéine particulière. Afin de permettre une analyse graphique de ces différents paramètres.

### Analyse des interactions protéine-protéine



### Scripts utiles dans PyMOL



## Citation

```bibtex

```
