# F2

## Environmental Requirements

Create environment for prodigal
```
conda create -n gene_pred
conda activate gene_pred
conda install -c bioconda prodigal
conda deactivate
```

Create environment for bakta
```
conda create -n bakta
conda activate bakta
conda install -c conda-forge -c bioconda bakta
bakta_db download --output <output-path> --type full
conda deactivate 
```

Create environment for amrfinder
```
conda create -n amrfinder
conda activate amrfinder
mamba install -c bioconda ncbi-amrfinderplus
conda deactivate
```

Create environment for pathofact
```
git lfs install
git clone -b master --recursive https://git-r3lab.uni.lu/laura.denies/PathoFact.git
cd PathoFact
conda env create -f=envs/PathoFact.yaml
cd ..
```

## Commandline usage for pipeline.sh

```
sh pipeline.sh <input_dir> <output_dir>
```
