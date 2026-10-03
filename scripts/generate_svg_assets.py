import os

def create_system_status_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 120" width="100%" height="auto" style="max-width: 920px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Courier New', monospace;">
  <defs>
    <filter id="tele-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="4" dy="4" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <g transform="translate(6, 6)">
    <!-- Shadow & Body -->
    <rect x="0" y="0" width="904" height="104" rx="8" fill="#121216" stroke="#121212" stroke-width="3" filter="url(#tele-shadow)"/>
    
    <!-- Top Bar -->
    <rect x="0" y="0" width="904" height="28" rx="6" fill="#fde047" stroke="#121212" stroke-width="3"/>
    <circle cx="16" cy="14" r="5" fill="#fb7185" stroke="#121212" stroke-width="1.5"/>
    <circle cx="32" cy="14" r="5" fill="#a78bfa" stroke="#121212" stroke-width="1.5"/>
    <circle cx="48" cy="14" r="5" fill="#4ade80" stroke="#121212" stroke-width="1.5"/>
    <text x="68" y="19" font-size="11" font-weight="900" fill="#121212" letter-spacing="1">SYSTEM TELEMETRY // MOHAMMED SHAFIQ S (NoBugNinja)</text>
    <rect x="740" y="4" width="150" height="20" rx="4" fill="#121212"/>
    <circle cx="754" cy="14" r="3.5" fill="#4ade80"/>
    <text x="764" y="18" font-size="10" font-weight="800" fill="#4ade80">● ONLINE // ACTIVE</text>

    <!-- Content 3 Columns -->
    <g transform="translate(18, 42)">
      <rect x="0" y="0" width="270" height="52" rx="4" fill="#1e1f26" stroke="#374151" stroke-width="1.5"/>
      <text x="12" y="20" font-size="10" font-weight="800" fill="#fde047" letter-spacing="0.5">CURRENT STATUS</text>
      <text x="12" y="38" font-size="12" font-weight="700" fill="#ffffff">Available for 2026 Roles</text>
      <circle cx="250" cy="26" r="4" fill="#4ade80"/>
    </g>

    <g transform="translate(304, 42)">
      <rect x="0" y="0" width="280" height="52" rx="4" fill="#1e1f26" stroke="#374151" stroke-width="1.5"/>
      <text x="12" y="20" font-size="10" font-weight="800" fill="#ff90e8" letter-spacing="0.5">ACTIVE LEARNING TRACK</text>
      <text x="12" y="38" font-size="12" font-weight="700" fill="#ffffff">AWS Solutions Architect Cert</text>
      <circle cx="260" cy="26" r="4" fill="#ff90e8"/>
    </g>

    <g transform="translate(600, 42)">
      <rect x="0" y="0" width="286" height="52" rx="4" fill="#1e1f26" stroke="#374151" stroke-width="1.5"/>
      <text x="12" y="20" font-size="10" font-weight="800" fill="#4ade80" letter-spacing="0.5">KEY ADOPTION MILESTONE</text>
      <text x="12" y="38" font-size="12" font-weight="700" fill="#ffffff">LeetBoard (Faculty &amp; Dept Adopted)</text>
      <circle cx="266" cy="26" r="4" fill="#fde047"/>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_exploring_cards_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="auto" style="max-width: 920px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="card-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3.5" dy="3.5" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <!-- Card 1: Full-Stack Products -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="212" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#card-shadow)"/>
    <rect x="0" y="0" width="212" height="32" rx="6" fill="#fde047" stroke="#121212" stroke-width="3"/>
    <text x="12" y="21" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">01 // FULL-STACK</text>
    <circle cx="196" cy="16" r="4" fill="#121212"/>
    <text x="14" y="56" font-size="13.5" font-weight="900" fill="#ffffff">PRODUCT BUILDER</text>
    <text x="14" y="76" font-size="11" font-weight="500" fill="#9ca3af">Building complete web products from idea to deployment.</text>
    <line x1="14" y1="102" x2="198" y2="102" stroke="#2d3139" stroke-width="1"/>
    <g transform="translate(14, 114)">
      <rect x="0" y="0" width="60" height="22" rx="4" fill="#232630" stroke="#fde047" stroke-width="1.5"/>
      <text x="7" y="15" font-size="9" font-weight="800" fill="#fde047">Next.js 16</text>
      <rect x="66" y="0" width="56" height="22" rx="4" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="73" y="15" font-size="9" font-weight="700" fill="#e5e7eb">React 19</text>
      <rect x="128" y="0" width="56" height="22" rx="4" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="139" y="15" font-size="9" font-weight="700" fill="#e5e7eb">Node.js</text>
    </g>
  </g>

  <!-- Card 2: Cloud Architecture -->
  <g transform="translate(237, 10)">
    <rect x="0" y="0" width="212" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#card-shadow)"/>
    <rect x="0" y="0" width="212" height="32" rx="6" fill="#a78bfa" stroke="#121212" stroke-width="3"/>
    <text x="12" y="21" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">02 // CLOUD INFRA</text>
    <circle cx="196" cy="16" r="4" fill="#121212"/>
    <text x="14" y="56" font-size="13.5" font-weight="900" fill="#ffffff">AWS SOLUTIONS</text>
    <text x="14" y="76" font-size="11" font-weight="500" fill="#9ca3af">Scalable cloud architectures, serverless, and AWS cert track.</text>
    <line x1="14" y1="102" x2="198" y2="102" stroke="#2d3139" stroke-width="1"/>
    <g transform="translate(14, 114)">
      <rect x="0" y="0" width="60" height="22" rx="4" fill="#232630" stroke="#a78bfa" stroke-width="1.5"/>
      <text x="9" y="15" font-size="9" font-weight="800" fill="#a78bfa">AWS S3</text>
      <rect x="66" y="0" width="56" height="22" rx="4" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="75" y="15" font-size="9" font-weight="700" fill="#e5e7eb">Lambda</text>
      <rect x="128" y="0" width="56" height="22" rx="4" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="143" y="15" font-size="9" font-weight="700" fill="#e5e7eb">R2</text>
    </g>
  </g>

  <!-- Card 3: AI Systems -->
  <g transform="translate(464, 10)">
    <rect x="0" y="0" width="212" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#card-shadow)"/>
    <rect x="0" y="0" width="212" height="32" rx="6" fill="#3b82f6" stroke="#121212" stroke-width="3"/>
    <text x="12" y="21" font-size="11" font-weight="900" fill="#ffffff" letter-spacing="0.5">03 // AI SYSTEMS</text>
    <circle cx="196" cy="16" r="4" fill="#ffffff"/>
    <text x="14" y="56" font-size="13.5" font-weight="900" fill="#ffffff">LLMS &amp; SCRAPERS</text>
    <text x="14" y="76" font-size="11" font-weight="500" fill="#9ca3af">Resilient data engines, schema enforcement, &amp; fast inference.</text>
    <line x1="14" y1="102" x2="198" y2="102" stroke="#2d3139" stroke-width="1"/>
    <g transform="translate(14, 114)">
      <rect x="0" y="0" width="60" height="22" rx="4" fill="#232630" stroke="#3b82f6" stroke-width="1.5"/>
      <text x="9" y="15" font-size="9" font-weight="800" fill="#3b82f6">Gemini</text>
      <rect x="66" y="0" width="56" height="22" rx="4" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="76" y="15" font-size="9" font-weight="700" fill="#e5e7eb">Groq</text>
      <rect x="128" y="0" width="64" height="22" rx="4" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="133" y="15" font-size="9" font-weight="700" fill="#e5e7eb">Playwright</text>
    </g>
  </g>

  <!-- Card 4: SaaS & Automation -->
  <g transform="translate(691, 10)">
    <rect x="0" y="0" width="218" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#card-shadow)"/>
    <rect x="0" y="0" width="218" height="32" rx="6" fill="#4ade80" stroke="#121212" stroke-width="3"/>
    <text x="12" y="21" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">04 // AUTOMATION</text>
    <circle cx="202" cy="16" r="4" fill="#121212"/>
    <text x="14" y="56" font-size="13.5" font-weight="900" fill="#ffffff">SAAS PIPELINES</text>
    <text x="14" y="76" font-size="11" font-weight="500" fill="#9ca3af">Autonomous workflows, background cron matchers, &amp; SSE streams.</text>
    <line x1="14" y1="102" x2="204" y2="102" stroke="#2d3139" stroke-width="1"/>
    <g transform="translate(14, 114)">
      <rect x="0" y="0" width="60" height="22" rx="4" fill="#232630" stroke="#4ade80" stroke-width="1.5"/>
      <text x="12" y="15" font-size="9" font-weight="800" fill="#4ade80">Supabase</text>
      <rect x="66" y="0" width="56" height="22" rx="4" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="79" y="15" font-size="9" font-weight="700" fill="#e5e7eb">SSE</text>
      <rect x="128" y="0" width="64" height="22" rx="4" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="135" y="15" font-size="9" font-weight="700" fill="#e5e7eb">GraphQL</text>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_how_i_build_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 180" width="100%" height="auto" style="max-width: 920px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="build-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3.5" dy="3.5" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <!-- Step 1: THINK -->
  <g transform="translate(10, 10)">
    <rect x="0" y="0" width="158" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#build-shadow)"/>
    <rect x="0" y="0" width="158" height="32" rx="6" fill="#fde047" stroke="#121212" stroke-width="3"/>
    <text x="10" y="21" font-size="11" font-weight="900" fill="#121212">01 // THINK</text>
    <text x="12" y="58" font-size="15" font-weight="900" fill="#ffffff">UNDERSTAND</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#fde047">THE PROBLEM</text>
    <line x1="12" y1="84" x2="146" y2="84" stroke="#2d3139" stroke-width="1"/>
    <text x="12" y="106" font-size="10.5" font-weight="500" fill="#9ca3af">Identify real friction</text>
    <text x="12" y="122" font-size="10.5" font-weight="500" fill="#9ca3af">and core user pain</text>
    <text x="12" y="138" font-size="10.5" font-weight="500" fill="#9ca3af">before touching code.</text>
  </g>

  <!-- Arrow 1 -->
  <g transform="translate(173, 75)">
    <circle cx="8" cy="8" r="12" fill="#121212"/>
    <path d="M4 8 L12 8 M9 5 L12 8 L9 11" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Step 2: DESIGN -->
  <g transform="translate(193, 10)">
    <rect x="0" y="0" width="158" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#build-shadow)"/>
    <rect x="0" y="0" width="158" height="32" rx="6" fill="#ff90e8" stroke="#121212" stroke-width="3"/>
    <text x="10" y="21" font-size="11" font-weight="900" fill="#121212">02 // DESIGN</text>
    <text x="12" y="58" font-size="15" font-weight="900" fill="#ffffff">ARCHITECT</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#ff90e8">THE SYSTEM</text>
    <line x1="12" y1="84" x2="146" y2="84" stroke="#2d3139" stroke-width="1"/>
    <text x="12" y="106" font-size="10.5" font-weight="500" fill="#9ca3af">Figure out the product</text>
    <text x="12" y="122" font-size="10.5" font-weight="500" fill="#9ca3af">flows, data schemas,</text>
    <text x="12" y="138" font-size="10.5" font-weight="500" fill="#9ca3af">and decoupled APIs.</text>
  </g>

  <!-- Arrow 2 -->
  <g transform="translate(356, 75)">
    <circle cx="8" cy="8" r="12" fill="#121212"/>
    <path d="M4 8 L12 8 M9 5 L12 8 L9 11" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Step 3: BUILD -->
  <g transform="translate(376, 10)">
    <rect x="0" y="0" width="158" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#build-shadow)"/>
    <rect x="0" y="0" width="158" height="32" rx="6" fill="#3b82f6" stroke="#121212" stroke-width="3"/>
    <text x="10" y="21" font-size="11" font-weight="900" fill="#ffffff">03 // BUILD</text>
    <text x="12" y="58" font-size="15" font-weight="900" fill="#ffffff">TURN IDEA</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#60a5fa">INTO SOFTWARE</text>
    <line x1="12" y1="84" x2="146" y2="84" stroke="#2d3139" stroke-width="1"/>
    <text x="12" y="106" font-size="10.5" font-weight="500" fill="#9ca3af">Ship clean, full-stack</text>
    <text x="12" y="122" font-size="10.5" font-weight="500" fill="#9ca3af">code with modern</text>
    <text x="12" y="138" font-size="10.5" font-weight="500" fill="#9ca3af">frameworks &amp; storage.</text>
  </g>

  <!-- Arrow 3 -->
  <g transform="translate(539, 75)">
    <circle cx="8" cy="8" r="12" fill="#121212"/>
    <path d="M4 8 L12 8 M9 5 L12 8 L9 11" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Step 4: BREAK -->
  <g transform="translate(559, 10)">
    <rect x="0" y="0" width="158" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#build-shadow)"/>
    <rect x="0" y="0" width="158" height="32" rx="6" fill="#fb7185" stroke="#121212" stroke-width="3"/>
    <text x="10" y="21" font-size="11" font-weight="900" fill="#121212">04 // BREAK</text>
    <text x="12" y="58" font-size="15" font-weight="900" fill="#ffffff">TEST LIMITS</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#fb7185">&amp; FIX ROOT CAUSE</text>
    <line x1="12" y1="84" x2="146" y2="84" stroke="#2d3139" stroke-width="1"/>
    <text x="12" y="106" font-size="10.5" font-weight="500" fill="#9ca3af">Push edge cases,</text>
    <text x="12" y="122" font-size="10.5" font-weight="500" fill="#9ca3af">find what fails, and</text>
    <text x="12" y="138" font-size="10.5" font-weight="500" fill="#9ca3af">harden against bugs.</text>
  </g>

  <!-- Arrow 4 -->
  <g transform="translate(722, 75)">
    <circle cx="8" cy="8" r="12" fill="#121212"/>
    <path d="M4 8 L12 8 M9 5 L12 8 L9 11" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Step 5: SHIP -->
  <g transform="translate(742, 10)">
    <rect x="0" y="0" width="168" height="155" rx="8" fill="#181920" stroke="#121212" stroke-width="3" filter="url(#build-shadow)"/>
    <rect x="0" y="0" width="168" height="32" rx="6" fill="#4ade80" stroke="#121212" stroke-width="3"/>
    <text x="10" y="21" font-size="11" font-weight="900" fill="#121212">05 // SHIP</text>
    <text x="12" y="58" font-size="15" font-weight="900" fill="#ffffff">DEPLOY TO</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#4ade80">REAL USERS</text>
    <line x1="12" y1="84" x2="156" y2="84" stroke="#2d3139" stroke-width="1"/>
    <text x="12" y="106" font-size="10.5" font-weight="500" fill="#9ca3af">Release to production,</text>
    <text x="12" y="122" font-size="10.5" font-weight="500" fill="#9ca3af">monitor performance,</text>
    <text x="12" y="138" font-size="10.5" font-weight="500" fill="#9ca3af">and iterate fast.</text>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_project_leetboard_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="auto" style="max-width: 440px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="p-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3" dy="3" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <g transform="translate(6, 6)">
    <rect x="0" y="0" width="424" height="204" rx="8" fill="#15171e" stroke="#121212" stroke-width="3" filter="url(#p-shadow)"/>
    <!-- Titlebar -->
    <rect x="0" y="0" width="424" height="30" rx="6" fill="#3b82f6" stroke="#121212" stroke-width="3"/>
    <circle cx="14" cy="15" r="4.5" fill="#fb7185" stroke="#121212" stroke-width="1"/>
    <circle cx="28" cy="15" r="4.5" fill="#fde047" stroke="#121212" stroke-width="1"/>
    <circle cx="42" cy="15" r="4.5" fill="#4ade80" stroke="#121212" stroke-width="1"/>
    <text x="60" y="20" font-size="11" font-weight="900" fill="#ffffff" letter-spacing="0.5">LEETBOARD // CP ANALYTICS</text>
    <rect x="325" y="5" width="88" height="20" rx="4" fill="#121212"/>
    <text x="333" y="19" font-size="9" font-weight="800" fill="#fde047">● DEPT ADOPTED</text>

    <!-- Mini UI Mockup inside card -->
    <g transform="translate(14, 42)">
      <rect x="0" y="0" width="396" height="88" rx="6" fill="#1c1e27" stroke="#2e3240" stroke-width="1.5"/>
      <!-- Metric pills -->
      <g transform="translate(10, 10)">
        <text x="0" y="12" font-size="9" font-weight="800" fill="#9ca3af">CONTEST RATING TRACKER</text>
        <text x="0" y="32" font-size="18" font-weight="900" fill="#60a5fa">1,942 <tspan font-size="11" fill="#4ade80">▲ +128</tspan></text>
        <path d="M 0 52 Q 25 45, 50 48 T 100 36 T 150 28 T 200 18" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
      </g>
      <!-- Leaderboard Mock snippet -->
      <g transform="translate(230, 8)">
        <rect x="0" y="0" width="156" height="20" rx="3" fill="#252834"/>
        <text x="8" y="14" font-size="9" font-weight="800" fill="#fde047">#1 @karthik_s</text>
        <text x="110" y="14" font-size="9" font-weight="700" fill="#9ca3af">2,140</text>
        <rect x="0" y="24" width="156" height="20" rx="3" fill="#252834"/>
        <text x="8" y="38" font-size="9" font-weight="800" fill="#e5e7eb">#2 @priya_m</text>
        <text x="110" y="38" font-size="9" font-weight="700" fill="#9ca3af">2,085</text>
        <rect x="0" y="48" width="156" height="20" rx="3" fill="#2a2d3d" stroke="#3b82f6" stroke-width="1"/>
        <text x="8" y="62" font-size="9" font-weight="800" fill="#60a5fa">#3 @shafiq (you)</text>
        <text x="110" y="62" font-size="9" font-weight="700" fill="#4ade80">1,942</text>
      </g>
    </g>

    <!-- Description & Stack -->
    <text x="14" y="150" font-size="11.5" font-weight="700" fill="#ffffff">Automated competitive programming analytics tracking daily contest metrics.</text>
    <g transform="translate(14, 166)">
      <rect x="0" y="0" width="56" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="6" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Next.js</text>
      <rect x="62" y="0" width="62" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="68" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Supabase</text>
      <rect x="130" y="0" width="58" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="136" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">GraphQL</text>
      <rect x="194" y="0" width="58" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="200" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Recharts</text>
      <rect x="315" y="0" width="95" height="20" rx="4" fill="#3b82f6" stroke="#121212" stroke-width="1.5"/>
      <text x="323" y="14" font-size="8.5" font-weight="900" fill="#ffffff">EXPLORE REPO ↗</text>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_project_quietdemand_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="auto" style="max-width: 440px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="p-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3" dy="3" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <g transform="translate(6, 6)">
    <rect x="0" y="0" width="424" height="204" rx="8" fill="#15171e" stroke="#121212" stroke-width="3" filter="url(#p-shadow)"/>
    <!-- Titlebar -->
    <rect x="0" y="0" width="424" height="30" rx="6" fill="#fb7185" stroke="#121212" stroke-width="3"/>
    <circle cx="14" cy="15" r="4.5" fill="#fde047" stroke="#121212" stroke-width="1"/>
    <circle cx="28" cy="15" r="4.5" fill="#3b82f6" stroke="#121212" stroke-width="1"/>
    <circle cx="42" cy="15" r="4.5" fill="#4ade80" stroke="#121212" stroke-width="1"/>
    <text x="60" y="20" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">QUIETDEMAND // STARTUP VALIDATION</text>
    <rect x="330" y="5" width="82" height="20" rx="4" fill="#121212"/>
    <text x="339" y="19" font-size="9" font-weight="800" fill="#4ade80">● SSE STREAM</text>

    <!-- Mini UI Mockup -->
    <g transform="translate(14, 42)">
      <rect x="0" y="0" width="396" height="88" rx="6" fill="#1c1e27" stroke="#2e3240" stroke-width="1.5"/>
      <g transform="translate(12, 10)">
        <text x="0" y="12" font-size="9" font-weight="800" fill="#fb7185">TARGET: r/SaaS • r/startups</text>
        <rect x="0" y="20" width="180" height="14" rx="3" fill="#282a36"/>
        <rect x="0" y="20" width="138" height="14" rx="3" fill="#fb7185"/>
        <text x="6" y="31" font-size="8.5" font-weight="900" fill="#121212">PAIN INTENSITY: 76% HIGH</text>
        <text x="0" y="54" font-size="9" font-weight="700" fill="#9ca3af">Scraped 340+ threads via Playwright</text>
        <text x="0" y="68" font-size="9" font-weight="700" fill="#4ade80">Gemini JSON: TAM $3.8M verified</text>
      </g>
      <g transform="translate(210, 10)">
        <rect x="0" y="0" width="176" height="66" rx="4" fill="#242735" stroke="#3d4255" stroke-width="1"/>
        <text x="10" y="18" font-size="9" font-weight="800" fill="#fde047">PURCHASE INTENT</text>
        <text x="10" y="38" font-size="16" font-weight="900" fill="#ffffff">84.2% <tspan font-size="10" fill="#4ade80">STRONG</tspan></text>
        <text x="10" y="54" font-size="8.5" font-weight="600" fill="#9ca3af">Streaming inference live...</text>
      </g>
    </g>

    <!-- Description & Stack -->
    <text x="14" y="150" font-size="11.5" font-weight="700" fill="#ffffff">Autonomous startup idea validation SaaS analyzing Reddit buyer signals.</text>
    <g transform="translate(14, 166)">
      <rect x="0" y="0" width="56" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="6" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Next.js</text>
      <rect x="62" y="0" width="68" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="68" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Playwright</text>
      <rect x="136" y="0" width="56" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="142" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Gemini</text>
      <rect x="198" y="0" width="46" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="204" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">SSE</text>
      <rect x="315" y="0" width="95" height="20" rx="4" fill="#fb7185" stroke="#121212" stroke-width="1.5"/>
      <text x="323" y="14" font-size="8.5" font-weight="900" fill="#121212">EXPLORE REPO ↗</text>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_project_skillsync_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="auto" style="max-width: 440px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="p-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3" dy="3" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <g transform="translate(6, 6)">
    <rect x="0" y="0" width="424" height="204" rx="8" fill="#15171e" stroke="#121212" stroke-width="3" filter="url(#p-shadow)"/>
    <!-- Titlebar -->
    <rect x="0" y="0" width="424" height="30" rx="6" fill="#fde047" stroke="#121212" stroke-width="3"/>
    <circle cx="14" cy="15" r="4.5" fill="#fb7185" stroke="#121212" stroke-width="1"/>
    <circle cx="28" cy="15" r="4.5" fill="#a78bfa" stroke="#121212" stroke-width="1"/>
    <circle cx="42" cy="15" r="4.5" fill="#4ade80" stroke="#121212" stroke-width="1"/>
    <text x="60" y="20" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">SKILLSYNC // NLP RESUME MATCHER</text>
    <rect x="306" y="5" width="108" height="20" rx="4" fill="#121212"/>
    <text x="313" y="19" font-size="9" font-weight="800" fill="#fde047">★ IDEATON WINNER</text>

    <!-- Mini UI Mockup -->
    <g transform="translate(14, 42)">
      <rect x="0" y="0" width="396" height="88" rx="6" fill="#1c1e27" stroke="#2e3240" stroke-width="1.5"/>
      <g transform="translate(12, 10)">
        <text x="0" y="12" font-size="9" font-weight="800" fill="#fde047">WEIGHTED NLP TOKENIZER (natural.js)</text>
        <g transform="translate(0, 22)">
          <rect x="0" y="0" width="95" height="18" rx="3" fill="#2f2b18" stroke="#fde047" stroke-width="1"/>
          <text x="6" y="12" font-size="8.5" font-weight="800" fill="#fde047">3x MUST-HAVE</text>
          <rect x="102" y="0" width="85" height="18" rx="3" fill="#252834"/>
          <text x="108" y="12" font-size="8.5" font-weight="700" fill="#9ca3af">1x Preferred</text>
        </g>
        <text x="0" y="56" font-size="9" font-weight="700" fill="#9ca3af">Client-side pdf.js text extraction</text>
        <text x="0" y="70" font-size="9" font-weight="700" fill="#4ade80">Zero keyword-stuffing exploits</text>
      </g>
      <g transform="translate(225, 10)">
        <rect x="0" y="0" width="160" height="66" rx="4" fill="#242735" stroke="#3d4255" stroke-width="1"/>
        <text x="10" y="18" font-size="9" font-weight="800" fill="#4ade80">MATCH RANKING</text>
        <text x="10" y="38" font-size="16" font-weight="900" fill="#ffffff">94.8% <tspan font-size="10" fill="#fde047">TOP FIT</tspan></text>
        <text x="10" y="54" font-size="8.5" font-weight="600" fill="#9ca3af">Sole Dev &amp; Team Lead</text>
      </g>
    </g>

    <!-- Description & Stack -->
    <text x="14" y="150" font-size="11.5" font-weight="700" fill="#ffffff">NLP-powered resume screening platform with weighted candidate matching.</text>
    <g transform="translate(14, 166)">
      <rect x="0" y="0" width="56" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="6" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Node.js</text>
      <rect x="62" y="0" width="70" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="68" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">natural.js</text>
      <rect x="138" y="0" width="52" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="144" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">pdf.js</text>
      <rect x="196" y="0" width="56" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="202" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Chart.js</text>
      <rect x="315" y="0" width="95" height="20" rx="4" fill="#fde047" stroke="#121212" stroke-width="1.5"/>
      <text x="323" y="14" font-size="8.5" font-weight="900" fill="#121212">EXPLORE REPO ↗</text>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_project_opportunityos_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 440 220" width="100%" height="auto" style="max-width: 440px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="p-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3" dy="3" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <g transform="translate(6, 6)">
    <rect x="0" y="0" width="424" height="204" rx="8" fill="#15171e" stroke="#121212" stroke-width="3" filter="url(#p-shadow)"/>
    <!-- Titlebar -->
    <rect x="0" y="0" width="424" height="30" rx="6" fill="#a78bfa" stroke="#121212" stroke-width="3"/>
    <circle cx="14" cy="15" r="4.5" fill="#fb7185" stroke="#121212" stroke-width="1"/>
    <circle cx="28" cy="15" r="4.5" fill="#fde047" stroke="#121212" stroke-width="1"/>
    <circle cx="42" cy="15" r="4.5" fill="#4ade80" stroke="#121212" stroke-width="1"/>
    <text x="60" y="20" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">OPPORTUNITYOS // CAREER SUITE</text>
    <rect x="315" y="5" width="98" height="20" rx="4" fill="#121212"/>
    <text x="323" y="19" font-size="9" font-weight="800" fill="#a78bfa">● PROD SYSTEM</text>

    <!-- Mini UI Mockup -->
    <g transform="translate(14, 42)">
      <rect x="0" y="0" width="396" height="88" rx="6" fill="#1c1e27" stroke="#2e3240" stroke-width="1.5"/>
      <g transform="translate(12, 10)">
        <text x="0" y="12" font-size="9" font-weight="800" fill="#a78bfa">GROQ SDK LLM INFERENCE ENGINE</text>
        <g transform="translate(0, 22)">
          <rect x="0" y="0" width="105" height="18" rx="3" fill="#2d2540" stroke="#a78bfa" stroke-width="1"/>
          <text x="6" y="12" font-size="8.5" font-weight="800" fill="#a78bfa">LATENCY &lt;110ms</text>
          <rect x="112" y="0" width="75" height="18" rx="3" fill="#252834"/>
          <text x="118" y="12" font-size="8.5" font-weight="700" fill="#9ca3af">ATS Opt</text>
        </g>
        <text x="0" y="56" font-size="9" font-weight="700" fill="#9ca3af">Cloudflare R2 multi-tenant document vault</text>
        <text x="0" y="70" font-size="9" font-weight="700" fill="#4ade80">Integrated via AWS S3 SDK presigned URLs</text>
      </g>
      <g transform="translate(225, 10)">
        <rect x="0" y="0" width="160" height="66" rx="4" fill="#242735" stroke="#3d4255" stroke-width="1"/>
        <text x="10" y="18" font-size="9" font-weight="800" fill="#ff90e8">ACTIVE PIPELINE</text>
        <text x="10" y="38" font-size="16" font-weight="900" fill="#ffffff">18 <tspan font-size="10" fill="#4ade80">LEADS MATCHED</tspan></text>
        <text x="10" y="54" font-size="8.5" font-weight="600" fill="#9ca3af">Next.js 16 + React 19</text>
      </g>
    </g>

    <!-- Description & Stack -->
    <text x="14" y="150" font-size="11.5" font-weight="700" fill="#ffffff">Full-stack career automation platform with AI resume roasting &amp; matching.</text>
    <g transform="translate(14, 166)">
      <rect x="0" y="0" width="62" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="6" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Next.js 16</text>
      <rect x="68" y="0" width="56" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="74" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">Groq AI</text>
      <rect x="130" y="0" width="56" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="136" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">AWS S3</text>
      <rect x="192" y="0" width="48" height="20" rx="3" fill="#232630" stroke="#374151" stroke-width="1"/>
      <text x="198" y="14" font-size="8.5" font-weight="800" fill="#e5e7eb">R2</text>
      <rect x="315" y="0" width="95" height="20" rx="4" fill="#a78bfa" stroke="#121212" stroke-width="1.5"/>
      <text x="323" y="14" font-size="8.5" font-weight="900" fill="#121212">EXPLORE REPO ↗</text>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_tech_toolbox_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 200" width="100%" height="auto" style="max-width: 920px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="box-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3.5" dy="3.5" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <g transform="translate(6, 6)">
    <!-- Container Body -->
    <rect x="0" y="0" width="904" height="184" rx="8" fill="#121318" stroke="#121212" stroke-width="3" filter="url(#box-shadow)"/>
    
    <!-- Top Bar -->
    <rect x="0" y="0" width="904" height="28" rx="6" fill="#ff90e8" stroke="#121212" stroke-width="3"/>
    <circle cx="16" cy="14" r="4.5" fill="#fb7185" stroke="#121212" stroke-width="1.5"/>
    <circle cx="32" cy="14" r="4.5" fill="#fde047" stroke="#121212" stroke-width="1.5"/>
    <circle cx="48" cy="14" r="4.5" fill="#4ade80" stroke="#121212" stroke-width="1.5"/>
    <text x="68" y="19" font-size="11" font-weight="900" fill="#121212" letter-spacing="1">DEVELOPER TOOLBOX // PRODUCTION STACK &amp; CAPABILITIES</text>

    <!-- Tray 1: Languages -->
    <g transform="translate(18, 38)">
      <rect x="0" y="0" width="100" height="26" rx="4" fill="#fde047" stroke="#121212" stroke-width="2"/>
      <text x="12" y="17" font-size="10" font-weight="900" fill="#121212">LANGUAGES</text>
      <g transform="translate(112, 1)">
        <rect x="0" y="0" width="76" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="10" y="16" font-size="10" font-weight="700" fill="#fde047">JavaScript</text>
        <rect x="84" y="0" width="78" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="94" y="16" font-size="10" font-weight="700" fill="#60a5fa">TypeScript</text>
        <rect x="170" y="0" width="46" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="184" y="16" font-size="10" font-weight="700" fill="#e5e7eb">C</text>
        <rect x="224" y="0" width="50" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="236" y="16" font-size="10" font-weight="700" fill="#e5e7eb">C++</text>
        <rect x="282" y="0" width="56" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="294" y="16" font-size="10" font-weight="700" fill="#e5e7eb">Java</text>
        <rect x="346" y="0" width="50" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="358" y="16" font-size="10" font-weight="700" fill="#e5e7eb">SQL</text>
        <rect x="404" y="0" width="80" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="414" y="16" font-size="10" font-weight="700" fill="#e5e7eb">HTML/CSS</text>
      </g>
    </g>

    <!-- Tray 2: Build -->
    <g transform="translate(18, 72)">
      <rect x="0" y="0" width="100" height="26" rx="4" fill="#ff90e8" stroke="#121212" stroke-width="2"/>
      <text x="12" y="17" font-size="10" font-weight="900" fill="#121212">BUILD WITH</text>
      <g transform="translate(112, 1)">
        <rect x="0" y="0" width="76" height="24" rx="4" fill="#1f222c" stroke="#ff90e8" stroke-width="1.5"/>
        <text x="10" y="16" font-size="10" font-weight="800" fill="#ff90e8">Next.js 16</text>
        <rect x="84" y="0" width="70" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="94" y="16" font-size="10" font-weight="700" fill="#60a5fa">React 19</text>
        <rect x="162" y="0" width="66" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="172" y="16" font-size="10" font-weight="700" fill="#4ade80">Node.js</text>
        <rect x="236" y="0" width="64" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="246" y="16" font-size="10" font-weight="700" fill="#e5e7eb">Express</text>
        <rect x="308" y="0" width="86" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="318" y="16" font-size="10" font-weight="700" fill="#38bdf8">Tailwind CSS</text>
        <rect x="402" y="0" width="62" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="412" y="16" font-size="10" font-weight="700" fill="#38bdf8">Flutter</text>
        <rect x="472" y="0" width="82" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="482" y="16" font-size="10" font-weight="700" fill="#4ade80">Playwright</text>
      </g>
    </g>

    <!-- Tray 3: Data -->
    <g transform="translate(18, 106)">
      <rect x="0" y="0" width="100" height="26" rx="4" fill="#3b82f6" stroke="#121212" stroke-width="2"/>
      <text x="12" y="17" font-size="10" font-weight="900" fill="#ffffff">DATABASES</text>
      <g transform="translate(112, 1)">
        <rect x="0" y="0" width="138" height="24" rx="4" fill="#1f222c" stroke="#3b82f6" stroke-width="1.5"/>
        <text x="10" y="16" font-size="10" font-weight="800" fill="#60a5fa">PostgreSQL (Supabase)</text>
        <rect x="146" y="0" width="60" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="156" y="16" font-size="10" font-weight="700" fill="#e5e7eb">MySQL</text>
        <rect x="214" y="0" width="76" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="224" y="16" font-size="10" font-weight="700" fill="#4ade80">MongoDB</text>
        <rect x="298" y="0" width="56" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="308" y="16" font-size="10" font-weight="700" fill="#fb7185">Redis</text>
      </g>
    </g>

    <!-- Tray 4: Cloud -->
    <g transform="translate(18, 140)">
      <rect x="0" y="0" width="100" height="26" rx="4" fill="#4ade80" stroke="#121212" stroke-width="2"/>
      <text x="12" y="17" font-size="10" font-weight="900" fill="#121212">CLOUD &amp; INFRA</text>
      <g transform="translate(112, 1)">
        <rect x="0" y="0" width="176" height="24" rx="4" fill="#1f222c" stroke="#fde047" stroke-width="1.5"/>
        <text x="10" y="16" font-size="10" font-weight="800" fill="#fde047">AWS (S3, EC2, Lambda, IAM)</text>
        <rect x="184" y="0" width="106" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="194" y="16" font-size="10" font-weight="700" fill="#fb923c">Cloudflare R2</text>
        <rect x="298" y="0" width="60" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="308" y="16" font-size="10" font-weight="700" fill="#e5e7eb">Vercel</text>
        <rect x="366" y="0" width="112" height="24" rx="4" fill="#1f222c" stroke="#374151" stroke-width="1"/>
        <text x="376" y="16" font-size="10" font-weight="700" fill="#60a5fa">GitHub Actions</text>
      </g>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

if __name__ == "__main__":
    create_system_status_svg("assets/system-status.svg")
    create_exploring_cards_svg("assets/exploring-cards.svg")
    create_how_i_build_svg("assets/build-pipeline.svg")
    create_project_leetboard_svg("assets/project-leetboard.svg")
    create_project_quietdemand_svg("assets/project-quietdemand.svg")
    create_project_skillsync_svg("assets/project-skillsync.svg")
    create_project_opportunityos_svg("assets/project-opportunityos.svg")
    create_tech_toolbox_svg("assets/tech-toolbox.svg")
