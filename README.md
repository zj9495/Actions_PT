# Actions_E5

> 通过官网提供的SDK和GitHub Action 实现自动化调用API [官网SDK地址](https://docs.microsoft.com/zh-cn/graph/sdks/sdk-installation?view=graph-rest-1.0)

> 修改自 [merrycodes](https://github.com/merrycodes/Office-E5) 去掉上传 log 文件至仓库的操作

## 前提：

##### 已经加入了Microsoft 365 开发人员计划 [链接](https://developer.microsoft.com/zh-cn/microsoft-365/dev-program)

## 使用：

1. ##### 登录到Microsoft  Azure [链接](https://portal.azure.com/)

2. ##### 注册新应用，新建客户端密码，跟着图片操作，其中 `1` `2` `3` 要记下来
   

![image-20201220181608269](md_img/image-20201220181608269.png)
    
![image-20201220181906371](md_img/image-20201220181906371.png)
    
![image-20201220182210469](md_img/image-20201220182210469.png)
    
![image-20201220182857805](md_img/image-20201220182857805.png)
    
![image-20201220183358551](md_img/image-20201220183358551.png)
    
![image-20201220183519522](md_img/image-20201220183519522.png)
    
![image-20201220183623883](md_img/image-20201220183623883.png)
    
![image-20201220183801992](md_img/image-20201220183801992.png)
    
![image-20201220183854762](md_img/image-20201220183854762.png)

3. ##### 在GitHub仓库中添加 `secrets`

| name          | secrets                                              | No.  |
| :------------ | :--------------------------------------------------- | :--: |
| CLIENT_ID     | 应用程序(客户端) ID                                  |  1   |
| CLIENT_SECRET | 证书和密码中的"客户端密码"                           |  3   |
| TENANT_GUID   | 目录(租户) ID                                        |  2   |
| USERNAME      | 登录Microsoft Azure的账号(xxxx@xxxx.onmicrosoft.com) |      |
| PASSWORD      | 登录Microsoft Azure的密码                            |      |

## 本地

用 `main.md` 中的代码替换 `Main.class` 中的代码，并把在 `resources` 目录中的 `officeE5.properties` 文件中的值替换成自己的

## 参考链接

[yml文件配置](https://github.com/moreant/auto-checkin-biliob)

[Microsoft Graph SKDK 邮件API](https://docs.microsoft.com/zh-cn/graph/api/message-list-attachments?view=graph-rest-1.0&tabs=http)

## 鸣谢

[merrycodes](https://github.com/merrycodes/Office-E5)
