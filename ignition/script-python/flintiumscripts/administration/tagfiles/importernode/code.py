import json
import os

class ImporterNode():
	def __init__(self, dirPath):
		self.dirPath = dirPath

	def __str__(self):
		return "%s(name=%s, parentDirPath=%s)" % (self.__class__.__name__,self.getName(),self.dirPath)

	def getName(self):
		return os.path.basename(self.dirPath)
		
	def getFilePath(self):
		return os.path.join(self.dirPath, "nodeconfig.json")
	
	def getTagPath(self,parentTagPath):
		return parentTagPath + "/" + self.getName()

	# tag config json without "name" or "tags" items. name and tags information is read from the folder structure.
	def getNodeConfig(self):
		with open(self.getFilePath()) as jsonFile:
			nodeConfig = json.load(jsonFile)
		nodeConfig["name"] = self.getName()
		return nodeConfig

	# create a list of nodes for direct children (not recursive).
	def getChildNodes(self):
		childNodes=[]
		for childName in os.listdir(self.dirPath):
			childPath = os.path.join(self.dirPath,childName)
			if os.path.isdir(childPath):
				childNodes.append(ImporterNode(childPath))
		return childNodes
	
	# create a json from the file structure containing all tag information for this node and children (recursive).
	def getFullConfig(self):
		fullConfig = self.getNodeConfig()
		fullConfig["name"]=self.getName()
		childNodes = self.getChildNodes()
		if childNodes:
			fullConfig["tags"]=[]
			for childNode in childNodes:
				childConfig = childNode.getFullConfig()
				fullConfig["tags"].append(childConfig)
		return fullConfig

	# import tag from file structure to a specified tag folder
	def importToTag(self,parentTagPath,removeExisting=True):
		if removeExisting:
			self.removeExistingTag(parentTagPath)
		fullConfig = self.getFullConfig()
		system.tag.configure(parentTagPath, fullConfig, "o")

	# delete any existing tags that current use this nodes tagpath
	def removeExistingTag(self,parentTagPath):
		tagPath = self.getTagPath(parentTagPath)
		system.tag.removeTag(tagPath)

# Import tags into the provided parentTagPath. Prompts to select tag directories to be imported and confirm.	
def importWithPrompts(parentTagPath):
	if parentTagPath:
		parentConfig = system.tag.getConfiguration(parentTagPath)[0]
		if not str(parentConfig["tagType"]).lower() in ["provider","folder","udttype","udtinstance"]:
			raise ValueError("Parent tag must be a Provider, folder, udtType or udtInstance")
		dirPaths = openFolderDialog("Select Tag Directory")
		if dirPaths:
			nodes=[]
			confirmMessage = "Are you sure you want to create or replace the following tag(s)?"
			for dirPath in dirPaths:
				node = ImporterNode(dirPath)
				confirmMessage += "\n" + node.getTagPath(parentTagPath)
				nodes.append(node)
			if system.gui.confirm(confirmMessage):
				# Repeat import twice in case imported tags are interdependent (one of the tags contains an instance of another). Avoids the need to sort imports by order of dependency.
				for node in nodes:
					node.importToTag(parentTagPath)
				for node in nodes:
					node.importToTag(parentTagPath,removeExisting=False)
				system.gui.messageBox("Import Complete")


def openFolderDialog(dialogTitle):
	from javax.swing import JFileChooser
	chooser = JFileChooser()
	chooser.setMultiSelectionEnabled(True);
	chooser.setFileSelectionMode(JFileChooser.DIRECTORIES_ONLY)
	chooser.setDialogTitle(dialogTitle)
	if chooser.showOpenDialog(None) == JFileChooser.APPROVE_OPTION:
		folderPathStrings = []
		for folderPath in chooser.getSelectedFiles():
			folderPathStrings.append(str(folderPath))
		return folderPathStrings