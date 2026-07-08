import numpy as np 
import matplotlib.pyplot as plt 

convergence_test = 0.02

simulated_rtp = []
hit_rate = []
n_units = []

convergence = 1

n = 100

wins = 0
total_payouts = 0
payouts = []
total_spins = 0
error_convergence = [] 

batch = 1000 

while convergence >= convergence_test:
    
    for _ in range(batch):

        total_spins += 1

        spin = np.random.choice(reelvals, size=3)
        reel = "".join(spin)

        if reel in payout:
            wins += 1
            total_payouts += payout[reel]
            payouts.append(payout[reel])
            

        current_rtp = total_payouts / total_spins
        current_hitrate = wins / total_spins

        simulated_rtp.append(current_rtp)
        hit_rate.append(current_hitrate)
        n_units.append(total_spins)

        convergence = abs(current_rtp - theoretical_rtp)


    error_convergence.append(convergence)

    
    n *= 10



payout_variance = np.var(payouts)


# Histogram
plt.figure(figsize=(6,4))
plt.hist(payouts)
plt.xlabel("Payout")
plt.ylabel("Frequency")
plt.title("Distribution of Slot Payouts")
plt.show()

# RTP Convergence
plt.figure(figsize=(6,4))
plt.plot(n_units, simulated_rtp, label="Simulated RTP")
plt.axhline(
    y=theoretical_rtp,
    linestyle="--",
    color="red",
    label="Theoretical RTP"
)
plt.xlabel("Total Spins")
plt.ylabel("RTP")
plt.title("RTP Convergence")
plt.legend()
plt.show()

# Hit Rate Convergence
plt.figure(figsize=(6,4))
plt.plot(n_units, hit_rate, label="Hit Rate")
plt.axhline(
    y=hit_rate,   # <-- use theoretical hit rate here
    linestyle="--",
    color="blue",
    label="Theoretical Hit Rate"
)
plt.xlabel("Total Spins")
plt.ylabel("Hit Rate")
plt.title("Hit Rate Convergence")
plt.legend()
plt.show()



simulated_rtp_mean = np.mean(payouts)
std = np.std(payouts,ddof=1)
se = std/np.sqrt(total_spins)


lower = simulated_rtp_mean - 1.96*se
upper = simulated_rtp_mean + 1.96*se

print(f"95% Confidence Interval: ({lower:.5f}, {upper:.5f})")
