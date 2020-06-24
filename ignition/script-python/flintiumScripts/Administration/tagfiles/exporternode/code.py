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

# Export a list of tags, with prompts to select export directory and confirm.
def exportWithPrompts(tagPaths):
	if not tagPaths:
		system.gui.errorBox("Select at least one tag for export.")
		return
	parentDirPath = flintiumScripts.util.openFolderDialog("Select Parent Directory")
	if parentDirPath:
		nodes = []
		for tagPath in tagPaths:
			nodes.append(ExporterNode(parentDirPath,tagPath=tagPath))
		nodeNames = getNodeNamesLower(nodes)
		if flintiumScripts.util.containsDuplicate(nodeNames):
			system.gui.errorBox("Duplicate node names are not permitted.")
			return
		confirmMessage = "Are you sure you want to create or overwrite the following folder(s)?"
		for node in nodes:
			confirmMessage += "\n" + node.getDirPath()
		parentDirName = os.path.basename(parentDirPath)
		if (parentDirName.lower() in nodeNames):
			confirmMessage += "\n\n WARNING: Parent directory name matches tag name."
		if system.gui.confirm(confirmMessage):
			for node in nodes:
				node.exportFiles()
			system.gui.messageBox("Export Complete")

def getNodeNamesLower(nodes):
	names = []
	for node in nodes:
		names.append(node.fullConfig["name"].lower())
	return names
	