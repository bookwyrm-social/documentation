#!/bin/bash

# latest
./bw-dev messages:update
python generate.py

# versions
for tag in $(git tag);
do
    git checkout ${tag}
    ./bw-dev messages:update
    python generate.py ${tag}
    git restore .
done