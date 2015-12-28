#!/bin/bash
docker run --device /dev/mem:/dev/mem --privileged -p 80:5000 -ti rpi-mearm-wb /bin/bash