# Pandas5

# 1 Problem 1 : Department Highest Salary (https://leetcode.com/problems/department-highest-salary/ )

import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(department, left_on = 'departmentId', right_on ='id', how ='left' )
    max_salary = df.groupby(['departmentId'])['salary'].transform('max')
    df = df[df['salary'] == max_salary]
    return df[['name_y','name_x','salary']].rename(columns = {'name_y':'Department','name_x':'Employee','salary':'Salary'})

# 2 Problem 2 : Rank Scores ( https://leetcode.com/problems/rank-scores/ )

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank']= scores['score'].rank(method = 'dense', ascending = False)
    scores = scores.sort_values(by = ['score'], ascending = False)
    return scores[['score','rank']]