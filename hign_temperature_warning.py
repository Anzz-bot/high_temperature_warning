import requests
server_key = 'SC***********************35'
gaode_key = 'bf***********************8e'
city = '深圳'
city_code = 440300
max_temperature = 30

def send_msg(title,content):
    data_param={}
    url = 'https://sctapi.ftqq.com/'+server_key+'.send'
    data_param['title'] = title
    data_param['desp'] = content
    response = requests.post(url=url,data=data_param)
    print(response.content)

def get_weather():
    data_param = {}
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?parameters'
    data_param['key'] = gaode_key
    data_param['city'] = city_code
    response = requests.get(url,params=data_param)
    return response.json()

def send_err():
    send_msg('天气获取失败','天气获取失败，请检查系统状态')

def handle_wether():
    try:
        weather_data = get_weather()
        print(weather_data)
        temperature = weather_data['lives'][0]['temperature']
        weather =  weather_data['lives'][0]['weather']
        winddirection = weather_data['lives'][0]['winddirection']
        windpower = weather_data['lives'][0]['windpower']
        humidity = weather_data['lives'][0]['humidity']
        reporttime = weather_data['lives'][0]['reporttime']
        desc = '* 今天天气：'+weather+' \r\n * 温度：'+temperature+'  \r\n* 风向:'+winddirection+','+windpower+'级  '+'\r\n* 湿度：'+humidity+'  \r\n* 更新时间：'+reporttime
        if int(temperature)>=max_temperature:
            send_msg('今天'+city+'天气温度过高，注意防晒！',desc)
        if '雨' in weather:
            send_msg('今天'+city+'天气为：'+weather+'，注意防晒！',desc)
    except:
        send_err()

if __name__ =='__main__':
    handle_wether()
