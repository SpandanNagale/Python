def onepyramid(a):                                         #these is the onesided pyramid
                                                          
    stars=1
    maxcol=a
    for i in range(a):
        maxspace=a-1
        print(stars*"*"+ maxspace* " ")
        stars=stars+1

a=int(input('enter the number height'))
onepyramid(a)    




