﻿from collections import Counter as C
from sys import stdin as si

def bazinga():
	a,b=map(int, si.readline().split())
	d = C(list(si.readline().strip()))
	for k,v in d.items():
		if v > b :	return 'NO'
	else:
		return 'YES'

if __name__=='__main__':
	print (bazinga())


'''
A. Generous Kefa
time limit per test
2 seconds
memory limit per test
256 megabytes
input
standard input
output
standard output

One day Kefa found n baloons. For convenience, we denote color of i-th baloon as si — lowercase letter of the Latin alphabet. Also Kefa has k friends. Friend will be upset, If he get two baloons of the same color. Kefa want to give out all baloons to his friends. Help Kefa to find out, can he give out all his baloons, such that no one of his friens will be upset — print «YES», if he can, and «NO», otherwise. Note, that Kefa's friend will not upset, if he doesn't get baloons at all.
Input

The first line contains two integers n and k (1 ≤ n, k ≤ 100) — the number of baloons and friends.

Next line contains string s — colors of baloons.
Output

Answer to the task — «YES» or «NO» in a single line.

You can choose the case (lower or upper) for each letter arbitrary.
Examples
Input

4 2
aabb

Output

YES

Input

6 3
aacaab

Output

NO

Note

In the first sample Kefa can give 1-st and 3-rd baloon to the first friend, and 2-nd and 4-th to the second.

In the second sample Kefa needs to give to all his friends baloons of color a, but one baloon will stay, thats why answer is «NO».
'''
