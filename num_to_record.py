import numpy as np
import pandas as pd
import datetime 

class Recorder:
    def __init__(self) -> None:
        pass

    def record(self, number:float, csv_path:str):
        try:
            df = pd.read_csv(csv_path,header=None)
        except:
            df = pd.DataFrame()
        pd.Series()
        line_to_add = pd.DataFrame([(self.get_currenttime_string(),number)])
        df = pd.concat([df,line_to_add])
        df.to_csv(csv_path,header=False,index=False)

    def get_currenttime_string(self):
        date_str = datetime.datetime.now()
        return date_str