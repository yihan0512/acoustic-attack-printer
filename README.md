# classifing 3d printing recordings 

## install
required packages
- `torch`, `torchvision`. `torchaudio`, `tensorboard`, `tqdm`

## run
* create `data/` in `repo_root`
* split train and test set `python train_test_split.py DATASET_DIR SPLIT_RATIO`
  (e.g. `python train_test_split.py data/F2000 0.8`, the resulting dir will be `data/F2000_split`)
* run `train_BiLSTM.ipynb`
