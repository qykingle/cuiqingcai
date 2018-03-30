# 崔庆才-网络爬虫实战代码
## 猫眼电影TOP100
使用的技术：python3, requests, re, json, pool

`注意`:需要为请求添加headers，不然会禁止访问.
部分运行结果：
```python
{"index": "1", "image": "http://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c", "title": "霸王别姬", "actor": "张国荣,张丰毅,巩俐", "time": "1993-01-01(中国香港)", "score": "9.6"}
{"index": "2", "image": "http://p0.meituan.net/movie/__40191813__4767047.jpg@160w_220h_1e_1c", "title": "肖申克的救赎", "actor": "蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿", "time": "1994-10-14(美国)", "score": "9.5"}
{"index": "3", "image": "http://p0.meituan.net/movie/23/6009725.jpg@160w_220h_1e_1c", "title": "罗马假日", "actor": "格利高利·派克,奥黛丽·赫本,埃迪·艾伯特", "time": "1953-09-02(美国)", "score": "9.1"}
```

