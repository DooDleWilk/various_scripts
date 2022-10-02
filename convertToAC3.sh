ffmpeg -i VideoFile.mkv -map 0 -vcodec copy -scodec copy -acodec ac3 -b:a 640k VideoFile-AC3.mkv
