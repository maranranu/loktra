import sys

letters = "acdegilmnoprstuw"

def reverse_hash(hash_long):
	return_str = ""
	i = 0
	while (hash_long > 7):
		if (hash_long % 37 == 0):
			return_str = return_str + letters[i]
			i = 0
			hash_long = hash_long / 37
		else:
			hash_long = hash_long - 1
			i = i + 1


	return return_str[::-1]

print reverse_hash(int((sys.argv)[1]))


	

