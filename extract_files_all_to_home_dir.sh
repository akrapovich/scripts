#!/bin/bash
# Exctract all *.tar files to Home directory
for f in *.tar
do
    tar -xvf "$f" -C ~
done

