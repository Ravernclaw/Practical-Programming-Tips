import os
def listdirInMac(path):
    ori_lists = os.listdir(path)
    lists = []
    for item in ori_lists:
        if item[0] == '.':
            continue
        lists.append(item)
    return lists
