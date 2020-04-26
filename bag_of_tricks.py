class BagOfTricks:
	def kadane_max_subarray(self, arr: list) -> int:
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
