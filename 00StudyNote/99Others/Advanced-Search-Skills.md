[TOC]

# 高级搜索技巧

## 基本搜索

- +： 英文字符， 表示逻辑『与』操作
- -： 英文字符， 表示逻辑『非』操作
- OR： 表示逻辑『或』操作。 但是这个关键字为中文的或查询似乎还有 BUG， 无法得到正确的查询结果。 小写 or 时， 将被忽略
- ~： 使用同义词代替原来查询中的某些字词。
- ""： 精确匹配
- ..： 用两个半角句号（不加空格）隔开两个数字可查看日期、价格和尺寸等指定数字范围的搜索结果。

## 辅助搜索

Google 不支持通配符，如“*”、“?”等，只能做精确查询，关键字后面的“*”或者“?”会被忽略掉。

GOOGLE对英文字符大小写不敏感，“GOD”和“god”搜索的结果是一样的。

GOOGLE的关键字可以是词组（中间没有空格），也可以是句子（中间有空格），但是，用句子做关键字，必须加英文引号。

GOOGLE对一些网路上出现频率极高的词（主要是英文单词），如“i”、“com”，以及一些符号如“*”、“.”等，作忽略处理，如果用户必须要求关键字中包含这些常用词，就要用强制语法“+”。

**注意**：英文符号（如问号，句号，逗号等）无法成为搜索关键字，加强制也不行。

## 高级搜索

- filetype： 可以限定在文档格式中搜索网页信息， 支持文档格式有 pdf, ps, dwf, kml, kmz, doc, xls, ppt, rtf, swf, all(所有上面的文档格式)


- site： 搜索结果局限于某个具体网站或者网站频道。 用法： "site:xxx.xx.xx"， 其中的冒号一定得为英文字符， 而且冒号后不能有空格。 此外， 网站域名不能有 `http` 以及 `www` 前缀， 也不能有任何 `/` 的目录后缀； 网站频道则只局限与 『频道名.域名』 方式， 而不能是 『域名/频道名』 方式。 
- link： 返回所有链接到某个URL地址的网页。「link」 不能与其他语法相混合操作， 所以 "link:" 后面即使有空格， 也将被 Google 忽略
- inurl： 返回的网页链接中包含第一个关键字，后面的关键字则出现在链接中或者网页文档中。 "inurl:" 后面不能有空格， Google 也不对 URL 符号如 「/」 进行搜索。 Google 对 「cgi-bin/phf」 中的 「/」 当成空格处理。
- allinurl： 返回的网页的链接中包含所有查询关键字。这个查询的对象只集中于网页的链接字符串。
- allintitle和intitle的用法类似于上面的allinurl和inurl，只是后者对URL进行查询，而前者对网页的标题栏进行查询。
- Google 高级搜索页面： http://www.google.com.hk/advanced_search
- 百度高级搜索页面： http://www.baidu.com/gaoji/advanced.html

## 罕见高级搜索语法

- related： 搜索结构内容方面相似的网页。
- cache： 搜索GOOGLE服务器上某页面的缓存，这个功能同“网页快照”，通常用于查找某些已经被删除的死链接网页，相当于使用普通搜索结果页面中的“网页快照”功能。
- info： 显示与某链接相关的一系列搜索，提供cache、link、related和完全包含该链接的网页的功能。

## 其他重要功能

- 目录服务。 如果不想搜索网页，而是想寻找某些专题网站，可以访问GOOGLE的分类目录“http://directory.google.com/”，中文目录是“http://directory.google.com/Top/World/Chinese_Simplified/”。不过由于GOOGLE的目录由志愿者服务，而GOOGLE在国内名气相对比较小，因此中文目录下收录站点很少。

- 工具条。 为了方便搜索者，GOOGLE提供了工具条，集成于浏览器中，用户无需打开GOOGLE主页就可以在工具条内输入关键字进行搜索。此外，工具条还提供了其他许多功能，如显示页面PageRank等。最方便的一点在于用户可以快捷的在GOOGLE主页、目录服务、新闻组搜索、高级搜索和搜索设定之间切换。欲安装GOOGLE的工具条，可以访问“http://toolbar.google.com/”，按页面提示可以自动下载并安装。

- 新闻组（USENET）搜索。 新闻组中有大量的有价值信息，DEJA一直是新闻组搜索引擎中的佼佼者。2001年2月份，GOOGLE将DEJA收购并提供了所有DEJA的功能。现在，除了搜索之外，GOOGLE还支持新闻组的WEB方式浏览和张贴功能。

  输入“http://groups.google.com/”后，便进入GOOGLE新闻组界面。可惜现在还没有中文界面。因为新闻组中的帖子实在是多，所以我点击“Advaced Groups Search”进入高级搜索界面[http://groups.google.com/advanced_group_search](http://groups.google.com/advanced_group_search)。新闻组高级搜索界面提供对关键字、新闻组、主题、作者、帖子序号、语言和发布日期的条件搜索。其中作者项指作者发帖所用的唯一识别号电子信箱。比如要在alt.chinese.text内搜索著名老牌网络写手图雅的帖子，可以用下列指令“group:alt.chinese.text author:tuya@ccmail.uoregon.edu”。不过一般而言，我更推荐使用图形搜索界面，方便而且直观。

- 搜索结果翻译。 曾经为那些你不懂的法文、西班牙文页面烦恼么？现在，GOOGLE支持一项搜索结果翻译功能，可以把非英文的搜索结果翻译成英文！！虽然目前只支持有限的拉丁语、法语、西班牙语、德语和葡萄牙文，但是我不得不承认，这是个伟大的改进。

  不过，目前只能在英文状态GOOGLE下实现这个功能。进入GOOGLE的设置页面，[http://www.google.com/preferences](http://www.google.com/preferences)，有一个“BETA: Enable translation of search results into your interface language. ”的选项，把它选中，就OK了。

- 搜索结果过滤。 网络上的成人内容浩如烟海，而且很多站点具有欺骗或者其他不良企图，浏览者很容易掉入其中的陷阱。为此，GOOGLE新设立了成人内容过滤功能，见GOOGLE的设置页面，[http://www.google.com/preferences](http://www.google.com/preferences)，最底下有一个选项SafeSearch Filtering。不过，中文状态下的GOOGLE尚没有这个功能。

- 图像文档搜索。 GOOGLE提供了Internet上图像文件的搜索功能！！目前该功能尚在B测试阶段，但已经非常好用。访问地址是“images.google.com”。你可以在关键字栏位内输入描述图像内容的关键字，如“britney spears”，也可以输入描述图像质量或者其他属性的关键字，如“high quality”。

  GOOGLE给出的搜索结果具有一个直观的缩略图（THUMBNAIL），以及对该缩略图的简单描述，如图像文件名称，以及大小等。点击缩略图，页面分成两祯，上祯是图像之缩略图，以及页面链接，而下祯，则是该图像所处的页面。屏幕右上角有一个“Remove Frame”的按钮，可以把框架页面迅速切换到单祯的结果页面，非常方便。GOOGLE还提供了对成人内容图像的限制功能，可以让搜索者免受不必要的骚扰。

  不过，非常遗憾的是，图像搜索功能还不支持中文。