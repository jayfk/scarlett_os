#!/bin/bash
#
########################################################################
# Performs cleanup, ensure unnecessary packages are removed
########################################################################
# `apt-mark showauto` for any additional installed packages

apt-get autoclean -y && \
apt-get autoremove -y && \
rm -rf /var/lib/{cache,log}/ && \
rm -rf /var/lib/apt/lists/*.lz4
