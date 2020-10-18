
# Development Environment Setup with Docker
These instructions will help you set up an development environment to work on Flintium. This repository will be cloned on your host computer, and bind-mounted to an Ignition Gateway Docker container. You will be able to use the Ignition Designer as normal, save changes, and commit the changes from the repository on the host. Likewise, any changes made to the repository on the host will automatically show up in the Designer. A database is set up in another container which is used by Ignition's historian.  

**Note: This has only been tested with a Linux host.**

### Requirements
* Git
* Docker
* Docker Compose

### Instructions
* Clone this repository `git clone https://github.com/jlbcontrols/Flintium.git`.
* Open a terminal in the [/docker/devenv](./devenv) folder (locally), and run `docker-compose up`.
* The Ignition Gateway webpage will be available at `http://localhost:8090`.
* If this is your first time setting up this project, or if any gateway resources in this repository have changed, you will need to import them. Follow the [Manual Setup](../README.md#Manual-Setup) instructions in the main README.
