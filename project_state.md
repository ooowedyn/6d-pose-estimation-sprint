# Project State

## 0. 프로젝트 이름

**RGB-D Based 6D Object Pose Estimation**

이 프로젝트는 RGB-D 또는 샘플 데이터를 이용해 물체 하나를 segmentation하고, point cloud를 생성한 뒤, PnP 또는 ICP 기반으로 6D pose를 추정하고, Open3D 또는 RViz에서 시각화하는 것을 목표로 한다.

---

## 1. 현재 주차

- 현재 주차: Week 2
- 현재 단계: Camera Model & Calibration
- 현재 날짜: 2026-06-01
- 현재 상태: Week 1 좌표계·3D 변환 기초를 마치고, 카메라 모델과 캘리브레이션으로 넘어감
- 이번 주 핵심 결과물: camera matrix `K`, distortion coefficients, reprojection error

---

## 2. 이번 주 목표

Week 2의 목표는 6D pose estimation에서 3D 점이 2D 이미지 점으로 투영되는 과정을 이해하고, OpenCV를 이용해 카메라 내부 파라미터를 추정하는 것이다.

이번 주에는 다음을 이해한다.

- pinhole camera model
- camera coordinate
- image coordinate
- intrinsic matrix `K`
- focal length `fx`, `fy`
- principal point `cx`, `cy`
- distortion coefficient
- checkerboard calibration
- object points
- image points
- reprojection error
- image undistortion

이번 주의 핵심 질문은 다음이다.

> object frame 또는 camera frame에 있는 3D 점이 camera intrinsic `K`를 거쳐 이미지 위의 2D pixel coordinate로 어떻게 투영되는가?

Week 2는 이후 Week 3의 PnP pose estimation을 위한 준비 단계이다.  
PnP에서는 3D object points와 2D image points의 대응을 이용해 object-to-camera pose `T_co`를 추정하는데, 이때 camera matrix `K`와 distortion coefficients가 반드시 필요하다.

---

## 3. 이번 주 산출물

Week 2가 끝날 때 남겨야 할 결과물은 다음이다.

- [ ] `docs/week2_camera_model.md`
- [ ] calibration용 checkerboard 이미지 데이터
- [ ] checkerboard 내부 corner 개수 기록
- [ ] square size 기록
- [ ] `notebooks/week2_day3_corner_detection.ipynb`
- [ ] checkerboard corner detection 결과 이미지
- [ ] `outputs/calibration/camera_matrix.npy`
- [ ] `outputs/calibration/dist_coeffs.npy`
- [ ] reprojection error 계산 결과
- [ ] undistortion 전후 비교 이미지
- [ ] `docs/week2_distortion.md`
- [ ] `experiment_log.md`에 Experiment 002 기록
- [ ] `error_log.md`에 calibration failure case 또는 reprojection error 관련 문제 기록
- [ ] README에 Week 2 결과 요약 추가

---

## 4. 오늘의 목표

Week 2 Day 1의 목표는 너무 넓게 잡지 않고, 아래 하나를 확실히 이해하는 것이다.

> 카메라가 3D 점을 2D 이미지 평면으로 투영할 때, intrinsic matrix `K`가 어떤 역할을 하는지 이해한다.

오늘 할 일은 다음이다.

- [ ] pinhole camera model 개념 정리하기
- [ ] camera coordinate와 image coordinate 차이 정리하기
- [ ] focal length `fx`, `fy` 의미 이해하기
- [ ] principal point `cx`, `cy` 의미 이해하기
- [ ] intrinsic matrix `K` 구조 외우기
- [ ] 3D camera point `P_c = [X, Y, Z]`가 2D pixel point `[u, v]`로 가는 흐름 정리하기
- [ ] `K`가 Week 3 PnP와 Week 4 depth-to-point-cloud에서 어떻게 쓰이는지 메모하기
- [ ] 오늘 헷갈린 개념을 `error_log.md` 또는 `experiment_log.md`에 적기

---

## 5. 현재 Camera Model Convention

Week 2에서는 카메라 모델을 다음 convention으로 정리한다.

### Camera Frame

- 카메라에 붙어 있는 3D 좌표계
- 카메라 기준 3D 점은 `P_c = [X, Y, Z]`로 표현한다
- `Z`는 카메라로부터의 깊이, 즉 depth 방향으로 사용한다
- 이후 PnP에서 추정하는 pose는 기본적으로 object frame에서 camera frame으로 가는 `T_co`로 해석한다

### Image Coordinate

- 이미지 위의 2D pixel 좌표계
- 이미지 점은 `p = [u, v]`로 표현한다
- `u`는 이미지의 가로 방향 pixel 좌표
- `v`는 이미지의 세로 방향 pixel 좌표
- OpenCV에서는 보통 이미지의 왼쪽 위가 원점이다

### Intrinsic Matrix

카메라 내부 파라미터는 다음 형태의 matrix로 정리한다.

```text
K = [[fx,  0, cx],
     [ 0, fy, cy],
     [ 0,  0,  1]]