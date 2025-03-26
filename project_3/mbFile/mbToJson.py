import re
import json

def markdown_to_json(markdown_text):
    # 줄바꿈 표준화 (윈도우/맥/리눅스 줄바꿈 차이 처리)
    markdown_text = markdown_text.replace('\r\n', '\n').replace('\r', '\n')
    
    # 정규식 패턴 개선 - 더 엄격한 패턴 적용
    pattern = r'(\d+)\.\s+(.*?)\?\s+-\s+(.*?)(?=\n\d+\.|$)'
    matches = re.findall(pattern, markdown_text, re.DOTALL)
    
    # JSON 형식으로 변환
    result = []
    found_numbers = set()
    
    for num, question, answer in matches:
        # 텍스트 정리 (여분의 공백과 줄바꿈 제거)
        question = re.sub(r'\s+', ' ', question.strip()) + "?"  # 물음표 다시 추가
        answer = re.sub(r'\s+', ' ', answer.strip())
        
        item = {
            "question": question,
            "answer": answer
        }
        result.append(item)
        found_numbers.add(int(num))
    
    # 누락된 항목 확인 (1부터 100까지 있어야 함)
    missing_numbers = [i for i in range(1, 101) if i not in found_numbers]
    
    if missing_numbers:
        print(f"누락된 항목: {missing_numbers}")
        
        # 누락된 항목 수동 추출 시도
        for missing_num in missing_numbers:
            # 누락된 항목 전후의 패턴을 더 넓게 찾기
            broader_pattern = fr'{missing_num}\.\s+(.*?)\?[\s\n]*-[\s\n]*(.*?)(?=\n{missing_num+1}\.|$)'
            additional_match = re.search(broader_pattern, markdown_text, re.DOTALL)
            
            if additional_match:
                question = re.sub(r'\s+', ' ', additional_match.group(1).strip()) + "?"
                answer = re.sub(r'\s+', ' ', additional_match.group(2).strip())
                
                result.append({
                    "question": question,
                    "answer": answer
                })
                print(f"항목 {missing_num}을(를) 추가로 찾았습니다.")
    
    # 항목 수 확인
    if len(result) != 100:
        print(f"경고: 변환된 항목이 100개가 아닙니다 (현재: {len(result)}개)")
    
    return result

# 마크다운 파일 읽기
with open('./malaysia_qa.md', 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# JSON으로 변환
json_data = markdown_to_json(markdown_content)

# JSON 파일로 저장
with open('malaysia_qa.json', 'w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, ensure_ascii=False, indent=2)

print(f"변환 완료: {len(json_data)}개의 질문-답변 쌍이 malaysia_qa.json 파일로 저장되었습니다.")