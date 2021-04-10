class BagOfTricks:
    """Various algorithms for solving typical computer science
    style interview questions

    Methods:
    kadane_max_subarray(arr)
        Find the largest contigious sum of elements in a list

    bubble_sort(vals)
        Applies a basic bubble sort

    quick_sort(vals)
        Sort an array via quick sort

    merge_sort(vals)
        Sort an array via merge sort
    """
    @staticmethod
    def kadane_max_subarray(vals: list) -> int:
        """Find the largest contigious sum of elements in a list
        
        Arguments:
        arr : []
        The list to search through
        
        Returns:
        best_so_far : int
        Largest sum of contigious elements
        """
        
        best_so_far = 0
        current = 0
        
        for ele in vals:
            current = max(0,current + ele)
            best_so_far = max(best_so_far,current)
        
        return best_so_far
    
    ######################
    # Sorting Algorithms #
    ######################
    
    @staticmethod
    def bubble_sort(vals):
        """Sort an array via bubble sort
        
        This algorithm compute scales quadratically n^2
        
        Arguments:
        vals : []
        	List of vals, must be comparable
        
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
    def quick_sort(vals):
        """Sort an array via quick sort
        
        This algorithm compute scales as n*log(n) in the best
        case and n^2 in the worst.
        
        We utilise here the variation where
        pivot is around the last value
        
        Arguments:
        vals : []
        	List of vals, must be comparable
        
        Returns:
        vals : []
        	The sorted list
        """
        
        # because the algorithm is recursive its easier
        # if the user doesnt get exposed to the details
        BagOfTricks.__inner_quick_sort__(vals,0,len(vals)-1)
        
        return vals
    
    @staticmethod
    def __inner_quick_sort__(vals,lower,higher):
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
            pi = BagOfTricks.__partition_quick_sort__(vals,
                                                      lower,
                                                      higher)
            
            # recursively call quick sort over the split arrays
            BagOfTricks.__inner_quick_sort__(vals,lower,pi - 1)
            BagOfTricks.__inner_quick_sort__(vals,pi + 1,higher)
    
    @staticmethod
    def __partition_quick_sort__(vals,lower,higher):
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
    def merge_sort(vals):
        """Sort an array via merge sort
        
        This algorithm is similar in nature to
        quick sort in that it to is a 'divide
        and conquer' algorithm however merge
        sort has better worse case performance
        
        Scales with n log(n) in all cases
        
        Arguments:
        vals : []
        	Array to be sorted
        
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
            
            vals.clear() # reset vals for new sorted elements
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
