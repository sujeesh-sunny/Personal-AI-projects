import speedtest

speed_test = speedtest.Speedtest()

def bits_to_mb(bits):
    MB = 1024 * 1024
    return bits / (MB * 8)  # Convert bits to megabits

download_speed = speed_test.download()
download_speed_mbps = bits_to_mb(download_speed)
print("Your Download speed is", download_speed_mbps, "Mbps")
