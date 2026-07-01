import numpy as np
from PIL import Image

""" Change the constant python parameters here 
    Will not change during execution predefine """
TERRAIN_TYPE = "Terraced"   # Choose from [Terraced, Flat, Hills]
RESOLUTION = 7      # How detailed the Heightmap is
TERRACE_STEPS = 7   # number of flat terrace levels on slopes
SEED = 29           # change this to randomize
VALLEY_SIZE = 0.2   # How wide the valley is
MULTIPLIER = 24     # Vertically multiply the hills


size = 2**RESOLUTION + 1
rng = np.random.default_rng(SEED)

def fbm(size, octaves=6, persistence=0.5):
    """Fractal motion to generate
    Size = """
    out = np.zeros((size, size), dtype=np.float64)
    amp, freq, total = 1.0, 2.0, 0.0
    for _ in range(octaves):
        n = max(2, int(freq) + 1)
        coarse = rng.random((n, n))

        img = np.array(Image.fromarray((coarse * 255).astype(np.uint8))
                       .resize((size, size), Image.BILINEAR), dtype=np.float64) / 255.0
        out += (img * amp)
        total += amp
        amp *= persistence
        freq *= 2
    return (out / total)

yy, xx = np.mgrid[0:size, 0:size] / size

if TERRAIN_TYPE == "Terraced":
    hills = fbm(size, octaves=6, persistence=0.55)
    valley = 1.0 - np.exp(-((xx - yy) ** 2) / VALLEY_SIZE)
    terrain = 0.7 * hills + 0.3 * valley
    terrain = (terrain - terrain.min()) / (terrain.max() - terrain.min())
    mask = terrain > 0.01
    terraced = terrain.copy()
    terraced[mask] = np.round(terrain[mask] * TERRACE_STEPS) / TERRACE_STEPS
    final = 0.75 * terraced + 0.25 * terrain

elif TERRAIN_TYPE == "Flat":
    base = fbm(size, octaves=3, persistence=0.3)
    noise = fbm(size, octaves=6, persistence=0.4)
    valley = 1.0 - np.exp(-((xx - yy) ** 2) / VALLEY_SIZE)
    final = 0.6 * base + 0.2 * noise + 0.2 * valley

elif TERRAIN_TYPE == "Hills":
    final = MULTIPLIER * fbm(size, octaves=8, persistence=0.6)

else:
    raise ValueError(f"Unknown TERRAIN_TYPE '{TERRAIN_TYPE}'. Choose from: Terraced, Flat, Hills")

final = (final - final.min()) / (final.max() - final.min())

# Export the Image into Heightmap
img = Image.fromarray((final * 65535).astype(np.uint16), mode="I;16")

filename = "高度图.png"
img.save(filename)
print(f"New heightmap has been saved to {filename}")
