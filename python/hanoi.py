def hanoi(n, src, dst, tmp):
	print('n', n)
	print('1', src)
	print('2', dst)
	print('3', tmp)
	if n > 0:
		hanoi(n-1,src,tmp,dst)
		src.remove(n)
		dst.add(n)
		hanoi(n-1,tmp,dst,src)

hanoi(3, set([3,2,1]), set([]), set([]))
