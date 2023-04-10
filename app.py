from konlpy.tag import Hannanum

hannanum = Hannanum()

#input 문자 ',' 기준으로 split
temp1 = input()
save = []
save.append(temp1.split(","))

E_save = []
i = 0

#a = 형태소 /  b = 품사 taging
a = hannanum.morphs(temp1)
b = hannanum.pos(temp1)
print(a)
for i in range(len(a)):
  if b[i]== ['E']:
    E_save.append(b[i])
# pos taging split using array C 
c = []

# declare pos array 
N = []
J = []
P = []
E = []
M = []
# save result array as result 
result = []

# split ',' and save array c 
for i in range(len(a)):
  c.append(str(b[i][1]).split(",")) 
print(c)

# N 조사 J 격조사 P 동사 E 어미 M 수식언 
for i in range(len(a)):
  if c[i] == ['P']:
    P.append(b[i][0])
    
  elif c[i] == ['N']:
    N.append(b[i][0])

print(len(P))
print(len(N))
print(N)

for i in range(len(P)):
  print('제가 생각하기에 ' + str(i+1)+ ' 번째로 중요한 의미는 '+ str(P[i])+"다"+" 인것 같아요!")
  i+=1
  num_save = i 

if len(P) == 0 : 
  for i in range(len(N)):
    print('제가 생각하기에 ' + str(i+1)+ ' 번째로 중요한 의미는 '+ str(N[i])+" 이/가"+" 인것 같아요!")
  
elif len(P) != 0 : 
  for i in range(len(N)):
    print('제가 생각하기에 ' + str(num_save+1)+ ' 번째로 중요한 의미는 '+ str(N[i])+" 이/가"+" 인것 같아요!")
    i+=1