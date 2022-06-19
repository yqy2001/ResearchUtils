文件路径操作：

获取当前用户家目录路径：`os.environ['HOME']`或者`os.path.expanduser("~")`

判断路径是否存在：`os.path.exists("/home/")`

`os.listdir()`: 列出目录下所有文件名

`os.path.join`: 拼接

`os.getlogin()`: 获取当前登录用户名

`os.mkdirs`

直接把一个对象写入文件 / 从文件中读取

```python
import pickle

acc = [['1', '2', '3'], ['a', 'b', 'c']]
# write / dump
with open('acc_file', 'wb') as f:
    pickle.dump(f, acc)
# read / load
with open('acc_file', 'rb') as f:
    a = pickle.load(f)
# a: [['1', '2', '3'], ['a', 'b', 'c']]
```

