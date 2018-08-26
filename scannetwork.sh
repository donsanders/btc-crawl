#!/bin/sh
mkdir -p scans
for i in $(seq 100) ; do ./btc-crawl --concurrency=1000 --output="scans/Satoshi-0-16-3-"$i".json" --peer-age="24h" --user-agent="/Satoshi:0.16.3/" --verbose & echo pre-sleep ; sleep 1800 ; echo post-sleep ; kill `pidof btc-crawl` ; done
