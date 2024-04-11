# Git Cheat Sheet

## Git Basics

* `git init [directory]`: 在指定的⽬录下创建⼀个空的git repo, 不带参数将在当前⽬录下创建⼀个git repo
*  `git clone [repo]`: 克隆⼀个指定repo到本地, 指定的repo可以是本地⽂件系统或者由 `HTTP` 或 `SSH` 指定的远程路径
* `git add [directory]`: 将指定⽬录的所有修改加⼊到下⼀次 `commit` 中, 可以使用 `git add .`将当前目录所有文件加入到暂存区
* `git commit -m "message"`: 将暂存区的修改提交到本地仓库, `-m` 参数后跟提交信息
* `git status`: 查看当前⽬录下 git仓库的状态, 显示哪些⽂件已被staged、未被staged以及未跟踪(untracked)
* `git log`: 查看提交历史
* `git diff`: 查看当前⽂件修改内容
* `git reset --hard HEAD^`: 回退到上⼀次提交, `HEAD^^` 表示回退到上上⼀次提交, `HEAD~100` 表示回退到前100次提交

## Git Config

* `git config --global --list`: 查看当前系统登录⽤户的所有配置
* `git config --global user.name [name]`: 配置当前⽤户名，使用 `--global`参数将针对当前系统登录⽤户⽣效
* `git config --global user.email [email]`: 配置当前⽤户邮箱，使用 `--global`参数将针对当前系统登录⽤户⽣效
* `git config --global core.editor [editor]`: 配置当前编辑器，使用 `--global`参数将针对当前系统登录⽤户⽣效
* `git config --global alias.<shortcut> [full command]`: 配置命令别名，使用 `--global`参数将针对当前系统登录⽤户⽣效
* `git config core.ignorecase false`: 配置git不忽略大小写

## Git Diff

* `git diff`: ⽐较⼯作区和暂存区的修改
* `git diff HEAD`: ⽐较⼯作区和上⼀次commit后的修改
* `git diff --cached`: ⽐较暂存区和上⼀次commit后的修改
* `git diff <commit1> <commit2>`: ⽐较两个commit之间的差异
* `git diff <commit> <file>`: ⽐较指定commit和指定file之间的差异
* `git diff <branch1> <branch2>`: ⽐较两个branch之间的差异
* `git diff <branch> <file>`: ⽐较指定branch和指定file之间的差异

## Git Reset

* `git reset`: 移除所有暂存区的修改，但不会修改⼯作区
* `git reset --hard`: 移除所有暂存区的修改，并强制删除所有⼯作区的修改
* `git reset --soft`: 移除所有暂存区的修改，但不会修改⼯作区
* `git reset [commit-id]`: 将当前分⽀回滚到指定<commit-id>, 清除暂存区的修改，但保持⼯作区状态不变 
* `git reset --hard [commit-id]`: 将当前分⽀回滚到指定<commit>, 清除暂存区的修改，并强制删除所有⼯作区的修改

## Git Branching

* `git branch [branchName]`: 创建一个名为 `branchName` 的分支
* `git checkout [branchName]`: 切换到 `branchName` 分支
* `git checkout -b [branchName]`: 创建并切换到 `branchName` 分支
* `git merge [branchName]`: 将 `branchName` 分支合并到当前分支
* `git branch -d [branchName]`: 删除 `branchName` 分支
* `git branch -D [branchName]`: 强制删除 `branchName` 分支
* `git branch`: 查看当前仓库的所有分支
* `git branch -a`: 查看当前仓库的所有分支, 包括本地和远程分支
* `git branch --merged`: 查看所有已合并到当前分支的分支
* `git branch --no-merged`: 查看所有未合并到当前分支的分支

## Git Remote Repositories

* `git remote add [remoteName] [remoteUrl]`: 添加一个名为 `remoteName` 的远程仓库, `remoteUrl` 为远程仓库的地址
* `git remote -v`: 查看所有远程仓库
* `git remote show [remoteName]`: 查看指定远程仓库的详细信息
* `git remote rm [remoteName]`: 删除远程仓库
* `git pull [remote]`: 从指定[remote]抓取所有分⽀的commit并⽴刻合并到本地repo
* `git fetch [remote] [branch]`: 从指定[remote]抓取指定[branch]的所有commit到本地repo
`git push [remote] [branch]`: 将本地指定[branch]推送到指定远程[remote], 如果远程没有对应的分⽀，将自动在远程创建此分支
* `git push [remote] --delete [branch]`: 删除远程指定[branch]
