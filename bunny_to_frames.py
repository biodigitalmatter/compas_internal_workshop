from compas import get_bunny
from compas.datastructures import Mesh

from compas_ghpython import draw_mesh


bunny = Mesh.from_ply(get_bunny())

print(bunny)

a = draw_mesh(*bunny.to_vertices_and_faces())
