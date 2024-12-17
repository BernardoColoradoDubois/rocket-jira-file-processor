from src.lib.process import Process, ProcessHandler

class Project(Process):
  name = 'project'
  

class ProjectHandler(ProcessHandler):
  name = 'project'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    pass