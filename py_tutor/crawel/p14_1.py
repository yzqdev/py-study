import urllib.request

response = urllib.request.urlopen("https://upload-bbs.miyoushe.com/upload/2021/06/17/287295887/b20dcc656b17d2ea88e6744210b40d61_7207833840047262272.jpg")
cat_img = response.read()

if __name__ == '__main__':
    with open(r'../dist/aaa', 'wb') as f:
        f.write(cat_img)
        print("生成完毕")
