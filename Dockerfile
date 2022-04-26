# The following docker lines are taken from the original 
# makensis docker file (from Marco Duiker). 

FROM ubuntu:bionic

## for apt to be noninteractive
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

RUN    echo $TZ > /etc/timezone                                              \
    && apt-get -y update                                                     \
    && apt-get -y install --no-install-recommends nsis locales               \
    && apt-get clean                                                         \
    && apt-get purge                                                         \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# locale config needed for nsis tp prevent errors like:
# Unable to convert string to codepage 0
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8 

# build with: docker built -t makensis:latest
# then create /usr/bin/makensis3 with contents:
##!/bin/bash
#CWD="$(pwd)"
#docker run -u "$UID" -w "$CWD" --net host -v /var/www:/var/www -v /home/marco:/home/marco -e PYTHONUNBUFFERED=0 makensis bash -c "/usr/bin/makensis $@"
# then use: makensis3 --help

# Continue the original image

RUN dpkg --add-architecture i386 \ 
    && apt-get update \
    && apt-get install -y \
    perl libfile-copy-recursive-perl libfile-rsync-perl wget unzip git wine-stable wine32 \
    && apt-get clean -y

WORKDIR /installer/3Di-additions