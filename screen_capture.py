import pyautogui
import os
from PIL import Image 

from config_reader import Config_Reader

class Screen_Capture:
    """
    It can capture the main monitor only.
    """
    def __init__(self) -> None:
        self.config = Config_Reader().get_config()
        pass 
    
    def capture(self,path=None):
        captured = pyautogui.screenshot()
        if path == None:
            path = self.config["path"]["captured_pics"]
        captured.save(os.path.join(path,"captured.png"))

    def crop_captured(self, image_path=None):
        if image_path==None:
            name_default_pic = "captured.png"
            image_path = os.path.join(self.config["path"]["captured_pics"],name_default_pic)
            
        image = Image.open(image_path)
        image.show()
        
        
    