import pandas as pd
import json
from pprint import pprint

# excel_file = 'table.xlsx'
# sheet_name = 'Филиалы'

# df = pd.read_excel(excel_file, sheet_name=sheet_name)
# df['первые 3 цифры ЛС'] = df['первые 3 цифры ЛС'].astype(str).str.zfill(3)
# df['Код сегмента'] = df['Код сегмента'].astype(str).str.zfill(2)
# df['BranchId (для ЕИП)'] = df['BranchId (для ЕИП)'].astype(str)

# result = {}

# nums = df.index.tolist()
# for num in nums:
#     type = df.at[num, "тип документа"]
#     segment = df.at[num, "Сегмент"]
#     account_3 = df.at[num, "первые 3 цифры ЛС"]
#     code = df.at[num, "Код сегмента"]
#     branch_id = df.at[num, "BranchId (для ЕИП)"]

#     if type.lower() == 'mvno':
#         type = 'mvno'
#     else:
#         type = 'other'
#         print(type)

#     if type not in result:  
#         result[type] = {}

#     if account_3 not in result[type]:
#         result[type][account_3] = {}

#     if code not in result[type][account_3]:
#         result[type][account_3][code] = branch_id

# json_str = json.dumps(result, indent=4)
# print(json_str)


excel_file = 'tabel_table.xlsx'

df = pd.read_excel(excel_file)
df['ФИО (ЦДС)'] = df['ФИО (ЦДС)'].astype(str)
df['Табельный номер'] = df['Табельный номер'].astype(str)

result = {}

nums = df.index.tolist()
for num in nums:
    fio = df.at[num, "ФИО (ЦДС)"]
    tab_number = df.at[num, 'Табельный номер']

    if fio not in result:  
        result[tab_number] = fio

json_str = json.dumps(result, indent=4, ensure_ascii=False)
print(json_str)
