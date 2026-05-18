import os
import subprocess
import sys


def concatenate_videos_with_ffmpeg(directory, output_file):
    """
    使用ffmpeg快速拼接指定文件夹内的所有视频，不进行转码。
    直接合并视频流，保持原始编码格式。

    参数:
    - directory (str): 包含要拼接的视频文件的文件夹路径。
    - output_file (str): 输出视频的文件路径。
    """
    video_files = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.mp4', '.avi', '.mov'))]
    video_files.sort()  # 按文件名的字母顺序排序

    # 创建一个临时文件列表
    with open("temp_list.txt", "w") as f:
        for video in video_files:
            f.write(f"file '{video}'\n")

    # 直接合并所有视频（不重新编码）
    merge_cmd = [
        r".\ffmpeg.exe", 
        "-f", "concat", 
        "-safe", "0", 
        "-i", "temp_list.txt", 
        "-c", "copy",  # 直接复制视频流，不重新编码
        output_file
    ]
    print("正在合并视频...")
    subprocess.call(merge_cmd)

    # 清理临时文件
    os.remove("temp_list.txt")

    print('处理完成！')


if __name__ == "__main__":
    directory = r"E:\marketVideos\20251025_XIUYING"  # 替换成你的视频文件夹路径
    output_file = r"E:\marketVideos\outputs\20251025_XIUYING.mp4"
    concatenate_videos_with_ffmpeg(directory, output_file)
