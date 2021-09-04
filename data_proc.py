import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

from rich.console import Console
from rich.table import Table

df = pd.read_csv('Data/raw/drug.csv', usecols=["smiles"])
pd.DataFrame(pd.unique(df['smiles']),columns = ['1'])['1'].to_csv(r'Data/interim/drug.txt', header=None, index=None, sep='\n', mode='w')
drug = pd.unique(df['smiles'])

df = pd.read_csv('Data/raw/drug_like.tsv', delimiter='\t', usecols=["smiles string"])
pd.DataFrame(pd.unique(df['smiles string']),columns = ['1'])['1'].to_csv(r'Data/interim/drug_like.txt', header=None, index=None, sep='\n', mode='w')
drug_like = pd.unique(df['smiles string'])

df = pd.read_csv('Data/raw/non_drug.csv', usecols=["smiles"])
pd.DataFrame(pd.unique(df['smiles']),columns = ['1'])['1'].to_csv(r'Data/interim/non_drug.txt', header=None, index=None, sep='\n', mode='w')
non_drug = pd.unique(df['smiles'])

filenames = ['Data/interim/drug.txt', 'Data/interim/drug_like.txt', 'Data/interim/non_drug.txt']
  
d    = pd.DataFrame(drug)
dl   = pd.DataFrame(drug_like)
nd   = pd.DataFrame(non_drug)
Y_d  = pd.DataFrame([0 for _ in range(len(drug))])
Y_dl = pd.DataFrame([1 for _ in range(len(drug_like))])
Y_nd = pd.DataFrame([2 for _ in range(len(non_drug))])

a1 = pd.concat([d, Y_d], axis=1)
a2 = pd.concat([dl, Y_dl], axis=1)
a3 = pd.concat([nd, Y_nd], axis=1)
final = pd.concat([a1, a2, a3])
final.columns = ['smiles', 'label']

X_train, X_test, y_train, y_test = train_test_split(
    final['smiles'], final['label'], test_size = 0.33,  shuffle = True, random_state = 42)

X_train.to_pickle('Data/processed/X_train.pkl')
y_train.to_pickle('Data/processed/y_train.pkl')
X_test.to_pickle('Data/processed/X_test.pkl')
y_test.to_pickle('Data/processed/y_test.pkl')

console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("Index No.", style="dim", justify="center", width=5)
table.add_column("Dataset")
table.add_column("Total No. of Unique SMILES", justify="right")

table.add_row(
    "1", 
    "[red]Drug[/red]", 
    f"{len(drug)}", 
)
table.add_row(
    "2",
    "[red]Drug-Like[/red]",
    f"{len(drug_like)}",
)
table.add_row(
    "3",
    "[red]Non-Drug[/red]",
    f"{len(non_drug)}",
)
table.add_row(
    "4",
    "[red]Total[/red]",
    f"{len(non_drug)+len(drug_like)+len(drug)}",
)
console.print(table)

console = Console()
table = Table(show_header=True, header_style="bold magenta")
table.add_column("")
table.add_column("Total")
table.add_column("Train Set")
table.add_column("Test Set")
table.add_column("Validation Set")


table.add_row(
    "[red]Drug[/red]", 
    f"{len(drug)}", 
    f"{len(y_train[y_train == 0])}",
    f"{len(y_test[y_test == 0])}",
    "0"
)
table.add_row(
    "[red]Drug-Like[/red]",
    f"{len(drug_like)}",
    f"{len(y_train[y_train == 1])}",
    f"{len(y_test[y_test == 1])}",
    "0"
)
table.add_row(
    "[red]Non-Drug[/red]",
    f"{len(non_drug)}",
    f"{len(y_train[y_train == 2])}",
    f"{len(y_test[y_test == 2])}",
    "0"
)
table.add_row(
    "[red]Total[/red]",
    f"{len(non_drug)+len(drug_like)+len(drug)}",
    f"{len(y_train)}",
    f"{len(y_test)}",
    "0"
)
console.print(table)
