import logging
import snowflake.connector
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

user = os.getenv('USER')
passwrd = os.getenv('PASSWORD')
account_name = os.getenv('ACCOUNT')
warehouse_name = os.getenv('WAREHOUSE')
database_name = os.getenv('DATABASE')
schema_name = os.getenv('SCHEMA')


def upload_on_snowflake(s):
    con_eb = snowflake.connector.connect(user=user,
                                         password=passwrd,
                                         account=account_name,
                                         warehouse=warehouse_name,
                                         database=database_name,
                                         schema=schema_name,
                                         autocommit=True)
    db_cursor_eb = con_eb.cursor()
    print(db_cursor_eb)

    db_cursor_eb.execute('create table if not exists users (id integer , name varchar (100));')
    db_cursor_eb.close()

    db_cursor_eb = con_eb.cursor()
    query = "insert into users (id, name) values (1, 'rahul'),(2, '" + str(s) + "');"
    db_cursor_eb.execute(query)
