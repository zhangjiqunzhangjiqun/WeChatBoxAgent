# -*- coding: utf-8 -*-

# ***********************************************************************
# Modified based on the KouriChat project
# Copyright of this modification: Copyright (C) 2025, iwyxdxl
# Licensed under GNU GPL-3.0 or higher, see the LICENSE file for details.
# 
# This file is part of WeChatBot, which includes modifications to the KouriChat project.
# The original KouriChat project's copyright and license information are preserved in the LICENSE file.
# For any further details regarding the license, please refer to the LICENSE file.
# ***********************************************************************

# 用户列表(请配置要和bot说话的账号的微信昵称，不要写备注！)
# 例如：LISTEN_LIST = ['微信昵称1','提示词示例1']
LISTEN_LIST = [['AI测试', '提示词示例1']]

# DeepSeek API 配置
DEEPSEEK_API_KEY = 'caf9787e-d1ae-433e-85d5-6c7e9bc4e826'
# 硅基流动API注册地址，免费15元额度 https://cloud.siliconflow.cn/
DEEPSEEK_BASE_URL = 'https://ark.cn-beijing.volces.com/api/v3'
# 硅基流动API的模型
MODEL = 'doubao-1-5-lite-32k-250115'

# 如果要使用官方的API
# DEEPSEEK_BASE_URL = 'https://api.deepseek.com'
# 官方API的V3模型
# MODEL = 'deepseek-chat'

# 回复最大token
MAX_TOKEN = 2000
# DeepSeek温度
TEMPERATURE = 1.1

# Moonshot AI配置（用于图片和表情包识别）
# API申请https://platform.moonshot.cn/
MOONSHOT_API_KEY = 'sk-NEhhtdpGrmXQHIV2RQewljWvuSx7tc2xJaBEc3WW1D8AhuNR'
MOONSHOT_BASE_URL = 'https://api.moonshot.cn/v1'
MOONSHOT_MODEL = 'moonshot-v1-128k-vision-preview'
MOONSHOT_TEMPERATURE = 0.8
ENABLE_IMAGE_RECOGNITION = False
ENABLE_EMOJI_RECOGNITION = False

# 消息队列等待时间
QUEUE_WAITING_TIME = 7

# 表情包存放目录
EMOJI_DIR = 'emojis'
ENABLE_EMOJI_SENDING = True
EMOJI_SENDING_PROBABILITY = 25

# 自动消息配置
AUTO_MESSAGE = '请你模拟系统设置的角色，在微信上找对方继续刚刚的话题或者询问对方在做什么'
ENABLE_AUTO_MESSAGE = True
# 等待时间
MIN_COUNTDOWN_HOURS = 1.0
MAX_COUNTDOWN_HOURS = 2.0
# 消息发送时间限制
QUIET_TIME_START = '22:00'
QUIET_TIME_END = '8:00'

# 消息回复时间间隔
# 间隔时间 = 字数 * (平均时间 + 随机时间)
AVERAGE_TYPING_SPEED = 0.2
RANDOM_TYPING_SPEED_MIN = 0.05
RANDOM_TYPING_SPEED_MAX = 0.1

# 记忆功能
# 采用综合评分公式：0.6*重要度 - 0.4*(存在时间小时数)
# 示例：
# 重要度5的旧记忆（存在12小时）得分：0.65 - 0.412 = 3 - 4.8 = -1.8
# 重要度4的新记忆（存在1小时）得分：0.64 - 0.41 = 2.4 - 0.4 = 2.0 → 保留新记忆
ENABLE_MEMORY = True
MEMORY_TEMP_DIR = 'Memory_Temp'
MAX_MESSAGE_LOG_ENTRIES = 30
MAX_MEMORY_NUMBER = 50

# 是否接收全部群聊消息
Accept_All_Group_Chat_Messages = False

# 登录配置编辑器设置
ENABLE_LOGIN_PASSWORD = False
LOGIN_PASSWORD = '123456'
PORT = 5000
