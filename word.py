import copy
word = "abcde"

char_list = [[ "a", "c", "c", "f"],
             [ "b", "z", "a", "g"],
             [ "c", "d", "e", "g"],
             [ "g", "z", "x", "y"]]

def find_next(i,j, tmp_list, tmp_word):
    if len(tmp_word) == 0:
        return True, tmp_list
    high = len(tmp_list)
    length = len(tmp_list[0])
    des_char = tmp_word[0]
    # 下方
    if i+1 <= high and tmp_list[i+1][j] == des_char:
        tmp_list2 = copy.deepcopy(tmp_list)
        tmp_list2[i+1][j] = None
        res = find_next(i+1,j,tmp_list2, tmp_word[1:])
        if res[0]:
            return res
    # 上方
    if i-1 >= 0 and tmp_list[i-1][j] == des_char:
        tmp_list2 = copy.deepcopy(tmp_list)
        tmp_list2[i-1][j] = None
        res = find_next(i-1,j,tmp_list2, tmp_word[1:])
        if res[0]:
            return res
    # 左方
    if j-1 >= 0 and tmp_list[i][j-1] == des_char:
        tmp_list2 = copy.deepcopy(tmp_list)
        tmp_list2[i][j-1] = None
        res = find_next(i,j-1,tmp_list2, tmp_word[1:])
        if res[0]:
            return res
    # 右方
    if j+1 <= length and tmp_list[i][j+1] == des_char:
        tmp_list2 = copy.deepcopy(tmp_list)
        tmp_list2[i][j+1] = None
        res = find_next(i,j+1,tmp_list2, tmp_word[1:])
        if res[0]:
            return res
    del tmp_list
    return False, None

def find_word(word, char_list):
    for i in range(len(char_list)):
        for j in range(len(char_list[0])):
            if char_list[i][j] == word[0]:
                tmp_list = copy.deepcopy(char_list)
                tmp_list[i][j] = None
                res = find_next(i,j, tmp_list, word[1:])
                if res[0]:
                    print(res)
                    return res

print(find_word(word,char_list))

