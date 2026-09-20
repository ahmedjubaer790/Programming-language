y=5
try:
    print(y)
except NameError:
    
    print('x is not define')
except:
    print('Something went wrong')
finally:
    print('Succes')    

