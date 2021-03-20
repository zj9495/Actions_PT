# Actions_PT

## 适用

NuxusPHP 程序的PT站点，每天自动签到 +魔力

## 使用

添加CONFIG ， Settings > Secrets > New secret > CONFIG

## CONFIG 格式

例子内 所有’#‘后的内容删除 , 不能写注释

````
[
    {
        # 地址
        'url':'https://www.XXX.com', 
        # cookie 执行从浏览器粘贴出来就行，不用处理，包在引号内就行
        'cookie':'XXXXX',
        #执行哪些任务的列表 签到、说谢谢 
        'tasks':['sign_in','say_thanks'] 
	},

    # 如果还有其他站点，把上面的 配置复制一份，
    {
        'url':'https://www.XXX.com', 
        'cookie':'XXXXX',
        'tasks':['sign_in',] 
	}
]
````

## 鸣谢
 
[@wdjoys](https://github.com/wdjoys/pt-tools)
