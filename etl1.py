from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import psycopg2
import pandas as pd 
   
host_mysql = "localhost"
user_mysql = "root"
password_mysql = "root" 
database_mysql = "sistema_mysql"
engine_mysql = create_engine(f"mysql+pymysql://{user_mysql}:{password_mysql}@{host_mysql}/{database_mysql}")

host_postgres = "localhost"
user_postgres = "postgres"
password_postgres = "POSTGRES"
database_postgres = "datawarehouse"
engine_postgres = create_engine(f"postgresql://{user_postgres}:{password_postgres}@{host_postgres}/{database_postgres}")

if not database_exists(engine_postgres.url):
    create_database(engine_postgres.url)

def executar_query(query):
    with engine_mysql.connect() as conn:
        return pd.read_sql(query,conn)
    
def criando_tabela(nome_da_tabela, df):
    with engine_postgres.connect() as conn:
        df.to_sql(nome_da_tabela, conn, index=False, if_exists='replace')

criando_tabela("pessoas", executar_query("SELECT * FROM pessoas"))
criando_tabela("vendas", executar_query("SELECT * FROM vendas"))