# -*- coding: UTF-8 -*-
import requests
import settings
import time

headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Cookie': 'tlog=1544543160299.27%7C00000000%7C00000000%7C00000000%7C00000000;mscid=00000000;uuid=9DF24360FFA84812400F42CE961DFDB1;abtest=0;fecdn_=1;uuid=1544543161319.07; Hm_lvt_a2647413544f5a04f00da7eee0d5e200=1544543161; e4d43317=ab67306d25f27898e20a7b792b515351; user_kind=0; is_lp_user=true; user_vip=0; user_photo=55557f3b28ee44a8919620ce01a.gif; c_flag=830e070bd4f5f84711456ce967380c04; new_user=false; need_bind_tel=false; gr_user_id=03dc9a1b-72fd-45ca-8da8-79c31bf19191; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id=4bec1761-1cac-43c1-ae6c-841429ada433; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_sid_with_cs1=4bec1761-1cac-43c1-ae6c-841429ada433; bad1b2d9162fab1f80dde1897f7a2972_gr_last_sent_cs1=5f5ed952903bfda71a667e00ad0d9493; bad1b2d9162fab1f80dde1897f7a2972_gr_cs1=5f5ed952903bfda71a667e00ad0d9493; imClientId=ba0a022c3c55153c8bd4766919c3a828; imId=ba0a022c3c55153c0d6d304ef614eb48; grwng_uid=b1ccb101-3a9c-456c-b0ba-487de4de6bc8; bad1b2d9162fab1f80dde1897f7a2972_gr_session_id_4bec1761-1cac-43c1-ae6c-841429ada433=true; fe_c_consultanshow_5f5ed952903bfda71a667e00ad0d9493=1; openChatWin=; verifycode=4ba6e70f460e4336944c888aa47b6956; __session_seq=3; __uv_seq=3; Hm_lpvt_a2647413544f5a04f00da7eee0d5e200=1544543317'
}


def download_file(file_url, name):
    # file_path = file_path.replace('/', '\\')
    r = requests.get(file_url, headers=headers)
    f = open(name, 'wb')
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
    f.close()


def captcha():
    print 'captcha random code............'
    file_name = str(int(time.time()))
    url = settings.captcha_api + file_name
    download_file(url, file_name+'.jpg')


captcha()