import pandas as pd
df = pd.read_csv('./big-mac-full-index.csv')
def iterate_apply(row):
    return row[2]

result = df.apply(iterate_apply, axis = 1)
count = 0
for res in result:
    if count < 10:
        print(res)
        count += 1

for index, row in df.iterrows():
    print(f'{row[2]}')