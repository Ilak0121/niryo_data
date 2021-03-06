## 가속도계와 진동 측정

### 정의 
- 기계 또는 구성 요소의 평형 위치에 대한 움직임 또는 기계적 떨림. 미터법 단위(m/s^2) 또는 중력 상수 g로 표현 가능.

***

- 사물은 자유 진동/강제 진동  두 가지 방식으로 진동이 가능하다
  1. 자유 진동 - 사물 또는 구조가 변형되거나 충격을 받아서 자연스럽게 떨릴 때 발생. 주로 충격 또는 변형 후에 구조가 '자연적으로' 진동하는 주파수.
  2. 강제 진동 - 변형력이 작용하여 구조가 진동할 때 발생. 회전 또는 변형 모션이 일어나면 사물이 비정상적 주파수로 진동. 

***

### 진동 측정 방법
- 진동은 일반적으로 압전 세라믹 센서 또는 가속도계를 사용하여 측정한다.
  - 가속도계는 물리적 디바이스의 동적 가속도를 전압으로 측정한다. 일반저긍로 롤러 베어링, 기어박스, 회전날과 같이 고주파수 요소에 직접 장착되는 전면 접촉 트랜스듀서이다.
  - 이 다목적 센서는 충격 측정 및 느린 저주파수 진동 측정에 사용할 수 있는 폭넓은 주파수 범위와 동적 범위를 포괄하는 선형성이라는 이점을 가진다.

- 진동 측정에 사용할 수 있는 또 다른 센서는 비접촉 변위센서이다. 가속도와 달리 진동을 판별하기 위해 대상까지의 거리를 측정한다.
  - 이 센서는 회전 기계류에서 샤프트의 진동을 측정하는데 거의 전용으로 사용된다.
  - 보편적인 적용 예는 터보 기계류와 같은 기계적 시스템에 대한 기계 모니터링 및 보호이다.
 

- 압전 또는 차지 타입 가속도계는 외부 증폭기 또는 인라인 전하 변환기가 필요하다. 이 기기들은 생성된 전하를 증폭시키고 측정 디바이스와 호환 되도록 출력 임피던스를 낮추고 외부 노이즈 소스 및 크로스토크에 대한 영향을 최소화 한다.
- 전하 감도 증폭기가 내장되어 있는 가속도계도 있다. 이 증폭기는 정전류 소스를 받으며 압전성 결정의 전하 변동에 따라 임피던스가 달라진다. 이런 센서들을 IEPE(Integrated Electonic Piezoelectric) 센서라고 한다.
***

- 민감도 : 민감도는 가속도계의 가장 중요한 파라미터 중 하나로, 160Hz 등의 참조 주파수에서 진동 및 전압 간의 변환을 나타낸다. 민감도는 mV/G로 지정된다. 일반적인 가속도계 민감도가 100mV/G인 경우 10G 신호를 측정하면 1000mV 또는 1V 출력을 예상할 수 있다. 
- 정확한 민감도는 교정을 통해 결정되며, 보통 센서와 함께 제공되는 교정 인증서에 명시되어 있다.
- 민감도는 주파수에 따라 달라지기도 한다.
> - 가속도계는 민감도가 상대적으로 일정한 폭넓은 가용 주파수 범위를 지원한다.
***
- 무게 : 일반적으로 가속도계의 무게는 테스트할 구조 무게의 10%를 초과하지 않아야 한다.
***
- 장착 옵션 : 가속도계를 대상 표면에 장착하는 방법.
  - 휴대용 또는 탐침기 팁.
  - 마그네틱
  - 접착형
  - 스터드 장착.
> 스터드 장착은 현재까지 최고의 장착 기법으로 알려져 있으나 대상 재질에 구멍을 뚫어야 하므로 센서를 영구적으로 설치하는 경웨 주로 사용됨. 일반적으로 연결이 헐거울수록 측정 가능 주파수 한계가 낮아진다.
***
- 환경적 조건
- 최고 작동 온도, 유해 화학물에 대한 노출, 습도 등의 주요 환경적 변수에 유의해야 한다.
- 시스템을 극한의 온도에서 작동해야 하는 경우, 차지 타입 가속도계를 사용한다. 이 가속도계에는 전자 부품이 내장되어 있지 않기 때문에, 구조에 사용되는 감지 요소 및 재질에 의해서만 작동 온도가 제한된다. 그러나 차지 타입은 내장 컨디셔닝 및 전하 증폭 장치가 없으므로 환경적 간섭에 민감하고 노이즈가 많은 경우에는 재장 전하 증폭기를 갖춘 차지 변환기 또는 IEPE 센서를 사용해야 한다.

*** 
### 가속도계에 대한 신호 컨디셔닝
- 다음과 같은 사항을 고려하여 신호 컨디셔닝 요구사항을 모두 충족해야 한다.
  - 측정 분해능을 증가시키고 신호 대 노이즈 비율을 개선하기 위한 증폭.
  - IEPE 센서의 증폭기에 전원을 공급하는 전류 구동.
  - 입력 장비의 전체 범위를 활용하고 분해능을 증가시키기 위해 DC 오프셋을 제거하는 AC 커플링.
  - 외부 고주파수 노이즈를 제거하기 위한 필터링.
  - 다양한 접지 전위 간의 전류 흐름에서 노이즈를 제거하는 데 적합한 접지.
  - 가속도계의 전체 진폭 범위를 측정하기 위한 동적 범위.

### reference 
> http://www.ni.com/white-paper/3807/ko/

