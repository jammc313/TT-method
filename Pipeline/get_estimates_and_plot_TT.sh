#!/bin/bash -l

# This bash script implements scripts which take as input the sample configuration counts outputted by 'get_counts_TT.sh'. These counts, should already be present in 'DIR_counts_per_5cm_TT/'.
# Before running this script, users should have the following empty directories to output results: 'DIR_estimates_TT/' and 'DIR_plots/'.
# The scripts below use the sample configuration counts to estimate divergence times (and other statistics of interest) for each of the comparisons. The resulting estimates can be found in 'DIR_estimates_TT/' with resulting plots found in 'DIR_plots' 

python get_estimates_TT.py &&
Rscript plot_TT.R

