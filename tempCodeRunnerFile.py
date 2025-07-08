csv_path = os.path.join(base_dir, "004_COMPRESSION_RESULTS_PROCESSPOOL.csv")
#     fieldnames = ["name", "original_bytes", "original_bytes_os", "compressed_bytes", "compression_ratio", "compression_ratio_os"]

#     # ✅ 修复缩进问题
#     with open(csv_path, mode='w', newline='', encoding='utf-8') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         writer.writeheader()

#         with ProcessPoolExecutor(max_workers=4) as executor:
#             futures = [executor.submit(cal_ratio, path) for path in avail_pt]

#             for future in tqdm(as_completed(futures), total=len(futures)):
#                 try:
#                     ans = future.result()
#                     writer.writerow(ans)
#                     # current output:
#                     '''
#                     name	original_bytes	original_bytes_os	compressed_bytes	compression_ratio	compression_ratio_os
# R_1_E_0_S_9_B_95.pt	[27228  4934 29184 ... 44630 32496 56268]	29383784	37213551.75	"[-1365.73834839 -7541.26829145 -1274.1354081  ...  -832.82370043
#  -1144.17330595  -660.3626173 ]"	-0.266465604

#                     '''
#                     csvfile.flush()
     
#                 except Exception as e:
#                     print(f"[Error] One task failed: {e}")


