n = int(input())

class User:
    def __init__(self, name, street_address, region):
        self.name = name
        self.street_address = street_address
        self.region = region

users = []
for _ in range(n):
    n_i, s_i, r_i = input().split()
    user = User(n_i, s_i, r_i)
    users.append(user)

max_user = users[0]
for user in users:
    if max_user.name < user.name:
        max_user = user

print(f"name {max_user.name}")
print(f"addr {max_user.street_address}")
print(f"city {max_user.region}")


