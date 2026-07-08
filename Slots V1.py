import numpy as np 

reelvals = ['A','B','C','D']

payout = {'AAA':10,'BBB':6,'CCC':4,'DDD':2}

theoretical_rtp = sum((1/4)**3 * value for value in payout.values())

n = 10000000

wins = 0 
payouts = 0

for i in range(n):
    spin1 = np.random.choice(reelvals,size = 3)

    reel = "".join(spin1)


    if reel in payout:
        wins += 1
        payouts += payout[reel]

simulated_rtp = payouts/n
hitrate = wins/n
