from src.lib.process import Process, ProcessHandler

class Projects(Process):
  _name = 'projects'
  

class ProjectsHandler(ProcessHandler):
  _name = 'projects'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    pass