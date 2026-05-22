# 6D Pose Estimation 기초 스프린트 학습 계획

## 1. 프로젝트 목적

이 프로젝트의 목표는 최신 6D pose 논문을 전부 이해하는 것이 아니라, 여름방학 안에 인식형 6D Pose Estimation 미니 프로젝트를 시작할 수 있는 최소 기반을 만드는 것이다.

최종 목표는 다음과 같다.

> RGB-D 또는 샘플 데이터를 이용해 물체 하나를 segmentation하고, point cloud를 생성한 뒤, PnP 또는 ICP 기반으로 6D pose를 추정하고, Open3D 또는 RViz에서 시각화할 수 있다.

---

## 2. 핵심 학습 방식

이 프로젝트는 이론을 전부 공부한 뒤 실습하는 방식이 아니라, 작은 실습 목표를 먼저 정하고 막히는 지점에서 필요한 이론을 보충하는 방식으로 진행한다.

```text
작은 목표 설정
-> 코드 실행
-> 결과 확인
-> 이상한 점 기록
-> 필요한 이론 학습
-> 코드 수정
-> 시각화
-> 내 말로 설명
-> README 또는 실험노트에 기록
```

핵심 원칙은 다음이다.

> 작은 6D pose 결과물을 먼저 만들고, 그 결과가 왜 맞는지 또는 왜 틀리는지 설명하는 데 필요한 이론만 즉시 보충한다.

---

## 3. 8주 최소 커리큘럼

| 주차 | 핵심 주제 | 최소로 배울 것 | 실습 목표 | 산출물 |
| --- | --- | --- | --- | --- |
| 1주차 | 선형대수·좌표계 기초 | 벡터, 행렬, 회전행렬, 이동벡터, 4x4 transformation matrix | 3D 점을 회전·이동시키는 코드 작성 | R, t, T 변환을 직접 계산한 노트북 |
| 2주차 | 카메라 모델·캘리브레이션 | pinhole camera, intrinsic, extrinsic, distortion, camera calibration | 체커보드로 카메라 내부 파라미터 추정 | camera matrix, distortion coefficient, reprojection error |
| 3주차 | PnP 기반 Pose Estimation | 2D-3D correspondence, solvePnP, RANSAC, reprojection error | 3D 큐브나 마커의 pose를 이미지에서 추정 | 이미지 위에 3D 좌표축을 그린 결과 |
| 4주차 | RGB-D·Point Cloud | depth image, RGB-D, point cloud, filtering, crop, downsampling | depth를 point cloud로 변환하고 물체 영역만 분리 | Open3D로 시각화한 object point cloud |
| 5주차 | Point Cloud Registration | ICP, registration, source/target point cloud, transformation matrix | 관측 point cloud와 모델 point cloud를 정합 | ICP 결과 pose와 정합 전후 비교 이미지 |
| 6주차 | Segmentation / Detection | bounding box, mask, instance segmentation, YOLO/SAM/Mask R-CNN 사용법 | 이미지에서 물체 mask를 얻고 depth와 결합 | 특정 물체의 mask + object point cloud |
| 7주차 | 6D Pose 미니 파이프라인 | PnP 또는 ICP 기반 6D pose, rotation/translation error, ADD 개념 | RGB-D 입력에서 물체 pose 추정 | 하나의 물체에 대한 6D pose 추정 코드 |
| 8주차 | ROS2 / RViz 시각화 | ROS2 node, topic, PoseStamped, TF, RViz | 추정한 object pose를 ROS2로 publish | RViz에서 camera frame과 object frame 시각화 |

---

## 4. 시간이 부족할 때 최소 필수 4개

| 우선순위 | 필수 주제 | 최소 목표 |
| --- | --- | --- |
| 1 | 좌표계 변환 | R, t, 4x4 transformation matrix 이해 |
| 2 | OpenCV solvePnP | 2D-3D 점 대응으로 pose 추정 |
| 3 | Open3D Point Cloud + ICP | depth -> point cloud -> registration |
| 4 | Segmentation | 물체 mask를 얻고 해당 depth/point cloud만 추출 |

---

## 5. 매주 반복할 학습 루프

| 단계 | 할 일 | 예시 |
| --- | --- | --- |
| 1 | 이번 주 결과물 정하기 | “큐브 pose를 이미지 위에 축으로 그린다” |
| 2 | 공식 문서/예제 보고 코드 실행 | OpenCV solvePnP 예제 확인 |
| 3 | 코드가 안 되는 부분 기록 | 축이 반대로 나옴, translation 값이 이상함 |
| 4 | 필요한 이론만 학습 | camera frame, Rodrigues vector, intrinsic |
| 5 | 다시 코드 수정 | 점 순서, distortion, 좌표계 확인 |
| 6 | 결과 시각화 | 이미지, Open3D, RViz |
| 7 | GPT에게 이해 검증 | “제가 이해한 게 맞나요?” |
| 8 | README에 정리 | 오늘 배운 개념, 실패 원인, 결과 이미지 |

---

## 6. 하루 공부 루틴

하루 4~5시간 기준 루틴은 다음과 같다.

| 시간 | 내용 |
| --- | --- |
| 30분 | 어제 막힌 문제 정리 |
| 60분 | 필요한 이론만 공부 |
| 120분 | 코드 실행·수정·시각화 |
| 30분 | 결과 캡처, 실험 로그 작성 |
| 30분 | ChatGPT에게 내 이해 검증받기 |
| 30분 | 다음 실험 하나 정하기 |

하루 목표는 “강의 몇 개 보기”가 아니라 작동하는 작은 결과 하나를 남기는 것이다.

예시:

```text
오늘의 결과:
- chessboard corner detection 성공
- camera matrix 저장
- reprojection error 확인
- solvePnP 입력 형식 이해
- 내일 3D axis overlay 실습
```

---

## 7. 여름방학 종료 시 목표 문장

여름방학이 끝날 때 아래 문장을 말할 수 있으면 된다.

> 카메라 캘리브레이션을 하고, RGB-D 입력에서 물체를 segmentation한 뒤, point cloud를 생성하고, PnP/ICP 기반으로 6D pose를 추정해서 Open3D나 RViz로 시각화해봤습니다.
