# Quattro
- [더 지니어스: 그랜드파이널] 규칙으로 제작하였습니다

## 경기 규칙
- 1 ~ 6까지의 빨강, 파랑, 노랑, 초록 카드와 2장의 0 카드로 구성
- 플레이어는 4장 씩 카드를 무작위로 받으며 2번의 멀리건 기회가 부여됨
    - 멀리건 : 4장을 다시 받음
- 가상 플레이어는 플레이어의 카드 배분 완료 후 3장 씩 무작위로 카드를 받음
- 콰트로에 0 카드를 포함해도 완성된 것으로 간주
- 6명의 가상 플레이어와 교환을 진행함. 이때 가상 플레이어의 교환 규칙은,
    - 교환 규칙 I. 교환하는 플레이어가 이미 오픈한 카드를 고려하여 콰트로를 완성시킬 수 있는 최적의 카드를 교환
    - 교환 규칙 II. 콰트로가 불가능한 카드뿐이라면 숫자가 가장 높은 카드를 교환
    - 교환 규칙 III. 숫자가 가장 높은 카드가 여러 장일 경우 빨강, 파랑, 노랑, 초록 순으로 카드를 선택해 교환
    - 단, 이 모든 경우에 앞서 교환하는 가상의 플레이어에게 0 카드가 있을 경우 무조건 0 카드를 선택해 교환
- 가상 플레이어에게 교환해 주는 카드는 공개되지만, 가상 플레이어가 교환해 주는 카드는 공개하지 않음
- A - B - B - A 순서로 게임 진행
- 콰트로 완성 > 콰트로 미완성
- 두 플레이어 모두 콰트로 완성 시 숫자 합이 더 큰 플레이어가 승리
- 두 플레이어 모두 콰트로 미완성시 가장 큰 숫자를 보유한 플레이어가 승리

## Build
```
$ pip install requirements.txt
```

## Execute
```
$ python3 main.py
```

## Execute Unit Test
```
$ python3 ./TestModule/UnitTest.py
```

## Commit Log
- 0.1: 게임 기본 사항 구현 완료
    - View 관련 부분 보완 필요:
        - 게임 시작 시 초기 화면
        - 게임 진행 상황 print 방식 등
    - 두 플레이어 모두 콰트로를 만들지 못했을 때, Draw 시나리오 구현 필요 (방송 상 내용 X)

- 1.0: 2인 플레이용 완성
    - 0.1 View 관련 부분 보완 + Draw 시나리오 구현
    - 완전 초기 화면이랑 마무리만 생각해두기
    - python3.5 이상 조건 추가하기
    
- 1.1: ASCII Art 추가
    - WelcomeView 추가, EndOfGame 보완
    - venv, requirements 추가
     
- 1.2.0: TDD
    - DeckTest 추가
    - Player Test Case 추가 예정

- 1.2.1: TDD Update
    - UnitTest 통합 파일 추가 (모든 unittest.TestCase class 파일 일괄 실행)
    - UserPlayerTest 추가
    - Anonymous Player Test Case, EndOFGame Test Case 추가 예정
    
- 1.2.2: TDD Update2
    - EndOfGame Test Case 추가
    - Anonymous Player Test Case 추가
    
- 1.2.3: minor
    - remove ComponentsTest.py