x=list(input())
y=list(map(str,input().split(',')))
p=len(x)
print("~~~~~~~ Transition Table ~~~~~~~")
val='between'
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
            print("φ ",end=" ")
        else:
            print("q0",end=" ")
    print()      
    for a in range(p-1):
        print("q"+str(a+1),end=" ")
        for b in y:
            if b==x[a]:
                print("q"+str(a+2),end=" ")
            else:
                print("φ ",end=" ")
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
            print("φ ",end=" ")
    print()
    x=x[1:]
    for a in range(p-1):
        print("q"+str(a+1),end=" ")
        for b in y:
            if b==x[a]:
                print("q"+str(a+2),end=" ")
            else:
                print("φ ",end=" ")
        print()
    print("q"+str(len(x)+1)+"*",("φ  ")*len(y))
