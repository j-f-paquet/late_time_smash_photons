#!/bin/bash
#SBATCH -c 1
#SBATCH --mem=0
#SBATCH --time=200:00
#SBATCH --account=def-gale

cd /project/def-gale/paquet/smash_photons/rhic_final_hydros/photons_T140-150_nx200_modified_brem

icpc -O3 photon.cpp rates.cpp

time ./a.out
