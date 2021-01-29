#code
count1 = 0
for j in range(0,1000):
    a = input()
    
    min1=int(a[0])
    max1=int(a[2:4])
    if a[1] == '-':
        if a[3] == ' ':
            str = a[4]
            str1 = a[7:len(a)]
            if str1[min1]==str or str1[max1]==str:
                count1 += 1
        else:
            str = a[5]
            str1 = a[8:len(a)]
            if str1[min1]==str or str1[max1]==str:
                count1 += 1
    else:
        str = a[6]
        min1 = int(a[0:2])
        max1 = int(a[3:5])
        str1 = a[9:len(a)]
        if str1[min1]==str or str1[max1]==str:
            count1 += 1

print(count1)
