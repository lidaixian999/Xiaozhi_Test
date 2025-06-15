# MCP Sample Project | MCP 示例项目

A powerful interface for extending AI capabilities through remote control, calculations, email operations, knowledge search, and more.

一个强大的接口，用于通过远程控制、计算、邮件操作、知识搜索等方式扩展AI能力。

## Overview | 概述

MCP (Model Context Protocol) is a protocol that allows servers to expose tools that can be invoked by language models. Tools enable models to interact with external systems, such as querying databases, calling APIs, or performing computations. Each tool is uniquely identified by a name and includes metadata describing its schema.

MCP（模型上下文协议）是一个允许服务器向语言模型暴露可调用工具的协议。这些工具使模型能够与外部系统交互，例如查询数据库、调用API或执行计算。每个工具都由一个唯一的名称标识，并包含描述其模式的元数据。

## Features | 特性

- 🔌 Bidirectional communication between AI and external tools | AI与外部工具之间的双向通信
- 🔄 Automatic reconnection with exponential backoff | 具有指数退避的自动重连机制
- 📊 Real-time data streaming | 实时数据流传输
- 🛠️ Easy-to-use tool creation interface | 简单易用的工具创建接口
- 🔒 Secure WebSocket communication | 安全的WebSocket通信

## Quick Start | 快速开始

1. Install dependencies | 安装依赖:
```bash
pip install -r requirements.txt
```

2. Set up environment variables | 设置环境变量:
```bash
export MCP_ENDPOINT=<your_mcp_endpoint>
```

3. Run the calculator example | 运行计算器示例:
```bash
python mcp_pipe.py calculator.py
```

4. Run the weather service | 运行天气服务:
```bash
python mcp_pipe.py weather.py
```

5. Run the IP weather service | 运行IP天气查询服务:
```bash
python mcp_pipe.py ip_weather.py
```

## Weather Service Features | 天气服务功能

The weather service provides the following tools | 天气服务提供以下工具:

### get_weather(city: str)
- Get current weather information for a specified city | 获取指定城市的当前天气信息
- Returns temperature, weather condition, humidity, wind speed, etc. | 返回温度、天气状况、湿度、风速等信息
- Example: `get_weather("北京")` or `get_weather("Beijing")`

### get_weather_forecast(city: str, days: int = 3)
- Get weather forecast for a specified city | 获取指定城市的天气预报
- Supports 1-5 days forecast (default 3 days) | 支持1-5天预报（默认3天）
- Example: `get_weather_forecast("上海", 5)`

**Note**: Currently using simulated data for demonstration. For production use, please obtain a valid API key from OpenWeatherMap or other weather service providers.

**注意**: 当前使用模拟数据进行演示。生产环境使用时，请从OpenWeatherMap或其他天气服务提供商获取有效的API密钥。

## IP Weather Service Features | IP天气服务功能

The IP weather service provides the following tools | IP天气服务提供以下工具:

### get_current_ip_weather(ip_address: str = None)
- Get weather information for the location corresponding to an IP address | 获取IP地址对应位置的天气信息
- Automatically detects current IP if no IP address is provided | 如果未提供IP地址则自动检测当前IP
- Returns location info and current weather conditions | 返回位置信息和当前天气状况
- Example: `get_current_ip_weather()` or `get_current_ip_weather("114.247.50.2")`

### get_ip_location(ip_address: str = None)
- Get geographical location information for an IP address | 获取IP地址的地理位置信息
- Returns province, city, area code, and coordinate rectangle | 返回省份、城市、区域代码和坐标矩形
- Example: `get_ip_location("114.247.50.2")`

**API Requirements | API要求**: This service uses Amap (高德地图) APIs. For production use, please obtain a valid API key from [Amap Open Platform](https://lbs.amap.com/).

**API要求**: 此服务使用高德地图API。生产环境使用时，请从[高德开放平台](https://lbs.amap.com/)获取有效的API密钥。

## Project Structure | 项目结构

- `mcp_pipe.py`: Main communication pipe that handles WebSocket connections and process management | 处理WebSocket连接和进程管理的主通信管道
- `calculator.py`: Example MCP tool implementation for mathematical calculations | 用于数学计算的MCP工具示例实现
- `weather.py`: Weather query MCP tool for getting current weather and forecasts | 用于获取当前天气和天气预报的MCP工具
- `ip_weather.py`: IP-based weather query MCP tool using Amap APIs | 基于IP地址的天气查询MCP工具，使用高德地图API
- `requirements.txt`: Project dependencies | 项目依赖

## Creating Your Own MCP Tools | 创建自己的MCP工具

Here's a simple example of creating an MCP tool | 以下是一个创建MCP工具的简单示例:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("YourToolName")

@mcp.tool()
def your_tool(parameter: str) -> dict:
    """Tool description here"""
    # Your implementation
    return {"success": True, "result": result}

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

## Use Cases | 使用场景

- Mathematical calculations | 数学计算
- Weather information queries | 天气信息查询
- IP-based location and weather queries | 基于IP的位置和天气查询
- Email operations | 邮件操作
- Knowledge base search | 知识库搜索
- Remote device control | 远程设备控制
- Data processing | 数据处理
- Custom tool integration | 自定义工具集成

## Requirements | 环境要求

- Python 3.7+
- websockets>=11.0.3
- python-dotenv>=1.0.0
- mcp>=1.8.1
- pydantic>=2.11.4
- requests>=2.31.0

## Contributing | 贡献指南

Contributions are welcome! Please feel free to submit a Pull Request.

欢迎贡献代码！请随时提交Pull Request。

## License | 许可证

This project is licensed under the MIT License - see the LICENSE file for details.

本项目采用MIT许可证 - 详情请查看LICENSE文件。

## Acknowledgments | 致谢

- Thanks to all contributors who have helped shape this project | 感谢所有帮助塑造这个项目的贡献者
- Inspired by the need for extensible AI capabilities | 灵感来源于对可扩展AI能力的需求
