# flask用法
```shell
$ export FLASK_APP=hello.py
$ flask run

```


## windows下
```shell

PS C:\path\to\app> $env:FLASK_APP = "hello.py"
PS C:\path\to\app> flask run

```


Swagger是一款Restful接口的文档在线自动生成+功能测试功能软件
当下支持 Flask 和 Swagger 的工具大概如下：
```text
flask-swagger
flasgger
flask-restplus
```
综合比较了一下，flask-restplus 对框架入侵较大， flask-swagger 集成 Swagger-UI比较繁琐，故尝试使用 flasgger
 