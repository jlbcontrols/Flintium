##### Funcions used with the tagScriptModule.  Only used during development to help build UDTs from AOI tags (from OPC browser).  Not called anywhere in the project. #####

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
		
#UdtConversion.updateOpcPaths("P_VSD")
#UdtConversion.folderize("P_VSD")
#UdtConversion.removePrefixes("P_VSD")
#UdtConversion.updateTagGroup("P_VSD")


# Run this to perform intitial conversion, after type is created from OPC drop.  May need to restart module on gateway webpage before use.
def convertFromOpcDrop(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	
	retFolderize = system.udtHelper.folderize(udtPath)
	
	opcStartString = "ns=1;s=[{PLC}]{PAX Tag}."
	retOpcUpdate = system.udtHelper.updateOpcPath(udtPath, opcStartString)
	
	retPrefixUpdate = system.udtHelper.removePrefixes(udtPath)
	
	tagGroupString = "FactoryPacks Leased"
	retTagGroupUpdate = system.udtHelper.updateTagGroup(udtPath, tagGroupString)
	
	return 'folderize=' + str(retFolderize) + '\n' +'opcUpdate=' + str(retOpcUpdate) + '\n' +'prefixUpdate=' + str(retPrefixUpdate) + '\n' +'tagGroupUpdate=' + str(retTagGroupUpdate)