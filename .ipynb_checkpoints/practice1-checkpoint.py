import pandas as pd
path1 = "data/chipotle.tsv"
chipo = pd.read_csv(path1, sep = '\t')
chipo.head