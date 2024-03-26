import os
import cv2
from base_camera import BaseCamera

class Camera(BaseCamera):
    video_source_1 = 'E:/Coding/Js/前端/大屏可视化ECharts/helmet/flask/video_1.mp4'  # 设置你的视频文件路径
    
    def __init__(self):
        super(Camera, self).__init__()

    @staticmethod
    def set_video_source(source):
        Camera.video_source = source

    @staticmethod
    def frames():
        video_path = Camera.video_source
        if not os.path.exists(video_path):
            raise RuntimeError(f'视频文件 {video_path} 不存在。')

        video = cv2.VideoCapture(video_path)
        if not video.isOpened():
            raise RuntimeError(f'无法打开视频文件 {video_path}.')

        while True:
            _, frame = video.read()

            if frame is None:
                # 如果没有帧了，重新开始播放视频
                video.set(cv2.CAP_PROP_POS_FRAMES, 0)
                continue

            # 将帧编码为JPEG格式并返回
            yield cv2.imencode('.jpg', frame)[1].tobytes()
