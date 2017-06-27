class MovingAverage(object):
	def __init__(self, size):
		self.window = [0]*size
		self.curr_index = 0
		self.rotated = False

	def next(self, val):
		if self.curr_index == len(self.window):
   		self.rotated = True
    	self.curr_index = 0
            
		self.window[self.curr_index] = val
		self.curr_index += 1
        
		if self.rotated == False:
   		return sum(self.window)/float(self.curr_index)
		else:
    	return sum(self.window)/float(len(self.window))

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
