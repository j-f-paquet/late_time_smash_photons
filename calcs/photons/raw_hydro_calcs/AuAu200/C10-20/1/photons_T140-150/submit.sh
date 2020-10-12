#!/bin/bash
#SBATCH -c 1
#SBATCH --mem=0
#SBATCH --time=8000:00
#SBATCH --account=def-gale

cd /scratch/paquet/smash_photons/rhic_final_hydros/photons_T140-150

icpc -O3 photon.cpp rates.cpp

time ./a.out
