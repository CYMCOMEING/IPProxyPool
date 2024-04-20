import os
import configparser

# 项目根目录
root_path = os.path.abspath(os.getcwd())

# 日志文件
log_path = os.path.join(root_path, 'log', 'main.log')
if not os.path.exists(os.path.dirname(log_path)):
    os.makedirs(os.path.dirname(log_path))

# 加载config.ini
config_ini_file = os.path.join(root_path, 'configs', 'config.ini')
configer = configparser.ConfigParser()
configer.read(config_ini_file)

MONGODB = {'host': '127.0.0.1',
           'port': 27017}

REDIS = {'host': '127.0.0.1',
         'port': 6379}

MYSQL = {'host': '127.0.0.1',
         'port': 3307,
         'user': 'root',
         'password': '123456',
         'db': 'myflask',
         'charset': 'utf8'}

HEADER = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'Accept-Language': 'zh-CN,zh;q=0.9',
          'Cache-Control': 'no-cache',
          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}


COOKIES_KUAIDILI = {
    'channelid': 'bdtg_a12_a12a1',
    'sid': '1681793618763678',
    '_gcl_au': '1.1.2021864452.1681793618',
    'Hm_lvt_e0cc8b6627fae1b9867ddfe65b85c079': '1681793618',
    '_ga': 'GA1.2.1509062306.1681793620',
    '_gid': 'GA1.2.1967780062.1681793620',
    'Hm_lpvt_e0cc8b6627fae1b9867ddfe65b85c079': '1681898835',
    '_gat': '1',
}

HEADER_KUAIDILI = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'channelid=bdtg_a12_a12a1; sid=1681793618763678; _gcl_au=1.1.2021864452.1681793618; Hm_lvt_e0cc8b6627fae1b9867ddfe65b85c079=1681793618; _ga=GA1.2.1509062306.1681793620; _gid=GA1.2.1967780062.1681793620; Hm_lpvt_e0cc8b6627fae1b9867ddfe65b85c079=1681898835; _gat=1',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}


COOKIES_66IP = {
    'Hm_lvt_1761fabf3c988e7f04bec51acd4073f4': '1681894047',
    'Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4': '1681894420',
}

HEADER_66IP = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'Hm_lvt_1761fabf3c988e7f04bec51acd4073f4=1681894047; Hm_lpvt_1761fabf3c988e7f04bec51acd4073f4=1681894420',
    'Pragma': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

COOKIES_BAIDU = {
    'BIDUPSID': 'C6B06B4F9BDEB31BDF905B8388975219',
    'PSTM': '1537419878',
    '__yjs_duid': '1_16cd3ed3ff36ea15f188225f40a83a2c1619608145649',
    'BDUSS': '5zaHF2cm14QVVvd1lKazhuZ1ZnUjZwMEZFRUx5ZnhXMjFoRGlRZk95UzBBMXBpSVFBQUFBJCQAAAAAAAAAAAEAAAB7z80KYTY0NjU5ODg5MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALR2MmK0djJifn',
    'BDUSS_BFESS': '5zaHF2cm14QVVvd1lKazhuZ1ZnUjZwMEZFRUx5ZnhXMjFoRGlRZk95UzBBMXBpSVFBQUFBJCQAAAAAAAAAAAEAAAB7z80KYTY0NjU5ODg5MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALR2MmK0djJifn',
    'BD_UPN': '12314753',
    'BAIDUID': 'F9CD59FD9A8A67EBD7BE76BE4EF37DC4:FG=1',
    'MCITY': '-104%3A198%3A',
    'BDSFRCVID': '8t_OJeC62CjlTlJfhmRfMZ3lWRN1TM6TH6aoG6wJMlobMr5hf-mYEG0PEf8g0KubJ2MRogKK3gOTHlkF_2uxOjjg8UtVJeC6EG0Ptf8g0f5',
    'H_BDCLCKID_SF': 'tbufVI8af-3bfTrlMtT0M-QH-UnLqhQtJgOZ0l8KtD0bS4QvhPjDbx73XJCe2pc-We7C2IQmWIQthpnIKlJEQtCzMbo3W6tO3254KKJxLpCWeIJo5Dc5-t53hUJiB5JMBan7WnvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC86j6tWe5cLepbJK4oLHDbhQJ55aIL-M6rnh6Rq2fKgyxomtjjm-6Ql2nrD2IKVqq6LDp5qXJIPK4RqLUkq5JAL3tPbQnRRHqb5K5bBQ4CIQttjQpOhfIkjahQzbnONfb7TyU45bU47yMvW0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OhJRLeoKDhJC-bhKvF-t7M5bOH2x7024oHbC6XBJTqajrjDnCrDjQNXUI8LNDHbJ5HLmv90JnXLhbYoCO-QUvSjx4q-RO7ttoyfgnDLRnEBp6mKqo5LJ6fefL1Db3GhTvMtg3t3foSJfboepvoDPJc3MkjMPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbADoCK2JKt3jRjd5bO2qRIJMfcKbJQKaDQ03Ru8Kb7VbIbhLfnkbfJBDl5qbqoxBKc3_qchBxF5DM3Gh5jcM4D7yajK25vR-6T3WlRzLT6ISpjub5rpQT8rLlAOK5OibCrNBIQmab3vOIOTXpO1h-PzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjDjJRCOoI--f-3bfTrc5tQEb-_thMuX5-RLfbbJMh7F5l8-hlOFhhOSy4KJhJ5hWlIeaNvN2DjmBCQxOKQphUt-5UIIhMnaWRDt2IFLWxTN3KJmsJL9bT3v5tDpD4cN2-biWb7M2MbdanvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe4bK-Tr3jHLttMK',
    'BAIDUID_BFESS': 'F9CD59FD9A8A67EBD7BE76BE4EF37DC4:FG=1',
    'BDSFRCVID_BFESS': '8t_OJeC62CjlTlJfhmRfMZ3lWRN1TM6TH6aoG6wJMlobMr5hf-mYEG0PEf8g0KubJ2MRogKK3gOTHlkF_2uxOjjg8UtVJeC6EG0Ptf8g0f5',
    'H_BDCLCKID_SF_BFESS': 'tbufVI8af-3bfTrlMtT0M-QH-UnLqhQtJgOZ0l8KtD0bS4QvhPjDbx73XJCe2pc-We7C2IQmWIQthpnIKlJEQtCzMbo3W6tO3254KKJxLpCWeIJo5Dc5-t53hUJiB5JMBan7WnvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC86j6tWe5cLepbJK4oLHDbhQJ55aIL-M6rnh6Rq2fKgyxomtjjm-6Ql2nrD2IKVqq6LDp5qXJIPK4RqLUkq5JAL3tPbQnRRHqb5K5bBQ4CIQttjQpOhfIkjahQzbnONfb7TyU45bU47yMvW0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OhJRLeoKDhJC-bhKvF-t7M5bOH2x7024oHbC6XBJTqajrjDnCrDjQNXUI8LNDHbJ5HLmv90JnXLhbYoCO-QUvSjx4q-RO7ttoyfgnDLRnEBp6mKqo5LJ6fefL1Db3GhTvMtg3t3foSJfboepvoDPJc3MkjMPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbADoCK2JKt3jRjd5bO2qRIJMfcKbJQKaDQ03Ru8Kb7VbIbhLfnkbfJBDl5qbqoxBKc3_qchBxF5DM3Gh5jcM4D7yajK25vR-6T3WlRzLT6ISpjub5rpQT8rLlAOK5OibCrNBIQmab3vOIOTXpO1h-PzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjDjJRCOoI--f-3bfTrc5tQEb-_thMuX5-RLfbbJMh7F5l8-hlOFhhOSy4KJhJ5hWlIeaNvN2DjmBCQxOKQphUt-5UIIhMnaWRDt2IFLWxTN3KJmsJL9bT3v5tDpD4cN2-biWb7M2MbdanvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe4bK-Tr3jHLttMK',
    'delPer': '0',
    'BD_CK_SAM': '1',
    'BD_HOME': '1',
    'BA_HECTOR': 'ak00al00250la4050404840h1i3vb7c1m',
    'ZFY': 'xp8OHMUHw5T4fd0aZw7vBwQ5MVCbBljWDpt8Kc:BtXbw:C',
    'BDRCVFR[feWj1Vr5u3D]': 'I67x6TjHwwYf0',
    'sugstore': '1',
    'baikeVisitId': 'bf162b50-18f3-464e-b674-29ebd0821a40',
    'PSINO': '1',
    'H_PS_PSSID': '38515_36543_38470_38368_38468_38486_37933_37709_38356_26350_38185',
    'COOKIE_SESSION': '62232_0_9_9_45_7_0_0_9_1_0_0_62158_0_4_0_1681956205_0_1681956201%7C9%231021_360_1681793615%7C9',
    'BDORZ': 'B490B5EBF6F3CD402E515D22BCDA1598',
}

HEADER_BAIDU = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'BIDUPSID=C6B06B4F9BDEB31BDF905B8388975219; PSTM=1537419878; __yjs_duid=1_16cd3ed3ff36ea15f188225f40a83a2c1619608145649; BDUSS=5zaHF2cm14QVVvd1lKazhuZ1ZnUjZwMEZFRUx5ZnhXMjFoRGlRZk95UzBBMXBpSVFBQUFBJCQAAAAAAAAAAAEAAAB7z80KYTY0NjU5ODg5MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALR2MmK0djJifn; BDUSS_BFESS=5zaHF2cm14QVVvd1lKazhuZ1ZnUjZwMEZFRUx5ZnhXMjFoRGlRZk95UzBBMXBpSVFBQUFBJCQAAAAAAAAAAAEAAAB7z80KYTY0NjU5ODg5MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALR2MmK0djJifn; BD_UPN=12314753; BAIDUID=F9CD59FD9A8A67EBD7BE76BE4EF37DC4:FG=1; MCITY=-104%3A198%3A; BDSFRCVID=8t_OJeC62CjlTlJfhmRfMZ3lWRN1TM6TH6aoG6wJMlobMr5hf-mYEG0PEf8g0KubJ2MRogKK3gOTHlkF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tbufVI8af-3bfTrlMtT0M-QH-UnLqhQtJgOZ0l8KtD0bS4QvhPjDbx73XJCe2pc-We7C2IQmWIQthpnIKlJEQtCzMbo3W6tO3254KKJxLpCWeIJo5Dc5-t53hUJiB5JMBan7WnvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC86j6tWe5cLepbJK4oLHDbhQJ55aIL-M6rnh6Rq2fKgyxomtjjm-6Ql2nrD2IKVqq6LDp5qXJIPK4RqLUkq5JAL3tPbQnRRHqb5K5bBQ4CIQttjQpOhfIkjahQzbnONfb7TyU45bU47yMvW0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OhJRLeoKDhJC-bhKvF-t7M5bOH2x7024oHbC6XBJTqajrjDnCrDjQNXUI8LNDHbJ5HLmv90JnXLhbYoCO-QUvSjx4q-RO7ttoyfgnDLRnEBp6mKqo5LJ6fefL1Db3GhTvMtg3t3foSJfboepvoDPJc3MkjMPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbADoCK2JKt3jRjd5bO2qRIJMfcKbJQKaDQ03Ru8Kb7VbIbhLfnkbfJBDl5qbqoxBKc3_qchBxF5DM3Gh5jcM4D7yajK25vR-6T3WlRzLT6ISpjub5rpQT8rLlAOK5OibCrNBIQmab3vOIOTXpO1h-PzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjDjJRCOoI--f-3bfTrc5tQEb-_thMuX5-RLfbbJMh7F5l8-hlOFhhOSy4KJhJ5hWlIeaNvN2DjmBCQxOKQphUt-5UIIhMnaWRDt2IFLWxTN3KJmsJL9bT3v5tDpD4cN2-biWb7M2MbdanvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe4bK-Tr3jHLttMK; BAIDUID_BFESS=F9CD59FD9A8A67EBD7BE76BE4EF37DC4:FG=1; BDSFRCVID_BFESS=8t_OJeC62CjlTlJfhmRfMZ3lWRN1TM6TH6aoG6wJMlobMr5hf-mYEG0PEf8g0KubJ2MRogKK3gOTHlkF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tbufVI8af-3bfTrlMtT0M-QH-UnLqhQtJgOZ0l8KtD0bS4QvhPjDbx73XJCe2pc-We7C2IQmWIQthpnIKlJEQtCzMbo3W6tO3254KKJxLpCWeIJo5Dc5-t53hUJiB5JMBan7WnvIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtnLhbC86j6tWe5cLepbJK4oLHDbhQJ55aIL-M6rnh6Rq2fKgyxomtjjm-6Ql2nrD2IKVqq6LDp5qXJIPK4RqLUkq5JAL3tPbQnRRHqb5K5bBQ4CIQttjQpOhfIkjahQzbnONfb7TyU45bU47yMvW0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OhJRLeoKDhJC-bhKvF-t7M5bOH2x7024oHbC6XBJTqajrjDnCrDjQNXUI8LNDHbJ5HLmv90JnXLhbYoCO-QUvSjx4q-RO7ttoyfgnDLRnEBp6mKqo5LJ6fefL1Db3GhTvMtg3t3foSJfboepvoDPJc3MkjMPjdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtbADoCK2JKt3jRjd5bO2qRIJMfcKbJQKaDQ03Ru8Kb7VbIbhLfnkbfJBDl5qbqoxBKc3_qchBxF5DM3Gh5jcM4D7yajK25vR-6T3WlRzLT6ISpjub5rpQT8rLlAOK5OibCrNBIQmab3vOIOTXpO1h-PzBN5thURB2DkO-4bCWJ5TMl5jDh3Mb6ksDMDtqjDjJRCOoI--f-3bfTrc5tQEb-_thMuX5-RLfbbJMh7F5l8-hlOFhhOSy4KJhJ5hWlIeaNvN2DjmBCQxOKQphUt-5UIIhMnaWRDt2IFLWxTN3KJmsJL9bT3v5tDpD4cN2-biWb7M2MbdanvP_IoG2Mn8M4bb3qOpBtQmJeTxoUJ25DnJhbLGe4bK-Tr3jHLttMK; delPer=0; BD_CK_SAM=1; BD_HOME=1; BA_HECTOR=ak00al00250la4050404840h1i3vb7c1m; ZFY=xp8OHMUHw5T4fd0aZw7vBwQ5MVCbBljWDpt8Kc:BtXbw:C; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; sugstore=1; baikeVisitId=bf162b50-18f3-464e-b674-29ebd0821a40; PSINO=1; H_PS_PSSID=38515_36543_38470_38368_38468_38486_37933_37709_38356_26350_38185; COOKIE_SESSION=62232_0_9_9_45_7_0_0_9_1_0_0_62158_0_4_0_1681956205_0_1681956201%7C9%231021_360_1681793615%7C9; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}