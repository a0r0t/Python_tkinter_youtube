from __future__ import unicode_literals
from pytube import YouTube


def Do_Download(url, savepath, filename):
    yt = YouTube(url)
    yt.streams.get_highest_resolution().download(savepath)