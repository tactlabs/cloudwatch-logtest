'''
Created on 
Course work: 
@author:
Source:
    
'''

# Import necessary modules
from datetime import datetime
import const
import culog


def startpy():
    time = datetime.now()
    print(time)
    culog.info(f'time : {time}')



if __name__ == '__main__':
    startpy()