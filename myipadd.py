class ipaddr():
	def __init__(ip = [ 0,0,0,0], no= [0,0,0,0]):
		self.ip = ip
		self.no = no
	def printip(self):
		print (" The address  is " + "." join(ip))
myip  = ipaddr([192,168,1,1],[255.255.255.0])
myip.printip()
