import os

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
    <text x="14" y="74" font-size="10.5" font-weight="500" fill="#9ca3af">Building products from</text>
    <text x="14" y="89" font-size="10.5" font-weight="500" fill="#9ca3af">idea to deployment.</text>
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
    <text x="14" y="74" font-size="10.5" font-weight="500" fill="#9ca3af">Designing cloud systems</text>
    <text x="14" y="89" font-size="10.5" font-weight="500" fill="#9ca3af">beyond the laptop.</text>
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
    <text x="14" y="74" font-size="10.5" font-weight="500" fill="#9ca3af">Building useful software</text>
    <text x="14" y="89" font-size="10.5" font-weight="500" fill="#9ca3af">around AI.</text>
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
    <text x="14" y="74" font-size="10.5" font-weight="500" fill="#9ca3af">Turning repetitive work</text>
    <text x="14" y="89" font-size="10.5" font-weight="500" fill="#9ca3af">into systems.</text>
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
    <rect x="0" y="0" width="424" height="30" rx="6" fill="#3b82f6" stroke="#121212" stroke-width="3"/>
    <circle cx="14" cy="15" r="4.5" fill="#fb7185" stroke="#121212" stroke-width="1"/>
    <circle cx="28" cy="15" r="4.5" fill="#fde047" stroke="#121212" stroke-width="1"/>
    <circle cx="42" cy="15" r="4.5" fill="#4ade80" stroke="#121212" stroke-width="1"/>
    <text x="60" y="20" font-size="11" font-weight="900" fill="#ffffff" letter-spacing="0.5">LEETBOARD // CP ANALYTICS</text>
    <rect x="325" y="5" width="88" height="20" rx="4" fill="#121212"/>
    <text x="333" y="19" font-size="9" font-weight="800" fill="#fde047">● DEPT ADOPTED</text>

    <!-- Mini UI Mockup -->
    <g transform="translate(14, 42)">
      <rect x="0" y="0" width="396" height="88" rx="6" fill="#1c1e27" stroke="#2e3240" stroke-width="1.5"/>
      <g transform="translate(10, 10)">
        <text x="0" y="12" font-size="9" font-weight="800" fill="#9ca3af">CONTEST RATING TRACKER</text>
        <text x="0" y="32" font-size="18" font-weight="900" fill="#60a5fa">1,942 <tspan font-size="11" fill="#4ade80">▲ +128</tspan></text>
        <path d="M 0 52 Q 25 45, 50 48 T 100 36 T 150 28 T 200 18" fill="none" stroke="#3b82f6" stroke-width="2.5"/>
      </g>
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
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 236" width="100%" height="auto" style="max-width: 920px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="box-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3.5" dy="3.5" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <g transform="translate(6, 6)">
    <!-- Container Body -->
    <rect x="0" y="0" width="904" height="220" rx="8" fill="#121318" stroke="#121212" stroke-width="3" filter="url(#box-shadow)"/>
    
    <!-- Top Bar -->
    <rect x="0" y="0" width="904" height="28" rx="6" fill="#fde047" stroke="#121212" stroke-width="3"/>
    <circle cx="16" cy="14" r="4.5" fill="#fb7185" stroke="#121212" stroke-width="1.5"/>
    <circle cx="32" cy="14" r="4.5" fill="#3b82f6" stroke="#121212" stroke-width="1.5"/>
    <circle cx="48" cy="14" r="4.5" fill="#4ade80" stroke="#121212" stroke-width="1.5"/>
    <text x="68" y="19" font-size="11" font-weight="900" fill="#121212" letter-spacing="1">DEVELOPER TOOLBOX // PRODUCTION STACK &amp; CAPABILITIES</text>

    <!-- ================= ROW 1: LANGUAGES ================= -->
    <g transform="translate(18, 40)">
      <rect x="0" y="0" width="102" height="28" rx="4" fill="#fde047" stroke="#121212" stroke-width="2"/>
      <text x="11" y="18" font-size="10" font-weight="900" fill="#121212">LANGUAGES</text>
      
      <!-- JavaScript -->
      <g transform="translate(114, 0)">
        <rect x="0" y="0" width="112" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <rect width="16" height="16" rx="2" fill="#F7DF1E"/>
          <path d="M4 11.5c.3.5.7.9 1.4.9.8 0 1.2-.4 1.2-1.3V5h1.6v6.1c0 1.7-1 2.5-2.6 2.5-1.4 0-2.3-.7-2.6-1.6l1-.5zm5.3.8c.4.3.9.5 1.5.5.9 0 1.4-.4 1.4-1 0-.6-.4-.9-1.3-1.3l-.5-.2c-1.3-.6-2-1.4-2-2.5 0-1.4 1.1-2.4 2.7-2.4 1 0 1.7.3 2.2.8l-.9 1.1c-.3-.3-.7-.5-1.3-.5-.7 0-1.1.4-1.1.9 0 .6.4.8 1.2 1.2l.5.2c1.4.6 2.2 1.4 2.2 2.6 0 1.6-1.2 2.5-2.9 2.5-1.2 0-2.1-.4-2.7-1l.9-1.2z" fill="#000000"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#fde047">JavaScript</text>
      </g>

      <!-- TypeScript -->
      <g transform="translate(234, 0)">
        <rect x="0" y="0" width="112" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <rect width="16" height="16" rx="2" fill="#3178C6"/>
          <path d="M3.5 6.5h4v1.2H6.1v4.7H4.9V7.7H3.5V6.5zm5 3.5c.3.2.7.4 1.2.4.6 0 .9-.3.9-.7 0-.4-.3-.6-.8-.8l-.4-.2c-.9-.4-1.4-.9-1.4-1.7 0-1 .8-1.7 2-1.7.7 0 1.2.2 1.5.5l-.6.9c-.3-.2-.5-.3-.9-.3-.5 0-.8.3-.8.6 0 .4.3.6.8.8l.4.2c1 .4 1.5.9 1.5 1.7 0 1.1-.9 1.8-2.1 1.8-.8 0-1.5-.3-1.8-.7l.6-.9z" fill="#FFFFFF"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#60a5fa">TypeScript</text>
      </g>

      <!-- C++ -->
      <g transform="translate(354, 0)">
        <rect x="0" y="0" width="76" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#00599C"/>
          <path d="M8 4.2a3.8 3.8 0 1 0 2.8 6.4l-1.1-.9A2.4 2.4 0 1 1 8 5.6c.9 0 1.6.4 2 1.1l1.1-.9A3.8 3.8 0 0 0 8 4.2z" fill="#FFFFFF"/>
          <path d="M11.5 7.2h.8v-.8h.6v.8h.8v.6h-.8v.8h-.6v-.8h-.8v-.6zm2.4 0h.8v-.8h.6v.8h.8v.6h-.8v.8h-.6v-.8h-.8v-.6z" fill="#38BDF8"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#e5e7eb">C++</text>
      </g>

      <!-- Java -->
      <g transform="translate(438, 0)">
        <rect x="0" y="0" width="80" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#292d3e"/>
          <path d="M6.2 13.2c1.8.1 3.5-.3 4.8-1 .3-.2.6-.4.4-.6-.2-.2-.5-.1-.7 0-1.1.6-2.5.9-4 .8-1.2-.1-2.2-.4-2.4-.7-.2-.2-.2-.5.1-.6 1.4-.6 3.4-.7 5.2-.4 1.9.3 3.3 1.1 3.4 2 .2 1.2-1.5 2.1-4 2.3-1.7.1-3.2-.2-4.1-.7-.3-.2-.2-.5 0-.6.2-.1.6 0 1.3.1zm1.1-2.2c1.2.1 2.4-.2 3.3-.6.3-.1.5-.3.4-.5s-.4-.1-.6 0c-.8.4-1.7.6-2.8.5-.9-.1-1.6-.3-1.7-.5-.1-.2-.1-.4.1-.4 1-.4 2.4-.5 3.6-.3 1.3.2 2.3.8 2.4 1.4.1.8-1 1.5-2.8 1.6-1.2.1-2.2-.1-2.9-.5-.2-.1-.2-.4 0-.5.2-.1.4-.2.9-.2zm-.8-3.4c.5.8 1.4 1.3 2.5 1.5.3 0 .4-.2.3-.4-.2-.2-.5-.4-.8-.6-.6-.4-1.1-1-1.3-1.7-.1-.5 0-1 .2-1.5.1-.2 0-.3-.2-.3-.2 0-.3.2-.4.4-.4.8-.5 1.8-.3 2.6zm3.1-4c-.1.6-.4 1.1-.8 1.6-.2.2-.1.4.1.4.2 0 .4-.1.6-.3.6-.6 1-1.3 1.1-2.1 0-.3-.1-.6-.3-.8-.1-.1-.3 0-.4.1-.2.3-.3.7-.3 1.1z" fill="#EA2D2E"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#e5e7eb">Java</text>
      </g>

      <!-- SQL -->
      <g transform="translate(526, 0)">
        <rect x="0" y="0" width="76" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <ellipse cx="8" cy="4" rx="6" ry="2.2" fill="#00BCF2"/>
          <path d="M2 4v3.5c0 1.2 2.7 2.2 6 2.2s6-1 6-2.2V4" fill="none" stroke="#00BCF2" stroke-width="1.2"/>
          <path d="M2 7.5V11c0 1.2 2.7 2.2 6 2.2s6-1 6-2.2V7.5" fill="none" stroke="#00BCF2" stroke-width="1.2"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#00BCF2">SQL</text>
      </g>
    </g>

    <!-- ================= ROW 2: BUILD ================= -->
    <g transform="translate(18, 82)">
      <rect x="0" y="0" width="102" height="28" rx="4" fill="#ff90e8" stroke="#121212" stroke-width="2"/>
      <text x="17" y="18" font-size="10" font-weight="900" fill="#121212">BUILD</text>

      <!-- React -->
      <g transform="translate(114, 0)">
        <rect x="0" y="0" width="88" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="1.6" fill="#61DAFB"/>
          <ellipse cx="8" cy="8" rx="7.2" ry="2.6" fill="none" stroke="#61DAFB" stroke-width="1.1"/>
          <ellipse cx="8" cy="8" rx="7.2" ry="2.6" transform="rotate(60 8 8)" fill="none" stroke="#61DAFB" stroke-width="1.1"/>
          <ellipse cx="8" cy="8" rx="7.2" ry="2.6" transform="rotate(120 8 8)" fill="none" stroke="#61DAFB" stroke-width="1.1"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#61DAFB">React</text>
      </g>

      <!-- Next.js -->
      <g transform="translate(210, 0)">
        <rect x="0" y="0" width="94" height="28" rx="5" fill="#1a1c24" stroke="#ff90e8" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#000000" stroke="#FFFFFF" stroke-width="0.8"/>
          <path d="M10.8 11.2 6 5.5h-.9v5.7h1.1V7.2l4.1 4.9c.2-.3.4-.6.6-.9zM10.8 5.5h-1.1v3.2l1.1 1.3V5.5z" fill="#FFFFFF"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="800" fill="#ff90e8">Next.js</text>
      </g>

      <!-- Node.js -->
      <g transform="translate(312, 0)">
        <rect x="0" y="0" width="94" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <path d="M8 1.5 14 5v6l-6 3.5L2 11V5l6-3.5z" fill="#339933"/>
          <path d="M8 5a3 3 0 0 0-3 3v1a3 3 0 0 0 6 0V8a3 3 0 0 0-3-3zm1.6 4a1.6 1.6 0 0 1-3.2 0V8a1.6 1.6 0 0 1 3.2 0v1z" fill="#FFFFFF"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#4ade80">Node.js</text>
      </g>

      <!-- Express -->
      <g transform="translate(414, 0)">
        <rect x="0" y="0" width="96" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#2b2d38"/>
          <text x="3.5" y="11" font-size="8.5" font-weight="900" fill="#FFFFFF" font-family="sans-serif">ex</text>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#e5e7eb">Express</text>
      </g>

      <!-- Tailwind CSS -->
      <g transform="translate(518, 0)">
        <rect x="0" y="0" width="112" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <path d="M8 4.2c-2.4 0-3.9 1.2-4.5 3.6 1-.9 2-.9 2.7-.4.6.4 1 1 1.7 1.7 1.1 1.1 2.3 2.4 5.1 2.4 2.4 0 3.9-1.2 4.5-3.6-1 .9-2 .9-2.7.4-.6-.4-1-1-1.7-1.7-1.1-1.1-2.4-2.4-5.1-2.4zm-4.5 5.3c-2.4 0-3.9 1.2-4.5 3.6 1-.9 2-.9 2.7-.4.6.4 1 1 1.7 1.7 1.1 1.1 2.4 2.4 5.1 2.4 2.4 0 3.9-1.2 4.5-3.6-1 .9-2 .9-2.7.4-.6-.4-1-1-1.7-1.7-1.1-1.1-2.4-2.4-5.1-2.4z" fill="#38BDF8"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#38BDF8">Tailwind CSS</text>
      </g>

      <!-- Flutter -->
      <g transform="translate(638, 0)">
        <rect x="0" y="0" width="92" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <path d="M8.8 1.5 3.2 7.1l1.8 1.8L12.4 1.5H8.8zm-.2 5.5L4.8 10.8l3.8 3.7h3.6L8.4 10.8l3.8-3.8H8.6z" fill="#54C5F8"/>
          <path d="M6.2 12.2 4.8 10.8 3.2 12.4l2.1 2.1h3.6l-2.7-2.3z" fill="#02569B"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#54C5F8">Flutter</text>
      </g>
    </g>

    <!-- ================= ROW 3: DATA ================= -->
    <g transform="translate(18, 124)">
      <rect x="0" y="0" width="102" height="28" rx="4" fill="#3b82f6" stroke="#121212" stroke-width="2"/>
      <text x="21" y="18" font-size="10" font-weight="900" fill="#ffffff">DATA</text>

      <!-- PostgreSQL -->
      <g transform="translate(114, 0)">
        <rect x="0" y="0" width="118" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#202a3a"/>
          <path d="M8 2.2C5.3 2.2 3.5 4 3.5 6.4c0 1.6.8 2.8 2.1 3.5-.2.5-.5 1-1 1.3l.8.8c.8-.4 1.3-1.1 1.6-1.8.7.2 1.4.3 2 .3 4.2 0 6.5-2.5 6.5-5.2 0-1.8-1.5-3.3-3.5-3.3zm0 1.2c1.4 0 2.4 1 2.4 2.2 0 1.7-1.7 3.5-4.2 3.5-.9 0-1.6-.3-1.9-.8-.4-.7-.2-1.8.7-2.6 1-.8 2-1.3 3-2.3z" fill="#336791"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#60a5fa">PostgreSQL</text>
      </g>

      <!-- MySQL -->
      <g transform="translate(240, 0)">
        <rect x="0" y="0" width="94" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#1f2c38"/>
          <path d="M2.5 10.5C3.2 7 5.8 4 9 4c2.2 0 4 1.2 4.8 3 .4.9.4 2-.2 2.8-.7.9-1.8 1.2-3 1.2-1.2 0-2.3-.4-3.1-1.1-.3-.2-.5-.5-.6-.8-.2.8-.5 1.5-.9 2.1-.3.4-.6.8-1 1.1l-.8-.8c.7-.6 1.1-1.2 1.3-1.9z" fill="#00758F"/>
          <circle cx="11.5" cy="5.8" r="0.8" fill="#F29111"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#e5e7eb">MySQL</text>
      </g>

      <!-- MongoDB -->
      <g transform="translate(342, 0)">
        <rect x="0" y="0" width="104" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#1b2e20"/>
          <path d="M8 1.5s-.3.4-.7 1.2c-.8 1.5-2 3.5-2 5.6 0 2.5 1.8 4.7 3.9 5.2.4.1.8.1.8.1s.4 0 .8-.1c2.1-.5 3.9-2.7 3.9-5.2 0-2.1-1.2-4.1-2-5.6-.4-.8-.7-1.2-.7-1.2s-.3 1.2-.5 2.8c-.3 2.2-.4 3.7-.4 4.8h-.6c0-1.1-.1-2.6-.4-4.8-.2-1.6-.5-2.8-.5-2.8z" fill="#47A248"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#4ade80">MongoDB</text>
      </g>

      <!-- Redis -->
      <g transform="translate(454, 0)">
        <rect x="0" y="0" width="88" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#2b1a1c"/>
          <path d="M8 2.2 1.8 5.4 8 8.6l6.2-3.2L8 2.2z" fill="#DC382D"/>
          <path d="m1.8 7.5 6.2 3.2 6.2-3.2v1.5L8 12.2l-6.2-3.2V7.5z" fill="#A82820"/>
          <path d="m1.8 10.5 6.2 3.2 6.2-3.2v1.5L8 15.2l-6.2-3.2v-1.5z" fill="#801C16"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#fb7185">Redis</text>
      </g>
    </g>

    <!-- ================= ROW 4: CLOUD & INFRA ================= -->
    <g transform="translate(18, 166)">
      <rect x="0" y="0" width="102" height="28" rx="4" fill="#4ade80" stroke="#121212" stroke-width="2"/>
      <text x="9" y="18" font-size="9.5" font-weight="900" fill="#121212">CLOUD/INFRA</text>

      <!-- AWS -->
      <g transform="translate(114, 0)">
        <rect x="0" y="0" width="82" height="28" rx="5" fill="#1a1c24" stroke="#fde047" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#25241b"/>
          <path d="M4.2 11.2c2.4 1.3 5.2 1.3 7.6 0 .3-.2.7.1.5.4-2.8 1.8-6.1 1.8-8.6 0-.3-.3.1-.6.5-.4z" fill="#FF9900"/>
          <path d="M12.4 10.8c-.1-.2-.6-.4-1.1-.4-.6 0-.9.4-.9.4s.2.2.4.3c.4.2.8.2 1.1.2.2 0 .5-.1.5-.5z" fill="#FF9900"/>
          <text x="3" y="7.5" font-size="6" font-weight="900" fill="#FFFFFF" font-family="sans-serif">aws</text>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="800" fill="#fde047">AWS</text>
      </g>

      <!-- Cloudflare -->
      <g transform="translate(204, 0)">
        <rect x="0" y="0" width="134" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#2d2218"/>
          <path d="M11.6 7.4c-.2-.9-.9-1.6-1.8-1.7-.5-.9-1.4-1.5-2.5-1.5-1.3 0-2.4.8-2.8 2-.3 0-.6.1-.8.3-.7.5-.9 1.4-.6 2.1H12c.7 0 1.2-.5 1.2-1.2 0-.6-.5-1.1-1.1-1.2-.2 0-.3 0-.5.2z" fill="#F38020"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#fb923c">Cloudflare R2</text>
      </g>

      <!-- Vercel -->
      <g transform="translate(346, 0)">
        <rect x="0" y="0" width="90" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#252525"/>
          <path d="M8 4 13.5 13H2.5L8 4z" fill="#FFFFFF"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#ffffff">Vercel</text>
      </g>

      <!-- GitHub Actions -->
      <g transform="translate(444, 0)">
        <rect x="0" y="0" width="144" height="28" rx="5" fill="#1a1c24" stroke="#2e3240" stroke-width="1.2"/>
        <g transform="translate(8, 6)">
          <circle cx="8" cy="8" r="7.5" fill="#1b2a3d"/>
          <path d="M8 4.2v2.4a1.8 1.8 0 1 1-1.8 1.8H3.8a4.2 4.2 0 1 0 4.2-4.2z" fill="#2088FF"/>
          <circle cx="10.8" cy="8.4" r="1.2" fill="#2088FF"/>
        </g>
        <text x="30" y="18" font-size="10.5" font-weight="700" fill="#60a5fa">GitHub Actions</text>
      </g>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_building_software_card_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 220" width="100%" height="auto" style="max-width: 920px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="card-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="3.5" dy="3.5" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
    <filter id="inner-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="2" dy="2" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <g transform="translate(6, 6)">
    <!-- Base Physical Card: Off-White Cardstock -->
    <rect x="0" y="0" width="904" height="206" rx="8" fill="#FAF9F6" stroke="#121212" stroke-width="3" filter="url(#card-shadow)"/>

    <!-- ================= TOP HEADER / STATUS ROW ================= -->
    <g transform="translate(18, 14)">
      <!-- Tab Badge -->
      <rect x="0" y="0" width="144" height="22" rx="4" fill="#121212"/>
      <text x="12" y="15" font-size="9.5" font-weight="900" fill="#fde047" letter-spacing="1">⚡ CORE DIRECTIVE</text>

      <!-- Micro-Labels: Input -> Output Pipeline -->
      <g transform="translate(156, 0)">
        <rect x="0" y="0" width="136" height="22" rx="4" fill="#ffffff" stroke="#121212" stroke-width="1.2"/>
        <text x="8" y="15" font-size="8.5" font-weight="800" fill="#64748b" font-family="monospace">INPUT // REAL PROBLEM</text>
        
        <!-- Connecting Circuit Trace -->
        <line x1="136" y1="11" x2="158" y2="11" stroke="#cbd5e1" stroke-width="1.5"/>
        <circle cx="147" cy="11" r="2" fill="#3b82f6"/>
        <polygon points="156,8 162,11 156,14" fill="#64748b"/>

        <rect x="166" y="0" width="168" height="22" rx="4" fill="#ffffff" stroke="#121212" stroke-width="1.2"/>
        <text x="174" y="15" font-size="8.5" font-weight="800" fill="#059669" font-family="monospace">OUTPUT // WORKING SOFTWARE</text>

        <!-- Seamless output lead -->
        <line x1="334" y1="11" x2="350" y2="11" stroke="#cbd5e1" stroke-width="1.5"/>
      </g>
    </g>

    <!-- Top-Right Subtle Circuit Trace -->
    <g transform="translate(506, 14)">
      <path d="M 0 11 L 320 11 L 336 26 L 336 34" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="0" cy="11" r="2.5" fill="#fde047" stroke="#121212" stroke-width="1"/>
      <circle cx="160" cy="11" r="2" fill="#3b82f6"/>
      <circle cx="336" cy="34" r="2.5" fill="#10b981" stroke="#121212" stroke-width="1"/>
      <text x="345" y="24" font-size="8" font-weight="800" fill="#94a3b8" font-family="monospace">PCB.01</text>
    </g>

    <!-- ================= RAISED QUOTE CARD ================= -->
    <g transform="translate(18, 44)">
      <!-- Quote Card Surface -->
      <rect x="0" y="0" width="868" height="68" rx="6" fill="#FFFFFF" stroke="#121212" stroke-width="2" filter="url(#inner-shadow)"/>
      
      <!-- Yellow Accent Left Spine -->
      <rect x="0" y="0" width="6" height="68" rx="2" fill="#fde047" stroke="#121212" stroke-width="2"/>

      <!-- Quote Emblem -->
      <g transform="translate(18, 16)">
        <rect x="0" y="0" width="26" height="26" rx="4" fill="#fde047" stroke="#121212" stroke-width="1.5"/>
        <text x="7" y="18" font-size="16" font-weight="900" fill="#121212" font-family="Georgia, serif">“</text>
      </g>

      <!-- The Quote Text -->
      <text x="56" y="27" font-size="15.5" font-weight="800" fill="#0f172a" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">"I like taking real problems, turning them into software,</text>
      <text x="56" y="49" font-size="15.5" font-weight="800" fill="#0f172a" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">and seeing how far I can take the idea."</text>
    </g>

    <!-- ================= MAIN PARAGRAPH (SECOND LAYER) ================= -->
    <g transform="translate(18, 122)">
      <text x="18" y="15" font-size="12.5" font-weight="500" fill="#334155" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">I’m a product-minded developer who builds complete web products from scratch.</text>
      <text x="18" y="32" font-size="12.5" font-weight="500" fill="#334155" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">Instead of building tutorial clones, I look for genuine friction points — manual tracking,</text>
      <text x="18" y="49" font-size="12.5" font-weight="500" fill="#334155" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">unvalidated startup assumptions, or noisy candidate screening —</text>
      <text x="18" y="67" font-size="12.5" font-weight="800" fill="#0f172a" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif">and build tools that actually work.</text>
    </g>

    <!-- ================= SUBTLE BOTTOM-RIGHT CIRCUIT TRACE & PORTFOLIO CTA ================= -->
    <g transform="translate(500, 172)">
      <path d="M 0 0 L 190 0 L 206 0" fill="none" stroke="#cbd5e1" stroke-width="1.5" stroke-linecap="round"/>
      <circle cx="0" cy="0" r="2.5" fill="#3b82f6" stroke="#121212" stroke-width="1.2"/>
      <circle cx="100" cy="0" r="2.5" fill="#fde047" stroke="#121212" stroke-width="1.2"/>
      <circle cx="206" cy="0" r="3" fill="#10b981" stroke="#121212" stroke-width="1.2"/>
      <text x="10" y="-6" font-size="8" font-weight="800" fill="#94a3b8" font-family="monospace">TRACE // 0x4B</text>
      <text x="110" y="-6" font-size="8" font-weight="800" fill="#64748b" font-family="monospace">LIVE // PROD</text>
    </g>

    <!-- Physical Button CTA: VIEW PORTFOLIO ↗ -->
    <a href="https://mohammed-shafiq-s.vercel.app" target="_blank" rel="noopener noreferrer" style="text-decoration: none;">
      <g transform="translate(706, 156)" cursor="pointer">
        <rect x="0" y="0" width="168" height="32" rx="5" fill="#fde047" stroke="#121212" stroke-width="2" filter="url(#inner-shadow)"/>
        <text x="18" y="20" font-size="10.5" font-weight="900" fill="#121212" letter-spacing="0.5" font-family="-apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace">VIEW PORTFOLIO ↗</text>
      </g>
    </a>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_portfolio_button_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 172 36" width="172" height="36" style="font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Segoe UI', monospace;">
  <defs>
    <filter id="btn-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="2" dy="2" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>
  <rect x="2" y="2" width="164" height="30" rx="5" fill="#fde047" stroke="#121212" stroke-width="2" filter="url(#btn-shadow)"/>
  <text x="18" y="21" font-size="10.5" font-weight="900" fill="#121212" letter-spacing="0.5">VIEW PORTFOLIO ↗</text>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

if __name__ == "__main__":
    create_exploring_cards_svg("assets/exploring-cards.svg")
    create_how_i_build_svg("assets/build-pipeline.svg")
    create_project_leetboard_svg("assets/project-leetboard.svg")
    create_project_quietdemand_svg("assets/project-quietdemand.svg")
    create_project_skillsync_svg("assets/project-skillsync.svg")
    create_project_opportunityos_svg("assets/project-opportunityos.svg")
    create_tech_toolbox_svg("assets/tech-toolbox.svg")
    create_building_software_card_svg("assets/building-software-card.svg")
    create_portfolio_button_svg("assets/portfolio-cta.svg")
