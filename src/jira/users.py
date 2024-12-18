from src.lib.process import Process, ProcessHandler

class Users(Process):
  name = 'users'


class UsersHandler(ProcessHandler):
  name = 'users'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    pass