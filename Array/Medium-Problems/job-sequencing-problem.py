class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def find(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    parent[find(parent, y)] = find(parent, x)

def JobScheduling(Jobs, N):
    # Step 1: Sort the jobs by profit in descending order
    Jobs.sort(key=lambda x: x.profit, reverse=True)
    
    # Step 2: Initialize a parent array for union-find
    max_deadline = max(job.deadline for job in Jobs)
    parent = list(range(max_deadline + 1))
    
    # Step 3: Initialize count of jobs and total profit
    count_jobs = 0
    max_profit = 0
    
    # Step 4: Schedule the jobs
    for job in Jobs:
        # Find the latest available slot for this job
        available_slot = find(parent, min(max_deadline, job.deadline))
        
        # If a valid slot is found, schedule the job
        if available_slot > 0:
            union(parent, available_slot - 1, available_slot)
            count_jobs += 1
            max_profit += job.profit
    
    return [count_jobs, max_profit]

# Example usage:
jobs = [Job(1, 4, 20), Job(2, 1, 10), Job(3, 1, 40), Job(4, 1, 30)]
N = len(jobs)
print(JobScheduling(jobs, N))  # Output: [2, 60]

jobs = [Job(1, 2, 100), Job(2, 1, 19), Job(3, 2, 27), Job(4, 1, 25), Job(5, 1, 15)]
N = len(jobs)
print(JobScheduling(jobs, N))  # Output: [2, 127]


##################################################################################################

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        Jobs.sort(key = lambda x : x.profit, reverse = True)
        max_deadline = max(job.deadline for job in Jobs)
        
        slots = [-1] * max_deadline 
        job_count = 0
        job_profit = 0
        
        for job in Jobs:
            # j_id, deadline, profit = job 
            
            for j in range(min(max_deadline,job.deadline)-1,-1,-1):
                if slots[j] == -1:
                    slots[j] = job.id
                    job_count += 1 
                    job_profit += job.profit
                    break
        return job_count, job_profit
