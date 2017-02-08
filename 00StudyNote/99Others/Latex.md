# 数学公式
* 角标（上下标）

上标命令： ^{}, 如 `x^2`, `x^{x+y}`

下标命令： _{}, 如 `x_2`, `x_{x+y}`

如果使用文字作为角标， 首先要把文字放到 `\mbox{}` 文字模式中， 另外要加上改变文字大小的命令。 如`\partial f_{\mbox{\tiny 极大值}}`

角标可以进行多级化， 如：
$$X^{x_{1}^{x^2}}$$

* 分式

分式命令： \frac{分子}{分母}

分数线长度值是预设为分子分母的最大长度， 如果想要使分数线再长一点， 可以在分子或分母两端添加一些间隔。
$$ x_0+\frac{1}{x_1+\frac{1}{x_2+\frac{1}{x_3+\frac{1}{x_4}}}}$$

* 根式
    -  二次根式命令：\sqrt{表达式} 
    -  n次根式命令：\sqrt[n]{表达式}

当被开方表达式较高时， 开方次数的位置显得略低， 解决办法为： 将开方次数改为上标， 并拉近与根式的水平距离， 即将命令中的`[n]`改为`[^n\!]`（^ 表示上标， 间隔命令 \! 表示缩小间隔）

命令 \surd 生成根号上没有横线的根式。

* 求和与积分
    - 求和命令： \sum_{k = 1 \}^n （求和项紧随其后，下同）
    - 积分命令： \int_a^b
    - 改变上下限位置的命令： \limits(强制上下限在上下侧)和 \nolimits(强制上下限在右侧)
    
 * 下划线、 上划线等
     - 上划线命令： \overline{公式}
     - 下划线命令： \underline{公式}
     - 上花括弧命令： \overbrace{公式}^{说明}
     - 下花括弧命令： \underbrace{公式}_{说明}     
    
* 数学重音符号

|公式|效果|
|---|:---:|
|\hat{a}| $$ \hat{a} $$|
|\check{a}|$$\check{a}$$|
|\breve{a}|$$\breve{a}$$|
|\tilde{a}|$$\tilde{a}$$|
|\bar{a}|$$\bar{a}$$|
|\vec{a}|$$\vec{a}$$|
|\acute{a}|$$\acute{a}$$|
|\grave{a}|$$grave{a}$$|
|\mathring{a}|$$\mathring{a}$$|
|\dot{a}|$$\dot{a}$$|
|\ddot{a}|$$\ddot{a}$$|
|\widehat{abc}|$$\widehat{abc}$$|
|\widetilde{xyz}|$$\widetilde{xyz}$$|

* 堆积符号
    * 符号堆积命令： \stacrel{上位符号}{基位符号}。基位符号大， 上位符号小
    * {上位公式\atop 下位公式}。上下符号一样大
    * {上位公式\choose 下位公式\}。上下符号一样大； 上下符号被包括在圆括弧内。 如：
    $$vec{x}\stackrel{\mathrm{def}}{=}{x_1,\dots,x_n}\\
                {n+1 \choose k}={n \choose k}+{n \choose k-1}\\
                \sum_{k_0,k_1,\ldots>0 \atop k_0+k_1+\cdots=n}A_{k_0}A_{k_1}\cdots$$


* 定界符

|公式|效果|
|---|:---:|
|\[|$$\[$$|
|()|$$()$$|
|\big(\big)|$$\big(\big)$$|
|\Big(\Big)|$$\Big(\Big)$$|
|\bigg(\bigg)|$$\bigg(\bigg)$$|
|\Bigg(\Bigg)|$$\Bigg(\Bigg)$$|
|\]|$$\]$$|