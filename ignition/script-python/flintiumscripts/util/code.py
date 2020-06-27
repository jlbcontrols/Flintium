# Returns path to an instance's UDT definition
def getTypePath(instancePath):
	udtTypePath = system.tag.read(instancePath + ".UDTParentType").value
	return udtTypePath

# Returns the name of an instance's UDT definition
def getTypeName(instancePath):
	udtTypePath = '/' + getTypePath(instancePath)
	udtTypeName = udtTypePath.rsplit('/',1)[1]
	return udtTypeName

# Check for duplicates in a list	
def containsDuplicate(list):
	return len(list) != len(set(list))