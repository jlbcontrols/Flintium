##### Fucntions to open the correct faceplate, depending on UDT of a given instance, and Main or Advanced popup. #####

# Called from vision component scripts
def open(instancePath, faceplateType):
	udtTypeName = fpScripts.util.getTypeName(instancePath)
	params = getPathParams(instancePath, udtTypeName)
	params.update(getTabProperties(udtTypeName,faceplateType))
	popupPath = 'FactoryPacks/Faceplates/' + faceplateType
	window = system.nav.openWindowInstance(popupPath, params)
	system.nav.centerWindow(window)
	

def getTabProperties(udtTypeName,faceplateType):
	if(faceplateType=='Main'):
		return getMainHiddenTabs(udtTypeName)
	if(faceplateType=='Advanced'):
		return getAdvancedPageCounts(udtTypeName)
	return {}


def getPathParams(instancePath, udtTypeName):
	params = {
		'instancePath':instancePath,
		'templateFolder':'FactoryPacks/Panels/'+ udtTypeName,
	}
	return params

	
def getMainHiddenTabs(udtTypeName):
	for obj in fpScripts.nav.navList:
		if(obj.name==udtTypeName):
			return obj.main.getHiddenTabs()	
	
	
def getAdvancedPageCounts(udtTypeName):
	for obj in fpScripts.nav.navList:
		if(obj.name==udtTypeName):
			return obj.advanced.getPageCounts()


	