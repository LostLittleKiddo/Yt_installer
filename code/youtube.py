import os
from pytube import YouTube
from moviepy.editor import AudioFileClip
from pytube import Playlist

def download_audio(url):
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    if stream is not None:
        output_path = stream.download(output_path='music/')
        mp3_path = output_path.replace(".mp4", ".mp3")
        audio = AudioFileClip(output_path)
        audio.write_audiofile(mp3_path)
        audio.close() 
        os.remove(output_path)

def download_playlist_audio(playlist_url):
    playlist = Playlist(playlist_url)
    for url in playlist.video_urls:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_audio_only()
            if stream is not None:
                output_path = stream.download(output_path='music/')
                mp3_path = output_path.replace(".mp4", ".mp3")
                audio = AudioFileClip(output_path)
                audio.write_audiofile(mp3_path)
                audio.close() 
                os.remove(output_path)
        except Exception as e:
            print(f"An error occurred while downloading {yt.title}: {e}")
            continue

def check_download(url):
    if 'playlist?' in url:
        download_playlist_audio(url)
    else:
        download_audio(url)

def download_audio_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for url in urls:
            message = download_audio(url)

if __name__ == "__main__":
    # check_download("https://music.youtube.com/playlist?list=PLhcgruU1AoCQoaJAgcRkL6lUp66B2kPdx&si=pP-owZU2igAWnVRv")
    # download_audio_from_file('urls.txt')
    # download_playlist_audio("https://music.youtube.com/playlist?list=PLhcgruU1AoCQoaJAgcRkL6lUp66B2kPdx&si=MXS8_zF9QMPbEAP4")
    print("ALL Done!")