from PIL import Image
import easyocr
import numpy as np

class Visual_Process:
    def __init__(self) -> None:
        self.reader = easyocr.Reader(['en'])

    def read_pic_from_path(self,image_path:str):
        #binary_image = self.image_path_to_binary(image_path)
        #Image.fromarray(binary_image).save(image_path)
        result = self.reader.readtext(image_path)
        return result

    def image_path_to_binary(self,image_path):
        image = np.array(Image.open(image_path).convert('L'), 'f')
        image = (image > 100) * 255
        return image
        
    def easyocr_result_interpreter(self, result:list):
        #Assuming the result is pretty constant.
        string_access_enum = 1
        price = ""
        for i,information in enumerate(result):
            if i == 0:
                continue
            extracted_text = information[string_access_enum]
            price += extracted_text
        try:
            float(price)
            return price
        except:
            return None
        