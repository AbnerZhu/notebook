# Google Java Style

## 前言

- 术语 *class* 可表示一个普通类， 枚举类， 接口或是 annotation 类型 (`@interface`)
- 术语 *comment* 只用来指代实现的注释 (implementation comments)， 不适用 "documentation comments" 一词， 而是用 *Javadoc*

## 源文件基础

### 文件名

源文件以其最顶层的类名来命名， 大小写敏感， 文件扩展名为 `.java`

### 文件编码： UTF-8

### 特殊字符

- 空白字符

  除了行结束符序列， ASCII 水平空格字符 (0x20, 即空格) 是源文件中唯一允许出现的空白字符， 这意味着：

  - 所有其他字符串中的空白字符都需要进行转义
  - 制表符不用于缩进

- 特殊转义字符

  对于具有特殊[转义序列](http://zh.wikipedia.org/wiki/%E8%BD%AC%E4%B9%89%E5%BA%8F%E5%88%97)的任何字符(\b, \t, \n, \f, \r, ", '及\)，我们使用它的转义序列，而不是相应的八进制(比如`\012`)或Unicode(比如`\u000a`)转义

- 非 ASCII 字符

  对于剩余的非ASCII字符，是使用实际的Unicode字符(比如∞)，还是使用等价的Unicode转义符(比如\u221e)，取决于哪个能让代码更易于阅读和理解。

  > Tip: 在使用Unicode转义符或是一些实际的Unicode字符时，建议做些注释给出解释，这有助于别人阅读和理解。

  ```java
  String unitAbbrev = "μs";                                 | 赞，即使没有注释也非常清晰
  String unitAbbrev = "\u03bcs"; // "μs"                    | 允许，但没有理由要这样做
  String unitAbbrev = "\u03bcs"; // Greek letter mu, "s"    | 允许，但这样做显得笨拙还容易出错
  String unitAbbrev = "\u03bcs";                            | 很糟，读者根本看不出这是什么
  return '\ufeff' + content; // byte order mark             | Good，对于非打印字符，使用转义，并在必要时写上注释
  ```

  > Tip: 永远不要由于害怕某些程序可能无法正确处理非ASCII字符而让你的代码可读性变差。当程序无法正确处理非ASCII字符时，它自然无法正确运行， 你就会去fix这些问题的了。(言下之意就是大胆去用非ASCII字符，如果真的有需要的话)

## 源文件结构

一个源文件包含 (按顺序地)：

- 许可证或版权信息 (如有需要)
- package 语句
- import 语句
- 一个顶级类(public, **只有一个**)

以上每个部分之间用一个空行隔开

### 许可证或版权信息

如果一个文件包含许可证或版权信息， 那么它应当被放在文件最前面。

### package 语句

package 语句不换行， 列限制并不适用于 package 语句。 (即 package 语句写在一行里)

### import 语句

- import 不用使用通配符。 即不要出现类似这样的 import 语句： `import java.util.*;`

- 不要换行。 import 语句不换行， 列限制并不适用于 import 语句。 (每个 import 语句独立成行)

- 顺序和间距。 import 语句可分为以下几组， 按照这个顺序， 每组由一个空行分隔：

  - 所有的静态导入独立成组
  - `com.google` imports (仅当这个源文件是在 `com.google` 包下)
  - 第三方的包。 每个顶级包为一组， 字典序。 例如: android, com, junit, org, sun
  - `java` imports
  - `javax` imports

  组内不空行， 按字典序排序

### 类声明

- 只有一个顶级类声明。 每个顶级类都在一个与它同名的源文件中 (当然， 还包含`.java` 后缀)。 例外: `package-info.java`， 该文件中可没有 `package-info` 类
- 类成员顺序。 类的成员顺序对易学性有很大的影响，但这也不存在唯一的通用法则。不同的类对成员的排序可能是不同的。 最重要的一点，每个类应该以某种逻辑去排序它的成员，维护者应该要能解释这种排序逻辑。比如， 新的方法不能总是习惯性地添加到类的结尾，因为这样就是按时间顺序而非某种逻辑来排序的。
  - 重载： 永不分离。 当一个类有多个构造函数，或是多个同名方法，这些函数/方法应该按顺序出现在一起，中间不要放进其它函数/方法。

## 格式

**术语说明**：块状结构 (block-like construct) 指的是一个类， 方法或构造函数的主体。 需要注意的是， 数组初始化中的初始值可被选择性的视为块状结构。

### 大括号

- ​

## 命名约定



## 编程实践



## Javadoc



## 后记

