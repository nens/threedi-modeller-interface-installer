# The following docker lines are taken from the original 
# makensis docker file (from Marco Duiker). 

FROM ubuntu:focal

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

RUN dpkg --add-architecture i386 \ 
    && apt-get update \
    && apt-get install -y \
    wget make unzip git curl \
    && apt-get clean -y

# WORKDIR /installer/3Di-additions