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

## 8. 세부 커리큘럼
## Week 1: Coordinate Frames & 3D Transformation

### Day 1: 3D 점 하나 변환하기

* 목표

    * `R`, `t`가 3D 점을 어떻게 바꾸는지 가장 작은 예제로 확인합니다.
    * object frame의 점이 camera frame의 점으로 변환되는 과정을 이해합니다.

* 할 일

    * 3D 점 `P_o = [1, 0, 0]` 정의
    * z축 기준 90도 회전행렬 `Rz` 정의
    * translation vector `t` 정의
    * `P_c = R P_o + t` 계산
    * 4x4 transformation matrix `T`로 같은 결과 확인
    * 두 결과가 같은지 확인

* 산출물

    * `notebooks/week1_day1_transform_basics.ipynb`
    * `R P + t`와 `T P_h` 비교 결과

* 반드시 이해할 문장

    * `R`은 방향을 바꾸고, `t`는 위치를 옮긴다.


### Day 2: 여러 개의 3D 점 변환하기

* 목표

    * 점 하나가 아니라 여러 개의 3D 점을 한 번에 변환합니다.
    * 물체를 구성하는 여러 점들이 같은 pose transform으로 함께 움직인다는 것을 이해합니다.

* 할 일

    * 큐브 또는 삼각형의 3D 점 여러 개 정의
    * object frame 기준 point set 생성
    * 같은 `R`, `t`를 모든 점에 적용
    * 변환 전 좌표와 변환 후 좌표 비교
    * point array shape 확인
    * row vector / column vector 혼동 여부 확인

* 산출물

    * 여러 3D point를 변환한 NumPy 코드
    * 변환 전/후 좌표 표
    * `experiment_log.md`에 Experiment 001 또는 002 기록

* 반드시 이해할 문장

    * 6D pose에서는 물체 위의 모든 3D 점이 같은 `R`, `t`로 함께 움직인다.


### Day 3: Homogeneous Transformation Matrix 이해하기

* 목표

    * `R`과 `t`를 4x4 transformation matrix `T`로 묶는 이유를 이해합니다.
    * 3D point를 homogeneous coordinate로 표현하는 방법을 익힙니다.

* 할 일

    * 3x3 rotation matrix `R` 정의
    * 3x1 translation vector `t` 정의
    * 4x4 transformation matrix `T` 구성
    * 3D point `[x, y, z]`를 homogeneous point `[x, y, z, 1]`로 변환
    * `T @ P_h` 계산
    * `R @ P + t` 결과와 비교

* 산출물

    * `T_co`를 직접 만든 코드
    * `R P + t`와 `T P_h` 결과 비교
    * homogeneous coordinate 설명 메모

* 반드시 이해할 문장

    * `T`는 rotation과 translation을 한 번에 적용하기 위해 만든 4x4 pose matrix이다.


### Day 4: 좌표계 변환 방향 구분하기

* 목표

    * `T_co`와 `T_oc`가 서로 다른 변환이라는 것을 이해합니다.
    * transformation inverse가 왜 필요한지 확인합니다.

* 할 일

    * object frame에서 camera frame으로 가는 `T_co` 정의
    * `T_oc = inverse(T_co)` 계산
    * object point를 camera point로 변환
    * camera point를 다시 object point로 복원
    * 복원 결과가 원래 `P_o`와 같은지 확인
    * 변환 방향을 말로 설명

* 산출물

    * `T_co`와 `T_oc` 비교 코드
    * `P_o -> P_c -> P_o` 복원 결과
    * inverse transform 실험 로그

* 반드시 이해할 문장

    * 변환 방향을 헷갈리면 pose가 맞아도 결과가 틀려 보인다.


### Day 5: Object Frame, Camera Frame, World Frame 정리하기

* 목표

    * object frame, camera frame, world frame의 차이를 말로 설명할 수 있게 정리합니다.
    * 같은 3D 점도 어떤 frame에서 보느냐에 따라 좌표값이 달라진다는 것을 이해합니다.

* 할 일

    * object frame 정의
    * camera frame 정의
    * world frame 정의
    * object frame의 점이 camera frame에서 어떻게 표현되는지 예시 작성
    * frame convention 문장 정리
    * `T_co`, `T_wo`, `T_wc` 같은 표기법 의미 정리

* 산출물

    * `docs/week1_coordinate_frames.md`
    * README에 `Coordinate Convention` 섹션 초안 추가

* 반드시 이해할 문장

    * 같은 3D 점도 어떤 frame에서 보느냐에 따라 좌표값이 달라진다.


### Day 6: 3D 변환 시각화하기

* 목표

    * 변환 전후 3D 점과 좌표축을 시각화해서 좌표계 변환을 눈으로 확인합니다.
    * 시각화를 통해 회전 방향이나 translation 실수를 잡는 연습을 합니다.

* 할 일

    * matplotlib 3D plot 준비
    * object frame의 3D 점 시각화
    * camera frame으로 변환된 점 시각화
    * x, y, z 좌표축 표시
    * 변환 전후 point set 비교
    * 결과 이미지 저장

* 산출물

    * `notebooks/week1_day6_visualize_transform.ipynb`
    * `results/week1_transform_visualization.png`
    * 변환 전후 3D plot 이미지

* 반드시 이해할 문장

    * 시각화는 좌표계 방향 실수를 잡는 가장 빠른 방법이다.


### Day 7: 정리 및 README 업데이트

* 목표

    * 1주차 내용을 실험노트와 README에 정리합니다.
    * `R`, `t`, `T`, coordinate frame의 의미를 6D pose pipeline과 연결해서 설명합니다.

* 할 일

    * Experiment 001 정리
    * Week 1에서 배운 개념 정리
    * 헷갈린 점 정리
    * `R`, `t`, `T` 설명 작성
    * object frame, camera frame, world frame 설명 작성
    * README에 Week 1 결과 추가
    * `project_state.md` 업데이트
    * 다음 주 Camera Calibration으로 넘어갈 준비

* 산출물

    * `experiment_log.md` 업데이트
    * `README.md` 업데이트
    * `project_state.md` 업데이트
    * Week 1 학습 요약

* 반드시 이해할 문장

    * 6D pose estimation은 결국 물체 좌표계와 카메라 좌표계 사이의 `R`, `t`를 찾는 문제다.
    
## Week 2: Camera Model & Calibration

### Day 1: Pinhole Camera Model 이해

* 목표

    * 카메라가 3D 점을 2D 이미지 평면으로 투영하는 기본 원리를 이해합니다.
    * `intrinsic matrix`가 6D pose pipeline에서 왜 필요한지 이해합니다.

* 할 일

    * pinhole camera model 개념 정리
    * image coordinate, camera coordinate 차이 정리
    * focal length, principal point 의미 정리
    * intrinsic matrix `K` 구조 정리
    * `fx`, `fy`, `cx`, `cy`가 각각 무엇인지 정리

* 산출물

    * `docs/week2_camera_model.md`
    * README에 camera model 요약 추가


### Day 2: Checkerboard Calibration 데이터 준비

* 목표

    * 카메라 내부 파라미터를 추정하기 위한 체커보드 이미지 데이터를 준비합니다.

* 할 일

    * checkerboard pattern 준비
    * 여러 각도에서 checkerboard 이미지 촬영 또는 샘플 데이터 준비
    * 이미지 파일 경로 정리
    * checkerboard 내부 corner 개수 확인
    * square size 단위 결정

* 산출물

    * `data/calibration/images/`
    * calibration 이미지 목록
    * checkerboard 설정값 기록


### Day 3: Checkerboard Corner Detection

* 목표

    * OpenCV로 checkerboard corner를 검출하고, calibration 입력 형식을 이해합니다.

* 할 일

    * `cv2.findChessboardCorners` 사용
    * object points 생성
    * image points 생성
    * 검출된 corner를 이미지 위에 시각화
    * 실패 이미지가 있다면 원인 기록

* 산출물

    * `notebooks/week2_day3_corner_detection.ipynb`
    * corner detection 결과 이미지
    * `experiment_log.md`에 Experiment 002 기록


### Day 4: Camera Calibration 수행

* 목표

    * OpenCV camera calibration을 수행하여 camera matrix와 distortion coefficient를 얻습니다.

* 할 일

    * `cv2.calibrateCamera` 실행
    * camera matrix `K` 출력
    * distortion coefficients 출력
    * rotation vector, translation vector 출력 형식 확인
    * calibration 결과 저장

* 산출물

    * `outputs/calibration/camera_matrix.npy`
    * `outputs/calibration/dist_coeffs.npy`
    * calibration 실험 로그


### Day 5: Reprojection Error 계산

* 목표

    * calibration 결과가 얼마나 좋은지 reprojection error로 확인합니다.

* 할 일

    * 3D checkerboard point를 이미지로 다시 projection
    * 검출된 2D corner와 projected point 비교
    * 평균 reprojection error 계산
    * error가 큰 이미지 확인
    * error가 큰 원인 후보 기록

* 산출물

    * reprojection error 수치
    * error 분석 노트
    * `error_log.md` 업데이트


### Day 6: Image Undistortion 확인

* 목표

    * distortion coefficient가 실제 이미지 보정에 어떻게 쓰이는지 확인합니다.

* 할 일

    * `cv2.undistort` 사용
    * 원본 이미지와 undistorted image 비교
    * 왜곡 보정 전후 시각화
    * distortion coefficient의 역할 정리
    * solvePnP에서 distortion coefficient가 왜 필요한지 정리

* 산출물

    * undistortion 전후 비교 이미지
    * `docs/week2_distortion.md`


### Day 7: 정리 및 README 업데이트

* 목표

    * 2주차 내용을 실험노트와 README에 정리합니다.

* 할 일

    * Experiment 002 정리
    * camera matrix 정리
    * distortion coefficient 정리
    * reprojection error 결과 정리
    * README에 Week 2 결과 추가
    * 다음 주 PnP로 넘어갈 준비

* 산출물

    * `experiment_log.md` 업데이트
    * `README.md` 업데이트
    * `project_state.md` 업데이트



## Week 3: PnP Based Pose Estimation

### Day 1: 2D-3D Correspondence 이해

* 목표

    * PnP가 2D 이미지 점과 3D object point의 대응으로 pose를 구한다는 것을 이해합니다.

* 할 일

    * object point와 image point 개념 정리
    * object frame 기준 3D 점 정의 방식 정리
    * image coordinate 기준 2D 점 정의 방식 정리
    * correspondence 순서가 왜 중요한지 정리
    * `solvePnP` 입력/출력 형식 확인

* 산출물

    * `docs/week3_pnp_correspondence.md`


### Day 2: 3D Object Points 정의

* 목표

    * 큐브 또는 마커의 3D 기준점을 object frame에서 정의합니다.

* 할 일

    * object frame origin 결정
    * 큐브 또는 마커 corner point 정의
    * `object_points` 배열 생성
    * 단위 설정: meter 또는 millimeter
    * 점 순서 문서화

* 산출물

    * `notebooks/week3_day2_object_points.ipynb`
    * object point 좌표표


### Day 3: 2D Image Points 지정

* 목표

    * 이미지에서 object point와 대응되는 2D image point를 준비합니다.

* 할 일

    * 샘플 이미지 준비
    * 수동 또는 자동으로 2D corner point 선택
    * `image_points` 배열 생성
    * object point와 image point 순서 일치 확인
    * 대응점 시각화

* 산출물

    * image point가 표시된 이미지
    * `experiment_log.md`에 Experiment 003 기록


### Day 4: OpenCV solvePnP 실행

* 목표

    * `solvePnP`로 object-to-camera pose를 추정합니다.

* 할 일

    * camera matrix `K` 불러오기
    * distortion coefficient 불러오기
    * `cv2.solvePnP` 실행
    * `rvec`, `tvec` 출력
    * `rvec`를 rotation matrix `R`로 변환
    * `T_co` 구성

* 산출물

    * `notebooks/week3_day4_solvepnp.ipynb`
    * 추정된 `rvec`, `tvec`, `T_co`


### Day 5: 3D Axis Projection

* 목표

    * 추정한 pose가 맞는지 이미지 위에 3D 좌표축을 그려 확인합니다.

* 할 일

    * object frame의 x, y, z축 점 정의
    * `cv2.projectPoints` 사용
    * 이미지 위에 3D axis overlay
    * 축 방향이 예상과 맞는지 확인
    * 이상하면 좌표계 방향, point order, camera matrix 확인

* 산출물

    * 3D axis overlay 이미지
    * pose 결과 해석 노트


### Day 6: RANSAC과 Reprojection Error 확인

* 목표

    * 잘못된 correspondence가 pose에 미치는 영향을 이해하고 RANSAC을 적용합니다.

* 할 일

    * `cv2.solvePnPRansac` 실행
    * inlier/outlier 확인
    * reprojection error 계산
    * 일반 `solvePnP`와 RANSAC 결과 비교
    * 실패 케이스 기록

* 산출물

    * RANSAC 결과
    * reprojection error 비교
    * `error_log.md` 업데이트


### Day 7: 정리 및 README 업데이트

* 목표

    * 3주차 PnP 실습 결과를 README와 실험노트에 정리합니다.

* 할 일

    * Experiment 003 정리
    * `object_points`, `image_points` 설명 추가
    * `solvePnP` 입력/출력 정리
    * `rvec`, `tvec`, `T_co` 의미 정리
    * 3D axis overlay 이미지 추가
    * 다음 주 RGB-D / Point Cloud로 넘어갈 준비

* 산출물

    * `README.md` 업데이트
    * `experiment_log.md` 업데이트
    * `project_state.md` 업데이트



## Week 4: RGB-D & Point Cloud

### Day 1: Depth Image와 RGB-D 이해

* 목표

    * depth image가 무엇이고, RGB image와 어떻게 결합되는지 이해합니다.

* 할 일

    * depth image 개념 정리
    * depth scale 개념 정리
    * RGB-D 데이터 구조 정리
    * pixel coordinate와 depth 값 관계 정리
    * 6D pose에서 depth가 왜 중요한지 정리

* 산출물

    * `docs/week4_rgbd_depth.md`


### Day 2: RGB-D 데이터 불러오기

* 목표

    * RGB image와 depth image를 코드에서 불러오고 shape와 값 범위를 확인합니다.

* 할 일

    * RGB 이미지 불러오기
    * depth 이미지 불러오기
    * image size 확인
    * depth min/max 확인
    * depth scale 적용 여부 확인
    * RGB와 depth가 같은 해상도인지 확인

* 산출물

    * `notebooks/week4_day2_load_rgbd.ipynb`
    * RGB/depth 기본 통계


### Day 3: Depth를 3D Point로 변환

* 목표

    * camera intrinsic을 이용해 depth pixel을 camera frame의 3D point로 변환합니다.

* 할 일

    * pixel coordinate `(u, v)` 정의
    * depth `Z` 읽기
    * `X = (u - cx) * Z / fx` 계산
    * `Y = (v - cy) * Z / fy` 계산
    * 여러 pixel에 대해 3D point 생성
    * camera frame 기준 point cloud 의미 정리

* 산출물

    * depth-to-3D 변환 코드
    * `experiment_log.md`에 Experiment 004 기록


### Day 4: Open3D Point Cloud 생성

* 목표

    * RGB-D 데이터를 Open3D point cloud로 변환하고 시각화합니다.

* 할 일

    * Open3D 설치 및 import 확인
    * RGBDImage 생성
    * camera intrinsic 설정
    * point cloud 생성
    * Open3D viewer로 시각화
    * point cloud 좌표계 방향 확인

* 산출물

    * `notebooks/week4_day4_open3d_pointcloud.ipynb`
    * Open3D point cloud 시각화 캡처


### Day 5: Point Cloud Filtering, Crop, Downsampling

* 목표

    * point cloud에서 필요한 영역만 남기고 노이즈를 줄이는 기본 처리를 익힙니다.

* 할 일

    * depth range filtering
    * voxel downsampling
    * statistical outlier removal
    * 관심 영역 crop
    * 처리 전후 point 수 비교
    * 시각화 결과 비교

* 산출물

    * filtering 전후 point cloud 이미지
    * point 수 비교표


### Day 6: Object-only Point Cloud 만들기

* 목표

    * 물체 주변 영역만 crop하여 object point cloud를 만듭니다.

* 할 일

    * bounding box 또는 수동 ROI 설정
    * ROI 내부 depth만 선택
    * object-only point cloud 생성
    * 배경 point 제거
    * Open3D로 object point cloud 시각화

* 산출물

    * object-only point cloud
    * `outputs/week4/object_pointcloud.ply`


### Day 7: 정리 및 README 업데이트

* 목표

    * 4주차 RGB-D / point cloud 실습 결과를 정리합니다.

* 할 일

    * Experiment 004 정리
    * depth image와 point cloud 관계 정리
    * depth scale에서 헷갈린 점 정리
    * Open3D 시각화 결과 추가
    * README에 Week 4 결과 추가
    * 다음 주 ICP로 넘어갈 준비

* 산출물

    * `README.md` 업데이트
    * `experiment_log.md` 업데이트
    * `project_state.md` 업데이트



## Week 5: Point Cloud Registration & ICP

### Day 1: Registration과 ICP 개념 이해

* 목표

    * source point cloud와 target point cloud를 맞추는 registration 문제를 이해합니다.

* 할 일

    * source point cloud 개념 정리
    * target point cloud 개념 정리
    * registration이 pose estimation과 어떻게 연결되는지 정리
    * ICP의 기본 아이디어 정리
    * initial transformation의 필요성 정리

* 산출물

    * `docs/week5_icp_registration.md`


### Day 2: Toy Point Cloud 준비

* 목표

    * ICP를 이해하기 위한 간단한 source/target point cloud를 준비합니다.

* 할 일

    * 간단한 3D point set 생성
    * 원본 point cloud를 target으로 사용
    * `R`, `t`를 적용해 source point cloud 생성
    * source와 target을 함께 시각화
    * 정합 전 차이 확인

* 산출물

    * `notebooks/week5_day2_toy_pointcloud.ipynb`
    * 정합 전 source/target 시각화


### Day 3: Initial Transformation 적용

* 목표

    * ICP 전에 초기 pose가 왜 필요한지 확인합니다.

* 할 일

    * identity transformation으로 시작
    * 임의의 initial transformation 설정
    * source point cloud를 initial pose로 이동
    * target과 얼마나 가까운지 시각화
    * 초기값이 나쁠 때 문제 기록

* 산출물

    * initial transformation 비교 이미지
    * `error_log.md`에 초기 pose 관련 메모


### Day 4: Point-to-Point ICP 실행

* 목표

    * Open3D로 point-to-point ICP를 실행하고 transformation matrix를 해석합니다.

* 할 일

    * `registration_icp` 실행
    * point-to-point estimation 사용
    * ICP 결과 transformation 출력
    * source를 변환하여 target과 비교
    * ICP 전후 시각화

* 산출물

    * `notebooks/week5_day4_icp_point_to_point.ipynb`
    * ICP 결과 `T`
    * `experiment_log.md`에 Experiment 005 기록


### Day 5: Point-to-Plane ICP와 Normal 이해

* 목표

    * point-to-plane ICP가 normal 정보를 사용한다는 것을 이해합니다.

* 할 일

    * point cloud normal 추정
    * point-to-plane ICP 실행
    * point-to-point 결과와 비교
    * fitness, RMSE 비교
    * normal 방향이 결과에 미치는 영향 정리

* 산출물

    * ICP 방식별 결과 비교
    * fitness/RMSE 표


### Day 6: ICP 결과 Pose 해석

* 목표

    * ICP 결과 transformation matrix가 어떤 frame 사이 변환인지 해석합니다.

* 할 일

    * ICP output transformation 읽기
    * source가 target으로 가는 변환인지 확인
    * `R`, `t` 분리
    * translation error 계산
    * rotation 차이 간단히 확인
    * 실패 케이스 기록

* 산출물

    * ICP pose 해석 노트
    * `error_log.md` 업데이트


### Day 7: 정리 및 README 업데이트

* 목표

    * 5주차 ICP 실습 결과를 README와 실험노트에 정리합니다.

* 할 일

    * Experiment 005 정리
    * source/target point cloud 설명 추가
    * ICP 전후 이미지 추가
    * ICP 결과 transformation matrix 해석 추가
    * 실패 원인 정리
    * 다음 주 Segmentation으로 넘어갈 준비

* 산출물

    * `README.md` 업데이트
    * `experiment_log.md` 업데이트
    * `project_state.md` 업데이트



## Week 6: Segmentation / Detection

### Day 1: Bounding Box와 Mask 이해

* 목표

    * bounding box와 mask의 차이를 이해하고, 6D pose에서 mask가 왜 중요한지 이해합니다.

* 할 일

    * bounding box 개념 정리
    * semantic segmentation 개념 정리
    * instance segmentation 개념 정리
    * mask가 depth와 결합되는 방식 정리
    * object-only point cloud와 연결

* 산출물

    * `docs/week6_segmentation_mask.md`


### Day 2: 샘플 이미지에서 물체 영역 표시

* 목표

    * 실제 이미지에서 물체 영역을 bounding box 또는 manual mask로 표시합니다.

* 할 일

    * 샘플 이미지 준비
    * 물체 bounding box 지정
    * manual mask 생성
    * mask 시각화
    * background와 object 영역 구분

* 산출물

    * `notebooks/week6_day2_manual_mask.ipynb`
    * mask overlay 이미지


### Day 3: Segmentation 모델 사용

* 목표

    * YOLO/SAM/Mask R-CNN 중 하나를 사용해 물체 mask를 얻어봅니다.

* 할 일

    * 사용할 segmentation 도구 선택
    * 샘플 이미지 추론 실행
    * detection 결과 확인
    * mask 결과 확인
    * confidence 또는 class 결과 기록

* 산출물

    * segmentation 결과 이미지
    * `experiment_log.md`에 Experiment 006 기록


### Day 4: Mask와 Depth 결합

* 목표

    * segmentation mask를 depth image에 적용해 물체 영역의 depth만 추출합니다.

* 할 일

    * mask 불러오기
    * depth image 불러오기
    * mask 영역의 depth만 남기기
    * object-only depth image 생성
    * depth 값 이상치 확인

* 산출물

    * object-only depth image
    * mask + depth 결합 코드


### Day 5: Mask 기반 Object Point Cloud 생성

* 목표

    * mask가 적용된 depth image로 object-only point cloud를 만듭니다.

* 할 일

    * masked depth를 point cloud로 변환
    * background point 제거 확인
    * Open3D 시각화
    * point cloud 저장
    * mask 품질이 point cloud에 미치는 영향 기록

* 산출물

    * `outputs/week6/object_masked_pointcloud.ply`
    * object-only point cloud 시각화


### Day 6: Segmentation Failure Case 정리

* 목표

    * segmentation이 틀렸을 때 6D pose estimation이 어떻게 망가지는지 이해합니다.

* 할 일

    * 잘못된 mask 사례 확인
    * 배경이 포함된 경우 확인
    * 물체 일부가 빠진 경우 확인
    * depth hole이 있는 경우 확인
    * pose estimation에 미칠 영향 정리

* 산출물

    * `error_log.md` 업데이트
    * segmentation failure case 이미지


### Day 7: 정리 및 README 업데이트

* 목표

    * 6주차 segmentation 결과를 README와 실험노트에 정리합니다.

* 할 일

    * Experiment 006 정리
    * bounding box와 mask 차이 정리
    * mask + depth 결합 과정 정리
    * object-only point cloud 결과 추가
    * 실패 사례 정리
    * 다음 주 6D pose mini pipeline으로 넘어갈 준비

* 산출물

    * `README.md` 업데이트
    * `experiment_log.md` 업데이트
    * `project_state.md` 업데이트



## Week 7: 6D Pose Mini Pipeline

### Day 1: Mini Pipeline 입출력 정의

* 목표

    * 지금까지 배운 요소를 연결해 하나의 6D pose mini pipeline 구조를 정의합니다.

* 할 일

    * 입력 데이터 정의
    * 출력 pose 형식 정의
    * pipeline 단계 정리
    * 사용할 방식 선택: PnP 또는 ICP
    * 폴더 구조 정리

* 산출물

    * `docs/week7_pipeline_design.md`
    * mini pipeline diagram


### Day 2: 데이터 로딩 모듈 작성

* 목표

    * RGB image, depth image, camera intrinsic, mask를 한 번에 불러오는 코드를 작성합니다.

* 할 일

    * RGB image loader 작성
    * depth image loader 작성
    * camera matrix loader 작성
    * mask loader 작성
    * 입력 데이터 shape 확인
    * 입력 데이터 validation 코드 작성

* 산출물

    * `src/pipeline/load_data.py`
    * `notebooks/week7_day2_load_inputs.ipynb`


### Day 3: Object Point Cloud 생성 모듈 작성

* 목표

    * mask와 depth를 이용해 object-only point cloud를 생성하는 단계를 pipeline에 넣습니다.

* 할 일

    * mask 적용
    * depth-to-point-cloud 변환
    * filtering 적용
    * downsampling 적용
    * object point cloud 저장
    * Open3D 시각화 확인

* 산출물

    * `src/pipeline/create_object_pointcloud.py`
    * object point cloud 결과


### Day 4: Pose Estimation 모듈 작성

* 목표

    * PnP 또는 ICP 중 하나를 선택해 object pose를 추정합니다.

* 할 일

    * PnP 방식이면 2D-3D correspondence 준비
    * ICP 방식이면 model point cloud와 observed point cloud 준비
    * pose estimation 실행
    * `R`, `t`, `T` 출력
    * pose convention 확인

* 산출물

    * `src/pipeline/estimate_pose.py`
    * `experiment_log.md`에 Experiment 007 기록


### Day 5: Pose Visualization

* 목표

    * 추정한 pose를 이미지 또는 3D viewer에서 확인합니다.

* 할 일

    * PnP 방식이면 이미지 위에 3D axis projection
    * ICP 방식이면 Open3D에서 model/observed point cloud 정합 결과 표시
    * pose 결과 이미지 저장
    * 시각화 결과가 직관적으로 맞는지 확인
    * 좌표축 방향 확인

* 산출물

    * pose visualization 이미지
    * `outputs/week7/pose_result.png`


### Day 6: Pose Evaluation 기초

* 목표

    * pose 결과를 간단한 지표로 평가하는 방법을 익힙니다.

* 할 일

    * translation error 개념 정리
    * rotation error 개념 정리
    * 2D projection error 개념 정리
    * ADD / ADD-S 개념 간단 정리
    * 현재 프로젝트에서 쓸 수 있는 평가 방식 선택

* 산출물

    * `docs/week7_pose_evaluation.md`
    * 간단한 error 계산 코드


### Day 7: 정리 및 README 업데이트

* 목표

    * 7주차 mini pipeline 결과를 README와 실험노트에 정리합니다.

* 할 일

    * Experiment 007 정리
    * pipeline 입력/출력 정리
    * pose estimation 결과 정리
    * visualization 결과 추가
    * failure case 정리
    * 다음 주 ROS2 / RViz로 넘어갈 준비

* 산출물

    * `README.md` 업데이트
    * `experiment_log.md` 업데이트
    * `project_state.md` 업데이트



## Week 8: ROS2 / RViz Visualization

### Day 1: ROS2 Topic과 PoseStamped 이해

* 목표

    * 추정한 object pose를 ROS2 메시지로 표현하는 방법을 이해합니다.

* 할 일

    * ROS2 node 개념 정리
    * topic 개념 정리
    * `PoseStamped` 메시지 구조 확인
    * position과 orientation 필드 확인
    * quaternion 표현 정리

* 산출물

    * `docs/week8_ros2_posestamped.md`


### Day 2: Pose Publisher Node 작성

* 목표

    * 추정한 object pose를 ROS2 topic으로 publish하는 node를 작성합니다.

* 할 일

    * ROS2 Python package 생성
    * pose publisher node 작성
    * `PoseStamped` 메시지 생성
    * `frame_id` 설정
    * topic publish 확인

* 산출물

    * `ros2_ws/src/pose_publisher/`
    * pose publish 코드


### Day 3: TF 개념 이해

* 목표

    * camera frame, object frame, world frame 관계를 TF로 표현하는 방법을 이해합니다.

* 할 일

    * TF tree 개념 정리
    * parent frame과 child frame 차이 정리
    * camera frame 설정
    * object frame 설정
    * transform broadcaster 개념 확인

* 산출물

    * `docs/week8_tf_concepts.md`


### Day 4: TF Broadcaster 작성

* 목표

    * 추정한 object pose를 TF transform으로 publish합니다.

* 할 일

    * static transform과 dynamic transform 차이 확인
    * `TransformStamped` 메시지 작성
    * translation 설정
    * rotation quaternion 설정
    * camera frame에서 object frame으로 TF publish

* 산출물

    * TF broadcaster node
    * `tf2_echo` 확인 결과


### Day 5: RViz에서 Pose 시각화

* 목표

    * RViz에서 camera frame과 object frame을 시각화합니다.

* 할 일

    * RViz 실행
    * Fixed Frame 설정
    * TF display 추가
    * Pose display 추가
    * camera frame과 object frame 방향 확인
    * 시각화 캡처 저장

* 산출물

    * RViz 캡처 이미지
    * `outputs/week8/rviz_pose_visualization.png`


### Day 6: Mini Pipeline과 ROS2 연결

* 목표

    * Week 7의 pose estimation 결과를 ROS2 publisher와 연결합니다.

* 할 일

    * pose estimation 결과 `R`, `t` 불러오기
    * rotation matrix를 quaternion으로 변환
    * `PoseStamped` publish
    * TF publish
    * RViz에서 결과 확인
    * frame convention 문제 확인

* 산출물

    * mini pipeline + ROS2 연결 코드
    * RViz 최종 데모 캡처


### Day 7: 최종 정리 및 README 업데이트

* 목표

    * 8주 전체 프로젝트를 README와 실험노트에 최종 정리합니다.

* 할 일

    * Experiment 008 정리
    * ROS2 / RViz 결과 정리
    * 최종 pipeline 설명 추가
    * calibration, PnP, point cloud, ICP, segmentation 결과 이미지 정리
    * failure cases 정리
    * What I Learned 작성
    * 포트폴리오용 프로젝트 소개 문장 작성

* 산출물

    * 최종 `README.md`
    * 최종 `experiment_log.md`
    * 최종 `project_state.md`
    * RViz demo image
    * 포트폴리오용 소개 문장