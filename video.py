import yt_dlp

def download_video(url):
    options = {
        'format': 'bestvideo[height<=1080][vcodec^=avc]+bestaudio[ext=m4a]/best[ext=mp4]',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s'
    }
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    video_url = input("👉 Entre le lien YouTube : ")
    download_video(video_url)
    print("✅ Téléchargement terminé !")
