# Run this with python multiprocessing_demo.py from the command line.
# It will not work in IPython.

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

def occupy(x):
    count = x
    for i in range(1, 1000):
        count += i
    return count


# it will only work if run in the name == main block
if __name__ == "__main__":
    print('.submit method for multiprocessing')
    jobs = []
    with ProcessPoolExecutor() as executor:
        for i in range(4):
            job = executor.submit(occupy, i)
            jobs.append(job)

    for job in jobs:
        print(job.result())

    print('.map method for multiprocessing')        
    # or, you can do it this way
    with ProcessPoolExecutor() as executor:
        results = [r for r in executor.map(occupy, range(4))]

    print(results)


    print('threading demo')
    jobs = []
    with ThreadPoolExecutor() as executor:
        for i in range(4):
            job = executor.submit(occupy, i)
            jobs.append(job)

    for job in jobs:
        print(job.result())