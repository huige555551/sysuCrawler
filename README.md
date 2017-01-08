# 中山大学研究生微教务系统

##系统介绍
1. 基于flask的python框架写的中山大学研究生微教务系统,之前一直没有时间把界面写出来,知道刚考完试,主要实现了利用ajax与后台
的爬虫机器人交互,利用爬虫机器人模拟登陆的,然后用beatuiful soup对标签进行解析,这里我比较懒,直接把整个table提取出来,
而没有选择逐个td进行获取重新整合,所以还是比较丑,但是基本功能不影响
2. 主要实现了:
- 成绩查询
- 课程查询
- 选课查询
- 个人基本信息查询

3. crawler.py是对之前写的(https://github.com/huige555551/crawler/blob/master/sysu/sysu.py)的结果调用,用flask的template_render()将结果
render出来,写完后对flask框架的基本功能有了一定的了解