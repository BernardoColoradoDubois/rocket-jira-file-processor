from src.lib.process import Process, ProcessHandler

class Users(Process):
  _name = 'users'


class UsersHandler(ProcessHandler):
  _name = 'users'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    pass