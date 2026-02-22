import cv2
from ultralytics import YOLO

def main():
    # 加载 YOLOv8 预训练模型（自动下载 if not exists）
    model = YOLO('yolov8n.pt')
    
    # 定义需要保护的隐私类别 ID (COCO数据集)
    # 0: person, 67: cell phone, 73: laptop
    privacy_class_ids = [0, 67, 73]
    
    # 初始化模糊模式，默认为马赛克
    blur_mode = 'mosaic'  # 可选 'mosaic' 或 'gaussian'
    
    # 打开默认摄像头（0）
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("错误：无法打开摄像头")
        return
    
    print("实时隐私保护系统已启动")
    print("按 'm' 切换到马赛克模式")
    print("按 'g' 切换到高斯模糊模式")
    print("按 'q' 退出程序")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("无法获取视频帧")
            break
        
        # 使用 YOLO 进行目标检测
        results = model(frame)
        
        # 处理检测到的目标
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                if class_id in privacy_class_ids:
                    # 获取边界框坐标
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    
                    # 提取目标区域
                    roi = frame[y1:y2, x1:x2]
                    if roi.size == 0:
                        continue
                    
                    # 根据当前模式进行模糊处理
                    if blur_mode == 'mosaic':
                        # 马赛克：先缩小再放大
                        roi = cv2.resize(roi, (10, 10), interpolation=cv2.INTER_LINEAR)
                        roi = cv2.resize(roi, (x2-x1, y2-y1), interpolation=cv2.INTER_NEAREST)
                    else:  # gaussian
                        # 高斯模糊，核大小必须为奇数，且大于等于 (99,99) 以保证明显效果
                        roi = cv2.GaussianBlur(roi, (99, 99), 30)
                    
                    # 将处理后的区域放回原图
                    frame[y1:y2, x1:x2] = roi
        
        # 显示当前模式在画面上
        mode_text = "Mode: Mosaic" if blur_mode == 'mosaic' else "Mode: Gaussian Blur"
        cv2.putText(frame, mode_text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        # 显示画面
        cv2.imshow('Privacy Protection - Press q to quit', frame)
        
        # 检测按键
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('m'):
            blur_mode = 'mosaic'
            print("切换到马赛克模式")
        elif key == ord('g'):
            blur_mode = 'gaussian'
            print("切换到高斯模糊模式")
    
    # 释放资源
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()