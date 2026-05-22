# Glossary

6D Pose Estimation을 공부하면서 자주 나오는 용어를 정리하는 문서.

---

## 작성 형식

### 용어명

**영문:**  
**한 줄 정의:**  
**6D Pose에서의 역할:**  
**예시:**  
**헷갈리는 개념:**  
**내가 이해한 설명:**  

---

## 예시

### 6D Pose

**영문:** 6D Object Pose  
**한 줄 정의:** 물체의 3D 위치와 3D 회전을 함께 나타내는 값  
**6D Pose에서의 역할:** 최종적으로 추정해야 하는 대상  
**예시:** 카메라 기준으로 물체가 앞쪽 50cm에 있고, z축 기준으로 30도 회전해 있는 상태  
**헷갈리는 개념:** 2D bounding box는 이미지상의 위치만 나타내지만, 6D pose는 3D 공간상의 위치와 방향을 나타낸다.  
**내가 이해한 설명:** 6D pose는 물체가 3D 공간에서 어디에 있고 어느 방향을 보고 있는지를 나타내는 값이다.

---

## 정리할 용어 목록

- 6D Pose
- Object Frame
- Camera Frame
- World Frame
- Robot Base Frame
- Rotation Matrix
- Translation Vector
- Homogeneous Transformation
- Quaternion
- Euler Angle
- Intrinsic Matrix
- Extrinsic Parameter
- Distortion Coefficient
- Camera Calibration
- Reprojection Error
- 2D-3D Correspondence
- PnP
- RANSAC
- Depth Image
- RGB-D
- Point Cloud
- Voxel Downsampling
- ICP
- Registration
- Segmentation
- Mask
- ADD
- ADD-S
- PoseStamped
- TF
- RViz
