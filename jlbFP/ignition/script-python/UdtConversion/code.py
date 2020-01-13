def updateOpcPaths(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	opcStartString = "ns=1;s=[{LeasedPLC}]{PAX Tag}."
	return system.udtHelper.updateOpcPath(udtPath, opcStartString)

def folderize(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	return system.udtHelper.folderize(udtPath)
		
def removePrefixes(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	return system.udtHelper.removePrefixes(udtPath)
		
def updateTagGroup(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	tagGroupString = "FactoryPacks Leased"
	return system.udtHelper.updateTagGroup(udtPath, tagGroupString)
		
#UdtConversion.updateOpcPaths("P_VSA")
#UdtConversion.folderize("P_VSA")
#UdtConversion.removePrefixes("P_VSA")
#UdtConversion.updateTagGroup("P_VSA")

def convertFromOpcDrop(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	
	retFolderize = system.udtHelper.folderize(udtPath)
	
	opcStartString = "ns=1;s=[{LeasedPLC}]{PAX Tag}."
	retOpcUpdate = system.udtHelper.updateOpcPath(udtPath, opcStartString)
	
	retPrefixUpdate = system.udtHelper.removePrefixes(udtPath)
	
	tagGroupString = "FactoryPacks Leased"
	retTagGroupUpdate = system.udtHelper.updateTagGroup(udtPath, tagGroupString)
	
	return 'folderize=' + str(retFolderize) + '\n' +'opcUpdate=' + str(retOpcUpdate) + '\n' +'prefixUpdate=' + str(retPrefixUpdate) + '\n' +'tagGroupUpdate=' + str(retTagGroupUpdate)