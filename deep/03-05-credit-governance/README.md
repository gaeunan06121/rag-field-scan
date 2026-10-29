**최종 판정: 조건부 Go** — 지금 모델 그대로는 출시 불가. 문제 변수 3개 삭제, 신용평가 목적 동의, 설명·재산출 절차, 거절 건 사람 재검토, 로그 6개월 이상 보관을 갖춘 뒤 재심사 (근거: L4 실사, L6 메모)

# 03·05 심화: AI 신용평가 출시 심사 (V뱅크)

질문: 신용 이력이 짧은 청년에게 대안 데이터로 점수를 매기는 모델을 출시해도 되는가?
최종 답: **조건부 Go** (2026-10-29 리즈 판정)

## 폴더 구성
- L0-trae-test/ — 10/11 Trae 도구 비교 작업 (질문 20, 함정 5, originals, 결과 기록)
- L1-regulation-cards.md — 규제 원문 카드 17장 (EU·홍콩·한국)
- L2-requirements.md — 요구사항 표 18개 (6분류, 관할·관할 간 차이 포함)
- L3-scorecard.md · L3-applicants.csv · L3-score.py · L3-agent-results.md · L3-hand-check.md — 가상 스코어카드, 신청자 30명, 계산 결과, 손 검산
- V-bank-client-facts.md · L4-due-diligence.md — 가상 의뢰 자료와 실사
- L5-engine-review/ — 함정 8개를 심은 보고서를 엔진 3개(Claude·DeepSeek·Qwen)가 검토, Gemini가 비교, 정답표로 채점, 엔진 선택 규칙
- L6-client-memo.md — 클라이언트 메모 1쪽
- prompts/ — 에이전트에게 준 지시문
- progress/ — 주차별 진행 기록

## 원칙
- 함정 정답표는 저장소 밖에 보관하고 커밋하지 않음
- 신청자·은행은 모두 가상
- 작업 과정은 저장소 루트의 worklog.md에 날짜별로 기록 (시킨 일 / 에이전트가 한 일 / 내가 확인하거나 고친 일)
