# README
## 项目简介
本文件夹包含用于.pt文件数据压缩与处理的辅助模块，旨在数据压缩、解压缩、计算压缩率等。

## 文件结构
- `cal_compression/`
    - `README.md`：项目说明文档
    - `run.py`：实现.pt数据压缩与压缩率计算的核心模块
    - `untilities.py`：包含各类工具函数 -- 现已支持使用**_fuct包裹用try-except捕获异常
    - `EG_encoding.py`：修改自吴俊师兄的代码，使用一位 signbit 表示正负
    - `ExpGolombCode.py`：吴俊师兄的源代码
    - `ErrorLogger.py`：记录异常的工具函数



## 贡献
欢迎提交 issue 或 pull request 以改进本项目。

## 许可证
本项目遵循 MIT 许可证。
