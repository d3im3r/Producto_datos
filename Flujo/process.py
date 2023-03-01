import sys
import simulator

if __name__ == '__main__':
    if len(sys.argv) == 1:
        simulator.process_work("2015-08-01")
    else:
        deadline=str(sys.argv[1])
        simulator.process_work(deadline)

