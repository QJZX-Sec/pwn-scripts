# 一个梳理TP-Link登录逻辑的脚本

## 研究背景

我买了一个带有5GHZ AP发射功能的TP-Link路由器（型号不透露）。为了能够在我的手机上获取同局域网电脑的ip，我尝试实现一个可以获取路由器DHCP在线设备表的函数。第一步需要做的就是梳理路由器的登录认知逻辑，因此本篇分享就开始了。

## 实现逻辑的核心的流程图

> 提示：你可以点击图片跳转链接来尝试查看原图（Github不支持从外链浏览超大图片，图床托管在 [imgbox](imgbox.com)上）.

<a href="https://images2.imgbox.com/63/f0/OxVtPkAv_o.jpg" target="_blank"><img src="https://thumbs2.imgbox.com/63/f0/OxVtPkAv_t.jpg" alt="image host"/></a>

## 总结

不使用标准的加密方案（如AES-256）自己取尝试零基础独创是很不安全的，并且不使用`https`之类的带加密的通信协议会使其更不安全。但另一方面，在这个场景下安全看起来并不是那么重要，毕竟这只是普通的家庭局域网环境。
