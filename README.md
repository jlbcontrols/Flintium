<p align="center">
  <img src="https://user-images.githubusercontent.com/46946127/83900821-f093c280-a727-11ea-9bd5-7f5cd4714d05.png" alt="Flintium"/><br/>
  Ignition Faceplates for Rockwell Process Library AOIs
</p>  

## Software  
* Studio v32.02  
* PlantPAx_Process_Library_v4.10.01  
* Emulate v32.00  
* Ignition v8.0.12  

## Setup  
* Open Git Bash in /Ignition/data/projects folder, and run ```git clone https://github.com/jlbcontrols/Flintium```  
* Import UDTs into Ignition. Flintium's UDTs are stored as a folder structure to improve merging. They must be imported using the tool on project window: Flintium/Administration/ExportImportTags. See Flintium Wiki page [Importing & Exporting UDTs](https://github.com/jlbcontrols/Flintium/wiki/Importing-&-Exporting-UDTs) for more info. The UDTs are stored in the /flintium-tags/FlintiumTypes folder.  
* Import the example instance tags using the Ignition Designer's built-in tool. The tags are saved as /flintium-tags/FlintiumInst.json, which should be imported into the default provider's root folder.  
* Import tag group files located in the /flintium-tags/FlintiumTagGroups folder using the Ignition Designer's built-in tool.  
* Create a Logix Driver device called "plc1" on the gateway webpage.  
* Create a database connection called "historydb" on the gateway webpage.  
* Create an internal user source using the Ignition gateway webpage, called "FlintiumUserSource".  
* Import /flintium-security/roles.json using the tool located on project window: Flintium/Administration/Utilities/ExportImportRolesAndUsers  
* Import /flintium-security/users.json using the tool located on proejct window: Flintium/Administration/Utilities/ExportImportRolesAndUsers

## User Source, Usernames & Passwords 
The project's user source is 'FlintiumUserSource' by default. Note: This means that users must belong to FlintiumUserSource to log into a client.  
Default users and roles are imported into the FlintiumUserSource in the SETUP section above.  
The default password for all imported users is 'password'.  
If logging into the designer with default (or other) user source: To have full permissions for all example project faceplates in the designer, add these roles to your user: 'Administrator' and 'area01'.  

## Modules 
Two third party modules are used in this project.  
* pidbot: Used for PIDE tuning faceplate. Download the latest version at jlbcontrols.com/pidbot.  
* tagScriptModule: Used to automate configuration of UDTs. This module is used for development only, and is not required when using the Flintium library. Converts UDTs created from PlantPAx AOI tag OPC drag/drop, making it closer to the format required for this project. The modl file is included in the flintium-modules folder. If using the tagScriptModule, you need to allow unsigned modules in your /Ignition/data/ignition.conf file, by adding this line to #Java Additional Parameters: ```wrapper.java.additional.4=-Dignition.allowunsignedmodules=true```

## Studio 5000 Project File
See [Issue #162](https://github.com/jlbcontrols/Flintium/issues/162) for status of the project file.  

## More Information
For more information about this project, head to the [Flintium Wiki](https://github.com/jlbcontrols/Flintium/wiki).
