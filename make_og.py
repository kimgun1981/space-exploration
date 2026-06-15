from PIL import Image, ImageDraw, ImageFont
import random, math

W, H = 1200, 630
BG = (11, 16, 38)
INK = (234, 242, 255)
SKY = (127, 216, 245)
SUN = (255, 209, 102)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img, "RGBA")

random.seed(7)
for _ in range(220):
    x, y = random.randint(0, W), random.randint(0, H)
    r = random.choice([1, 1, 1, 2, 2, 3])
    a = random.randint(140, 255)
    tint = random.choice([(255,255,255,a), (207,228,255,a), (255,233,201,a)])
    d.ellipse([x-r, y-r, x+r, y+r], fill=tint)

def planet(cx, cy, r, color, glow=True, ring=False):
    if glow:
        for i in range(40, 0, -1):
            alpha = int(8 * (i / 40))
            d.ellipse([cx-r-i*2, cy-r-i*2, cx+r+i*2, cy+r+i*2],
                      fill=(color[0], color[1], color[2], alpha))
    d.ellipse([cx-r, cy-r, cx+r, cy+r], fill=color)
    if ring:
        for off in range(-3, 4):
            d.ellipse([cx-int(r*2.1), cy-int(r*0.45)+off,
                       cx+int(r*2.1), cy+int(r*0.45)+off],
                      outline=(217, 199, 154, 180), width=1)

planet(1040, 470, 75, SUN, glow=True)
planet(720, 180, 15, (184, 168, 144), glow=False)
planet(820, 280, 22, (240, 201, 135), glow=False)
planet(760, 420, 28, (79, 157, 247), glow=False)
planet(910, 130, 18, (224, 107, 74), glow=False)
planet(680, 540, 40, (217, 160, 102), glow=False)
planet(960, 320, 32, (232, 213, 163), glow=False, ring=True)

KOR_BOLD = "/System/Library/Fonts/AppleSDGothicNeo.ttc"
try:
    title = ImageFont.truetype(KOR_BOLD, 96, index=8)
except Exception:
    title = ImageFont.truetype(KOR_BOLD, 96)
try:
    sub = ImageFont.truetype(KOR_BOLD, 38, index=2)
except Exception:
    sub = ImageFont.truetype(KOR_BOLD, 38)
small = ImageFont.truetype(KOR_BOLD, 26)

title_text = "우주 탐험"
sub_text = "아이들과 함께 보는 태양계"
tag_text = "행성을 누르면 한국어로 알려줘요"

tx, ty = 100, 100
for dx, dy in [(0,3),(3,0)]:
    d.text((tx+dx, ty+dy), title_text, font=title, fill=(0,0,0,120))
d.text((tx, ty), title_text, font=title, fill=INK)

d.text((tx, ty + 130), sub_text, font=sub, fill=SUN)

bx0, by0 = tx, ty + 200
pad_x, pad_y = 18, 10
bbox = d.textbbox((bx0+pad_x, by0+pad_y), tag_text, font=small)
d.rounded_rectangle([bx0, by0, bbox[2]+pad_x, bbox[3]+pad_y],
                    radius=22, fill=(127, 216, 245, 36),
                    outline=(127, 216, 245, 120), width=2)
d.text((bx0+pad_x, by0+pad_y), tag_text, font=small, fill=SKY)

out = "/Users/kimgun/Desktop/space probe/og-image.png"
img.save(out, "PNG", optimize=True)
print("saved", out, img.size)
