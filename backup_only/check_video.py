import cv2
import os

def get_video_info(video_path):
    try:
        if not os.path.exists(video_path):
            print(f"错误：找不到视频文件 {video_path}")
            return
            
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("错误：无法打开视频文件")
            return
            
        # 获取视频的基本信息
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration = frame_count / fps if fps > 0 else 0
        fourcc = int(cap.get(cv2.CAP_PROP_FOURCC))
        codec = "".join([chr((fourcc >> 8 * i) & 0xFF) for i in range(4)])
        
        print(f"视频编码: {codec}")
        print(f"视频分辨率: {width}x{height}")
        print(f"视频时长: {duration:.2f}秒")
        print(f"视频帧率: {fps} fps")
        
        cap.release()
    except Exception as e:
        print(f"获取视频信息时出错: {str(e)}")

if __name__ == "__main__":
    video_path = r"C:\onedrive\python\Viewer\101629_100.mp4"
    get_video_info(video_path) 