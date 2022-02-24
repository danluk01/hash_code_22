import imp
import os
import pandas as pd
import numpy as np


from read_data import (
    ReadData
)

from generate_score import (
    GenerateSubmission
)


class Solution():

    def run(self):
        pass


test_data = ReadData().read_data()
score = GenerateSubmission().generate_submission()

print(f'this is score {score}')
print(f'this is test_data {test_data}')
print('works')
