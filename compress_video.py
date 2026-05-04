import subprocess
import os


def compress_video(input_file, output_file, crf=28, preset="medium"):
    """
    Compress video using FFmpeg

    crf: 18-28 (lower = better quality, larger file size)
    preset: affects speed/compression ratio (ultrafast, fast, medium, slow, veryslow)
    """

    command = [
        "ffmpeg",
        "-i", input_file,
        "-vcodec", "libx264",
        "-crf", str(crf),
        "-preset", preset,
        "-acodec", "aac",
        "-b:a", "128k",
        "-movflags", "+faststart",
        output_file
    ]

    subprocess.run(command, check=True)


if __name__ == "__main__":
    input_video = "./predict_runs/video_predict_gpu/video.avi"
    output_video = "./predict_runs/video_predict_gpu/compressed.mp4"

    if not os.path.exists(input_video):
        print("File not found")
    else:
        compress_video(input_video, output_video)
        print("Done!")
