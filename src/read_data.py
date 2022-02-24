import os
import pandas as pd
import numpy as np

PATH = 'src/data/'


class ReadData():

    def read_data(self):
        data_path = f'{PATH}test_read.csv'
        data = pd.read_csv(data_path)
        return data

    def prepare_data(self):
        pass
