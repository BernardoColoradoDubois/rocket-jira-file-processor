from src.lib.process import Process, ProcessHandler
import boto3

class Issue(Process):
  name = 'issue'

class IssueHandler(ProcessHandler):
  name = 'issue'
  
  def __init__(self):
    pass
  
  def execute(self,process:Process)->None:
    ...
  