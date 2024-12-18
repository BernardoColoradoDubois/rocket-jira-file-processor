from src.lib.process import Process, ProcessHandler

class Projects(Process):
  name = 'projects'
  

class ProjectsHandler(ProcessHandler):
  name = 'projects'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    pass