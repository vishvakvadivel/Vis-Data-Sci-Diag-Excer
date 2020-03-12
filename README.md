# vis-data-science-diagnostic-exercise
Using a pipenv environment, write a python script to extract gene information from UniProt, perform some computations, and visualize this data.
## Assignment
1. Create pipenv python environment and install all necessary packages.
2. In main.py, import the list of UniProt ID's provided in data/uniprot_ids.csv.
3. Programmatically grab all of the relevant information pertaining to that UniProt entry. (Hint: You can access the data from the UniProt API by making an HTTP request using one of the following patterns):
    ```
   https://www.uniprot.org/uniprot/<uniprot_id>.tab
   https://www.uniprot.org/uniprot/<uniprot_id>.xml
   https://www.uniprot.org/uniprot/<uniprot_id>.fasta
   ```
3. Load this data into a Pandas DataFrame.
4. Remove or rename the columns so that the only remaining are Uniprot ID, Protein, Gene, Organism, and Length.
5. Export the DataFrame as an excel file data/unprot.xlsx,
6. Create a Boxplot that plots the "Length" for Human and Mouse entries.
7. Save the figure as plots/boxplot.png.
7. Check this repo and all files into your own github repo.
8. Email the link to your github repo to albert.hurwitz@agenusbio.com and christian.schlubach@agenusbio.com.