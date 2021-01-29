import copy
def remove_duplicate_list(the_list:list):
    '''
    the obj of list should be simple obj like str, int, float
    '''
    new_list = []
    for i in the_list:
        for j in new_list:
            if set(i) == set(j):
                break
        else:
            new_list.append(i)
    return new_list

def get_element_combination(the_list:list, n):
    '''
    the obj of list should be simple obj like str, int, float
    it is Cmn, m = len(the_list), n should be no more than m, no less than 1
    '''
    m = len(the_list)
    new_list = []
    if n == 1:
        new_list = [[i] for i in the_list]
    else:
        _tmp_list1 = copy.deepcopy(the_list)
        for i in range(m):
            _tmp_element = _tmp_list1[0]
            _tmp_list1.pop(0)
            _tmp_list2 = get_element_combination(_tmp_list1, n - 1)
            for j in _tmp_list2:
                _tmp_list3 = copy.deepcopy(j)
                _tmp_list3.append(_tmp_element)
                _tmp_list3.sort()
                new_list.append(_tmp_list3)
    return new_list

def get_all_combination(the_list:list, n, m = 0):
    '''
    the obj of list should be simple obj like str, int, float
    the n is the shortest len of list that you need
    the m is the longest len of list that you need, the default is len of the_list
    '''
    new_list = []
    if m == 0:
        m = len(the_list)
    for i in range(n, m + 1):
        new_list.extend(get_element_combination(the_list, i))
    return new_list

class CheckList():

    @staticmethod
    def mutual_contain(a, b):
        '''
        if a in b or b in a,then true
        '''
        _tmp1 = copy.deepcopy(a)
        _tmp2 = copy.deepcopy(b)
        _tmp1.extend(_tmp2)
        if set(_tmp1) == set(b) or set(_tmp1) == set(a):
            return True
        else:
            return False 

if __name__ == "__main__":
    a = [1,2,3]
    b = [1,2]
    c = CheckList.contain(a,b)
    print(c)
    pass