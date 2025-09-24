import yt_dlp

def get_format(choice):
    """Retourne la commande format en fonction du choix de l'utilisateur"""
    if choice == "1080p":
        return 'bestvideo[height<=1080][vcodec^=avc]+bestaudio[ext=m4a]/best[ext=mp4]'
    elif choice == "720p":
        return 'bestvideo[height<=720][vcodec^=avc]+bestaudio[ext=m4a]/best[ext=mp4]'
    elif choice == "audio":
        return 'bestaudio[ext=m4a]/bestaudio'
    else:
        return 'best'  # par défaut meilleure qualité dispo

def download(url, quality):
    ydl_opts = {
        'format': get_format(quality),
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s'
    }

    # Si c'est une playlist, on ajoute l'index au nom du fichier
    if "playlist" in url.lower():
        ydl_opts['outtmpl'] = '%(playlist_index)02d - %(title)s.%(ext)s'

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    url = input("👉 Entre le lien YouTube (vidéo ou playlist) : ").strip()
    quality = input("🎥 Choisis la qualité (1080p / 720p / audio) : ").strip().lower()
    download(url, quality)
    print("✅ Téléchargement terminé !")
