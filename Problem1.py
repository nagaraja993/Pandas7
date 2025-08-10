import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    y = (delivery[delivery['order_date'] == delivery['customer_pref_delivery_date']].shape[0]*100)/delivery.shape[0]
    return pd.DataFrame([round(y,2)], columns = ['immediate_percentage'])



    