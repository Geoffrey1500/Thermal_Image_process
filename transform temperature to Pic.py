import pandas as pd

CSV_FILE_PATH = 'tmp_data/1.csv'
df = pd.read_csv(CSV_FILE_PATH, error_bad_lines=False, sep='\t', header=None).drop([0], axis=0)

df = df[0].str.split(',', expand=True,).drop([0, 385], axis=1).astype('float64')

tem_data = df.values

