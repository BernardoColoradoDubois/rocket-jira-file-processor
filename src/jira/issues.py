from src.lib.process import Process, ProcessHandler

class Issues(Process):
  name = 'issues'



class IssuesHandler(ProcessHandler):
  name = 'issues'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    pass