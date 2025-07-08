# run
import os
import torch
import numpy as np
from concurrent.futures import ProcessPoolExecutor, as_completed
import csv
from tqdm import tqdm

from cal_ratio import cal_ratio
from utilities import scan_pt







def main():
    if not torch.cuda.is_available():
        print("local test")
    else:
        print("running on hpc")
        
    # base_dir = "D:\\NYU_Files\\2025 SPRING\\Summer_Research\\新\\PYTHON\\QWEN\\dummy_files" if (not torch.cuda.is_available) else "/gpfsnyu/scratch/zg2598/Qwen/OUT/COMMUNICATION_LOG/"
    base_dir = "D:\\NYU_Files\\2025 SPRING\\Summer_Research\\新\\PYTHON\\QWEN\\dummy_files" if (not torch.cuda.is_available()) else "/gpfsnyu/scratch/zg2598/Qwen/OUT/COMMUNICATION_LOG/"
    print(f"working on: {base_dir}")
    avail_pt = scan_pt(base_dir=base_dir)
    
    print(f"{len(avail_pt)} files found...")

    csv_path = os.path.join(base_dir, "004_COMPRESSION_RESULTS_PROCESSPOOL.csv")
    fieldnames = ["name", "byte_theory", "byte_os", "byte_encoded", "ratio_theory", "ratio_os"]

    
    
    # ✅ 修复缩进问题
    with open(csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with ProcessPoolExecutor(max_workers=4) as executor:
            k = 0 # 或者你可以根据需要设置k的值
            futures = [executor.submit(cal_ratio, path, k) for path in avail_pt]

            for future in tqdm(as_completed(futures), total=len(futures)):
                try:
                    ans = future.result()
                    writer.writerow(ans)
                    csvfile.flush()
     
                except Exception as e:
                    print(f"[Error] One task failed: {e}")

    return csv_path
if __name__ == "__main__":
    csv_path = main()
    print(f"ALL FILE PRPROCESSED, CHECK\n{csv_path}\nTO SEE THE RESULT")




# if not torch.cuda.is_available():
#     print("local test")
# else:
#     print("running on hpc")
    
# BASE_DIR = "" if torch.cuda.is_available() else ""
# avail_pt = scan_pt(BASE_DIR)
# print(f"{len(avail_pt)} files found...")