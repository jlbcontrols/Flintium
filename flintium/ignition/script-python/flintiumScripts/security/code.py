def isAllowed(instancePath,componentRoles):
	userRoles = system.tag.readBlocking(["[System]Client/User/RolesDataSet"])[0].value
	areaAllowed = isAllowedArea(instancePath,userRoles)
	userAllowed = isAllowedUser(userRoles,componentRoles)
	return (areaAllowed and userAllowed)
	
	
	
	


def isAllowedArea(instancePath,userRoles):
	areaPath = instancePath + "/Meta/Area"
	area = system.tag.readBlocking([areaPath])[0].value
	userRoleList = userRoles.getColumnAsList(0)
	return (area in userRoleList)

def isAllowedUser(userRoles,componentRoles):
	return matchAnyElementInDatasets(userRoles,componentRoles,0)
	

def matchAnyElementInDatasets(ds1,ds2,colNumber):
	dsList1 = ds1.getColumnAsList(colNumber)
	dsList2 = ds2.getColumnAsList(colNumber)
	for value in dsList1:
		if value in dsList2:
			return True
	return False