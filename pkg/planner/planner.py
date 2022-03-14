import requests, sys

class Planner:
    def __init__(self):
        print(sys.path)
        
        self.domain = open('pkg/domainX.txt', 'r').read()
        self.problem = open('pkg/problemX.txt', 'r').read()
        self.data = {'domain': self.domain,
                    'problem': self.problem}

    def generate(self):
        resp = requests.post('http://solver.planning.domains/solve',
                             verify=False, json=self.data).json()
        return '\n'.join([act['name'] for act in resp['result']['plan']])
