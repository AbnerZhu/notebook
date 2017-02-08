# Nginx

## 简介

Nginx 做为 HTTP 服务器， 有以下几项基本特性：

- 处理静态文件， 索引文件以及自动索引； 打开文件描述符缓冲。
- 无缓存的反向代理加速， 简单的负载均衡和容错
- FastCGI， 简单的负载均衡和容错
- 模块化的结构。 包括“gzipping, byte ranges, chunked responses,以及 SSI-filter 等 filter。如果由 FastCGI 或其它代理服务器处理单页中存在的多个 SSI，则这项处理可以并行运行，而不需要相互等待。
- 支持 SSL 和 TLSSNI

