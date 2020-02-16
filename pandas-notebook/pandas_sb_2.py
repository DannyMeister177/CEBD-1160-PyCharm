import pandas as pd

df = pd.read_csv('winter2020-code/4-python-advanced-notebook/data/insurance.csv', header=0)

print(df.age)
print()
print(df[['age', 'children', 'charges']])
print()
print(df[['age', 'children', 'charges']].iloc[:5])
print()
print(df['charges'].mean())
print()
print(df['charges'].min())
print()
print(df['charges'].max())
print()
print(df[df['charges']==10797.3362])
print()
print(df[df['charges']==df['charges'].max()])
print()
for name, group in df.groupby('region'):
    print('Group: {}'.format(name))
    print('Size: {} insured'.format(len(group)))
    print('------------------------')
