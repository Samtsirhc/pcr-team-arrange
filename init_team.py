import string
from config import *
from my_team import MyTeam

# 从文件读取阵容
def get_teams(file_name:str):
    with open(file_name, 'r', encoding = 'utf-8') as f:
        teams = []
        for line in f:
            teams.append(MyTeam(line))
    return teams

# 找出绝对安全的阵容
def get_safe_team(teams:list):
    use_times = {}
    for i in range(len(teams)):
        for j in range(5):
            if teams[i].wifes[j] not in use_times.keys():
                use_times[teams[i].wifes[j]] = 1
            else:
                use_times[teams[i].wifes[j]] += 1
    
    safe_mark = 0
    for i in range(len(teams)):
        for j in range(5):
            if use_times[teams[i].wifes[j]] == 1:
                safe_mark += 1
        if safe_mark == 5:
            teams[i].safe_team = 1
            teams[i].assistors.append('随便借')
        if safe_mark == 4:
            teams[i].safe_team = 1
            for j in range(5):
                if use_times[teams[i].wifes[j]] != 1:
                    teams[i].assistors.append(teams[i].wifes[j])
        safe_mark = 0

def get_conflict_team(teams:list):
    team_count = len(teams)
    for i in range(team_count):
        if teams[i].safe_team == 1:
            continue
        for j in range(i + 1, team_count):
            if teams[j].safe_team == 1:
                continue
            if check_conflict(teams[i].wifes, teams[j].wifes):
                teams[i].conflicts.append(teams[j].name)
                teams[j].conflicts.append(teams[i].name)

def check_conflict(team_1:list, team_2:list):
    _tmp = [i for i in team_1]
    _tmp.extend(team_2)
    if len(set(_tmp)) < 8:
        return True
    else:
        return False

def init_team():
    teams = get_teams(FILE_NAME)
    get_safe_team(teams)
    get_conflict_team(teams)
    return teams

if __name__ == "__main__":
    teams = init_team()
    for i in teams:
        print(i.wifes)
        print(i.conflicts)
    #     if i.safe_team == 1:
    #         print(i.name);print(i.wifes);print(i.assistors)
    pass