from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import pandas as pd 

def criando_tabela(nome_da_tabela, df):
    with engine.connect() as conn:
        df.to_sql(nome_da_tabela, conn, index=False, if_exists='replace')
    
host = "localhost"
user = "root"
password = "root" 
database = "sistema_mysql"
engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

if not database_exists(engine.url):
    create_database(engine.url)

criando_tabela('pessoas', pd.read_csv("arquivos\\pessoas.csv"))
criando_tabela('vendas', pd.read_csv("arquivos\\vendas.csv"))