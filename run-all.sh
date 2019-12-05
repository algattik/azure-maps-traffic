#!/bin/bash

set -euo pipefail
set -x

mkdir -p data
python code/download-map-tiles.py
python code/download-traffic-tiles.py
python code/stitch-images.py
python code/download-routes.py
python code/draw-routes.py
python code/quantize-traffic.py
