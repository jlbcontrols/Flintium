# Flintium - Ignition Faceplates for PlantPAX AOIs

SOFTWARE  
-Studio v32.02  
-PlantPAx_Process_Library_v4.10.01  
-Emulate 32.00  
-Ignition 8.0.6  

SETUP  
Open Git Bash in /Ignition/data/projects folder, and run ```git clone https://github.com/jlbcontrols/Flintium```  
Import UDTs into Ignition (files located at /flintium-tags/udt_types_/Flintium/...). To import all at once, use the tool located on project window: Administration/Utilities/Export Import All UDTs Individually  
Import /flintium-tags/instance.json into the root Tags folder in the Ignition Designer  
Import the tag-groups file (/flintium-tags/groups folder) into Ignition using the Designer   
Create a Logix Driver device called "plc1" on the gateway webpage  
Create a database connection called "historydb" on the gateway webpage  
Create an internal user source using the Ignition gateway webpage, called "FlintiumUserSource"  
Import /flintium-security/roles.json using the tool located on project window: Administration/Utilities/Export Import Roles and Users  
Import /flintium-security/users.json using the tool located on proejct window: Administration/Utilities/Export Import Roles and Users  

USER SOURCE, USERNAMES & PASSWORDS  
The project's user source is 'FlintiumUserSource' by default. Note: This means that users must belong to FlintiumUserSource to log into a client.  
Default users and roles are imported into the FlintiumUserSource in the SETUP section above.  
The default password for all imported users is 'password'.  
If logging into the designer with default (or other) user source - To have full permissions for all example project faceplates in the designer, add these roles to your user: 'Administrator' and 'area01'.  

MODULES  
Two third party modules are used in this project, but neither are required.  
-pidbot: used for PIDE tuning faceplate.  Download the latest version at jlbcontrols.com/pidbot.  
-tagScriptModule: used to automate configuration of UDTs.  Converts PlantPax UDTs from OPC drag/drop closer to the format required for this project.  Included in the flintium-modules folder.

ALLOW UNSIGNED MODULES (Only needed if using the tagScriptModule)  
Modify /Ignition/data/ignition.conf to add this line to #Java Additional Parameters:  
wrapper.java.additional.4=-Dignition.allowunsignedmodules=true
