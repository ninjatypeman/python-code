dict_ticket = {'G1011': ['上海-南京', '09:30', '10:30', '1小时'],
               'G1089': ['北京-南京', '09:30', '10:30', '5小时'],
               'G1088': ['北京-广州', '09:30', '10:30', '10小时'],
               'G1099': ['哈尔滨-广州', '09:30', '10:30', '15小时']}
for key in dict_ticket.keys():
    print(key, end=' ')  # 不换行
    for item in dict_ticket.get(key):  # get()根据 key 获取值，返回一个列表；而 dict_ticket.items()返回所有键值对。
        print(item, end='\t')
    print()  # 换行

train_id = input('请输入你要购买的车次：')
train_info = dict_ticket.get(train_id, '车次不存在')

if train_info != '车次不存在':
    passengers = input('请输入乘客的姓名：')
    print(
        f"恭喜你，购票成功！乘车人：{passengers}，车票信息：{train_info[0]}，出发时间：{train_info[1]}，到达时间：{train_info[2]}，全长：{train_info[3]}。")
else:
    print('你输入的车次不存在！')
