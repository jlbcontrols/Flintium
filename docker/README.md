Quickly setup everything needed to run Flintium using Docker, including an Ignition Gateway container and database container.

# Flintium Docker Options
### Option 1: Release
* Uses the most recent Flintium release (not the latest Flintium code).
* Easiest setup, with most configuration completed by restoring a .gwbk file.
* Dockerfile and docker-compose file located in the [/docker/release](./release) folder.

### Option 2: Development Environment
* Use the latest Flintium code.
* Setup a version controlled development environment to work on Flintium. The repository will be cloned on your host computer, and bind-mounted to an Ignition Gateway Docker container. You will be able to use the Ignition Designer as normal, save changes, and commit the changes from the repository on the host. Likewise, any changes made to the repository on the host will automatically show up in the Designer.
* Requires additional steps to configure the gateway.
* Dockerfile and docker-compose file located in the [/docker/devenv](./devenv) folder.

### Requirements
* Git
* Docker
* Docker Compose

### Instructions
* Clone this repository `git clone https://github.com/jlbcontrols/Flintium.git`.
* Open a terminal in the [/docker/release](./release) or [/docker/devenv](./devenv) folder (locally), and run `docker-compose up`.
* The Ignition Gateway webpage will be available at `http://localhost:8090`.
* See the main README for gateway [login credentials](../../README.md#user-source-usernames--passwords).
* See the main README for [PLC Setup](../../README.md#PLC-Setup) instructions.

### Additional Instructions (Required for Dev Env Only)
* Follow instructions in the main README to [Import Gateway Resources](../../README.md#Import-Gateway-Resources).
