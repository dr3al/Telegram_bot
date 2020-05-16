import vk_api

token = 'token'

def main():
    vk_session = vk_api.VkApi('login', 'password')
    vk_session.auth()
    domains=['']
    res = []
    aaa = []


    for domain in domains:
        f = open(domain, 'a+')
        f.close()
        vk = vk_session.get_api()
        count = 10
        ids = []
        news = []
        news.append(vk.groups.getById(group_id=domain)[0]['name'])
        text = vk.wall.get(domain=domain, count=count)
        for i in range(count):
            x = text['items'][i]['id']
            ids.append(int(x))
        f = open(domain)
        id = f.read()
        f.close()
        if id == '':
            n = count
        else:
            if int(id) in ids: 
                n = ids.index(int(id))
                if n == 0: 
                    news.append('Ничего нового.')
            else:
                n = count
        f = open(domain, 'w')
        f.write(str(ids[0]))
        f.close()
        for i in range(n-1, -1, -1):
            x = text['items'][i]['text']
            if 'photo' in text['items'][i]['attachments'][0]['type']:
                x+=('\n' + str(text['items'][i]['attachments'][0]['photo']['sizes'][6]['url']))
            elif 'video' in text['items'][i]['attachments'][0]['type']:
                x+='\n [Видео]'
            news.append(x)
        res.append(news)
        
    return res
print(main())
