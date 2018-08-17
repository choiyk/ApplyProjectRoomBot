# ApplyProjectRoomBot

성공회대학교 소프트웨어공학과 프로젝트실 신청 공지가 업데이트되면 알려주는 챗봇입니다.

## Getting Started

Ubuntu 시스템의 cron/스케쥴러를 이용하여 자동으로 크롤링하고 Telegram 메세지를 보냅니다.

### Prerequisites

Ubuntu 시스템 환경 준비

```
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get autoremove
sudo apt-get install python3
sudo apt install python3-pip python3-setuptools build-essential
sudo locale-gen "ko_KR.UTF-8"
pip3 install selenium bs4 python-telegram-bot 
```

PhantomJs 설치
* [Debian/Ubuntu](https://gist.github.com/julionc/7476620)

* [Windows/Mac OS X](http://phantomjs.org/download.html)

### Installing

```
python bot.py
```

매 1분 마다 실행하도록 Crontab 설정

```
crontab -e
* * * * * /usr/bin/python3 /home/ubuntu/ApplyProjectRoomBot/bot.py
```

매 12분마다로 하려면 */12 * * * * /usr/bin/python3 /home/ubuntu/ApplyProjectRoomBot/bot.py

## Run

* Telegram에서 @ApplyProjectRoom을 검색

* [성공회대 소프 플젝실 신청 알림](https://web.telegram.org/#/im?p=@ApplyProjectRoom) 링크로 이동


## reference

* [나만의 웹크롤러 만들기](https://beomi.github.io/gb-crawling/)
