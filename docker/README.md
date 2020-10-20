Quickly setup everything needed to run Flintium using Docker, including an Ignition Gateway container and database container.

# Flintium Docker Options
### Option 1: Release
* Easiest setup, with most configuration completed by restoring a .gwbk file.
* Does not use the latest Flintium code. Uses the most recent .gwbk release.
* Dockerfile and docker-compose file located in the [/docker/release](./release) folder.

### Option 2: Development Environment
* Takes a bit longer to setup. Additional steps are needed to configure the gateway.
* Uses the latest Flintium code.
* Sets up a version controlled development environment to work on Flintium. The repository will be cloned on your host computer, and bind-mounted to an Ignition Gateway Docker container. You will be able to use the Ignition Designer as normal, save changes, and commit the changes from the repository on the host. Likewise, any changes made to the repository on the host will automatically show up in the Designer.
* Dockerfile and docker-compose file located in the [/docker/devenv](./devenv) folder.

# Requirements
* Git
* Docker
* Docker Compose

# Instructions
* Clone this repository `git clone https://github.com/jlbcontrols/Flintium.git`.
* Open a terminal in the [/docker/release](./release) or [/docker/devenv](./devenv) folder (locally), and run `docker-compose up`.
* The Ignition Gateway webpage will be available at `http://localhost:8090`.
* See the main README for gateway [login credentials](../README.md#user-source-usernames--passwords).
* See the main README for [PLC Setup](../README.md#PLC-Setup) instructions.

### Additional Steps (Required for Development Environment Only)
* Follow instructions in the main README to [Import Gateway Resources](../README.md#import-gateway-resources-required-for-development-only).
