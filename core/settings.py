login_api = 'https://passport.liepin.com/c/login.json?__mn__=user_login'
refresh_api = 'https://c.liepin.com/resume/refreshresume.json'
# 登陆猎聘后的PC首页，F12开启，请求一下 【刷新简历】，在network中找到refresh_api的请求。Form Data中有你的res_id_encode
res_id_encode = '6ad0f760M7*****'
# 登陆猎聘的账户名
user_login = '1851******'
# 登陆猎聘的密码
user_pwd = 'hmn52***'
# 刷新多少次简历后重新登陆，默认半个小时。
relogin_interval = 1800