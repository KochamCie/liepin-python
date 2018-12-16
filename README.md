# liepin
auto refresh your resume

settings.py中以下是需要调整的个人配置项
> 登陆猎聘后的PC首页，F12开启，请求一下 【刷新简历】，在network中找到refresh_api的请求。Form Data中有你的res_id_encode

res_id_encode = '6ad0f760M7*****'
> 登陆猎聘的账户名

user_login = '1851******'
> 登陆猎聘的密码

user_pwd = 'hmn52***'
> 刷新多少次简历后重新登陆，默认半个小时。
relogin_interval = 1800

**运行refreshresume.py**，如果你的python版本是2.*，请使用分之python2。


