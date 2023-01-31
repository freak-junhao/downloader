import os


if __name__ == '__main__':
    """
    url:
    
    """

    base_url = [
        "https://cn.pornhub.com/"
    ]

    save_path = r"src/pornhub/"
    for r in base_url:
        run = f"yt-dlp.exe -P {save_path} {r}"
        print(run)
        os.system(run)

    print("Done.")
