# ch1. Data analysis.

- 데이터 정제(Data set normalization)
- 기술 통계 분석과 탐색적 분석 
    - 산포도, 히스토그램, 통계적 요약
    - 이 과정에서 데이터셋에 감을 잡아 후속 분석 방향을 정할 수 있다.

# ch2. 올바른 자료구조.
- Data structure that most uses is `list, tuple, set, dictionary`.
- four types are all collection of data/
- `list`에서 아이템을 검색할 때 걸리는 시간은 선형적으로 증가하기 때문에, 검색이 가능한 대용량의 데이터를 저장하는 용도로는 실용성이 떨어진다.
- `Tuple`은 변형이 불가능한 리스트로 한 번 생성되면 변형할 수 없다. 튜플 역시, 검색에 걸리는 시간이 선형적으로 증가한다.
- `set`은 리스트나 튜플과 달리 저장되는 순서가 없고 이에 따라 index 또한 없다. 같은 아이템이 중복으로 저장될 수 없으며 검색 시간은 준 선형적인 O(log(N))이다.

    bigList = [str(i) for i in range(10000000)]
    "abc" in bigList # takes for 0.2 second
    bigSet = set(bigList)
    "abc" in bigSet # 15~30 micro seconds. much faster.

- `dictionary`는 key를 value에 매핑한다. number, bool, str, tuple처럼 해시화할 수 있는 data type은 key가 될 수 있고 같은 dictionary에 들어 있다 하더라도 키들은 서로 다른 data type에 속할 수 있다. value의 data 형식에도 별도의 제약사항은 없다. dictionary의 search time은 준선형적인 O(log N)으로 증가한다. 
    - tuple(key,value)이 여러 개 있는 리스트에서 딕셔너리를 만들 수 있다. 그리고 내장된 class constructor인 enumerate(seq)를 사용해 seq 안의 아이템 순번을 키로 지정한 딕셔너리를 만들 수 있다.


# ch6. Pandas
- python 데이터 구조 셋은 이미 잘 갖추어져 있지만, pandas 모듈은 여기에 두 가지 새로운 컨테이너인 Series와 DataFrame을 추가한다. 
- Series는 label이 붙은(혹은 index 처리된) 1차원 vector이다.
- Frame은 label이 붙은 행과 열로 구성된 table이지만 Excel spreadsheet나 MySQL table과는 다르다. Frame의 각 열은 series이다. 몇 가지 예외를 제외하면 pandas는 frame을 시리즈와 유사하게 취급한다.
    - Data Frame은 label이 붙은 행과 열로 구성된 table이다. data frame은 2차원 numpy 배열, 튜플로 구성된 list, python dictionary와 또 다른 data frame으로 생성할 수 있다. 

