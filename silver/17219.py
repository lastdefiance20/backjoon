import sys

N, M = map(int, sys.stdin.readline().split())

pwd_dic = {}

for i in range(N):
    url, pwd = sys.stdin.readline().split()
    pwd_dic[url] = pwd

for i in range(M):
    url = sys.stdin.readline().rstrip()
    print(pwd_dic[url])