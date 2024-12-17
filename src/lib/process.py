from abc import abstractmethod
from src.lib.decorators import singleton

class Process:
  
  # nombre unico del proceso
  _name=''
  
  # inicializamos el DTO con el nombre del bucket, la ruta del archivo y los parametros opcionales
  def __init__(self,bucket_name:str,file_key:str,params:dict={}):
    self._bucket_name = bucket_name
    self._file_key = file_key
    self._params = params
    
  # devuelve el nombre clave del proceso
  def get_name(self)->str:
    return self._name
  
  # devuelve los parametros opcionales
  def get_params(self)->dict:
    return self._params
  
  # devuelve el nombre del bucket
  def get_bucket_name(self):
    return self._bucket_name
  
  # devuelve la ruta del archivo
  def get_file_key(self):
    return self._file_key


class ProcessHandler:
  
  # nombre unico del proceso
  _name=''
  
  # metodo donde se implementa el servicio
  @abstractmethod
  def execute(self,process:Process)->None:
    pass
  
  # devuelve el nombre del proceso
  def get_name(self)->str:
    return self._name
  

@singleton
class ProcessBus:
  
  # inicializamos handlers como un diccionario vacio
  def __init__(self):
    self._handlers={}
    
  # agregamos handler en base a su nombre
  def subscribe(self,handler:ProcessHandler):
    self._handlers[handler.get_name()]=handler
    
  # ejecutamos handler en base al nombre del proceso
  def dispatch(self,process:Process):
        
    # en caso de no existir estar suscrito un handler para el proceso
    if process.get_name() not in self._handlers.keys():
      print(f"Process Named {process.get_name()} Not Found")
    
    # en caso de si estar suscrito ejecutamos
    else:
      self._handlers[process.get_name()].execute(process)
      