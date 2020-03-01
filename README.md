# FP - Ignition with PlantPAX AOIs

SOFTWARE  
-Studio v32.02  
-PlantPAx_Process_Library_v4.10.01  
-Emulate 32.00  
-Ignition 8.0.6  

IGNITION LOGIN  
u: admin
pw: password

SETUP  
Clone this repo to /Ignition/data/projects  
Import /tags/dataTypes.json into the Data Types folder in the Ignition Designer  
Import /tags/instance.json into the root Tags folder in the Ignition Designer  
Import the tag-groups file (/tags/groups folder) into Ignition using the Designer  
Add fpImage folder to root of Image Management in Designer
Create a Logix Driver device called "plc1" on the gateway webpage
Create a database connection called "MySQL" on the gateway webpage

MODULES  
Two third party modules are used in this project, but neither are required.  
-pidbot: used for PIDE tuning faceplate.  Download the latest version at jlbcontrols.com/pidbot.
-tagScriptModule: used to automate configuration of UDTs.  Converts PlantPax UDTs from OPC drag/drop closer to the format required for this project.  Included in the modules folder.

ALLOW UNSIGNED MODULES  
Modify /Ignition/data/ignition.conf to add this line to #Java Additional Parameters:  
wrapper.java.additional.4=-Dignition.allowunsignedmodules=true
