# 第三章 模板-Jinja模板语法在flask里的应用

## 三种定界符

### 1. if,for等语句
{% if ... %} 
{% else %}
{% endif %}

{% for ... %}
{% endfor %}


### 2. 字符串、变量、函数调用
{{ ... }}


### 3. HTML模板注释
{# ... #}

## 内置全局函数
range([start,]stop[,step])
lipsum(n=5,html=True,min=20,max=100)
dict(**items)


## Flask全局函数
1.render_template       渲染模板 <br/>
2.url_for               用于生成URL <br/>
3.get_flashed_messages  获取flash消息 <br/>


## 自定义全局函数
@app.template_global()


## 内置过滤器
### title
### length
[参考链接](http://jinja.pocoo.org/docs/2.10/templates/#builtin-filters) 


## 自定义过滤器
@app.template_filter()


## 内置测试器
[参考链接](http://jinja.pocoo.org/docs/2.10/templates/#list-of-builtin-tests) 

## 自定义测试器
@app.template_test()
Enviroment类的属性和方法说明: [参考链接](http://jinja.pocoo.org/docs/2.10/api/#jinja2.Enviroment)


## 宏
宏默认代码文件: macros.html 或 _macros.html
在html模板中使用宏

## 基模板和块
默认基模板文件: base.html 或 layout.html
块的修饰符: 
<p>{% block head %} ... {% endblock %}</p> 
<p>{% block title %} ... {% endblock %}</p> 
<p>{% block content %} ... {% endblock %}</p> 
<p>{% block footer %} ... {% endblock %}</p> 
<p>{% block scripts %} ... {% endblock %}</p> 




