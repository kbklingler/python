#! /usr/bin/env python3

zoo_dict = {'lion': 420, 'rabbit': 2, 'giraffe': 1800, 'bear': 500}

for (k,v) in zoo_dict.items():
	if v>=20:
		print(k, "big")
	else: 
		print(k, "small")




