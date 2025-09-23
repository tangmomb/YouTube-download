# 🎬 Télécharger des vidéos YouTube avec **yt-dlp** et **FFmpeg**

## 1. Installation

⚠️ Attention aux chemins des dossiers lors de l'entièreté du processus.

### a) Télécharger **yt-dlp**

- Téléchargez la dernière version de **yt-dlp.exe** depuis [GitHub](https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#installation).
- Choisissez **yt-dlp.exe** (version standalone pour Windows).
- Placez-le dans un dossier, par exemple :  
  `C:\Users\Documents\dlp-yt`

### b) Télécharger **FFmpeg**

- Téléchargez **FFmpeg** depuis [FFmpeg builds](https://www.gyan.dev/ffmpeg/builds/).
- Sélectionnez la version **essentials build** (fichier zip).
- Décompressez le fichier et notez le chemin du dossier `bin`, par exemple :  
  `C:\Users\Documents\ffmpeg\bin`

---

## 2. Ajouter au **PATH** dans la fenêtre actuelle

1. Pour yt-dlp

```powershell
$env:Path += ";C:\Users\Documents\dlp-yt"
```

2. Pour FFmpeg

```powershell
$env:Path += ";C:\Users\Documents\ffmpeg\bin"
```

---

## 3. Vérifier l’installation

Dans PowerShell, exécutez :

```powershell
yt-dlp --version
ffmpeg -version
```

✅ Si les numéros de version s’affichent, l’installation est correcte.

---

## 4. Pourquoi FFmpeg ?

YouTube, au-delà du 360p, sépare souvent les flux vidéo et audio. **yt-dlp** télécharge les deux, mais **FFmpeg** est nécessaire pour les fusionner en un seul fichier MP4 lisible partout.  
Sans FFmpeg, si vous voulez mieux que du 360p, vous obtiendrez deux fichiers séparés :

- Vidéo : `.webm`
- Audio : `.m4a`

---

## 5. Commandes utiles

### a) Télécharger une vidéo en 1080p H.264

```powershell
yt-dlp -f "bestvideo[height<=1080][vcodec^=avc]+bestaudio[ext=m4a]/best[ext=mp4]" --merge-output-format mp4 -o "$env:USERPROFILE\Downloads\%(title)s.%(ext)s" https://www.youtube.com/watch?v=ID_DE_LA_VIDEO
```

### b) Télécharger une playlist en 1080p H.264 avec numérotation

```powershell
yt-dlp -f "bestvideo[height<=1080][vcodec^=avc]+bestaudio[ext=m4a]/best[ext=mp4]" --merge-output-format mp4 -o "$env:USERPROFILE\Downloads\%(playlist_index)02d - %(title)s.%(ext)s" https://www.youtube.com/playlist?list=ID_DE_LA_PLAYLIST
```

### c) Télécharger avec sous-titres FR intégrés (désactivables, softsubs)

```powershell
yt-dlp -f "bestvideo[height<=1080][vcodec^=avc]+bestaudio[ext=m4a]" --merge-output-format mp4 --sub-langs "fr" --embed-subs -o "$env:USERPROFILE\Downloads\%(title)s.%(ext)s" https://www.youtube.com/watch?v=ID_DE_LA_VIDEO
```

### d) Télécharger avec sous-titres encodés (toujours visibles, hardsubs)

```powershell
yt-dlp -f "bestvideo[height<=1080][vcodec^=avc]+bestaudio[ext=m4a]" --merge-output-format mp4 --sub-langs "fr" --write-subs --convert-subs srt --embed-subs --recode-video mp4 -o "$env:USERPROFILE\Downloads\%(title)s.%(ext)s" https://www.youtube.com/watch?v=ID_DE_LA_VIDEO
```

---

## 6. Résultats

- Les vidéos sont enregistrées dans le dossier de la fenêtre PowerShell.
- Le nom des fichiers est basé sur le titre de la vidéo YouTube, ou avec numérotation + titre pour les playlists.
- Format final : **MP4** (codec vidéo H.264 + audio AAC).
- Sous-titres :
  - **Softsubs** : intégrés et désactivables (ex. dans VLC).
  - **Hardsubs** : encodés et toujours visibles.

---

## 7. Cheat Sheet rapide

### 🎥 Vidéo simple

```powershell
yt-dlp URL
```

### 📺 Playlist avec numérotation (1080p H.264)

```powershell
yt-dlp -f "bestvideo[height<=1080][vcodec^=avc]+bestaudio[ext=m4a]" --merge-output-format mp4 -o "%(playlist_index)02d - %(title)s.%(ext)s" PLAYLIST_URL
```

### 📝 Avec sous-titres FR (softsubs)

```powershell
yt-dlp --sub-langs "fr" --embed-subs URL
```
