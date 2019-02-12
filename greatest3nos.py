# your code goes here
inputs=input().split()
fn=int(inputs[0])
sn=int(inputs[1])
tn=int(inputs[2])
if fn>=sn and fn>=tn:
	print(fn)
elif sn>=fn and sn>=tn:
	print(sn)
else:
	print(tn)
