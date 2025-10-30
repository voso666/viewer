# 运动物体检测程序

这个Python程序用于检测视频中的移动人或物体，同时过滤掉小幅随风摆动的树叶或衣服等物体。

## 功能特点

- 使用OpenCV进行实时视频处理
- 通过背景减除技术检测运动物体
- 使用运动稳定性分析过滤掉小幅摆动的物体
- 支持摄像头输入和视频文件输入
- 可视化显示检测结果

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 使用默认摄像头

```bash
python matching.py
```

### 使用视频文件

修改matching.py文件中的最后几行，取消注释并指定视频文件路径：

```python
if __name__ == "__main__":
    # 使用视频文件
    detect_motion("path/to/your/video.mp4")
```

## 参数调整

您可以通过修改`detect_motion`函数的参数来调整检测效果：

- `min_area`: 最小运动区域面积，小于此面积的移动物体将被忽略
- `motion_threshold`: 运动检测阈值，值越大检测越不敏感
- `history_frames`: 用于计算运动稳定性的历史帧数
- `stability_threshold`: 稳定性阈值，值越大要求运动越稳定

例如：

```python
detect_motion(min_area=300, motion_threshold=20, history_frames=15, stability_threshold=0.8)
```

## 操作说明

- 按'q'键退出程序
- 程序会显示两个窗口：原始视频和运动掩码
- 绿色框表示检测到的所有运动区域
- 红色框表示经过稳定性分析后被认为是人或物体的移动区域 