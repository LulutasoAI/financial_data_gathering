import os 
import time

from numpy import record

import gui_related
from num_to_record import Recorder
from screen_capture import Screen_Capture
import utilities
from visual_processing import Visual_Process
from config_reader import Config_Reader
from gui_related import GUI_functions
import pyautogui

class Execute:
    def __init__(self):
        """
        process to create required folders.
        call utilities for that.
        """
        utils = utilities.Utilities()
        self.config = Config_Reader().get_config()
        utils.create_folder("captured_pics")
        utils.create_folder("pic_to_extract")
        utils.create_folder("buy_sell_particles")
        self.csv_path = self.config["path"]["csv_path"]

    def main(self):
        recorder = Recorder()
        screen_capture = Screen_Capture()
        picture_save_path = self.config["path"]["captured_pics"]
        path_data_picture = os.path.join("pic_to_extract","data.png")
        screen_capture.capture(picture_save_path)
        GUI_func = GUI_functions()
        sell_image_path = os.path.join("buy_sell_particles","sell.png")
        buy_image_path = os.path.join("buy_sell_particles","buy.png")
        coordinates_sell = GUI_func.get_coordinates(sell_image_path)
        coordinates_buy = GUI_func.get_coordinates(buy_image_path)
        cropped_buy = screen_capture.crop_captured(coordinates_buy)
        cropped_sell = screen_capture.crop_captured(coordinates_sell)
        visual_process = Visual_Process()
        screen_capture.save_image(cropped_sell,path_data_picture)
        result1 = visual_process.read_pic_from_path(path_data_picture) 
        price = visual_process.easyocr_result_interpreter(result1)
        print(price)
        #visual_process.easyocr_result_interpreter(result2)
        recorder.record(price,self.csv_path)


    def test_main(self):
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
        cropped_buy = Screen_Capture().crop_captured(coordinates_buy)
        cropped_sell = Screen_Capture().crop_captured(coordinates_sell)

        """
        GUI_func.click_pic(sell_image_path)
        time.sleep(3)
        GUI_func.click_pic(buy_image_path)
        """


if __name__ == "__main__":
    Execute().main()