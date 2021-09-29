# Chapter06-04
# Futrues 동시성(파이썬 3.2부터)
# 비동기 작업 실행
# A → B : A가 한시간 B가 1분이 걸리는 작업이더라도 순서대로 해야하는 것 → 동기작업
# 지연시간(Block) CPU 및 리소스 낭비 방지 → File, Network Input/Output 관련 작업 → 동시성 활용 권장
# Ex) 웹에서 응답이올때까지 기다리지 말고, 다른작업을 먼저 수행하자 : 동시성 활용 비동기 작업 실행
# 비동기 작업과 적합한 프로그램일 경우 압도적으로 성능 향상

# 파이썬 3.2 이전에서는 아래 모듈을 임포트 했었음
# import threading
# import multiprocessing

# futures 패키지 : 비동기 실행을 위한 API를 고수준으로 작성 → 사용하기 쉽도록 개선
# threading, multiprocessing이 이미 포함되어 있음
# 1. 멀티스레딩/멀티프로세싱 API 통일 → 매우 사용하기 쉬움
# 실행중인 작업 취소, 완료 여부 체크, 타임아웃 옵션, 콜백 추가, 동기화 코드 매우 쉽게 작성 → Promise 개념

# 2가지 패턴 실습
# concurrent.futures 사용법1
# concurrent.futures 사용법2

# GIL : 파이썬에만 있음, 여러개의 작업을 처리할때 전체가 Lock이 걸리는 현상
# 두개이상의 스레드가 동시에 실행될때 하나의 자원을 엑세스 하는 경우 → 문제점 방지를 위해 GIL이 실행됨, 리소스 전체에 Lock이 걸림

# GIL 우회 : 멀티프로세싱 사용, CPython

from concurrent.futures.process import ProcessPoolExecutor
import os
import time
from concurrent import futures

WORK_LIST = [10000, 100000, 1000000, 10000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제너레이터)

def sum_generator(n):
    return sum(n for n in range(1, n+1))

def main():
    # Worker Count
    worker = min(10, len(WORK_LIST)) # 4
    
    # 시작 시간
    start_tm = time.time()
    
    # 결과 건수
    # result = []
    with futures.ThreadPoolExecutor() as excutor:
        # map → 작업순서 유지, 즉시 실행
        result = excutor.map(sum_generator, WORK_LIST)
        
    
    # 종료 시간
    end_tm = time.time() - start_tm
    # 출력 포맷
    msg = '\n Result -> {} Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(list(result), end_tm))

# 실행    
if __name__ == '__main__':
    main()