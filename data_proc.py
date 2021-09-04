import pandas as pd
df = pd.read_csv('Data/raw/drug_like.tsv', delimiter='\t', usecols=["smiles string"])
pd.DataFrame(pd.unique(df['smiles string']),columns = ['1'])['1'].to_csv(r'Data/interim/drug_like.txt', header=None, index=None, sep='\n', mode='w')

df = pd.read_csv('Data/raw/drug.csv')['smiles']
drug = len(pd.unique(df))

df = pd.read_csv('Data/raw/drug_like.tsv', delimiter='\t')["smiles string"]
drug_like = len(pd.unique(df))

df = pd.read_csv('Data/raw/non_drug.csv')['smiles']
non_drug = len(pd.unique(df))

from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")

table.add_column("Index No.", style="dim", justify="center", width=5)
table.add_column("Dataset")
table.add_column("Total No. of Unique SMILES", justify="right", width=35)

table.add_row(
    "1", 
    "[red]Drug[/red]", 
    f"{drug}", 
)
table.add_row(
    "2",
    "[red]Drug-Like[/red]",
    f"{drug_like}",
)
table.add_row(
    "3",
    "[red]Non-Drug[/red]",
    f"{non_drug}",
)

console.print(table)
