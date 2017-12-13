import requests

def check_if_user(user_id, user_pw):
    payload = {
        'user_id': str(user_id),
        'user_pw': str(user_pw)
    }
    with requests.Session() as s:
        s.post('https://nid.naver.com/nidlogin.login', data=payload)
        print('로그인완료')

'''
        if auth.status_code == 200: # 성공적으로 가져올 때
            return True
        else: # 로그인이 실패시
            return False
'''

a = check_if_user('hqpark', '123')
