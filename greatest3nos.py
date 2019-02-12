inputs=input().split()
fn=int(inputs[0])
sn=int(inputs[1])
tn=int(inputs[2])
if fn>sn&fn>tn:
	print(fn)
elif sn>fn&sn>tn:
	print(sn)
else:
	print(tn)
