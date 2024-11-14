import seaborn as sns
import pandas as pd
from statsmodels.regression.linear_model import OLS
import statsmodels.api as sm

# read data
df = pd.read_csv('ms_data_insurance.csv')

# part 1 - analyze walking speed
df.loc[df['education_level']=='High School', 'education_num'] = 0
df.loc[df['education_level']=='Some College', 'education_num'] = 1
df.loc[df['education_level']=='Bachelors', 'education_num'] = 2
df.loc[df['education_level']=='Graduate', 'education_num'] = 3
print("=== Linear Regression for Walking Speed by Age and Education ===")
X_with_const = sm.add_constant(df[['age', 'education_num']])
y = df['walking_speed']
model = OLS(y, X_with_const)
results = model.fit()
print(results.summary().tables[1], '\n')

# part 2 - analyze costs

print('Overall visit cost statistics:\n', df['visit_cost'].describe(), '\n')
print('Basic insurance visit cost statistics:\n', df.loc[df['insurance']=='Basic', 'visit_cost'].describe(), '\n')
print('Premium insurance visit cost statistics:\n', df.loc[df['insurance']=='Premium', 'visit_cost'].describe(), '\n')
print('Platinum insurance visit cost statistics:\n', df.loc[df['insurance']=='Platinum', 'visit_cost'].describe(), '\n')

ax = sns.boxplot(data=df, x='insurance', y='visit_cost', color='lightblue')
ax.set_title('BMI Distribution by Age Group')