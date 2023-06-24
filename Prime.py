def prime(num):
    for i in range(num):
        if i>1:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i,"is a Prime Number")

num=20
prime(num)