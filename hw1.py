from sys import stdin

def remove_unfreq(dic, min_sup):
    to_remove = []
    for key in dic.keys():
        if dic[key] < min_sup:
            to_remove.append(key)
    for remove in to_remove:
        dic.pop(remove)

def check_freq(transactions, item_set):
    count = 0
    for tran in transactions:
        add_to = True
        for item in item_set:
            if item not in tran:
                add_to = False
        if add_to:
            count += 1
    return count
            

min_sup = int(input())

item1_dic = {}
dic = {}
transactions = []
output = []
while(True):
    input_str = stdin.readline()
    if (input_str == ''):
        break
        
    input_str = set(input_str.split())
    transactions.append(input_str)
    for i in input_str:
        if (i, ) in item1_dic.keys():
            item1_dic[(i,)] += 1
        else:
            item1_dic[(i,)] = 1

remove_unfreq(item1_dic, min_sup)
dic = item1_dic.copy()

while len(dic.keys()) != 0:
    new_dic = {}
    for key in dic.keys():
        temp = []
        for i in key:
            temp.append(i)
        output.append((dic[key], temp))
        
        for i in item1_dic.keys():
            temp_add_1 = temp.copy()
            if i[0] not in temp_add_1:
                temp_add_1.append(i[0])
                count = check_freq(transactions, temp_add_1)
                if count >= min_sup:
                    new_dic[tuple(sorted(temp_add_1))] = count
    remove_unfreq(new_dic, min_sup)
    dic = new_dic.copy()
    

print(output)