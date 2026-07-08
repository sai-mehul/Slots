convergence_test = 0.2

simulated_rtp = []
hit_rate = []
n_units = []

convergence = 1

n = 100

wins = 0
payouts = 0
total_spins = 0

while convergence > convergence_test:

    for _ in range(n):

        spin = np.random.choice(reelvals, size=3)
        reel = "".join(spin)

        if reel in payout:
            wins += 1
            payouts += payout[reel]

    current_rtp = payouts / n
    current_hitrate = wins / n

    simulated_rtp.append(current_rtp)
    hit_rate.append(current_hitrate)
    n_units.append(total_spins)

    convergence = abs(current_rtp - theoretical_rtp)/theoretical_rtp

    
    n_units.append(n)
    n *= 10
