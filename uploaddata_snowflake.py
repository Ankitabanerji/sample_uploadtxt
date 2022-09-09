import logging
import snowflake.connector

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def upload_on_snowflake(s):
    con_eb = snowflake.connector.connect(user='ankitaSnowflake',
                                         password='Ankitasnowflake#1802',
                                         account='WC52939.ap-southeast-1',
                                         warehouse='COMPUTE_WH',
                                         database='YOUTUBE_SCRAPE_DATA',
                                         schema='PUBLIC',
                                         autocommit=True)
    db_cursor_eb = con_eb.cursor()
    print(db_cursor_eb)

    db_cursor_eb.execute('create table if not exists users (id integer , name varchar (100));')
    db_cursor_eb.close()

    db_cursor_eb = con_eb.cursor()
    query = "insert into users (id, name) values (1, 'rahul'),(2, '" + str(s) + "');"
    db_cursor_eb.execute(query)
