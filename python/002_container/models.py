import trimesh
import json
import numpy as np


id = 4
file_path = f"./base{id}.glb"
save_path = f"./model_data{id}.json"
with open(file_path, 'rb') as file_obj:
    mesh = trimesh.load(file_obj, file_type='glb')

oriented_bounding_box = mesh.bounding_box_oriented
red_color = [1.0, 0.0, 0.0, 0.5]  # 红色, A=1 表示不透明

scale = [0.05,0.05,0.05]


target_sphere = trimesh.creation.icosphere(subdivisions=2, radius=0.1)
target_trans_matrix_sphere = trimesh.transformations.translation_matrix([0,-0.47,0])
target_sphere.apply_transform(target_trans_matrix_sphere)
target_sphere.visual.vertex_colors = np.array([red_color] * len(target_sphere.vertices))
target_trans_list = target_trans_matrix_sphere.tolist()



contact_sphere = trimesh.creation.icosphere(subdivisions=2, radius=0.05)
contact_trans_matrix_sphere = trimesh.transformations.translation_matrix([0, 0, 0])
contact_sphere.apply_transform(contact_trans_matrix_sphere)
contact_sphere.visual.vertex_colors = np.array([red_color] * len(contact_sphere.vertices))
contact_trans_list = contact_trans_matrix_sphere.tolist()
# 创建一个场景
scene = trimesh.Scene(mesh)

# axis1
axis1 = trimesh.creation.axis(axis_length=1.5)
# 旋转矩阵的参数顺序是 (X, Y, Z)   to endpose axis
trans_matrix1 = trimesh.transformations.euler_matrix(0,-1.57,0)
# 应用旋转矩阵到坐标轴
axis1.apply_transform(trans_matrix1)
transform_matrix_list1 = trans_matrix1.tolist()

data = {
    'center': oriented_bounding_box.centroid.tolist(),  # 中心点
    'extents': oriented_bounding_box.extents.tolist(),   # 尺寸
    'scale': scale,
    'target_pose': target_trans_list,    
    'contact_pose' : contact_trans_list,
    'trans_matrix' : transform_matrix_list1
}
with open(save_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)

# 将坐标轴添加到场景
axis = trimesh.creation.axis(axis_length=1.5,origin_size= 0.05)
# axis.apply_transform(trimesh.transformations.euler_matrix(0, -1.57, 0))
# scene.add_geometry(axis)
scene.add_geometry(axis1)
# # 可视化网格和坐标轴
scene.add_geometry(target_sphere)
scene.add_geometry(contact_sphere)
scene.show()





