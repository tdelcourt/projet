#!/bin/bash -l

#PBS -l nodes=1:ppn=1
#PBS -l walltime=00:10:00
#PBS -o test1.out
#PBS -N test1

# echo "Running job on $HOST - " `date` 
# echo "prout"
# run_prog -tmp $TMPDIR -in $HOME/my_input -out $WORKDIR/my_output 


# cd $TMPDIR

module load python/3.4.0a1 

python3.4 $HOME/projet_hydra.py -out $TMPDIR/test1
# cd $TMPDIR
gzip ./test1.out

mv ./test1.out.gz $HOME/

# CLeanup my temporary space:

# Make sure that I am still in my temporary space:

# cd $TMPDIR 
# echo "Done"
# Delete everything

#/bin/rm -r *