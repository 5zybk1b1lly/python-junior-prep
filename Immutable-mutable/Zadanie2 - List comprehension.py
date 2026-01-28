sell = [100, 200, 300, 400, 500]
podwojone = [x*2 for x in sell if x > 200]

print(sell)
print(podwojone)

parzyste_ind = [sell[i] for i in range(len(sell)) if i%2==0 ]
print(parzyste_ind)

