import mysql.connector
from mysql.connector import Error

import time
import argparse
import pandas as pd
from datetime import date

def sql_query(query_string):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port='3309',
            database='fbdb',
            user='socialmon',
            password='rapplers'
        )
        cursor = connection.cursor()
        cursor.execute(query_string)
        records = cursor.fetchall()

    except Error as e:
        print("Error while connecting to MySQL", e)

    finally:
        return records

if __name__ == "__main__":
    start_code = time.time()

    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", 
                        help="Keyword to be queried")
    args = parser.parse_args()

    sdate = date(2018,8,1)
    edate = date(2018,8,1)
    dates0 = pd.date_range(sdate,edate,freq='d')
    dates = list(dates0.strftime('%Y-%m-%d'))

    result = []
    for day in dates:
        sql_select_query = f"""
            SELECT COUNT(message)
            FROM m_posts
            WHERE created_date = '{day}'
            AND message LIKE '%{args.keyword}%'
        """

        query_result = sql_query(sql_select_query)
        result.append(query_result)

    print(result)