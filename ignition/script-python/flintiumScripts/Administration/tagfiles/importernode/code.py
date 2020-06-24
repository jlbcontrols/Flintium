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
	def importTag(self,parentTagPath):
		self.removeExistingTag(parentTagPath)
		fullConfig = self.getFullConfig()
		system.tag.configure(parentTagPath, fullConfig, "o")

	# delete any existing tags that current use this nodes tagpath
	def removeExistingTag(self,parentTagPath):
		tagPath = parentTagPath + "/" + self.getName()
		system.tag.removeTag(tagPath)
		
def importWithPrompts(parentTagPath):
	if parentTagPath:
		parentConfig = system.tag.getConfiguration(parentTagPath)[0]
		if not str(parentConfig["tagType"]).lower() in ["folder","udttype","udtinstance"]:
			system.gui.errorBox("Parent tag must be a folder, udtType or udtInstance")
			return
		dirPath = flintiumScripts.util.openFolderDialog("Select Tag Directory")
		if dirPath:
			node = ImporterNode(dirPath)
			if system.gui.confirm("Are you sure you want to create or replace the following tag?\n" + parentTagPath + "/" + node.getName()):
				node.importTag(parentTagPath)
