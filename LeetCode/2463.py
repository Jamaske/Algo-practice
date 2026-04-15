from collections import deque
from math import inf

class Solution:
    TC = [
        [[0,4,6], [[2,2],[6,2]]],
        [[1,-1], [[-2,1],[2,1]]],
        [[9,11,99,101], [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]],
        [[9486709,305615257,214323605,282129380,763907021,-662831631,628054452,-132239126,50488558,381544523,-656107497,810414334,421675516,-304916551,571202823,478460906,-972398628,325714139,-86452967,660743346],
         [[-755430217,18],[382914340,2],[977509386,4],[94299927,9],[32194684,16],[-371001457,2],[-426296769,13],[-284404215,8],[-421288725,0],[-893030428,2],[291827872,17],[-766616824,8],[-730172656,17],[-722387876,1],[510570520,20],[756326049,7],[-242350340,14],[6585224,19],[-173457765,15]]]
    ]
    cnt1 = 0
    cnt2 = 0

    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort(key = lambda x:x[0])
        N = len(factory)
        M = len(robot)
        capacity = [0] * (N+1)
        acc = 0
        for j, (pos, lim) in enumerate(factory):
            acc += lim
            capacity[j+1] = acc

        dc = [1 << 60]*(M+1)
        dc[-1] = 0
        dn = [0]*(M+1)
        for j in range(N):
            pos, lim = factory[j]
            for i in range(M):
                best = dc[i]
                acc = 0
                #pre sum acc
                k = i
                while k > capacity[j]:
                    r = robot[k]
                    acc += abs(pos - r)
                    k -= 1
                    self.cnt1+=1
                #both acc and valid best examination
                while k > max(i-lim, -1):
                    r = robot[k]
                    acc += abs(pos - r)
                    x = acc + dc[k-1]
                    print(f'{x:<6} ', end='')
                    best = min(best, x)
                    k -= 1
                    self.cnt2+=1
                dn[i] = best
                print('')
            print('===========')
            dn, dc = dc, dn
        return dc[-2]
    
    def reference(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        m, n = len(robot), len(factory)
        dp = [[0]*(n+1) for _ in range(m+1)] 
        for i in range(m): dp[i][-1] = 1 << 60 
        for j in range(n-1, -1, -1): 
            prefix = 0 
            qq = deque([(m, 0)])
            for i in range(m-1, -1, -1): 
                prefix += abs(robot[i] - factory[j][0])
                if qq[0][0] > i+factory[j][1]: qq.popleft()
                while qq and qq[-1][1] >= dp[i][j+1] - prefix: qq.pop()
                qq.append((i, dp[i][j+1] - prefix))
                dp[i][j] = qq[0][1] + prefix
        return dp[0][0]

    
    def runCase(self, n):
        print(self.reference(*self.TC[n]))
        print(self.cnt1, self.cnt2)

if __name__ == "__main__":
    Solution().runCase(0)
