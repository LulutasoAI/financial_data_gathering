import os 
import time

import gui_related
import num_to_record
from screen_capture import Screen_Capture
import utilities
from visual_processing import Visual_Process
from config_reader import Config_Reader
from gui_related import GUI_functions
import pyautogui

def test_main():
    test_image_path_sell = os.path.join("test_pics","sell.png")
    test_image_path_buy = os.path.join("test_pics","buy.png")
    utils = utilities.Utilities()
    utils.create_folder("captured_pics")
    config = Config_Reader().get_config()
    sell_image_path = os.path.join("buy_sell_particles","sell.png")
    buy_image_path = os.path.join("buy_sell_particles","buy.png")
    picture_save_path = config["path"]["captured_pics"]
    print(picture_save_path)
    print(type(picture_save_path))
    Screen_Capture().capture(picture_save_path)
    GUI_func = GUI_functions()
    coordinates_sell = GUI_func.get_coordinates(sell_image_path)
    coordinates_buy = GUI_func.get_coordinates(buy_image_path)
    print(coordinates_buy)
    print(coordinates_buy[0],coordinates_buy[1],"coords xy")
    print(coordinates_sell)
    print(type(coordinates_buy))
    visual_process = Visual_Process()
    result1 = visual_process.read_pic(test_image_path_buy)
    result2 = visual_process.read_pic(test_image_path_sell)
    visual_process.easyocr_result_interpreter(result1)
    visual_process.easyocr_result_interpreter(result2)
    Screen_Capture().crop_captured()
    """
    GUI_func.click_pic(sell_image_path)
    time.sleep(3)
    GUI_func.click_pic(buy_image_path)
    """


if __name__ == "__main__":
    test_main()