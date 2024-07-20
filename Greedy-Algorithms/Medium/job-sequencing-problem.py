def JobScheduling(Jobs, n):
    # Sort jobs according to the decreasing order of profit
    Jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # To keep track of free time slots
    result = [False] * n
    
    # To store the result (Count of jobs and total profit)
    count_jobs = 0
    max_profit = 0
    
    # Iterate through all given jobs
    for job in Jobs:
        # Find a free slot for this job (Note that we start from the last possible slot)
        for j in range(min(n, job.deadline) - 1, -1, -1):
            if result[j] is False:
                result[j] = True
                count_jobs += 1
                max_profit += job.profit
                break
    
    return [count_jobs, max_profit]

# Example usage
N1 = 4
Jobs1 = [(1, 4, 20), (2, 1, 10), (3, 1, 40), (4, 1, 30)]
print(JobScheduling(Jobs1, N1))  # Output: [2, 60]

N2 = 5
Jobs2 = [(1, 2, 100), (2, 1, 19), (3, 2, 27), (4, 1, 25), (5, 1, 15)]
print(JobScheduling(Jobs2, N2))  # Output: [2, 127]
