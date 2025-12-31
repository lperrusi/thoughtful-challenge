def is_bulky(width, height, length):
	"""
	Determines whether a package is bulky based on volume
    or individual dimension thresholds.
	"""

	volume = (width * height)*length
	if volume >= 1000000:
		return True
	if width >=150 or height >= 150 or length>=150:
		return True
	return False

def is_heavy(mass):
	"""
	Determines whether a package is heavy based on mass.
	"""
	return mass >= 20

def sort(width, height, length, mass):
	"""
	Determines the appropriate dispatch stack for a package.
	Based on the package dimensions and mass.
	"""
	isBulky = is_bulky(width, height, length)
	isHeavy = is_heavy(mass)

	if isBulky and isHeavy:
		return "REJECTED"
	elif isBulky or isHeavy:
		return "SPECIAL"
	else:
		return "STANDARD"



def test_sort():
	assert sort(10, 10,15,5) == "STANDARD"
	assert sort(10, 10,15,50) == "SPECIAL"
	assert sort(10, 10,150,2) == "SPECIAL"
	assert sort(10, 10,150,50) == "REJECTED"
	assert sort(-10000, 10000000000000000000000,15000000000000000000000000000000000,500000000000000000000) == "REJECTED"

