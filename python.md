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

