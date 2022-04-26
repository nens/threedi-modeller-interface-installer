FROM ubuntu:cosmic
MAINTAINER Marco Duiker

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
