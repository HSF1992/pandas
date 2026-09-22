import pandas as pd
    
df = pd.DataFrame(
    [['001',"002",'003']],
    columns = pd.MultiIndex.from_tuples([
        ('A','x'),
        ('B','y'),
        ('C','z')
])
print('多级列名')
print(df.columns)

print('\n访问A下的x')
print(df[('A','x')]

print('\n访问A列')
print(df['A'])

print('\n压成单列')
df.columns = ['_',join(col) for col in df.columns]
print(df.columns)
