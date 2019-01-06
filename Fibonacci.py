def sumFibs(num):
    Fib = [1,1]
    Soln = 2
    i = 0
    while i >= 0:
        new_Fib = Fib[i] + Fib[i+1]
        Fib.extend([new_Fib])
        if new_Fib > num:
                break  
        if new_Fib <= num and new_Fib%2 != 0:
            Soln = Soln + new_Fib
            i += 1
        else:
            i += 1
    return(Soln)
        
