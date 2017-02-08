# Python 学习笔记

## 第一章 基本环境

### 1.1 虚拟机
Python 是一种半编译半解释型运行环境。 首先， 它会在模块 『载入』 时将源码编译成代码字节码 (Byte Code)。 而后， 这些字节码会被虚拟机在一个 『巨大』 的核心函数里解释执行。 这是导致 Python 性能较低的重要原因， 好在现在有了内置 Just-in-time 二次编译器的 [PyPy](http://pypy.org/) 可供选择。

当虚拟机开始运行时， 它通过初始化函数完成整个环境设置：

* 创建解释器和主线程状态对象， 这是整个进程的跟对象。
* 初始化内置类型。 数字、 列表等类型都有专门的缓存策略需要处理。
* 创建 `__builtin__` 模块， 该模块持有内置类型和函数。
* 创建 sys 模块， 其中包含了 sys.path、 modules 等重要的运行期信息。
* 初始化 import 机制。
* 初始化内置 Exception。
* 创建 `__main__` 模块， 准备运行所需的 namespace
* 通过 site.py 将 site-packages 中的第三方扩展库添加到搜索路径列表。
* 执行入口 py 文件。 执行前会将 `__main__.__dict__` 作为 namespace 传递进去。
* 程序执行结束。
* 执行清理操作， 包括调用退出函数， GC 清理现场， 释放所有模块等。
* 终止进程。

### 1.2 类型和对象
先有类型 (Type)， 而后才能生成实例 (Instance). Python 中的一切都是对象， 包括类型在内的每个对象都包含一个标准头， 通过头部信息就可以明确知道其具体类型。

头信息由 『引用计数』 和 『类型指针』 组成， 前者在对象被引用时增加， 超出作用域或手工释放后减小， 等于 0 时会被虚拟机回收 (某些被缓存的对象计数器永远不会为 0)。

以 `int` 为例， 对应 Python 结构定义是：

```
     #define PyObject_HEAD
     Py_ssize_t ob_refcnt;
     struct _typeobject *ob_type;
        
     typedef struct _object {
         PyObject_HEAD
     } PyObject;
     
     typedef struct {
         PyObject_HEAD    // 在 64 位版本中， 头长度为 16 字节
         long ob_ival;    // long 是 8 字节
     } PyIntObject;
```

