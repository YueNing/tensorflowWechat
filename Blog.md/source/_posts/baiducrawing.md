---
title: 百度检索Github Page博客
categories: 
  - 技术
  - 博客
tags:
  - Hexo
abbrlink: 43402
date: 2018-03-15 02:03:13
---

Github Page Hexo博客系统百度无法正确检索到，缺少来自百度的流量。为了解决这个问题，本篇博文记录下自己捣鼓解决这个问题的方法。

### 同时部署到GitHub和Coding

思路：Coding 有和 Github Page 一样的页面功能，只需要将博客系统同时部署在两个平台上，设置博客系统的部署配置每次同时更新到两个地方，然后配置DNS，将国内的流量引到Coding，国外的引到Github Page上即可。

#### 创建Coding账号

#### Linux 下公钥生成

具体参考博文 [ssh-keygen 基本用法](https://www.liaohuqiu.net/cn/posts/ssh-keygen-abc/)
如果已经生成过，跳至下一节

#### 添加公钥到Coding

- 如果已经生成过   `` cat ~/.ssh/id_rsa.pub ``
- 点击头像个人设置，SSH公钥，新建
- 测试成功与否  `` ssh -T git@git.coding.net ``

#### 开启Coding的Page页面功能

返回首页创建新项目，作为个人博客页面，使用用户名作为项目名称，其他默认
创建好后，可以在线添加index.html 页面用于测试用

``` 
<h1> Hello Monkey </h1>
```

选择代码，page页面，选择page页面的分支保存（master）
跳出成功界面，点击域名出现 Hello Monkey 配置成功

### 配置Hexo博客

打开站点配置文件 `` _config.yml ``
找到 `` deploy: ``
修改代码如下，替换用户名和仓库名 

``` 
deploy: 
- type: git
  repo: git@github.com:yuening/yuening.github.io.git
  branch: master
- type: git
  repo: git@git.coding.net:yuening/yuening.git
  branch: master 
```

记得yml的配置格式得有空格

#### 同步博客

执行如下代码

``` 
hexo clean       #清理文件以避免不必要的出错

hexo generate -d

```

现在可以在 ``{user_name}.coding.me`` 看到部署的博客

#### 配置 DNS分流

购买的是namecheap的 ``jumpen.me `` 域名
使用DNSPOD 进行国内外分流，先将域名与 Pages 绑定。Github 是在仓库的根目录下新建一个名为 CNAME 文件，里面写入要绑定域名。coding 是直接在代码-> Pages 服务里配置。接着去 NameCheap 将 Dns 设置为 Custom DNS，并添加 `` f1g1ns1.dnspod.net、f1g1ns2.dnspod.net ``

![Namecheap](https://storage.googleapis.com/ning_picture/namecheap.PNG)

然后配置DNSPOD，国外国内进行分流

![DNSPOD](https://storage.googleapis.com/ning_picture/dnspod.PNG)

#### 百度收录

百度站长之家里添加sitemap，进行抓取测试，可能需要等一段时间才能成功。

![](https://storage.googleapis.com/ning_picture/mainlogo.png)
