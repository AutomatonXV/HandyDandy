#Eq 5.33 from Modest
N = 3 #number of objects

def symboi(s,i):
    return s+str(i)
    
for i in range(1,N+1):
    eq = "i = "+str(i) +": \t"
    eq += symboi("q",i) +"/" + symboi("e",i)
    for j in range(1,N+1):
        if j == i: continue
        eq += " - (1/" + symboi("e",j) + " - 1)" + "F_("+str(i)+"-"+str(j)+")"+symboi("q",j)
    eq += " + "+symboi("Ho",i)+ " = "
    for j in range(1,N+1):
        if j == 1: continue
        eq += "+ F_("+str(i)+"-"+str(j)+")" + "[" + symboi("E_(b",i)+") - "+symboi("E_(b",j)+")"+"]"
    print(eq)
