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
    
    def capture(self,path:str=None):
        captured = pyautogui.screenshot()
        if path == None:
            path = self.config["path"]["captured_pics"]
        captured.save(os.path.join(path,"captured.png"))

    def crop_captured(self, xy:tuple,image_path:str=None,):
        if image_path==None:
            name_default_pic = "captured.png"
            image_path = os.path.join(self.config["path"]["captured_pics"],name_default_pic)
        #image.crop takes box = (left, upper, right, lower)
        image = Image.open(image_path)
        w,h = image.size
        x,y = xy
        x_adjustment_left = w *0.03 
        y_adjustment_top  = h *0.03
        x_ajdustment_right = w* 0.1
        y_adjustment_lower = h*0.1
        left = x-x_adjustment_left
        top = y-y_adjustment_top
        right = x+x_ajdustment_right
        lower = y+y_adjustment_lower
        image = image.crop((left,top,right,lower))
        image.show()
        
        
    