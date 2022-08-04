# Python program to show how to use else clause with try and except clauses  
  
def reciprocal( num1 ):  
    try:  
        reci = 1 / num1  
    except ZeroDivisionError:  
        print( "We cannot divide by zero" )  
    else:  
        print ( reci )  
reciprocal( 4 )  
reciprocal( 0 )  