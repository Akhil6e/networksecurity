from setuptools import find_packages,setup
from typing import List
def get_req_list()->List[str]:
 requirment_list:List[str]=[]
 try:
  with open('requirements.txt','r') as files:
    Lines=files.readlines()
    for lines in Lines:
      requirement=Lines
    if requirement and requirement!='e .':
      requirment_list.append(requirement)
 except FileNotFoundError:
    print("file not found")

    return requirment_list
 
print(get_req_list()) 