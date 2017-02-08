# 什么是 Promise
## 什么是 Promise
Promise 是抽象异步处理对象以及对其进行各种操作的组件。

Promise 最初被提出是在 [E语言](http://erights.org/elib/distrib/pipeline.html) 中， 它是基于并列/并行处理设计的一种编程语言。

如果说到基于 JavaScript 的异步处理， 大多数都会想到利用回调函数。

下面的代码即为使用了回调函数的异步处理。

```
getAsync('fileA.txt', function(error, result) { // 传给回调函数的参数为 (error 对象， 执行结果) 组合
        if(error) { // 取得失败时的处理
            throw error;
        }
        // 取得成功时的处理
})
```

Node.js 等规定在 JavaScript 的回调函数的第一个参数为 `Error` 对象， 这也是它的一个惯例。

像上面这样基于回调函数的异步处理如果统一参数使用规则的话， 写法也会很明了。 但是， 这也仅是编码规约而已， 即使采用不同的写法也不会出错。

而 Promise 则是把类似的异步处理对象和处理规则进行规范化， 并按照采用统一的接口来编写， 而采取规定方法之外的写法都会出错。

下面是使用了 Promise 进行异步处理的一个例子。

 ```
var promise = getAsyncPromise('fileA.txt'); // 返回 Promise 对象
promise.then(function(result) {
    // 获取文件内容成功时的处理
}).catch(function(error) {
    // 获取文件内容失败时的处理
})
 ```

我们可以向这个预设了抽象化异步处理的 promise 对象， 注册这个 promise 对象执行成功时和失败时相应的回调函数。

这和回调函数方式相比有哪些不同之处呢？ 在使用 promise 进行异步处理的使用。 我们必须按照接口规定的方法编写处理代码。 即除 promise 对象规定的方法以外的方法都是不可以使用的， 而不会像回调函数方式那样可以自己自由的定义回调函数的参数， 而必须严格遵守固定、 统一的编码方式来编写代码。

这样， 基于 Promise 的统一接口的做法， 就可以形成基于接口的各种各样的异步处理模式。 所以， Promise 的功能是可以将复杂的异步处理轻松地进行模式化， 这也可以说得上是使用 promise 的理由之一。

Promise 对象有以下两个特点

- 对象的状态不受外界影响。 Promise 对象代表一个异步操作， 有三种状态： *Pending, Resolved, Rejected*。 只有异步操作的结果， 可以决定当前是哪一种状态， 任何其他操作都无法改变这个状态。 这也是 Promise 这个名字的由来。
- 一旦状态改变， 就不会再变， 任何时候都可以得到这个结果。 Promise 对象的状态改变， 只有两种可能： *Pending —> Resolved, Pending —> Rejected*。 只要这两种情况发生， 状态就凝固了， 不会再变了， 会一直保持这个结果。 就算改变已经发生了， 再对 Promise 对象添加回调函数， 也会立即得到这个结果。 这与事件完全不同， 事件的特点是， 如果你错过了它， 再去监听， 是得不到结果的。

Promise 也有一些缺点：

- 无法取消 Promise， 一旦新建它就会立即执行， 无法中途取消
- 如果不设置回调函数， Promise 内部抛出的错误， 不会反应到外部
- 当处于 Pending 状态时， 无法得知目前进展到哪一个阶段（刚刚开始还是即将完成）

## Promise 简介
在 *ES6 Promises* 标准中定义的 API 还不是很多。 目前大致有下面三种类型。

* Constructor

Promise 类似于 `XMLHttpRequest`， 从构造函数 `Promise` 来创建一个新 Promise 对象作为接口。 如下：

```
var promise = new Promise(function(resolve, reject) {
    // 异常处理
    // 处理结束后， 调用 resolve 或 reject
});
```

* Instance Method

对通过 *new* 生成的 Promise 对象为了设置其值在 resolve(成功)/reject(失败)时调用的回调函数， 可以使用 `promise.then()` 实例方法。

    promise.then(onFulfilled, onRejected)
​    

* * resolve(成功)时： onFulfilled 会被调用
    * reject(失败)时: onRejected 会被调用

`onFulfilled`、 `onRejected` 两个都为可选参数。

`promise.then` 成功和失败时都可以使用。 另外在只想对异常进行处理时可以采用。

`promise.then(undefined, onRejected)` 这种方式， 只指定 reject 时的回调函数即可。 不过这种情况下 `promise.catch(onRejected)` 应该是个更好的选择。

    promise.catch(onRejected)

* Static Method

像 Promise 这样的全局对象还拥有一些静态方法。 包括 `Promise.all()` 还有 `Promise.resolve()` 等在内， 主要都是一些对 Promise 进行操作的辅助方法。

## Promise 基本的 API

- Promise.resolve()
- Promise.reject()
- Promise.prototype.then()
- Promise.prototype.catch()
- Promise.all() // 所有的完成
- Promise.race() // 竞速， 完成一个即可








​    

