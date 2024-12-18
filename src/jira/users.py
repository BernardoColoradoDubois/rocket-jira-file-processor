from src.lib.process import Process, ProcessHandler

class Issue(Process):
  name = 'issue'



class IssueHandler(ProcessHandler):
  name = 'issue'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    pass