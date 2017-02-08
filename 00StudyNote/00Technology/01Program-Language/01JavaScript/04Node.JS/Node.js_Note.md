[TOC]

# Lean Cloud Vedio

## Node.js 开发实战

### Node.js 介绍和异步风格

> Atwood 定律： 任何能够用 JavaScript 实现的应用系统， 最终都必将用 JavaScript 实现

**Node.js 优势**

- 生态系统
- 同构应用
- 细粒度的异步控制
- 异步操作没有额外开销
- 不需要考虑线程同步

**Node.js 劣势**

- 社区发展速度很『快』
- 强制异步编程的负担

**异步编程**

- 异步风格的 API
  - callback 风格
  - event 风格
  - 两种风格的差异
    - 响应速度快的一般用 callback 风格， 否则最好是用 event 风格


- 注意程序执行的流程
  - 注意处理异常
- [推荐文章](http://www.infoq.com/cn/news/2011/09/nodejs-async-code)

**异常处理**

- 同步代码使用 `try-catch` 捕获异常
- 异步代码使用回调 err 对象捕获异常
- [uncaughtException](https://nodejs.org/api/process.html#process_event_uncaughtexception): 不得以的挽救手段

### NPM 包管理器

NPM: Node Package Manager

**常用命令**

- npm init
- npm install xxx
  - --save: 自动更新依赖列表
  - --save-dev: 自动更新开发依赖列表
  - g: 全局安装
- npm list
- npm shrinkwrap

**依赖管理**

- dependencies
  - 运行依赖
  - 编译依赖， 如 Babel
- devDependencies
  - 测试依赖
  - 开发工具依赖
- [依赖包保存方式](https://docs.npmjs.com/how-npm-works/npm3)

**Scripts**

[文档](https://docs.npmjs.com/misc/scripts)

**指定云引擎 Noode.js 版本**

[文档](https://leancloud.cn/docs/leanengine_webhosting_guide-node.html#package.json)

### 开发工具介绍： curl, Postman, lean-cli

- curl
  - 命令行的 http client
  - 常用参数
    - -X <method>
    - -H <header>
    - -d <data>
- ​

### Promise

### 云函数调试页面的使用

### 使用 mocha 编写测试

### 使用 Express 开发 web 项目

### Redis 介绍和使用 LeanCache





