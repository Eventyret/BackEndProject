from database.mysql import pymysql
from settings import db_config

db = mySQLdb(db_config.get('db_name'),
             db_config.get('user'),
             db_config.get('pass'),
             db_config.get('host'))
 
# Get all the available tables for
# our database and print them out.
tables = db.get_available_tables()
print tables