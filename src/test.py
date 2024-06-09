
from logs import logger

def start(a: int, b: int):
    
    if a == 5 and b == 8: 
        logger('CRITICAL', 'invalid values')
        return
    
    if a == 4 and b == 7: logger('WARNING', 'Warning values')
    
    list = []
    list.append(a + b)
    list.append(a - b)
    list.append(a * b)
    list.append(a / b)

    write('DEBUG', 'Result is returned')
    return list



if __name__ == '__main__':
    logger('INFO', 'Service is started')
    
    var1 = int(input('>>> '))
    var2 = int(input('>>> '))
    
    logger('DEBUG', f'variable one is {var1}. Variable two is {var2}')
    
    logger('DEBUG', 'functions "start" is running')
    total = start(var1, var2)
    
    logger('INFO', f'Result >>> {total}')
    