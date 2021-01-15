---------------------------------------------------------
README : The TT method
---------------------------------------------------------

This repository contains guidelines and scripts for implementating the TT method for estimating divergence times between populations.
This simple, quick, and transparent method requires two haploid genomes (or a single diploid genome) from each of two populations. Please see the published paper for details.

The directory 'Pipeline' contains all the scripts necessary to run both the TT method (estimating divergence times without using an outgroup) and the TTO method (estimating population divergence using an outgroup). Users should download all scripts and empty directories to a suitable location.

Both TT and TTO methods require the ancestral states at all positions in the genome. An example of such files created for the human genome based on consensus among three species of apes can be found at the zenodo DOI below. The TT & TTO methods consider a particular position informative only when the ancestral state has consensus support among all three of Gorilla, Chimpanzee and Orangutan. If intending to estimate divergence times for human populations, the files in 'ancestral_states' can be downloaded and used. To estimate divergence times for other species, the user will need to create their own 'ancestral state' files of similar format, (one '.txt' file per chromosome, one line per site, for all sites in the genome).
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4441887.svg)](https://doi.org/10.5281/zenodo.4441887)

---------------------------------------------------------

To implement the methods, users should edit the following downloaded scripts:

'get_file_name.py' - this script links keywords to full vcf file names and paths for ease of implementation. Edit to include a keyword for each individual's vcfs.

'count_sample_confs_per_ind_TT.py' & 'count_sample_confs_per_ind_TTO.py'.<br/>
These scripts take all-sites vcfs as input, and return counts of sample configurations in 5MB blocks of the genome. Users should edit each script to include file paths for downloaded/created ancestral state files and vcf files. Resulting counts are outputted to 'DIR_counts_per_5cm_TT/' and 'DIR_counts_per_5cm_TTO/' respectively.

'get_counts_TT.sh' and 'get_counts_TTO.sh'.<br/>
These are example SLURM submission scripts that can be used to implement the above scripts for the 22 autosomes of the human genome, and for as many pairwise individual comparisons as desired. Users should edit to include relevant vcf keywords and SLURM commands.

'get_estimates_and_plot_TT.sh'.<br/>
This simple bash script which will implement 'get_estimates_TT.py', using the sample configuration counts previously obtained to estimate parameters including divergence times. Results are outputted to 'DIR_estimates_TT/' and the R script 'plot_TT.R' will output resulting plots to 'DIR_plots/'.

'get_estimates_and_plot_TTO.sh'.<br/>
Implements the equivalent scripts for the TTO method, also outputting resulting plots 'DIR_plots/'.

---------------------------------------------------------

Once the above scripts have been edited, the TT & TTO methods can be implemented simply by using:<br/>
bash get_counts_TT.sh<br/>
bash get_counts_TTO.sh<br/>
bash get_estimates_and_plot.sh<br/>

---------------------------------------------------------

For reference:<br/>
Estimating divergence times from DNA sequences.<br/>
Per Sjödin, James McKenna, Mattias Jakobsson.<br/>
doi: https://doi.org/10.1101/2020.10.16.342600 








