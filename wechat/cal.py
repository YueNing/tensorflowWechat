import itchat
itchat.login()
friends = itchat.get_friends(update=True)[0:]

male = female = other = 0
for friend in friends[1:]:
    sex = friend['Sex']
    if sex == 1:
        male +=1
    if sex == 0:
        female +=1
    else:
        other +=1
total = len(friends[1:])
print total, male, female
