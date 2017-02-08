# Git 工作流指南
工作流其实不是一个初级主体， 背后的本质问题其实是有效的项目流程管理和高效的开发协同约定， 不仅是 Git 或 SVN 等 SCM 工具的使用。

常用的工作流用法如下：

* 集中式工作流
* 功能分支工作流
* Gitflow 工作流
* Forking 工作流
* Forking 工作流
* Pull Requests

工作流有各式各样的用法， 但也正因此使得在实际工作中如何上手使用变得棘手。

!['git工作流'](./images/git_workflow.png)

## 概述
### 集中式工作流
如果熟悉 Subversion， 集中式工作流让你无需去适应一个全新流程就可以体验 Git 带来的收益。 这个工作流也可以作为向更 Git 风格工作流迁移的友好过渡。

!['集中式工作流'](./images/git-workflow-svn.png)

### 功能分支工作流
功能分支工作流以集中式工作流为基础， 不同的是为各个新功能分配一个专门的分支来开发。 这样可以在把新功能继承到正是项目前， 用 **pull Requests** 的方法讨论变更。

![](./images/git-workflow-feature_branch.png)

### Gitflow 工作流
Gitflow工作流通过为功能开发， 发布准备和维护独立的分支， 让发布迭代过程更流程。 严格的分支模型也为大型项目提供了一些非常必要的结构。

![](./images/git-workflows-gitflow.png)

### Forking 工作流
Forking 工作流是分布式工作流， 充分利用了 Git 在分支和克隆上的优势。 可以安全可靠地管理大团队的开发者 (developer)， 并能接受不信任贡献者 (contributor) 的提交。

![](./images/git-workflow-forking.png)

### Pull Requests
Pull Requests 是 **Bitbucket**提供的让开发者更方便地进行协作的功能， 提供了友好的 Web 界面可以在提议的修改合并到正式项目之前对修改进行讨论。

![](./images/pull-request.png)

## 集中式工作流
转到分布式版本控制系统看起来像个令人生畏的任务， 但不概念已用的工作流你也可以用上 Git 带来的收益。 团队可以用和 Subversion 完全不变的方式来开发项目。

但使用 Git 加强开发的工作流， Git 比 SVN 有几个优势。 首先， 每个开发者可以有属于自己的整个工程的本地拷贝。 隔离的环境让各个开发者的工作和项目的其他部分（修改）独立开来 —— 即自由地提交到自己的本地仓库， 先完全忽略上游的开发， 直到方便的时候再把修改反馈上去。

其次， Git 提供了强壮的分支和合并模型。 不像SVN，Git的分支设计成可以做为一种用来在仓库之间集成代码和分享修改的『失败安全』的机制。

### 工作方式
像Subversion一样，集中式工作流以中央仓库作为项目所有修改的单点实体。相比SVN缺省的开发分支trunk，Git叫做master，所有修改提交到这个分支上。该工作流只用到master这一个分支。

开发者开始先克隆中央仓库。在自己的项目拷贝中，像SVN一样的编辑文件和提交修改；但修改是存在本地的，和中央仓库是完全隔离的。开发者可以把和上游的同步延后到一个方便时间点。

要发布修改到正式项目中，开发者要把本地master分支的修改『推（push）』到中央仓库中。这相当于svn commit操作，但push操作会把所有还不在中央仓库的本地提交都推上去。

![](./images/git-workflow-svn-push-local.png)

### 冲突解决
中央仓库代表了正式项目，所以提交历史应该被尊重且是稳定不变的。如果开发者本地的提交历史和中央仓库有分歧，Git会拒绝push提交否则会覆盖已经在中央库的正式提交。

![](./images/git-workflow-svn-managingconflicts.png)

在开发者提交自己功能修改到中央库前，需要先fetch在中央库的新增提交，rebase自己提交到中央库提交历史之上。这样做的意思是在说，『我要把自己的修改加到别人已经完成的修改上。』最终的结果是一个完美的线性历史，就像以前的SVN的工作流中一样。

如果本地修改和上游提交有冲突，Git会暂停rebase过程，给你手动解决冲突的机会。Git解决合并冲突，用和生成提交一样的 [git status](https://www.atlassian.com/git/tutorials/setting-up-a-repository/#!status) 和 [git add](https://www.atlassian.com/git/tutorials/setting-up-a-repository/#!add) 命令，很一致方便。还有一点，如果解决冲突时遇到麻烦，Git可以很简单中止整个rebase操作，重来一次（或者让别人来帮助解决）。

### 示例
让我们一起逐步分解来看看一个常见的小团队如何用这个工作流来协作的。有两个开发者小明和小红，看他们是如何开发自己的功能并提交到中央仓库上的。

#### 有人先初始化好中央仓库
![](./images/git-workflow-svn-initialize.png)

第一步，有人在服务器上创建好中央仓库。如果是新项目，你可以初始化一个空仓库；否则你要导入已有的Git或SVN仓库。

中央仓库应该是个裸仓库（bare repository），即没有工作目录（working directory）的仓库。可以用下面的命令创建：

    ssh user@host
    git init --bare /path/to/repo.git

确保写上有效的user（SSH的用户名），host（服务器的域名或IP地址），/path/to/repo.git（你想存放仓库的位置）。注意，为了表示是一个裸仓库，按照约定加上.git扩展名到仓库名上。

#### 所有人克隆中央仓库
![](./images/git-workflow-svn-clone.png)

下一步，各个开发者创建整个项目的本地拷贝。通过 [git clone](https://www.atlassian.com/git/tutorials/setting-up-a-repository/#!clone) 命令完成：

    git clone ssh://user@host/path/to/repo.git

基于你后续会持续和克隆的仓库做交互的假设，克隆仓库时Git会自动添加远程别名 *origin* 指回『父』仓库

#### 小明开发功能
![](./images/git-workflow-svn-1.png)

在小明的本地仓库中，他使用标准的Git过程开发功能：编辑、暂存（Stage）和提交。如果你不熟悉暂存区（Staging Area），这里说明一下：**暂存区**的用来准备一个提交，但可以不用把工作目录中所有的修改内容都包含进来。这样你可以创建一个高度聚焦的提交，尽管你本地修改很多内容。

    git status # 查看本地仓库的修改状态
    git add # 暂存文件
    git commit # 提交文件

请记住，因为这些命令生成的是本地提交，小明可以按自己需求反复操作多次，而不用担心中央仓库上有了什么操作。对需要多个更简单更原子分块的大功能，这个做法是很有用的。

#### 小红开发功能
![](./images/git-workflow-svn-2.png)

与此同时，小红在自己的本地仓库中用相同的编辑、暂存和提交过程开发功能。和小明一样，她也不关心中央仓库有没有新提交；当然更不关心小明在他的本地仓库中的操作，因为所有本地仓库都是私有的。

#### 小明发布功能
![](./images/git-workflow-svn-3.png)

一旦小明完成了他的功能开发，会发布他的本地提交到中央仓库中，这样其它团队成员可以看到他的修改。他可以用下面的 [git push](https://www.atlassian.com/git/tutorial/remote-repositories#!push) 命令：

    git push origin master

注意，*origin*是在小明克隆仓库时Git创建的远程中央仓库别名。*master*参数告诉Git推送的分支。由于中央仓库自从小明克隆以来还没有被更新过，所以push操作不会有冲突，成功完成。

#### 小红试着发布功能
![](./images/git-workflow-svn-4.png)
一起来看看在小明发布修改后，小红push修改会怎么样？她使用完全一样的push命令：

一起来看看在小明发布修改后，小红push修改会怎么样？她使用完全一样的push命令：

    git push origin master

但她的本地历史已经和中央仓库有分岐了，Git拒绝操作并给出下面很长的出错消息：

>error: failed to push some refs to '/path/to/repo.git'

>hint: Updates were rejected because the tip of your current branch is behind

>hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')

>hint: before pushing again.

>hint: See the 'Note about fast-forwards' in 'git push --help' for details.

这避免了小红覆写正式的提交。她要先pull小明的更新到她的本地仓库合并上她的本地修改后，再重试。

#### 小红在小明的提交之上 rebase
![](./images/git-workflow-svn-5.png)

小红用 [git pull](https://www.atlassian.com/git/tutorials/syncing/#!pull) 合并上游的修改到自己的仓库中。这条命令类似svn update——拉取所有上游提交命令到小红的本地仓库，并尝试和她的本地修改合并：

    git pull --rebase origin master

--rebase选项告诉Git把小红的提交移到同步了中央仓库修改后的master分支的顶部，如下图所示：

![](./images/git-workflow-svn-6.png)

如果你忘加了这个选项，pull操作仍然可以完成，但每次pull操作要同步中央仓库中别人修改时，提交历史会以一个多余的『合并提交』结尾。对于集中式工作流，最好是使用rebase而不是生成一个合并提交。

#### 小红解决合并冲突
![](./images/git-workflow-svn-7.png)

rebase操作过程是把本地提交一次一个地迁移到更新了的中央仓库master分支之上。这意味着可能要解决在迁移某个提交时出现的合并冲突，而不是解决包含了所有提交的大型合并时所出现的冲突。这样的方式让你尽可能保持每个提交的聚焦和项目历史的整洁。反过来，简化了哪里引入Bug的分析，如果有必要，回滚修改也可以做到对项目影响最小。

如果小红和小明的功能是相关的，不大可能在rebase过程中有冲突。如果有，Git在合并有冲突的提交处暂停rebase过程，输出下面的信息并带上相关的指令：
>CONFLICT (content): Merge conflict in

![](./images/git-workflow-svn-8.png)

Git很赞的一点是，任何人可以解决他自己的冲突。在这个例子中，小红可以简单的运行 [git status](https://www.atlassian.com/git/tutorial/git-basics#!status) 命令来查看哪里有问题。冲突文件列在Unmerged paths（未合并路径）一节中：

>Unmerged paths:

>(use “git reset HEAD …” to unstage)

>(use “git add/rm …” as appropriate to mark resolution)

>both modified:

接着小红编辑这些文件。修改完成后，用老套路暂存这些文件，并让 [git rebase](https://www.atlassian.com/git/tutorials/rewriting-history/#!rebase)完成剩下的事：

    git add
    git rebase --continue

要做的就这些了。Git会继续一个一个地合并后面的提交，如其它的提交有冲突就重复这个过程。

如果你碰到了冲突，但发现搞不定，不要惊慌。只要执行下面这条命令，就可以回到你执行[git pull --rebase](https://www.atlassian.com/git/tutorial/remote-repositories#!pull)命令前的样子：

    git rebase --abort
    
#### 小红成功发布功能
![](./images/git-workflow-svn-9.png)

小红完成和中央仓库的同步后，就能成功发布她的修改了：

    git push origin master


## 功能分支工作流
![](./images/git-workflow-feature-branch-1.png)

一旦你玩转了**集中式工作流**，在开发过程中可以很简单地加上功能分支，用来鼓励开发者之间协作和简化交流。

功能分支工作流背后的**核心思路**是<u>*所有的功能开发应该在一个专门的分支，而不是在master分支上*</u>。这个隔离可以方便多个开发者在各自的功能上开发而不会弄乱主干代码。另外，也保证了master分支的代码一定不会是有问题的，极大有利于集成环境。

功能开发隔离也让**pull requests工作流**成为可能，pull requests工作流能为每个分支发起一个讨论，在分支合入正式项目之前，给其它开发者有表示赞同的机会。另外，如果你在功能开发中有问题卡住了，可以开一个pull requests来向同学们征求建议。这些做法的重点就是，pull requests让团队成员之间互相评论工作变成非常方便！

### 工作方式
功能分支工作流仍然用中央仓库，并且master分支还是代表了正式项目的历史。但不是直接提交本地历史到各自的本地master分支，开发者每次在开始新功能前先创建一个新分支。功能分支应该有个有描述性的名字，比如animated-menu-items或issue-#1061，这样可以让分支有个清楚且高聚焦的用途。

在master分支和功能分支之间，Git是没有技术上的区别，所以开发者可以用和集中式工作流中完全一样的方式编辑、暂存和提交修改到功能分支上。

另外，功能分支也可以（且应该）push到中央仓库中。这样不修改正式代码就可以和其它开发者分享提交的功能。由于master仅有的一个『特殊』分支，在中央仓库上存多个功能分支不会有任何问题。当然，这样做也可以很方便地备份各自的本地提交。

### Pull Requests
功能分支除了可以隔离功能的开发，也使得通过Pull Requests讨论变更成为可能。一旦某个开发完成一个功能，不是立即合并到master，而是push到中央仓库的功能分支上并发起一个Pull Request请求去合并修改到master。在修改成为主干代码前，这让其它的开发者有机会先去Review变更。

Code Review是Pull Requests的一个重要的收益，但Pull Requests目的是讨论代码一个通用方式。你可以把Pull Requests作为专门给某个分支的讨论。这意味着可以在更早的开发过程中就可以进行Code Review。比如，一个开发者开发功能需要帮助时，要做的就是发起一个Pull Request，相关的人就会自动收到通知，在相关的提交旁边能看到需要帮助解决的问题。

一旦Pull Request被接受了，发布功能要做的就和集中式工作流就很像了。首先，确定本地的master分支和上游的master分支是同步的。然后合并功能分支到本地master分支并push已经更新的本地master分支到中央仓库。

仓库管理的产品解决方案像[Bitbucket](https://bitbucket.org/)或[Stash](https://www.atlassian.com/stash)，可以良好地支持Pull Requests。可以看看Stash的[Pull Requests文档](https://confluence.atlassian.com/stash/using-pull-requests-in-stash-299570995.html)。

### 示例
下面的示例演示了如何把Pull Requests作为Code Review的方式，但注意Pull Requests可以用于很多其它的目的。

#### 小红开始开发一个新功能
![](./images/git-workflow-feature-branch-2.png)

在开始开发功能前，小红需要一个独立的分支。使用下面的命令[新建一个分支](https://www.atlassian.com/git/tutorials/using-branches/#!checkout)：

    git checkout -b marys-feature master

这个命令检出一个基于master名为marys-feature的分支，Git的-b选项表示如果分支还不存在则新建分支。这个新分支上，小红按老套路编辑、暂存和提交修改，按需要提交以实现功能：

    git status
    git add
    git commit

#### 小红要去吃个午饭
![](./images/git-workflow-feature-branch-3.png)

早上小红为新功能添加一些提交。去吃午饭前，push功能分支到中央仓库是很好的做法，这样可以方便地备份，如果和其它开发协作，也让他们可以看到小红的提交。

    git push -u origin marys-feature

这条命令push marys-feature分支到中央仓库（origin），-u选项设置本地分支去跟踪远程对应的分支。设置好跟踪的分支后，小红就可以使用git push命令省去指定推送分支的参数。

#### 小红完成功能开发
![](./images/git-workflow-feature-branch-4.png)

小红吃完午饭回来，完成整个功能的开发。[在合并到master之前](https://www.atlassian.com/git/tutorials/using-branches/#!merge)，她发起一个Pull Request让团队的其它人知道功能已经完成。但首先，她要确认中央仓库中已经有她最近的提交：

    git push

然后，在她的Git GUI客户端中发起Pull Request，请求合并marys-feature到master，团队成员会自动收到通知。Pull Request很酷的是可以在相关的提交旁边显示评注，所以你可以很对某个变更集提问。

#### 小黑收到Pull Request
![](./images/git-workflow-feature-branch-5.png)

小黑收到了Pull Request后会查看marys-feature的修改。决定在合并到正式项目前是否要做些修改，且通过Pull Request和小红来回地讨论。

#### 小红再做修改
![](./images/git-workflow-feature-branch-6.png)

要再做修改，小红用和功能第一个迭代完全一样的过程。编辑、暂存、提交并push更新到中央仓库。小红这些活动都会显示在Pull Request上，小黑可以断续做评注。

如果小黑有需要，也可以把marys-feature分支拉到本地，自己来修改，他加的提交也会一样显示在Pull Request上。

#### 小红发布她的功能
![](./images/git-workflow-feature-branch-7.png)

一旦小黑可以的接受Pull Request，就可以合并功能到稳定项目代码中（可以由小黑或是小红来做这个操作）：

    git checkout master
    git pull
    git pull origin marys-feature
    git push

无论谁来做合并，首先要检出master分支并确认是它是最新的。然后执行git pull origin marys-feature合并marys-feature分支到和已经和远程一致的本地master分支。你可以使用简单git merge marys-feature命令，但前面的命令可以保证总是最新的新功能分支。最后更新的master分支要重新push回到origin。

这个过程常常会生成一个合并提交。有些开发者喜欢有合并提交，因为它像一个新功能和原来代码基线的连通符。但如果你偏爱线性的提交历史，可以在执行合并时rebase新功能到master分支的顶部，这样生成一个快进（fast-forward）的合并。

一些GUI客户端可以只要点一下『接受』按钮执行好上面的命令来自动化Pull Request接受过程。如果你的不能这样，至少在功能合并到master分支后能自动关闭Pull Request。

#### 与此同时，小明在做和小红一样的事
当小红和小黑在marys-feature上工作并讨论她的Pull Request的时候，小明在自己的功能分支上做完全一样的事。

通过隔离功能到独立的分支上，每个人都可以自主的工作，当然必要的时候在开发者之间分享变更还是比较繁琐的。

## Gitflow 工作流
参考 [nvie](http://nvie.com/posts/a-successful-git-branching-model/) 的 Vincent Driessen

Gitflow 工作流定义了一个围绕项目发布的严格分支模型。 芮然比功能分支工作流复杂积分， 但提供了用于一个健壮的用于管理大型项目的框架。

Gitflow工作流没有用超出功能分支工作流的概念和命令，而是为不同的分支分配一个很明确的角色，并定义分支之间如何和什么时候进行交互。除了使用功能分支，在做准备、维护和记录发布也使用各自的分支。当然你可以用上功能分支工作流所有的好处：Pull Requests、隔离实验性开发和更高效的协作。

### 工作方式
Gitflow工作流仍然用中央仓库作为所有开发者的交互中心。和其它的工作流一样，开发者在本地工作并push分支到要中央仓库中。

### 历史分支

相对使用仅有的一个master分支，Gitflow工作流使用2个分支来记录项目的历史。master分支存储了正式发布的历史，而develop分支作为功能的集成分支。这样也方便master分支上的所有提交分配一个版本号。

![](./images/git-workflow-release-cycle-1historical.png)

剩下要说明的问题围绕着这2个分支的区别展开。

### 功能分支

每个新功能位于一个自己的分支，这样可以[push到中央仓库以备份和协作](https://www.atlassian.com/git/tutorials/syncing/#!push)。但功能分支不是从master分支上拉出新分支，而是使用develop分支作为父分支。当新功能完成时，[合并回develop分支](https://www.atlassian.com/git/tutorials/using-branches/#!merge)。新功能提交应该从不直接与master分支交互。

![](./images/git-workflow-release-cycle-2feature.png)

注意，从各种含义和目的上来看，功能分支加上develop分支就是功能分支工作流的用法。但Gitflow工作流没有在这里止步。

### 发布分支
![](./images/git-workflow-release-cycle-3release.png)

一旦develop分支上有了做一次发布（或者说快到了既定的发布日）的足够功能，就从develop分支上fork一个发布分支。新建的分支用于开始发布循环，所以从这个时间点开始之后新的功能不能再加到这个分支上 —— 这个分支只应该做Bug修复、文档生成和其它面向发布任务。一旦对外发布的工作都完成了，发布分支合并到master分支并分配一个版本号打好Tag。另外，这些从新建发布分支以来的做的修改要合并回develop分支。

使用一个用于发布准备的专门分支，使得一个团队可以在完善当前的发布版本的同时，另一个团队可以继续开发下个版本的功能。
这也打造定义良好的开发阶段（比如，可以很轻松地说，『这周我们要做准备发布版本4.0』，并且在仓库的目录结构中可以实际看到）。

常用的分支约定：

* 用于新建发布分支的分支: develop
* 用于合并的分支: master
* 分支命名: release-* 或 release/*

### 维护分支

![](images/git-workflow-release-cycle-4maintenance.png)

维护分支或说是热修复（hotfix）分支用于生成快速给产品发布版本（production releases）打补丁，这是唯一可以直接从master分支fork出来的分支。修复完成，修改应该马上合并回master分支和develop分支（当前的发布分支），master分支应该用新的版本号打好Tag。

为Bug修复使用专门分支，让团队可以处理掉问题而不用打断其它工作或是等待下一个发布循环。你可以把维护分支想成是一个直接在master分支上处理的临时发布。

### 示例

下面的示例演示本工作流如何用于管理单个发布循环。假设你已经创建了一个中央仓库。

#### 创建开发分支

![](images/git-workflow-release-cycle-5createdev.png)

第一步为master分支配套一个develop分支。简单来做可以[本地创建一个空的develop分支](https://www.atlassian.com/git/tutorials/using-branches/#!branch)，push到服务器上：

    git branch develop
    git push -u origin develop

以后这个分支将会包含了项目的全部历史，而master分支将只包含了部分历史。其它开发者这时应该[克隆中央仓库](https://www.atlassian.com/git/tutorials/setting-up-a-repository/#!clone)，建好develop分支的跟踪分支：

    git clone ssh://user@host/path/to/repo.git
    git checkout -b develop origin/develop

现在每个开发都有了这些历史分支的本地拷贝。

#### 小红和小明开始开发新功能

![](images/git-workflow-release-cycle-6maryjohnbeginnew.png)

这个示例中，小红和小明开始各自的功能开发。他们需要为各自的功能创建相应的分支。新分支不是基于master分支，而是应该[基于develop分支](https://www.atlassian.com/git/tutorials/using-branches/#!checkout)：

    git checkout -b some-feature develop

他们用老套路添加提交到各自功能分支上：编辑、暂存、提交：
    
    git status
    git add
    git commit

#### 小红完成功能开发

![](images/git-workflow-release-cycle-7maryfinishes.png)

添加了提交后，小红觉得她的功能OK了。如果团队使用Pull Requests，这时候可以发起一个用于合并到develop分支。否则她可以直接合并到她本地的develop分支后push到中央仓库：

    git pull origin develop
    git checkout develop
    git merge some-feature
    git push
    git branch -d some-feature

第一条命令在合并功能前确保develop分支是最新的。注意，功能决不应该直接合并到master分支。冲突解决方法和**集中式工作流**一样。

#### 小红开始准备发布

![](images/git-workflow-release-cycle-8maryprepsrelease.png)

这个时候小明正在实现他的功能，小红开始准备她的第一个项目正式发布。像功能开发一样，她用一个新的分支来做发布准备。这一步也确定了发布的版本号：

    git checkout -b release-0.1 develop

这个分支是清理发布、执行所有测试、更新文档和其它为下个发布做准备操作的地方，像是一个专门用于改善发布的功能分支。

只要小红创建这个分支并push到中央仓库，这个发布就是功能冻结的。任何不在develop分支中的新功能都推到下个发布循环中。

#### 小红完成发布
![](images/git-workflow-release-cycle-9maryfinishes.png)

一旦准备好了对外发布，小红合并修改到master分支和develop分支上，删除发布分支。合并回develop分支很重要，因为在发布分支中已经提交的更新需要在后面的新功能中也要是可用的。另外，如果小红的团队要求Code Review，这是一个发起Pull Request的理想时机。

    git checkout master
    git merge release-0.1
    git push
    git checkout develop
    git merge release-0.1
    git push
    git branch -d release-0.1

发布分支是作为功能开发（develop分支）和对外发布（master分支）间的缓冲。只要有合并到master分支，就应该打好Tag以方便跟踪。

    git tag -a 0.1 -m "Initial public release" master
    git push --tags

Git有提供各种勾子（hook），即仓库有事件发生时触发执行的脚本。可以配置一个勾子，在你push中央仓库的master分支时，自动构建好对外发布。

#### 最终用户发现Bug

![](images/git-workflow-gitflow-enduserbug.png)

对外发布后，小红回去和小明一起做下个发布的新功能开发，直到有最终用户开了一个Ticket抱怨当前版本的一个Bug。为了处理Bug，小红（或小明）从master分支上拉出了一个维护分支，提交修改以解决问题，然后直接合并回master分支：

    git checkout -b issue-#001 master

#### Fix the bug

    git checkout master
    git merge issue-#001
    git push

就像发布分支，维护分支中新加这些重要修改需要包含到develop分支中，所以小红要执行一个合并操作。然后就可以安全地删除这个分支了：

    git checkout develop
    git merge issue-#001
    git push
    git branch -d issue-#001

## Forking 工作流

Forking工作流和前面讨论的几种工作流有根本的不同。这种工作流不是使用单个服务端仓库作为『中央』代码基线，而让各个开发者都有一个服务端仓库。这意味着各个代码贡献者有2个Git仓库而不是1个：一个本地私有的，另一个服务端公开的。

Forking工作流的一个主要优势是，贡献的代码可以被集成，而不需要所有人都能push代码到仅有的中央仓库中。开发者push到自己的服务端仓库，而只有项目维护者才能push到正式仓库。这样项目维护者可以接受任何开发者的提交，但无需给他正式代码库的写权限。

效果就是一个分布式的工作流，能为大型、自发性的团队（包括了不受信的第三方）提供灵活的方式来安全的协作。也让这个工作流成为开源项目的理想工作流。

### 工作方式

和其它的Git工作流一样，Forking工作流要先有一个公开的正式仓库存储在服务器上。但一个新的开发者想要在项目上工作时，不是直接从正式仓库克隆，而是fork正式项目在服务器上创建一个拷贝。

这个仓库拷贝作为他个人公开仓库 —— 其它开发者不允许push到这个仓库，但可以pull到修改（后面我们很快就会看这点很重要）。在创建了自己服务端拷贝之后，和之前的工作流一样，开发者执行[git clone命令](https://www.atlassian.com/git/tutorials/setting-up-a-repository/#!clone)克隆仓库到本地机器上，作为私有的开发环境。

要提交本地修改时，push提交到自己公开仓库中 —— 而不是正式仓库中。然后，给正式仓库发起一个pull request，让项目维护者知道有更新已经准备好可以集成了。对于贡献的代码，pull request也可以很方便地作为一个讨论的地方。

为了集成功能到正式代码库，维护者pull贡献者的变更到自己的本地仓库中，检查变更以确保不会让项目出错，[合并变更到自己本地的master分支](https://www.atlassian.com/git/tutorial/git-branches#!merge)，然后[push](https://www.atlassian.com/git/tutorials/syncing/#!push) master分支到服务器的正式仓库中。到此，贡献的提交成为了项目的一部分，其它的开发者应该执行pull操作与正式仓库同步自己本地仓库。

### 正式仓库

在Forking工作流中，『官方』仓库的叫法只是一个约定，理解这点很重要。从技术上来看，各个开发者仓库和正式仓库在Git看来没有任何区别。事实上，让正式仓库之所以正式的唯一原因是它是项目维护者的公开仓库。

### Forking工作流的分支使用方式

所有的个人公开仓库实际上只是为了方便和其它的开发者共享分支。各个开发者应该用分支隔离各个功能，就像在**功能分支工作流**和**Gitflow工作流**一样。唯一的区别是这些分支被共享了。在Forking工作流中这些分支会被pull到另一个开发者的本地仓库中，而在功能分支工作流和Gitflow工作流中是直接被push到正式仓库中。

### 示例

#### 项目维护者初始化正式仓库

![](images/git-workflows-forking-1.png)

和任何使用Git项目一样，第一步是创建在服务器上一个正式仓库，让所有团队成员都可以访问到。通常这个仓库也会作为项目维护者的公开仓库。

[公开仓库应该是裸仓库](https://www.atlassian.com/git/tutorial/git-basics#!init)，不管是不是正式代码库。所以项目维护者会运行像下面的命令来搭建正式仓库：

    ssh user@host
    git init --bare /path/to/repo.git

Bitbucket和Stash提供了一个方便的GUI客户端以完成上面命令行做的事。这个搭建中央仓库的过程和前面提到的工作流完全一样。如果有现存的代码库，维护者也要push到这个仓库中。

#### 开发者fork正式仓库

![](images/git-workflows-forking-2.png)

其它所有的开发需要fork正式仓库。可以用git clone命令用[SSH协议连通到服务器](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-git-728138079.html)，拷贝仓库到服务器另一个位置 —— 是的，fork操作基本上就只是一个服务端的克隆。Bitbucket和Stash上可以点一下按钮就让开发者完成仓库的fork操作。

这一步完成后，每个开发都在服务端有一个自己的仓库。和正式仓库一样，这些仓库应该是裸仓库。

#### 开发者克隆自己fork出来的仓库

![](images/git-workflows-forking-3.png)

下一步，各个开发者要克隆自己的公开仓库，用熟悉的git clone命令。

在这个示例中，假定用Bitbucket托管了仓库。记住，如果这样的话各个开发者需要有各自的Bitbucket账号，使用下面命令克隆服务端自己的仓库：

    git clone https://user@bitbucket.org/user/repo.git

相比前面介绍的工作流只用了一个origin远程别名指向中央仓库，Forking工作流需要2个远程别名 —— 一个指向正式仓库，另一个指向开发者自己的服务端仓库。别名的名字可以任意命名，常见的约定是使用origin作为远程克隆的仓库的别名（这个别名会在运行git clone自动创建），upstream（上游）作为正式仓库的别名。

    git remote add upstream https://bitbucket.org/maintainer/repo

需要自己用上面的命令创建upstream别名。这样可以简单地保持本地仓库和正式仓库的同步更新。注意，如果上游仓库需要认证（比如不是开源的），你需要提供用户：

    git remote add upstream https://user@bitbucket.org/maintainer/repo.git

这时在克隆和pull正式仓库时，需要提供用户的密码。

#### 开发者开发自己的功能

![](images/git-workflows-forking-4.png)

在刚克隆的本地仓库中，开发者可以像其它工作流一样的编辑代码、[提交修改](https://www.atlassian.com/git/tutorial/git-basics#!commit)和[新建分支](https://www.atlassian.com/git/tutorials/using-branches/#!branch)：

    git checkout -b some-feature
    // Edit some code
    git commit -a -m "Add first draft of some feature"

所有的修改都是私有的直到push到自己公开仓库中。如果正式项目已经往前走了，可以用[git pull](https://www.atlassian.com/git/tutorials/syncing/#!pull)命令获得新的提交：

    git pull upstream master

由于开发者应该都在专门的功能分支上工作，pull操作结果会都是[快速合并](https://www.atlassian.com/git/tutorials/using-branches/#!merge)。

#### 开发者发布自己的功能

![](images/git-workflows-forking-5.png)

一旦开发者准备好了分享新功能，需要做二件事。首先，通过push他的贡献代码到自己的公开仓库中，让其它的开发者都可以访问到。他的origin远程别名应该已经有了，所以要做的就是：

    git push origin feature-branch

这里和之前的工作流的差异是，origin远程别名指向开发者自己的服务端仓库，而不是正式仓库。

第二件事，开发者要通知项目维护者，想要合并他的新功能到正式库中。Bitbucket和Stash提供了[Pull Request](https://confluence.atlassian.com/display/STASH/Using+pull+requests+in+Stash)按钮，弹出表单让你指定哪个分支要合并到正式仓库。一般你会想集成你的功能分支到上游远程仓库的master分支中。

#### 项目维护者集成开发者的功能

![](images/git-workflows-forking-6.png)

当项目维护者收到pull request，他要做的是决定是否集成它到正式代码库中。有二种方式来做：

* 直接在pull request中查看代码
* pull代码到他自己的本地仓库，再手动合并

第一种做法更简单，维护者可以在GUI中查看变更的差异，做评注和执行合并。但如果出现了合并冲突，需要第二种做法来解决。这种情况下，维护者需要从开发者的服务端仓库中[fetch](https://www.atlassian.com/git/tutorials/syncing/#!fetch)功能分支，合并到他本地的master分支，解决冲突：

    git fetch https://bitbucket.org/user/repo feature-branch
    // 查看变更
    git checkout master
    git merge FETCH_HEAD

变更集成到本地的master分支后，维护者要push变更到服务器上的正式仓库，这样其它的开发者都能访问到：

    git push origin master

注意，维护者的origin是指向他自己公开仓库的，即是项目的正式代码库。到此，开发者的贡献完全集成到了项目中。


#### 开发者和正式仓库做同步

![](images/git-workflows-forking-7.png)

由于正式代码库往前走了，其它的开发需要和正式仓库做同步：

    git pull upstream master

## Pull Requests

Pull Requests是Bitbucket上方便开发者之间协作的功能。提供了一个用户友好的Web界面，在集成提交的变更到正式项目前可以对变更进行讨论。

![](images/pull-request-bitbucket.png)

开发者向团队成员通知功能开发已经完成，Pull Requests是最简单的用法。开发者完成功能开发后，通过Bitbucket账号发起一个Pull Request。这样让涉及这个功能的所有人知道，要去做Code Review和合并到master分支。

但是，Pull Request远不止一个简单的通知，而是为讨论提交的功能的一个专门论坛。如果变更有任何问题，团队成员反馈在Pull Request中，甚至push新的提交微调功能。所有的这些活动都直接跟踪在Pull Request中。

相比其它的协作模型，这种分享提交的形式有助于打造一个更流畅的工作流。SVN和Git都能通过一个简单的脚本收到通知邮件；但是，讨论变更时，开发者通常只能去回复邮件。这样做会变得杂乱，尤其还要涉及后面的几个提交时。Pull Requests把所有相关功能整合到一个和Bitbucket仓库界面集成的用户友好Web界面中。

### 解析Pull Request

当要发起一个Pull Request，你所要做的就是请求（Request）另一个开发者（比如项目的维护者），来pull你仓库中一个分支到他的仓库中。这意味着你要提供4个信息（源仓库、源分支、目的仓库、目的分支），以发起Pull Request。

![](images/pull-request-anatomy.png)

这些值多数Bitbucket都会设置上合适的缺省值。但取决你用的协作工作流，你的团队可能会要指定不同的值。上图显示了一个Pull Request请求合并一个功能分支到正式的master分支上，但可以有多种不同的Pull Request用法。

### 工作方式

Pull Request可以和**功能分支工作流**、**Gitflow工作流**或**Forking工作流**一起使用。但Pull Request要求要么分支不同，要么仓库不同，所以不能用于**集中式工作流**。在不同的工作流中使用Pull Request会有一些不同，但基本的过程是这样的：

1. 开发者在本地仓库中新建一个专门的分支开发功能。
2. 开发者push分支修改到公开的Bitbucket仓库中。
3. 开发者通过Bitbucket发起一个Pull Request。
4. 团队的其它成员review code，讨论并修改。
5. 项目维护者合并功能到官方仓库中并关闭Pull Request。

本文后面内容说明，Pull Request在不同协作工作流中如何应用。

在功能分支工作流中使用Pull Request

功能分支工作流用一个共享的Bitbucket仓库来管理协作，开发者在专门的分支上开发功能。但不是立即合并到master分支上，而是在合并到主代码库之前开发者应该开一个Pull Request发起功能的讨论。

![](images/pull-request-feature-branch.png)

功能分支工作流只有一个公开的仓库，所以Pull Request的目的仓库和源仓库总是同一个。通常开发者会指定他的功能分支作为源分支，master分支作为目的分支。

收到Pull Request后，项目维护者要决定如何做。如果功能没问题，就简单地合并到master分支，关闭Pull Request。但如果提交的变更有问题，他可以在Pull Request中反馈。之后新加的提交也会评论之后接着显示出来。

在功能还没有完全开发完的时候，也可能发起一个Pull Request。比如开发者在实现某个需求时碰到了麻烦，他可以发一个包含正在进行中工作的Pull Request。其它的开发者可以在Pull Request提供建议，或者甚至直接添加提交来解决问题。

### 在Gitflow工作流中使用Pull Request

Gitflow工作流和功能分支工作流类似，但围绕项目发布定义一个严格的分支模型。在Gitflow工作流中使用Pull Request让开发者在发布分支或是维护分支上工作时，可以有个方便的地方对关于发布分支或是维护分支的问题进行交流。

![](images/gitflow-workflow-pull-request.png)

Gitflow工作流中Pull Request的使用过程和上一节中完全一致：当一个功能、发布或是热修复分支需要Review时，开发者简单发起一个Pull Request，团队的其它成员会通过Bitbucket收到通知。

新功能一般合并到develop分支，而发布和热修复则要同时合并到develop分支和master分支上。Pull Request可能用做所有合并的正式管理。

### 在Forking工作流中使用Pull Request

在Forking工作流中，开发者push完成的功能到他自己的仓库中，而不是共享仓库。然后，他发起一个Pull Request，让项目维护者知道他的功能已经可以Review了。

在这个工作流，Pull Request的通知功能非常有用，因为项目维护者不可能知道其它开发者在他们自己的仓库添加了提交。

![](images/pull-request-forking-workflow-1.png)

由于各个开发有自己的公开仓库，Pull Request的源仓库和目标仓库不是同一个。源仓库是开发者的公开仓库，源分支是包含了修改的分支。如果开发者要合并修改到正式代码库中，那么目标仓库是正式仓库，目标分支是master分支。

Pull Request也可以用于正式项目之外的其它开发者之间的协作。比如，如果一个开发者和一个团队成员一起开发一个功能，他们可以发起一个Pull Request，用团队成员的Bitbucket仓库作为目标，而不是正式项目的仓库。然后使用相同的功能分支作为源和目标分支。

![](images/pull-request-forking-workflow-2.png)

2个开发者之间可以在Pull Request中讨论和开发功能。完成开发后，他们可以发起另一个Pull Request，请求合并功能到正式的master分支。在Forking工作流中，这样的灵活性让Pull Request成为一个强有力的协作工具。

### 示例

下面的示例演示了Pull Request如何在在Forking工作流中使用。也同样适用于小团队的开发协作和第三方开发者向开源项目的贡献。

在示例中，小红是个开发，小明是项目维护者。他们各自有一个公开的Bitbucket仓库，而小明的仓库包含了正式工程。

#### 小红fork正式项目

![](images/pull-request-1.png)

小红先要fork小明的Bitbucket仓库，开始项目的开发。她登陆Bitbucket，浏览到小明的仓库页面，
点Fork按钮。

![](images/pull-request-2.png)

然后为fork出来的仓库填写名字和描述，这样小红就有了服务端的项目拷贝了。

#### 小红克隆她的Bitbucket仓库

![](images/pull-request-3.png)

下一步，小红克隆自己刚才fork出来的Bitbucket仓库，以在本机上准备出工作拷贝。命令如下：

    git clone https://user@bitbucket.org/user/repo.git

请记住，git clone会自动创建origin远程别名，是指向小红fork出来的仓库。

#### 小红开发新功能

![](images/pull-request-4.png)

在开始改代码前，小红要为新功能先新建一个新分支。她会用这个分支作为Pull Request的源分支。

    git checkout -b some-feature

#### 编辑代码

    git commit -a -m “Add first draft of some feature”

在新功能分支上，小红按需要添加提交。甚至如果小红觉得功能分支上的提交历史太乱了，她可以用[交互式rebase](https://www.atlassian.com/git/tutorials/rewriting-history/#!rebase-i)来删除或压制提交。对于大型项目，整理功能分支的历史可以让项目维护者更容易看出在Pull Request中做了什么内容。

#### 小红push功能到她的Bitbucket仓库中

![](images/pull-request-5.png)

小红完成了功能后，push功能到她自己的Bitbucket仓库中（不是正式仓库），用下面简单的命令：

    git push origin some-branch

这时她的变更可以让项目维护者看到了（或者任何想要看的协作者）。

#### 小红发起Pull Request

![](images/example-6.png)

Bitbucket上有了她的功能分支后，小红可以用她的Bitbucket账号浏览到她的fork出来的仓库页面，点右上角的【Pull Request】按钮，发起一个Pull Request。弹出的表单自动设置小红的仓库为源仓库，询问小红以指定源分支、目标仓库和目标分支。

小红想要合并功能到正式仓库，所以源分支是她的功能分支，目标仓库是小明的公开仓库，而目标分支是master分支。另外，小红需要提供Pull Request的标题和描述信息。如果需要小明以外的人审核批准代码，她可以把这些人填在【Reviewers】文本框中。

![](images/pull-request-7.png)

创建好了Pull Request，通知会通过Bitbucket系统消息或邮件（可选）发给小明。

#### 小明review Pull Request

![](images/pull-request-8.png)

在小明的Bitbucket仓库页面的【Pull Request】Tab可以看到所有人发起的Pull Request。点击小红的Pull Request会显示出Pull Request的描述、功能的提交历史和每个变更的差异（diff）。

如果小明想要合并到项目中，只要点一下【Merge】按钮，就可以同意Pull Request并合并到master分支。

但如果像这个示例中一样小明发现了在小红的代码中的一个小Bug，要小红在合并前修复。小明可以在整个Pull Request上加上评注，或是选择历史中的某个提交加上评注。

![](images/pull-request-9.png)

#### 小红补加提交

如果小红对反馈有任何疑问，可以在Pull Request中响应，把Pull Request当作是她功能讨论的论坛。

小红在她的功能分支新加提交以解决代码问题，并push到她的Bitbucket仓库中，就像前一轮中的做法一样。这些提交会进入的Pull Request，小明在原来的评注旁边可以再次review变更。

#### 小明接受Pull Request

最终，小明接受变更，合并功能分支到master分支，并关闭Pull Request。至此，功能集成到项目中，其它的项目开发者可以用标准的git pull命令pull这些变更到自己的本地仓库中。
