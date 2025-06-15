# MCP Tools Collection | MCP工具集合

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MCP](https://img.shields.io/badge/MCP-1.8.1+-orange.svg)](https://github.com/modelcontextprotocol/python-sdk)

一个功能强大的MCP工具集合，为AI模型提供数学计算、天气查询、IP定位等扩展能力。

A powerful collection of MCP tools that extend AI capabilities with mathematical calculations, weather queries, IP geolocation, and more.

## 🚀 概述 | Overview

**MCP (Model Context Protocol)** 是一个标准化协议，允许AI模型安全地调用外部工具和服务。本项目提供了一套完整的MCP工具实现，包括：

- 🧮 **数学计算器** - 支持复杂数学表达式求解
- 🌤️ **天气查询** - 获取实时天气和预报信息  
- 🌍 **IP定位** - 基于IP地址的地理位置和天气查询
- 🔧 **可扩展架构** - 轻松创建自定义工具

**MCP (Model Context Protocol)** is a standardized protocol that enables AI models to securely invoke external tools and services. This project provides a complete suite of MCP tool implementations.

## ✨ 核心特性 | Key Features

### 🔧 技术特性 | Technical Features
- **🔌 双向通信** - AI与外部工具间的实时双向数据交换
- **🔄 智能重连** - 指数退避算法确保连接稳定性
- **📊 流式处理** - 支持实时数据流传输和处理
- **🛡️ 安全通信** - 基于WebSocket的加密通信协议
- **⚡ 高性能** - 异步处理架构，支持并发调用

### 🎯 功能特性 | Functional Features
- **📐 数学计算** - 支持复杂表达式、科学计算、随机数生成
- **🌦️ 天气服务** - 实时天气、多日预报、城市搜索
- **🗺️ 地理定位** - IP地址解析、位置查询、区域天气
- **🔨 工具框架** - 标准化的工具开发和部署框架

## 🚀 快速开始 | Quick Start

### 📦 环境准备 | Environment Setup

```bash
# 1. 克隆项目 | Clone repository
git clone <repository-url>
cd mcp-test

# 2. 安装依赖 | Install dependencies
pip install -r requirements.txt

# 3. 配置环境变量 (可选) | Configure environment (optional)
export MCP_ENDPOINT=<your_mcp_endpoint>
export WEATHER_API_KEY=<your_weather_api_key>
export AMAP_API_KEY=<your_amap_api_key>
```

### 🎮 运行示例 | Run Examples

```bash
# 数学计算器 | Mathematical Calculator
python mcp_pipe.py calculator.py

# 天气查询服务 | Weather Query Service
python mcp_pipe.py weather.py

# IP定位天气服务 | IP-based Weather Service
python mcp_pipe.py ip_weather.py
```

### 🔧 验证安装 | Verify Installation

```bash
# 检查MCP连接状态
python -c "import mcp; print('MCP installed successfully')"

# 测试WebSocket连接
python mcp_pipe.py --test
```

## 🧮 数学计算器 | Mathematical Calculator

### 📋 功能概览 | Feature Overview

| 工具名称 | 功能描述 | 支持模块 | 安全特性 |
|---------|---------|----------|----------|
| `calculator` | 数学表达式求解 | `math`, `random` | 沙箱执行 |

### 🔧 API详细说明 | API Details

#### `calculator(expression: str) -> dict`
安全地计算Python数学表达式

**支持功能:**
- 基础运算: `+`, `-`, `*`, `/`, `**`, `%`
- 数学函数: `sin()`, `cos()`, `sqrt()`, `log()`, `abs()`
- 随机数: `random()`, `randint()`, `choice()`
- 常量: `pi`, `e`

**使用示例:**
```python
# 基础计算
calculator("2 + 3 * 4")  # 结果: 14

# 科学计算
calculator("math.sin(math.pi/2)")  # 结果: 1.0

# 随机数生成
calculator("random.randint(1, 100)")  # 结果: 随机整数
```

## 🌤️ 天气服务 | Weather Service

### 📋 功能概览 | Feature Overview

| 工具名称 | 功能描述 | 参数 | 返回数据 |
|---------|---------|------|----------|
| `get_weather` | 实时天气查询 | `city: str` | 温度、湿度、风速、天气状况 |
| `get_weather_forecast` | 天气预报查询 | `city: str, days: int` | 多日天气预报数据 |

### 🔧 API详细说明 | API Details

#### `get_weather(city: str) -> dict`
获取指定城市的实时天气信息

**参数说明:**
- `city`: 城市名称，支持中英文 (如: "北京", "Beijing", "New York")

**返回数据:**
```json
{
  "city": "北京",
  "temperature": 25,
  "condition": "晴朗",
  "humidity": 60,
  "wind_speed": 12,
  "pressure": 1013,
  "visibility": 10
}
```

#### `get_weather_forecast(city: str, days: int = 3) -> dict`
获取指定城市的天气预报

**参数说明:**
- `city`: 城市名称
- `days`: 预报天数 (1-5天，默认3天)

**使用示例:**
```python
# 获取北京当前天气
result = get_weather("北京")

# 获取上海5天天气预报
forecast = get_weather_forecast("上海", 5)
```

> **⚠️ 重要提示:** 当前使用模拟数据演示。生产环境请配置真实的天气API密钥。

## 🌍 IP定位服务 | IP Geolocation Service

### 📋 功能概览 | Feature Overview

| 工具名称 | 功能描述 | 参数 | 数据源 |
|---------|---------|------|--------|
| `get_current_ip_weather` | IP位置天气查询 | `ip_address?: str` | 高德地图API |
| `get_ip_location` | IP地理位置查询 | `ip_address?: str` | 高德地图API |

### 🔧 API详细说明 | API Details

#### `get_current_ip_weather(ip_address: str = None) -> dict`
根据IP地址获取对应位置的天气信息

**参数说明:**
- `ip_address`: IP地址 (可选，默认自动检测当前IP)

**返回数据:**
```json
{
  "ip": "114.247.50.2",
  "location": {
    "province": "北京市",
    "city": "北京市",
    "adcode": "110000"
  },
  "weather": {
    "temperature": 22,
    "condition": "多云",
    "humidity": 65
  }
}
```

#### `get_ip_location(ip_address: str = None) -> dict`
获取IP地址的详细地理位置信息

**返回数据:**
```json
{
  "ip": "114.247.50.2",
  "province": "北京市",
  "city": "北京市",
  "adcode": "110000",
  "rectangle": "116.0119343,39.66127144;116.7829835,40.2164962"
}
```

**使用示例:**
```python
# 获取当前IP位置天气
weather = get_current_ip_weather()

# 获取指定IP地理位置
location = get_ip_location("114.247.50.2")
```

### 🔑 API配置 | API Configuration

本服务使用**高德地图开放平台**API，需要配置API密钥：

1. 访问 [高德开放平台](https://lbs.amap.com/)
2. 注册账号并创建应用
3. 获取API Key
4. 设置环境变量: `export AMAP_API_KEY=your_api_key`

## 📁 项目结构 | Project Structure

```
mcp-test/
├── 📄 README.md              # 项目文档
├── 📄 requirements.txt       # Python依赖包
├── 📄 .gitignore            # Git忽略文件
├── 🔧 mcp_pipe.py           # MCP通信管道 (核心组件)
├── 🧮 calculator.py         # 数学计算器工具
├── 🌤️ weather.py            # 天气查询工具
└── 🌍 ip_weather.py         # IP定位天气工具
```

### 🔧 核心组件说明 | Core Components

#### `mcp_pipe.py` - MCP通信管道
- **功能**: WebSocket连接管理、进程调度、消息路由
- **特性**: 自动重连、错误处理、日志记录
- **架构**: 异步事件驱动，支持多工具并发

#### `calculator.py` - 数学计算器
- **功能**: 数学表达式求解、科学计算
- **支持**: math模块、random模块、复杂表达式
- **安全**: 沙箱执行环境，防止恶意代码

#### `weather.py` - 天气查询服务
- **功能**: 实时天气、天气预报
- **数据源**: OpenWeatherMap API (可配置)
- **特性**: 多语言支持、缓存机制

#### `ip_weather.py` - IP定位服务
- **功能**: IP地理定位、位置天气查询
- **数据源**: 高德地图API
- **特性**: 自动IP检测、精确定位

## 🛠️ 开发指南 | Development Guide

### 🎯 创建自定义工具 | Creating Custom Tools

#### 基础模板 | Basic Template

```python
from mcp.server.fastmcp import FastMCP
from typing import Optional, Dict, Any
import logging

# 初始化MCP服务
mcp = FastMCP("CustomTool")

@mcp.tool()
def custom_function(param1: str, param2: Optional[int] = 10) -> Dict[str, Any]:
    """自定义工具函数
    
    Args:
        param1: 必需参数说明
        param2: 可选参数说明 (默认: 10)
    
    Returns:
        Dict[str, Any]: 返回结果字典
    """
    try:
        # 业务逻辑实现
        result = process_data(param1, param2)
        
        return {
            "success": True,
            "data": result,
            "message": "操作成功"
        }
    except Exception as e:
        logging.error(f"工具执行错误: {e}")
        return {
            "success": False,
            "error": str(e),
            "message": "操作失败"
        }

def process_data(param1: str, param2: int) -> Any:
    """业务逻辑处理函数"""
    # 实现具体业务逻辑
    pass

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

#### 高级特性 | Advanced Features

```python
# 1. 参数验证
from pydantic import BaseModel, validator

class ToolInput(BaseModel):
    text: str
    count: int = 1
    
    @validator('count')
    def validate_count(cls, v):
        if v < 1 or v > 100:
            raise ValueError('count must be between 1 and 100')
        return v

@mcp.tool()
def validated_tool(input_data: ToolInput) -> dict:
    """带参数验证的工具"""
    return {"processed": input_data.text * input_data.count}

# 2. 异步工具
import asyncio
import aiohttp

@mcp.tool()
async def async_tool(url: str) -> dict:
    """异步HTTP请求工具"""
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            return {"status": response.status, "data": data}

# 3. 资源管理
@mcp.tool()
def resource_tool(file_path: str) -> dict:
    """文件处理工具"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return {"success": True, "content": content}
    except FileNotFoundError:
        return {"success": False, "error": "文件不存在"}
```

### 📋 开发最佳实践 | Best Practices

1. **🔒 安全性**: 验证输入参数，防止注入攻击
2. **⚡ 性能**: 使用异步操作，避免阻塞
3. **🛡️ 错误处理**: 完善的异常捕获和错误返回
4. **📝 文档**: 详细的函数文档和类型注解
5. **🧪 测试**: 编写单元测试确保工具稳定性

## 🎯 应用场景 | Use Cases

### 🔢 数据处理与计算 | Data Processing & Computing
- **数学计算**: 复杂表达式求解、科学计算、统计分析
- **数据转换**: 格式转换、编码解码、数据清洗
- **算法实现**: 排序、搜索、图算法等

### 🌐 信息查询服务 | Information Query Services  
- **天气服务**: 实时天气、预报查询、气象数据分析
- **地理定位**: IP定位、地址解析、距离计算
- **知识检索**: 文档搜索、FAQ查询、信息聚合

### 🔧 系统集成与自动化 | System Integration & Automation
- **API集成**: 第三方服务调用、数据同步
- **设备控制**: IoT设备管理、远程操作
- **工作流自动化**: 任务调度、批处理、监控告警

### 💼 企业级应用 | Enterprise Applications
- **业务流程**: 订单处理、库存管理、财务计算
- **客户服务**: 智能客服、问题诊断、解决方案推荐
- **数据分析**: 报表生成、趋势分析、预测建模

## 📋 技术要求 | Technical Requirements

### 🐍 Python环境 | Python Environment
- **Python版本**: 3.7+ (推荐 3.9+)
- **操作系统**: Windows, macOS, Linux
- **内存要求**: 最小 512MB，推荐 1GB+

### 📦 核心依赖 | Core Dependencies

| 包名 | 版本要求 | 用途 |
|------|---------|------|
| `websockets` | >=11.0.3 | WebSocket通信 |
| `python-dotenv` | >=1.0.0 | 环境变量管理 |
| `mcp` | >=1.8.1 | MCP协议实现 |
| `pydantic` | >=2.11.4 | 数据验证 |
| `requests` | >=2.31.0 | HTTP请求 |
| `aiohttp` | >=3.8.0 | 异步HTTP (可选) |

### 🔧 开发依赖 | Development Dependencies

```bash
# 安装开发依赖
pip install pytest>=7.0.0 black>=22.0.0 flake8>=4.0.0

# 代码格式化
black .

# 代码检查
flake8 .

# 运行测试
pytest
```

## 🤝 贡献指南 | Contributing

### 🚀 如何贡献 | How to Contribute

1. **🍴 Fork项目** - 点击右上角Fork按钮
2. **🌿 创建分支** - `git checkout -b feature/your-feature`
3. **💻 编写代码** - 遵循代码规范，添加测试
4. **✅ 测试验证** - 确保所有测试通过
5. **📝 提交更改** - `git commit -m 'Add some feature'`
6. **📤 推送分支** - `git push origin feature/your-feature`
7. **🔄 创建PR** - 提交Pull Request

### 📝 代码规范 | Code Standards

- **代码风格**: 遵循PEP 8规范
- **注释要求**: 函数必须有docstring
- **类型注解**: 使用类型提示增强代码可读性
- **测试覆盖**: 新功能需要对应的单元测试

### 🐛 问题报告 | Issue Reporting

发现Bug或有功能建议？请创建Issue并包含：
- 详细的问题描述
- 复现步骤
- 期望行为
- 系统环境信息

## 📄 许可证 | License

本项目采用 **MIT许可证** 开源。详情请查看 [LICENSE](LICENSE) 文件。

```
MIT License - 允许商业使用、修改、分发和私人使用
```

## 🙏 致谢 | Acknowledgments

### 🌟 核心贡献者 | Core Contributors
- 感谢所有为项目贡献代码的开发者
- 感谢提供反馈和建议的用户社区

### 🔧 技术支持 | Technical Support
- [Model Context Protocol](https://github.com/modelcontextprotocol) - MCP协议标准
- [FastMCP](https://github.com/jlowin/fastmcp) - 快速MCP开发框架
- [高德地图开放平台](https://lbs.amap.com/) - 地理位置服务

### 💡 灵感来源 | Inspiration
项目灵感来源于AI能力扩展的需求，致力于构建标准化、可复用的工具生态系统。

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给我们一个Star！**

**🔗 [项目主页](https://github.com/your-repo) | [文档](https://docs.your-site.com) | [问题反馈](https://github.com/your-repo/issues)**

</div>
