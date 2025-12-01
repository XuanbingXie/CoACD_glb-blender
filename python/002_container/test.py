import coacd
from trimesh import load, Trimesh

# Load the input 3D model
input_file = 'python/002_container/1101.glb'
mesh = load(input_file, force='mesh')

# Create CoACD's Mesh object
coacd_mesh = coacd.Mesh(mesh.vertices, mesh.faces)

# Run convex decomposition
parts = coacd.run_coacd(coacd_mesh)

# Inspect the output
print(f"Number of parts: {len(parts)}")
for i, part in enumerate(parts):
    print(f"Part {i}: {part} (Type: {type(part)})")  # Inspect each part

# Continue with saving the meshes after confirming their structure
output_file_prefix = 'output_part_'  # Output file name prefix

for i, part in enumerate(parts):
    # Extract vertices and faces depending on the structure of part
    if isinstance(part, list) and len(part) >= 2:
        vertices = part[0]  # Assuming first element contains vertices
        faces = part[1]  # Assuming second element contains faces
    else:
        print(f"Unexpected structure for part {i}: {part}")
        continue

        # Create Trimesh object
    part_mesh = Trimesh(vertices=vertices, faces=faces)
    output_file = f"{output_file_prefix}{i}.glb"  # Set output file name
    part_mesh.export(output_file, file_type='glb')  # Export as GLB format
    print(f"Saved {output_file}")

print("All parts have been saved.")

