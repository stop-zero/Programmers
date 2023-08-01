while True:
    try:
        N=int(input())
    except:
        break

    cnt=1
    i=1
    
    while True:
        if(cnt %N==0):
            print(i)
            break
        else:
            cnt = (cnt*10)+1;
            cnt %=N
            i+=1