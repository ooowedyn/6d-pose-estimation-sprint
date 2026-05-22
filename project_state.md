# Project State

## 0. 프로젝트 이름

**RGB-D Based 6D Object Pose Estimation**

이 프로젝트는 RGB-D 또는 샘플 데이터를 이용해 물체 하나를 segmentation하고, point cloud를 생성한 뒤, PnP 또는 ICP 기반으로 6D pose를 추정하고, Open3D 또는 RViz에서 시각화하는 것을 목표로 한다.

---

## 1. 현재 주차

- 현재 주차: Week 1
- 현재 단계: 좌표계·3D 변환 기초
- 현재 날짜: 2026-05-22
- 현재 상태: 프로젝트 시작 첫날
- 아직 실제 실험 결과는 없음

---

## 2. 이번 주 목표

Week 1의 목표는 6D pose estimation에서 계속 쓰이는 좌표계 변환의 기본을 이해하는 것이다.

이번 주에는 다음을 이해한다.

- vector
- matrix
- rotation matrix `R`
- translation vector `t`
- homogeneous transformation matrix `T`
- object frame
- camera frame
- world frame

이번 주의 핵심 질문은 다음이다.

> object frame에 있는 3D 점을 rotation과 translation을 이용해 camera frame 또는 world frame으로 어떻게 옮기는가?

---

## 3. 이번 주 산출물

Week 1이 끝날 때 남겨야 할 결과물은 다음이다.

- [ ] 3D 점을 정의한 Python notebook
- [ ] rotation matrix `R`를 직접 만든 예제
- [ ] translation vector `t`를 직접 적용한 예제
- [ ] 4x4 homogeneous transformation matrix `T`를 만든 예제
- [ ] 변환 전후 3D 좌표 비교
- [ ] object frame, camera frame, world frame 차이 정리
- [ ] README 또는 실험노트에 배운 점 정리

---

## 4. 오늘의 목표

Week 1 Day 1의 목표는 너무 넓게 잡지 않고, 아래 하나를 확실히 이해하는 것이다.

> 3D 점 하나가 회전 `R`과 이동 `t`를 거쳐 다른 좌표계의 점으로 바뀌는 과정을 코드로 확인한다.

오늘 할 일은 다음이다.

- [ ] 3D 점 `P_o = [x, y, z]` 정의하기
- [ ] 간단한 translation vector `t` 정의하기
- [ ] z축 기준 rotation matrix `Rz` 정의하기
- [ ] `P_c = R P_o + t` 계산하기
- [ ] 같은 변환을 4x4 transformation matrix `T`로 다시 계산하기
- [ ] 두 결과가 같은지 확인하기
- [ ] 오늘 헷갈린 개념을 `error_log.md` 또는 `experiment_log.md`에 적기

---

## 5. 현재 좌표계 Convention

초기 convention은 다음과 같이 둔다.

### Object Frame

- 물체 자체에 붙어 있는 좌표계
- 물체의 중심 또는 기준점을 origin으로 둔다
- 물체 위의 3D 점은 `P_o`로 표현한다

### Camera Frame

- 카메라에 붙어 있는 좌표계
- 카메라에서 본 물체의 위치와 방향을 표현한다
- 카메라 기준 3D 점은 `P_c`로 표현한다

### World Frame

- 실험 공간 전체의 기준 좌표계
- 아직 Week 1에서는 깊게 다루지 않는다
- 나중에 ROS2, RViz, robot base frame과 연결할 때 사용한다

### Pose Convention

이 프로젝트에서 기본 pose는 우선 다음 의미로 사용한다.

```text
object frame -> camera frame