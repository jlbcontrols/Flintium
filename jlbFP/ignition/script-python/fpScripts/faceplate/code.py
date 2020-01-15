def openMain(instancePath):
	popupPath = 'FactoryPacks/Faceplates/Main'
	params = {'instancePath':instancePath}
	window = system.nav.openWindowInstance(popupPath, params)
	system.nav.centerWindow(window)



def open(instancePath, faceplateType):
	udtTypeName = fpScripts.util.getTypeName(instancePath)
	params = getPathParams(instancePath, udtTypeName)
	params.update(getTabProperties(udtTypeName,faceplateType))
	popupPath = 'FactoryPacks/Faceplates/' + faceplateType
	window = system.nav.openWindowInstance(popupPath, params)
	system.nav.centerWindow(window)
	

def getTabProperties(udtTypeName,faceplateType):
	if(faceplateType.lower()=='main'):
		return getMainHiddenTabs(udtTypeName)
	if(faceplateType.lower()=='advanced'):
		return getAdvancedPageCounts(udtTypeName)
	return {}


#def getHiddenTabs(udtTypeName,faceplateType):
#	if(faceplateType.lower()=='main'):
#		return getMainHiddenTabs(udtTypeName)
#	if(faceplateType.lower()=='advanced'):
#		return getAdvancedHiddenTabs(udtTypeName)
#	return {}

def getPathParams(instancePath, udtTypeName):
	params = {
		'instancePath':instancePath,
		'templateFolder':'FactoryPacks/Panels/'+ udtTypeName,
	}
	return params
	
#def getMainHiddenTabs(udtTypeName):
#	hiddenTabs = {
#		'hideOperator':False,
#		'hideMaintenance':False,
#		'hideTrends':False,
#		'hideDiagnostics':False,
#		'hideAlarms':False
#	}
#	if(udtTypeName=="P_Intlk" or udtTypeName=="P_Alarm" or udtTypeName=="P_CmdSrc"):
#		hiddenTabs['hideTrends']=True
#		hiddenTabs['hideDiagnostics']=True
#		hiddenTabs['hideAlarms']=True
#	return hiddenTabs
	
def getMainHiddenTabs(udtTypeName):
	for obj in fpScripts.nav.navList:
		if(obj.name==udtTypeName):
			return obj.main.getHiddenTabs()	
	
	
def getAdvancedPageCounts(udtTypeName):
	for obj in fpScripts.nav.navList:
		if(obj.name==udtTypeName):
			return obj.advanced.getPageCounts()


	