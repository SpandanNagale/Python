import requests


def download(url,name):
    response=requests.get(url)
    open(f"C:\\Users\\spand\\Downloads\\ {name}.mp4","wb").write(response.content)



url="https://video.damplips.com/video7/658/34.mp4" #link of your file which you want to download
name="pouhga"
download(url,name)