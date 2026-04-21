import nibabel as nib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.animation as animation
import numpy as np
from skimage import measure

# Use Case Spleen_01 (our best CT model result @ 93% accuracy)
pred_path = r"c:\The Sketchbook\SEM VI\CV-Project\data\predictions_spleen\spleen_1.nii.gz"
lbl = nib.load(pred_path).get_fdata()

fig = plt.figure(figsize=(10, 10), facecolor='black')
ax = fig.add_subplot(111, projection='3d', facecolor='black')

# Label 1 = Spleen
def add_mesh(value, color, alpha, label):
    mask = (lbl == value).astype(float)
    if np.sum(mask) == 0: return # Skip if empty
    # Marching Cubes algorithm to generate 3D surface
    verts, faces, normals, values = measure.marching_cubes(mask, 0.5, step_size=2)
    mesh = Poly3DCollection(verts[faces], alpha=alpha)
    mesh.set_facecolor(color)
    mesh.set_edgecolor('white')
    mesh.set_linewidth(0.01)
    ax.add_collection3d(mesh)
    return verts

print("Rendering Spleen 3D CT model...")
v1 = add_mesh(1, [1.0, 0.7, 0.2], 0.9, 'Spleen') # Gold/Orange for Spleen

# Set limits
ax.set_xlim(0, lbl.shape[0])
ax.set_ylim(0, lbl.shape[1])
ax.set_zlim(0, lbl.shape[2])

ax.set_axis_off() 
plt.title("Premium AI Spleen 3D Visualization (93% Accuracy)\nMedical CT-Inferred Organ Model", color='white', size=14)

out_path = r"c:\The Sketchbook\SEM VI\CV-Project\best_spleen_prediction_3d.gif"

def init():
    return fig,

def update(frame):
    print(f"Rendering frame {frame}/36")
    ax.view_init(elev=20 + 5*np.sin(frame*np.pi/18), azim=frame * 10)
    return fig,

# Create animation
print("Generating final premium AI Spleen animation...")
ani = animation.FuncAnimation(fig, update, frames=36, init_func=init, blit=False)

try:
    ani.save(out_path, writer='pillow', fps=12)
    print("Saved Spleen 3D AI visualization to:", out_path)
except Exception as e:
    print("Failed to save GIF, error:", e)
