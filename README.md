<p align="center">
  <img src="https://user-images.githubusercontent.com/46946127/83900821-f093c280-a727-11ea-9bd5-7f5cd4714d05.png" alt="Flintium"/><br/>
  Ignition Faceplates for Rockwell Process Library AOIs
</p>  

# Software  
* Ignition v8.0.12   
* PlantPAx_Process_Library_v4.10.01  
* Studio 5000 v32.02  
* Emulate v32.00  

# Basic Setup
The easiest way to try Flintium is to use a Flintium gateway backup file. Note that the gateway backups do not reflect the latest updates. If you would like to use the latest Flintium code, see the Development Environment Setup section instead.
### Restoring a Gateway Backup
* Download a Flintium Gateway backup from here: [Flintium Gateway Backups](https://drive.google.com/drive/folders/1VR1llj7gU4xmlLSO3eSFc16aup2XHHFG?usp=sharing).
* Restore the .gwbk following Ignition's [gateway restore instructions](https://docs.inductiveautomation.com/display/DOC80/Gateway+Backup+and+Restore).
* See the [User Source, Usernames & Passwords](#user-source-usernames--passwords) for login details.
* Follow the instructions in the [Database Setup](#Database-Setup), [Modules Setup](#Modules-Setup), and [PLC Setup](#PLC-Setup) sections below to complete the setup.

# Development Environment Setup  
Follow these instructions to use the latest Flintium code, and set up a version controlled development environment.
### Option 1: Docker
* Follow the [Flintium Docker Dev Environment README](./docker/devenv/README.md) instructions.
* Follow instructions below to [Import Gateway Resources](#Import-Gateway-Resources).
* Follow instructions in the [PLC Setup](#PLC-Setup) section to connect to your PLC.

### Option 2: Using a Local Ignition Gateway 
* On your Ignition Gateway computer, open your /Ignition/data/projects folder, and run  
`git clone https://github.com/jlbcontrols/Flintium.git`  
* Follow instructions below to [Import Gateway Resources](#Import-Gateway-Resources).
* Follow the instructions in the [Database Setup](#Database-Setup), [Modules Setup](#Modules-Setup), and [PLC Setup](#PLC-Setup) sections below to complete the setup.

### Import Gateway Resources
* Import UDTs into Ignition. Flintium's UDTs are stored as a folder structure to improve merging. They must be imported using the tool on project window: Flintium/Administration/ExportImportTags. See Flintium Wiki page [Importing & Exporting UDTs](../../wiki/Importing-&-Exporting-UDTs) for more info.
* Import the example instance tags using the Ignition Designer's built-in tool. The tags are saved as [/gw-resources/tags/FlintiumInst.json](./gw-resources/tags/FlintiumInst.json), which should be imported into the default provider's root folder.  
* Import tag group files located in the [/gw-resources/tags/tag-groups](./gw-resources/tags/tag-groups) folder using the Ignition Designer's built-in tool.  
* Create an internal user source using the Ignition gateway webpage, called `FlintiumUserSource`.  
* Import [/gw-resources/user-sources/FlintiumUserSource/roles.json](./gw-resources/user-sources/FlintiumUserSource/roles.json) using the tool located on project window: Flintium/Administration/Utilities/ExportImportRolesAndUsers  
* Import [/gw-resources/user-sources/FlintiumUserSource/users.json](./gw-resources/user-sources/FlintiumUserSource/users.json) using the tool located on proejct window: Flintium/Administration/Utilities/ExportImportRolesAndUsers

# Additional Setup (if required)  
### Database Setup
By default, historical tags in this project use a database connection called `historydb`.
* Create a database to use with Ignition's Historian. Ignition supports many popular databases.
* Create a connection to your database called `historydb` using the gateway webpage. If you restored a Gateway Backup, a connection called `historydb` is configured already. Change the configuration of this connection as necessary to connect with your database.

### Modules Setup
Two third party modules are used in this project. The `pidbot` module is used for tuning P_PIDE controllers. The `Flintium Tag Config Tools` module is used for development only, and is not required when using the Flintium library. Converts UDTs created from PlantPAx AOI tag OPC drag/drop, making it closer to the format required for this project.  
* [Download Pidbot](https://www.jlbcontrols.com/pidbot) module from JLB Controls.
* [Download Flintium Tag Config Tools](https://github.com/jlbcontrols/flintium-tag-config-tools) module from the releases section of the Github repository.
* Install the .modl files following Ignition's [module installation instructions](https://docs.inductiveautomation.com/display/DOC80/Installing+or+Upgrading+a+Module).

### PLC Setup
The examlpe tags in this project are mapped to Ignition's built-in OPC server `Ignition OPC UA Server`, and a device `plc1`.
* Create a Logix Driver device called `plc1` using the gateway webpage. If you restored a Gateway Backup, a device called `plc1` is configured already.  
* Edit connectivity settings for `plc1` to connect with your Logix PLC or RSLogix Emulate. See more details on setting up [RSLogix Emulate](../../wiki/Setting-up-RSLogix-Emulate).
* Develop your PLC code using AOIs from Rockwell's Process Library v4.10.01. Search for "Process Library" in [Rockwell Downloads](https://compatibility.rockwellautomation.com/Pages/MultiProductDownload.aspx?crumb=112).
* See [Issue #162](../../issues/162) for the status of the Studio 5000 project file associated with Flintium's example tags.

# User Source, Usernames & Passwords
### Gateway/Designer
* Login credentials for the Ignition Gateway webpage are username: `admin`, password `password`.
* Gateway uses the `Default` user source.
* If logging into the Designer with `Default` (or other) user source: To have full permissions for all example project faceplates in the designer, add these roles to your user: `Administrator` and `area01`.
### Client
* The project's user source is `FlintiumUserSource` by default. Note: This means that users must belong to FlintiumUserSource to log into a client.  
* Default users are configured in `FlintiumUserSource`: `defaultAdmin`, `defaultEngr`, `defaultMaintSup`, `defaultMaint`, `defaultOperSup` and `defaultOper`. The default password for all users is `password`.

# More Information
For more information about this project, and how to contribute head to the [Flintium Wiki](../../wiki).
