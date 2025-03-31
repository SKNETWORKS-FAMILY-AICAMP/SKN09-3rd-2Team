# [SKN09-3rd-2Team]
✅ SKN AI FAMILY CAMP 9기<br>


---
# 🔊Contents

1. [팀 소개](#%EF%B8%8Fteam-introduce)
2. [프로젝트 개요](#project-overview)
3. [기술 스택 & 사용한 모델 (임베딩 모델, LLM)](#3-기술-스택--사용한-모델-임베딩-모델-llm)
4. [시스템 아키텍처](#4-시스템-아키텍처)
5. [WBS](#5-wbs)
6. [요구사항 명세서](#6-요구사항-명세서)
7. [수집한 데이터 및 전처리 요약](#7-수집한-데이터-및-전처리-요약)
8. [DB 연동 구현 코드 (링크만)](#8-db-연동-구현-코드-링크만)
9. [테스트 계획 및 결과 보고서](#9-테스트-계획-및-결과-보고서)
10. [진행 과정 중 프로그램 개선 노력](#10-진행-과정-중-프로그램-개선-노력)
11. [수행결과(테스트/시연 페이지)](#11-수행결과테스트시연-페이지)
12. [한 줄 회고](#한-줄-회고)


---

# 🎙️Team Introduce
### 🎃팀명: 트래블 체커 🍀<br>
### 🐱팀원


| 윤 환 | 이세진 | 이재혁 | 허정윤 |
|------|------|------|------|
| [@MNYH](https://github.com/MNYH) | [@sejin](https://github.com/tpwls9494) | [@ohdyo](https://github.com/ohdyo) | [@jy](https://github.com/devunis) |
---

# 🎼Project Overview
✅ **프로젝트 기간: 2025.03.28 - 2025. 03.31**

## 1. 프로젝트 주제
#### ✈️ 여행 정보 챗봇 시스템

## 2. 프로젝트 소개
#### 프로젝트 필요성
<img src="https://github.com/user-attachments/assets/248799a3-7949-413e-ad92-6e66c1e1b778" width="400" height="300">
<img src="https://github.com/user-attachments/assets/2445c053-66dd-4b1e-97b6-1a16e05f2c15" width="400" height="300">

<br>

**출처**  
- [에어부산 화재원인은 보조배터리?…지난달에도 비슷한 사고 있어(종합)](https://www.yna.co.kr/view/AKR20250129029651003)
- [[이건왜] 비행기 내 보조배터리, 더 위험한 이유](https://www.sisajournal-e.com/news/articleView.html?idxno=409149)


#### 프로젝트 목표
- **여행 정보 제공** 
  - 여행 정보 챗봇 시스템은 사용자에게 항공 수하물 규정, 현지 문화 등 여행 관련 정보를 제공.
- **AI 기반 대화형 서비스** 
  - AI를 활용하여 자연스럽고 대화형으로 정보를 전달, 사용자가 쉽게 이해하고 활용할 수 있도록 지원.
- **사용자 맞춤형 응답** 
  - 사용자의 질문과 필요에 따라 개인화된 정보를 제공하여 여행 경험을 최적화.

=> 최종적으로 개개인이 원하는 여행 취지에 맞게 궁금한 요소를 해결해주는 **해결사 역할**을 해준다. 

<br><br>

## 3. 기술 스택 & 사용한 모델 (임베딩 모델, LLM)
## 🧰 기술 스택 및 사용한 모델

- 개발 언어:  ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white)
- 개발 환경: ![VS Code](https://img.shields.io/badge/-VS%20Code-007ACC?logo=visualstudiocode&logoColor=white) ![Colab](https://img.shields.io/badge/-Google%20Colab-F9AB00?logo=googlecolab&logoColor=white) ![RunPod](https://img.shields.io/badge/-RunPod-5F43DC?logo=cloud&logoColor=white)
- VectorDB :  ![ChromaDB](https://img.shields.io/badge/ChromaDB-white)
- LLM : ![Gemma](https://img.shields.io/badge/-Gemma-4285F4?logo=google&logoColor=white)
- 프레임워크 : <img src='https://img.shields.io/badge/%F0%9F%A4%97%20HF_transformer%20-yellow'> ![Gradio](https://img.shields.io/badge/Gradio-orange)
- 협업 툴 : ![GitHub](https://img.shields.io/badge/-GitHub-181717?logo=github&logoColor=white)



<br>

## 4. 시스템 아키텍처
<img width="1109" alt="스크린샷 2025-03-31 오전 2 17 05" src="https://github.com/user-attachments/assets/f18584ec-0c51-40ec-aa80-6e29a4d1749f" />

<br>

## 5. WBS
<img width="1082" alt="스크린샷 2025-03-31 오전 2 57 11" src="https://github.com/user-attachments/assets/3742c840-9aa1-486d-97ba-94bc30388af8" />

<br>

## 6. 요구사항 명세서
![Require_doc](https://github.com/user-attachments/assets/35ccdaeb-fc3c-4ad3-a78b-8f264b14480a)

<br>

![function_doc](https://github.com/user-attachments/assets/15f5ebaf-f6dd-4711-bc27-175fe6e83ef0)

<br>

## 7. 수집한 데이터 및 전처리 요약
- 수집한 데이터의 개행, 링크, 출처등과 관련된 일반적인 전처리 진행

| 순서 | 내용                   | 설명 |
|------|------------------------|------|
| 1    | `\xa0` → 공백 치환      | PDF에서 자주 나타나는 비표준 공백을 일반 공백으로 치환 |
| 2    | URL 제거               | `http`로 시작하는 웹 링크를 삭제 |
| 3    | 공백 정리              | 연속된 공백 및 줄바꿈, 탭 등을 하나의 공백으로 정리 |
| 4    | 특수 문자 제거         | 한글, 영문, 숫자, 일부 구두점을 제외한 특수 문자 제거 |
| 5    | 양쪽 공백 제거         | 문자열의 좌우 공백 제거 |


<br>

## 8. DB 연동 구현 코드 (링크만)
[DB 연동 구현 파일 바로가기](https://github.com/SKNETWORKS-FAMILY-AICAMP/SKN09-3rd-2Team/blob/main/fine_tune/testing_yh.ipynb)
<img width="1431" alt="스크린샷 2025-03-30 오후 1 56 21" src="https://github.com/user-attachments/assets/f7b88867-d936-4923-841b-9bd9bfc1e0bb" />
<img width="784" alt="스크린샷 2025-03-30 오후 5 18 06" src="https://github.com/user-attachments/assets/62d5c625-3ac6-41d6-bcc2-3c732ff0bf86" />
<img width="530" alt="스크린샷 2025-03-30 오후 5 19 02" src="https://github.com/user-attachments/assets/ed187b91-1dde-4984-94af-93491455967d" />
<img width="1423" alt="스크린샷 2025-03-30 오후 1 56 38" src="https://github.com/user-attachments/assets/95225e30-0d1a-4814-8ed1-baaa5f54abe4" />

<br>

## 9. 테스트 계획 및 결과 보고서

### 🧪 테스트 계획서 (Test Plan)

#### 1. 테스트 목적
Gemma3 기반 파인튜닝된 LLM이 다음 조건에 맞는지 검증:
- 규정에 맞는 항공 관련 정보 제공
- 정보가 없는 국가에 대한 정보 요청에 대해 일관된 거절 응답 처리

#### 2. 테스트 범위

- **정답 응답 케이스**: 항공 화물, 위험물, 반입 가능 품목, 여행지 정보 등
- **거절 응답 케이스**: 자료가 존재하지 않는 국가별 문화·예절·금지 품목 질문

#### 3. 테스트 구성

| 구분         | 수량 |
|--------------|------|
| 정답 케이스   | 14건 |
| 거절 케이스   | 10건 |
| **총합**      | 24건 |

#### 4. 테스트 기준

| 항목             | 기준 설명 |
|------------------|-----------|
| 정답 응답        | 기대 응답 내용과 동일하거나 유사한 항공 관련 정보 포함 |
| 거절 응답        | "해당 국가에 대한 정보는 제공하지 않습니다." 포함 |
| 실패 기준        | 기대와 다른 내용, 오답, 엉뚱한 정보, 무응답 등 |

#### 5. 테스트 방식

- RetrievalQA 체인을 통해 질문 입력 → 모델 응답 → 기대값과 비교
- 수동 평가로 통과/실패 판별

---

### ✅ 테스트 결과 보고서 (Test Report)

#### 1. 테스트 요약

| 총 케이스 | 통과 | 실패 | 통과율 |
|-----------|------|------|--------|
| 24        | 9    | 15   | 37.5%  |

#### 2. 통과/실패 분포

##### ✅ 통과된 케이스 (9건)

| 테스트 ID | 유형   | 질문                                        |
|-----------|--------|---------------------------------------------|
| QA001     | 정답   | 화물과 수하물의 차이는 무엇인가요?          |
| QA002     | 정답   | 강아지를 샌프란시스코에 데려가려면?         |
| QA003     | 정답   | 위험물이란 무엇인가요?                      |
| QA004     | 정답   | 유해 유골 운반에 필요한 서류는?             |
| QA005     | 정답   | 화물 cut-off time 알려주세요.               |
| QA006     | 정답   | Spot Rate 입력은 어떻게 하나요?             |
| QA007     | 정답   | 리튬 배터리 기내 반입 가능한가요?           |
| QA011     | 정답   | 일본 여행 시 추천 관광지는 어디인가요?      |
| QA012     | 정답   | 대만 여행 중 꼭 먹어봐야 할 음식은?         |

##### ❌ 실패된 케이스 (15건)

| 테스트 ID | 유형   | 실패 사유 요약 |
|-----------|--------|----------------|
| QA008     | 정답   | 엉뚱한 국가(인도네시아) 정보 제공 |
| QA009     | 정답   | "위탁 수하물" 명시 없이 조건부 허용 언급 |
| QA010     | 정답   | 혼란스러운 기준 설명 및 출처 누락 |
| QA013     | 정답   | 화폐명 오류(페르피히오 → 페소), 불명확 환율 |
| QA014     | 정답   | 정보는 있지만 단편적이며 포맷 일관성 부족 |
| NG001~NG010 | 거절 | 대부분 실제 국가 정보가 포함되어 거절 실패 |

#### 3. 개선 포인트 요약

| 문제점 유형                 | 설명 |
|-----------------------------|------|
| ❌ 거절 실패                 | "정보 제공하지 않음" 응답이 아닌 실제 정보 응답 |
| ❌ 정답 불명확 or 혼란       | 애매한 기준, 잘못된 수치, 출처 누락 등 |
| ❌ 문맥 일탈                 | 엉뚱한 국가 정보 응답 등 |
| ✅ 일부 개선된 응답 포맷     | QA001~007은 포맷과 정보 적절 |

#### 4. 개선 권장 사항

- **거절 응답 정책 강화**: RAG 결과가 없거나 금지 국가일 경우 무조건 거절하도록 명확한 로직 필요
- **정답 정제 및 기준 통일**: Wh 기준, 배터리 규정 등에서 표준화 필요
- **추론 포맷 일관화**: Markdown 또는 표 기반으로 응답 포맷 통일
- **출처 명시 옵션 추가**: 신뢰 확보를 위한 링크 혹은 출처 포함

<br>

## 10. 진행 과정 중 프로그램 개선 노력
- 초기 파인튜닝 학습 중 학습률 문제 발생

  1. 초기 학습 단계에서 모델의 학습률이 비정상적으로 낮게 나타나는 문제가 있었음

  2. 원인 분석 결과, 학습에 필요한 데이터 양이 부족하다고 판단하여 다양한 출처로부터 추가 데이터를 지속적으로 수집
 
  3. 파인튜닝 시 학습에 사용되는 input_text 형식을 "질문: {질문 내용}\n답변:"으로 통일하여, 입력 의도를 명확히 전달하고 학습 효율을 개선

  4. LoRA 세부 설정값(loraconfig)의 파라미터를 조정하여 모델 학습 효율 개선 시도 (특히 r값, alpha 값, dropout 비율 등 변경)
 
  5. 학습 epoch 수를 기존보다 증가시켜 성능 개선을 시도하고, validation loss가 적정 수준인 모델을 선택하여 최종 결과에 활용
- 학습 종료 후 성능 검증 및 응답 품질 향상 시도

  1. 학습이 정상적으로 완료되었는지 확인하기 위해 테스트 질의 응답을 다수 수행
     
  2. 학습된 데이터 외 새로운 키워드나 질문에 대해 부정형 응답(정보가 없음을 알려주는 응답)이 자연스럽게 나오도록 프롬프트 구조와 거절 응답 데이터 추가 조정
     
  3. 부정형 응답의 정확도를 높이기 위해 프롬프트 내 거절 의도를 명확히 전달하도록 문구 수정
     
  4. 학습 데이터와 테스트 데이터를 지속적으로 비교하며 가중치와 파인튜닝 설정값을 재조정
   
  5. 질문 내 국가 키워드를 감지 후 허용 국가의 경우에 응답을 허용하고 나머지의 경우 관련 데이터가 없다고 반환

<br><br>

## 11. 수행결과(테스트/시연 페이지)
[jeongyoonhuh/travel-checker 모델 업로드](https://huggingface.co/jeongyoonhuh/travel-checker)

<img width="630" alt="스크린샷 2025-03-30 오후 11 23 44" src="https://github.com/user-attachments/assets/416ab982-377a-4633-beb8-8905f4e353d3" />

![image](https://github.com/user-attachments/assets/e2986044-80a0-4a7a-83ff-8c1ccac9321d)

![image (1)](https://github.com/user-attachments/assets/3a4ae4d3-972a-4b0c-888c-c4816f0535a0)

![포함된국가](https://github.com/user-attachments/assets/b08483d2-b5f7-4e09-84fa-5ff4c22dab38)

![미포함된국가](https://github.com/user-attachments/assets/8e5d8627-3a1e-444f-8a90-705b63373d03)




<br><br>

# 🎶결론
- 사용자 질문에 대해 자연스럽고 정확한 답변을 제공할 수 있도록 학습 데이터를 기반으로 응답 시스템을 완성하였음

- 제한된 정보나 학습되지 않은 키워드에 대해서는 명확한 거절 응답을 제공하도록 설정하여 사용자 혼란을 최소화하였음

- 궁극적으로 사용자가 여행을 계획할 때 필요한 정보와 유용한 팁을 빠르고 편리하게 얻을 수 있도록 지원하는 시스템을 구현하였음

<br><br>

## 향후 과제
- 아직 수집되지 않은 국가별 입국 절차, 문화 정보 등 추가 데이터 확보

- 챗봇 사용성 향상을 위한 지속적인 데이터 정제 및 추가 학습 진행

- 실제 사용자 피드백을 바탕으로 Q&A 데이터 개선 및 고도화

<br><br>

# 🎧한 줄 회고
- 윤환 : 
- 이세진 : 
- 이재혁 :
- 허정윤 :
