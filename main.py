# python3

def parallel_processing(n, m, data):
    output = []
    threads = [(i, 0) for i in range(n)]  # list of threads, each thread is represented by a tuple (index, time)
    for i in range(m):
        t = data[i]
        thread = min(threads, key=lambda x: x[1])  # find the thread that will finish its job the earliest
        output.append((thread[0], thread[1]))  # add the output pair
        threads.remove(thread)  # remove the thread from the list
        threads.append((thread[0], thread[1] + t))  # add the thread back with the updated time
    return output

def main():
    # read input from keyboard
    n, m = map(int, input().split())
    data = list(map(int, input().split()))
    
    # call the function
    result = parallel_processing(n, m, data)
    
    # print out the results
    for pair in result:
        print(pair[0], pair[1])

if __name__ == "__main__":
    main()
