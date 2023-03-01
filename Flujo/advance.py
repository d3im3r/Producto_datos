import sys
import simulator
import datetime
from datetime import datetime

if __name__ == '__main__':
    if len(sys.argv) == 1:
        simulator.main_work("2015-08-01")
    else:
        deadline=str(sys.argv[1])
        limit_1 = datetime.strptime("2015-07-01", '%Y-%m-%d')
        limit_2 = datetime.strptime("2017-08-31", '%Y-%m-%d')
        deadline = datetime.strptime(deadline, '%Y-%m-%d')
        if deadline >= limit_1 and deadline <= limit_2:
            simulator.main_work(deadline)
        else:
            print("#"*100,"Por favor ingrese una fecha comprendida entre: 2015-07-01 y 2017-08-31.".center(100,"*"),"#"*100,sep="\n")


