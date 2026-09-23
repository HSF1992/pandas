import pandas as pd
    
df = pd.read_csv('实战数据.csv')
print('原文件数据:')
print(df)

df.columns = df.columns.str.strip()

#df['产品'] = pd.to_texting(df['产品'],error='coerce')
df['产量'] = pd.to_numeric(df['产量'],errors='coerce')
df['收率'] = pd.to_numeric(df['收率'],errors='coerce')
df['日期'] = pd.to_datetime(df['日期'],errors='coerce')

df = df.drop_duplicates()

df['产量'] = df['产量'].fillna(0)
df['收率'] = df['收率'].fillna(0)
df['日期'] = df['日期'].fillna(pd.Timestamp('2026-09-01'))

print('\n清洗后数据')
print(df)

汇总 = df.groupby('产品').agg(
    总产量 = ('产量','sum'),
    平均产量 = ('产量','mean'),
    批数 = ('批号','count')
).reset_index()

print('\n汇总记录')
print(汇总)

df['月份'] = df['日期'].dt.month.values
#df_透视 = df[['月份','产量','产品']]
'''透视表 = pd.pivot_table(df_透视,
    values='产量',
    index='产品',
    columns='月份',
    aggfun='sum',
    fill_value=0
)'''
透视 = df.groupby(['产品','月份'])['产量'].sum()
透视表 = 透视.unstack(fill_value=0)

print('\n透视表记录:')
print(透视表)


with pd.ExcelWriter('实战汇总.xlsx') as writer:
    汇总.to_excel(writer,sheet_name = '汇总记录',index=False)
    透视表.to_excel(writer,sheet_name='透视记录')
print('\n记录已导出,文件名:实战汇总.xlsx')
