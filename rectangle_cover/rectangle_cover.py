### rectangle_cover.py
### 
### Author:	Graeme Douglas
### Info:	A rectangle cover calculation.
###		
###		The problem is: given a rectangle with integral width
###		and height, find the smallest number of squares with
###		integral dimensions that completely fills the square.
###		Problem originally formulated in the "Colourful Challenges"
###		section of the September 2012 ACM publication.
###		
###		My only question: Can this problem be solved "greedily"?

import sys

def rectangleCover(w, h):
	# Some initial setup/guards.  Width always less than or equal to height.
	if w == 0 or h == 0:
		return 0
	elif w == h:
		return 1
	elif w == 1 or h == 1:
		return w*h
	elif w > h:
		temp = w
		w = h
		h = temp
	
	# The current best.  Wish to minimize.
	best = w*h
	
	# For each potential square size ...
	for i in range(w, 0, -1):
		# Num of i*i squares that fit per width.
		j = w / i
		
		# Optimization: when j >= 2, better off with j*i sized sqares.
		if j >= 2:
			break
		
		# Number of squares high.
		k = h / i;
		
		# Two potential calculations, depending on how you form
		# remaining rectangles.  Do both, take min.
		test1 = k*j + rectangleCover(w % i, h)+rectangleCover(i, h % i)
		test2 = k*j + rectangleCover(w % i, k)+rectangleCover(w, h-i*j)
		
		# Keep the best overall solution found so far.
		if test1 < best:
			best = test1
		if test2 < best:
			best = test2
	
	# Finally, return.
	return best

# Defaults.
if __name__ == '__main__':
	w = 1
	h = 1
	if sys.argv[1]:
		h = int(sys.argv[1])
	if sys.argv[2]:
		w = int(sys.argv[2])
	
	print rectangleCover(h, w)
