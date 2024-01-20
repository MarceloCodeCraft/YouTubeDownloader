from pytube import YouTube
from moviepy.editor import VideoFileClip

def download_and_adjust_video(video_url, output_path, target_aspect_ratio=None, start_time=None, end_time=None):
    try:
        # Baixar vídeo do YouTube
        yt = YouTube(video_url)
        video_stream = yt.streams.filter(file_extension='mp4').first()
        video_stream.download(output_path)

        # Criar nome de arquivo para o vídeo baixado
        video_file = f"{output_path}/{yt.title}.mp4"

        # Carregar o vídeo usando moviepy
        clip = VideoFileClip(video_file)

        # Ajustar o vídeo para a proporção desejada
        if target_aspect_ratio is not None:
            original_width, original_height = clip.size
            target_width = int(original_height * target_aspect_ratio)

            # Verificar se o vídeo já tem a largura desejada ou maior
            if original_width < target_width:
                clip = clip.crop(x_center=original_width // 2, y_center=original_height // 2, width=target_width, height=original_height)

        # Cortar o vídeo se start_time e end_time estiverem definidos
        if start_time is not None and end_time is not None:
            clip = clip.subclip(start_time, end_time)

        # Salvar o vídeo ajustado
        clip.write_videofile(f"{output_path}/{yt.title}_adjusted.mp4", codec="libx264", audio_codec="aac", fps=30)

        print(f"Vídeo ajustado e salvo como {yt.title}_adjusted.mp4")

    except Exception as e:
        print(f"Erro: {e}")

# Exemplo de URL de vídeo do YouTube
video_url = "https://youtu.be/bON-KPiiNCk?si=RLYB73EdRRR2nwc1"

# Pasta de saída para salvar o vídeo baixado
output_path = "videos_youtube"

# Proporção desejada (exemplo: 9:16)
target_aspect_ratio = 9 / 16

# Adicione start_time e end_time se quiser cortar o vídeo
start_time = 1  # Substitua por segundos de início desejado
end_time = 15 # Substitua por segundos de término desejado

download_and_adjust_video(video_url, output_path, target_aspect_ratio, start_time, end_time)
