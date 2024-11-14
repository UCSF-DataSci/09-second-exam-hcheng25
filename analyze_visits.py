import pandas as pd
import numpy as np
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm

# step 1
df = pd.read_csv('ms_data.csv')
df['visit_date'] = pd.to_datetime(df['visit_date'])
df.sort_values(by=['patient_id','visit_date'])

# step 2
# dictionary for each patient_id value to get a random insurance type
insurance = pd.read_table('insurance.lst')
insurance = pd.Series(insurance['insurance_type'])
id_list = np.unique(df['patient_id'])
insurance_type = {}
for i in range(len(id_list)):
    insurance_type[id_list[i]] = insurance[np.random.randint(3)]

# insert values into insurance column based on dictionary
for i in range(len(df)):
    df.loc[i, 'insurance'] = insurance_type[df.loc[i, 'patient_id']]
    # generate a random cost for each visit based on insurance type
    # average of basic coverage is 1000, premium is 750, platinum is 500
    # actual cost can range from 80-120% of average, and each visit is generated independently
    if df.loc[i, 'insurance']=='Basic': df.loc[i, 'visit_cost'] = round(1000*np.random.uniform(low=0.8, high=1.2), 2)
    if df.loc[i, 'insurance']=='Premium': df.loc[i, 'visit_cost'] = round(750*np.random.uniform(low=0.8, high=1.2), 2)
    if df.loc[i, 'insurance']=='Platinum': df.loc[i, 'visit_cost'] = round(500*np.random.uniform(low=0.8, high=1.2), 2)

# step 3
print('Mean Walking Speed by Education Level\n', df.groupby('education_level')['walking_speed'].mean(), '\n')
print('Mean Visit Cost by Insurance Type\n', df.groupby('insurance')['visit_cost'].mean(), '\n')
print("=== Linear Regression for Walking Speed by Age ===")
X_with_const = sm.add_constant(df['age'])
y = df['walking_speed']
model = OLS(y, X_with_const)
results = model.fit()
print(results.summary().tables[1])