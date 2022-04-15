import pyautogui


class GUI_functions:
    def __init__(self) -> None:
        pass 
    
    def get_coordinates(self,image_path:str):
        coordinates = pyautogui.locateCenterOnScreen(image_path)
        if coordinates is not None:
            return (coordinates[0],coordinates[1])
        else:
            print("failed to get the coordinates")
            return (0,0)

    def click_pic(self, image_path:str):
        pyautogui.click(image_path)
