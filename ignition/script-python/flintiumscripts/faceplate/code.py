##### Fucntions to open the correct faceplate, depending on UDT of a given instance, and Main or Advanced popup. #####

# Called from vision component scripts to open a devices faceplate
def open(event, instancePath, faceplateType):

	udtName = flintiumscripts.util.getTypeName(instancePath)
	
	params = {
		'instancePath':instancePath,
		'templateFolder':'Flintium/Panels/'+ udtName,
	}
	tabProperties = getTabProperties(event,udtName,faceplateType)
	params.update(tabProperties)
	
	popupPath = 'Flintium/Faceplates/' + faceplateType
	window = system.nav.openWindowInstance(popupPath, params)
	system.nav.centerWindow(window)
	
# Return a dictionary of tab data for the faceplate instance. Visible tabs depend on what panel templates exist for a given UDT.
def getTabProperties(event,udtName,faceplateType):
	templateManager = event.source.getAppContext().getTemplateManager()
	if(faceplateType=='Main'):
		return getMainTabDict(udtName, templateManager)
	if(faceplateType=='Advanced'):
		return getAdvancedPageCountDict(udtName, templateManager)
	print "Must select 'Main' or 'Advanced' faceplate type. Received:'" + faceplateType + "'"
	return {}

# Count all templates in folder with sequential integer names "1", "2" ...
def getNumberedTemplateCount(folderPath,templateManager):
	max = 10
	for i in range(1,max):
		templatePath = folderPath + "/" + str(i)
		if not templateExists(templatePath,templateManager):
			break
	return i-1

# Check if a template with given path exists in this project
def templateExists(templatePath,templateManager):
	if templateManager.getId(templatePath):
		return True
	else:
		return False

# Return the UDT's template folder path
def getUdtTemplFolderPath(udtName):
	return "Flintium/Panels/" + udtName

# Dictionary of template page counts for advanced templates
def getAdvancedPageCountDict(udtName, templateManager):
	advTemplFolderPath = getUdtTemplFolderPath(udtName)+"/Advanced"
	return{
		'maintenancePages':getNumberedTemplateCount(advTemplFolderPath+"/Maintenance",templateManager),
		'engineeringPages':getNumberedTemplateCount(advTemplFolderPath+"/Engineering",templateManager),
		'hmiPages':getNumberedTemplateCount(advTemplFolderPath+"/HMI",templateManager),
		'faultsPages':getNumberedTemplateCount(advTemplFolderPath+"/Faults",templateManager)
	}

# Find which main templates exist for a particular UDT
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
	


