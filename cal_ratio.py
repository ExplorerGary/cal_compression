# run_cal_ratio.py

import os
import numpy as np
import torch
from utilities import read_pt,to_int
from EG_encoding import ExpGolombEncoding

def preprocess(pt_path:str):
    '''
    阅读一个pt文件，进行预处理转化为整数
    预备后续处理
    
    返回 处理过的array，理论和由os.path.getsize得到的字节数
    
    '''
    pt_array =  to_int(read_pt(pt_path=pt_path))
    byte_theory = 2 * len(pt_array )
    byte_os = os.path.getsize(pt_path)
    
    return pt_array ,byte_theory,byte_os

def cal_ratio(pt_path:str,k:int=0):
    '''
    args: k = 0, 传入ExpGolombEncoding的k
    对一个pt文件进行编码
    计算其压缩比率
    删除原压缩文件
    返回各个答案
    '''
    name = os.path.basename(pt_path)
    pt_array , byte_theory, byte_os  = preprocess(pt_path=pt_path)
    
    EG = ExpGolombEncoding(k=k)
    byte_encoded = len(EG.streamEncode(pt_array))/8
    
    ratio_theory = (byte_theory-byte_encoded)/byte_theory
    ratio_os = (byte_os-byte_encoded)/byte_os
    
    return {"name":name,
            "byte_theory":byte_theory,
            "byte_os":byte_os,
            "byte_encoded":byte_encoded,
            "ratio_theory":ratio_theory,
            "ratio_os":ratio_os
            }

