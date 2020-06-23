import json
import os
import shutil
from com.inductiveautomation.ignition.common.tags import TagUtilities
from com.inductiveautomation.ignition.client.gateway_interface import GatewayConnectionManager
from com.inductiveautomation.ignition.common.tags.paths.parser import TagPathParser

class ExporterNode():
	def __init__(self, parentDirPath,fullConfig={},tagPath=""):
		self.parentDirPath = parentDirPath
		if (not fullConfig) and (not tagPath):
			raise ValueError("Must provide a fullConfig or tagPath")
		elif not fullConfig:
			self.fullConfig = getFullConfigFromGateway(tagPath)
		else:
			self.fullConfig = fullConfig

	def __str__(self):
		return "%s(name=%s,dirPath=%s)" % (self.__class__.__name__,self.fullConfig["name"],self.getDirPath())

	def getDirPath(self):
		return os.path.join(self.parentDirPath, self.fullConfig['name'])

	def getNodeFilePath(self):
		return os.path.join(self.getDirPath(), "nodeconfig.json")

	# tag config json without "name" or "tags" items. name and tags information becomes part of the folder structure.
	def getNodeConfig(self):
		nodeConfig = dict(self.fullConfig)
		del nodeConfig["name"]
		if "tags" in nodeConfig:
			del nodeConfig["tags"]
		return nodeConfig

	# create a list of nodes for direct children (not recursive).
	def getChildNodes(self):
		nodes = []
		if "tags" in self.fullConfig:
			for childConfig in self.fullConfig["tags"]:
				nodes.append(ExporterNode(self.getDirPath(),fullConfig=childConfig))
		return nodes

	# save all tag information as a directory of files (recursive).
	def exportFiles(self):
		self.exportNodeConfig()
		for node in self.getChildNodes():
			node.exportFiles()
	
	# export the json for this node's top level tag.
	def exportNodeConfig(self):
		self.clearDirectory()
		with open(self.getNodeFilePath(),'w') as outfile:
			json.dump(self.getNodeConfig(),outfile,indent=4,sort_keys=True)

	# Delete any existing directory, and create new
	def clearDirectory(self):
		dirPath = self.getDirPath()
		if os.path.exists(dirPath):
			shutil.rmtree(dirPath)
		os.makedirs(dirPath)

# Get tagConfiguration dictionary for tagpath. "system.tag.getConfiguration" dict does not dump to json, so using Using "TagProviderRpc.getTagExport" instead.
def getFullConfigFromGateway(tagPath):
	configString = GatewayConnectionManager.getInstance().getGatewayInterface().invoke("TagProviderRpc.getTagExport", [[TagPathParser.parse(tagPath)],True,"json"])
	fullConfig = json.loads(configString)
	if fullConfig["tagType"]=="Unknown":
		raise ValueError(fullConfig["name"] + " tagType is Unknown. Check if tag exists.")
	return fullConfig

def testExport():
	tagPath = system.gui.inputBox("Enter tag path to export.")
	parentDirPath = flintiumScripts.util.openFolderDialog("Select Parent Directory")
	if parentDirPath:
		node = ExporterNode(parentDirPath,tagPath=tagPath)
		if system.gui.confirm("Are you sure you want to create or overwrite folder %s in directory %s?" % (node.fullConfig["name"], parentDirPath)):
			node.exportFiles()
