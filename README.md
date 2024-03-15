# Pipeline for gene prediction and gene annotation: 

## Tools used for the pipeline: 

1. Gene Prediction: 
For gene prediction we used Prodigal as it was the best performing and user friendly tool after testing.

Article: Hyatt, D., Chen, GL., LoCascio, P.F. et al. Prodigal: prokaryotic gene recognition and translation initiation site identification. BMC Bioinformatics 11, 119 (2010). https://doi.org/10.1186/1471-2105-11-119

2. Gene Annotation: 
For gene annotation we are using Bakta. 

Article: Schwengers, Oliver et al. “Bakta: rapid and standardized annotation of bacterial genomes via alignment-free sequence identification.” Microbial genomics vol. 7,11 (2021): 000685. doi:10.1099/mgen.0.000685

3. Anti-microbial genes: For identifying anti-microbial genes we used AMRfinderplus

Article: Feldgarden M, Brover V, Gonzalez-Escalona N, Frye JG, Haendiges J, Haft DH, Hoffmann M, Pettengill JB, Prasad AB, Tillman GE, Tyson GH, Klimke W. AMRFinderPlus and the Reference Gene Catalog facilitate examination of the genomic links among antimicrobial resistance, stress response, and virulence. Sci Rep. 2021 Jun 16;11(1):12728. doi: 10.1038/s41598-021-91456-0. PMID: 34135355; PMCID: PMC8208984.

4. Bacterial virulence factor: For pathogenicity factor we have used PathOFact. 

Article: de Nies, L., Lopes, S., Busi, S.B. et al. PathoFact: a pipeline for the prediction of virulence factors and antimicrobial resistance genes in metagenomic data. Microbiome 9, 49 (2021). https://doi.org/10.1186/s40168-020-00993-9

 
## Making the required environments for the pipeline: 
Environment for Prodigal: 
```pythonng a
#env for prodigal
conda create -n gene_pred
conda activate gene_pred
conda install -c bioconda prodigal
conda deactivate
```
Environment for Bakta: 
```python
# env for bakta
conda create -n bakta
conda activate bakta
conda install -c conda-forge -c bioconda bakta
bakta_db download --output <output-path> --type full
conda deactivate 
```
Environment for AMRfinder:
```python
# env for amrfinder
conda create -n amrfinder
conda activate amrfinder
mamba install -c bioconda ncbi-amrfinderplus
conda deactivate
```
Environment for PathOFact: 
```python
#env for pathofact
git lfs install
git clone -b master --recursive https://git-r3lab.uni.lu/laura.denies/PathoFact.git
cd PathoFact
conda env create -f=envs/PathoFact.yaml
cd ..
```
## Preparing the assembly files for bakta
Bakta requires assembly files in zipped fasta format. You can use the provided Python script called gzip_it.py to gzip the .fa assembly files.

## Pipeline:
The pipeline takes the input as the fasta files from the assembly and those are used by Prodigal, Bakta and PathOFact. The prodigal generates the faa and gff files that are used by AMR for determining the genes responsible for pathogenicity.

## Pipeline Usage: 

```python
sh pipeline.sh [input_dir] [output_dir]
```

The pipeline fully automates the cumbersome process and it generates the required files that will help in taxonomic classification and comparative genomics.  



