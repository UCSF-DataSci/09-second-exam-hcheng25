import seaborn as sns
import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm

# read data
df = pd.read_csv('ms_data_insurance.csv')

# part 1 - analyze walking speed
print('Part 1 - Analyze walking speed\n')
df.loc[df['education_level']=='High School', 'education_num'] = 0
df.loc[df['education_level']=='Some College', 'education_num'] = 1
df.loc[df['education_level']=='Bachelors', 'education_num'] = 2
df.loc[df['education_level']=='Graduate', 'education_num'] = 3
print("=== Linear Regression for Walking Speed by Age and Education ===")
model = smf.ols(formula='walking_speed~age+education_level', data=df)
results = model.fit()
print(results.summary().tables[1], '\n')

# part 2 - analyze costs
print('Part 2 - Analyze costs\n')
print('Overall visit cost statistics:\n', df['visit_cost'].describe(), '\n')
print('Basic insurance visit cost statistics:\n', df.loc[df['insurance']=='Basic', 'visit_cost'].describe(), '\n')
print('Premium insurance visit cost statistics:\n', df.loc[df['insurance']=='Premium', 'visit_cost'].describe(), '\n')
print('Platinum insurance visit cost statistics:\n', df.loc[df['insurance']=='Platinum', 'visit_cost'].describe(), '\n')

ax = sns.boxplot(data=df, x='insurance', y='visit_cost', color='lightblue')
ax.set_title('BMI Distribution by Age Group')

# part 3 - advanced analysis
print('Part 3 - Advanced analysis\n')
sns.scatterplot(data=df, 
                x='age', 
                y='walking_speed', 
                hue='education_level',
                alpha=0.5,
                markers='.')

print("=== Examination of Confounding of Education Level on Walking Speed by Age ===")
model2 = smf.ols(formula='walking_speed~age', data=df)
results = model2.fit()
print('Unadjusted R2 value: ', results.rsquared)
model2 = smf.ols(formula='walking_speed~age+education_level', data=df)
results2 = model2.fit()
print('Adjusted by education_level R2 value: ', results2.rsquared)
print('Difference in R2: ', results2.rsquared-results.rsquared, '\n')

print("=== Interaction of Education Level on Walking Speed by Age ===")
model2 = smf.ols(formula='walking_speed~age*education_level', data=df)
results = model2.fit()
print(results.summary().tables[1])