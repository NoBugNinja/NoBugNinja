import os
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions - Window fills canvas completely with crisp 3px neo-brutalist border
WIDTH = 840
HEIGHT = 410

# Color Palette
COLOR_TERMINAL_BG = (15, 17, 23)  # Sleek dark graphite
COLOR_INK_BLACK = (18, 18, 18)    # #121212
COLOR_YELLOW = (253, 224, 71)     # #fde047
COLOR_PINK = (255, 144, 232)      # #ff90e8
COLOR_BLUE = (59, 130, 246)       # #3b82f6
COLOR_GREEN = (74, 222, 128)      # #4ade80
COLOR_PURPLE = (167, 139, 250)    # #a78bfa
COLOR_CORAL = (251, 113, 133)     # #fb7185
COLOR_WHITE = (255, 255, 255)
COLOR_MUTED_GRAY = (156, 163, 175)# Gray 400
COLOR_PANEL_BG = (22, 24, 31)     # Inner panel
COLOR_STATUS_BG = (18, 20, 26)

# Fonts
FONT_MONO_BOLD = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 14)
FONT_MONO_SMALL = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 11)
FONT_MONO_TITLE = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 13)
FONT_MONO_BOT = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 15)
FONT_MONO_BIG = ImageFont.truetype("C:/Windows/Fonts/consolab.ttf", 18)

STAGES = [
    {
        "id": "01",
        "stage_title": "01 // PROBLEM HUNT",
        "badge_color": COLOR_YELLOW,
        "badge_text_color": COLOR_INK_BLACK,
        "bot_face": "SCANNING",
        "bot_quote": "\"Wait... why is this",
        "bot_quote_2": "still done manually?\"",
        "cmd": "$ nobugninja --scan-real-pain",
        "lines": [
            ("> Scanning campus & communities for friction...", COLOR_MUTED_GRAY),
            ("> DETECTED: IT Dept lacks automated CP tracking.", COLOR_YELLOW),
            ("> Thesis: Find a real problem -> turn it to software.", COLOR_WHITE),
            ("> Target: LeetBoard Analytics Platform.", COLOR_GREEN),
        ],
        "progress": "[===>-------] 20%",
        "footer_status": "PROBLEM HUNT",
    },
    {
        "id": "02",
        "stage_title": "02 // ARCHITECT",
        "badge_color": COLOR_PURPLE,
        "badge_text_color": COLOR_INK_BLACK,
        "bot_face": "ARCHITECT",
        "bot_quote": "\"Decoupled services &",
        "bot_quote_2": "clean data schemas.\"",
        "cmd": "$ architect --stack=next16,supabase",
        "lines": [
            ("> Modeling normalized PostgreSQL schema in Supabase", COLOR_MUTED_GRAY),
            ("> LeetCode GraphQL automated ingestion pipeline", COLOR_PURPLE),
            ("> Server-Sent Events (SSE) streaming configured", COLOR_WHITE),
            ("> System architecture blueprint locked in.", COLOR_GREEN),
        ],
        "progress": "[=====>-----] 40%",
        "footer_status": "ARCHITECTING",
    },
    {
        "id": "03",
        "stage_title": "03 // BUILD MODE",
        "badge_color": COLOR_PINK,
        "badge_text_color": COLOR_INK_BLACK,
        "bot_face": "BUILDING",
        "bot_quote": "\"Headphones on.",
        "bot_quote_2": "1,420 lines committed.\"",
        "cmd": "$ git commit -m 'feat: fullstack core'",
        "lines": [
            ("> Next.js App Router + TypeScript + Tailwind CSS", COLOR_PINK),
            ("> Automated daily cron ingestion engine active", COLOR_MUTED_GRAY),
            ("> Interactive Recharts comparison dashboards", COLOR_WHITE),
            ("> 02:40 AM code session. Coffee level: optimal.", COLOR_YELLOW),
        ],
        "progress": "[=======>---] 60%",
        "footer_status": "BUILDING",
    },
    {
        "id": "04",
        "stage_title": "04 // IT BROKE!",
        "badge_color": COLOR_CORAL,
        "badge_text_color": COLOR_INK_BLACK,
        "bot_face": "BROKE",
        "bot_quote": "\"Good! That means",
        "bot_quote_2": "we're learning.\"",
        "cmd": "$ npm test --strict",
        "lines": [
            ("! FAIL: Rate limit hit on external GraphQL API (429)", COLOR_CORAL),
            ("! Edge memory threshold exceeded during heavy sync", COLOR_CORAL),
            ("> Philosophy: Break it -> Learn -> Improve.", COLOR_YELLOW),
            ("> Isolating failure points & refactoring...", COLOR_WHITE),
        ],
        "progress": "[========>--] 70%",
        "footer_status": "BREAK & LEARN",
    },
    {
        "id": "05",
        "stage_title": "05 // DEBUG & REFINE",
        "badge_color": COLOR_BLUE,
        "badge_text_color": COLOR_WHITE,
        "bot_face": "DEBUG",
        "bot_quote": "\"Tracing root cause...",
        "bot_quote_2": "Zero bugs tolerated.\"",
        "cmd": "$ debug --trace-root-cause --tune",
        "lines": [
            ("> Added exponential backoff & token bucket queue", COLOR_MUTED_GRAY),
            ("> Optimized DB queries: latency 420ms -> 38ms", COLOR_BLUE),
            ("> Re-running test suite across all edge cases...", COLOR_WHITE),
            ("> PASS: 48/48 tests passing. Resilient.", COLOR_GREEN),
        ],
        "progress": "[==========>-] 90%",
        "footer_status": "HARDENED",
    },
    {
        "id": "06",
        "stage_title": "06 // SHIPPED & ADOPTED",
        "badge_color": COLOR_GREEN,
        "badge_text_color": COLOR_INK_BLACK,
        "bot_face": "SHIPPED",
        "bot_quote": "\"DEPLOYED TO PROD!",
        "bot_quote_2": "Software that works.\"",
        "cmd": "$ deploy --env=production --cloud=aws",
        "lines": [
            ("> Deployed: Vercel CDN + Supabase + AWS S3 / R2", COLOR_GREEN),
            ("> ADOPTED: Officially used by SVCE IT Department!", COLOR_YELLOW),
            ("> Real student ratings tracked in real-time.", COLOR_WHITE),
            ("> RESULT: BUILDING SOFTWARE THAT WORKS.", COLOR_PINK),
        ],
        "progress": "[===========] 100%",
        "footer_status": "PROD ADOPTED",
    },
]

def draw_bot(draw, x, y, bot_face, color_accent):
    box_w, box_h = 230, 160
    draw.rectangle([x, y, x + box_w, y + box_h], fill=COLOR_PANEL_BG, outline=COLOR_INK_BLACK, width=2)
    draw.rectangle([x, y, x + box_w, y + 25], fill=color_accent, outline=COLOR_INK_BLACK, width=2)
    draw.text((x + 10, y + 6), "NOBUGNINJA // BOT v2.6", font=FONT_MONO_SMALL, fill=COLOR_INK_BLACK)
    
    # Antenna
    antenna_x = x + box_w // 2
    draw.line([antenna_x, y + 25, antenna_x, y + 40], fill=color_accent, width=2)
    draw.ellipse([antenna_x - 4, y + 36, antenna_x + 4, y + 44], fill=COLOR_YELLOW, outline=COLOR_INK_BLACK, width=1)
    
    # Face Screen Box
    screen_x = x + 25
    screen_y = y + 48
    screen_w = box_w - 50
    screen_h = 72
    draw.rectangle([screen_x, screen_y, screen_x + screen_w, screen_y + screen_h], fill=(10, 11, 15), outline=color_accent, width=2)
    
    # Face Expressions
    if bot_face == "SCANNING":
        draw.text((screen_x + 28, screen_y + 14), "[ •   • ]", font=FONT_MONO_BIG, fill=COLOR_YELLOW)
        draw.text((screen_x + 55, screen_y + 42), "=====", font=FONT_MONO_BOLD, fill=COLOR_MUTED_GRAY)
    elif bot_face == "ARCHITECT":
        draw.text((screen_x + 28, screen_y + 14), "[ *   * ]", font=FONT_MONO_BIG, fill=COLOR_PURPLE)
        draw.text((screen_x + 58, screen_y + 42), "\\___/", font=FONT_MONO_BOLD, fill=COLOR_PURPLE)
    elif bot_face == "BUILDING":
        draw.text((screen_x + 22, screen_y + 14), "[#]═[#]", font=FONT_MONO_BIG, fill=COLOR_PINK)
        draw.text((screen_x + 58, screen_y + 42), "|===|", font=FONT_MONO_BOLD, fill=COLOR_GREEN)
    elif bot_face == "BROKE":
        draw.text((screen_x + 28, screen_y + 14), "[ x   x ]", font=FONT_MONO_BIG, fill=COLOR_CORAL)
        draw.text((screen_x + 56, screen_y + 42), "~~~~~", font=FONT_MONO_BOLD, fill=COLOR_CORAL)
    elif bot_face == "DEBUG":
        draw.text((screen_x + 28, screen_y + 14), "[ -   - ]", font=FONT_MONO_BIG, fill=COLOR_BLUE)
        draw.text((screen_x + 58, screen_y + 42), "-===-", font=FONT_MONO_BOLD, fill=COLOR_WHITE)
    elif bot_face == "SHIPPED":
        draw.text((screen_x + 28, screen_y + 14), "[ ^   ^ ]", font=FONT_MONO_BIG, fill=COLOR_GREEN)
        draw.text((screen_x + 58, screen_y + 42), "\\___/", font=FONT_MONO_BIG, fill=COLOR_GREEN)
        
    # Energy / Mood strip
    draw.rectangle([x + 8, y + 130, x + box_w - 8, y + 150], fill=(14, 15, 20), outline=COLOR_INK_BLACK, width=1)
    status_tag = f"STATE: {bot_face}"
    draw.text((x + 14, y + 134), status_tag, font=FONT_MONO_SMALL, fill=color_accent)
    draw.text((x + 138, y + 134), "ENERGY 100%", font=FONT_MONO_SMALL, fill=COLOR_GREEN)

def render_frame(stage, cursor_blink=True):
    img = Image.new("RGB", (WIDTH, HEIGHT), COLOR_TERMINAL_BG)
    draw = ImageDraw.Draw(img)
    
    # Outer Border (Solid 3px Neo-Brutalist Black Outline)
    draw.rectangle([0, 0, WIDTH - 1, HEIGHT - 1], outline=COLOR_INK_BLACK, width=3)
    
    # Titlebar (Yellow #fde047)
    TITLEBAR_H = 38
    draw.rectangle([0, 0, WIDTH - 1, TITLEBAR_H], fill=COLOR_YELLOW, outline=COLOR_INK_BLACK, width=3)
    
    # Window Buttons (Circles with 1px border)
    draw.ellipse([14, 11, 26, 23], fill=COLOR_CORAL, outline=COLOR_INK_BLACK, width=2)
    draw.ellipse([34, 11, 46, 23], fill=COLOR_PURPLE, outline=COLOR_INK_BLACK, width=2)
    draw.ellipse([54, 11, 66, 23], fill=COLOR_GREEN, outline=COLOR_INK_BLACK, width=2)
    
    # Titlebar text
    draw.text((80, 11), "shafiq.dev ~ nobugninja@builder-v2.6", font=FONT_MONO_TITLE, fill=COLOR_INK_BLACK)
    
    # Right Badge in Titlebar
    pill_w = 195
    pill_x = WIDTH - pill_w - 14
    pill_y = 7
    draw.rectangle([pill_x, pill_y, pill_x + pill_w, pill_y + 24], fill=stage["badge_color"], outline=COLOR_INK_BLACK, width=2)
    draw.text((pill_x + 10, pill_y + 5), stage["stage_title"], font=FONT_MONO_SMALL, fill=stage["badge_text_color"])
    
    # Work Area: Left Side (Bot Pod)
    bot_x = 18
    bot_y = 50
    draw_bot(draw, bot_x, bot_y, stage["bot_face"], stage["badge_color"])
    
    # Quote bubble below bot
    quote_y = bot_y + 172
    draw.rectangle([bot_x, quote_y, bot_x + 230, quote_y + 68], fill=COLOR_PANEL_BG, outline=COLOR_INK_BLACK, width=2)
    draw.text((bot_x + 10, quote_y + 8), stage['bot_quote'], font=FONT_MONO_SMALL, fill=COLOR_WHITE)
    draw.text((bot_x + 10, quote_y + 26), f"  {stage['bot_quote_2']}", font=FONT_MONO_SMALL, fill=COLOR_YELLOW)
    draw.text((bot_x + 10, quote_y + 46), f"PROGRESS: {stage['progress']}", font=FONT_MONO_SMALL, fill=stage["badge_color"])
    
    # Work Area: Right Side (Terminal Output)
    term_x = 264
    term_y = 50
    term_w = WIDTH - term_x - 18
    term_h = 286
    draw.rectangle([term_x, term_y, term_x + term_w, term_y + term_h], fill=COLOR_PANEL_BG, outline=COLOR_INK_BLACK, width=2)
    
    # Terminal Subheader inside right pane
    draw.rectangle([term_x, term_y, term_x + term_w, term_y + 24], fill=(28, 30, 38), outline=COLOR_INK_BLACK, width=2)
    draw.text((term_x + 12, term_y + 5), "BASH // PRODUCT PIPELINE TELEMETRY", font=FONT_MONO_SMALL, fill=COLOR_MUTED_GRAY)
    
    # Active Command Prompt
    prompt_y = term_y + 32
    draw.text((term_x + 14, prompt_y), stage["cmd"], font=FONT_MONO_BOLD, fill=COLOR_GREEN)
    
    # Separator
    draw.line([term_x + 14, prompt_y + 20, term_x + term_w - 14, prompt_y + 20], fill=(42, 45, 56), width=1)
    
    # Terminal Log Lines
    line_y = prompt_y + 28
    for line_text, line_color in stage["lines"]:
        draw.text((term_x + 14, line_y), line_text, font=FONT_MONO_BOLD, fill=line_color)
        line_y += 24
        
    # Blinking cursor line
    cursor_str = "nobugninja@builder:~/build$ "
    draw.text((term_x + 14, line_y + 6), cursor_str, font=FONT_MONO_BOLD, fill=COLOR_PINK)
    cursor_x = term_x + 14 + int(draw.textlength(cursor_str, font=FONT_MONO_BOLD))
    if cursor_blink:
        draw.rectangle([cursor_x + 2, line_y + 6, cursor_x + 11, line_y + 20], fill=COLOR_GREEN)
        
    # Mini project tags inside terminal bottom
    tag_y = term_y + term_h - 44
    draw.line([term_x + 14, tag_y - 6, term_x + term_w - 14, tag_y - 6], fill=(42, 45, 56), width=1)
    draw.text((term_x + 14, tag_y), "BUILDS: LEETBOARD | QUIETDEMAND | SKILLSYNC | OPPORTUNITYOS", font=FONT_MONO_SMALL, fill=COLOR_MUTED_GRAY)
    draw.text((term_x + 14, tag_y + 16), "STACK:  NEXT.JS 16 * TYPESCRIPT * SUPABASE * AWS S3 * PLAYWRIGHT", font=FONT_MONO_SMALL, fill=COLOR_MUTED_GRAY)
    
    # Bottom Status Bar (Full Width across bottom of window)
    STATUSBAR_Y = HEIGHT - 34
    draw.rectangle([0, STATUSBAR_Y, WIDTH - 1, HEIGHT - 1], fill=COLOR_STATUS_BG, outline=COLOR_INK_BLACK, width=2)
    
    # Status bar contents - beautifully spaced out
    draw.ellipse([16, STATUSBAR_Y + 11, 24, STATUSBAR_Y + 19], fill=COLOR_GREEN)
    draw.text((30, STATUSBAR_Y + 8), "FULL-STACK • AI • CLOUD", font=FONT_MONO_SMALL, fill=COLOR_WHITE)
    draw.text((215, STATUSBAR_Y + 8), "│", font=FONT_MONO_SMALL, fill=COLOR_MUTED_GRAY)
    draw.text((228, STATUSBAR_Y + 8), "BUILDING SOFTWARE THAT WORKS.", font=FONT_MONO_SMALL, fill=COLOR_YELLOW)
    draw.text((475, STATUSBAR_Y + 8), "│", font=FONT_MONO_SMALL, fill=COLOR_MUTED_GRAY)
    draw.text((490, STATUSBAR_Y + 8), f"STATUS: {stage['footer_status']}", font=FONT_MONO_SMALL, fill=stage["badge_color"])
    draw.text((670, STATUSBAR_Y + 8), "│", font=FONT_MONO_SMALL, fill=COLOR_MUTED_GRAY)
    draw.text((685, STATUSBAR_Y + 8), "ONLINE // LIVE", font=FONT_MONO_SMALL, fill=COLOR_MUTED_GRAY)

    return img

frames = []
durations = []

for stage in STAGES:
    f1 = render_frame(stage, cursor_blink=True)
    frames.append(f1)
    durations.append(1200)
    
    f2 = render_frame(stage, cursor_blink=False)
    frames.append(f2)
    durations.append(600)

output_path = "assets/hero-terminal.gif"
frames[0].save(
    output_path,
    save_all=True,
    append_images=frames[1:],
    duration=durations,
    loop=0,
    optimize=True
)

file_size = os.path.getsize(output_path)
print(f"Generated {output_path} successfully!")
print(f"Total frames: {len(frames)}, File size: {file_size / 1024:.1f} KB")
