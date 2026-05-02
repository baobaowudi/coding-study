# 本地环境设置

本仓库使用项目本地虚拟环境 `.venv`，避免污染系统 Python。

## 已验证环境

- Python：3.12.6
- Git：2.53.0.windows.2
- VS Code：已找到
- PyCharm Community：已找到
- JupyterLab：4.5.7
- Notebook：7.5.6
- NumPy：2.4.4
- Pandas：3.0.2
- Matplotlib：3.10.9

## 启动方式

在仓库根目录执行：

```powershell
.\.venv\Scripts\Activate.ps1
python -m jupyter lab
```

如果 PowerShell 阻止激活脚本，可以直接使用：

```powershell
.\.venv\Scripts\python.exe -m jupyter lab
```

Jupyter 内核名称：

```text
Python (coding-study-ai)
```

## 重新安装依赖

如果换电脑或环境损坏：

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name coding-study-ai --display-name "Python (coding-study-ai)"
```

