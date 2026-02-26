基于 YOLOv8 的实时隐私保护系统

📖 项目简介
本项目利用 YOLOv8 目标检测模型，自动识别摄像头画面中的人脸、手机、电脑等隐私目标，并进行实时模糊处理（支持马赛克/高斯模糊切换），旨在探索计算机视觉在隐私保护和人机交互中的应用。

本人本科专业为网络空间安全，该项目将信息安全中的隐私保护理念拓展到视觉领域，体现了跨学科的思考与实践。

✨ 功能特性
- 🎥 实时摄像头画面处理：调用电脑摄像头，实时检测并保护隐私区域
- 🔄 两种模糊模式：支持马赛克（像素化）和高斯模糊，可通过键盘一键切换
- 🎯 多目标检测：基于 YOLOv8 预训练模型，可识别 person(人)、cell phone(手机)、laptop(笔记本电脑) 等隐私目标
- ⌨️ 交互控制：按 `m` 切换马赛克，按 `g` 切换高斯模糊，按 `q` 退出程序

 🛠️ 技术栈
- Python：核心编程语言
- YOLOv8：目标检测模型
- OpenCV：图像处理与实时视频流
- Git：版本控制

 📋 环境要求
- Python 3.8 或更高版本
- 操作系统：Windows / macOS / Linux（需支持摄像头）

 🚀 快速开始
 1. 克隆仓库
git clone https://github.com/J461-ZY/privacy-protection-cv.git
cd privacy-protection-cv  
2. 安装依赖 
pip install -r requirements.txt 
 3. 运行程序 
python privacy_mosaic_video.py  
4. 操作说明 
•  程序启动后会自动打开摄像头  
•  按  m  切换到马赛克模式  
•  按  g  切换到高斯模糊模式  
•  按  q  退出程序   

📸 效果演示  
左侧：原图 | 右侧：隐私保护后 
![效果对比图](https://github.com/J461-ZY/privacy-protection/raw/main/images/demo.png)


🔮 未来展望 
•  集成到 VR/AR 设备中，实现沉浸式交互的实时隐私保护  
•  结合 具身智能，让机器人理解环境中的隐私规范并调整行为 
•  优化模糊算法，实现更自然、语义级别的隐私遮挡（如仅模糊证件号码）
  
 📧 联系我 
•  姓名：金周苑
•  邮箱：501837010@qq.com
•  GitHub：https://github.com/J461-ZY

🙏 致谢
•  YOLOv8 团队提供的优秀目标检测框架  
•  OpenCV 社区提供的强大图像处理库
