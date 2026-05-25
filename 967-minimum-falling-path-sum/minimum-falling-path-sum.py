class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        # Dynamic programming attempt 1
        # min_dist = {}

        # for row in range(1, len(matrix) ) : 

        #     for col in range( len(matrix[row]) ) :
        #         print('1',min_dist)

        #         num_cols = len(matrix[row])
        #         ind = row*num_cols + col + 1

        #         print(ind, row, col)

        #         min_dist[ind] = 100000

        #         if ( ind - num_cols in min_dist.keys() ) :
                    
        #             min_dist[ind] = min(min_dist[ind] , min_dist[ind - num_cols] + matrix[row][col] )
                    
        #         elif ( ind - num_cols + 1 in min_dist.keys() ) :
        #             # print('1.5' ,min_dist[ind] , min_dist[ind - num_cols] , matrix[row][col])
        #             min_dist[ind] = min(min_dist[ind] , min_dist[ind - num_cols +1] + matrix[row][col] )
                    
        #         elif ( ind - num_cols -1 in min_dist.keys() ):
        #             min_dist[ind] = min(min_dist[ind] , min_dist[ind - num_cols -1] + matrix[row][col] )

        #         elif row-1 == 0:
        #     if ( col -1 ) > 0 and col + 1 < len(matrix[row]) :
        #         min_dist[ind] =  min( matrix[row - 1][col] , matrix[row - 1][col-1] , matrix[row - 1][col+1] )
        #     elif ( col -1 ) < 0 : 
        #         min_dist[ind] =  min( matrix[row - 1][col] , matrix[row - 1][col+1] )
        #     elif ( col + 1 ) > 0 : 
        #         min_dist[ind] =  min( matrix[row - 1][col] , matrix[row - 1][col-1] )

        # print('2', min_dist)

        # Dynamic programming attempt # using Genai
        n = len(matrix)

        dp = [[0] * n for _ in range(n)]

        # first row stays same
        for col in range(n):
            dp[0][col] = matrix[0][col]

        for row in range(1, n):

            for col in range(n):

                best = dp[row - 1][col]

                if col - 1 >= 0:
                    best = min(best, dp[row - 1][col - 1])

                if col + 1 < n:
                    best = min(best, dp[row - 1][col + 1])

                dp[row][col] = matrix[row][col] + best

        return min(dp[n - 1])
                    



        