import os
import pandas as pd
import numpy as np

PATH = 'src/data/'


class ReadData():

    def read_data(self, filename):
        data_path = f'{PATH}{filename}'

        contributors = {}
        projects = []

        with open(data_path) as f:

            number_contributors, number_projects = f.readline().split()

            for contr in range(int(number_contributors)):
                name_contr, nskills = f.readline().split()


                skills = {}
                skill_list = []
                for nskill in range(int(nskills)):
                    skill, level = f.readline().split()
                    skills[skill] = int(level)
                    skill_list.append(skill)
                contributors.update({name_contr: {'skills': skills, 'skill_list': skill_list, 'busy_until': 0}})


            for proj in range(int(number_projects)):
                name_proj, complete_days, score, best_before, nroles = f.readline().split()
                skills = []
                skill_acc = 0
                for roles in range(int(nroles)):
                    skill, level = f.readline().split()
                    skill_acc += int(level)
                    skills.append((skill, int(level)))

                projects.append(
                    (name_proj, {
                        'complete_days' : int(complete_days), 
                        'score': int(score),
                        'best_before' : int(best_before),
                        'skill': skills,
                        'skill_acc': skill_acc,
                        'value': int(score)/int(complete_days)
                    }))

        return contributors, projects

    def prepare_data(self):
        pass
