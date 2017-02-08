# AngularJS Basic Concept

## Directive

### 指令的编译过程

- 加载 angularjs 库， 查找到 `ng-app` 指令， 从而找到应用的边界
- 根据 `ng-app` 划分的作用域来调用 `$compile` 服务进行编译
- angularjs 会遍历整个 HTML 文档， 并根据 js 中指令的定义来处理在页面上声明的各种指令
- 按照指令的优先级(priority)排列， 根据指令中的配置参数 (template, place, transclude 等) 转换 DOM
- 按顺序执行各指令的 compile 函数(如果指令上有定义 compile 函数) 对模块自身进行转换。 *注意， 此处的 compile 函数是指令中配置的， 跟上面的 `$compile` 服务不一样*
- compile 函数执行完会返回一个 link 函数， 所有的 link 函数会合成一个大的 link 函数， 然后这个大的 link 函数就会被执行， 主要做 数据绑定， 通过在 DOM 上注册监听器来动态修改 scope 中的数据， 或者使用 `$watchs` 来监听 scope 中的变量来修改 DOM， 从而建立双向数据绑定等等。
- 若指令中没有配置 compile 函数， 则配置的 link 函数就会运行。 它做的事情大致跟上面 compile 返回之后所有的 link 函数合成的大的 link 函数差不多。

**注意：** 在指令中 compile 与 link 选项是互斥的， 如果同时设置了这两个选项， 就会把 compile 所返回的函数当做是 link 函数， 而 link 属性本身就会被忽略。

### 属性介绍

| 属性          | 含义                                       |
| ----------- | ---------------------------------------- |
| restrict    | 申明标识符在模板中的作为元素、 属性、 类、 注释或组合， 如何使用       |
| priority    | 设置模板中相对于其他标识符的执行顺序                       |
| template    | 指定一个字符串式的内嵌模板， 如果你指定了模板是一个 URL， 就无须使用此属性 |
| templateUrl | 指定 URL 加载的模板， 如果你已经指定了内嵌的模板字符串， 就无须使用此属性 |
| replace     | 如果为真， 替换当前元素， 如果是假或未指定， 拼接到当前元素          |
| transclude  | 移动一个标识符的原始字节带你到一个新模板的位置                  |
| scope       | 为这个标识符创建一个新的作用域， 而不是继承父作用域               |
| controller  | 创建一个控制器通过标识符公开通信 API                     |
| Require     | 当前标识符需要两一个标识符提供正确的函数                     |
| link        | 通过代码修改目标 DOM 元素的实例， 添加事件监听， 建立数据绑定       |
| compile     | 通过标识符拷贝编程修改 DOM 模板                       |

- restrict(String): 可选参数， 指明指令在 DOM 里面以什么形式被声明；可取以下值

  - E(Element): <directiveName></directiveName>
  - A(Attribute): 默认， <div directiveName='expression'></div>
  - C(Class): <div class='directiveName'></div>
  - M(Moment): <--directive:directiveName expression-->

  一般来说，当你创建一个有自己模板的组件的时候，需要使用元素名，如果仅仅是为为已有元素添加功能的话，就使用属性名

  *注意：如果想支持IE8，则最好使用属性和类形式来定义。 另外Angular从1.3.x开始, 已经放弃支持IE8了.*

- priority(Number): 可选参数， 指明指令的优先级， 若在单个 DOM 上有多个指令， 则优先级高的限制性， 设置指令的优先级算是不常用的

- terminal(bool): 可选参数， 可以被设置为 true 或 false， 若设置为 true， 则优先级低于此指令的其他指令则无效， 不会被调用， 优先级相同的的还是会执行

- template(String or Function): 可选参数。 参数为函数是， 可接受两个参数 tElement 和 tAttrs

- templateUrl(String or Function): 可选参数。 参数为函数是， 可接受两个参数 tElement 和 tAttrs。由于加载html模板是通过异步加载的，若加载大量的模板会拖慢网站的速度，可以先缓存模板。*注意：在本地开发时候，需要运行一个服务器，不然使用templateUrl会报错 Cross Origin Request Script（CORS）错误*

- replace(bool): 默认值为 false

- scope(bool or Object): 可选参数， 可取以下值

  - false: 默认，继承父作用域
  - true: 继承父作用域， 并创建自己的作用域（子作用域）
  - Object: 表示创建一个全新的隔离作用域

  **注意：**

  - 若一个元素上有多个指令，使用了隔离作用域，则只有其中一个可以生效；
  - 只有指令模板中的根元素才能获得一个新的作用域，这时候，scope就被设置为true了；

  *当你想要创建一个可重用的组件时隔离作用域是一个很好的选择，通过隔离作用域我们确保指令是‘独立’的,并可以轻松地插入到任何HTML app中，并且这种做法防止了父作用域被污染*

  另外， 隔离作用域可以通过绑定策略来访问父作用域的属性， 具体的绑定方式有以下几种：

  - @(@attr):单向文本(字符串)绑定， 如果绑定的隔离作用域属性名与元素的属性名相同， 则可以采取缺省写法
  - =(=attr): 双向绑定。也可采用缺省写法。*注意：若要直接在指令运行的那个元素上设置属性时候，是直接将 实际的作用域模型 赋值给该属性*
  - &: 调用父作用域中的函数 

- transclude(bool or 'Element'): 该选项可以提取包含在指令那个元素里面的内容， 再将其放置在指令模板特定的位置。 当开启 transclude 后， 可以使用 `ng-transclude` 来指明应该放在什么地方放置 transcluded 内容。另外， 当开启 transclude， 会创建一个新的 transcluyde 空间， 并继承了父作用域(*即使 scope 设置为隔离作用域*) 。 默认为 false。 

  transclude: true 与 transclude: 'element' 的区别：true 是嵌入表达式的值， 而 element 嵌入的是整个元素， 可以参考 [transclude: 'element' is useless without replace:true](https://github.com/angular/angular.js/issues/3368).

  **注意: ** 在一个指令的模板 template 上只能申明一个 `ng-transclude`. 若想把嵌入部分多次放入到模板中的话， 可以使用 `$transclude` 或使用 compile 函数(transcludeFn 函数) 或使用 link 函数

- controller(String or Fn): 字符串时， 则将其看成是控制器的名字， 来查找注册在应用中的控制的构造函数。 也可以直接在指令内部定义为匿名函数（可以注入任何服务）此处可以注入一些特殊的服务(参数)， 具体如下：

  - $scope: 与指令元素相关联的作用域
  - $element: 当前指定对应的元素
  - $attrs: 由当前元素的属性组成的对象
  - $transclude： 嵌入链接函数， 实际被执行用来克隆元素和操作 DOM 的函数

  **注意：** 除非用来定义一些可复用的行为， 一般不推荐在这使用。 指令的控制器和 link 函数可以进行互换。 区别在于， 控制器主要是用来提供可在指令间复用的行为但 link 函数只能在当前内部指令中定义行为， 且无法再指令间复用。

  **注意：** 使用 `$transclude` 会生成一个新的作用域。 默认情况下， 如果简单使用 `$transclude()`， 那么默认的其作用域就是 `$transclude` 生成的作用域。 但是如果使用 `$transclude($scope, function(clone){})`, 那么作用域就是 directive 的作用域了。 如果想使用父作用域， 可以通过 `$scope.$parent`来获取父作用域。 同理想要一个新的作用域， 也可以使用 `$scope.$parent.new()`.

- controllerAs: 设置控制器的别名

- require(String or Array): String 表示另一个指令的名字， 它将作为 link 函数的第四个参数。 可以在 require 的参数值加上下述前缀， 用来改变查看控制器的行为：

  - 没有前缀: 指令会自身提供的控制器中进行查找， 如果找不到任何控制器， 则会抛出一个 error
  - ?: 如果在当前的指令没有找到所需的控制器， 则会将 null 传给 link 函数的第四个参数
  - ^: 如果在当前的指令没有找到所需的控制器， 则会查找父元素的控制器
  - ?^ 组合

- compile 函数: 该选项可以返回一个对象或者函数。 在这里可以在指令和实时数据被放到 DOM 中之前进行 DOM 操作。 此函数是负责对模板的 DOM 进行转换， 并且仅仅只会运行一次。一般不需要对模板进行转换， 所以只要编写 link 函数即可。

  *tips:* preLink 函数会在编译阶段之后， 指令链接到子元素之前执行， 类似的， postLink 会在指令连接到子元素之后执行。 这意味着， 为了不破坏绑定过程， 如果你需要修改 DOM 结构， 应该在 postLink 函数中来修改 DOM 结构。

- link 函数:   该函数负责将作用域和 DOM 进行链接。 若指令中定义有 require 选项， 则 link 函数会有第四个参数， 代表控制器或者所依赖的指令的控制器。

### ng-model

该对象中包含的属性和方法如下：

- `$viewValue`: 视图值， 即显示在视图 (页面) 的实际值。
- `$modelValue`: 模型值， 即赋给 ng-model 的值 (与控制绑定的值)。 它与 `$viewValue` 不一定相等， 因为 `$viewValue` 同步到 `$modelValue` 需要经过一系列的操作（经过三个管道）， 大多数情况下两者是相等的。
- `$parsers`: 是一个执行它里面每一个元素 (每一个元素都是一个函数) 的数组， 主要是用来验证和转换值的过程， ngModel 从 DOM 读取的值会被传入到其中的函数， 它会依次执行每一个函数， 把每一个函数指定的结果传个下一个函数， 而最后一个函数执行的值将会传到 model 中。
- `$formatters`: 是一个执行它里面每一个元素 (每一个元素都是一个函数) 的数组，主要用来对值进行格式化和转化， 以便在绑定了这个值的控件中显示。 当数据的模型值发生变化的时候， 里面的函数会被一一执行
- `$viewChangeListeners`: 是一个由函数组成的数组， 当视图的值发生变化的时候， 里面的函数会被一一调用， 实现跟 `$watch` 类似的功能
- `$render`: 负责将模型值同步到视图上， 如果模型值被改变， 需要同步视图的值。
- `$setViewValue`: 设置视图值
- `$error`： 一个包含所有 error 的对象
- `$setPristine`: 设置为原始状态， 会添加 `ng-pristine` 的 class 类名， 移除 `ng-dirty` 的 class 类名
- `$setValidity`: 设置错误的标志。 这个函数接受两个参数， 第一个参数为错误标志的名字， 是 String， 将会被设置成 $error 的属性， 第二个参数为 bool， 为这个错误标志的值。
- `$name`: input 的 name 属性的值
- `$$validityState`: 
- `$isEmpty(value)`: 判断是否为空。
- `$pristine`: 没有交互时， 为 true
- `$dirty`: 已经进行交互过， 为 true
- `$valid`: 没有错误时为 true
- `$invalid`: 有错误时为 true