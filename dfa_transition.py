x=list(input())
y=list(map(str,input().split(',')))
val='between'
def dfatrans(x,y,val):
    p=len(x)
    print("~~~~~~~ Transition Table ~~~~~~~")
    
    if val=='starts':
        print("δ",end="  ")
        print("  ".join(y))
        for a in range(p):
            print("q"+str(a),end=" ")
            for b in y:
                if b==x[a]:
                    print("q"+str(a+1),end=" ")
                else:
                    print("φ",end=" ")
            print()
        print("q"+str(len(x)+1)+"*",("q"+str(len(x)+1)+" ")*len(y))
    if val=='ends':
        print("δ",end="  ")
        print("  ".join(y))
        print("q0",end=" ")
        for a in y:
            if a==y[0]:
                print("q1",end=" ")
            else:
                print("q0",end=" ")
        print()      
        for a in range(p-1):
            print("q"+str(a+1),end=" ")
            for b in y:
                if b==x[a]:
                    print("q"+str(a+2),end=" ")
                else:
                    print("q0",end=" ")
            print()
        print("q"+str(len(x))+"*","q0 "*len(y))

    if val=='between':
        print("δ",end="  ")
        print("  ".join(y))
        print("q0",end=" ")
        for a in y:
            if a==y[0]:
                print("q1",end=" ")
            else:
                print("q0",end=" ")
        print()
        x=x[1:]
        for a in range(p-1):
            print("q"+str(a+1),end=" ")
            for b in y:
                if b==x[a]:
                    print("q"+str(a+2),end=" ")
                else:
                    print("q0",end=" ")
            print()
        print("q"+str(len(x)+1)+"*",("q"+str(len(x)+1)+" ")*len(y))
dfatrans(x,y,val)
