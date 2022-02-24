PATH = 'src/submission_files/'

submission_example_dict = {
    'project_count': 1,
    'project_solution': [
        {
            'project_name': 'project_name',
            'contributors': ['contributor_1', 'contributor_2']
        },
    ]
}


class GenerateSubmission():

    def generate_submission(self, solution, example):
        path_to_file = f'{PATH}{example}.out.txt'
        with open(path_to_file, 'w') as f:
            project_count = solution['project_count']
            f.write(str(project_count))
            f.write('\n')
            for sol in solution['project_solution']:
                f.write(sol['project_name'])
                f.write('\n')
                contributors_string = ''
                for i, contributors in enumerate(sol['contributors']):
                    contributors_string += contributors
                    if i < len(sol['contributors']) - 1:
                        contributors_string += ' '
                f.write(contributors_string)
                f.write('\n')


generate_submission = GenerateSubmission()

generate_submission.generate_submission(submission_example_dict, 'test')
