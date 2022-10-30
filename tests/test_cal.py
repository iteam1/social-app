from app.calculations  import add

def test_add():
	'''
	the test pass if using this function without any error
	the naming must be test_* some
	'''
	print('testing add function')
	sum = add(5,3)
	assert 8 == sum

if __name__ == "__main__":
	
	test_add()
