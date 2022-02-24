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

    def run(self, contributors, projects):
        
        solution_list = []

        day = 0

        for project_tuple in projects:
            project_name = project_tuple[0]
            project = project_tuple[1]
            complete_days = project['complete_days']
            day += complete_days

            assigned_contributors = []

            for skill in project['skill']:

                skill_name = skill[0]
                skill_value = skill[1]

                for hacker_name, hacker_dict in contributors.items():

                    if skill_name not in hacker_dict['skill_list']:
                        continue

                    if skill_value < hacker_dict['skills'][skill_name]:
                        continue

                    if hacker_dict['busy_until'] > day:
                        continue
                    assigned_contributors.append(hacker_name)
                    hacker_dict['busy_until'] = day
                    break
                else:
                    break
                solution_list.append({'project_name': project_name,
                                      'contributors': assigned_contributors})
        return solution_list




example = sys.argv[1]

contributors, projects = ReadData().read_data(example)

projects.sort(key=lambda x: (x[1]['value'], x[1]['best_before'], x[1]['skill_acc']), reverse = True)

for project in projects:
    print(project)

solution_list = Solution().run(contributors, projects)

print(solution_list)


solution = {
    'project_count': len(solution_list),
    'project_solution': solution_list
}

score = GenerateSubmission().generate_submission(solution, example)

print(f'score {score}')
