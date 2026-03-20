"""
Canva Designer — Test Deck
Demonstrates all major slide types using CanvaSlideGenerator.
Themed as a "Build with Canva Connect" developer pitch.

Run from this directory:
    python test_deck.py
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))
from generator import CanvaSlideGenerator

gen = CanvaSlideGenerator("Build with Canva Connect — Developer Pitch")

# 1. Title
gen.add_title_slide(
    title="Build with Canva",
    subtitle="Enterprise-grade design automation via Connect API",
    author="Developer Relations",
    badge="Connect API",
    show_powered_by=True,
)

# 2. Section
gen.add_section_slide(
    title="The Opportunity",
    subtitle="Design is the last mile of every workflow",
    color="purple",
)

# 3. Badge slide — problem framing
gen.add_badge_slide(
    badge_label="THE PROBLEM",
    title="Design is a Bottleneck",
    bullets=[
        "Marketing teams wait days for on-brand assets",
        "Inconsistent visuals undermine brand equity",
        "Agency costs eat into margins for routine content",
        "Manual processes don't scale with business growth",
    ],
    subtitle="Every company faces this — Canva solves it at the API layer",
)

# 4. Hero stat
gen.add_hero_stat_slide(
    title="The Design Economy",
    number="$58B",
    label="Global design software market by 2027",
    sublabel="CAGR 13.2% — Canva is the platform of record",
    badge="Market Size",
)

# 5. Flow — how it works
gen.add_flow_slide(
    title="How Canva Connect Works",
    steps=["Authenticate", "Sync Brand Kit", "Apply Templates", "Generate Assets", "Export & Distribute"],
    badge="Integration",
    subtitle="5-step setup — production-ready in hours",
    accent_last=True,
)

# 6. Stat grid
gen.add_stat_slide(
    title="Platform at Scale",
    stats=[
        {"number": "500M+", "label": "Monthly Active Users", "icon": "👥"},
        {"number": "190+", "label": "Countries", "icon": "🌏"},
        {"number": "15B+", "label": "Designs Created", "icon": "🎨"},
        {"number": "4,000+", "label": "Templates", "icon": "📐"},
    ],
    badge="Scale",
    columns=4,
)

# 7. Feature grid
gen.add_feature_grid_slide(
    title="Core API Capabilities",
    features=[
        {"title": "Brand Kit API", "description": "Enforce brand colors, fonts, and logos across all auto-generated designs.", "icon": "🎨"},
        {"title": "Template Engine", "description": "Populate Canva templates programmatically with dynamic data.", "icon": "⚡"},
        {"title": "Asset Sync", "description": "Bidirectional sync between your DAM and Canva asset library.", "icon": "🔄"},
        {"title": "Export API", "description": "Output finished designs as PNG, PDF, MP4 or SVG on demand.", "icon": "📤"},
    ],
    badge="Features",
    columns=2,
)

# 8. Comparison
gen.add_comparison_slide(
    title="Before vs After Canva Connect",
    left={
        "title": "Manual Process",
        "items": [
            "Designer bottleneck for every asset",
            "Days to produce campaign materials",
            "Inconsistent brand application",
            "High agency & freelancer costs",
            "No programmatic control",
        ],
    },
    right={
        "title": "With Canva Connect",
        "items": [
            "Self-serve via API, no designer needed",
            "Assets generated in seconds",
            "Brand-locked templates enforce consistency",
            "Reduce production costs by 60–80%",
            "Full programmatic control & audit trail",
        ],
    },
    badge="Value Prop",
)

# 9. Bar chart
gen.add_bar_chart_slide(
    title="Time to Publish: Before vs After",
    data=[
        {"label": "Campaign Brief", "value": 2},
        {"label": "Design Production", "value": 72},
        {"label": "Brand Review", "value": 24},
        {"label": "Revisions", "value": 48},
        {"label": "With Canva Connect", "value": 3},
    ],
    badge="Efficiency",
    subtitle="Hours from brief to published asset",
)

# 10. Phase cards — roadmap
gen.add_phase_cards_slide(
    title="Integration Roadmap",
    phases=[
        {"label": "Week 1–2", "title": "API Setup", "description": "Authenticate, configure Brand Kit, run quickstart demo."},
        {"label": "Week 3–4", "title": "Template Build", "description": "Create your template library with locked brand elements."},
        {"label": "Month 2", "title": "DAM Integration", "description": "Connect your asset management system bidirectionally."},
        {"label": "Month 3", "title": "Team Rollout", "description": "Onboard content teams, train on self-serve workflows."},
    ],
    badge="Roadmap",
)

# 11. Timeline — Canva history
gen.add_timeline_slide(
    title="Canva's Journey",
    milestones=[
        {"date": "2013", "title": "Founded", "description": "Launched in Sydney by Melanie Perkins."},
        {"date": "2019", "title": "100M Users", "description": "Crossed 100 million registered users globally."},
        {"date": "2021", "title": "$40B Valuation", "description": "Became one of the world's most valuable startups."},
        {"date": "2023", "title": "Connect API Beta", "description": "Enterprise integration platform opens to developers."},
        {"date": "2024", "title": "Connect API GA", "description": "General availability — production integrations open."},
    ],
    badge="Milestones",
)

# 12. Quote
gen.add_quote_slide(
    quote="Canva Connect has transformed how we deliver branded content to 200 markets simultaneously. What used to take our team three weeks now happens overnight.",
    author="Sarah Chen",
    role="VP Marketing Operations, Fortune 500",
    badge="Testimonial",
)

# 13. Two-column — technical architecture
gen.add_two_col_slide(
    title="Technical Architecture",
    left_content="""
        <div style="text-align:left; width:100%;">
            <h4 style="color:#8B3DFF; text-align:left;">Your Stack</h4>
            <ul>
                <li>Any language / framework</li>
                <li>REST API — OpenAPI spec</li>
                <li>OAuth 2.0 authentication</li>
                <li>Webhook events</li>
                <li>SDK generators available</li>
            </ul>
        </div>
    """,
    right_content="""
        <div style="text-align:left; width:100%;">
            <h4 style="color:#00C4CC; text-align:left;">Canva Platform</h4>
            <ul>
                <li>Brand Kit enforcement</li>
                <li>Template rendering engine</li>
                <li>Asset storage & CDN</li>
                <li>Collaboration layer</li>
                <li>Export pipeline</li>
            </ul>
        </div>
    """,
    badge="Developer",
)

# 14. Closing stat
gen.add_stat_slide(
    title="What Partners Achieve",
    stats=[
        {"number": "80%", "label": "Reduction in design costs"},
        {"number": "50×", "label": "Faster asset production"},
        {"number": "100%", "label": "Brand consistency score"},
    ],
    badge="Results",
    columns=3,
)

# 15. Thank you
gen.add_thank_you_slide(
    title="Start Building Today",
    subtitle="Join 10,000+ developers building on Canva Connect",
    contact={
        "Docs": "canva.dev/docs/connect",
        "Quickstart": "canva.dev/docs/connect/quickstart",
        "Contact": "connect@canva.com",
    },
    show_powered_by=True,
)

# Save
result = gen.save("canva-connect-demo.html", folder=os.path.join(os.path.dirname(__file__), "presentations"))
print(f"✓ Generated: {result['path']}")
print(f"  Slides: {result['slides']}")
print(f"  Size:   {result['size_kb']} KB")
