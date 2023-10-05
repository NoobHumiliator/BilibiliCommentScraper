import Bilicomment
import schedule
import time

# 每隔3小时秒执行一次任务
schedule.every(3).hours.do(Bilicomment.main)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(1)