# 실시간 얼굴 인식 시스템

이 프로젝트는 Python과 OpenCV의 face_recognition 라이브러리를 사용하여 실시간 얼굴 인식 시스템을 구현한 것입니다. 고등학교 과학과제연구 주제로 선정되어 제작되었습니다.

## 설치 및 실행

### 필수 요구사항

- Python 3.10 이상
- OpenCV
- face_recognition 라이브러리

### 가상환경 설정

1. 프로젝트 디렉토리로 이동합니다.
2. VSCode 터미널에서 다음 명령어를 실행하여 가상환경을 생성합니다:

   ```
   python -m venv cv_env
   ```

3. `F1` 키를 누르고 `select interpreter`를 선택한 후, 방금 만든 가상환경을 선택합니다.
4. 터미널에 `(cv_env)`가 앞에 잘 붙어있으면 가상환경 설정이 성공한 것입니다.

### 라이브러리 설치

`requirements.txt` 파일에 필요한 라이브러리 목록이 있습니다. 다음 명령어를 실행하여 라이브러리를 설치합니다:

```
pip install -r requirements.txt
```

**주의**: dlib 라이브러리는 로컬 환경에서 설치가 어려울 수 있습니다.

### 실행 방법

다음 명령어를 실행하여 프로그램을 시작합니다:

```
python main.py
```

가상환경을 다시 실행할 때는 다음 명령어를 사용합니다:

```
cv_env\Scripts\activate
```

## 사용 방법

1. 프로그램을 실행하면 사용자 등록 화면이 나타납니다.
2. 사용자 등록 버튼을 클릭하면 등록할 사진의 개수를 선택할 수 있습니다.
3. 지정된 개수만큼 사진을 찍으면 사용자
4.  등록이 완료됩니다.
5. 등록된 사용자의 얼굴이 인식되면 해당 사용자의 이름이 화면에 표시됩니다.

## 기여

이 프로젝트에 대한 기여와 피드백은 언제나 환영합니다. 문제나 개선 사항이 있다면 이슈를 열어주시기 바랍니다.
연락 ksb19558@naver.com
