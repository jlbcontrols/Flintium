def getTypePath(instancePath):
	print instancePath
	udtTypePath = system.tag.read(instancePath + ".UDTParentType").value
	return udtTypePath

def getTypeName(instancePath):
	udtTypePath = '/' + getTypePath(instancePath)
	udtTypeName = udtTypePath.rsplit('/',1)[1]
	return udtTypeName