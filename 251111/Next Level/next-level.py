user2_id, user2_level = input().split()
user2_level = int(user2_level)

class Info:
    def __init__(self, user2_id = "codetree", user2_level = 10):
        self.user2_id = user2_id
        self.user2_level = user2_level

info1 = Info()
print(f"user {info1.user2_id} lv {info1.user2_level}")
info2 = Info(user2_id, user2_level)
print(f"user {info2.user2_id} lv {info2.user2_level}")
