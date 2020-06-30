##### Funcions used with the tagScriptModule.  Only used during development to help build UDTs from AOI tags (from OPC browser).  Not called anywhere in the project. #####
# May need to restart module on gateway webpage before use.


def updateOpcPaths(udtName):
	udtPath = "_types_/FlintiumTypes/" + udtName
	opcStartString = "{opcPrefix}[{plcName}]{plcTag}."
	return system.udtHelper.updateOpcPath(udtPath, opcStartString)
	
def updateOpcServer(udtName):
	udtPath = "_types_/FlintiumTypes/" + udtName
	opcServerString = "{opcServName}"
	return system.udtHelper.updateOpcServer(udtPath, opcServerString)

def updateHistoryProvider(udtName):
	udtPath = "_types_/FlintiumTypes/" + udtName
	historyProviderString = "{histProvName}"
	return system.udtHelper.updateHistoryProvider(udtPath, historyProviderString)

def folderize(udtName):
	udtPath = "_types_/FlintiumTypes/" + udtName
	return system.udtHelper.folderize(udtPath)
		
def removePrefixes(udtName):
	udtPath = "_types_/FlintiumTypes/" + udtName
	return system.udtHelper.removePrefixes(udtPath)
		
def updateTagGroup(udtName):
	udtPath = "_types_/FlintiumTypes/" + udtName
	tagGroupString = "FlintiumLeased"
	opcPathFilterString = ""  # For expample "Cfg_ would only update tags with Cfg_ in opc path, "" would update all opc tags
	return system.udtHelper.updateTagGroup(udtPath, tagGroupString, opcPathFilterString)

# Examples:		
# udtconversion.updateOpcPaths("P_VSD")
# udtconversion.folderize("P_VSD")
# udtconversion.removePrefixes("P_VSD")
# udtconversion.updateTagGroup("P_VSD")

# Use this to apply a function to all the UDT tags.  The function must take udtName as the sole input (i.e. one of the functions listed above)
# Example: udtconversion.updateAllUdts(udtconversion.updateTagGroup)
def updateAllUdts(updateFunction):
	udtList = ["Meta","P_AIn","P_Alarm","P_CmdSrc","P_Gate","P_Intlk","P_Motor","P_MotorRev","P_Perm","P_PIDE","P_ValveC","P_ValveSO","P_VSD","VariableOwner"]
	for udtName in udtList:
		updateFunction(udtName)


# Run this to perform intitial conversion, after type is created from OPC drop.  May need to restart module on gateway webpage before use.
def convertFromOpcDrop(udtName):

	udtPath = "_types_/FlintiumTypes/" + udtName
	
	folderizedQty = system.udtHelper.folderize(udtPath)
	
	opcStartString = "{opcPrefix}[{plcName}]{plcTag}."
	opcPathQty = system.udtHelper.updateOpcPath(udtPath, opcStartString)
	
	opcServerString = "{opcServName}"
	opcServerQty = system.udtHelper.updateOpcServer(udtPath, opcServerString)
	
	prefixUpdatedQty = system.udtHelper.removePrefixes(udtPath)
	
	tagGroupString = "FlintiumLeased"
	opcPathFilterString = ""
	tagGroupUpdateAllQty = system.udtHelper.updateTagGroup(udtPath, tagGroupString, opcPathFilterString)
	
	return {
		'folderizedQty':folderizedQty,
		'opcPathQty':opcPathQty,
		'opcServerQty':opcServerQty,
		'prefixUpdatedQty':prefixUpdatedQty,
		'tagGroupUpdateAllQty':tagGroupUpdateAllQty,
		'tagGroupUpdateCfgQty':tagGroupUpdateCfgQty
		}
		
		

