def openMain(instancePath):
	popupPath = 'FactoryPacks/Faceplates/Main'
	params = getMainParams(instancePath)
	
#	udtType = getInstanceType(instancePath)
#	hiddenTabs = getMainHiddenTabs(udtType)
#	params.update(hiddenTabs)
	window = system.nav.openWindowInstance(popupPath, params)
	system.nav.centerWindow(window)
	
	
	
def getMainParams(instancePath):
	udtTypeName = fpScripts.util.getTypeName(instancePath)
	templateFolder = getTemplateFolder(udtTypeName)
	params = {
		'instancePath':instancePath,
		'templateFolder':templateFolder,
	}
	hiddenTabs = getMainHiddenTabs(udtTypeName)
	params.update(hiddenTabs)
	return params
	
	
def getTemplateFolder(udtTypeName):
	return 'FactoryPacks/Panels/'+ udtTypeName
	

def getMainHiddenTabs(udtTypeName):
	hiddenTabs = {
		'hideOperator':False,
		'hideMaintenance':False,
		'hideTrends':False,
		'hideDiagnostics':False,
		'hideAlarms':False
	}
	if(udtTypeName=="P_Intlk" or udtTypeName=="P_Alarm"):
		hiddenTabs['hideTrends']=True
		hiddenTabs['hideDiagnostics']=True
		hiddenTabs['hideAlarms']=True
	return hiddenTabs


	