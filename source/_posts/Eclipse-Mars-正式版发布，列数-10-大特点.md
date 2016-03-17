---
title: Eclipse Mars 正式版发布，列数 10 大特点
tags: []
date: 2015-06-27 23:48:23
---

代号 Mars 的 Eclipse 4.5 版本发布了，这一版本在 Linux 工具中结合了额外的 Docker 工具，更好地支持 
Maven 和 Gradle （包括对嵌入工具的更新），提升了 Java 8 的特性，并通过 Eclipse Marketplace 支持对 
Java 9 早期访问。主要更新内容有以下几个方面：

*   新 Java IDE 特性， 包括对嵌套的项目层次视图，可自定义 perspectives，并提升了文本搜索的速度。

*   集成的工具，用于建立和维护 Docker 容器，可在 Linux Tools 项目获取.

*   Oomph 项目现在能够跨工作区记录和分享个人偏好设置。

*   &nbsp;Gradle 新的集成，使得更加容易管理 Gradle 构建，通过 Buildship 项目。

*   &nbsp;提升对 Maven 支持，包括支持 Maven 3.3.3, 提升 Maven 原型整合和在 pom 编辑器中的自动完成。

*   自动错误报告，让 Eclipse 用户可以直接报告错误到Eclipse项目。&nbsp;&nbsp;
*   &nbsp;新的 Thym 项目提供了使用 Apache Cordova 创建跨平台移动应用的工具。

下面，是一篇对 Eclipse Mars 的分析文章：

Eclipse Mars 来了！在过去的十天里，我一直在细数最令我兴奋的十个 Eclipse Mars 的特点。想了解最新特性的详细信息，请查看以下链接：

10\. [Mac Application Layout](http://eclipsesource.com/blogs/2015/06/11/mac-application-layout-top-eclipse-mars-feature-10/)
9\. [Platform Improvements](http://eclipsesource.com/blogs/2015/06/12/platform-improvements-top-eclipse-mars-feature-9/)
8\. [UI Monitoring](http://eclipsesource.com/blogs/2015/06/15/ui-monitoring-top-eclipse-mars-feature-8/)
7\. [C/C++ Launching](http://eclipsesource.com/blogs/2015/06/16/cc-launching-top-eclipse-mars-feature-7/)
6\. [e4 Tools](http://eclipsesource.com/blogs/2015/06/17/e4-tools-top-eclipse-mars-feature-6/)
5\. [JDT Improvements](http://eclipsesource.com/blogs/2015/06/18/jdt-improvements-top-eclipse-mars-feature-5/)
4\. [Docker Tools](http://eclipsesource.com/blogs/2015/06/19/docker-tools-top-eclipse-mars-feature-4/)
3\. [Git Flow in Eclipse](http://eclipsesource.com/blogs/2015/06/22/git-flow-top-eclipse-mars-feature-3/)
2\. [Eclipse Automatic Error Reporting](http://eclipsesource.com/blogs/2015/06/23/error-reporting-top-eclipse-mars-feature-2/)

今年 Eclipse Mars 将完全提供一个下载和使用 IDE 新的方法。不用单独下载每个包，Oomph 的 Eclipse 安装包可以提你想要的安装包。

![Screen Shot 2015-06-23 at 9.14.23 PM](http://eclipsesource.com/blogs/wp-content/uploads/2015/06/Screen-Shot-2015-06-23-at-9.14.23-PM.png)

你可以通过“_bundle pool_”在安装程序之间分享 Eclipse 插件。这就意味着如果你安装了其他的包，所有常见的位就会被共享。

![Screen Shot 2015-06-23 at 9.07.21 PM](http://eclipsesource.com/blogs/wp-content/uploads/2015/06/Screen-Shot-2015-06-23-at-9.07.21-PM.png)

一旦 Eclipse 启动，你可以通过走完 Eclipse Welcome Questionnaire 流程来按你的喜好设置 Eclipse。

![Screen Shot 2015-06-23 at 9.09.29 PM](http://eclipsesource.com/blogs/wp-content/uploads/2015/06/Screen-Shot-2015-06-23-at-9.09.29-PM.png)

除
了提供 IDE 给你，Oomph 还能安装你的工作空间。这就是说可以从 Git 中复制项目，配置你的目标平台，初始化项目设置等等。一旦 
Eclipse 启动，选择 File -&gt; Import -&gt; Oomph -&gt; Projects 进入 
Workspace。几个 Eclipse 项目已经配置好并且可以一键安装。

![Screen Shot 2015-06-23 at 9.22.59 PM](http://eclipsesource.com/blogs/wp-content/uploads/2015/06/Screen-Shot-2015-06-23-at-9.22.59-PM.png)

Oomph 甚至提供工具帮你创作自己的安装文件。

![Screen Shot 2015-06-23 at 9.58.12 PM](http://eclipsesource.com/blogs/wp-content/uploads/2015/06/Screen-Shot-2015-06-23-at-9.58.12-PM.png)

Oomph 的 Eclipse 安装器可以让安装，配置，分享 Eclipse 项目变得更容易。如果你是名使用者，你能从简单的安装过程中受益。如果你是位贡献者，你也能轻松设置你的工作空间；如果你是提交者，你可以创建配置文件，帮助他人获取你的项目。想获得最新 Eclipse Mars，可[点击此处下载](http://www.eclipse.org/downloads/installer.php)，或者选择你[最喜欢的安装包](http://www.eclipse.org/downloads/)。

想获得更多有关 Eclipse Mars 的信息，请关注 [Eclipse 官网](http://www.eclipse.org/)。