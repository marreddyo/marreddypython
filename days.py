Days=['yesterday','tomorrow','today','dayafter']
for value in Days:
	print value,len(value)
	print value[:Days.index(value)+1].upper()+value[Days.index(value)+1:]
	
	
