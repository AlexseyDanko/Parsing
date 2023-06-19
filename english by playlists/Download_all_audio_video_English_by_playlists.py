from pytube import YouTube
from art import tprint


def download_audio(link=""):
    # tprint('>>Download>>Audio>>function>>start>>', 'small')
    url = YouTube(link)
    audio = url.streams.get_audio_only()
    # tprint('Download process......', 'small')
    audio.download()
    # tprint('>>>File>>>Uploaded>>>')


def main():
    with open('video_urls.txt', 'r') as uriki:
        for link in uriki:
            download_audio(link)


if __name__ == '__main__':
    main()



# def download_video(link=""):
#     # tprint('>>Download>>Video>>function>>start>>', 'small')
#     url = YouTube(link)
#     video = url.streams.get_highest_resolution()
#     # tprint('Download process......', 'small')
#     video.download()
#     # tprint('>>>File>>>Uploaded>>>')
#
#
# def main():
#     with open('video_urls.txt', 'r') as uriki:
#         for link in uriki:
#             download_video(link)
#
#
# if __name__ == '__main__':
#     main()