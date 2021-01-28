from init_team import init_team
import copy
from config import *

class TeamGroup():
    def __init__(self, teams):
        self.teams = copy.deepcopy(teams)
    pass

    def get_output(self):
        _output = ''
        for i in self.teams:
            _output += f'{i.name}{SEPARATOR}{i.damage}{SEPARATOR}'
            _wifes = f'{i.wifes[0]}{SEPARATOR}{i.wifes[1]}{SEPARATOR}{i.wifes[2]}{SEPARATOR}{i.wifes[3]}{SEPARATOR}{i.wifes[4]}{SEPARATOR}'
            _output += _wifes
            try:
                _output += f'借用：{i.assistors[0]}'
            except:
                _output += f'借用：随便借'
            _output += '\n'
        self.output = _output
    
    def sum_damage(self):
        self.damage = 0
        for i in self.teams:
            self.damage += i.damage


if __name__ == "__main__":
    teams = init_team()
    test = TeamGroup(teams)
    test.get_output()
    test.sum_damage()
    print(test.output)
    print(test.damage)
    # for i in teams:
    #     print(i.conflicts)
    #     if i.safe_team == 1:
    #         print(i.name);print(i.wifes);print(i.assistors)
    pass