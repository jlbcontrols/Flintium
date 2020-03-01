##### Fucntions to open the correct faceplate, depending on UDT of a given instance, and Main or Advanced popup. #####

# Called from vision component scripts
def open(instancePath, faceplateType):

	print "instancePath=" +instancePath
	udtTypeName = fpScripts.util.getTypeName(instancePath)
	print udtTypeName
	
	params = {
		'instancePath':instancePath,
		'templateFolder':'FactoryPacks/Panels/'+ udtTypeName,
	}
	tabProperties = getTabProperties(udtTypeName,faceplateType)
	params.update(tabProperties)
	
	popupPath = 'FactoryPacks/Faceplates/' + faceplateType
	window = system.nav.openWindowInstance(popupPath, params)
	system.nav.centerWindow(window)
	

def getTabProperties(udtTypeName,faceplateType):
	udtNav = fpScripts.nav.getNavObject(udtTypeName)
	if(faceplateType=='Main'):
		return udtNav.main.getTabDict()
	if(faceplateType=='Advanced'):
		return udtNav.advanced.getPageCountDict()
	print "Must select 'Main' or 'Advanced' faceplate type. Received:'" + faceplateType + "'"
	return {}




	