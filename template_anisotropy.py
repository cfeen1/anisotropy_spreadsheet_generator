import csv
# Ask for a file name.
file_name = input("Enter the name of the file: ")
# Create the new file
out_file = open(file_name + '.csv', 'w', newline='')
out_file_writer = csv.writer(out_file)

# Writing the header row
out_file_writer.writerow(['Injection', 'Protein(uM)',
	'amt to add(uL)', 'total volume(uL)', 'stock(uM)', 'anisotropy'])
	
# injection number
i = 1.0		
# Protein concentration
p = 0.0
# amt to add
a = 0.0
# total volume
v = 0.0
# stock protein
s = 0.0
# cuvette volume
c = 500

# These conditions change per experiment, ask user to input them.  
inject_amt = int(input("How many injections would you like? "))
start_amt = float(input("Desired [protein] for first injection(uM): "))
stock_prot = float(input("What is your stock protein concentration(uM)? "))

while i < inject_amt + 1:
	"""Each loop, write the updated values to the row and stop
	when the loop reaches the number of desired injections.""" 
	out_file_writer.writerow([i, p, a, v, s])
	# Each loop through, add 1 to the injections.  
	i += 1
	# Check to see if the protein concentration is 0, if it is, add
	# the desired starting amount to p.  The start of injections.  
	if p == 0:
		p += start_amt
		# Check if the volume added is above 1uL when using the stock
		# protein concentration.  
		a = ((p * c)/ stock_prot)
		# If it isn't, use a lower protein stock concentration, in this
		# case, use the concentration that yields 1uL for the first 
		# injection based on the user input starting amount.  
		if a < 1:
			a = ((p * c)/ (start_amt * c))
			s = start_amt * c
		else:
			a = ((p * c)/ (stock_prot))
			s = stock_prot
	# Else, very similar to the if above but for all other injections
	# besides the first.  
	else:
		p *= 2
		a = (((p-old) * c)/ stock_prot)
		if a > 1:
			a = (((p-old) * c)/ (stock_prot))
			s = stock_prot
		else:
			a = (((p-old) * c)/ (start_amt * c))
			s = start_amt * c
	
	# Since, with each injection, protein is being added, we need to 
	# keep track of how much protein is already in cuvette for calculating
	# how much to add nex time.  So at the end of the loop we store the
	# old protein amount as old and use it on the next loop through.  	
	old = p
	
	# It is also import to keep track of the volume added because you 
	# need to stay under 10% of the cuvette volume to reduce error
	# in the experiment.  
	# Here, we add the amount each time to the total volume.  
	v += a
	
