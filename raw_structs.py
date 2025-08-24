option_categories = {
    "외관": "Экстерьер",
    "멀티미디어": "Мультимедиа",
    "내장": "Интерьер",
    "안전": "Безопасность",
    "편의": "Комфорт и удобства",
}



car_options = [
        {
            "optionCd": "010",
            "optionName": "선루프",
            "optionTypeCd": "01",
            "sort": 1,
            "imagePath": "/carsdata/option_images/option1-1.png",
            "description": "자동차 루프가 유리로 되어 개폐할 수 있는 장치로 선루프와 넓은 파노라마 선루프가 있습니다.",
            "group": False,
            "optionTitle": "선루프",
            "groupOptionName": "선루프",
            "location": "루프가 유리로 되어 있으며, 여닫을 수 있는 형태입니다. 간혹 루프가 개폐되지 않는 유리 형태의 글래스 루프도 있으나, 해당 모델 또한 선루프의 한 종류로 볼 수 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "001",
            "optionName": "헤드램프",
            "optionTypeCd": "01",
            "sort": 2,
            "imagePath": "/carsdata/option_images/option1-2.png",
            "description": "HID/LED 헤드램프는 일반 할로겐 대비 색상이 자연광에 가까워 눈에 피로를 주지 않고 가시거리가 넓습니다.",
            "group": True,
            "optionTitle": "헤드램프(HID, LED)",
            "groupOptionName": "헤드램프",
            "location": "HID/LED 헤드램프는 일반 할로겐 대비 색상이 자연광에 가까워 눈에 피로를 주지 않고 가시거리가 넓습니다.",
            "subOptions": [
                {
                    "optionCd": "029",
                    "optionName": "헤드램프(HID)",
                    "optionTypeCd": "01",
                    "sort": 2,
                    "imagePath": "/carsdata/option_images/option1-2.png",
                    "description": "HID/LED 헤드램프는 일반 할로겐 대비 색상이 자연광에 가까워 눈에 피로를 주지 않고 가시거리가 넓습니다.",
                    "group": False,
                    "optionTitle": "헤드램프(HID, LED)",
                    "groupOptionName": "헤드램프(HID)",
                    "location": "할로겐 램프보다 색상이 자연광에 가까워 육안으로 확인되며, HID는 밸러스트 유무로 확인하며, 겉에서는 식별이 어렵습니다.\nLED는 한 개가 아닌 여러 개로 구성된 디자인도 있으며 라이트 커버 LED 로고가 새겨진 모델도 있습니다. 고사양 버전인 레이저의 경우도 LED 헤드램프 옵션으로 확인합니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "075",
                    "optionName": "헤드램프(LED)",
                    "optionTypeCd": "01",
                    "sort": 3,
                    "imagePath": "/carsdata/option_images/option1-2.png",
                    "description": "HID/LED 헤드램프는 일반 할로겐 대비 색상이 자연광에 가까워 눈에 피로를 주지 않고 가시거리가 넓습니다.",
                    "group": False,
                    "optionTitle": "헤드램프(HID, LED)",
                    "groupOptionName": "헤드램프(LED)",
                    "location": "할로겐 램프보다 색상이 자연광에 가까워 육안으로 확인되며, HID는 밸러스트 유무로 확인하며, 겉에서는 식별이 어렵습니다.\nLED는 한 개가 아닌 여러 개로 구성된 디자인도 있으며 라이트 커버 LED 로고가 새겨진 모델도 있습니다. 고사양 버전인 레이저의 경우도 LED 헤드램프 옵션으로 확인합니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "059",
            "optionName": "파워 전동 트렁크",
            "optionTypeCd": "01",
            "sort": 4,
            "imagePath": "/carsdata/option_images/option1-3.png",
            "description": "힘을 주지 않고 스위치로 트렁크를 쉽게 닫을 수 있는 기능입니다.",
            "group": False,
            "optionTitle": "파워 전동 트렁크",
            "groupOptionName": "파워 전동 트렁크",
            "location": "트렁크 라인 주변에 여닫이 스위치가 육안으로 확인 가능합니다.",
            "subOptions": None
        },
        {
            "optionCd": "080",
            "optionName": "고스트 도어 클로징",
            "optionTypeCd": "01",
            "sort": 5,
            "imagePath": "/carsdata/option_images/option1-4.png",
            "description": "전동 파워도어 시스템이라고도 불리며 탑승자가 도어를 완전히 닫지 않아도 도어 내부에 부착된 센서가 감지해 모터를 작동시켜 도어를 완전히 닫아 줍니다.",
            "group": False,
            "optionTitle": "고스트 도어 클로징",
            "groupOptionName": "고스트 도어 클로징",
            "location": "도어를 힘주어 완전히 닫지 않아도, 닫기 전까지의 상태가 되면 부드럽게 완전히 닫힙니다.",
            "subOptions": None
        },
        {
            "optionCd": "024",
            "optionName": "전동접이 사이드 미러",
            "optionTypeCd": "01",
            "sort": 6,
            "imagePath": "/carsdata/option_images/option1-5.png",
            "description": "좁은 공간이나 주차 시 사이드미러를 스위치로 접을 수 있는 기능입니다.",
            "group": False,
            "optionTitle": "전동접이 사이드 미러",
            "groupOptionName": "전동접이 사이드 미러",
            "location": "운전석 윈도우 스위치 주변에 주로 스위치가 있으며, 일부 튜닝된 차량은 스위치가 없이 접히기도 합니다. 스위치로 누르면 접히고 펴지는\n기능이 있거나, 시동 전후로 접고 펴지는 기능 중 한 가지를 충족하면 전동접이 사이드 미러로 확인합니다.",
            "subOptions": None
        },
        {
            "optionCd": "017",
            "optionName": "알루미늄 휠",
            "optionTypeCd": "01",
            "sort": 7,
            "imagePath": "/carsdata/option_images/option1-6.png",
            "description": "알루미늄 합금 재질로 만들어진 휠로서 일반 스틸 휠 보다 가볍습니다.",
            "group": False,
            "optionTitle": "알루미늄 휠",
            "groupOptionName": "알루미늄 휠",
            "location": "일반 스틸은 스틸 위에 플라스틱 재질의 커버를 씌우지만 알루미늄 휠은 커버를 따로 하지 않고 무게가 가벼워 연비에도 좋습니다. 스틸 휠과의 구분을\n위함으로, 스틸 휠이 아닌 크롬 휠 등 다양한 방식의 휠도 알루미늄 휠로 확인하고 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "062",
            "optionName": "루프랙",
            "optionTypeCd": "01",
            "sort": 8,
            "imagePath": "/carsdata/option_images/option1-7.png",
            "description": "차량의 지붕에 짐을 싣거나 고정의 용도로 사용하기 위해 세로로 설치된 2개의 봉으로 루프랙 또는 루프레일이라고 합니다.",
            "group": False,
            "optionTitle": "루프랙",
            "groupOptionName": "루프랙",
            "location": "차량의 루프에 세로로 설치된 2개의 레일이나 봉이 있는걸 육안으로 확인 가능합니다.",
            "subOptions": None
        },
        {
            "optionCd": "082",
            "optionName": "열선 스티어링 휠",
            "optionTypeCd": "01",
            "sort": 9,
            "imagePath": "/carsdata/option_images/option1-8.png",
            "description": "겨울철 차가운 스티어링 휠을 따뜻하게 해주는 기능입니다.",
            "group": False,
            "optionTitle": "열선 스티어링 휠",
            "groupOptionName": "열선 스티어링 휠",
            "location": "스티어링 휠 부분이나 센터패시아에 버튼이 대부분 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "083",
            "optionName": "전동 조절 스티어링 휠",
            "optionTypeCd": "01",
            "sort": 10,
            "imagePath": "/carsdata/option_images/option1-9.png",
            "description": "스티어링 휠을 틸트와 텔레스코픽을 전동으로 조절하여 운전자에 맞는 위치에 놓을 수 있습니다.",
            "group": False,
            "optionTitle": "전동 조절 스티어링 휠",
            "groupOptionName": "전동 조절 스티어링 휠",
            "location": "스티어링 휠 조정 스위치는 스티어링 휠 안쪽에 조절 할 수 있는 기능을 확인 할 수 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "084",
            "optionName": "패들 시프트",
            "optionTypeCd": "01",
            "sort": 11,
            "imagePath": "/carsdata/option_images/option1-10.png",
            "description": "스티어링 휠 부근에 레버 또는 버튼이 장착되어 기어 변속이 가능하고, 일부 전기, 하이브리드차는 회생 제동의 감도 조절이 가능합니다.",
            "group": False,
            "optionTitle": "패들 시프트",
            "groupOptionName": "패들 시프트",
            "location": "스티어링 휠 중심으로 좌우로 있으며, 일반적인 패들 방식과 함께 버튼 방식도 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "031",
            "optionName": "스티어링 휠 리모컨",
            "optionTypeCd": "01",
            "sort": 12,
            "imagePath": "/carsdata/option_images/option1-11.png",
            "description": "스티어링 휠에 장착된 버튼으로 오디오, 핸즈프리 장치를 편리하게 조작 할 수 있는 기능입니다.",
            "group": False,
            "optionTitle": "스티어링 휠 리모컨",
            "groupOptionName": "스티어링 휠 리모컨",
            "location": "스티어링 휠에 스위치가 장착되어 있는걸 확인 할 수 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "030",
            "optionName": "ECM 룸미러",
            "optionTypeCd": "01",
            "sort": 13,
            "imagePath": "/carsdata/option_images/option1-12.png",
            "description": "야간 주행 시 뒤 차량의 전조등에 의해 룸미러로 운전자에게 눈부심 현상을 없애주는 장치입니다.",
            "group": False,
            "optionTitle": "ECM 룸미러",
            "groupOptionName": "ECM 룸미러",
            "location": "미러에 있는 센서가 자동으로 눈부심을 방지해 주는 기능입니다. 룸미러 중앙 상단에 원형의 센서를 확인할 수 있으며, 프레임 리스 룸미러도 출시되어 평상시에는\n확인이 잘 안되는 것도 있으니 참고하시기 바랍니다.",
            "subOptions": None
        },
        {
            "optionCd": "074",
            "optionName": "하이패스",
            "optionTypeCd": "01",
            "sort": 14,
            "imagePath": "/carsdata/option_images/option1-13.png",
            "description": "유로 고속도로 톨게이트 출차 시 하이패스 단말기에 내장된 카드로 통행료가 자동으로 결제되는 시스템입니다.",
            "group": False,
            "optionTitle": "하이패스",
            "groupOptionName": "하이패스",
            "location": "룸미러에 내장되어 있는 경우가 많으며, 일부 모델이나 외부 시공 방식에 따라 대시보드 등 위치가 다를 수 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "006",
            "optionName": "파워 도어록",
            "optionTypeCd": "01",
            "sort": 15,
            "imagePath": "/carsdata/option_images/option1-14.png",
            "description": "운전석에서 도어록 스위치를 잠그면 모든 도어가 자동으로 닫히는 기능입니다.",
            "group": False,
            "optionTitle": "파워 도어록",
            "groupOptionName": "파워 도어록",
            "location": "운전석 좌측 윈도우 스위치 부근에 위치해 있으며, 스위치를 통해 전체의 문을 열고 닫을 수 있는 것을 확인할 수 있습니다. 일정 속도와 정지 시, 잠금 장치 작동 또는 해지 기능이 없는 차종도 있으니 참고하시기 바랍니다.",
            "subOptions": None
        },
        {
            "optionCd": "008",
            "optionName": "파워 스티어링 휠",
            "optionTypeCd": "01",
            "sort": 16,
            "imagePath": "/carsdata/option_images/option1-15.png",
            "description": "스티어링 휠을 돌리는데 다른 힘으로 보충해줘 쉽게 조향 할 수 있게 도와주는 기능입니다. 과거에는 유압식을 사용하였지만 최근에 와서는 전동식을 사용하는 추세입니다.",
            "group": False,
            "optionTitle": "파워 스티어링 휠",
            "groupOptionName": "파워 스티어링 휠",
            "location": "차량이 정지 시, 스티어링 휠을 돌릴 때 힘들이지 않고 돌릴 수 있다면 파워 스티어링 휠로 판단할 수 있습니다. 오래된 연식의 모델이 아니라면\n다마스 등 일부 차종을 제외한 대부분의 차량에 장착되어 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "007",
            "optionName": "파워 윈도우",
            "optionTypeCd": "01",
            "sort": 17,
            "imagePath": "/carsdata/option_images/option1-16.png",
            "description": "도어에 달린 유리 창문을 스위치로 쉽게 여닫을 수 있는 기능입니다.",
            "group": False,
            "optionTitle": "파워 윈도우",
            "groupOptionName": "파워 윈도우",
            "location": "도어 안쪽에 스위치가 장착되어 있습니다. 일부만 있는 차량도 있으며, 고급 옵션의 경우 원터치로 업다운이 되는 차량도 있습니다. 스위치로 윈도우를 움직일 수 있으면 파워 윈도우로 확인합니다.",
            "subOptions": None
        },
        {
            "optionCd": "002",
            "optionName": "에어백",
            "optionTypeCd": "02",
            "sort": 18,
            "imagePath": "/carsdata/option_images/option2-1.png",
            "description": "차량 충돌 때 충격으로부터 자동차 승객을 보호하는 장치이며 안전벨트와 더불어 대표적인 탑승객 보호장치입니다.",
            "group": True,
            "optionTitle": "에어백(운전석, 동승석)",
            "groupOptionName": "에어백",
            "location": "차량 충돌 때 충격으로부터 자동차 승객을 보호하는 장치이며 안전벨트와 더불어 대표적인 탑승객 보호장치입니다.",
            "subOptions": [
                {
                    "optionCd": "026",
                    "optionName": "에어백(운전석)",
                    "optionTypeCd": "02",
                    "sort": 18,
                    "imagePath": "/carsdata/option_images/option2-1.png",
                    "description": "차량 충돌 때 충격으로부터 자동차 승객을 보호하는 장치이며 안전벨트와 더불어 대표적인 탑승객 보호장치입니다.",
                    "group": False,
                    "optionTitle": "에어백(운전석, 동승석)",
                    "groupOptionName": "에어백(운전석)",
                    "location": "운전석은 스티어링 휠 중앙에 에어백이 장착된 문구를 확인할 수 있으며, 동승석의 경우 대시보드에 문구를 확인할 수 있습니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "027",
                    "optionName": "에어백(동승석)",
                    "optionTypeCd": "02",
                    "sort": 19,
                    "imagePath": "/carsdata/option_images/option2-1.png",
                    "description": "차량 충돌 때 충격으로부터 자동차 승객을 보호하는 장치이며 안전벨트와 더불어 대표적인 탑승객 보호장치입니다.",
                    "group": False,
                    "optionTitle": "에어백(운전석, 동승석)",
                    "groupOptionName": "에어백(동승석)",
                    "location": "운전석은 스티어링 휠 중앙에 에어백이 장착된 문구를 확인할 수 있으며, 동승석의 경우 대시보드에 문구를 확인할 수 있습니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "020",
            "optionName": "에어백(사이드)",
            "optionTypeCd": "02",
            "sort": 20,
            "imagePath": "/carsdata/option_images/option2-2.png",
            "description": "차량이 충돌할 때 탑승자의 측면을 보호하기 위해 운전석과 동승석에 장착하는 측면 에어백입니다.",
            "group": False,
            "optionTitle": "에어백(사이드)",
            "groupOptionName": "에어백(사이드)",
            "location": "운전석과 동승석 바깥쪽 시트 부분에 장착이 되어 문구로 확인이 가능하여 모델에 따라 뒷좌석 사이드 에어백이 별도 장착이 되기도 합니다.",
            "subOptions": None
        },
        {
            "optionCd": "056",
            "optionName": "에어백(커튼)",
            "optionTypeCd": "02",
            "sort": 21,
            "imagePath": "/carsdata/option_images/option2-3.png",
            "description": "차량의 측면 충돌 시 승객의 머리를 보호하기 위해 창문을 따라 길게 펼쳐지는 커튼 에어백입니다.",
            "group": False,
            "optionTitle": "에어백(커튼)",
            "groupOptionName": "에어백(커튼)",
            "location": "보통 차량 내부 필러쪽에 장착이 되며 필러쪽에 에어백 문구가 새겨져 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "001",
            "optionName": "브레이크 잠김 방지(ABS)",
            "optionTypeCd": "02",
            "sort": 22,
            "imagePath": "/carsdata/option_images/option2-4.png",
            "description": "급제동 시 바퀴가 잠기면 미끄러지거나 옆으로 밀려 운전자가 차의 방향을 제대로 제어할 수 없는 부분을 방지해주는 브레이크시스템이다.",
            "group": False,
            "optionTitle": "브레이크 잠김 방지(ABS)",
            "groupOptionName": "브레이크 잠김 방지(ABS)",
            "location": "엔진룸 안쪽에서 ABS 모듈의 확인이 가능하며, 시동 전 KEY ON 시 계기판에 ABS 경고등 점등으로 확인 가능합니다.",
            "subOptions": None
        },
        {
            "optionCd": "019",
            "optionName": "미끄럼 방지(TCS)",
            "optionTypeCd": "02",
            "sort": 23,
            "imagePath": "/carsdata/option_images/option2-5.png",
            "description": "미끄러운 노면에서 차량을 출발 및 가속 시 타이어가 헛돌지 않도록 차량의 구동력을 제어하는 시스템입니다.",
            "group": False,
            "optionTitle": "미끄럼 방지(TCS)",
            "groupOptionName": "미끄럼 방지(TCS)",
            "location": "TCS 모듈은 식별은 어렵지만, 운전석 주변에 TCS 스위치 등으로 확인할 수 있으며, 계기판의 경고등이나 설정 기능으로도 확인할 수 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "055",
            "optionName": "차체자세 제어장치(ESC)",
            "optionTypeCd": "02",
            "sort": 24,
            "imagePath": "/carsdata/option_images/option2-6.png",
            "description": "ABS, TCS는 전진/후진의 안전장치라면 ESC는 급회전 시 나타나는 차량의 언더스티어나 오버스티어가 일어날 경우 제어해줍니다. 각각의 제조사마다 명칭은 다르며 의미는 모두 비슷합니다. ESP, VDC, DSC 등 다양한 명칭 등을 사용하고 있습니다.",
            "group": False,
            "optionTitle": "차체자세 제어장치(ESC)",
            "groupOptionName": "차체자세 제어장치(ESC)",
            "location": "운전석 주변의 스위치나 계기판에서 확인할 수 있습니다. 2012년 1월 승용 자동차 및 4.5톤 이하인 완전 신차에 대해 장착 의무화되었으며, 1월 이전부터 생산\n및 변경만 된 차량은 2014년 7월 의무 장착되었습니다.",
            "subOptions": None
        },
        {
            "optionCd": "033",
            "optionName": "타이어 공기압센서(TPMS)",
            "optionTypeCd": "02",
            "sort": 25,
            "imagePath": "/carsdata/option_images/option2-7.png",
            "description": "차량의 4바퀴에 공기압을 측정하는 감지장치이며 운전자에게 경고로 알려주는 센서입니다. 2013년부터 신차 모델 중에 승용차, 3.5톤 이하 차량에는 의무화되었으며 2015년 1월부터 출고되는 모든 새 차들은 TPMS 장착이 의무화되었습니다.",
            "group": False,
            "optionTitle": "타이어 공기압센서(TPMS)",
            "groupOptionName": "타이어 공기압센서(TPMS)",
            "location": "타이어 안쪽에 센서가 있으나, 육안 확인이 어려운 경우가 많으며 계기판 TMPS 경고등 점등으로 확인 가능합니다.",
            "subOptions": None
        },
        {
            "optionCd": "088",
            "optionName": "차선이탈 경보 시스템(LDWS)",
            "optionTypeCd": "02",
            "sort": 26,
            "imagePath": "/carsdata/option_images/option2-8.png",
            "description": "방향지시등없이 차선을 이탈할 경우 운전자에게 경고음,신호등으로 알려주며 모델에 따라 다르지만 스티어링 휠에 진동을 줘 운전자에게 알리는 경우도 있습니다.",
            "group": False,
            "optionTitle": "차선이탈 경보 시스템(LDWS)",
            "groupOptionName": "차선이탈 경보 시스템(LDWS)",
            "location": "운전석 주변에 스위치나 계기판에서 확인할 수 있습니다. 룸미러 뒤쪽 앞유리에 레이더가 부착되며, 사양에 따라 경고신호 점멸이나 경고음만 주는\n차량도 있고, 차선을 강제로 유지해 주거나 스티어링 휠에서 진동으로 경고해 주는 기능이 있는 차량도 있습니다. 기본적인 경고신호나 경고음 등이 되는 경우 옵션으로 확인하고 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "002",
            "optionName": "전자제어 서스펜션(ECS)",
            "optionTypeCd": "02",
            "sort": 27,
            "imagePath": "/carsdata/option_images/option2-9.png",
            "description": "주행 환경에 따라 컴퓨터가 입력받아 차량의 높낮이 혹은 감쇠력을 조절하여 주행 안전성과 승차감을 자동 조정하는 장치입니다. 종류로는 전자제어 에어 서스펜션, 액티브 댐퍼 서스펜션, 액티브 프리뷰 서스펜션 등의 종류가 있습니다.",
            "group": False,
            "optionTitle": "전자제어 서스펜션(ECS)",
            "groupOptionName": "전자제어 서스펜션(ECS)",
            "location": "쇽업 쇼버의 구조 및 센서 등 많은 부품을 통해 작동하지만, 육안으로 확인은 어렵습니다. 차종에 따라 스위치가 있는 차량도 있으며, 전자제어 서스펜션은 서스펜션의 감쇠력을 조절하는 기능도 있고, 차고 조절을 하는 기능도 있습니다.  2가지 기능 중에 하나의 기능이 충족되면 전자제어 서스펜션 옵션으로 확인합니다.",
            "subOptions": None
        },
        {
            "optionCd": "003",
            "optionName": "주차감지센서",
            "optionTypeCd": "02",
            "sort": 28,
            "imagePath": "/carsdata/option_images/option2-10.png",
            "description": "주차 및 서행 시 앞쪽 범퍼와 뒤쪽 범퍼에 장착된 센서로 장애물을 감지하여 운전자에게 경고음이나 모니터 등으로 알려주는 시스템입니다.",
            "group": True,
            "optionTitle": "주차감지센서(전방, 후방)",
            "groupOptionName": "주차감지센서",
            "location": "주차 및 서행 시 앞쪽 범퍼와 뒤쪽 범퍼에 장착된 센서로 장애물을 감지하여 운전자에게 경고음이나 모니터 등으로 알려주는 시스템입니다.",
            "subOptions": [
                {
                    "optionCd": "085",
                    "optionName": "주차감지센서(전방)",
                    "optionTypeCd": "02",
                    "sort": 28,
                    "imagePath": "/carsdata/option_images/option2-10.png",
                    "description": "주차 및 서행 시 앞쪽 범퍼와 뒤쪽 범퍼에 장착된 센서로 장애물을 감지하여 운전자에게 경고음이나 모니터 등으로 알려주는 시스템입니다.",
                    "group": False,
                    "optionTitle": "주차감지센서(전방, 후방)",
                    "groupOptionName": "주차감지센서(전방)",
                    "location": "차량 범퍼에 센서가 2개에서 4개까지 보통 장착되어 있어서 육안으로 확인이 가능합니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "032",
                    "optionName": "주차감지센서(후방)",
                    "optionTypeCd": "02",
                    "sort": 29,
                    "imagePath": "/carsdata/option_images/option2-10.png",
                    "description": "주차 및 서행 시 앞쪽 범퍼와 뒤쪽 범퍼에 장착된 센서로 장애물을 감지하여 운전자에게 경고음이나 모니터 등으로 알려주는 시스템입니다.",
                    "group": False,
                    "optionTitle": "주차감지센서(전방, 후방)",
                    "groupOptionName": "주차감지센서(후방)",
                    "location": "차량 범퍼에 센서가 2개에서 4개까지 보통 장착되어 있어서 육안으로 확인이 가능합니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "086",
            "optionName": "후측방 경보 시스템",
            "optionTypeCd": "02",
            "sort": 30,
            "imagePath": "/carsdata/option_images/option2-11.png",
            "description": "주행 중 차선을 바꿀 때 후측방(사각지대)에서 접근하는 차량을 감지해 운전자에서 알려주는 기능입니다.",
            "group": False,
            "optionTitle": "후측방 경보 시스템",
            "groupOptionName": "후측방 경보 시스템",
            "location": "사이드 미러에 후측방 경보 아이콘이 있으며, 운전석 주변에 스위치가 있는 경우도 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "058",
            "optionName": "후방 카메라",
            "optionTypeCd": "02",
            "sort": 31,
            "imagePath": "/carsdata/option_images/option2-12.png",
            "description": "트렁크 또는 번호판 주변에 카메라를 장착하여 주차 및 후진 시 모니터를 통해 후방을 확인 할 수 있는 기능입니다.",
            "group": False,
            "optionTitle": "후방 카메라",
            "groupOptionName": "후방 카메라",
            "location": "후진기어 R 위치에 놓으면 센터패시아에 놓인 모니터나 혹은 룸미러에서 확인할 수 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "087",
            "optionName": "360도 어라운드 뷰",
            "optionTypeCd": "02",
            "sort": 32,
            "imagePath": "/carsdata/option_images/option2-13.png",
            "description": "주차 및 전방 서행 시 차량 주변을 360도 모니터로 보여주는 기능으로 공간 인지가 쉬워 주차 및 협소한 장소를 편리하게 주행할 수 있게 도와주는 기능입니다.",
            "group": False,
            "optionTitle": "360도 어라운드 뷰",
            "groupOptionName": "360도 어라운드 뷰",
            "location": "차량 외부에 카메라가 장착되어 있으며, 모니터로 뷰를 확인할 수 있습니다. 일부 차종은 전방 등을 제외한 화면이 보이는 경우도 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "004",
            "optionName": "크루즈 컨트롤",
            "optionTypeCd": "03",
            "sort": 33,
            "imagePath": "/carsdata/option_images/option3-1.png",
            "description": "운전자가 속도를 설정하면 운전자가 페달을 밟지 않아도 속도를 유지해주는 장치입니다. 어댑티브은 기존 크루즈 컨트롤의 추가 장착된 기능으로 속도 및 앞차와의 거리를 설정해 앞차가 속도를 줄이면 자동으로 속도까지 줄여주는 기능입니다.",
            "group": True,
            "optionTitle": "크루즈 컨트롤(일반, 어댑티브)",
            "groupOptionName": "크루즈 컨트롤",
            "location": "운전자가 속도를 설정하면 운전자가 페달을 밟지 않아도 속도를 유지해주는 장치입니다. 어댑티브은 기존 크루즈 컨트롤의 추가 장착된 기능으로 속도 및 앞차와의 거리를 설정해 앞차가 속도를 줄이면 자동으로 속도까지 줄여주는 기능입니다.",
            "subOptions": [
                {
                    "optionCd": "068",
                    "optionName": "크루즈 컨트롤(일반)",
                    "optionTypeCd": "03",
                    "sort": 33,
                    "imagePath": "/carsdata/option_images/option3-1.png",
                    "description": "운전자가 속도를 설정하면 운전자가 페달을 밟지 않아도 속도를 유지해주는 장치입니다. 어댑티브은 기존 크루즈 컨트롤의 추가 장착된 기능으로 속도 및 앞차와의 거리를 설정해 앞차가 속도를 줄이면 자동으로 속도까지 줄여주는 기능입니다.",
                    "group": False,
                    "optionTitle": "크루즈 컨트롤(일반, 어댑티브)",
                    "groupOptionName": "크루즈 컨트롤(일반)",
                    "location": "크루즈 컨트롤은 스티어링 휠 주변에서 스위치를 확인할 수 있으며, 어댑티브는 차량 전면부에 레이더가 적용되며 계기판 설정으로 확인할 수 있습니다. 어댑티브는 기본적으로 차간 거리를 설정해 속도를 조절해 주는 기능이 되는 것을 옵션으로 확인합니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "079",
                    "optionName": "크루즈 컨트롤(어댑티브)",
                    "optionTypeCd": "03",
                    "sort": 34,
                    "imagePath": "/carsdata/option_images/option3-1.png",
                    "description": "운전자가 속도를 설정하면 운전자가 페달을 밟지 않아도 속도를 유지해주는 장치입니다. 어댑티브은 기존 크루즈 컨트롤의 추가 장착된 기능으로 속도 및 앞차와의 거리를 설정해 앞차가 속도를 줄이면 자동으로 속도까지 줄여주는 기능입니다.",
                    "group": False,
                    "optionTitle": "크루즈 컨트롤(일반, 어댑티브)",
                    "groupOptionName": "크루즈 컨트롤(어댑티브)",
                    "location": "크루즈 컨트롤은 스티어링 휠 주변에서 스위치를 확인할 수 있으며, 어댑티브는 차량 전면부에 레이더가 적용되며 계기판 설정으로 확인할 수 있습니다. 어댑티브는 기본적으로 차간 거리를 설정해 속도를 조절해 주는 기능이 되는 것을 옵션으로 확인합니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "095",
            "optionName": "헤드업 디스플레이(HUD)",
            "optionTypeCd": "03",
            "sort": 35,
            "imagePath": "/carsdata/option_images/option3-2.png",
            "description": "운전자의 앞 유리에 차량의 정보를 투영하여 운전자가 쉽게 정보(속도, 내비게이션)를 확인 할 수 있는 기능입니다.",
            "group": False,
            "optionTitle": "헤드업 디스플레이(HUD)",
            "groupOptionName": "헤드업 디스플레이(HUD)",
            "location": "운전석 앞 대시보드에서 유리로 투영할 수 있는 장치가 있어 육안으로 확인할 수 있으며, 운전석 주변에 스위치가 있는 차량도 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "094",
            "optionName": "전자식 주차브레이크(EPB)",
            "optionTypeCd": "03",
            "sort": 36,
            "imagePath": "/carsdata/option_images/option3-3.png",
            "description": "차량을 주차한 후에는 주차브레이크를 손이나 발로 잠그지 않고 손가락으로 쉽게 조작할 수 있는 기능입니다. 또한 자동으로 브레이크 해지 또한 가능해 주차브레이크를 잠금 상태로 주행하는 것을 예방할 수 있습니다.",
            "group": False,
            "optionTitle": "전자식 주차브레이크(EPB)",
            "groupOptionName": "전자식 주차브레이크(EPB)",
            "location": "운전석 또는 변속기 주변에 위치하고 있으며 스위치 방식으로 되어 작동합니다.",
            "subOptions": None
        },
        {
            "optionCd": "023",
            "optionName": "자동 에어컨",
            "optionTypeCd": "03",
            "sort": 37,
            "imagePath": "/carsdata/option_images/option3-4.png",
            "description": "사용자가 원하는 온도 설정 시 풍량, 온도 등을 자동으로 조절하여 일정한 온도를 유지해 주는 에어컨입니다. 듀얼 풀 오토 에어컨의 경우는 동승석의 온도를 독립적으로 조절할 수 있습니다.",
            "group": False,
            "optionTitle": "자동 에어컨",
            "groupOptionName": "자동 에어컨",
            "location": "공조 시스템은 센터페시아에 위치하고 있으며, AUTO 버튼이 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "057",
            "optionName": "스마트키",
            "optionTypeCd": "03",
            "sort": 38,
            "imagePath": "/carsdata/option_images/option3-5.png",
            "description": "스마트키를 몸에 지니는 것만으로도 도어 잠금장치를 해지할 수 있거나 버튼을 눌러 시동까지 걸 수 있는 편의장치입니다.",
            "group": False,
            "optionTitle": "스마트키",
            "groupOptionName": "스마트키",
            "location": "스마트키는 외관상 열쇠 모양을 하고 있지 않으며 스마트키를 소지하고 문을 열거나 (KEYLESS ENTRY) 시동이 가능한 (KEYLESS GO) 기능이 있는데, 2가지 기능 중에 하나의 기능이\n충족되면 스마트키의 옵션으로 확인합니다.",
            "subOptions": None
        },
        {
            "optionCd": "015",
            "optionName": "무선도어 잠금장치",
            "optionTypeCd": "03",
            "sort": 39,
            "imagePath": "/carsdata/option_images/option3-6.png",
            "description": "열쇠를 도어에 꽂지 않고 차량을 무선 리모컨으로 잠금/해지 가능한 편의장치입니다.",
            "group": False,
            "optionTitle": "무선도어 잠금장치",
            "groupOptionName": "무선도어 잠금장치",
            "location": "자동차 키에 잠금/해지 리모컨 버튼이 부착되어 있거나 열쇠와 함께 리모컨이 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "081",
            "optionName": "레인센서",
            "optionTypeCd": "03",
            "sort": 40,
            "imagePath": "/carsdata/option_images/option3-7.png",
            "description": "앞 유리창에 빗물이 떨어지는 걸 감지해 와이퍼가 자동으로 앞유리 물을 닦아줍니다. 빗줄기의 양에 따라 와이퍼 속도도 자동 조절됩니다.",
            "group": False,
            "optionTitle": "레인센서",
            "groupOptionName": "레인센서",
            "location": "스티어링 휠 주변 와이퍼 조절 스위치에서 확인 가능합니다. AUTO 버튼이 있으며 앞 유리 상단에 감지 센서가 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "097",
            "optionName": "오토 라이트",
            "optionTypeCd": "03",
            "sort": 41,
            "imagePath": "/carsdata/option_images/option3-8.png",
            "description": "차량의 라이트를 수동으로 조작하지 않고 터널이나 주변에 어둠을 감지하여 자동 ON/OFF 제어하는 기능입니다.",
            "group": False,
            "optionTitle": "오토 라이트",
            "groupOptionName": "오토 라이트",
            "location": "스티어링 휠 주변 헤드램프 조절 스위치에서 확인 가능합니다. AUTO 버튼이 있으며 대시보드 앞쪽에 감지 센서가 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "005",
            "optionName": "커튼/블라인드",
            "optionTypeCd": "03",
            "sort": 42,
            "imagePath": "/carsdata/option_images/option3-9.png",
            "description": "햇빛을 차단해 주는 커튼/블라인드입니다.",
            "group": True,
            "optionTitle": "커튼/블라인드(뒷좌석, 후방)",
            "groupOptionName": "커튼/블라인드",
            "location": "햇빛을 차단해 주는 커튼/블라인드입니다.",
            "subOptions": [
                {
                    "optionCd": "092",
                    "optionName": "커튼/블라인드(뒷좌석)",
                    "optionTypeCd": "03",
                    "sort": 42,
                    "imagePath": "/carsdata/option_images/option3-9.png",
                    "description": "햇빛을 차단해 주는 커튼/블라인드입니다.",
                    "group": False,
                    "optionTitle": "커튼/블라인드(뒷좌석, 후방)",
                    "groupOptionName": "커튼/블라인드(뒷좌석)",
                    "location": "뒷좌석의 도어 창문 주변에 수동/자동으로 커튼을 칠 수 있는 장치가 있으며, 자동인 경우 도어 주변에 스위치가 있으며, 후방은 뒷유리 쪽 커튼으로 수동/자동으로 커튼을\n칠 수 있는 장치가 있으며, 자동인 경우 앞/뒤로 스위치가 있습니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "093",
                    "optionName": "커튼/블라인드(후방)",
                    "optionTypeCd": "03",
                    "sort": 43,
                    "imagePath": "/carsdata/option_images/option3-9.png",
                    "description": "햇빛을 차단해 주는 커튼/블라인드입니다.",
                    "group": False,
                    "optionTitle": "커튼/블라인드(뒷창문, 후방)",
                    "groupOptionName": "커튼/블라인드(후방)",
                    "location": "뒷좌석의 도어 창문 주변에 수동/자동으로 커튼을 칠 수 있는 장치가 있으며, 자동인 경우 도어 주변에 스위치가 있으며, 후방은 뒷유리 쪽 커튼으로 수동/자동으로 커튼을\n칠 수 있는 장치가 있으며, 자동인 경우 앞/뒤로 스위치가 있습니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "005",
            "optionName": "내비게이션",
            "optionTypeCd": "03",
            "sort": 44,
            "imagePath": "/carsdata/option_images/option3-10.png",
            "description": "목적지를 설정하면 GPS가 내장된 모니터에서 길 안내, 각종 교통정보를 제공해 줍니다.",
            "group": False,
            "optionTitle": "내비게이션",
            "groupOptionName": "내비게이션",
            "location": "센터페시아에 모니터 화면이 장착되어 차량의 위치가 지도상에 확인되며 목적지 설정이 가능합니다.",
            "subOptions": None
        },
        {
            "optionCd": "004",
            "optionName": "앞좌석 AV 모니터",
            "optionTypeCd": "03",
            "sort": 45,
            "imagePath": "/carsdata/option_images/option3-11.png",
            "description": "차량 내부에 TV, 비디오와 같은 영상 시스템을 갖춘 장치입니다.",
            "group": False,
            "optionTitle": "앞좌석 AV 모니터",
            "groupOptionName": "앞좌석 AV 모니터",
            "location": "센터페시아에 모니터 화면이 장착되어 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "054",
            "optionName": "뒷좌석 AV 모니터",
            "optionTypeCd": "03",
            "sort": 46,
            "imagePath": "/carsdata/option_images/option3-12.png",
            "description": "차량 내부에 TV, 비디오와 같은 영상 시스템을 갖춘 장치입니다.",
            "group": False,
            "optionTitle": "뒷좌석 AV 모니터",
            "groupOptionName": "뒷좌석 AV 모니터",
            "location": "앞좌석 시트 뒤에 설치되는 경우가 많으며, 일부 차종은 앞좌석 암레스트, 루프 등에 장착되기도 합니다.",
            "subOptions": None
        },
        {
            "optionCd": "096",
            "optionName": "블루투스",
            "optionTypeCd": "03",
            "sort": 47,
            "imagePath": "/carsdata/option_images/option3-13.png",
            "description": "스마트폰을 차량의 블루투스 기능이 되는 오디오와 무선으로 연결해 전화 및 음악 등의 각종 파일 및 정보 등을 이용할 수 있는 기능입니다.",
            "group": False,
            "optionTitle": "블루투스",
            "groupOptionName": "블루투스",
            "location": "오디오 설정에서 기능을 확인할 수 있습니다. 블루투스는 음악 감상이 가능한 오디오 스트리밍 기능과 전화를 할 수 있는 핸즈프리 가능이 있습니다. 2가지 기능 중에 하나의 기능이\n충족되면 블루투스 옵션으로 확인합니다. 일부 내비게이션 등을 시공하는 과정에서 기능이 상실되는 경우가 있으니 정상 작동여부를 확인하시기 바랍니다.",
            "subOptions": None
        },
        {
            "optionCd": "003",
            "optionName": "CD 플레이어",
            "optionTypeCd": "03",
            "sort": 48,
            "imagePath": "/carsdata/option_images/option3-14.png",
            "description": "음악이 저장된 CD를 재생시키는 장치입니다.",
            "group": False,
            "optionTitle": "CD 플레이어",
            "groupOptionName": "CD 플레이어",
            "location": "CD를 재생시킬 수 있는 플레이어 또는 체인저로 되어 센터페시아에 위치하고 있습니다. 경우에 따라 콘솔박스, 트렁크 등에 설치된 경우도 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "072",
            "optionName": "USB 단자",
            "optionTypeCd": "03",
            "sort": 49,
            "imagePath": "/carsdata/option_images/option3-15.png",
            "description": "USB 연결 잭을 통한 외부입력으로 MP3, PMP 등과 같은 휴대용 장치의 음악을 차량의 오디오에서 감상할 수 있게 만들어주는 단자입니다.",
            "group": False,
            "optionTitle": "USB 단자",
            "groupOptionName": "USB 단자",
            "location": "USB 단자는 센터패시아 하단에 있는 경우가 대부분이며 일부 콘솔박스에 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "071",
            "optionName": "AUX 단자",
            "optionTypeCd": "03",
            "sort": 50,
            "imagePath": "/carsdata/option_images/option3-16.png",
            "description": "AUX 연결 잭을 통한 외부입력으로 MP3, PMP 등과 같은 휴대용 장치의 음악을 차량의 오디오에서 감상할 수 있게 만들어주는 단자입니다.",
            "group": False,
            "optionTitle": "AUX 단자",
            "groupOptionName": "AUX 단자",
            "location": "AUX 단자는 센터패시아 하단에 있는 경우가 대부분이며 일부 콘솔박스에 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "014",
            "optionName": "가죽시트",
            "optionTypeCd": "04",
            "sort": 51,
            "imagePath": "/carsdata/option_images/option4-1.png",
            "description": "차량의 좌석 재질이 가죽, 스웨이드 그리고 직물+가죽 혼합의 재질로 사용된 시트를 가죽시트로 봅니다.",
            "group": False,
            "optionTitle": "가죽시트",
            "groupOptionName": "가죽시트",
            "location": "시트의 재질이 직물이 아닌 가죽이나 가죽 느낌의 재질로 만든 부분을 확인할 수 있습니다. 사양에 따라 인조, 천연, 스웨이드, 직물과 혼합된 시트 등으로 종류가 다양하며\n종류에 관계없이 가죽시트로 확인합니다.",
            "subOptions": None
        },
        {
            "optionCd": "006",
            "optionName": "전동시트",
            "optionTypeCd": "04",
            "sort": 52,
            "imagePath": "/carsdata/option_images/option4-2.png",
            "description": "스위치로 시트의 높낮이, 앞뒤, 등받이 기울기를 원하는 위치로 편리하게 조절할 수 있는 기능입니다.",
            "group": True,
            "optionTitle": "전동시트(운전석, 동승석)",
            "groupOptionName": "전동시트",
            "location": "스위치로 시트의 높낮이, 앞뒤, 등받이 기울기를 원하는 위치로 편리하게 조절할 수 있는 기능입니다.",
            "subOptions": [
                {
                    "optionCd": "021",
                    "optionName": "전동시트(운전석)",
                    "optionTypeCd": "04",
                    "sort": 52,
                    "imagePath": "/carsdata/option_images/option4-2.png",
                    "description": "스위치로 시트의 높낮이, 앞뒤, 등받이 기울기를 원하는 위치로 편리하게 조절할 수 있는 기능입니다.",
                    "group": False,
                    "optionTitle": "전동시트(운전석, 동승석)",
                    "groupOptionName": "전동시트(운전석)",
                    "location": "시트 아래나 도어 쪽에 스위치가 있으며, 높낮이, 앞뒤, 등받이 기능 중에 일부 기능이 없는 전동시트도 있습니다. 3가지 기능 중에 하나의 기능이 충족되면\n전동시트 옵션으로 확인합니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "035",
                    "optionName": "전동시트(동승석)",
                    "optionTypeCd": "04",
                    "sort": 53,
                    "imagePath": "/carsdata/option_images/option4-2.png",
                    "description": "스위치로 시트의 높낮이, 앞뒤, 등받이 기울기를 원하는 위치로 편리하게 조절할 수 있는 기능입니다.",
                    "group": False,
                    "optionTitle": "전동시트(운전석, 동승석)",
                    "groupOptionName": "전동시트(동승석)",
                    "location": "시트 아래나 도어 쪽에 스위치가 있으며, 높낮이, 앞뒤, 등받이 기능 중에 일부 기능이 없는 전동시트도 있습니다. 3가지 기능 중에 하나의 기능이 충족되면\n전동시트 옵션으로 확인합니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "089",
            "optionName": "전동시트(뒷좌석)",
            "optionTypeCd": "04",
            "sort": 54,
            "imagePath": "/carsdata/option_images/option4-3.png",
            "description": "보통 대형차에서 접할 수 있으며 스위치로 시트의 높낮이, 앞뒤, 등받이 기울기를 원하는 위치로 편리하게 조절할 수 있는 기능입니다.",
            "group": False,
            "optionTitle": "전동시트(뒷좌석)",
            "groupOptionName": "전동시트(뒷좌석)",
            "location": "뒷좌석 도어나 센터 암레스트에서 스위치를 확인할 수 있습니다. SUV 등 폴딩을 전동 스위치로 조절하는 차량도 뒷좌석 전동시트로 볼 수 있습니다.",
            "subOptions": None
        },
        {
            "optionCd": "007",
            "optionName": "열선시트",
            "optionTypeCd": "04",
            "sort": 55,
            "imagePath": "/carsdata/option_images/option4-4.png",
            "description": "겨울철 스위치 ONOFF로 시트를 따뜻하게 해주는 기능입니다.",
            "group": True,
            "optionTitle": "열선시트(앞좌석, 뒷좌석)",
            "groupOptionName": "열선시트",
            "location": "겨울철 스위치 ONOFF로 시트를 따뜻하게 해주는 기능입니다.",
            "subOptions": [
                {
                    "optionCd": "022",
                    "optionName": "열선시트(앞좌석)",
                    "optionTypeCd": "04",
                    "sort": 55,
                    "imagePath": "/carsdata/option_images/option4-4.png",
                    "description": "겨울철 스위치 ONOFF로 시트를 따뜻하게 해주는 기능입니다.",
                    "group": False,
                    "optionTitle": "열선시트(앞좌석, 뒷좌석)",
                    "groupOptionName": "열선시트(앞좌석)",
                    "location": "앞좌석은 변속기나 센터페시아 주변에 위치하고 있으며, 뒷좌석은 뒷도어 윈도우 스위치나 리어 에어벤트, 리어 암레스트 주변에 있습니다. 스위치 작동 시\n시트가 따뜻해집니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "063",
                    "optionName": "열선시트(뒷좌석)",
                    "optionTypeCd": "04",
                    "sort": 56,
                    "imagePath": "/carsdata/option_images/option4-4.png",
                    "description": "겨울철 스위치 ONOFF로 시트를 따뜻하게 해주는 기능입니다.",
                    "group": False,
                    "optionTitle": "열선시트(앞좌석, 뒷좌석)",
                    "groupOptionName": "열선시트(뒷좌석)",
                    "location": "앞좌석은 변속기나 센터페시아 주변에 위치하고 있으며, 뒷좌석은 뒷도어 윈도우 스위치나 리어 에어벤트, 리어 암레스트 주변에 있습니다. 스위치 작동 시\n시트가 따뜻해집니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "008",
            "optionName": "메모리 시트",
            "optionTypeCd": "04",
            "sort": 57,
            "imagePath": "/carsdata/option_images/option4-5.png",
            "description": "운전석 및 동승석에 편한 위치에 시트를 고정해 두고 해당 위치를 기억하게 설정해두면 버튼으로 편하게 그 위치로 조정해 주는 기능입니다. 그리고 다른 운전자가 좌석 위치를 다르게 조작해 놓았을 때 편리하게 사용 할 수 있습니다. ",
            "group": True,
            "optionTitle": "메모리 시트(운전석, 동승석)",
            "groupOptionName": "메모리 시트",
            "location": "운전석 및 동승석에 편한 위치에 시트를 고정해 두고 해당 위치를 기억하게 설정해두면 버튼으로 편하게 그 위치로 조정해 주는 기능입니다. 그리고 다른 운전자가 좌석 위치를 다르게 조작해 놓았을 때 편리하게 사용 할 수 있습니다. ",
            "subOptions": [
                {
                    "optionCd": "051",
                    "optionName": "메모리 시트(운전석)",
                    "optionTypeCd": "04",
                    "sort": 57,
                    "imagePath": "/carsdata/option_images/option4-5.png",
                    "description": "운전석 및 동승석에 편한 위치에 시트를 고정해 두고 해당 위치를 기억하게 설정해두면 버튼으로 편하게 그 위치로 조정해 주는 기능입니다. 그리고 다른 운전자가 좌석 위치를 다르게 조작해 놓았을 때 편리하게 사용 할 수 있습니다. ",
                    "group": False,
                    "optionTitle": "메모리 시트(운전석, 동승석)",
                    "groupOptionName": "메모리 시트(운전석)",
                    "location": "도어트림이나 시트 하단에 위치하고 있으며, 세팅을 하고 번호를 지정하면 조정한 시트의 내용이 저장됩니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "078",
                    "optionName": "메모리 시트(동승석)",
                    "optionTypeCd": "04",
                    "sort": 58,
                    "imagePath": "/carsdata/option_images/option4-5.png",
                    "description": "운전석 및 동승석에 편한 위치에 시트를 고정해 두고 해당 위치를 기억하게 설정해두면 버튼으로 편하게 그 위치로 조정해 주는 기능입니다. 그리고 다른 운전자가 좌석 위치를 다르게 조작해 놓았을 때 편리하게 사용 할 수 있습니다. ",
                    "group": False,
                    "optionTitle": "메모리 시트(운전석, 동승석)",
                    "groupOptionName": "메모리 시트(동승석)",
                    "location": "도어트림이나 시트 하단에 위치하고 있으며, 세팅을 하고 번호를 지정하면 조정한 시트의 내용이 저장됩니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "009",
            "optionName": "통풍시트",
            "optionTypeCd": "04",
            "sort": 59,
            "imagePath": "/carsdata/option_images/option4-6.png",
            "description": "더운 날씨에 에어컨에 닿지 않는 엉덩이 부분을 통풍시트 스위치를 작동시켜 시트에 시원한 공기를 순환시켜 열을 제거해 쾌적함을 유지해 줍니다.",
            "group": True,
            "optionTitle": "통풍시트(운전석, 동승석)",
            "groupOptionName": "통풍시트",
            "location": "더운 날씨에 에어컨에 닿지 않는 엉덩이 부분을 통풍시트 스위치를 작동시켜 시트에 시원한 공기를 순환시켜 열을 제거해 쾌적함을 유지해 줍니다.",
            "subOptions": [
                {
                    "optionCd": "034",
                    "optionName": "통풍시트(운전석)",
                    "optionTypeCd": "04",
                    "sort": 59,
                    "imagePath": "/carsdata/option_images/option4-6.png",
                    "description": "더운 날씨에 에어컨에 닿지 않는 엉덩이 부분을 통풍시트 스위치를 작동시켜 시트에 시원한 공기를 순환시켜 열을 제거해 쾌적함을 유지해 줍니다.",
                    "group": False,
                    "optionTitle": "통풍시트(운전석, 동승석)",
                    "groupOptionName": "통풍시트(운전석)",
                    "location": "변속기나 센터페시아 주변에 위치하고 있으며, 스위치 작동 시 시원한 공기가 느껴집니다.",
                    "subOptions": None
                },
                {
                    "optionCd": "077",
                    "optionName": "통풍시트(동승석)",
                    "optionTypeCd": "04",
                    "sort": 60,
                    "imagePath": "/carsdata/option_images/option4-6.png",
                    "description": "더운 날씨에 에어컨에 닿지 않는 엉덩이 부분을 통풍시트 스위치를 작동시켜 시트에 시원한 공기를 순환시켜 열을 제거해 쾌적함을 유지해 줍니다.",
                    "group": False,
                    "optionTitle": "통풍시트(운전석, 동승석)",
                    "groupOptionName": "통풍시트(동승석)",
                    "location": "변속기나 센터페시아 주변에 위치하고 있으며, 스위치 작동 시 시원한 공기가 느껴집니다.",
                    "subOptions": None
                }
            ]
        },
        {
            "optionCd": "090",
            "optionName": "통풍시트(뒷좌석)",
            "optionTypeCd": "04",
            "sort": 61,
            "imagePath": "/carsdata/option_images/option4-7.png",
            "description": "뒷좌석에도 별도의 통풍시트 기능으로 더운 날씨에 에어컨에 닿지 않는 엉덩이 부분을 통풍시트 스위치를 작동시켜 시트에 시원한 공기를 순환시켜 열을 제어해 쾌적함을 유지해 줍니다.",
            "group": False,
            "optionTitle": "통풍시트(뒷좌석)",
            "groupOptionName": "통풍시트(뒷좌석)",
            "location": "뒷도어 윈도우 스위치나 리어 에어벤트, 리어 암레스트 주변에 있으며, 스위치 작동 시 시원한 공기가 느껴집니다.",
            "subOptions": None
        },
        {
            "optionCd": "091",
            "optionName": "마사지 시트",
            "optionTypeCd": "04",
            "sort": 62,
            "imagePath": "/carsdata/option_images/option4-8.png",
            "description": "안마시트 라고도 칭하고 있으며 자동차 시트에 마사지 기능이 추가되어 피로감을 풀어주는 기능입니다.",
            "group": False,
            "optionTitle": "마사지 시트",
            "groupOptionName": "마사지 시트",
            "location": "앞좌석이나 뒷좌석의 전체나 일부에 기능이 있으며, 스위치 작동 시 시트에 에어 튜브 등으로 등받이 쪽으로 마사지 작동 여부를 알 수 있습니다.",
            "subOptions": None
        }
    ]




truck_options = [
        {
            "optionCd": "001",
            "optionName": "리프트(파워게이트)",
            "optionTypeCd": "01",
            "sort": 10,
            "imagePath": "/carsdata/option_images/tr_option1-1.jpg",
            "description": "부피가 큰 적재물의 상하차를 위한 적재함 보조장치"
        },
        {
            "optionCd": "002",
            "optionName": "알루미늄휠",
            "optionTypeCd": "01",
            "sort": 20,
            "imagePath": "/carsdata/option_images/option1-1.jpg",
            "description": "알루미늄 합금 재질로 만들어진 휠로서 일반 스틸 휠보다 장점이 많다.<br>첫 번째는 가벼워서 연료소비가 적고, 서스펜션에 부담을 줄여 주행 성능을 향상시킨다. 두 번째는 열 전도율이 3배가량 높으므로 노면 마찰로 인해 타이어에 발생하는 열을 빠르게 흡수하고 발산시켜서 타이어와 브레이크의 성능이 향상된다. 세 번째로 충격 흡수력이 2배 이상 뛰어나 타이어와 노면의 충격을 완화해 승차감 향상에 도움을 준다. "
        },
        {
            "optionCd": "003",
            "optionName": "선루프",
            "optionTypeCd": "01",
            "sort": 30,
            "imagePath": "/carsdata/option_images/option2-9.jpg",
            "description": "자동차 지붕에 고강도 유리로 창틀을 만들어 지붕 일부 또는 전부를 개폐할 수 있는 장치.<br>실내 온도가 올라가거나 탁할 때 지붕을 열어서 차량 내부의 공기를 빠르게 환기할 수 있으며, 탁 트인 개방감을 주어 쾌적한 운전에 도움을 준다. 선루프에 사용되는 유리는 대부분 특수 열처리가 되어 자외선과 적외선을 차단하는 효과가 있다. "
        },
        {
            "optionCd": "004",
            "optionName": "전동접이 사이드미러",
            "optionTypeCd": "01",
            "sort": 40,
            "imagePath": "/carsdata/option_images/option2-6.jpg",
            "description": "사이드미러 속에 전동모터를 내장하여 차내에서 조작 버튼을 누르면 사이드미러를 자동으로 접거나 펼 수 있는 시스템.<br>차량시동을 끄면 자동으로 접히거나 운전자에 따른 설정 위치를 기억시켜 놓을 수 있는 차량도 있다."
        },
        {
            "optionCd": "005",
            "optionName": "전동 틸팅캡",
            "optionTypeCd": "01",
            "sort": 50,
            "imagePath": "/carsdata/option_images/tr_option1-5.jpg",
            "description": "토션바가 장착되어 캡을 손쉽게 들어올릴 수 있음으로써 정비공간 확보에 용이한 기능"
        },
        {
            "optionCd": "006",
            "optionName": "루프 스포일러",
            "optionTypeCd": "01",
            "sort": 60,
            "imagePath": "/carsdata/option_images/tr_option1-6.jpg",
            "description": "차량을 운행할때 전방으로부터 받는 공기의 저항을 감소시키는 목적으로 루프에 장착하는 장치 "
        },
        {
            "optionCd": "007",
            "optionName": "PTO",
            "optionTypeCd": "01",
            "sort": 70,
            "imagePath": "/carsdata/option_images/tr_option1-7.jpg",
            "description": "엔진 동력을 추출하여 윈치나 펌프 등을 구동하는 장치로 특수기계, 크레인 등에 연결하여 사용한다."
        },
        {
            "optionCd": "008",
            "optionName": "자동 호루 덮개",
            "optionTypeCd": "01",
            "sort": 80,
            "imagePath": "/carsdata/option_images/tr_option1-8.jpg",
            "description": "적재물 낙하를 방지하기 위한 덮개의 개폐를 자동으로 조절하는 장치"
        },
        {
            "optionCd": "009",
            "optionName": "그리스 주유기",
            "optionTypeCd": "01",
            "sort": 90,
            "imagePath": "/carsdata/option_images/tr_option1-9.jpg",
            "description": "자동윤활시스템으로 마찰과 열이 발생하는 곳에 자동으로 그리스를 주유하여 윤활작업을 진행한다."
        },
        {
            "optionCd": "010",
            "optionName": "매연저감장치",
            "optionTypeCd": "01",
            "sort": 100,
            "imagePath": "/carsdata/option_images/tr_option1-10.jpg",
            "description": "디젤엔진의 배기가스 내 유해물질을 저감하기 위한 장치"
        },
        {
            "optionCd": "011",
            "optionName": "스티어링 휠 리모컨",
            "optionTypeCd": "02",
            "sort": 110,
            "imagePath": "/carsdata/option_images/option2-11.jpg",
            "description": "운전대에 장착된 버튼으로 오디오, 핸즈프리 등의 각종 장치를 편리하게 조작할 수 있는 시스템.<br>특히 오디오는 전원, 음량, 재생 등의 조작이 가능하며, 운전대 중앙의 양옆이나 하단에 위치한다. 주행 중에 편리하게 이용할 수 있어 안전운전에 많은 도움을 준다. "
        },
        {
            "optionCd": "012",
            "optionName": "파워 스티어링",
            "optionTypeCd": "02",
            "sort": 120,
            "imagePath": "/carsdata/option_images/option2-2.jpg",
            "description": "조향 시 엔진의 구동력을 이용해 적은 힘으로도 운전대를 가볍게 돌릴 수 있게 해주는 시스템.<br>운전자가 운전대를 돌리면 센서가 회전 방향과 속도 등을 감지하여 전기모터를 돌려 차량 앞바퀴에 적절한 구동력을 전달해 준다. 주차 시나 저속에서는 파워의 효력이 강해지고, 고속에서는 안정성을 위해 효력이 약해져서 스티어링 휠이 무거워지는 속도감응식 파워스티어링도 많이 사용된다."
        },
        {
            "optionCd": "013",
            "optionName": "통풍 시트(앞좌석)",
            "optionTypeCd": "02",
            "sort": 130,
            "imagePath": "/carsdata/option_images/option2-20.jpg",
            "description": "시트 표면에 작은 구멍을 뚫고 통풍구를 만들어 시원한 공기를 순환시켜 시트의 습기와 열을 제거해주는 시트.<br>특히 장시간 주행 시 등과 엉덩이의 땀, 습기 등을 제거하여 쾌적함을 유지시켜 준다. 직물 시트보다는 통풍성이 떨어지는 가죽 시트에 더 많이 장착된다."
        },
        {
            "optionCd": "014",
            "optionName": "가죽 시트",
            "optionTypeCd": "02",
            "sort": 140,
            "imagePath": "/carsdata/option_images/option2-5.jpg",
            "description": "가죽으로 만들어져 안락한 승차감을 제공하고 내구성이 우수한 시트로서 천연가죽 시트와 인조가죽 시트를 모두 포함하여 지칭한다.<br>직물시트에 비해 고급스럽고, 먼지를 빨아들이지 않아 청결 유지에 좋다. 여름철에는 보냉 효과로 시원하고, 겨울철에는 보온 효과가 있어 따뜻한 특징이 있다."
        },
        {
            "optionCd": "015",
            "optionName": "열선 시트(앞좌석)",
            "optionTypeCd": "02",
            "sort": 150,
            "imagePath": "/carsdata/option_images/option2-7.jpg",
            "description": "시트 등받이와 엉덩이 부분의 내부에 열선이 내장되어 있어 전기장판처럼 앞좌석 시트를 따뜻하게 만들어 주는 장치.<br>겨울철에도 안방과 같은 따뜻함과 안락감을 느끼게 해준다. "
        },
        {
            "optionCd": "016",
            "optionName": "열선 내장형 슬리핑 베드",
            "optionTypeCd": "02",
            "sort": 160,
            "imagePath": "/carsdata/option_images/tr_option2-16.jpg",
            "description": "내부에 열선이 내장되어 슬리핑 베드를 따뜻하게 만들어 주는 장치"
        },
        {
            "optionCd": "017",
            "optionName": "ECM",
            "optionTypeCd": "02",
            "sort": 170,
            "imagePath": "/carsdata/option_images/option1-6.jpg",
            "description": "야간운전 중에 뒷차량의 전조등에 의해 룸미러에 들어오는 빛을 광센서로 자동감지하고, 거울의 반사율을 자동으로 낮추어 운전자의 눈부심 현상을 없애주는 장치.<br>센서는 보통 룸미러 위쪽 중앙에 설치되어 있다. "
        },
        {
            "optionCd": "024",
            "optionName": "타코메타",
            "optionTypeCd": "02",
            "sort": 180,
            "imagePath": "/carsdata/option_images/tr_option3-24.jpg",
            "description": "자동차 운행에 관련한 정보를 기록하는 기기로서 차량 운행에 관련된 정보를 실시간 저장하고 운전습관에 해당하는 과속, 엔진회전수(rpm), 급가속, 급제  동과 같은 운전 자료를 데이터베이스로 남겨 업무 효율을 높이는 장치이다."
        },
        {
            "optionCd": "018",
            "optionName": "리타더 (유압식보조제동장치) ",
            "optionTypeCd": "03",
            "sort": 190,
            "imagePath": "/carsdata/option_images/tr_option3-18.jpg",
            "description": "페이드 현상(계속되는 브레이크 사용으로 제동력이 감속되는 현상)을 완화하기 위한 장치로, 브레이크 라이닝 수명을 증대시키고 운영비용을 절감하는 효과가 있다.  "
        },
        {
            "optionCd": "019",
            "optionName": "ABS",
            "optionTypeCd": "03",
            "sort": 200,
            "imagePath": "/carsdata/option_images/option1-2.jpg",
            "description": "급제동 시 바퀴에 달린 센서가 각 바퀴의 잠김을 감지하여 자동차가 미끄러지는 현상을 방지하고, 제동거리를 짧게 만들어주는 브레이크 조절 시스템.<br>특히 빗길이나 빙판길에서 미끄러짐과 회전현상을 감소시켜 주어 안정적인 제동을 할 수 있다. ABS 원리는 잠긴 바퀴에 전자제어장치를 이용하여 브레이크를 밟았다 놓았다 하는 펌핑 작동을 1초에 10회 이상 반복시켜 네 바퀴의 균형을 유지시키는 것이다."
        },
        {
            "optionCd": "020",
            "optionName": "ASR/TCS(미끄럼 방지)",
            "optionTypeCd": "03",
            "sort": 210,
            "imagePath": "/carsdata/option_images/option1-5.jpg",
            "description": "빗길, 눈길, 자갈길 등 미끄러지기 쉬운 노면에서 출발하거나 가속할 때 엔진 출력과 브레이크를 제어하여 미끄러짐을 방지하고, 곡선도로에서 주행 안정성을 향상시켜 주는 시스템"
        },
        {
            "optionCd": "021",
            "optionName": "에어 브레이크",
            "optionTypeCd": "03",
            "sort": 220,
            "imagePath": "/carsdata/option_images/tr_option3-21.jpg",
            "description": "압축공기로 바퀴 회전을 제동하여 속도를 줄이고 정지하는 장치 "
        },
        {
            "optionCd": "022",
            "optionName": "TPMS(타이어 공기압감지)",
            "optionTypeCd": "03",
            "sort": 230,
            "imagePath": "/carsdata/option_images/option1-11.jpg",
            "description": "타이어에 부착된 센서로 타이어의 공기압과 온도를 자동감지하여 운전자에게 정보를 제공하고, 공기압이 일정 기준보다 낮아진 타이어가 감지되면 경고등으로 알려주는 시스템.<br>이 시스템을 이용하여 타이어의 내구성과 승차감, 제동력, 연비 등을 향상시키고 미연의 사고를 방지할 수 있다."
        },
        {
            "optionCd": "023",
            "optionName": "EHS(언덕길 발진 보조장치)",
            "optionTypeCd": "03",
            "sort": 240,
            "imagePath": "/carsdata/option_images/tr_option3-23.jpg",
            "description": "언덕길에서 가속페달을 밟았을때 밀림 현상을 없앨 수 있는 언덕길 발진 보조 장치 "
        },
        {
            "optionCd": "025",
            "optionName": "에어백(운전석)",
            "optionTypeCd": "03",
            "sort": 250,
            "imagePath": "/carsdata/option_images/option1-3.jpg",
            "description": "차량 충돌 시 순간적으로 운전대에서 공기주머니가 부풀어 나와 운전자의 충격과 부상을 최소한으로 줄여주는 보호 장치.<br>운전석 에어백은 전방으로부터 충돌 시 설정 값 이상의 충격을 감지한 경우에 작동한다. 시트벨트를 착용한 상태에서 효과를 충분히 발휘할 수 있으며, 운전자의 상반신을 보호할 수 있다.  "
        },
        {
            "optionCd": "026",
            "optionName": "후방 카메라",
            "optionTypeCd": "03",
            "sort": 260,
            "imagePath": "/carsdata/option_images/option2-18.jpg",
            "description": "차량의 트렁크 또는 번호판 부분 등 후방에 카메라를 장착하여 후방 주차 시 실내 모니터를 통해 뒤쪽의 장애물과 단계별 진도 등을 확인할 수 있는 장치.<br>차량 주차 시 운전자의 후방 사각지대에 놓인 장애물을 알려주어 충돌을 예방하고, 정확한 간격으로 주, 정차할 수 있도록 유도해 준다."
        },
        {
            "optionCd": "027",
            "optionName": "수동 에어컨",
            "optionTypeCd": "04",
            "sort": 270,
            "imagePath": "/carsdata/option_images/tr_option4-27.jpg",
            "description": "수동으로 조작하는 에어컨 "
        },
        {
            "optionCd": "028",
            "optionName": "자동 에어컨",
            "optionTypeCd": "04",
            "sort": 280,
            "imagePath": "/carsdata/option_images/option2-8.jpg",
            "description": "사용자가 원하는 온도 설정 시 풍량, 공기 온도, 통풍 방향 등을 자동으로 조절하여 일정한 온도를 유지해 주는 에어컨 시스템.<br>실내 공기의 온도 및 습도를 조절하는 일반 에어컨 기능에 컴퓨터 자체제어 기능이 더해진 것이며, 센서를 통해 실내 온도를 감지하여 작동한다."
        },
        {
            "optionCd": "029",
            "optionName": "무시동 히터/에어컨 ",
            "optionTypeCd": "04",
            "sort": 290,
            "imagePath": "/carsdata/option_images/tr_option4-29.jpg",
            "description": "차량에 시동을 걸지 않은 상태에서 배터리로 가동되는 히터와 에어컨  "
        },
        {
            "optionCd": "030",
            "optionName": "무선 도어잠금장치",
            "optionTypeCd": "04",
            "sort": 300,
            "imagePath": "/carsdata/option_images/option2-4.jpg",
            "description": "키를 꽂지 않고 리모컨의 버튼을 눌러 원격에서 차량 문을 여닫을 수 있는 편의장치.<br>대부분 트렁크 여닫이 기능을 포함하고 있으며 경보 기능, 원격 시동 등의 다양한 기능을 추가한 무선 도어잠금장치도 출시되고 있다.  "
        },
        {
            "optionCd": "031",
            "optionName": "파워 윈도우",
            "optionTypeCd": "04",
            "sort": 310,
            "imagePath": "/carsdata/option_images/option2-1.jpg",
            "description": "간단하게 스위치를 누르면 전기모터를 이용해 자동차 창문을 자동으로 올리거나 내릴 수 있게 해주는 편의장치.<br>운전석 창문은 기본으로 제공되며, 모델에 따라 전 창문에 제공되는 차량이 많다. 윈도 록 기능이 포함되어 있으면 어린아이가 함부로 창문을 조작하지 못하게 하여 안전한 운행을 할 수 있다.      "
        },
        {
            "optionCd": "032",
            "optionName": "크루즈 컨트롤",
            "optionTypeCd": "04",
            "sort": 320,
            "imagePath": "/carsdata/option_images/option4-68.jpg",
            "description": "일정한 속도를 설정하면 운전자가 액셀이나 브레이크를 조작하지 않아도 설정된 속도를 유지하는 정속주행 장치.<br>일반적으로 브레이크나 액셀을 조작하게 되면 해제된다. 고속도로나 국도에서 장거리 운전 시 유용하게 사용할 수 있는 시스템이며, 정속 주행하기 때문에 급발진에 의한 연료소비를 막을 수 있어 연비의 효율이 높아진다. "
        },
        {
            "optionCd": "034",
            "optionName": "내비게이션",
            "optionTypeCd": "04",
            "sort": 330,
            "imagePath": "/carsdata/option_images/option3-4.jpg",
            "description": "GPS(인공위성이 지원하는 위치확인 시스템)를 통해 현재 위치, 진행방향, 목적지까지 경로 등을 모니터 상의 전자지도에 표시하고 음성으로 안내해주는 시스템.<br>출발지와 목적지를 입력하면 이동 경로와 예상 시간 등을 표시해 준다. 더불어 과속카메라, 사고다발지역, 어린이 보호구역 등을 안내하여 안전운전에도 도움을 준다.  "
        },
        {
            "optionCd": "037",
            "optionName": "냉(온)장고",
            "optionTypeCd": "04",
            "sort": 340,
            "imagePath": "/carsdata/option_images/tr_option4-37.jpg",
            "description": "차량 내부에 장착된 냉(온)장고 "
        },
        {
            "optionCd": "033",
            "optionName": "CD 플레이어",
            "optionTypeCd": "05",
            "sort": 350,
            "imagePath": "/carsdata/option_images/option3-1.jpg",
            "description": "CD를 삽입하여 차량에서 높은 음질의 음악을 감상할 수 있게 만들어주는 오디오 장치.<br>기본적으로 웨이브 파일형식으로 담긴 CD를 재생하고, 모델에 따라 MP3 파일형식을 재생할 수 도 있다.  "
        },
        {
            "optionCd": "035",
            "optionName": "AUX 단자",
            "optionTypeCd": "05",
            "sort": 360,
            "imagePath": "/carsdata/option_images/option4-71.jpg",
            "description": "AUX 연결 잭을 통한 외부입력으로 MP3, PMP 등과 같은 휴대용 장치의 음악을 차량의 오디오에서 감상할 수 있게 만들어주는 단자."
        },
        {
            "optionCd": "036",
            "optionName": "USB 단자",
            "optionTypeCd": "05",
            "sort": 370,
            "imagePath": "/carsdata/option_images/option4-72.jpg",
            "description": "USB 연결 잭을 꽂아서 MP3, PMP 등과 같은 휴대용 장치의 음악을 차량의 오디오에서 감상할 수 있게 만들어주는 단자."
        }
    ]