# A.-Minimal-Square
t = int(input())
for _ in range(t):
	a, b = map(int, input().split())
	x = max(a, b)
	y = min(a, b)
	tot = max(x, 2* y)
	tot *= tot
	print(tot)
