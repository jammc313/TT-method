---------------------------------------------------------
README : The TT method
---------------------------------------------------------

This repository contains guidelines and scripts for implementating the TT method for estimating divergence times between populations.
This quick and transparent method requires two haploid genomes (or a single diploid genome) from each of two populations. Please see the published paper for details.

The directory 'Pipeline' contains all the scripts necessary to run both the TT method (estimating divergence times without using an outgroup) and the TTO method (estimating population divergence using an outgroup). Users should download all scripts and empty directories to a suitable location.

Both TT and TTO methods require the ancestral states at all positions in the genome. An example of such files created for the human genome based on consensus among three species of apes can be found at the zenodo DOI below. The TT & TTO methods consider a particular position informative only when the ancestral state has consensus support among all three of Gorilla, Chimpanzee and Orangutan. If intending to estimate divergence times for human populations, the files in 'Ancestral_states.zip' can be downloaded and used (without decompressing). To estimate divergence times for other species, the user will need to create their own ancestral state files of similar format, (one '.txt' file per chromosome, one line per site, for all sites in the genome).
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.4441887.svg)](https://doi.org/10.5281/zenodo.4441887)

---------------------------------------------------------

Description of scripts:

'get_file_name.py' - this script links keywords to full vcf file names and paths for ease of implementation. The User should edit to include vcf file paths and a relevant keyword for each individual's vcfs.

'count_sample_confs_per_ind_TT.py' & 'count_sample_confs_per_ind_TTO.py'.<br/>
These scripts take all-sites vcfs as input, and return counts of sample configurations in 5MB blocks of the genome. Users should edit each script to include file paths for downloaded/created ancestral state files and vcf files. Resulting counts are outputted to 'DIR_counts_per_5cm_TT/' and 'DIR_counts_per_5cm_TTO/' respectively.

'get_counts_TT.sh' and 'get_counts_TTO.sh'.<br/>
These are example SLURM submission scripts that can be used to implement the above scripts for the 22 autosomes of the human genome, and for as many pairwise individual comparisons as desired. Users should edit to include relevant vcf keywords and SLURM commands.

'get_estimates_TT.py'.<br/>
This script uses the sample configuration counts previously obtained to estimate parameters including divergence times. Results are outputted to 'DIR_estimates_TT/'.

'get_estimates_TTO.py'.<br/>
This script uses the sample configuration counts previously obtained to estimate parameters including divergence times. Results are outputted to 'DIR_estimates_TTO/'.

'plot_TT.R'.<br/>
This R script will create plots of divergence time estimates present in 'DIR_estimates_TT/', and output plots to 'DIR_plots/'.

'plot_TTO.R'.<br/>
This R script will create plots of divergence time estimates present in 'DIR_estimates_TTO/', and output plots to 'DIR_plots/'.

'wbj.py'.<br/>
This script contains functions used by 'get_estimates_TT.py' and 'get_estimates_TTO.py' to perform weighted bloack jack-knife estimation of parameters.

---------------------------------------------------------

Implementation:<br/>
The User should create the following directories at the same location as scripts:<br/>
DIR_counts_per_5cm_TT<br/>
DIR_counts_per_5cm_TTO_$OUTGROUP<br/>
DIR_error_TT<br/>
DIR_error_TTO<br/>
DIR_estimates_TT<br/>
DIR_estimates_TTO/$OUTGROUP_res/<br/> 
DIR_plots/TTO_$OUTGROUP<br/>
(where $OUTGROUP is the keyword of an outgroup individual from 'get_file_name.py')

Once the necessary script have been edited to include vcf locations, the TT & TTO methods can be implemented simply by using:<br/>
bash get_counts_TT.sh<br/>
python get_estimates_TT.py<br/>
Rscript TT_plot.R

bash get_counts_TTO.sh<br/>
python get_estimates_TTO.py $OUTGROUP<br/> 
Rscript TTO_plot.R $OUTGROUP<br/> 
(where OUTGROUP is the keyword of an outgroup individual from 'get_file_name.py')


---------------------------------------------------------

For reference:<br/>
Estimating divergence times from DNA sequences.<br/>
Per Sjödin, James McKenna, Mattias Jakobsson.<br/>
https://doi.org/10.1093/genetics/iyab008








