# RGB-D Based 6D Object Pose Estimation

## 1. Project Goal

이 프로젝트의 목표는 RGB-D 또는 샘플 데이터를 이용해 물체 하나의 6D pose를 추정하고, Open3D 또는 RViz에서 시각화하는 것이다.

최종적으로 다음 파이프라인을 구현하는 것을 목표로 한다.

```text
Camera Calibration
-> Segmentation
-> RGB-D to Point Cloud
-> PnP / ICP Pose Estimation
-> Visualization
```

## 2. 진행 상황 체크리스트

이 프로젝트는 이론을 전부 공부한 뒤 실습하는 방식이 아니라, 작은 실습 결과를 먼저 만들고 막히는 지점에서 필요한 이론을 보충하는 방식으로 진행한다.

기록할 때는 완료한 항목을 `- [x]`로 바꾼다.

### 학습 루프

- [ ] 이번 주에 만들 작은 결과물 정하기
- [ ] 예제 코드 실행하기
- [ ] 결과 확인하기
- [ ] 이상한 점 또는 실패 원인 기록하기
- [ ] 필요한 이론만 보충하기
- [ ] 코드 수정하기
- [ ] 이미지, Open3D, RViz 등으로 시각화하기
- [ ] 배운 내용을 README 또는 실험노트에 내 말로 정리하기

### 8주 진행 상황

- [ ] 1주차: 선형대수와 좌표계 기초
  - 목표: 벡터, 행렬, 회전행렬, 이동벡터, 4x4 transformation matrix 이해
  - 실습: 3D 점을 회전, 이동시키는 코드 작성
  - 산출물: R, t, T 변환을 직접 계산한 노트북
- [ ] 2주차: 카메라 모델과 캘리브레이션
  - 목표: pinhole camera, intrinsic, extrinsic, distortion, camera calibration 이해
  - 실습: 체커보드로 카메라 내부 파라미터 추정
  - 산출물: camera matrix, distortion coefficient, reprojection error
- [ ] 3주차: PnP 기반 Pose Estimation
  - 목표: 2D-3D correspondence, solvePnP, RANSAC, reprojection error 이해
  - 실습: 3D 큐브나 마커의 pose를 이미지에서 추정
  - 산출물: 이미지 위에 3D 좌표축을 그린 결과
- [ ] 4주차: RGB-D와 Point Cloud
  - 목표: depth image, RGB-D, point cloud, filtering, crop, downsampling 이해
  - 실습: depth를 point cloud로 변환하고 물체 영역만 분리
  - 산출물: Open3D로 시각화한 object point cloud
- [ ] 5주차: Point Cloud Registration
  - 목표: ICP, registration, source/target point cloud, transformation matrix 이해
  - 실습: 관측 point cloud와 모델 point cloud 정합
  - 산출물: ICP 결과 pose와 정합 전후 비교 이미지
- [ ] 6주차: Segmentation / Detection
  - 목표: bounding box, mask, instance segmentation, YOLO/SAM/Mask R-CNN 사용법 이해
  - 실습: 이미지에서 물체 mask를 얻고 depth와 결합
  - 산출물: 특정 물체의 mask와 object point cloud
- [ ] 7주차: 6D Pose 미니 파이프라인
  - 목표: PnP 또는 ICP 기반 6D pose, rotation/translation error, ADD 개념 이해
  - 실습: RGB-D 입력에서 물체 pose 추정
  - 산출물: 하나의 물체에 대한 6D pose 추정 코드
- [ ] 8주차: ROS2 / RViz 시각화
  - 목표: ROS2 node, topic, PoseStamped, TF, RViz 이해
  - 실습: 추정한 object pose를 ROS2로 publish
  - 산출물: RViz에서 camera frame과 object frame 시각화

### 최소 필수 항목

- [ ] 좌표계 변환: R, t, 4x4 transformation matrix 이해
- [ ] OpenCV solvePnP: 2D-3D 점 대응으로 pose 추정
- [ ] Open3D Point Cloud + ICP: depth -> point cloud -> registration
- [ ] Segmentation: 물체 mask를 얻고 해당 depth/point cloud만 추출

### 하루 공부 루틴

- [ ] 어제 막힌 문제 정리
- [ ] 필요한 이론만 공부
- [ ] 코드 실행, 수정, 시각화
- [ ] 결과 캡처와 실험 로그 작성
- [ ] 이해한 내용을 검증받기
- [ ] 다음 실험 하나 정하기

### 최종 목표

- [ ] RGB-D 또는 샘플 데이터 준비
- [ ] 물체 segmentation 수행
- [ ] object point cloud 생성
- [ ] PnP 또는 ICP 기반 6D pose 추정
- [ ] Open3D 또는 RViz에서 pose 시각화
- [ ] 실패 사례와 배운 점 정리
