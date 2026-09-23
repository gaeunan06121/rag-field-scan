# worklog.md — 작업 기록

날짜별로 한 일 / 막힌 점 / 다음 할 일을 짧게 남기기.

## 2026-09-22
- 저장소 구조 세팅, README/AGENTS/scope/field-map 초안 작성
- GitHub 업로드 과정에서 여러 시행착오 (zip 파일을 그대로 올려서 개별 파일이 안 보였던 문제, areas 폴더 없이 파일들이 루트에 올라갔던 문제) → 파일명 앞에 `areas/`를 붙여 rename하는 방식으로 해결
- **에이전트가 틀렸던 순간**: 저장소 이름을 실제 확인 없이 `consulting-ai-finance`로 가정하고 README의 배포 URL을 `https://<username>.github.io/consulting-ai-finance/`로 써줬다. 그런데 실제로는 사용자가 이미 만들어둔 저장소 이름이 `rag-field-scan`이었다. 사용자가 실제 GitHub 화면 스크린샷을 보여줬을 때에서야 이 차이를 발견했고, URL을 `https://gaeunan06121.github.io/rag-field-scan/`로 수정했다. → 교훈: 에이전트가 만들어준 값(저장소 이름, URL 등)은 실제 화면과 대조해서 확인해야 한다.
- 다음: 영역 파일 10개 내용 채우기 시작

## 2026-09-23
- 10개 영역 파일 전부 웹 리서치 기반으로 채움 (은행 AI 운영모델, 자산관리 AI, 신용평가, AML, AI 규제, 데이터 품질, 토큰화, 임베디드 금융, 컨설팅 산업 AI 전환, AX 조직·인재)
- 그 중 5개 출처(PwC, BCBS 239 Wikipedia, Sumsub, aimultiple, NHIMG EU AI Act)는 직접 페이지를 열어 본문 내용이 실제로 작성한 문장과 맞는지 확인함 (sources.md [1]~[5])
- 나머지 8개 출처는 검색 결과 제목/스니펫만 확인한 상태 — 시간이 되면 직접 열어서 검증 예정
- key-contexts.md에 5개 핵심 맥락 작성
- 다음: process.md 마무리, README 결론 작성, 최종 배포 확인
