import telegram
import asyncio
import datetime

async def send_telegram_message():
    token = "YOUR_TELEGRAM_BOT_TOKEN"  
    bot = telegram.Bot(token=token)
    chat_id = "YOUR_CHAT_ID"  
    current_time = datetime.datetime.now()

    if 6 <= current_time.hour < 23:  # 오후 11시부터 아침 6시까지는 출력하지 않음
        text = '현재 시간: {}'.format(await get_current_time())
        await bot.sendMessage(chat_id=chat_id, text=text)
    else:
        print("현재 시간은 메시지를 출력할 시간이 아닙니다.")

async def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")

async def main():
    while True:
        await send_telegram_message()
        await asyncio.sleep(1800)  # 30분 간격으로 메시지 전송

if __name__ == "__main__":
    asyncio.run(main())
