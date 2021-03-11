import requests, os
from bs4 import BeautifulSoup
from PIL import Image

dirname = os.path.dirname(__file__)

urls = ['url-string', 'url-string']


def scrape_img(url_dir):
    loop = 0
    imgs = soup.find_all('img')
    for img in imgs:
        loop += 1
        try:
            print('Downloading...')
            img_src = img['src']
            img_name = img_src.split('/')[-1]
            img_name = img_name.split('?')[0]
            img = Image.open(requests.get(img_src, stream=True).raw)
            img.save(url_dir + img_name)
            print('Save Successful to {}'.format(url_dir))
        except:
            print('SKIPPED IMG')
            pass
        if loop == len(imgs):
            print(
                '================\nCOLLECTION FINISHED\n================\n\n')


def scrape_bg(url_dir):
    loop = 0
    bg_imgs = soup.find_all('a', class_='popup-gallery-link')
    for bg_img in bg_imgs:
        loop += 1
        try:
            print('Downloading BG...')
            bg_img_src = bg_img['href']
            bg_img_name = bg_img_src.split('/')[-1]
            bg_img_name = bg_img_name.split('?')[0]
            bg_img = Image.open(requests.get(bg_img_src, stream=True).raw)
            bg_img.save(url_dir + bg_img_name)
            print('Save Successful of BG to {}'.format(url_dir))
        except:
            print('SKIPPED IMG')
            pass
        if loop == len(bg_imgs):
            print(
                '================\nCOLLECTION FINISHED\n================\n\n')


for i in range(len(urls)):
    r = requests.get(urls[i])
    soup = BeautifulSoup(r.content, 'html.parser')
    split_url = urls[i].split('/')
    # print(len(split_url))
    if (len(split_url) == 6):
        if os.path.exists(
                os.path.join(dirname + '/saved_images/' + split_url[-2])):
            url_dir = os.path.join(dirname + '/saved_images/' + split_url[-2] +
                                   '/')
        else:
            new_dir = os.mkdir(
                os.path.join(dirname + '/saved_images/' + split_url[-2]))
            url_dir = os.path.join(dirname + '/saved_images/' + split_url[-2] +
                                   '/')
    elif (len(split_url) == 7):
        if os.path.exists(
                os.path.join(dirname + '/saved_images/' + split_url[-3])):
            url_dir = os.path.join(dirname + '/saved_images/' + split_url[-3] +
                                   '/')
        else:
            new_dir = os.mkdir(
                os.path.join(dirname + '/saved_images/' + split_url[-3]))
            url_dir = os.path.join(dirname + '/saved_images/' + split_url[-3] +
                                   '/')
    else:
        url_dir = dirname + '/saved_images/'

    scrape_img(url_dir)
    scrape_bg(url_dir)