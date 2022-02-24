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

example = sys.argv[1]

contributors, projects = ReadData().read_data(example)

projects.sort(key=lambda x: (x[1]['value'], x[1]['skill_acc']), reverse = True)

for project in projects:
    print(project)

solution_list = []

solution = {
    'project_count': len(solution_list),
    'project_solution': solution_list
}

score = GenerateSubmission().generate_submission(solution, example)

print(f'score {score}')
