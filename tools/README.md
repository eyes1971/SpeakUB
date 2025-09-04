
# SpeakUB 开发工具和脚本

这个目录包含用于开发、测试和调试 SpeakUB 项目的辅助脚本和工具。

## 📁 文件说明

### 语音相关工具
- **`check_voices.py`** - 检查edge-tts可用的语音列表，统计中文和女性语音
- **`debug_voices.py`** - 调试语音数据结构，对比不同API的输出
- **`simple_test.py`** - 简单测试EdgeTTSProvider的基本功能
- **`voice_selector_demo.py`** - 独立的语音选择器演示脚本

### 布局和UI工具
- **`simple_layout_check.py`** - 静态检查TTS footer布局代码结构
- **`test_my_help_screen.py`** - 验证help screen是否包含语音功能

## 🚀 使用方法

### 运行脚本
```bash
# 检查可用语音
python tools/check_voices.py

# 调试语音数据
python tools/debug_voices.py

# 测试EdgeTTSProvider
python tools/simple_test.py

# 语音选择器演示
python tools/voice_selector_demo.py

# 检查布局
python tools/simple_layout_check.py

# 验证help screen
python tools/test_my_help_screen.py
```

## 📋 脚本用途

这些脚本主要用于：

1. **开发调试** - 帮助开发者理解和调试TTS功能
2. **功能验证** - 验证代码修改是否正确
3. **问题排查** - 快速定位和解决语音相关问题
4. **演示功能** - 向用户展示语音选择功能

## ⚠️ 注意事项

- 这些脚本需要安装相应的依赖（特别是edge-tts）
- 部分脚本可能需要网络连接来获取语音列表
- 这些脚本不影响项目的正常运行

## 🔧 依赖要求

```bash
pip install edge-tts
```

## 📞 技术支持

如果在使用这些脚本时遇到问题，请检查：
1. edge-tts是否正确安装
2. 网络连接是否正常
3. Python版本是否兼容（推荐3.8+）

