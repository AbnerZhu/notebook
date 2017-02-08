#Angular Material

## Material Design

Material Design 是 Google 提出的一套用户界面设计的参考指南。使用 Material Design 的应用在外观、交互性和动画效果等方面都有很好的用户体验。

Material Design 是一套用户界面的设计指南。它的设计目标是创造一个把经典设计原则和科技的创新与潜能有机地融合起来的视觉语言。开发一个在不同的平台和设备尺寸上拥有统一用户体验的底层系统。

Material Design 的首要设计原则是使用材质（material）作为隐喻。材质的灵感来源于对纸张和墨水的研究，并在触觉体验上做了进一步的提升。材质的表面和边缘可以提供视觉上的线索，帮助用户更快的了解界面元素的用法。光照、表面和移动等元素传递了物体如何在空间中移动和交互的相关信息。第二个原则是采用基于印刷品的设计思路来指导视觉元素的设计，包括字体、网格、间隔、大小、颜色和图片使用等。这些元素用来创建层次结构、含义和焦点。最后一个原则是使用动作来表达含义。动作的作用在于保持用户的注意焦点并保证交互的连贯性。

Material Design 是一个很复杂的用户界面指南。大多数时候开发人员并不需要了解指南的具体细节，只需要使用相关的 API 和库即可。例如，对于 Android 开发人员来说，只需要使用 Android 提供的 Material Design 主题即可。对于 Web 应用来说，可以使用 Polymer 项目提供的 paper elements 库。如果使用 AngularJS，则可以使用本文中要介绍的 Angular Material 项目。这个项目提供了一系列基于 Material Design 的可复用用户界面组件。

angular-material 是 AngularJS 的一个子项目，用来提供实现了 Material Design 风格的组件。是 AngularJS 框架之上的 Material Design 的具体实现，由 AngularJS 项目组负责开发和维护。

## Angular Material 使用

### 引用

Angular Material 使用起来非常简单， 只需要在页面上添加响应的 JavaScript 和 CSS， 可以通过以下三种方式引用：

- 从 Google 提供的 CDN 下载（可越狱情况下， 相对来说稳定点）
- 官方网站直接下载
- Bower 安装

示例如下：

```
<html lang="en" ng-app=“MyApp">
 <head>
   <link rel="stylesheet" href="https://rawgit.com/angular/bower-material/master/angular-material.css">
 </head>
 <body ng-controller="AppCtrl">
   <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.6/angular.min.js"></script>
   <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.6/angular-animate.min.js"></script>
   <script src="//ajax.googleapis.com/ajax/libs/angularjs/1.3.6/angular-aria.min.js"></script>
   <script src="https://rawgit.com/angular/bower-material/master/angular-material.js"></script>
 </body>
</html>
```

### 布局

Angular Material 使用的是 CSS3 规范中定义的弹性盒布局模型（flexbox）。该布局模型作为 W3C 的推荐规范，已经被主流浏览器的新版本所支持，可以在很大程度上简化常见的布局场景的实现，而不必使用过多的 DIV 元素来进行布局。因此在使用 Angular Material 进行布局之前，需要先对弹性盒布局模型有一定的了解。

与 Bootstrap 不同的是，Angular Material 使用 HTML 属性而不是 CSS 类来定义布局。

- 布局方式：
    - 行布局 (layout="row")
    - 列布局 (layout="column")
    
布局容器中的子元素可以通过 flex 属性来定义其大小。如果只是添加一个 flex 属性，则该子元素会被自动分配容器元素的可用空间。也可以为 flex 属性指定一个 0 到 100 之间的整数来定义其所占空间的百分数。不过该整数值只能是 33、66 或 5 的倍数。