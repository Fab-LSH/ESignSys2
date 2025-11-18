# 配置conda环境
```
conda create -n fdd python=3.11
pip install -r requirements.txt
conda activate fdd
```

# 测试
```
# 测试demo位于example.py文件中，file_path参数表示合同路径
python example.py --file_path ./测试合同.pdf
```