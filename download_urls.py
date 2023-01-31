import requests
import re
import os
from tqdm import trange


def download_imgs(base_url, folder_name):
    # base_url = '2048'
    folder = 'src/books/' + f'{folder_name}'
    os.makedirs(folder, exist_ok=True)

    res = requests.get(url=base_url)
    image_urls = re.findall('"https://.*?"', res.text)

    num = len(image_urls)
    for i in trange(num):
        url = image_urls[i][1:-1].replace('&#46;', '.')
        if '.jpg' not in url:
            continue

        file_name = f'{folder}/content_{i:0>3}.jpg'
        res = requests.get(url=url)
        with open(file_name, 'wb') as f:
            f.write(res.content)


def find_urls(base_url):
    # base_url = 'rule34video'
    requests.packages.urllib3.disable_warnings()
    res = requests.get(url=base_url, verify=False)
    video_urls = re.findall('"https://rule34video.com/get_file.*?"', res.text)

    num = 0
    video_path = []
    for urls in video_urls:
        if 'download' in urls:
            url = urls[1:-1]
            index = list(re.search('.mp4', url).span())[0]
            ans = url[:index + len('.mp4')]
            video_path.append(ans)
            print(f'{num}: {ans}')
            num += 1
    return base_url[:-1].split('/')[-1], video_path


def download_videos(base_url):
    file_name, urls = find_urls(base_url)
    # index = int(input("Please Input Choice Number: "))
    # if index < 0 or index > len(urls):
    #     return
    index = len(urls) - 1

    output_path = r"src\rule34video"
    url = urls[index]
    run = f"yt-dlp.exe -P {output_path} -o {file_name}.mp4 {url}"

    # cmd = f"you-get -o {output_path} -O {file_name} {url}"
    print(run)
    os.system(run)


if __name__ == '__main__':
    """
    urls:
    
    """

    addr = [
        "https://rule34video.com/",
        
    ]

    for i in range(len(addr)):
        root_url = addr[i]

        project_name = ""

        if project_name != "":
            download_imgs(root_url, project_name)
        else:
            download_videos(root_url)

    print('Done.')
