import requests
import csv
from datetime import datetime, timedelta

# OpenWeatherMap API 配置
API_KEY = '5796abbde9106b7da4febfae8c44c232'  # 替换为你的 API 密钥 1824293259 1824293259@qq.com 125800qwer123
CITY = 'London'  # china 替换为你需要查询的城市
LAT = 30.2937  # 替换为你城市的纬度
LON = 120.1614  # 替换为你城市的经度
URL = 'https://api.openweathermap.org/data/2.5/onecall/timemachine'

# 获取过去12个月的天气数据
def get_weather_data(months):
    weather_data = []
    current_date = datetime.utcnow()  # 当前时间（UTC）

    for i in range(months):
        # 计算每个月的时间点（往回推一个月）
        timestamp = (current_date - timedelta(days=i*30)).timestamp()  # 每30天作为一个月
        # 请求 API 获取天气数据
        params = {
            'lat': LAT,
            'lon': LON,
            'dt': int(timestamp),
            'appid': API_KEY,
            'units': 'metric'
        }

        response = requests.get(URL, params=params)
        if response.status_code == 200:
            data = response.json()
            # 提取需要的天气信息
            weather_info = {
                'Date': datetime.utcfromtimestamp(data['current']['dt']).strftime('%Y-%m-%d'),
                'Temperature (C)': data['current']['temp'] - 273.15,  # 转换为摄氏度
                'Humidity': data['current']['humidity'],
                'Pressure': data['current']['pressure'],
                'Weather': data['current']['weather'][0]['description']
            }
            weather_data.append(weather_info)
        else:
            print(f"Error fetching data for {current_date.strftime('%Y-%m-%d')}: {response.status_code}")

    return weather_data

# 导出数据到 CSV 文件
def save_to_csv(data, filename='weather_data.csv'):
    keys = data[0].keys()  # 获取 CSV 表头
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()  # 写入表头
        writer.writerows(data)  # 写入数据

# 主程序
def main():
    weather_data = get_weather_data(months=1)  # 获取过去12个月的天气数据
    if weather_data:
        save_to_csv(weather_data)  # 导出为 CSV 文件
        print("天气数据已成功导出到 weather_data.csv")
    else:
        print("没有获取到天气数据")

if __name__ == "__main__":
    main()