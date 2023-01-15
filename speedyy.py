import speedtest
import requests

print('Testing your network speed..')
ip = requests.get('https://api.ipify.org').text
print(f"Your IP: {ip}")

def internet_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    host = st.results.server['host']
    download_speed = round(st.download() / (10**6),2)
    upload_speed = round(st.upload() / (10**6),2)
    return (host, download_speed, upload_speed)

host, download_speed, upload_speed = internet_speed()
print(f"Connected to: {host}" + '  '+'(best server)')
print(f"Download speed: {download_speed} Mbps")
print(f"Upload speed: {upload_speed} Mbps")
