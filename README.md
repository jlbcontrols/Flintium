# FP
Ignition with PlantPAX AOIs

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
Import the tag files (/tags folder) into Ignition using the Designer
Import the tag-groups file (/tags/groups folder) into Ignition using the Designer

MODULES
Two third party modules are used in this project, but neither are required. The .modl files are included in the modules folder.
-pidbot: used for PIDE tuning faceplate.
-tagScriptModule: used to automate configuration of UDTs.  Converts PlantPax UDTs from OPC drag/drop closer to the format required for this project.

ALLOW UNSIGNED MODULES
Modify /Ignition/data/ignition.conf to add this line to #Java Additional Parameters:
wrapper.java.additional.4=-Dignition.allowunsignedmodules=true
