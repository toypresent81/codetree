MAX_N = 5

class User:
    def __init__(self, codename="", score=0):
        self.codename = codename
        self.score = score

users = []
for i in range(MAX_N):
    codename, score = tuple(input().split())
    users.append(User(codename, int(score)))

min_user = users[0]
for user in users:
    if min_user.score > user.score:
        min_user = user

print(min_user.codename, min_user.score)




    


    
    

