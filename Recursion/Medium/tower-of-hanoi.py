class Solution:
    def toh(self, n, fromm, to, aux):
        # Your code here
        if n == 0:
            return 0 
        if n == 1:
            print("move disk " + str(n) + " from rod " + str(fromm) +
                  " to rod " + str(to))
            return 1
        move = self.toh(n-1,fromm,aux,to)
        # print(f"move disk {n} from rod {fromm} to rod {to}")
        print("move disk " + str(n) + " from rod " + str(fromm) + " to rod " +
              str(to))
        move += 1 
        move += self.toh(n-1,aux, to, fromm)
        
        return move

# Test cases
    n = 1
    total_moves = toh(n, 1, 3, 2)
    print(total_moves)  # Output should include the steps and the total number of moves
