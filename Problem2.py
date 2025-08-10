import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    def category(x):
        if x < 20000:
            return 'Low Salary'
        elif x > 50000:
            return 'High Salary'
        else:
            'Average Salary'
    accounts['category'] = accounts['income'].apply(category)
    return accounts.groupby("category")['income'].agg('count').reset_index()
    