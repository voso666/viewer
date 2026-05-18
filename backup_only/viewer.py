import cv2


def play_video_at_high_speed(video_path, speedup_factor):
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Couldn't open the video file.")
        return

    # 获取视频的帧速率
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    delay = int(1000 / (fps * speedup_factor))  # 以毫秒为单位的延迟

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video Playback', frame)

        # 等待并检查是否按下'q'键来退出播放
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    video_path = r"C:\Users\JGH\Videos\output\xinhuabei_231026.mp4"  # 替换成你的视频文件路径
    speedup_factor = 80  # 修改这里设置不同的加速因子
    play_video_at_high_speed(video_path, speedup_factor)
