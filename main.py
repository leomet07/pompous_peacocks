import operator
def getUnbeatable(peacocks):
	realwinners = 0

	currentwinners = [] 

	exacts = []

	changedLast = 0
	for i in range(len(peacocks)):
		pck = peacocks[i]
		

		v ,c  = pck

		if len(currentwinners) > 0:
			# print("currentwinners: ", currentwinners)
			
			

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
					change.append(pck)
					changedLast = i
					print("Changed last one:", changedLast)
					
				elif isbiggerc and isbiggerv:
					print("Beaten Both: ")
					change = []
					change.append(pck)
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
	# maxv = 0 # Vibrance
	# maxc = 0 # Confidence

	# realwinners = 0
	# winnersofv = set()
	# winnersofc = set()
	# for i in range(len(peacocks)):
	# 	pck = peacocks[i]
	# 	v , c = pck

	# 	if v > maxv:
	# 		maxv = v
	# 		winnersofv = set()
	# 		winnersofv.add(i)
	# 	elif v == maxv:
	# 		winnersofv.add(i)


	# 	if c > maxc:
	# 		maxc = c
	# 		winnersofc = set()
	# 		winnersofc.add(i)
	# 	elif c == maxc:
	# 		winnersofc.add(i)


	# for winnervindex in winnersofv:
	# 	winner = peacocks[winnervindex]
	# 	v , c = winner

	# 	if c > maxc:
	# 		realwinners = 1
	# 		maxc = c
	# 	elif c == maxc:
	# 		realwinners += 1


		
	# print("Winners of c: ", winnersofc)
	# if len(winnersofc) > 1:

	# 	tempmaxv = 0
	# 	n = 0
	# 	for winnercindex in winnersofc:
	# 		winner = peacocks[winnercindex]
	# 		v , c = winner

	# 		if v > tempmaxv:
	# 			tempmaxv = v
	# 			n = 1
	# 		elif v == tempmaxv:
	# 			n += 1

	# 		print(winner)

	# 	print(n)
	# 	realwinners += n
	


	return realwinners

if __name__ == "__main__":
	

	# peacocks = [[1 ,3], [0 ,5]] # v ,c
	# peacocks = [[1 ,2], [1 , 4],] # v ,c
	# peacocks = [[1 ,3], [0 , 5], [1 , 5]] # v ,c
	# peacocks = [[3 ,4], [3, 4], [3 , 4]]
	peacocks = [[1 ,3], [2, 3] ,  [ 2, 3 ] , [0 ,5]] # v ,c

	print("unbeatable peacocks: " , getUnbeatable(peacocks))
	

		# if c > max
		



