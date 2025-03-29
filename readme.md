# 说明
- 这是一个精简优化版的聊天机器人。通过wxauto收发微信消息，deepseek生成回复消息。
- 原项目仓库：https://github.com/KouriChat/KouriChat
- 本项目由iwyxdxl在原项目基础上修改创建。
- 本机器人拥有更优化的消息处理流程，更加拟人化的聊天服务。
- 本版本致力于实现更加拟人化聊天效果，因此不提供生成语音、生成图片等功能。
- 欢迎加入QQ交流群 一群 617379532 二群 964162330

# 效果图
<img src="Demo_Image/1.jpg" alt="示例图片1" width="300px">
<img src="Demo_Image/2.jpg" alt="示例图片2" width="300px">
<img src="Demo_Image/3.png" alt="示例图片3" width="900px">
<img src="Demo_Image/4.png" alt="示例图片4" width="900px">

# 版本号
- v3.10

# 目前支持的功能
1. 自动回复
2. 识别图片/表情包内容
3. 群聊功能
4. 多个微信用户/群聊同时聊天
5. 给每个微信用户/群聊自由分配不同的提示词Prompt
6. 时间感知
7. 识别情绪回复表情包
8. 主动发消息
9. 合并处理多条消息和多个表情包
10. 自行决定是否开启部分功能
11. 使用WebUI启动程序、修改配置文件、生成和修改Prompt
12. 记忆保存到Prompt
13. 自动更新功能


# 使用前准备
1. 申请API,推荐WeAPIs https://vg.v1api.cc/register?aff=Rf3h 或 DeepSeek官方API
2. 申请Moonshot API（用于图片和表情包识别）https://platform.moonshot.cn/ （免费15元额度）
3. 请先安装python、pip，python版本应大于3.8

# 使用方式
1. 登录电脑微信，确保在后台运行
2. 运行 Run.bat 启动程序，等待自动安装依赖文件
3. 在打开的网页中修改配置文件，选择您的API服务提供商、模型，并填入您的API KEY
4. 在页面右上角点击 'Prompt管理' 进入提示词管理页面
5. 在提示词管理页面您可以参考自带的提示词样式编写或者使用提示词生成器生成您需要的提示词
6. 回到配置编辑器页面，填入微信昵称（注意不要在微信为他设置备注）或群聊名称，并选择对应提示词
7. 修改完配置后点击页面右上角'Start Bot'启动程序
8. 如果想要自定义表情包请将表情包(.gif .png .jpg .jpeg)文件放入emojis中对应的文件夹中

# 联系我
1. 邮箱iwyxdxl@gmail.com
2. QQ 2025128651
   
# 声明
- 本项目基于 [KouriChat](https://github.com/KouriChat/KouriChat) 修改，遵循 **GNU GPL-3.0 或更高版本** 许可证。
- 原项目版权归属：umaru (2025)。
# WeChatBoxAgent
