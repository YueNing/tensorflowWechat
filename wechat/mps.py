import itchat

itchat.auto_login(enableCmdQR=2, hotReload=True)

mpsList = itchat.get_chatrooms()

for mp in mpsList:
	print(mp['NickName'], mp['UserName'])
