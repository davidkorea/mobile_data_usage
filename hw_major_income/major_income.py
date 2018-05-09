import pandas as pd
import matplotlib.pyplot as plt
from pd_utils import utils

edu = './data_employee/employee_edu.csv'
info = './data_employee/employee_info.csv'

edu_df = pd.read_csv(edu)
info_df =pd.read_csv(info)

merge_df = pd.merge(edu_df,info_df,how='inner',on='EmployeeNumber')
# utils(merge_df)

mean_income = merge_df.groupby('EducationField')['MonthlyIncome'].mean()
mean_income.sort_values(ascending=False,inplace=True)
print(mean_income)

mean_income.plot(kind='bar',rot=0)
plt.ylabel('Income')
plt.tight_layout()
plt.show()