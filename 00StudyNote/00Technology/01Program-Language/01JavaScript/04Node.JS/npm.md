# npm

<!--
create time: 2015-11-20 10:37:57
Author: Abner Zhu

This file is created by Marboo<http://marboo.io> template file $MARBOO_HOME/.media/starts/default.md
本文件由 Marboo<http://marboo.io> 模板文件 $MARBOO_HOME/.media/starts/default.md 创建
-->

# 基本命令
* `npm init`:  会引导你创建一个 *package.json* 文件，包括名称、版本、作者这些信息等;
* `npm install <name>`: 安装nodejs的依赖包， 默认安装包的最新版本， 若需安装指定的版本， 使用命令 `npm install <name>@version`;
* `npm install <name> -g`:  将包安装到全局环境中。 安装在全局环境中的模块是不能通过 `require()` 的方式引用依赖的， 它是供命令行使用的;
* `npm install <name> --save`: 安装的同时，将信息写入 *package.json* 中;
* `npm remove <name>`: 移除;
* `npm update <name>`: 更新;
* `npm ls`: 列出当前安装的了所有包;
* `npm ls -g`: 列出全局安装的了所有包;
* `npm root`: 查看当前包的安装路径;
* `npm root -g`: 查看全局的包的安装路径;
* `npm help `: 帮助，如果要单独查看install命令的帮助，可以使用的`npm help install`.

<https://docs.npmjs.com/>




