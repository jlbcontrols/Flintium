<p align="center">
  <img src="https://user-images.githubusercontent.com/46946127/83900821-f093c280-a727-11ea-9bd5-7f5cd4714d05.png" alt="Flintium"/><br/>
  Ignition Faceplates for Rockwell Process Library AOIs
</p>  

## Software  
* Ignition v8.0.12   
* PlantPAx_Process_Library_v4.10.01  
* Studio 5000 v32.02  
* Emulate v32.00  

## Setup  
* On your Ignition Gateway computer, open your /Ignition/data/projects folder, and run  
```git clone https://github.com/jlbcontrols/Flintium.git```  
* Import UDTs into Ignition. Flintium's UDTs are stored as a folder structure to improve merging. They must be imported using the tool on project window: Flintium/Administration/ExportImportTags. See Flintium Wiki page [Importing & Exporting UDTs](https://github.com/jlbcontrols/Flintium/wiki/Importing-&-Exporting-UDTs) for more info.
* Import the example instance tags using the Ignition Designer's built-in tool. The tags are saved as [/flintium-tags/FlintiumInst.json](https://github.com/jlbcontrols/Flintium/blob/master/flintium-tags/FlintiumInst.json), which should be imported into the default provider's root folder.  
* Import tag group files located in the [/flintium-tags/FlintiumTagGroups](https://github.com/jlbcontrols/Flintium/tree/master/flintium-tags/FlintiumTagGroups) folder using the Ignition Designer's built-in tool.  
* Create a Logix Driver device called ```plc1``` on the gateway webpage.  
* Create a database connection called ```historydb``` on the gateway webpage.  
* Create an internal user source using the Ignition gateway webpage, called ```FlintiumUserSource```.  
* Import [/flintium-security/roles.json](https://github.com/jlbcontrols/Flintium/blob/master/flintium-security/roles.json) using the tool located on project window: Flintium/Administration/Utilities/ExportImportRolesAndUsers  
* Import [/flintium-security/users.json](https://github.com/jlbcontrols/Flintium/blob/master/flintium-security/users.json) using the tool located on proejct window: Flintium/Administration/Utilities/ExportImportRolesAndUsers

## User Source, Usernames & Passwords 
* The project's user source is ```FlintiumUserSource``` by default. Note: This means that users must belong to FlintiumUserSource to log into a client.  
* Default users and roles are imported into the FlintiumUserSource in the SETUP section above.  
* The default password for all imported users is ```password```  
* If logging into the designer with default (or other) user source: To have full permissions for all example project faceplates in the designer, add these roles to your user: ```Administrator``` and ```area01```  

## Modules 
Two third party modules are used in this project.  
* pidbot: Used for PIDE tuning faceplate. Download the latest version from here: [https://www.jlbcontrols.com/pidbot](https://www.jlbcontrols.com/pidbot)  
* tagScriptModule: Used to automate configuration of UDTs. This module is used for development only, and is not required when using the Flintium library. Converts UDTs created from PlantPAx AOI tag OPC drag/drop, making it closer to the format required for this project. The modl file is included in the flintium-modules folder. If using the tagScriptModule, you need to allow unsigned modules in your /Ignition/data/ignition.conf file, by adding this line to #Java Additional Parameters: ```wrapper.java.additional.4=-Dignition.allowunsignedmodules=true```

## Studio 5000 Project File
See [Issue #162](https://github.com/jlbcontrols/Flintium/issues/162) for status of the project file.  

## More Information
For more information about this project, head to the [Flintium Wiki](https://github.com/jlbcontrols/Flintium/wiki).

## Alternate Setup
It is recommended to use the setup procedure above, which allows you to easily pull the latest updates, and ensures you receive version controlled files. However, Gateway backups are made occasionally, and can be downloaded at the link below. The gateway backups are not tested or version controlled, and may not reflect the latest updates.
* Download a Flintium Gateway backup from here: [Flintium Gateway Backups](https://drive.google.com/drive/folders/1VR1llj7gU4xmlLSO3eSFc16aup2XHHFG?usp=sharing)  
* Restore the gateway backup, and login to the gateway webpage with username: ```admin``` password: ```password```  
* Using the gateway webpage, edit the ```historydb``` database connection details to connect to a database that you create.
* Using the gateway webpage, edit the ```plc1``` device connection details to connect to a Logix PLC, or RSLogix Emulate application that you have set up.
* See the **User Source, Usernames & Passwords** section for Client login details.
* See the **Modules** section for module installation details.
