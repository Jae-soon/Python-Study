import pickle

# 파일 입력
profile_file = open("profile.pickle", "wb")
profile = {"이름" : "박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장
profile_file.close()

# 파일 불러오기
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)
print(profile)
profile_file.close()