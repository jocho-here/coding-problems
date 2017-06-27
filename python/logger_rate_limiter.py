class Logger(object):
	def __init__(self):
		self.dict = {}
        
	def shouldPrintMessage(self, timestamp, message):
		if self.dict.has_key(message):
			last_timestamp = self.dict.get(message)

			if timestamp - last_timestamp < 10:
				return False

			else:
				self.dict[message] = timestamp

		else:
			self.dict.setdefault(message, timestamp)
            
		return True

logger = Logger();

# logging string "foo" at timestamp 1
print(logger.shouldPrintMessage(1, "foo"))# returns true;

# logging string "bar" at timestamp 2
print(logger.shouldPrintMessage(2,"bar"))# returns true;

# logging string "foo" at timestamp 3
print(logger.shouldPrintMessage(3,"foo"))# returns false;

# logging string "bar" at timestamp 8
print(logger.shouldPrintMessage(8,"bar"))# returns false;

# logging string "foo" at timestamp 10
print(logger.shouldPrintMessage(10,"foo"))# returns false;

# logging string "foo" at timestamp 11
print(logger.shouldPrintMessage(11,"foo"))# returns true;
