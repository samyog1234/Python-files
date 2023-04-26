dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
sort_dict= sorted(dict.items(),key=lambda x:x[1], reverse=True)
print(f"{sort_dict[0][0]}: {sort_dict[0][1]}")
print(f"{sort_dict[1][0]}: {sort_dict[1][1]}")
print(f"{sort_dict[2][0]}: {sort_dict[2][1]}")