import pandas as pd
import numpy as np
import openpyxl

path = 'C:/Users/shaot/Desktop/listnode/SocapForm-Sample-Ver2-final.xlsx'
socap_data = pd.read_excel(path, error_bad_lines=False)
socap_data = np.array(socap_data)
get_file = openpyxl.load_workbook(path)
sheet_names = get_file.get_sheet_names()
number_of_companies = len(sheet_names) - 3
companies_list = []
target_list = []

for i in range(0, number_of_companies):
    companies_list.append(sheet_names[i])
'generate companies list'

for i in range(29, 46):
    a = socap_data[i][0]
    a = a[8:]
    a = a.strip(')')
    target_list.append(a)
'generate target list'

socap_matrix = np.zeros([int(len(target_list)+1), int(len(companies_list)+1)])
socap_matrix = socap_matrix.astype(np.str)

for i in range(0, len(companies_list)):
    socap_matrix[0][i+1] = companies_list[i]
    company_data = pd.read_excel(path, error_bad_lines=False, sheet_name=companies_list[i])
    company_data = np.array(company_data)
    for j in range(0, len(target_list)):
        socap_matrix[j+1][i+1] = company_data[29+j][1]

for i in range(0, len(target_list)):
    socap_matrix[i+1][0] = target_list[i]
'get necessary data from excel and input it into matrix'

socap_matrix[0][0] = 'Target\Organization'

for i in range(0, len(socap_matrix)):
    for j in range(0, len(socap_matrix[0])):
        if socap_matrix[i][j] == 'nan':
            socap_matrix[i][j] = 0
'change nan in matrix into 0'

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('max_colwidth', 1000)
pd.set_option('expand_frame_repr', False)
socap_matrix = pd.DataFrame(socap_matrix)
print(socap_matrix)
