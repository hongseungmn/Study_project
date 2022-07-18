# 딕셔너리의 파일 쓰기와 파일 읽기
import pickle 

# 딕셔너리 생성
# gameOption = {
#     "Sound" : 8,
#     "VideoQuality" : "HIGH",
#     "Money" : 100000,
#     "WeaponList" :["gun","missile","knife"]
# }

# file = open("save.p","wb")  # 이진 파일 오픈
# pickle.dump(gameOption,file) #딕셔너리를 피클 모듈을 이용하여 파일로 저장
# file.close()


# 딕셔너리로 출력된 파일 읽기
file = open("save.p","rb")  #이진 파일 오픈
obj = pickle.load(file)
print(obj)