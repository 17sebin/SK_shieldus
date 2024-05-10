ascii = int(input('숫자 입력 : '))

min = 1
max = 127
cha = 1

while min < max:
    avg = int((min + max)/2)
    print("{}차 : ({}+{})/2={}".format(cha,min,max,avg))
    if ascii > avg:
        min = avg + 1
        print("참") 
    else:
        max = avg
        print("거짓")
    cha = cha + 1
print("아스키코드는 : " + str(min))