import os
import pandas as pd
import numpy as np

PATH = 'src/data/'


class ReadData():

    def read_data(self, filename):
        data_path = f'{PATH}{filename}'

        contributors = {}
        projects = {}

        with open(data_path) as f:

            number_contributors, number_projects = f.readline().split()

            for contr in range(int(number_contributors)):
                name_contr, nskills = f.readline().split()

                contributors.update({name_contr: []})

                for nskill in range(int(nskills)):
                    skill, level = f.readline().split()
                    contributors[name_contr].append({skill : int(level)})

            for proj in range(int(number_projects)):
                name_proj, complete_days, score, best_before, nroles = f.readline().split()
                projects[name_proj] = {'complete_days' : int(complete_days), 
                                        'score': int(score),
                                        'best_before' : int(best_before),
                                        'skill': []
                                        }
                for roles in range(int(nroles)):
                    skill, level = f.readline().split()
                    projects[name_proj]['skill'].append((skill, int(level)))

        return contributors, projects

    def prepare_data(self):
        pass
