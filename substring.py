# idont know y this is taking very high large time on codechef
# while this is working on my mac in just 0.002 seconds

T = input()
ans_list = []
for tc in range(T):
	N = input()
	S = raw_input()
	ans = 0
	for i in range(N):
		if S[i] == '0':
			continue
		for j in range(i,N):
			if S[j] == '1':
				ans = ans + 1
	ans_list.append(ans)
for a in ans_list:
    print(a)
