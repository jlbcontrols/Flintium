##### Fucntions to open the correct faceplate, depending on UDT of a given instance, and Main or Advanced popup. #####

# Called from vision component scripts
def open(event, instancePath, faceplateType):

	udtName = flintiumScripts.util.getTypeName(instancePath)
	
	params = {
		'instancePath':instancePath,
		'templateFolder':'Flintium/Panels/'+ udtName,
	}
	tabProperties = getTabProperties(event,udtName,faceplateType)
	params.update(tabProperties)
	
	popupPath = 'Flintium/Faceplates/' + faceplateType
	window = system.nav.openWindowInstance(popupPath, params)
	system.nav.centerWindow(window)
	

def getTabProperties(event,udtName,faceplateType):
	templateManager = event.source.getAppContext().getTemplateManager()
	if(faceplateType=='Main'):
		return getMainTabDict(udtName, templateManager)
	if(faceplateType=='Advanced'):
		return getAdvancedPageCountDict(udtName, templateManager)
	print "Must select 'Main' or 'Advanced' faceplate type. Received:'" + faceplateType + "'"
	return {}



def getNumberedTemplateCount(folderPath,templateManager):
	max = 10
	for i in range(1,max):
		templatePath = folderPath + "/" + str(i)
		if not templateExists(templatePath,templateManager):
			break
	return i-1
	
def templateExists(templatePath,templateManager):
	if templateManager.getId(templatePath):
		return True
	else:
		return False
	
def getUdtTemplFolderPath(udtName):
	return "Flintium/Panels/" + udtName

def getAdvancedPageCountDict(udtName, templateManager):
	advTemplFolderPath = getUdtTemplFolderPath(udtName)+"/Advanced"
	return{
		'maintenancePages':getNumberedTemplateCount(advTemplFolderPath+"/Maintenance",templateManager),
		'engineeringPages':getNumberedTemplateCount(advTemplFolderPath+"/Engineering",templateManager),
		'hmiPages':getNumberedTemplateCount(advTemplFolderPath+"/HMI",templateManager),
		'faultsPages':getNumberedTemplateCount(advTemplFolderPath+"/Faults",templateManager)
	}

def getMainTabDict(udtName, templateManager):
	mainTemplFolderPath = getUdtTemplFolderPath(udtName)+"/Main"
	return{
		'hasOperator':templateExists(mainTemplFolderPath+"/Operator",templateManager),
		'hasMaintenance':templateExists(mainTemplFolderPath+"/Maintenance",templateManager),
		'hasTrends':templateExists(mainTemplFolderPath+"/Trends",templateManager),
		'hasDiagnostics':templateExists(mainTemplFolderPath+"/Diagnostics",templateManager),
		'hasAlarms':templateExists(mainTemplFolderPath+"/Alarms",templateManager),
		'hasAdvanced':sum(getAdvancedPageCountDict(udtName, templateManager).values())>0
	}
	
