import os

def create_build_pipeline_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 220" width="100%" height="auto" style="max-width: 920px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Consolas, 'Courier New', monospace;">
  <defs>
    <filter id="neo-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="4" dy="4" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
    <filter id="neo-shadow-sm" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="2.5" dy="2.5" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <!-- Step 1: DISCOVER -->
  <g transform="translate(10, 10)">
    <!-- Shadow & Card -->
    <rect x="0" y="0" width="162" height="195" rx="8" fill="#fefce8" stroke="#121212" stroke-width="3" filter="url(#neo-shadow)"/>
    <!-- Header Pill -->
    <rect x="0" y="0" width="162" height="34" rx="6" fill="#fde047" stroke="#121212" stroke-width="3"/>
    <text x="12" y="22" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">01 // DISCOVER</text>
    <circle cx="145" cy="17" r="4" fill="#121212"/>
    <!-- Content -->
    <text x="12" y="58" font-size="16" font-weight="900" fill="#121212">FIND PAIN</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#854d0e">REAL USER FRICTION</text>
    <line x1="12" y1="84" x2="150" y2="84" stroke="#121212" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="12" y="104" font-size="10.5" font-weight="600" fill="#374151">• Reddit sentiment</text>
    <text x="12" y="122" font-size="10.5" font-weight="600" fill="#374151">• Campus workflows</text>
    <text x="12" y="140" font-size="10.5" font-weight="600" fill="#374151">• "Why is this manual?"</text>
    <!-- Status Pill -->
    <rect x="12" y="158" width="138" height="24" rx="4" fill="#ffffff" stroke="#121212" stroke-width="2"/>
    <text x="22" y="174" font-size="9.5" font-weight="800" fill="#121212">SIGNAL VERIFIED ✓</text>
  </g>

  <!-- Arrow 1 -->
  <g transform="translate(176, 92)">
    <circle cx="9" cy="9" r="14" fill="#121212"/>
    <path d="M5 9 L13 9 M10 6 L13 9 L10 12" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Step 2: ARCHITECT -->
  <g transform="translate(196, 10)">
    <rect x="0" y="0" width="162" height="195" rx="8" fill="#fdf2f8" stroke="#121212" stroke-width="3" filter="url(#neo-shadow)"/>
    <rect x="0" y="0" width="162" height="34" rx="6" fill="#ff90e8" stroke="#121212" stroke-width="3"/>
    <text x="12" y="22" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">02 // ARCHITECT</text>
    <circle cx="145" cy="17" r="4" fill="#121212"/>
    <text x="12" y="58" font-size="16" font-weight="900" fill="#121212">BUILD CLEAN</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#9d174d">SCHEMAS &amp; STREAMS</text>
    <line x1="12" y1="84" x2="150" y2="84" stroke="#121212" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="12" y="104" font-size="10.5" font-weight="600" fill="#374151">• Next.js 16 + React 19</text>
    <text x="12" y="122" font-size="10.5" font-weight="600" fill="#374151">• Supabase PostgreSQL</text>
    <text x="12" y="140" font-size="10.5" font-weight="600" fill="#374151">• SSE Real-time feeds</text>
    <rect x="12" y="158" width="138" height="24" rx="4" fill="#ffffff" stroke="#121212" stroke-width="2"/>
    <text x="22" y="174" font-size="9.5" font-weight="800" fill="#121212">MODULAR STACK ✓</text>
  </g>

  <!-- Arrow 2 -->
  <g transform="translate(362, 92)">
    <circle cx="9" cy="9" r="14" fill="#121212"/>
    <path d="M5 9 L13 9 M10 6 L13 9 L10 12" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Step 3: BREAK IT -->
  <g transform="translate(382, 10)">
    <rect x="0" y="0" width="162" height="195" rx="8" fill="#fff1f2" stroke="#121212" stroke-width="3" filter="url(#neo-shadow)"/>
    <rect x="0" y="0" width="162" height="34" rx="6" fill="#fb7185" stroke="#121212" stroke-width="3"/>
    <text x="12" y="22" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">03 // BREAK IT</text>
    <circle cx="145" cy="17" r="4" fill="#121212"/>
    <text x="12" y="58" font-size="16" font-weight="900" fill="#121212">STRESS TEST</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#be123c">PUSH BOUNDARIES</text>
    <line x1="12" y1="84" x2="150" y2="84" stroke="#121212" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="12" y="104" font-size="10.5" font-weight="600" fill="#374151">• Rate limit triggers</text>
    <text x="12" y="122" font-size="10.5" font-weight="600" fill="#374151">• Malformed inputs</text>
    <text x="12" y="140" font-size="10.5" font-weight="600" fill="#374151">• "If it didn't break,</text>
    <text x="12" y="152" font-size="9.5" font-weight="600" fill="#be123c">  you didn't push."</text>
    <rect x="12" y="158" width="138" height="24" rx="4" fill="#ffffff" stroke="#121212" stroke-width="2"/>
    <text x="22" y="174" font-size="9.5" font-weight="800" fill="#121212">FAILURE IS INTEL ✓</text>
  </g>

  <!-- Arrow 3 -->
  <g transform="translate(548, 92)">
    <circle cx="9" cy="9" r="14" fill="#121212"/>
    <path d="M5 9 L13 9 M10 6 L13 9 L10 12" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Step 4: DEBUG -->
  <g transform="translate(568, 10)">
    <rect x="0" y="0" width="162" height="195" rx="8" fill="#f5f3ff" stroke="#121212" stroke-width="3" filter="url(#neo-shadow)"/>
    <rect x="0" y="0" width="162" height="34" rx="6" fill="#a78bfa" stroke="#121212" stroke-width="3"/>
    <text x="12" y="22" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">04 // DEBUG</text>
    <circle cx="145" cy="17" r="4" fill="#121212"/>
    <text x="12" y="58" font-size="16" font-weight="900" fill="#121212">TRACE ROOT</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#6d28d9">SYSTEM HARDENING</text>
    <line x1="12" y1="84" x2="150" y2="84" stroke="#121212" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="12" y="104" font-size="10.5" font-weight="600" fill="#374151">• Exponential backoff</text>
    <text x="12" y="122" font-size="10.5" font-weight="600" fill="#374151">• 420ms -> 38ms query</text>
    <text x="12" y="140" font-size="10.5" font-weight="600" fill="#374151">• Zero bug ninja style</text>
    <rect x="12" y="158" width="138" height="24" rx="4" fill="#ffffff" stroke="#121212" stroke-width="2"/>
    <text x="22" y="174" font-size="9.5" font-weight="800" fill="#121212">TESTS PASSING ✓</text>
  </g>

  <!-- Arrow 4 -->
  <g transform="translate(734, 92)">
    <circle cx="9" cy="9" r="14" fill="#121212"/>
    <path d="M5 9 L13 9 M10 6 L13 9 L10 12" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
  </g>

  <!-- Step 5: SHIP -->
  <g transform="translate(754, 10)">
    <rect x="0" y="0" width="156" height="195" rx="8" fill="#f0fdf4" stroke="#121212" stroke-width="3" filter="url(#neo-shadow)"/>
    <rect x="0" y="0" width="156" height="34" rx="6" fill="#4ade80" stroke="#121212" stroke-width="3"/>
    <text x="12" y="22" font-size="11" font-weight="900" fill="#121212" letter-spacing="0.5">05 // SHIP &amp; SCALE</text>
    <circle cx="138" cy="17" r="4" fill="#121212"/>
    <text x="12" y="58" font-size="16" font-weight="900" fill="#121212">PROD ADOPTION</text>
    <text x="12" y="74" font-size="10" font-weight="700" fill="#15803d">SOFTWARE THAT WORKS</text>
    <line x1="12" y1="84" x2="144" y2="84" stroke="#121212" stroke-width="1.5" stroke-dasharray="3,3"/>
    <text x="12" y="104" font-size="10.5" font-weight="600" fill="#374151">• Vercel + AWS S3</text>
    <text x="12" y="122" font-size="10.5" font-weight="600" fill="#374151">• Cloudflare R2 presign</text>
    <text x="12" y="140" font-size="10.5" font-weight="600" fill="#374151">• SVCE IT Dept adopted</text>
    <rect x="12" y="158" width="132" height="24" rx="4" fill="#ffffff" stroke="#121212" stroke-width="2"/>
    <text x="20" y="174" font-size="9.5" font-weight="800" fill="#121212">SHIPPED TO LIVE 🚀</text>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

def create_telemetry_monitor_svg(filepath):
    svg_content = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 120" width="100%" height="auto" style="max-width: 920px; font-family: -apple-system, BlinkMacSystemFont, Consolas, 'Courier New', monospace;">
  <defs>
    <filter id="tele-shadow" x="0%" y="0%" width="120%" height="120%">
      <feDropShadow dx="4" dy="4" stdDeviation="0" flood-color="#121212" flood-opacity="1"/>
    </filter>
  </defs>

  <!-- Main Container -->
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
    <text x="764" y="18" font-size="10" font-weight="800" fill="#4ade80">● ONLINE // CHENNAI</text>

    <!-- Content 3 Columns -->
    <!-- Col 1 -->
    <g transform="translate(18, 42)">
      <rect x="0" y="0" width="270" height="52" rx="4" fill="#1e1f26" stroke="#374151" stroke-width="1.5"/>
      <text x="12" y="20" font-size="10" font-weight="800" fill="#fde047" letter-spacing="0.5">CURRENT STATUS</text>
      <text x="12" y="38" font-size="12" font-weight="700" fill="#ffffff">Available for 2026 Roles</text>
      <circle cx="250" cy="26" r="4" fill="#4ade80"/>
    </g>

    <!-- Col 2 -->
    <g transform="translate(304, 42)">
      <rect x="0" y="0" width="280" height="52" rx="4" fill="#1e1f26" stroke="#374151" stroke-width="1.5"/>
      <text x="12" y="20" font-size="10" font-weight="800" fill="#ff90e8" letter-spacing="0.5">ACTIVE LEARNING TRACK</text>
      <text x="12" y="38" font-size="12" font-weight="700" fill="#ffffff">AWS Solutions Architect Cert</text>
      <circle cx="260" cy="26" r="4" fill="#ff90e8"/>
    </g>

    <!-- Col 3 -->
    <g transform="translate(600, 42)">
      <rect x="0" y="0" width="286" height="52" rx="4" fill="#1e1f26" stroke="#374151" stroke-width="1.5"/>
      <text x="12" y="20" font-size="10" font-weight="800" fill="#4ade80" letter-spacing="0.5">KEY ADOPTION MILESTONE</text>
      <text x="12" y="38" font-size="12" font-weight="700" fill="#ffffff">LeetBoard (SVCE IT Dept Adopted)</text>
      <circle cx="266" cy="26" r="4" fill="#fde047"/>
    </g>
  </g>
</svg>"""
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg_content.strip())
    print(f"Created {filepath}")

if __name__ == "__main__":
    create_build_pipeline_svg("assets/build-pipeline.svg")
    create_telemetry_monitor_svg("assets/system-status.svg")
