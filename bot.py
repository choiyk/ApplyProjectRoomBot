import telegram
from noticeParse import Notice
import os

my_token = '666407138:AAHpt3BDlWFCtHAgDG6GCxBnjJXdxHIXVaE'
#@ApplyProjectRoomBot
bot = telegram.Bot(token=my_token)
#성공회대 소프 플젝실 신청 알림 채널 id="-1001180931435"
chat_id = "-1001180931435"
#bot.deleteWebhook()
#updates = bot.getUpdates()
#recent_chat_id = updates[-1].message.chat.id #342213484

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

notice = Notice()
latest = notice.simplify(notice.getNewNotice())
print(latest)

with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+') as f_read:
    before = f_read.readline()
    if before != latest.get('title'):
        with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+') as f_write:
            f_write.write(latest.get('title'))
            f_write.close()

        if "프로젝트실" in latest.get('title'):
            text = latest.get('title') + "\n\n" + latest.get('content') + "..." + "\n연결: " + "http://sw.skhu.ac.kr" + latest.get('url')
            bot.sendMessage(chat_id=chat_id, text=text)
    else:
        pass
    f_read.close()


