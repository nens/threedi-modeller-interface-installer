dockered nsis
=========

nsis 3 is not that easy to build from sources.

This docker container installs one from apt.

Building
-----------

build the container with tag makensis:latest eg:

	docker build -t makensis:latest path_to_docker_file_goes_here
	
Running
-----------

To run `makensis` from a container create a shell script similar to below, perhaps called `makensis3`, but you can call it anything you want. Actually, you don't have to create this file as it is included in this repository under the name `makensis3`.


	#!/bin/bash
	CWD="$(pwd)"
	docker run -u "$UID" -w "$CWD" --net host -e PYTHONUNBUFFERED=0 makensis "$@"

Be sure to make the `makensis3` script (or whatever you called your script) an executable.

	chmod a+x makensis3

Copy this file into a directory listed in your PATH environment variable to run it from any place you like, eg:

	sudo cp makensis3 /usr/local/bin