def getTypePath(instancePath):
	print instancePath
	udtTypePath = system.tag.read(instancePath + ".UDTParentType").value
	return udtTypePath

def getTypeName(instancePath):
	udtTypePath = '/' + getTypePath(instancePath)
	udtTypeName = udtTypePath.rsplit('/',1)[1]
	return udtTypeName
	
def openFolderDialog(dialogTitle):
	from javax.swing import JFileChooser
	chooser = JFileChooser()
	chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
	chooser.setDialogTitle(dialogTitle)
	if chooser.showOpenDialog(None) == JFileChooser.APPROVE_OPTION:
		return str(chooser.getSelectedFile())