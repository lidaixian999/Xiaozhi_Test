# ip_weather.py
from mcp.server.fastmcp import FastMCP
import sys
import logging
import requests
import json
from datetime import datetime

logger = logging.getLogger('IPWeather')

# Fix UTF-8 encoding for Windows console
if sys.platform == 'win32':
    sys.stderr.reconfigure(encoding='utf-8')
    sys.stdout.reconfigure(encoding='utf-8')

# 高德地图API密钥 - 需要在高德开放平台申请
AMAP_API_KEY = "b6a024a9b9a310dc076db4f80acf2d8a"  # 请在 https://lbs.amap.com/ 申请API密钥

# Create an MCP server
mcp = FastMCP("IP天气查询")

def get_location_by_ip(ip_address: str = None) -> dict:
    """
    根据IP地址获取地理位置信息
    参数:
    - ip_address: IP地址，如果为空则使用当前请求IP
    """
    try:
        url = "https://restapi.amap.com/v3/ip"
        params = {
            "key": AMAP_API_KEY
        }
        
        # 如果指定了IP地址，添加到参数中
        if ip_address:
            params["ip"] = ip_address
        
        # 如果没有API密钥，使用模拟数据
        if AMAP_API_KEY == "your_amap_api_key":
            logger.info("使用模拟IP定位数据")
            return {
                "status": "1",
                "info": "OK",
                "infocode": "10000",
                "province": "北京市",
                "city": "北京市",
                "adcode": "110000",
                "rectangle": "116.0119343,39.66127144;116.7829835,40.2164962"
            }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"IP定位成功: {data}")
            return data
        else:
            logger.error(f"IP定位API请求失败: {response.status_code}")
            return {"status": "0", "info": f"请求失败: {response.status_code}"}
            
    except Exception as e:
        logger.exception("IP定位查询异常")
        return {"status": "0", "info": f"查询异常: {str(e)}"}
@mcp.tool()
def get_weather_by_city(city: str, adcode: str = None) -> dict:
    """
    根据城市名称获取天气信息，询问城市天气如何时调用
    参数:
    - city: 城市名称
    - adcode: 城市编码（可选）
    """
    try:
        url = "https://restapi.amap.com/v3/weather/weatherInfo"
        params = {
            "key": AMAP_API_KEY,
            "city": adcode if adcode else city,
            "extensions": "base"  # base:实况天气, all:预报天气
        }
        
        # 如果没有API密钥，使用模拟数据
        if AMAP_API_KEY == "your_amap_api_key":
            logger.info(f"使用模拟天气数据 - 城市: {city}")
            return {
                "status": "1",
                "count": "1",
                "info": "OK",
                "infocode": "10000",
                "lives": [{
                    "province": city.replace("市", ""),
                    "city": city,
                    "adcode": adcode or "110000",
                    "weather": "晴",
                    "temperature": "22",
                    "winddirection": "南",
                    "windpower": "≤3",
                    "humidity": "65",
                    "reporttime": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }]
            }
        
        response = requests.get(url, params=params, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            logger.info(f"天气查询成功: {data}")
            return data
        else:
            logger.error(f"天气API请求失败: {response.status_code}")
            return {"status": "0", "info": f"请求失败: {response.status_code}"}
            
    except Exception as e:
        logger.exception("天气查询异常")
        return {"status": "0", "info": f"查询异常: {str(e)}"}

@mcp.tool()
def get_current_ip_weather(ip_address: str = None) -> dict:
    """
    获取当前IP地址对应位置的天气信息。
    参数:
    - ip_address: 可选的IP地址，如果不提供则使用当前请求IP
    
    返回IP地址对应城市的当前天气信息。
    """
    try:
        logger.info(f"开始查询IP天气信息 - IP: {ip_address or '当前IP'}")
        
        # 第一步：根据IP获取地理位置
        location_data = get_location_by_ip(ip_address)
        
        if location_data.get("status") != "1":
            return {
                "success": False,
                "error": f"IP定位失败: {location_data.get('info', '未知错误')}"
            }
        
        province = location_data.get("province", "")
        city = location_data.get("city", "")
        adcode = location_data.get("adcode", "")
        
        if not city:
            return {
                "success": False,
                "error": "无法获取城市信息，可能是局域网IP或国外IP"
            }
        
        # 第二步：根据城市获取天气信息
        weather_data = get_weather_by_city(city, adcode)
        
        if weather_data.get("status") != "1":
            return {
                "success": False,
                "error": f"天气查询失败: {weather_data.get('info', '未知错误')}"
            }
        
        # 解析天气数据
        lives = weather_data.get("lives", [])
        if not lives:
            return {
                "success": False,
                "error": "未获取到天气数据"
            }
        
        weather_info = lives[0]
        
        result = {
            "success": True,
            "ip_address": ip_address or "当前IP",
            "location": {
                "province": province,
                "city": city,
                "adcode": adcode
            },
            "weather": {
                "condition": weather_info.get("weather", ""),
                "temperature": f"{weather_info.get('temperature', '')}°C",
                "humidity": f"{weather_info.get('humidity', '')}%",
                "wind_direction": weather_info.get("winddirection", ""),
                "wind_power": weather_info.get("windpower", ""),
                "report_time": weather_info.get("reporttime", "")
            },
            "message": f"📍 位置: {province} {city}\n🌤 天气: {weather_info.get('weather', '')}\n🌡 温度: {weather_info.get('temperature', '')}°C\n💧 湿度: {weather_info.get('humidity', '')}%\n🌬 风向: {weather_info.get('winddirection', '')} {weather_info.get('windpower', '')}\n⏰ 更新时间: {weather_info.get('reporttime', '')}"
        }
        
        logger.info(f"IP天气查询成功 - {city}: {weather_info.get('weather', '')} {weather_info.get('temperature', '')}°C")
        return result
        
    except Exception as e:
        logger.exception("IP天气查询工具异常")
        return {
            "success": False,
            "error": f"查询失败: {str(e)}"
        }

@mcp.tool()
def get_ip_location(ip_address: str = None) -> dict:
    """
    获取IP地址的地理位置信息。
    参数:
    - ip_address: 可选的IP地址，如果不提供则使用当前请求IP
    
    返回IP地址对应的省份、城市等地理位置信息。
    """
    try:
        logger.info(f"开始查询IP地理位置 - IP: {ip_address or '当前IP'}")
        
        location_data = get_location_by_ip(ip_address)
        
        if location_data.get("status") != "1":
            return {
                "success": False,
                "error": f"IP定位失败: {location_data.get('info', '未知错误')}"
            }
        
        result = {
            "success": True,
            "ip_address": ip_address or "当前IP",
            "province": location_data.get("province", ""),
            "city": location_data.get("city", ""),
            "adcode": location_data.get("adcode", ""),
            "rectangle": location_data.get("rectangle", ""),
            "message": f"📍 IP地址 {ip_address or '当前IP'} 位于: {location_data.get('province', '')} {location_data.get('city', '')}"
        }
        
        logger.info(f"IP定位成功 - {location_data.get('city', '')}")
        return result
        
    except Exception as e:
        logger.exception("IP定位查询工具异常")
        return {
            "success": False,
            "error": f"查询失败: {str(e)}"
        }

# Start the server
if __name__ == "__main__":
    mcp.run(transport="stdio")