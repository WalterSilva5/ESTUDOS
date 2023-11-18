from array import array

l = [1, 2, 3, 4]

floats = array('d', l)

fil = open('sample.txt', 'wb')

floats.tofile(fil)
