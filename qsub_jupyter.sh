#!/bin/bash
qsub -q m*@* -b y -cwd -V -N inotebook ./jupyter_cluster.sh
