[TOC]

# Chinahadoop Course Abstract

## 大数据之 Linux 实战

- 步入 Linux
  - Linux 简要介绍
  - Linux 各个 distribution 选择
  - Linux 磁盘分区选择
  - Linux 目录结构
  - 实践1 CentOS 安装
  - 实践2 Linux 基本命令实验
- 一切皆文件
  - Linux 用户和组概念
  - Linux 文件属性及权限
  - Linux 文件与目录 CRUD
  - 实践1 创建文件及目录并修改权限
  - 实践2 对文件和目录的操作
  - 实践3 创建 Hadoop 用户及 Hadoop 组等
- 文件系统
  - 磁盘物理简要介绍
  - Linux 文件系统原理
  - Ext2/Ext3/Ext4 及 swap 介绍
  - 挂载点
  - 文件系统的操作
  - 实践 df， du 实际用法
- Shell 的世界
  - 认识 Vim 及熟悉 Vim
  - 常见 shell 命令学习
- Shell 脚本
  - shell script 介绍
  - hello shell 练习
  - 判断符号
  - 条件判断语句
  - 循环语句
  - 传递参数
  - 实践1 检查磁盘空间脚本练习
  - 实践2 分析一个 Hadoop 脚本 (Shell 源码)
- 进程介绍
  - 进程简介
  - 进程的查看
  - 进程的管理
  - 进程的执行顺序
  - 进程资源占用监控
  - 任务管理
  - 实践1 查看进程及资源使用情况
  - 实践2 设置后台运行 job
- Linux 软件包管理
  - tarball 安装
  - rpm 安装方式操作
  - yum 安装方式操作
  - Linux 压缩命令
  - 实践1 tarsal 安装实践
  - 实践2 rpm 安装实践
  - 实践3 yum 安装实践
- Linux 网络详解
  - 网络基本常识
  - 网络参数常用命令
  - 网络通信
  - 网络下载

## 大数据之 JAVA 编程

- Java 入门
  - Java 概述
  - Java 代码初运行
  - 环境搭建及 Java 编译过程
  - 基本数据类型
  - 变量和常量
  - 修饰符与运算符
  - 初始面向对象
  - 对象和类
- Java 基础
  - 程序流程控制
  - 认识字符串
  - 必须了解的常用类
  - 数组
  - 方法
  - 流、 文件及 IO 初步
  - 样例： Hadoop 中的一些 Java 应用
- 深入面向对象
  - 面向对象的 『世界观』
  - 封装
  - 继承
  - 覆盖于重载
  - 多态
  - 抽象类
  - 接口
  - 包 (package)
  - 样例， Hadoop Datanode
- 数据结构、 集合与泛型
  - 常见数据结构
  - 集合框架及使用
  - Java 泛型
  - 集合与泛型在实际项目中的使用样例
- 序列化与 Java IO
  - Java 序列化
  - JavaIO 基本架构
  - JavaIO 磁盘IO
  - JavaIO  Socket
  - JavaIO  NIO
  - 样例， Hadoop Mapper 中疏忽序列化
- 多线程与并发
  - 线程创建与控制
  - 线程同步互斥与通信
  - 并发包
- Java 虚拟机
  - JVM 的基本架构
  - 类加载器
  - 运行数据区及执行引擎
  - Java GC
  - Java 工具介绍及应用
  - 实例， 用 Java 工具观测进程状态
- Java 反射
  - 介绍反射
  - Class 类
  - 反射 API
  - 反射机制的使用及示例
  - 样例， Hadoop 中的反射应用
- Java 项目管理
  - Maven 环境搭建
  - Maven 构建项目
  - Maven 依赖管理
  - Maven 常用命令
- 最有影响力的 Java 开源项目 —— Hadoop
  - Hadoop 生态系统特点
  - Hadoop 介绍
  - Hadoop 生态系统
  - Hadoop 生态系统版本衍化

## 大数据之 Scala 编程

- Scala 基础
  - 值与变量的声明
  - 常用类型简介
  - 函数与方法的定义与使用
  - 条件表达式
  - 循环及高级 for 循环使用
  - lazy 值
  - 默认参数、 带名参数及边长参数
  - 异常处理
  - 数组相关操作
  - Map 操作
- Scala 面向对象编程
  - 类定义
  - 类的属性
  - 主构造器
  - 辅助构造器
  - object 对象
  - apply 方法
  - 类的继承
  - 方法重写与字段重写
  - 抽象类
  - trait
  - 包的定义与使用
  - 包对象定义与使用
  - 文件访问
- Sca 函数式编程
  - 高阶函数的定义
  - 值函数
  - 匿名函数
  - 闭包
  - SAM 与 Curry
  - 高阶函数示例
  - 集合简介
  - 序列
  - 可变列表与不可变列表
  - 集合操作
  - case class
  - 模式匹配
- Scala 高级编程
  - 泛型类
  - 泛型函数
  - Lower bounds 与 Upper bounds
  - View bounds
  - Context bounds
  - 协变与逆变
  - 隐式转换
  - 隐式参数
  - 隐式类

## R 语言机器学习

- 机器学习基础

  - 监督与非监督学习
  - 最优化求解算法（包含梯度下降、 牛顿法、 SGD 等）
  - 过拟合问题及优化

- R 语言基础

  - 数据框及列表
  - 矩阵及向量化计算
  - 数据处理基础（包含 plyr/reshape/data.table 等包的介绍）

- 聚类算法剖析

  - kMeans 聚类剖析
  - 系统聚类算法
    - 基础距离及类间距离
    - 系统聚类的手动演算案例
  - 最佳聚类数目的确定
  - 分类变量用于聚类的问题

- 关联算法剖析

  - Apriori 算法
    - 基本原理
    - Apriori 算法的手动演算案例
  - Eclat 算法
    - 基本原理
    - Eclat 算法的手动演算案例
  - SPADE 算法
    - 基本原理
    - SPADE 算法的手动演算案例

- 随机森林剖析

  - 随机森林算法的构建过程
    - 随机抽样生成独立样本
    - 变量的重要性衡量
    - 基于 R 语言计算各变量的重要性指标
    - 基于决策树模拟随机森林的实现
  - 基于 R 语言实现并行的随机森林

- 神经网络剖析

  - BP 神经网络
    - 算法原理
    - 基于 R 语言手动实现 BP 神经网络

  - RBF 神经网络
    - 算法原理
    - 基于 R 语言手动实现 RBF 神经网络
  - Elman 神经网络
    - 算法原理
    - 基于 R 语言手动实现 Elman 神经网络

- 特征自动生成技术

  - 遗传算法简介
  - 遗传编程简介
  - 基于遗传编程的特征自动生成
    - 基本思路
    - 特征表达式
    - 产生初始种群
    - 计算适应度
    - 选择、 交叉、 变异
    - 实例分析

- R 语言并行计算

  - R 语言常见并行包介绍
    - multicore
    - snow
    - snowfall
    - doParallel
    - doSNOW
    - parallel
    - RHadoop
  - SupR 并行计算
    - SupR 简介
    - SupR 的环境安装
    - SupR 的使用案例

- 精品案例： 短期日负荷曲线预测

  - 电力行业负荷预测介绍
  - 数据准备及说明
  - 基于 RBF 神经网络的预测
  - 基于遗产编程的预测

## Spark —— 原理、 内幕与案例实践

hulu 大数据

- 《Hadoop技术内幕：深入解析MapReduce架构设计与实现原理》
- 《Hadoop技术内幕：深入解析YARN架构设计与实现原理》

### 课程大纲

- Spark 概述
  - Spark 产生背景
    - Map Reduce 缺陷
    - 多计算框架并行
    - 其他
  - Spark 基本特点
  - Spark 版本yanhua
  - Spark 核心概念
    - RDD
    - transformation
    - action
    - cache
    - 其他
  - Spark 生态系统
    - Spark 生态系统构成
    - 与Hadoop 生态系统的关系
  - Spark 在互联网公司中的地位与应用
    - 当前互联网公司的 Spark 应用案例
  - 本课程与 Spark 2.0 的关系
  - Spark 集群搭建
    - 测试集群搭建和生产环境中集群搭建方法
    - 亲手演示整个过程
- Spark Core
  - Spark 程序设计与实战
    - Spark 运行模式介绍。 Spark 运行组件构成， Spark 运行模式(local， standalone， mesos/yarn 等)
    - Spark 开发环境构建。 集成开发环境选择， 亲手演示 Spark 程序开发与调试， Spark 运行
    - 常见 transformation 与 action 用法。 介绍常见 transformation 与 action 使用方法， 以及代码片段剖析
    - 常见控制函数介绍。 包括 cache、 broadcast、 accumulator 等
    - 在线演示： 简易电影受众分析系统。 
      - 背景介绍
      - 数据导入
      - 数据分析
      - 常见 Spark transformation 和 action 用法在线演示
  - Spark 内部原理剖析与源码阅读
    - Spark 运行模式剖析。 深入分析 Spark 运行模式， 包括 local， standalone 以及 Spark on yarn
    - Spark 运行流程剖析。 包括 Spark 逻辑查询计划， 物理查询计划以及分布式执行
    - Spark shuffle 剖析。 深入介绍 Spark shuffle 的实现， 主要介绍 hash-based 和 sort-based 两种实现
    - Spark 源码阅读。 Spark 源码构成以及阅读方式
  - Spark 程序调优
    - 数据存储格式调优。 数据存储格式选择， 数据压缩算法选择等。
    - 资源调优。 如何设置合理的 executor， cpu 和内存数目
    - 程序参数调优。 介绍常见的调优参数
    - 程序实现调优。 如何选择最合适的 transformation 与 action 函数
- Spark SQL 2.0
  - Spark SQL 基本原理
    - Spark SQL 是什么
    - Spark SQL  基本原理
    - Spark Dataframe 与 DataSets
    - Spark SQL  与 Spark Core 的关系
  - Spark SQL 程序设计与应用案例
    - Spark SQL 程序设计
      - 如何访问 MySQL、 HDFS 等数据源
      - 如何处理 parquet 格式数据
      - 常用的 DSL 语法及其使用
    - Spark SQL 应用案例： 篮球运动员评估系统
      - 北京介绍
      - 数据导入
      - 数据分析
      - 结论
- Spark Streaming
  - Spark Streaming 基本原理
    - Spark Streaming 是什么
    - Spark Streaming 基本原理
    - Structured Streaming
    - Spark Streaming 编程接口介绍
    - Spark Streaming 应用案例
  - Spark Streaming 程序设计
    - 常见流式数据处理模式
    - Spark Streaming 与 Kafka 交互
    - Spark Streaming 与 Redis 交互
    - Spark Streaming 部署与运行
- Spark MLlib
  - Spark MLlib 简介
  - 数据表示方式
  - MLlib 中的聚类、 分类和推荐算法
  - 如何使用 MLlib 的算法
  - MLlib 2.0 时间
- Spark 综合案例： 简易电影推荐系统
  - 背景介绍
  - 什么是 Lambda Architecture
  - 利用 HDFS + Spark Core + MLlib + Redis 构建批处理线
  - 利用 Kafka + Spark Streaming + Redis 构建实时处理线
  - 整合批处理线和实时处理线

## Hive 2.1 高级特性

- Hive 架构和基本原理
- 语法分析器和语义分析器
- 序列化器与反序列化器
- 各种不同类型的算子及优化
- 内置函数及自定义函数的原理
- 不同的执行引擎 MapReduce 和 Tez
- LLAP(Long Live And Process)
- HiveServer 2
- ACID 及存储过程的原理
- 各种查询优化器

## Python 数据分析

### 课程目标

- 熟悉数据分析的流程， 包括数据采集、 处理、 可视化等
- 掌握 Python 语言作为数据分析工具， 从而有能力驾驭不同领域的数据分析时间
- 快速掌握多个业务领域的数据分析项目经验
- 掌握使用 Python 实现基于机器学习的数据分析和预测

### 课程大纲

- 工作环境准备及 Python 数据结构讲解
  - 课程介绍
  - 工作环境准备
  - Python 语言基础回顾
  - Python 数据结构讲解
    - 列表
    - 字典
    - 元组
    - 集合
  - Python高级特性
    - 切片
    - 迭代
  - Python 高阶函数
    - map
    - filter
    - reduce
- 科学计算及数据可视化入门
  - 使用 NumPy 和 SciPy 进行科学计算
  - Matplotlib 绘图入门
  - 实战案例： 2016 美国总统大选数据分析 (2016 Election Polls)
- 本地数据的采集与操作
  - 常用格式的本地数据读写
  - SQL 常用语法讲解
  - Python 的数据库基本操作
  - 数据库多表连接用法详解
    - left join
    - right  join
    - inner join
    - full join
  - 实战案例： 欧洲职业足球数据库分析 (European Soccer Database)
- 网络数据的获取与表示
  - BeautifulSoup 解析网页
  - 爬虫框架 Scrapy 基础
  - 实战案例： 获取电商网站的商品信息
- 数据分析工具 Pandas 基础
  - Pandas 的数据结构
    - Series
    - DataFrame
  - Pandas 的数据操作
    - 数据的导入、 导出
    - 数据的过滤筛选
    - 索引及多重索引
  - Pandas 统计计算和描述
  - Pandas 的绘图函数
  - 实战案例： 星际争霸II重放分析 (StarCraft II Replay Analysis)
- 数据分析工具 Pandas 进阶
  - 数据的分组与聚合
  - 数据的分组运算
  - Pandas 透视表和交叉表
  - 实战案例： 互联网电影资料库分析 (IMDB 5000 Movie Dataset)
- 数据的规整与可视化
  - 数据清洗、 合并、 转化和重构
  - 常用的 Python 数据可视化工具
    - Matplotlib 回顾及扩充
    - Seaborn 绘图
    - 交互式数据可视化 —— Bokeh 绘图
  - 实战案例： 空难历史数据分析 (Airplane Crashes Since 1908)
- 机器学习基础及机器学习库 scikit-learn 入门
  - 机器学习基础
  - scikit-learn 入门
  - 实战案例： 利用声音数据进行性别识别 (Gender Recognition by Voice)
- 项目实战： 『闪电约会』配对预测
  - 项目介绍 (Speed Dating Experiment)
  - 数据分析与处理
  - 模型选择及训练
  - 课程总结


## Hadoop

### 基础要求

- 了解 Linux 基础知识
- 掌握 Java 语言基础

### 目标人群

- 大数据爱好者
- Hadoop 初中级学者， 希望系统性学习 Hadoop 的人

### 课程大纲

- Hadoop 概述
  - 大数据背景
  - 大数据技术体系
  - Hadoop 生态系统构成以及核心组件
  - Hadoop 主流发行版以及选型， 包括 Apache， CDH， HDP 等
  - Hadoop 单机及分布式集群搭建方法
  - Hadoop 典型应用场景， 包括日志分析， 搜索引擎索引构建、 机器学习等
  - 课程综合案例： 分布式日志分析系统。 介绍分布式日志分析系统的背景、 关键模块以及采用的关键大数据技术
- 大数据技术体系关键组件原理、 使用与实战
  - 分布式数据收集： Flume 原理与应用
    - Flume 产生背景
    - Flume 基本原理及架构
    - Flume 部署模式
    - Flume 与 Hadoop 整合与实战
    - 分布式日志分析系统： 数据收集模块剖析。 详细介绍基于 TailDir 和 Pool Directory Source， File Channel 以及 HDFS sink 收集日志的 Flume 拓扑构建方式
  - 分布式文件系统： HDFS 基础与应用
    - HDFS 产生背景
    - HDFS 基本原理
    - HDFS 架构以及关键组件
    - HDFS 使用方式
    - HDFS 优化小技巧
    - 分布式日志分析系统： 文件存储模块剖析。 详细介绍日志文件在 HDFS 存放方式， 以及如何解决小文件， 文件归档等问题
  - 分布式资源管理系统： YARN 架构与应用
    - YARN 产生背景
    - YARN 基本原理以及架构
    - YARN 资源调度器（Capacity Scheduler 以及 Fair Scheduler）
    - YARN 基于标签的调度策略以及启动方式
    - YARN 典型应用场景及在大数据系统中的地位
    - 分布式日志分析系统： 资源管理模块剖析。 详细介绍容量调度器， 多队列管理， 如果启用基于标签的调度机制
  - 分布式计算： 批处理引擎 MapReduce
    - MapReduce 产生背景
    - MapReduce 基本原理
    - MapReduce 基本架构
    - MapReduce Java 分布式程序设计
    - 什么情况下 Spark 性能比 MapReduce 差
    - MapReduce 的未来
  - 分布式计算： 批处理引擎 MapReduce
    - MapReduce 回顾
    - MapReduce 多语言程序设计
    - MapReduce 优化小技巧
    - 分布式日志分析系统： ETL 模块剖析。 详细介绍如何使用 Java API 以及 Hadoop Streaming 方式设计 ELT 程序
  - 分布式计算： 数据分析引擎 Hive
    - Hive 产生背景
    - Hive 基本架构以及部署模式
    - Hive HQL 基础
    - Hive 创建 Parquet 与 ORC 表
    - 总结
  - 分布式计算： 数据分析引擎 Hive
    - Hive 编程访问
    - Hive On Tez/Spark
    - Hive 优化小技巧
    - 分布式日志分析系统： 数据仓库模块剖析。 详细介绍如何在 Hive 中进行数据建模， 并使用 Hive 查询引擎查询日志数据
  - 分布式计算： 数据查询引擎 Presto
    - Presto 产生背景
    - Presto 基本架构以及魔术模式
    - Presto SQL 基础
    - Presto 优化小技巧
    - 分布式日志分析系统： 数据仓库查询模块剖析。 详细介绍如何使用 Presto 加速数据查询效率（相比于 Hive）
  - 大数据可视化： 可视化主流方案
    - 什么是大数据可视化
    - 可视化主流解决方案
    - EChart， D3， tableau， Hue 等
    - 分布式日志分析系统： 报表可视化模块剖析。 详细介绍如何构建日志分析系统的可视化模块
- 综合案例回顾： 分布式日志分析系统
  - 案例背景
  - 基本架构与关键模块
  - 日志分析系统部署及维护
  - 总结

## **统计建模实战**

- 简介
  - 数据的类型
  - 数据的来源
  - 数据的展示
  - 数据的概括性度量
- 列联分析
  - 问题： 泰坦尼克号的死亡记录
  - 列联表的构造
  - 拟合优度检验
  - 独立性实验
  - 案例分析： 家庭状况与青少年犯罪的关系研究
  - 列联分析的项目演练
- 方差分析
  - 问题： 新药的临床试验
  - 方差分析的引论
  - 单因素方差分析
  - 多因素方差分析
  - 案例分析： 广告媒体和广告方案对营销额的影响研究
  - 方差分析的项目演练
- 回归分析
  - 问题： 父代和子代的关系
  - 变量间关系的度量
  - 一元线性回归
  - 多元线性回归
  - 案例分析： 研究我国民航客运量的变化趋势及其成因
  - 回归分析的项目演练
- 聚类分析
  - 问题： 欧洲各国语言的相似性
  - 相似性度量
  - 系统聚类
  - K-means 聚类
  - 案例分析： 上市公司的财务数据分析
  - 聚类分析的项目演练
- 判别分析
  - 问题： 费歇尔的鸢尾花数据
  - 判别分析的基本思想
  - 两总体的距离判别
  - 多总体的距离判别
  - 案例分析： 全国各地区消费水平的类型研究
  - 判别分析的项目演练
- 主成分分析
  - 问题： 各地区生产总值比较
  - 主成分分析的基本思想
  - 主成分分析的模型
  - 主成分分析的性质
  - 案例分析： 企业经济效益评价研究
  - 主成分分析的项目演练
- 因子分析
  - 问题： 1904 年 Spearman 对学生考试成绩的研究
  - 因子分析的基本思想
  - 因子分析的模型
  - 因子分析的步骤
  - 案例分析： 全国 35 个中心城市的综合发展水平评价研究
  - 因子分析的项目演练
- 市场调查
  - 市场调查总论
  - 市场调查过程
  - 问卷设计
  - 抽样设计
  - 案例分析： 规模以下工业抽样调查方案
- 项目案例分析
  - 基于手机 APP 数据的重复消费行为
  - 中国市场经济秩序的测度指标体系研究
  - 北京市水资源分配博弈模型研究
  - 全国经济普查方案研究

## **分布式爬虫实战**

### 课程简介

这是一门培养专业爬虫工程师的课程。 本课程以大数据业务需求为导向， 旨在**掌握分布式爬虫的原理、 理解互联网技术和各类数据分析挖掘的应用技巧**

### 目标

- 掌握分布式爬虫的实现原理以及常用的使用场景。 例如内容聚合、 过程跟踪、 比较， 数据挖掘等
- 了解如 Google， 百度， 今日头条等互联网公司的产品技术和解决方案

### 课程大纲

- 互联网、 互联网架构方面介绍， 网站基本原理及扫盲
  - 互联网的暴露方式
    - URL
    - 静态网页
    - 动态网页
    - Web Service
  - 网站分析及评估
    - Robox.txt
    - 网站地图
    - 估算网站及内容数量
    - 分析网站所使用的技术
    - 网站分析常用工具即方法
- 爬虫基本原理、 搭建第一个爬虫
  - 网页结构分析
  - 宽度 OR 深度？
  - 设置爬虫偏好
  - 设计爬虫队列
    - 任务分配
    - Visited 列表
    - 去重
- 分布式爬虫
  - 分布式爬虫
    - 串行爬虫
    - 多线程爬虫
    - 多进程爬虫
    - 线程、 进程及多机之间的协作
  - 分布式存储及处理
    - HDFS
    - MongoDB
    - Redis
    - 常用数据处理方式
- 爬虫与范爬虫的对抗
  - 动态内容
  - 验证码
  - 表单交互
  - 登录及访问限制
- 处理 HTML 页面
  - 正则表达式
  - HTML 解析
  - WebView、 JavaScript 直接处理页面
  - NPL 及分类器
- 去除页面中的噪声
  - 数据清洗
  - 噪声对网页的影响
  - 利用统计学消除噪声
  - 利用视觉消除噪声
- 内容去重
  - 定义重复
  - 排重
  - 指纹技术的应用
- 网页内容处理： 文档、 视频、 音频
  - PDF 文件及内容处理
  - Office 内容抽取
  - RTF 内容抽取
  - 多媒体内容
    - 视频及视频关键帧
    - 音频抽取
- 网页内容处理： 图像、 3D 模型、 分类、 聚类
  - 网页分类
  - 网页聚类
- 爬虫应用： 自然语言处理和数据追踪
  - NLP
  - 广告分析（淘宝、 西贴）
  - 动态追踪（人人车、 优信拍）
- 爬虫应用： 搜索引擎
  - 内容提取与结构化（百科）
  - 搜索引擎（Google， 百度）
- 爬虫应用： 知识库、 聚合类应用哦及网站、 机器学习
  - 知识库（WikiWand）
  - 新闻聚类（今日头条）
  - 机器学习样本数据

