from src.lib.process import Process, ProcessHandler

class Issues(Process):
  _name = 'issues'


class IssuesHandler(ProcessHandler):
  _name = 'issues'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    pass