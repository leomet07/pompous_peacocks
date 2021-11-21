def unbeatable(peacocks):
	realwinners = 0
	currentwinners = [] 
	exacts = []

	changedLast = 0
	for i in range(len(peacocks)):
		pck = peacocks[i]
		v , c  = pck

		if len(currentwinners) > 0:
			change = currentwinners
			
			for it in range(len(currentwinners)):
				w = currentwinners[it]
				print("NEWBOI: ", change)
				
				isbiggerv = v > w[0]	
				isbiggerc = c > w[1]
				
				if (isbiggerv or isbiggerc) and not((isbiggerv and isbiggerc)):
					print("Beaten only one: ", w, pck)
					
					if v == w[0] or c == w[1]:
						print("RESET")
						change = []
						exacts = []
					change.append(pck)
					changedLast = i
					print("Changed last one:", changedLast)
					
				elif isbiggerc and isbiggerv:
					print("Beaten Both: ")
					change = []
					change.append(pck)
					exacts = []
					changedLast = i

					print("Changed last both: ", changedLast)
					
				elif v == w[0] and c == w[1]:
					if changedLast < i:
						print("--------------------Exact match", w, pck, changedLast, i)
						print(v , w[0], c , w[1])
						exacts.append(pck)

				print("ENDBOI: ", change)
			currentwinners = change

		if i == 0:
			currentwinners.append(pck)

	print("end winners: ", currentwinners)
	print("end exacts", exacts)
	realwinners = len(currentwinners) + len(exacts)

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
