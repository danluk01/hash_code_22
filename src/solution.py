import imp
import os
import sys
import pandas as pd
import numpy as np


from read_data import (
    ReadData
)

from generate_submission import (
    GenerateSubmission
)


class Solution():

    def run(self):
        pass

contributors, projects = ReadData().read_data(sys.argv[1])

print(contributors)
print(projects)

score = GenerateSubmission().generate_submission()

print(f'this is score {score}')

print('works')
