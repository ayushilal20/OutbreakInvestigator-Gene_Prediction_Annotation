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
