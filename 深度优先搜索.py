# -*- coding: utf-8 -*-
__author__ = 'iswing'
#深度优先搜索
#原理：从某个状态开始，不断转移到无法转移为止，不断重复直到找到最终的解
#可以用于数独求解
#复杂度O(2^n)
n=4
a=[1,2,4,7]
k=13
def dfs(i,sum):
    if i==n:
        return sum==k

    if dfs(i+1,sum):
        return True

    if dfs(i+1,sum+a[i]):
        return True
    else:
        return False
 if __name__=='__main__':
     if dfs(0,0):
         print 'yes'
     else:
         print 'no'

#宽度优先搜索
#和深度优先搜索类似。只是顺序搜索，同一个状态只经过一次
#可用于迷宫的最短路径判断
#复杂度O()




