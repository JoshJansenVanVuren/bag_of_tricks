class BagOfTricks:
	@staticmethod
	def kadane_max_subarray(arr: list) -> int:
		"""
		Parameters
		----------
		arr : str
		The array to search through

		Returns
		-------
		best_so_far : int
		Largest sum of any sub array
		"""
		
		best_so_far = 0
		current = 0

		for i in arr:
			current = max(0,current + i)
			best_so_far = max(best_so_far,current)

		return best_so_far

	"""
	Sorting Algorithms XD
	"""

	@staticmethod
	def bubble_sort(vals,timeout = 0):
		#TODO: add in timeout functionality
		"""Sort an array via bubble sort

		This algorithm compute scales quadratically n^2

		Arguments:
		vals : []
			List of vals, must be comparable
		timeout : int
			ms value of how long the algorithm should wait between steps
			useful for comparing animations of sorting

		Returns:
		vals : []
			The sorted list
		"""
		sorted = False
		while not sorted:
			sorted = True
			for i in range(len(vals)-1):
				if vals[i] > vals[i+1]:
					temp = vals[i]
					vals[i] = vals[i+1]
					vals[i+1] = temp
					sorted = False

		return vals

	@staticmethod
	def quick_sort(vals,timeout = 0):
		#TODO: add in timeout functionality
		"""Sort an array via quick sort

		This algorithm compute scales as n*log(n) in the best
		case and n^2 in the worst.

		We utilise here the variation where pivot is around the last value

		Arguments:
		vals : []
			List of vals, must be comparable
		timeout : int
			ms value of how long the algorithm should wait between steps
			useful for comparing animations of sorting

		Returns:
		vals : []
			The sorted list
		"""

		# because the algorithm is recursive its easier
		# if the user doesnt get exposed to the details
		BagOfTricks.inner_quick_sort(vals,0,len(vals)-1)

		return vals
	
	@staticmethod
	def inner_quick_sort(vals,lower,higher):
		"""Local function for implementation of quick sort

		Function finds the value to partition over
		Then recursively calls the sort until the 
		array is completely split

		Arguments:
		vals : []
			Array of partially sorted elements
		lower : int
			Index in array of lower index to loop through
		higher : int
			Index in array of higher index to loop through
		"""
		if lower < higher:
			# find the point to split over
			pi = BagOfTricks.partition_quick_sort(vals,lower,higher)

			# recursively call quick sort over the split arrays
			BagOfTricks.inner_quick_sort(vals,lower,pi - 1)
			BagOfTricks.inner_quick_sort(vals,pi + 1,higher)

	@staticmethod
	def partition_quick_sort(vals,lower,higher):
		"""Partition an array for quick sort

		Function loops over partition

		and places the partition in the correct place
		i.e. it places all values higher to the right
		and all values lower to the left
		"""
		pivot_val = vals[higher]

		i = lower - 1

		for j in range(lower,higher):
			if vals[j] <= pivot_val:
				i += 1
				# swap
				temp = vals[j]
				vals[j] = vals[i]
				vals[i] = temp
		temp = vals[i+1]
		vals[i+1] = vals[higher]
		vals[higher] = temp

		return i + 1

	@staticmethod
	def merge_sort(vals,timeout = 0):
		#TODO: add in timeout functionality
		"""Sort an array via quick sort

		This algorithm is similar in nature to
		quick sort in that it to is a 'divide
		and conquer' algorithm however merge
		sort has better worse case performance

		Scales with n log(n) in all cases

		Arguments:
		vals : []
			Array to be sorted
		timeout : int
			ms value of how long the algorithm should wait between steps
			useful for comparing animations of sorting

		Returns:
		vals : []
			The sorted list
		"""

		# split until only one entry in vals
		if len(vals) > 1:
			# split the array over the midpoint
			mid_point = len(vals)//2 

			left_split = vals[:mid_point]
			right_split = vals[mid_point:]

			# recursively call merge sort on the left and right
			BagOfTricks.merge_sort(left_split)
			BagOfTricks.merge_sort(right_split)

			vals.clear() # reset vals to reinput the sorted elements
			while len(left_split) > 0 and len(right_split) > 0:
				if left_split[0] <= right_split[0]:
					vals.append(left_split[0])
					left_split.pop(0)
				else:
					vals.append(right_split[0])
					right_split.pop(0)
			
			for i in left_split:
				vals.append(i)
			for i in right_split:
				vals.append(i)

		return vals