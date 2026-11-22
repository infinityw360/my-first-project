import sys
import platform

print("你好，Codespaces！")
print("Python 版本：", platform.python_version())
print("运行路径：", sys.executable)

for i in range(1, 4):
    print(f"第 {i} 次循环")