import random
import math

width = 1200
height = 260
num_nodes = 48

random.seed(42)
nodes = []
for i in range(num_nodes):
    x = random.uniform(30, width - 30)
    y = random.uniform(25, height - 25)
    r = random.uniform(1.8, 3.8)
    opacity = random.uniform(0.35, 0.9)
    color = random.choice(['#00F5D4', '#7928CA', '#00BBF9', '#F72585', '#4CC9F0'])
    dur = random.uniform(2.5, 5.5)
    nodes.append((x, y, r, opacity, color, dur))

# Generate edges between nearby nodes
edges = []
max_dist = 135
for i in range(len(nodes)):
    for j in range(i + 1, len(nodes)):
        x1, y1 = nodes[i][0], nodes[i][1]
        x2, y2 = nodes[j][0], nodes[j][1]
        d = math.hypot(x1 - x2, y1 - y2)
        if d < max_dist:
            stroke_op = (1.0 - d / max_dist) * 0.38
            edges.append((x1, y1, x2, y2, stroke_op))

svg_parts = [
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="100%" height="{height}">',
    '  <defs>',
    '    <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">',
    '      <stop offset="0%" stop-color="#050811" />',
    '      <stop offset="50%" stop-color="#0A0F1D" />',
    '      <stop offset="100%" stop-color="#0D1117" />',
    '    </linearGradient>',
    '    <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">',
    '      <stop offset="0%" stop-color="#00F5D4" />',
    '      <stop offset="50%" stop-color="#7000FF" />',
    '      <stop offset="100%" stop-color="#FF007A" />',
    '    </linearGradient>',
    '    <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">',
    '      <feGaussianBlur stdDeviation="5" result="blur" />',
    '      <feMerge>',
    '        <feMergeNode in="blur" />',
    '        <feMergeNode in="SourceGraphic" />',
    '      </feMerge>',
    '    </filter>',
    '    <radialGradient id="nebula" cx="50%" cy="50%" r="50%">',
    '      <stop offset="0%" stop-color="rgba(112, 0, 255, 0.18)" />',
    '      <stop offset="100%" stop-color="rgba(0, 0, 0, 0)" />',
    '    </radialGradient>',
    '  </defs>',
    '  <rect width="100%" height="100%" fill="url(#bg-grad)" rx="14" />',
    f'  <circle cx="{width//2}" cy="{height//2}" r="320" fill="url(#nebula)" />',
    '  <!-- Perspective Matrix Grid -->',
    '  <g stroke="rgba(0, 245, 212, 0.04)" stroke-width="1">'
]

for x in range(0, width, 40):
    svg_parts.append(f'    <line x1="{x}" y1="0" x2="{x}" y2="{height}" />')
for y in range(0, height, 40):
    svg_parts.append(f'    <line x1="0" y1="{y}" x2="{width}" y2="{y}" />')

svg_parts.append('  </g>')
svg_parts.append('  <!-- Constellation Connections -->')
svg_parts.append('  <g stroke="#00F5D4">')

for x1, y1, x2, y2, op in edges:
    svg_parts.append(f'    <line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke-opacity="{op:.3f}" stroke-width="1.2" />')

svg_parts.append('  </g>')
svg_parts.append('  <!-- Constellation Interactive Pulsing Nodes -->')

for i, (x, y, r, op, col, dur) in enumerate(nodes):
    svg_parts.append(f'  <circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{col}" opacity="{op:.2f}">')
    svg_parts.append(f'    <animate attributeName="r" values="{r:.1f};{r*1.8:.1f};{r:.1f}" dur="{dur:.1f}s" repeatCount="indefinite" />')
    svg_parts.append(f'    <animate attributeName="opacity" values="{op:.2f};{min(1.0, op*1.5):.2f};{op:.2f}" dur="{dur:.1f}s" repeatCount="indefinite" />')
    svg_parts.append('  </circle>')

svg_parts.extend([
    '  <!-- Cyberpunk Branding & Typography -->',
    '  <g text-anchor="middle" font-family="-apple-system, BlinkMacSystemFont, \'Segoe UI\', Roboto, \'Helvetica Neue\', sans-serif">',
    f'    <text x="{width//2}" y="105" font-size="46" font-weight="900" fill="url(#text-grad)" filter="url(#glow)" letter-spacing="3">ROUSHAN SINGH</text>',
    f'    <text x="{width//2}" y="105" font-size="46" font-weight="900" fill="#FFFFFF" letter-spacing="3">ROUSHAN SINGH</text>',
    f'    <rect x="{width//2 - 280}" y="130" width="560" height="32" rx="16" fill="rgba(0, 245, 212, 0.08)" stroke="rgba(0, 245, 212, 0.3)" stroke-width="1" />',
    f'    <text x="{width//2}" y="151" font-size="13" font-weight="700" fill="#00F5D4" letter-spacing="3.2">EMBODIED AI • AUTONOMOUS ROBOTICS • DEEP LEARNING</text>',
    f'    <text x="{width//2}" y="196" font-size="13" font-weight="500" fill="#8B949E" letter-spacing="1.5">IIT MADRAS BS DATA SCIENCE &amp; APPLICATIONS • MUMBAI, INDIA</text>',
    '  </g>',
    '</svg>'
])

full_svg = '\n'.join(svg_parts)

with open('C:/AI_Engineering_Projects/RoushanSingh01-profile/banner.svg', 'w', encoding='utf-8') as f:
    f.write(full_svg)

print("Generated banner.svg successfully! Size:", len(full_svg))
