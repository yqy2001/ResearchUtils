## 关于内存占用

查看tensor所占内存大小，`element_size()`每个元素所占字节数，`nelement()`元素个数。

```python
a = torch.zeros([128, 128])
print(a.element_size() * a.nelement())
```

int32和float32一般都占4字节，float64是8字节

## DistributedDataParallel

运行：

```shell
python -m torch.distributed.launch --nproc_per_node=n_gpus main.py
```

main.py中需要有接受local_rank的参数选项，launch会创建多个进程并给不同进程的main.py传入这个参数。每个进程的batch_size是一个GPU(一个进程)所需要的batch_size大小。

train_sampler = DistributedSampler(train_dataset)

每个训练epoch之前，要调用sampler的set_epoch方法，重置shuffle数据的种子。有了指定的sampler，Dataloader就不需要指定shuffle参数了，不然给的sampler就没有意义了。

保存加载模型/log在local_rank=0的位置进行保存。保存时要调用model.module.state_dict()

多机多卡：

在每个机器上运行语句：

```shell
python -m torch.distributed.launch --nproc_per_node=n_gpus --nnodes=2 --node_rank=0 --master_addr="主节点IP" --master_port="主节点端口" main.py
```