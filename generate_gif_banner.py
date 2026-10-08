import math
import random
from PIL import Image, ImageDraw, ImageFont

width = 1200
height = 280
num_frames = 50
num_particles = 70

random.seed(2026)

# Colors matching the portfolio: cyan, electric violet, sky blue, neon mint
colors_rgb = [
    (0, 245, 255),
    (139, 92, 246),
    (168, 85, 247),
    (56, 189, 248),
    (0, 255, 170),
    (244, 63, 94)
]

particles = []
for _ in range(num_particles):
    particles.append({
        'x': random.uniform(15, width - 15),
        'y': random.uniform(15, height - 15),
        'vx': random.uniform(-1.5, 1.5),
        'vy': random.uniform(-1.1, 1.1),
        'radius': random.uniform(2.0, 4.2),
        'color': random.choice(colors_rgb)
    })

frames = []

for frame_idx in range(num_frames):
    img = Image.new('RGB', (width, height), color=(6, 9, 18))
    draw = ImageDraw.Draw(img, 'RGBA')

    # 1. Perspective Cyber Grid
    grid_color = (0, 245, 255, 7)
    for x in range(0, width, 40):
        draw.line([(x, 0), (x, height)], fill=grid_color, width=1)
    for y in range(0, height, 40):
        draw.line([(0, y), (width, y)], fill=grid_color, width=1)

    # 2. Update particle positions
    for p in particles:
        p['x'] += p['vx']
        p['y'] += p['vy']
        if p['x'] <= 12 or p['x'] >= width - 12:
            p['vx'] *= -1
        if p['y'] <= 12 or p['y'] >= height - 12:
            p['vy'] *= -1

    # 3. Draw Constellation Network Connections
    max_dist = 125.0
    for i in range(len(particles)):
        for j in range(i + 1, len(particles)):
            p1 = particles[i]
            p2 = particles[j]
            dist = math.hypot(p1['x'] - p2['x'], p1['y'] - p2['y'])
            if dist < max_dist:
                alpha = int((1.0 - dist / max_dist) * 95)
                draw.line([(p1['x'], p1['y']), (p2['x'], p2['y'])], fill=(0, 245, 255, alpha), width=1)

    # 4. Draw Particles (Nodes)
    for p in particles:
        r = p['radius'] + 0.5 * math.sin(frame_idx * 0.18 + p['x'])
        c = p['color']
        # Outer soft glow halo
        draw.ellipse([p['x'] - r - 3, p['y'] - r - 3, p['x'] + r + 3, p['y'] + r + 3], fill=(c[0], c[1], c[2], 40))
        # Solid core
        draw.ellipse([p['x'] - r, p['y'] - r, p['x'] + r, p['y'] + r], fill=(c[0], c[1], c[2], 240))

    # 5. Cyberpunk HUD Header Center Card
    box_w, box_h = 760, 160
    bx1 = (width - box_w) // 2
    by1 = (height - box_h) // 2
    bx2 = bx1 + box_w
    by2 = by1 + box_h

    # Semi-transparent glassmorphic plate (particles pass behind and around it!)
    draw.rounded_rectangle([bx1, by1, bx2, by2], radius=18, fill=(10, 15, 29, 215), outline=(0, 245, 212, 90), width=1)

    # Corner cyber accents
    accent_len = 14
    draw.line([(bx1, by1 + accent_len), (bx1, by1), (bx1 + accent_len, by1)], fill=(0, 245, 212, 220), width=2)
    draw.line([(bx2 - accent_len, by1), (bx2, by1), (bx2, by1 + accent_len)], fill=(0, 245, 212, 220), width=2)
    draw.line([(bx1, by2 - accent_len), (bx1, by2), (bx1 + accent_len, by2)], fill=(0, 245, 212, 220), width=2)
    draw.line([(bx2 - accent_len, by2), (bx2, by2), (bx2, by2 - accent_len)], fill=(0, 245, 212, 220), width=2)

    # Typography
    try:
        font_title = ImageFont.truetype("arialbd.ttf", 46)
        font_sub = ImageFont.truetype("arialbd.ttf", 14)
        font_affil = ImageFont.truetype("arial.ttf", 13)
    except:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
        font_affil = ImageFont.load_default()

    # Title
    title_text = "ROUSHAN SINGH"
    bbox_title = draw.textbbox((0, 0), title_text, font=font_title)
    tw = bbox_title[2] - bbox_title[0]
    draw.text(((width - tw) // 2, by1 + 22), title_text, fill=(255, 255, 255), font=font_title)

    # Subtitle Pill
    pill_w, pill_h = 630, 28
    px1 = (width - pill_w) // 2
    py1 = by1 + 84
    draw.rounded_rectangle([px1, py1, px1 + pill_w, py1 + pill_h], radius=14, fill=(0, 245, 212, 22), outline=(0, 245, 212, 100), width=1)

    sub_text = "EMBODIED AI  •  AUTONOMOUS ROBOTICS  •  DEEP LEARNING SYSTEMS"
    bbox_sub = draw.textbbox((0, 0), sub_text, font=font_sub)
    sw = bbox_sub[2] - bbox_sub[0]
    draw.text(((width - sw) // 2, py1 + 6), sub_text, fill=(0, 245, 212), font=font_sub)

    # Affiliation
    affil_text = "IIT MADRAS BS DATA SCIENCE & APPLICATIONS  •  MUMBAI, INDIA"
    bbox_aff = draw.textbbox((0, 0), affil_text, font=font_affil)
    aw = bbox_aff[2] - bbox_aff[0]
    draw.text(((width - aw) // 2, py1 + 38), affil_text, fill=(156, 163, 175), font=font_affil)

    frames.append(img.convert('P', palette=Image.ADAPTIVE))

# Save
out_path = 'C:/AI_Engineering_Projects/RoushanSingh01-profile/banner.gif'
frames[0].save(
    out_path,
    save_all=True,
    append_images=frames[1:],
    optimize=True,
    duration=50,
    loop=0
)

print(f"Generated high-def banner.gif successfully! Total frames: {len(frames)}")
