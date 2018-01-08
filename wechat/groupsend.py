import itchat, time

itchat.auto_login(hotReload=True)
WISH = u'祝%s新年快乐'
friendList = itchat.get_friends(update=True)[1:]
i = 1
with open('info.txt', 'w') as f:
	for friend in friendList:
		f.write('%d.NickName:%s RemarkName:%s UserName:%s \n' % (i, friend['NickName'], friend['RemarkName'], 
									friend['UserName']))
		i +=1
		# time.sleep(.5)
	https://github.com/YueNing/tensorflowWechat.git