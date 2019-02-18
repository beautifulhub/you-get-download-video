
you-get 是一个强大的抓取视频的工具，原理就是上面的swf反编译后抓取了加密方式，然后对网页请求进行一个解析，然后从视屏站服务器中骗取地址出来。

由于这个语言是基于Python的，所以电脑首先需要安装python，然后设置好python的环境变量。详情请查看下面：

1. python下载地址：https://www.python.org/downloads/windows/

2. 下载后直接默认安装

3. 找到python安装地址，并添加到环境变量中。具体操作如下：点击电脑图标右键，选择属性->高级系统设置->环境变量->在系统变量中找到Path变量->然后选择编辑->在变量值这一栏中的末尾，填写英文格式下的分句号“;”->然后粘贴python的安装地址->点击确定->点击确定->点击确定。

4. 然后打开cmd命令（win+R组合键，然后输入cmd，点击运行，就能进入cmd命令），输入以下命令行来安装最新版本的
 you-get pip install --upgrade you-get

5. 然后是下载视频命令行，在cmd中输入下面的代码：（下面的url指的是你想要下载视频的地址，该地址就是打开网页在线视频时，最上面网址栏的地址）
you-get url

更多关于you-get的使用请看： https://www.cnblogs.com/ys-wuhan/p/6057526.htmlyou-get的源代码在
  git://github.com/soimort/you-get.git
  
***[ 另外一个文件是python利用you-get下载批量视频的](https://github.com/xiaowei3223/python-you-get-/blob/master/python%E5%88%A9%E7%94%A8you-get%E4%B8%8B%E8%BD%BD%E6%89%B9%E9%87%8F%E8%A7%86%E9%A2%91.py)***
