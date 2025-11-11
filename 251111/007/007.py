secret_code, meeting_point, time = input().split()
time = int(time)

class Result:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time


result = Result(secret_code, meeting_point, time)
print(f"secret code : {result.secret_code}")
print(f"meeting point : {result.meeting_point}")
print(f"time : {result.time}")