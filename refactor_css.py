import re

file_path = 'src/styles.css'

with open(file_path, 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Typography Clamps
css = re.sub(r'font-size:\s*clamp\([^)]+\);', r'font-size: clamp(2.2rem, 7vw, 4.5rem);', css, count=1) # The hero title specifically
css = re.sub(r'(?<!@media(?:\s|\())(?<!-)font-size:\s*2\.5rem;', r'font-size: clamp(1.8rem, 5vw, 2.5rem);', css)
css = re.sub(r'(?<!@media(?:\s|\())(?<!-)font-size:\s*3rem;', r'font-size: clamp(2.2rem, 6vw, 3rem);', css)
css = re.sub(r'(?<!@media(?:\s|\())(?<!-)font-size:\s*1\.5rem;', r'font-size: clamp(1.2rem, 3vw, 1.5rem);', css)

# 2. Spacing Clamps
css = re.sub(r'padding:\s*2\.5rem;', r'padding: clamp(1.25rem, 4vw, 2.5rem);', css)
css = re.sub(r'padding:\s*3rem;', r'padding: clamp(1.5rem, 5vw, 3rem);', css)
css = re.sub(r'gap:\s*3rem;', r'gap: clamp(1.5rem, 4vw, 3rem);', css)
css = re.sub(r'gap:\s*2rem;', r'gap: clamp(1rem, 3vw, 2rem);', css)
css = re.sub(r'margin:\s*4rem\s+auto;', r'margin: clamp(2rem, 5vw, 4rem) auto;', css)

# 3. Dynamic Container Widths
css = css.replace('.hero-section {\n    max-width: 860px;', '.hero-section {\n    width: min(90%, 860px);')
css = css.replace('.about-content {\n    display: grid;\n    grid-template-columns: 1fr;\n    gap: 2rem;\n    max-width: 860px;', 
                  '.about-content {\n    display: grid;\n    grid-template-columns: 1fr;\n    gap: clamp(1.5rem, 4vw, 2rem);\n    width: min(90%, 860px);')
css = css.replace('.faq-section {\n    max-width: 860px;', '.faq-section {\n    width: min(90%, 860px);')

# 4. Strip out redundant mobile overrides that are now handled by clamp
# Hero/About overrides that are no longer needed
red1 = """    .hero-title {
        font-size: 2.2rem !important;
    }

    .hero-subtitle {
        font-size: 1.1rem !important;
    }

    .glass-card, section, .section, .imprint-card, .links-card, .schedule-card, .stat-card, .artist-card, .card, .artist-card-full {
        padding: 1.25rem !important;
        margin: 1.5rem 0 !important;
    }

    .about-text {
        padding: 1.25rem !important;
    }

    .stat-number {
        font-size: 2.2rem !important;
    }"""
css = css.replace(red1, "")

# Remove specific h2 resizes in the 768 media block
red2 = """    /* Überschriften verkleinern, damit sie nicht über den Rand schießen */
    .hero-text h2,
    .about-text h2 {
        font-size: 1.8rem !important;
        word-wrap: break-word;
        /* Bricht zu lange Wörter (wie 'Nhywyll') zur Not um */
    }"""
# Let's keep word-wrap but not the font-size override since clamp handles it
rep2 = """    /* Überschriften verhalten sich nun fluide dank clamp, aber word-wrap bleibt zur Sicherheit */
    .hero-text h2,
    .about-text h2 {
        word-wrap: break-word;
    }"""
css = css.replace(red2, rep2)

red3 = """    .hero h2 {
        font-size: 2.2rem;
    }"""
css = css.replace(red3, "")

red4 = """    .section-title {
        font-size: 2rem;
        margin-bottom: 2rem;
    }"""
css = css.replace(red4, """    .section-title {
        margin-bottom: 2rem;
    }""")

# 5. Fix badge sizing for accessibility using clamp instead of !important fixed sizes
badge_block_old = """.hero-badges {
        flex-wrap: nowrap !important;
        justify-content: center !important;
        gap: 0.4rem !important;
        width: 100%;
    }

    .badge {
        padding: 0.4rem 0.6rem !important;
        font-size: 0.7rem !important;
        text-align: center;
        flex: 0 1 auto;
        white-space: nowrap;
    }"""

badge_block_new = """.hero-badges {
        flex-wrap: nowrap !important;
        justify-content: center !important;
        gap: clamp(0.2rem, 1vw, 0.5rem) !important;
        width: 100%;
    }

    .badge {
        padding: clamp(0.3rem, 1vw, 0.6rem) clamp(0.4rem, 1.5vw, 1rem) !important;
        font-size: clamp(0.6rem, 2.5vw, 0.85rem) !important;
        text-align: center;
        flex: 0 1 auto;
        white-space: nowrap;
    }"""
css = css.replace(badge_block_old, badge_block_new)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(css)

print("Fluid CSS update applied successfully.")
