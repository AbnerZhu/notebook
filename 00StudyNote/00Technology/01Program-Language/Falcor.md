# Falcor



**Feature**

- One Model Everywhere
- The Data is the API
- Bind to the Cloud



为了提供通信的效率

- 缓冲： 把请求的数据暂存在本地。 下次同样的请求就可以直接从本地获取， 大大减少通信量和响应时间
- 打包： 负责把若干小的请求汇集为一个大的情趣， 可以大大提高有效载荷的比例
- 去重： 对请求进行过滤， 去除不必要的请求

