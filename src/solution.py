import imp
import os
import pandas as pd
import numpy as np


from read_data import (
    ReadData
)

from generate_score import (
    GenerateScore
)


class Solution():

    def run(self):
        pass


test_data = ReadData().read_data()
score = GenerateScore().generate_score()

print(f'this is score {score}')
print(f'this is test_data {test_data}')
print('works')
