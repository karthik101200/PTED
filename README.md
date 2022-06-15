# PTED

## Instruction to run the code
### Clone the repository
``` shell
git clone https://github.com/karthik101200/PTED.git
```

### Make an environment
``` shell
conda create -y -n pted python=3.7
conda activate pted
conda install -y -c anaconda numpy scipy
conda install -y -c conda-forge h5py opencv tqdm
conda install -y -c pytorch pytorch torchvision cudatoolkit=10.2
pip3 install h5py==3.1.0
pip3 install hdf5plugin
pip3 install numba
```
### Run the Code 
``` shell
cd PTED
python3 convert_to_TS.py --h5file {add the h5 file path}
```
