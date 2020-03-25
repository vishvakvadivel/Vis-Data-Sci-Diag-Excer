import csv
import pandas as pd
import requests
import matplotlib.pyplot as plt
import seaborn as sns
from tqdm import tqdm

pd.options.display.max_columns = 10

# import the list of UniProt ID's provided in data/uniprot_ids.csv.
uniprot = pd.read_csv('data/uniprot_ids.csv', header=None, na_values = '|').dropna()
uniprot.head()


cols = ['Uniprot ID','Entry name','Status','Protein','Gene','Organism','Length']

# Programmatically grab all of the relevant information pertaining to that UniProt entry.
out = []
for item in tqdm(uniprot[0]):
    url = 'https://www.uniprot.org/uniprot/{0}.tab'.format(item)
    res = requests.get(url)
    text = res.text
    info = text.split('\n')[1].split('\t')
    out.append(info)

# Load this data into a Pandas DataFrame
df = pd.DataFrame(out, columns=cols)
df.head()

# Remove or rename the columns so that the only remaining are Uniprot ID, 
# Protein, Gene, Organism, and Length.
df = df.drop(columns=['Entry name','Status'])
df.head()

# Export the DataFrame as an excel file data/unprot.xlsx
df.to_excel("data/unprot.xlsx")


#Create a Boxplot that plots the "Length" for Human and Mouse entries.
df['Organism'].value_counts()
df['Length'] = df['Length'].astype(int)
sns.boxplot(x='Organism', y='Length', data=df)

#Save the figure as plots/boxplot.png.
plt.savefig('plots/boxplot.png')

print ("Boxplot of data created")


