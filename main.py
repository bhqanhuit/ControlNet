from share import *

import pytorch_lightning as pl
from torch.utils.data import DataLoader
from data_utils.dataset import MyDataset
# from cldm.logger import ImageLogger
# from cldm.model import create_model, load_state_dict
from base_config.base_config import build_arg

import warnings
warnings.filterwarnings("ignore")

# build config
opt = build_arg()

print(opt.data_root_dir)
dataset = MyDataset(opt)
# dataloader = DataLoader(dataset, num_workers=0, batch_size=3, shuffle=True)
