from pytube import YouTube

def download_video(video_url, output_path):
    try:
        # Baixar vídeo do YouTube
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(file_extension='mp4').first()
        video_stream.download(output_path)

        print(f"Vídeo baixado com sucesso e salvo como {yt.title}.mp4")

    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de URL de vídeo do YouTube
video_url = "https://youtu.be/QkkoHAzjnUs?si=ytUt6nlGoT9SxoKn"

# Pasta de saída para salvar o vídeo baixado
output_path = "videos_youtube"

download_video(video_url, output_path)

