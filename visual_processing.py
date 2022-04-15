from PIL import Image
import easyocr

class Visual_Process:
    def __init__(self) -> None:
        self.reader = easyocr.Reader(['ch_sim','en'])

    def read_pic(self,image_path:str):
        result = self.reader.readtext(image_path)
        return result
    
    def easyocr_result_interpreter(self, result:list):
        string_access_enum = 1
        for information in result:
            extracted_text = information[string_access_enum]
            print(extracted_text)