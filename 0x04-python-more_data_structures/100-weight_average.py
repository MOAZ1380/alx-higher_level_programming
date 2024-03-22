#!/usr/bin/python3
def weight_average(my_list=[]):

	f = 0
	d = 0
	c = 0
	for i in my_list:
		f += i[0] * i[1]
		d += i[1]
	c = f / d
	return c
