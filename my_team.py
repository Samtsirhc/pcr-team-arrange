import string

from config import *


class MyTeam():
    def __init__(self, team_info: str):
        '''
        传入一行阵容信息
        '''
        self._info = team_info.replace('\n', '').split(SEPARATOR)
        self.name = self._info[POS.index('name')]
        self.damage = int(self._info[POS.index('damage')])
        self.get_wifes()
        self.assistors = []
        self.safe_team = 0  # 表示这个阵容是安全的随便打，即conflicts为空
        self.conflicts = []  # 与这个阵容冲突的阵容，空则无冲突

    def get_wifes(self):
        self.wifes = []
        for i in range(1, 6):
            self.wifes.append(self._info[POS.index(i)])

if __name__ == "__main__":
    pass
