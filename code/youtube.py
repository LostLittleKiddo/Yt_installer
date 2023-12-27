import os
from pytube import YouTube
from moviepy.editor import AudioFileClip



def download_audio(url):
        yt = YouTube(url)
        stream = yt.streams.get_audio_only()
        if stream is not None:
            output_path = stream.download(output_path='music/playlist')
            mp3_path = output_path.replace(".mp4", ".mp3")
            audio = AudioFileClip(output_path)
            audio.write_audiofile(mp3_path)
            os.remove(output_path)

def download_audio_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            message = download_audio(url)

if __name__ == "__main__":
    download_audio_from_file('urls.txt')
    current_folder = os.getcwd()
    print(current_folder)
    print("ALL Done!")