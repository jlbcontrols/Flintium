#def updateOpcPaths(udtName):
#	udtPath = "_types_/FactoryPacks/" + udtName
#	opcStartString = "ns=1;s=[{LeasedPLC}]{PAX Tag}."
#	return system.udtHelper.updateOpcPath(udtPath, opcStartString)
#
#def folderize(udtName):
#		udtPath = "_types_/FactoryPacks/" + udtName
#		return system.udtHelper.folderize(udtPath)
#		
#def removePrefixes(udtName):
#		udtPath = "_types_/FactoryPacks/" + udtName
#		return system.udtHelper.removePrefixes(udtPath)
#		
#def updateTagGroup(udtName):
#		udtPath = "_types_/FactoryPacks/" + udtName
#		tagGroupString = "FactoryPacks Leased"
#		return system.udtHelper.updateTagGroup(udtPath, tagGroupString)
		
#updateUDT.updateOpcPaths("P_VSA")
#updateUDT.folderize("P_VSA")
#updateUDT.removePrefixes("P_VSA")
#updateUDT.updateTagGroup("P_VSA")

def convertFromOpcDrop(udtName):
	udtPath = "_types_/FactoryPacks/" + udtName
	
	system.udtHelper.folderize(udtPath)
	
	opcStartString = "ns=1;s=[{LeasedPLC}]{PAX Tag}."
	system.udtHelper.updateOpcPath(udtPath, opcStartString)
	
	system.udtHelper.removePrefixes(udtPath)
	
	tagGroupString = "FactoryPacks Leased"
	system.udtHelper.updateTagGroup(udtPath, tagGroupString)