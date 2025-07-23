![JiYuKiller.ico](https://github.com/Level3R/JiYuKiller/blob/main/JiYuKiller.ico "JiYuKiller")
# **JiYuKiller**
**JiYuKiller** 是一个能帮你在信息课上畅玩电脑的程序。
## 适用系统及版本
- **Windows 7 及以上**
## 原理
- **JiYuKiller** 会在获取管理员权限后通过运行 **[PowerShell](https://microsoft.com/powershell/)** 命令结束/运行 **StudentMain.exe** ，从而使教师机无法监控学生机。所以在某些删除了学生机 **taskkill.exe** 的学校（比如说我所在的学校）上依然可以起效。
## 使用方法
- 将拷有 **JiYuKiller.exe** 的 U盘/硬盘 插到学生机上;
- 运行 **JiYuKiller.exe**;
- 点击“我已知晓且同意该声明”按钮;
- 根据各按钮上的悬浮提示运行功能。
## 常见问题
- Q：学生机被限制插入 U盘/硬盘 ，怎么运行 **JiYuKiller** 呢?
- A：请参考 **[JiYuTrainer](https://github.com/imengyu/JiYuTrainer/)** 的 **一些提示** 。
- Q：学生机的 **PowerShell** 也被删掉了怎么办？
- A：可在 **[这里](https://learn.microsoft.com/zh-cn/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.5)** 下载 **PowerShell** 。我一般会下载 **ZIP** 文件再将 **pwsh.exe** 添加到学生机 **高级系统设置** 的 **环境变量** 中。
## 开发初衷
- 我们的信息老师会在上课时承诺给我们 5 ~ 10 分钟的“自由”上机时间，但几乎每次都会拖到下课或者让我们做练习（在问卷星上答题）。为了争得我们应有的时间，遂开发本程序。
- 什么？你问我为什么不用 **[JiYuTrainer](https://github.com/imengyu/JiYuTrainer/)** ？因为它的远程注入等功能，只要一启动它就会被未知程序检测到并“蓝屏”（不是那个 **[蓝屏](https://support.microsoft.com/zh-cn/windows/%E8%A7%A3%E5%86%B3-windows-%E4%B8%AD%E7%9A%84%E8%93%9D%E5%B1%8F%E9%94%99%E8%AF%AF-60b01860-58f2-be66-7516-5c45a66ae3c6)** ）且无法使用（除非重启）。
## 其他
- 欢迎各位大佬参与到 **JiYuKiller** 的开发当中。
## 许可证
- 目前本项目基于 **[MIT协议](https://mit-license.org/)** 开源（致敬 **[imengyu](https://github.com/imengyu/)** 大佬的 **[JiYuTrainer](https://github.com/imengyu/JiYuTrainer/)**）。

P.S.这是我发布的第一个开源项目，很多东西还不明白，如有不足还请指出。喜欢的话，请给个 **Star** 吧。
