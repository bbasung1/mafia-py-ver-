import random

a=int(input("인원 수는?"))
b=random.randint(1,a)
print(b)
print("마피아가 정해졌습니다.")
aa=[]
bb=[]
d=0
e=0
i=0
for i in range(0,a):
    aa.append(i+1)

def sad():
    bb.sort()
    print("죽은자 :", bb)

    
while True:
    c=int(input("마피아 일것 같은 사람의 번호를 입력하세요"))
    d+=1
    print(d,"번째 밤입니다....")
    if(c==0):
        ("마피아 게임 강제 종료")
        break
    if(c==b):
        print("맞췄습니다.")
        break
    else:
        bb.append(c)
        aa.remove(c)
    
        print("틀렸습니다.마피아가 한명을 죽이려 시도합니다....")
        e=random.choice(aa)
        
        if(e==b):
            print("마피아가 살인을 실패했습니다. 한명만 죽습니다")
            sad()
            if(len(aa)==1):
                print("마피아 승리")
                break
            continue
        print("마피아가 한명을 죽였습니다.....")
        bb.append(e)
        aa.remove(e)
        sad()
        
    if(len(aa)==1):
        print("마피아 승리")
        break
