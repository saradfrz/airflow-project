from datetime import datetime
from airflow.decorators import dag


@dag(
    start_date=datetime(2022, 1, 1), 
    schedule='@daily',
    catchup=False,
    tags=['stock_market']
)
def stock_market():
    pass

stock_market()