# view_distribution.py
'''
使用这个脚本查看各个.pt文件的数值分布，方便日后bucket化
'''

# 未完成

import os
import numpy as np
import torch
from concurrent.futures import ProcessPoolExecutor, as_completed
import csv
from tqdm import tqdm
import multiprocessing

from utilities import scan_pt,read_pt,to_int
from cal_ratio import preprocess

def view_distribution(pt_path:str,img_path:str,scale:float=1e6):
    ''' 
    阅读一个.pt文件，然后对他进行计算，产看其数值分布后，将结果写入,
    '''
    name = os.path.basename(pt_path)
    pt_array,_,__ = preprocess(pt_path=pt_path,scale=scale)
    del _
    del __
    
    



def main():
    print("total cpu:", multiprocessing.cpu_count())
    max_workers=max(4,multiprocessing.cpu_count()-2)
    print(f"working on: {max_workers}")
    if not torch.cuda.is_available():
        print("local test")
    else:
        print("running on hpc")
        
    # base_dir = "D:\\NYU_Files\\2025 SPRING\\Summer_Research\\新\\PYTHON\\QWEN\\dummy_files" if (not torch.cuda.is_available) else "/gpfsnyu/scratch/zg2598/Qwen/OUT/COMMUNICATION_LOG/"
    base_dir = "D:\\NYU_Files\\2025 SPRING\\Summer_Research\\新\\PYTHON\\QWEN\\dummy_files" if (not torch.cuda.is_available()) else "/gpfsnyu/scratch/zg2598/Qwen/OUT/COMMUNICATION_LOG/"
    print(f"working on: {base_dir}")
    avail_pt = scan_pt(base_dir=base_dir)
    
    print(f"{len(avail_pt)} files found...")
    
    pass
if __name__ == "__main__":
    main()