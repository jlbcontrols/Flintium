
# Development Environment Setup with Docker
Note: These instructions have only been tested with a Linux host.

These instructions will help you set up an development environment to work on Flintium. This repository will be cloned on your host computer, and bind-mounted to an Ignition Gateway Docker container. You will be able to use the Ignition Designer as normal, save changes, and commit the changes from the repository on the host. Likewise, any changes made to the repository on the host will automatically show up in the Designer. A database is set up in another container which is used by Ignition's historian.  

### Requirements
* Git
* Docker
* Docker Compose

### Instructions
* Clone this repository `git clone https://github.com/jlbcontrols/Flintium.git`.
* Open a terminal in the [/docker/devenv](./devenv) folder (locally), and run `docker-compose up`.
* The Ignition Gateway webpage will be available at `http://localhost:8090`.
* If this is your first time setting up this project or if gateway resources in this repository have changed, continue following the [Development Environment Option 1: Docker](../README.md#option-1-docker) instructions in the main README.
