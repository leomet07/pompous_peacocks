def getUnbeatable(peacocks):
	maxv = 0 # Vibrance
	maxc = 0 # Confidence

	realwinners = 0
	winnersofv = set()
	winnersofc = set()
	for i in range(len(peacocks)):
		pck = peacocks[i]
		v , c = pck

		if v > maxv:
			maxv = v
			winnersofv = set()
			winnersofv.add(i)
		elif v == maxv:
			winnersofv.add(i)


		if c > maxc:
			maxc = c
			winnersofc = set()
			winnersofc.add(i)
		elif c == maxc:
			winnersofc.add(i)


	for winnervindex in winnersofv:
		winner = peacocks[winnervindex]
		v , c = winner

		if c > maxc:
			realwinners = 1
			maxc = c
		elif c == maxc:
			realwinners += 1


		
	print("Winners of c: ", winnersofc)
	if len(winnersofc) > 1:

		tempmaxv = 0
		n = 0
		for winnercindex in winnersofc:
			winner = peacocks[winnercindex]
			v , c = winner

			if v > tempmaxv:
				tempmaxv = v
				n = 1
			elif v == tempmaxv:
				n += 1

			print(winner)

		print(n)
		realwinners += n
	


	return realwinners

if __name__ == "__main__":
	

	# peacocks = [[1 ,3], [0 ,5]] # v ,c
	# peacocks = [[1 ,2], [1 , 4],] # v ,c
	peacocks = [[1 ,3], [0 , 5], [1 , 5]] # v ,c
	# peacocks = [[1 ,3], [2, 3] ,  [ 2, 3 ] , [0 ,5]] # v ,c

	print("unbeatable peacocks: " , getUnbeatable(peacocks))
	

		# if c > max
		



