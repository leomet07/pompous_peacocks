def unbeatable(peacocks):
	maxv = 0 # Vibrance
	maxc = 0 # Confidence

	winnersofv = set()
	for i in range(len(peacocks)):
		pck = peacocks[i]
		v , c = pck

		if v > maxv:
			maxv = v
			winnersofv = set()
			winnersofv.add(i)
		elif v == maxv:
			winnersofv.add(i)

	realwinners = 0

	for winnerindex in winnersofv:
		winner = peacocks[winnerindex]
		v , c = winner

		if c > maxc:
			realwinners = 1
			maxc = c
		elif c == maxc:
			realwinners += 1

	return realwinners


# do not modify below
total = int(input().strip())
for i in range(total):
    sumos = []
    while True:
        s = input().strip()
        if s == '':
            break
        sumo = s.split(" ")
        sumo[0] = int(sumo[0])
        sumo[1] = int(sumo[1])
        sumos.append(sumo)
    print(unbeatable(sumos))
