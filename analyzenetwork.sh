#!/bin/sh
./scannetwork.sh
./cleanscans.sh
python testforsmallworldness.py
