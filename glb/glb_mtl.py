import bpy

# 假设源物体和目标物体的名字
source_object_name = "SourceObject"  # 替换为源物体名
target_object_name = "TargetObject"  # 替换为目标物体名

# 获取对象
source_object = bpy.data.objects.get(source_object_name)
target_object = bpy.data.objects.get(target_object_name)

if source_object and target_object:
    # 获取源物体的材质
    source_materials = source_object.data.materials

    # 清除目标物体的现有材质
    target_object.data.materials.clear()

    # 将源物体的材质复制给目标物体
    for mat in source_materials:
        target_object.data.materials.append(mat)

    print("材质已成功复制！")
else:
    print("未找到相应的物体。请检查名称。")