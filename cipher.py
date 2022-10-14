countPrime = 3
flag = True

def primeNumber():
    global countPrime
    global flag
    for i in range(countPrime+1,100000000000000):
        # print(countPrime)
        for j in range(2,int(i/2)+1):
            if i%j==0:
                flag = False
                pass
        if flag == True:
            countPrime = i
            return i
        countPrime = countPrime +1


for i in range(10):
    print(primeNumber())



def cipherr(context):
    for i in context:

        x = chr(ord(i) + 3)
