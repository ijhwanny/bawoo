# Overview
웹 스크랩핑을 통해 최신 업데이트 내용을 Telegram Bot을 활용해 채널구독자에게 알림 서비스 제공

추후 배포 및 환경에 대한 독립관리를 위해 Virtual Environment 내 개발환경을 생성하고,
Windows 운영환경 내, 작업 스케줄러에 실행 스크립트를 등록해 1시간 마다 해당 스크립트가 실행되도록 구성

# Language & Key Packages
python 3.8
	requests
	bs4
	python-telegram-bot

# Setup
anaconda 또는 pycharm을 활용하지 않고 기본 python 패키지와 atom editor만을 활용해 
다른 프로젝트와 의존성이 없도록 별도의 Virtual Environment 환경을 구성하고 프로젝트 생성하고자 함.
conda와 pycharm을 활용해 virtual environment 구성 시 불필요한 라이브러리가 포함되어
빌드시간이 길어지고, 패키지 사이즈가 증가함


 1. Install virtualenv
	PS> pip install virtualenv

 2. Launch virtualenv
	PS> cd your_project
 	PS> virtualenv env --python=python3.8
		or 
 	PS> python -m virtualenv venv 

 3. Activate your virtualenv:
 	PS> ./Scripts/activate

 4. Install ipykernal to activate Hydrogen
	PS> python -m pip install ipykernel
	PS> python -m ipykernel install --user

 5. Launch Atom
	PS> atom .

