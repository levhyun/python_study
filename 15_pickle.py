# 피클 (파일 입출력)

import pickle

p_file = open("p_file.pickle", "wb")
file = {"1,2,3,4,5,6,7,8,9,10"}
print(file)
pickle.dump(file,p_file)
p_file.close()

with open("p_file.pickle", "rb") as p_file:
    print(pickle.load(p_file))