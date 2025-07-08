import os
import torch
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

from utilities import scan_csv


def select_csv(data_folder="./DATA/"):
    avail_csv = scan_csv(data_folder)
    print(f"共找到 {len(avail_csv)} 个 CSV 文件")
    for idx, a_csv in enumerate(avail_csv):
        print(f"[{idx}] {a_csv}")
    
    file_idx = int(input("请输入你想分析的 CSV 编号："))
    return pd.read_csv(avail_csv[file_idx]), avail_csv[file_idx]


def select_columns(df):
    print("\n列名如下：")
    for i, col in enumerate(df.columns):
        print(f"[{i}] {col}")
    
    col_input = input("\n请输入列编号（如 2 或 1:4）：")
    if ':' in col_input:
        start, end = map(int, col_input.split(":"))
        return df.columns[start:end]
    else:
        return [df.columns[int(col_input)]]


def describe_columns(df, columns):
    print(f"\n正在分析列: {columns}")
    print(df[columns].describe())


def plot_histograms(df, columns, bins=50, percentage_enable=True):
    for col in columns:
        data = df[col].dropna()
        plt.figure(figsize=(8, 5))

        # 百分比模式
        if percentage_enable:
            counts, bin_edges, patches = plt.hist(data, bins=bins, density=True, edgecolor='black', color='skyblue')
            percentages = counts * np.diff(bin_edges) * 100
            plt.clf()
            plt.bar(bin_edges[:-1], percentages, width=np.diff(bin_edges), align="edge", edgecolor='black', color='skyblue')
            plt.ylabel("Percentage (%)")
            plt.gca().yaxis.set_major_formatter(PercentFormatter())
        else:
            plt.hist(data, bins=bins, edgecolor='black', color='skyblue')
            plt.ylabel("Frequency")

        plt.xlabel(col)
        plt.title(f"Histogram of {col}")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig(f"Histogram of {col}.png")
        plt.show()


def main():
    percentage_enable = True  # 默认启用百分比 y 轴
    data_folder = "./DATA/"
    
    df, selected_csv_path = select_csv(data_folder)
    cols_to_analyze = select_columns(df)
    describe_columns(df, cols_to_analyze)

    bin_input = input("\n请输入直方图 bin 数（按回车默认50）：")
    bins = int(bin_input) if bin_input.strip() else 50

    plot_histograms(df, cols_to_analyze, bins=bins, percentage_enable=percentage_enable)
    print(f"\n分析完成，图像已保存。来源文件：{selected_csv_path}")


if __name__ == "__main__":
    main()


