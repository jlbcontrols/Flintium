import json
import os
import shutil
from com.inductiveautomation.ignition.common.tags import TagUtilities
from com.inductiveautomation.ignition.client.gateway_interface import GatewayConnectionManager
from com.inductiveautomation.ignition.common.tags.paths.parser import TagPathParser

class Node():
	def __init__(self, fullConfig, parentDirPath):
		self.fullConfig = fullConfig
		self.parentDirPath = parentDirPath

	def __str__(self):
		return "%s(name=%s, parentDirPath=%s)" % (self.__class__.__name__,self.fullConfig["name"],self.parentDirPath)

	def getDirPath(self):
		return self.parentDirPath + "/" + self.fullConfig['name']

	def getFilePath(self):
		return self.getDirPath() + "/" + "nodeconfig.json"

	def getNodeConfig(self):
		nodeConfig = dict(self.fullConfig)
		if "tags" in nodeConfig:
			del nodeConfig["tags"]
		return nodeConfig

	def getChildNodes(self):
		nodes = []
		if "tags" in self.fullConfig:
			for childConfig in self.fullConfig["tags"]:
				nodes.append(Node(childConfig,self.getDirPath()))
		return nodes

	def exportAsFileTree(self):
		self.saveToFile()
		for node in self.getChildNodes():
			node.exportAsFileTree()

	def saveToFile(self):
		self.overwriteDirectory()
		with open(self.getFilePath(),'w') as outfile:
			json.dump(self.getNodeConfig(),outfile,indent=4,sort_keys=True)

	# Delete any existing directory, and create new
	def overwriteDirectory(self):
		dirPath = self.getDirPath()
		if os.path.exists(dirPath):
			shutil.rmtree(dirPath)
		os.makedirs(dirPath)

# Get tagConfiguration dictionary for tagpath
# Using "TagProviderRpc.getTagExport" instead of "system.tag.getConfiguration" because of errors on json.dump
def getFullConfigFromGateway(tagPath):
	configUnicode = GatewayConnectionManager.getInstance().getGatewayInterface().invoke("TagProviderRpc.getTagExport", [[TagPathParser.parse(tagPath)],True,"json"])
	configDict = json.loads(configUnicode)
	if configDict["tagType"]=="Unknown":
		raise ValueError(configDict["name"] + " tagType is Unknown. Check if tag exists.")
	return configDict

def test():
	tagPath = "[default]_types_/Flintium/P_AIn"
	parentDirPath = flintiumScripts.util.openFolderDialog("Select Parent Folder")
	if parentDirPath:
		fullConfig = getFullConfigFromGateway(tagPath)
		if system.gui.confirm("Are you sure you want to create or overwrite folder %s in directory %s?" % (fullConfig["name"], parentDirPath)):
			node = Node(fullConfig,parentDirPath)
			node.exportAsFileTree()
