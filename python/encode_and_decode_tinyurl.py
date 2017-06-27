class Codec:
	def __init__(self):
		self.url_map = {}
        
	def encode(self, longUrl):
		key = len(self.url_map)
        
		while self.url_map.has_key(str(key)):
			key += 1
        
		self.url_map.setdefault(str(key), longUrl)
        
		return "http://tinyurl.com/" + str(key)

	def decode(self, shortUrl):
		key = shortUrl[len("http://tinyurl.com/"):]
        
		return self.url_map.get(key)

codec = Codec()
a = codec.encode("https://leetcode.com/problems/design-tinyurl")
print a

b = codec.decode(a)
print b
