from hashlib import sha256
import math

class Node():
	def __init__(self, value, hashdigest):
		self.value = value
		self.hashdigest = hashdigest
	
def NodeCombiner(left, right):
	newvalue = left.value + right.value
	lefthash, righthash = left.hashdigest, right.hashdigest
	hashdigest = sha256(str(newvalue) + lefthash + righthash).hexdigest()
	
	return Node(newvalue, hashdigest)

class HashTree():
	def __init__(self, nodelist):
		self.nodelist = nodelist
		self.roothash = ''
		self.tree = []
		self.GenTree(nodelist)
		self.lookup = {}
		self.GenLookup()
	
	def GenTree(self, nodelist):
		self.tree.append(nodelist)
		newnodelist = []
		
		if len(nodelist) % 2:
			nodelist.append(Node(0.0, sha256('0').hexdigest()))
		
		for x in range(int(math.ceil(len(nodelist)/2.0))):
			newnodelist.append(NodeCombiner(nodelist[x], nodelist[-(x + 1)]))
		
		if len(newnodelist) > 1:
			return self.GenTree(newnodelist)
		else:
			self.tree.append(newnodelist)
			self.roothash = newnodelist[0].hashdigest
			return self.roothash
	
	def RegenTree(self):
		self.tree = []
		return self.GenTree(self.nodelist)
	
	def GetNodeInfo(self, index):
		pairlist = []
		
		return True
		
	def GenLookup(self):
		index = 0
		for x in self.nodelist:
			self.lookup[x.hashdigest] = index
			index += 1
	

def ValidateNode(self, value, hashdigest, roothash, pairlist):
	return True
