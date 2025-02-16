# crea una clase que se conecte a postgres utilizando sqlalchemy y permita extraer dataframes de las tablas de la base de datos
from sqlalchemy import create_engine
from sqlalchemy import text

import pandas as pd
from src.lib.decorators import singleton

@singleton
class PostgresConnection:
    
  def __init__(self,user:str,password:str,host:str,port:str,database:str):
    connection_string=f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
    self._engine = create_engine(connection_string)
    self._connection = self._engine.connect()

  def query(self, sql:str):
    df = pd.read_sql(sql, self._connection)
    return df
  
  def load_df(self,table_schema,table_name:str,df:pd.DataFrame):
    
    df.to_sql(table_name,self._engine, schema=table_schema, if_exists='replace', index=False)

  def execute_sql_command(self, sql: str):

    self._connection.execute(text(sql))
 