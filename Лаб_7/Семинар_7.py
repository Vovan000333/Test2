import pandas as pd

lst = ['Java', 'Python', 'C', 'C++',
         'JavaScript', 'Swift', 'Go']

# data = {'Name': ['Tom', 'Joseph', 'Krish', 'John'], 'Age': [20, 21, 19, 18]}
#
# df = pd.DataFrame(data)

excel_data_df = pd.read_excel('test1.xlsx', sheet_name='Лист1', usecols=['Фамилия', 'Лаб 6.'])

print(excel_data_df)
print(excel_data_df['Фамилия'].tolist())


