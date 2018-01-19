import itchat, time

itchat.auto_login(hotReload=True)
friendList = itchat.get_friends(update=True)[1:]
i = 1
total = len(friendList)
male = female = other =0
for friend in friendList:
    if friend['Sex'] == 1:
        male += 1
    if friend['Sex'] == 0:
        female += 1
    else:
        other += 1
print(male ,female, other, total)
#with open('info.txt', 'w') as f:
#	for friend in friendList:
#		f.write('%d.NickName:%s RemarkName:%s UserName:%s \n' % (i, friend['NickName'], friend['RemarkName'], 
#									friend['UserName']))
#		i +=1
		# time.sleep(.5)
#	https://github.com/YueNing/tensorflowWechat.git
