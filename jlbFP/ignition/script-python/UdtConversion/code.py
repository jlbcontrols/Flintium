##### Funcions used with the tagScriptModule.  Only used during development to help build UDTs from AOI tags (from OPC browser).  Not called anywhere in the project. #####

def updateOpcPaths(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	opcStartString = "ns=1;s=[{LeasedPLC}]{PAX Tag}."
	return system.udtHelper.updateOpcPath(udtPath, opcStartString)
	
def updateOpcServer(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	opcServerString = "{OPC Server}"
	return system.udtHelper.updateOpcServer(udtPath, opcServerString)

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
	opcPathFilterString = ""
	return system.udtHelper.updateTagGroup(udtPath, tagGroupString, opcPathFilterString)
		
#UdtConversion.updateOpcPaths("P_VSD")
#UdtConversion.folderize("P_VSD")
#UdtConversion.removePrefixes("P_VSD")
#UdtConversion.updateTagGroup("P_VSD")


# Run this to perform intitial conversion, after type is created from OPC drop.  May need to restart module on gateway webpage before use.
def convertFromOpcDrop(udtName):
	import system
	udtPath = "_types_/FactoryPacks/" + udtName
	
	folderizedQty = system.udtHelper.folderize(udtPath)
	
	opcStartString = "ns=1;s=[{PLC}]{PAX Tag}."
	opcPathQty = system.udtHelper.updateOpcPath(udtPath, opcStartString)
	
	opcServerString = "{OPC Server}"
	opcServerQty = system.udtHelper.updateOpcServer(udtPath, opcServerString)
	
	prefixUpdatedQty = system.udtHelper.removePrefixes(udtPath)
	
	tagGroupString = "FactoryPacks Leased"
	opcPathFilterString = ""
	tagGroupUpdateAllQty = system.udtHelper.updateTagGroup(udtPath, tagGroupString, opcPathFilterString)
	
	tagGroupString = "FactoryPacks Leased-Slow"
	opcPathFilterString = "Cfg_"
	tagGroupUpdateCfgQty = system.udtHelper.updateTagGroup(udtPath, tagGroupString, opcPathFilterString)
	
	return {
		'folderizedQty':folderizedQty,
		'opcPathQty':opcPathQty,
		'opcServerQty':opcServerQty,
		'prefixUpdatedQty':prefixUpdatedQty,
		'tagGroupUpdateAllQty':tagGroupUpdateAllQty,
		'tagGroupUpdateCfgQty':tagGroupUpdateCfgQty
		}