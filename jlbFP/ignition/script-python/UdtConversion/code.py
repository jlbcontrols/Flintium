##### Funcions used with the tagScriptModule.  Only used during development to help build UDTs from AOI tags (from OPC browser).  Not called anywhere in the project. #####
# May need to restart module on gateway webpage before use.

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

def updateHistoryProvider(udtName):
		import system
		udtPath = "_types_/FactoryPacks/" + udtName
		historyDbString = "{History DB}"
		return system.udtHelper.updateHistoryProvider(udtPath, historyDbString)

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
	tagGroupString = "FactoryPacks Leased-Slow"
	opcPathFilterString = "Cfg_"
	return system.udtHelper.updateTagGroup(udtPath, tagGroupString, opcPathFilterString)

# Examples:		
# UdtConversion.updateOpcPaths("P_VSD")
# UdtConversion.folderize("P_VSD")
# UdtConversion.removePrefixes("P_VSD")
# UdtConversion.updateTagGroup("P_VSD")

# Use this to apply a function to all the UDT tags.  The function must take udtName as the sole input (i.e. one of the functions listed above)
# Example: UdtConversion.updateAllUdts(UdtConversion.updateTagGroup)
def updateAllUdts(updateFunction):
	udtList = ["Meta","P_AIn","P_Alarm","P_CmdSrc","P_Gate","P_Intlk","P_Motor","P_MotorRev","P_PIDE","P_ValveC","P_ValveSO","P_VSD","ProgOperKeep"]
	for udtName in udtList:
		updateFunction(udtName)


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
		
		

