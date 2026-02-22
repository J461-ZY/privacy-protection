import cv2
from ultralytics import YOLO
import argparse

def main():
    # 1. 加载官方预训练的YOLOv8模型（无需自己训练）
    model = YOLO('yolov8n.pt')  # 自动下载小巧的纳米模型
    
    # 2. 指定要检测的“隐私类别” (COCO数据集中: 0:person, 67:cell phone, 73:laptop)
    privacy_class_ids = [0, 67, 73]  # 人、手机、笔记本电脑
    
    # 3. 读取输入图片或视频
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, default='input.jpg', help='输入图片路径')
    parser.add_argument('--output', type=str, default='output.jpg', help='输出路径')
    args = parser.parse_args()
    
    img = cv2.imread(args.input)
    if img is None:
        print("错误：无法读取文件。")
        return
    
    # 4. 进行目标检测
    results = model(img)
    
    # 5. 遍历检测结果，对隐私物品打码
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls[0])
            if class_id in privacy_class_ids:  # 如果是隐私类别
                x1, y1, x2, y2 = map(int, box.xyxy[0])  # 获取坐标
                # 对矩形区域打马赛克（像素化）
                roi = img[y1:y2, x1:x2]
                roi = cv2.resize(roi, (10, 10), interpolation=cv2.INTER_LINEAR)
                roi = cv2.resize(roi, (x2-x1, y2-y1), interpolation=cv2.INTER_NEAREST)
                img[y1:y2, x1:x2] = roi
    
    # 6. 保存输出
    cv2.imwrite(args.output, img)
    print(f"处理完成！结果已保存至：{args.output}")
    # 可以同时显示图片（可选）
    cv2.imshow('Privacy Protected', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()