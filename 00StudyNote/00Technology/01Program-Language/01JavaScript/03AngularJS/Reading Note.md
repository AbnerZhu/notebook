### AngularJS 权威指南
#### 第 1 章 初始 AngularJS
##### 1.1 浏览器如何获取网页
###### 1.2 浏览器是什么

- 基本功能： 获取网页， 并将其显示给用户
- 工作原理： 浏览器获取页面对应的 HTML 文本， 将其解析为一个浏览器内部使用的结构（DOM）， 对页面内容进行布局， 并在内容显示到屏幕上之前加上养伤， 所有这些工作都是在浏览器内部进行的。 

##### 1.3 AngularJS 是什么

官方介绍： 完全使用 JavaScript 编写的客户端技术。 同其他历史悠久的 Web 技术（HTML、 CSS 和 JavaScript）配合使用， 使 Web 应用开发比以往更简单、 更快捷。 是一种构建动态 Web 应用的结构化框架。

用途： 构建单页面 Web 应用。 

目的： 它通过增加开发人员和常用 Web 应用开发任务之间的抽象级别， 使构建交互式的现代 Web 应用变得更加简单。

优势： AngularJS 使开发 Web 应用变得非常简单， 同时也降低了构建复杂应用的难度。 

常用功能：

- 解耦应用逻辑、 数据模型和视图（MVC）；
- Ajax 服务；
- 依赖注入（DI）
- 浏览历史（使书签和前进、 后退按钮能够像在普通 Web 应用中一样工作）；
- 测试；
- 其他。

###### 1.3.1 AngularJS 有什么不同
在其他 JavaScript 框架中， 我们被迫从自定义的 JavaScript 对象中进行扩展 ， 并从外到内操作 DOM。 如 jQuery。

    var btn = $('<button>Hi</button>');
    btn.on('click', function(vet) { console.log('Clicked button');})
    $('#checkoutHolder').append(btn);
    
尽管这个操作的过程不是很复杂， 但是它要求开发着对整个 DOM 结构都有所了解， 并强迫我们在 JavaScript 代码中加入复杂的控制逻辑， 用以操作外部 DOM。

而 AngularJS 则通过原生的 MVC 功能增强了 HTML。 结果表明， 这个选择可以快捷和愉悦地构建出令人印象深刻并且极富表现力的客户端应用。

利用它， 开发者可将页面的一部分封装为一个应用， 并且不强迫整个页面都是用 AngularJS 进行开发。 这个特质在某些情况下非常有用， 比如你的工作流程中已经包含了另外一个框架， 或者你只希望页面中的某一部分是动态的， 而剩下的部分是静态的或者由其他 JavaScript 框架来控制的。

此外， AngularJS 团队非常重视框架文件压缩后的大小， 这样使用它就不会付出太多的额外代价。 这一特性使得 AngularJS 非常适合用于开发功能原型。


#### 第 2 章 数据绑定和第一个 AngularJS Web 应用
**Hello World**

```
    <!DOCTYPE html>
    <html ng-app>
        <head>
            <title>Simple App</title>
            <script src="https://ajax.googleapis.com/ajax/libs/angularjs/1.2.13/angular.js"/>
        </head>
        <body>
            <input ng-model="name" type="text" placeholder="Your name" />
            <h1>Hello {{name}}</h1>
        </body>
    </html>
```
这个例子展示了 AngularJS 最基本也最令人印象深刻的功能之一： 数据绑定。

**注**： 以上范例中的代码不是为规范的代码。

##### 2.1 AngularJS 中的数据绑定
在 Rails 等传统 Web 框架中， 控制器将多个模型中的数据和模板组合在一起形成视图， 并将其提供给用户， 这个组合过程产量一个单向视图。 如果没有创建任何自定义的 JavaScript 组件， 视图只会体现它渲染时模型暴露出的数据。

Angu 则采用了完全不同的解决方案。 它创建*实时*模板来代替视图， 而不是将数据合并进模板之后更新 DOM。 任何一个独立视图组件中的值都是动态替换的。 这个功能可以说是 Angularjs 中最重要的功能之一， 也是让我们只用 10 行代码， 并且在没有人和 JavaScript 的情况下就可以写出 Hello World 的关键。

要实现这个功能， 只要在 HTML 页面中引用 angular.js， 并在某个 DOM 元素上明确设置 ng-app 属性即可。 ng-app 属性声明所有被其包含的内容都属于这个 AngularJS 引用， 这也是我们可以在 Web 应用中嵌套 Angul 应用的原因。 只有被具有 ng-app 属性的 DOM 元素包含的元素才会受 AngularJS 影响。

**TIPS**：
> 视图中插值会在计算一个或多个变量时被动态替换， 替换结果是字符串中的插值被变量的值替代。

自动数据绑定使我们可以将视图理解为*模型状态的映射*。 当客户端的数据模型发生变化时， 视图就能反映出这些变化， 并且不需要写任何自定的代码， 他就可以工作。 在 MVC 的世界里， 控制器可以不必担心会牵扯到渲染视图的工作。这样我们就不必再担心如何分离视图和控制器， 并且也可以使测试变得即简单又令人愉快。
**TIPS**
> MVC 是一种软件架构设计模式， 它将表现从用户交互中分离出来。 通常来讲， 模型中包含应用的数据和数据进行交互的方法， 视图将数据呈献给用户， 而控制器则是二者之间的桥梁。   
> 这种[表现分离]("http://martinfowler.com/eaaDev/uiArchs.html")能将应用中的表现很好地隔离开来， 因此视图不需要知道如何保存对象， 只要知道如何显示它即可。 这也意味着数据模型不需要同时图进行交互， 只需要包含数据和操作视图的方法。 控制器用来存放将二者绑定在一起的业务逻辑。

AngularJS 会记录数据模型所包含的数据在任何特定时间点的值， 而不是原始值。

当 AngularJs 认为某个值可能发生变化时， 它会运行自己的事件循环来检查这个值是否变 『脏』。 如果该值从上次时间循环运行之后发生了变化， 则该值被认为是『脏』值。 这也是 Angular 可以跟踪和相应应用变化的方式。

>这个事件循环会调用$digest() 循环。

这个过程被称为脏检查(dirty checking)。 脏检查是检查数据模型变化的有效手段。 当有潜在的变化存在时， AngularJS 会在事件循环时执行脏检查来保证数据的一致性。

如果使用 *KnockoutJS* 这种通过在数据模型上绑定事件监听器来监听数据变化的框架， 这个过程会变得更复杂且抵消。处理事件合并、依赖跟踪和大量的事件触发 (event firing) 是非常复杂的， 而且会在性能方面导致额外的问题。

> 尽管存在搞笑的方式， 但脏检查可以运行在所有浏览器中并且是可预测的。 此外， 很多在速度和效率方面有要求的软件都会使用[脏检查的方案][1]。

##### 2.2 简单的数据绑定

> 数据模型对象 (model object) 是指 $scope 对象。 $scope 对象是一个简单的 JavaScript 对象， 其中的属性可以被视图访问， 也可以同控制器进行交互。
> 
> 双向数据绑定 (bi-directional) 意味着如果视图改变了某个值， 数据模型会通过脏检查观察到这个变化， 而如果数据模型改变了某个值， 视图也会依据变化重新渲染。

##### 2.3 数据绑定的最佳实践

由于 JavaScript 自身的特点， 以及它在传递值和引用时的不同处理方式， 通常认为， 在视图中通过对象的属性而非对象本身来进行引用绑定， 是 *ng* 中的 *最佳实践*

#### 第 3 章 模块

在 JavaScript 中， 将函数代码全部都定义在全局命名空间中绝对不是什么好主意， 这样做会导致冲突从而使调试变得非常困难， 浪费宝贵的开发时间。

在 *ng* 中， 我们将生产环境中的控制器、 指令等代码封装在 *模块 (module)* 的单元内。

在 *ng* 中， 模块是定义应用的最主要方式。 模块包含了主要的应用代码。 一个应用可以包含多个模块， 每个模块都包含了定义具体功能的代码。 

使用模块能有以下几点好处： 

* 保持全局命名空间的清洁；
* 编写测试代码更容易，并能保持其清洁，以便更容易找到互相隔离的功能；
* 易于在不同应用间复用代码；
* 使应用能够以任意顺序加载代码的各个部分。

在 *ng* 中，通过 `angular.module('moduleName', [denpencies...])` 方法来声明模块， 这个方法能接受两个参数， 第一个是模块的名称， 第二个是依赖列表， 即可以注入到模块中的对象列表。 这个方法相当于 *ng* 模块的 *setter*  方法， 是用来定义模块的。

在 *ng* 中， 通过 `angular.module('moduleName')` 来引用一个模块。该方法只传递一个参数，为模块的名称。这个方法相当于 *ng* 模块中的 *getter* 方法， 用于获取对模块的引用。

##### 3.1 参数

下面是 `angular.module()` 的参数列表

* name (字符串)： 模块的名称；
* requires (字符串数组)： 包含了一个字符串变量组成的列表， 每个元素都是一个模块名称， 本模块依赖于这些模块， 依赖需要在本模块加载之前由注入器进行预加载。

#### 第 4 章 作用域

作用域 (scope) 是构成 *ng* 应用的核心基础。




---

### AngularJS 慕课
#### I AngularJS 实战
##### 2 基本概念和用法

AngularJS 四大核心特性

+ MVC
+ 模块化和依赖注入
+ 双向数据绑定
+ 指令

为什么需要 MVC

+ 代码规模越来越大，切分职责是大势所趋
+ 为了复用： 很多逻辑是一模一样的
+ 为了后期维护方便： 修改一块功能不影响其他功能。
+ MVC 只是手段， 终极目标是模块化和复用    

前段 MVC 的困难在哪里
    + 浏览器加载脚本 ---> 加载完成之后 JIT 编译执行
    + 操作 DOM 的代码必须等待整个页面全部加载完成
    + 多个 JS 文件之间如果出现互相依赖， 程序员必须自己解决
    + JS 的原型继承也给前端编程带来了很多困哪    
AngularJS 语境下的 MVC 是如何实现的？
    + 
    

###### 2.1 MVC

**Controller**

Controller 使用过程中的注意点

* 不要试图去复用 Controller， 一个控制器一般只负责一小块视图
* 不要再 Controller 中操作 DOM， 这不是控制器的职责
* 不要再 Controller 里面做数据格式化， ng 有很好用的表单空间
* 不要在 Controller 里面做数据过滤操作， ng 有 $filter 服务
* 一般来说， *Controller 是不会互相调用的*， 控制器之间的交互会通过事件进行

**Model**

**View**

如何复用 View？ (Directive)

AngularJS 的 MVC 是借助 *$scope* 来实现的。

神奇的 $scope

* $scope 是一个 POJO(Plain Old JavaScript Object)
* $scope 提供了一些工具方法 $watch()/$apply()
* $scope 是表达式的执行环境 (或者叫作用域)
* $scope 是一个树型结构， *与 DOM 标签平行*
* 子 $scope 对象会继承父 $scope 上的属性和方法
* 每一个 Angular 应用只有一个根 $scope 对象 (一般位于 ng-app 上)
* $scope 可以传播事件， 类似 DOM 事件， 可以向上也可以向下
* $scope 不仅是 MVC 的基础， 也是后面实现双向数据绑定的基础
* 可以用 angular.element($0).scope() 进行调试。

$scope 的生命周期

###### 2.2 路由、 模块、 依赖注入

* AngularJS 的模块化实现
* 一个完整项目结构是什么样的？
* 使用 ngRoute 进行视图之间的路由
* 一切都是从模块开始的 (Modules are containers.)
* ng 官方推荐的模块切分方式是什么？
    + 
    + 
    + 
* 模块之间的依赖应该怎么做？ —— 依赖注入

**路由**

为什么需要前端路由？

* Ajax 请求不会留下 History 记录（对网络型应用、 门户网站是有影响的）
* 用户无法直接通过 URL  进入应用中的指定页面（保存书签、链接分享给朋友？）
* Ajax 对 SEO 是个灾难

使用 ngRoute 进行视图之间的路由

```
    $routeProvider.when('xxx', {
        templateUrl: 'xxx/xxx',
        controller: 'xxxCtrl'
    }).otherwise({
        redirectTo: '/xxx'
    });
```

ngRoute 的功能比较弱， 可以使用 ui-route， 可以参见 <http://angular-ui.github.io>

前端路由的基本原理

* 哈希 #
* H5 中新的 history API
* 路由的核心是给应用定义 『状态』
* 使用路由机制会影响到应用的整体编码方式（需要预先定义好状态）
* 考虑兼容性问题与 『优雅降级』

**模块**


**依赖注入**

###### 2.3 双向数据绑定

* 什么是双向数据绑定
* 取值表达式与ng-bind指令
    + 取值表达式会显示 `{{xxxx}}`， 会影响用户体验， 可以使用 `ng-bind`
    + 一般在首页上使用 `ng-bind`， 后面可以使用取值表达式， 因为一般当 AngularJS 加载以后， 便不会出现 `{{xxxx}}`
* 双向绑定的典型场景 —— 表单
* 动态切换标签样式
* ng-show 和 ng-hide
* ng-class
* ngAnimate([css3 api](htt[://css.doyo.com]))

###### 2.4 指令

* 匹配模式 restrict
    + AEMC， 可以同时使用
    + A： 默认
    + C： 很少使用
    + M 时， 要注意标签前后要留下一个空格 `<!-- directive:xxx -->`
    + 推荐使用元素和属性的方式使用指令
        - 当需要创建带有自己的模板的指令时， 使用元素名称的方式创建指令
        - 当需要为已有的 HTML 标签增加功能时， 使用属性的方式创建指令
    + a
* 模板： template, templateUrl, $templateCache
    + $tempalateCache: 
* replace 与 transclude
    + replace: 指令内部的内容会被替换
    + tranclude: 指令内部的内容不会替换。
* compile 与 link (操作元素、 添加 CSS 样式、 绑定事件)
    + 指令执行的阶段： 加载阶段 ---> 编译阶段 ---> 链接阶段
    + 加载阶段: 加载 angular.js， 找到 ng-app 指令， 确定应用的边界
    + 编译阶段: 
        - 遍历 DOM， 找到所有指令
        - 根据指令代码中的 template、 replace、 transclude 转换 DOM 结构
        - 如果存在 compile 函数则调用 (一般不会自定义， 因为自定义的 compile 函数要实现 ng 已实现的 compile 函数， 会比较麻烦)
    + 链接阶段：
        - 对每一个指令的 link 函数 (此处可以操作 DOM 结构)
        - link 函数一般用来操作 DOM、 绑定事件监听器
    + compile 函数用来对模板自身进行转换， 而 link 函数负责在模型和视图之间进行动态关联
    + 作用域在链接阶段才会被绑定到编译之后的 link 函数上
    + compile 函数仅仅在编译阶段运行一次， 而对于指令的每个实例， link 函数都会执行一次
    + compile 可以返回 preLink 和 postLink 函数， 而 link 函数只会返回 postLink 函数
    + 如果需要修改 DOM 结构， 应该在 postLink 中来做这件事情， 而如果在 preLink 中做这件事情会导致错误
    + 大多数时候我们只要编写 link 函数即可
    + link 函数有四个参数， 分别为 scope、 element、 attribute 和 Controller
* 指令与控制器之间的交互
    + 通过指令的属性来实现， 在 link 函数中的属性要全小写(如 howToLoad ---> howtoload)
* 指令间的交互
    + 指令内部 Controller： 为了让指令暴露出一组 public 方法来让外部使用
    + require： 指令之间的依赖 ***还需详细了解***
    
scope 的类型与独立 scope

* 指令配置的时候添加一个 scope 属性既可创建一个 独立 scope

 
scope 的绑定策略

* 策略
    + @： 把当前属性作为字符串传递。 还可以绑定来自父 scope 的值， 在属性值中插入 {{}} 即可
    + =： 与父 scope 中的属性进行双向绑定
    + &： 传一个来自父 scope 中的属性进行双向绑定  
* 实例

AngularJS 内置的指令 (63 个)

*  form 指令
    * 介绍
        + HTML 原生的 form 表单是不能嵌套的， 而 ng 封装之后的 form 可以嵌套
        + ng 为 form 扩展了自动校验、 防止重复提交等功能
        + ng 对 input 元素的 type 进行了扩展， 一共提供了以下 10 中类型：
            - text
            - number
            - url
            - email
            - radio
            - checkbox
            - hidden
            - button
            - submit
            - reset
        + ng 为表单内置了 4 种 CSS 样式
            - ng-valid
            - ng-invalid
            - ng-pristine
            - ng-dirty
        + 内置校验器
            - require
            - maxlength
            - minlength
    * 实例 (指令（5）) 
*  

Expander（指令（6））

* 

 
* Accordion（指令（6））
    + 
* 指令的运行原理： compile 和 link
    + 
* ERP 类型的系统必备的 UI 组件 <http://miniui.com>
    + 
* 互联网/电商型系统必备的 UI 组件
    + 
* 第三方指令库 angular-ui <http://angular-io.github.io>
    + 
* Directive 思想的起源和原理概述 <http:>
    +
  
  
module.run(): 注射器加载完所有模块时， 此方法执行一次。  




[1]: 比如在游戏开发中就大量使用脏检查技术






