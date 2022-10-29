ffmpeg -i input.mp4 -map 0 -c:v libx264 -crf 18 -c:a copy output-h264.mp4
