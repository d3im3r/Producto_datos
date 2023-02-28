import sys
import simulator

if __name__ == '__main__':
    if len(sys.argv) == 1:
        simulator.process_work(1)
    else:
        n_days=int(sys.argv[1])
        simulator.process_work(n_days)

