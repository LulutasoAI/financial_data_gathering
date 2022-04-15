import os 

class Utilities:
    def __init__(self) -> None:
        pass 
    
    def create_folder(self,path):
        os.makedirs(path,exist_ok=True)

