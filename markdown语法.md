#Markdown语法
##一.标题使用

    #这是一级标题
#这是一级标题
    ##这是二级标题
##这是二级标题
    ###这是三级标题
###这是三级标题
##二.字体

- **加粗**
  要加粗的字体用两个*包起来
- *斜体*
  要斜体的分别用一个*包起来
- ***斜体加粗***
  要斜体加粗的文字分别用三个*包起来
- ~~删除线~~ 
  要加删除线的文字分别用两个~~`英文`包起来
##三.引用

在引用的文字前加>即可。引用也可以嵌套，如加两个>>三个>>>
n个…
示例：
   1. >这是引用的内容
   2. >>这是引用的内容 
##四.分割线

三个或者三个以上的-或者*都可以。
示例：
    ---
    ----
    ***
    ****
效果如下：
  1. ---
  2. ----
  3. ***
  4. *****

##五.图片
语法：
 1. ![图片alt](图片地址 ''图片title'')
 2. 图片alt就是显示在图片下面的文字，相当于对图片内容的解释。
 3. 图片title是图片的标题，当鼠标移到图片上时显示的内容。title可加可不加

代码块：
```markdown
![blockchain](https://s.cn.bing.net/th?id=OHR.HawksbillTurtle_ZH-CN0562063994_1920x1080.webp&qlt=50) 
```
示例：
  1. 效果如下：
   ![blockchain](https://s.cn.bing.net/th?id=OHR.HawksbillTurtle_ZH-CN0562063994_1920x1080.webp&qlt=50) 
##六.超链接
- 语法：
  ```markdown
  [超链接名](超链接地址 "超链接title")
  ```
  title可加可不加
- 效果如下：
  [简书](http://jianshu.com)
  [百度](http://baidu.com)
注：Markdown本身语法不支持链接在新页面中打开，貌似简书做了处理，是可以的。别的平台可能就不行了，如果想要在新页面中打开的话可以用html语言的a标签代替。


 ```markdown
 <a href="超链接地址" target="_blank">超链接名</a>

示例:
<a href="https://www.jianshu.com/u/1f5ac0cf6a8b" target="_blank">简书</a>
 ```
##七.列表
###无序列表
####语法：
无序列表用`- + *`都可以
```markdown
- 列表内容
+ 列表内容
* 列表内容

注意：- + * 跟内容之间都要有一个空格

```
`效果如下：`
1. - 列表内容
2. + 列表内容
3. * 列表内容
###有序列表
####语法：
数字加点：
```markdown
1. 列表内容
2. 列表内容
3. 列表内容

注意：序号跟内容之间要有空格

```
`效果如下：`
1.  列表内容
2.  列表内容
3.  列表内容
##八. 表格
语法：
```markdown
表头|表头|表头
---|:--:|---:
内容|内容|内容
内容|内容|内容

第二行分割表头和内容。
- 有一个就行，为了对齐，多加了几个
文字默认居左
- 两边加：表示文字居中
- 右边加：表示文字居右
注：原生的语法两边都要用 | 包起来。此处省略
```
示例：
```markdown
姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟
```
效果如下：
姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

#九.代码
-  语法：
单行代码：代码之间用一个反引号包起来
```markdown
`代码内容`
```
代码块：
```markdown
(```)
    代码...
    代码...
    代码...
(```)
```
> 注:为了防止转译，前后三个反引号处加了小括号，实际是没有的。这里只是用来演示，实际中去掉两边小括号即可。

单行代码：
```markdown
`create datebase test;`
```
代码块：
```markdown
(```)
function fun(){
         echo "测试代码";
    }
    fun();
(```)
```
效果如下：
单行代码：
`create datebase test;`
代码块：
(```)
function fun(){
         echo "测试代码";
    }
    fun();
(```)
#十.流程图
```markdown
```mermaid
flowchat
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```
```
效果如下：
```mermaid
flowchat
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```



    
   




