# Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Score: 10


n = int(input())
arr = list(map(int, input().split()))
  arr = Counter(map(int, raw_input().split())).keys()
    arr.sort()
    print arr[-2]
