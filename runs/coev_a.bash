#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=30:00:00
#PBS -o coev_a.out
#PBS -N coev_a

module load python/3.4.0a1 

python3.4 $HOME/coev_hydra.py