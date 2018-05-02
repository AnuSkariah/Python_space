print ('Imported my_module...')
#import my_courses
test = 'Test string'
def find_index(to_search,target): # 2 arg : list to search and a target that we are looking for 
	'''find  the index of a value in a sequence'''
	for i,value in enumerate(to_search,target): 
		'''find the index of a value in a sequence'''
		if  value == target:
			return i 
	return -i #if doesnt return a value, it returns minus value


