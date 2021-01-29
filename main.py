from init_team import init_team
import copy
from config import *
from tools import *

class TeamGroup():
    def __init__(self, teams):
        self.my_group = []
        self.teams = copy.deepcopy(teams)
        self.get_safe_group()
        self.get_conflict_group_name()
        self.get_mutual_unconflict_group_name()
        self.get_unconflict_group_name()
        self.output_my_group()
    pass

    def output_my_group(self):
        with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
            f.write('随便打的阵容是：\n')
            f.write(self.get_output(self.safe_group))
            for i in range(len(self.my_group)):
                f.write(f'无冲突的阵容【{i + 1}】：\n')
                f.write(self.get_output(self.my_group[i]))

    def get_safe_group(self):
        self.safe_group = []
        self.unsafe_group = []
        for i in self.teams:
            if i.safe_team == 1:
                self.safe_group.append(copy.deepcopy(i))
            else:
                self.unsafe_group.append(copy.deepcopy(i))

    def get_mutual_unconflict_group_name(self):
        '''
        only get the group with teams that they do not mutual conflict, not realiy unconflict
        '''
        _unsafe_names = [self.unsafe_group[i].name for i in range(len(self.unsafe_group))]
        self.team_combination = get_all_combination(_unsafe_names, LEAST_TEAM_COUNT)
        self.mutual_unconflict_group_name = []
        for i in self.team_combination:
            for j in self.conflict_group_name:
                if CheckList.mutual_contain(i, j):
                    break
            else:
                self.mutual_unconflict_group_name.append(i)

    def get_conflict_group_name(self):
        self.conflict_group_name = []
        _conflict_group = []
        _team_count = len(self.unsafe_group)
        for i in range(_team_count):
            if len(self.unsafe_group[i].conflicts) > 0:
                _conflict_group.append(self.unsafe_group[i].name)
                for j in self.unsafe_group[i].conflicts:
                    _conflict_group.append(j)
            _conflict_group.sort()
            if _conflict_group != []:
                self.conflict_group_name.append(_conflict_group)
            _conflict_group = []
        self.conflict_group_name = remove_duplicate_list(self.conflict_group_name)
        return self.conflict_group_name

    def check_conflict(self, the_list:list):
        '''
        true means conflict
        meanwhile, the unconflict group will be added to self.my_group
        '''
        teams = []
        for i in the_list:
            for j in self.unsafe_group:
                if i == j.name:
                    teams.append(copy.deepcopy(j))
                    break
        
        use_times = {}
        for i in range(len(teams)):
            for j in range(5):
                if teams[i].wifes[j] not in use_times.keys():
                    use_times[teams[i].wifes[j]] = 1
                else:
                    use_times[teams[i].wifes[j]] += 1

        # if conflict, return
        for i in teams:
            _tmp = 0
            for j in i.wifes:
                if use_times[j] == 2:
                    i.assistors.append(j)
                _tmp += use_times[j]
            print(_tmp)
            if _tmp > 7:
                return True
        
        self.my_group.append(teams)
        return False

    def get_unconflict_group_name(self):
        self.unconflict_group_name = copy.deepcopy(self.mutual_unconflict_group_name)
        for i in range(len(self.unconflict_group_name)):
            if self.check_conflict(self.unconflict_group_name[i]):
                self.unconflict_group_name.pop(i)

    def get_output(self, teams):
        _output = []
        self.output = ''
        for i in teams:
            _output.append(i.name)
            _output.append(i.damage)
            _output.extend(i.wifes)
            _output = ' '.join(_output)
            try:
                if len(i.assistors) == 2:
                    _output += f' 借用：{i.assistors[0]}/{i.assistors[1]}'
                else:
                    _output += f' 借用：{i.assistors[0]}'
            except:
                _output += f' 借用：随便借'
            _output += '\n'
            self.output += _output
            _output = []
        return self.output
    
    def sum_damage(self, teams):
        self.damage = 0
        for i in teams:
            self.damage += int(i.damage)

if __name__ == "__main__":
    teams = init_team()
    test = TeamGroup(teams)
    for i in test.my_group:
        print(test.get_output(i))
    pass