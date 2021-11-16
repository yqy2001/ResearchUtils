Git

工作区就是目录，和版本库独立，只有一个工作区，但版本库里有多个版本。

暂存区：工作区和版本库之间的桥梁，每次存一点，一次commit之后全放到版本库里（HEAD后面）

版本库

名字和email放在~/.gitconfig

```shell
git config --global user.name yqy
git config --global user.email 178526723@qq.com
```

git status: 查看当前仓库的状态

git diff XX: 查看文件相比于暂存区修改了哪些内容

git restore --staged: 将文件从暂存区拿出来，但还是管理的

gti rm --cached: 不再管理

git log --pretty=oneline: 起点走到当前HEAD节点的路径

git reset --hard HEAD^: 回到某个版本

git reflog: HEAD的移动记录

git restore: 将未加入暂存区的更改删除，即回到暂存区的版本
git restore可以回滚误删的文件，回到暂存区版本

git restore --staged: 将暂存区里的文件拿出来

## 远程

git remote add origin XX: 将本地仓库关联到远程仓库

## 多分支

git checkout -b XX: 创建并切换到这个分支

git branch: 查看所有分支和当前所处分支

git checkout XX: 切换到分支

不同分支共用一个暂存区，但是commit的时候，看在哪个分支，然后提交到这个分支上。暂存区和分支完全独立 

冲突怎么办