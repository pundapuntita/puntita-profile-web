import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # Set 16:9 widescreen layout
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Theme Colors
    COLOR_BG = RGBColor(248, 250, 252)       # Light Slate #f8fafc
    COLOR_CARD = RGBColor(255, 255, 255)     # White #ffffff
    COLOR_PRIMARY = RGBColor(15, 23, 42)     # Deep Slate #0f172a
    COLOR_SECONDARY = RGBColor(71, 85, 105)  # Muted Slate #475569
    COLOR_BLUE = RGBColor(2, 132, 199)       # Accent Blue #0284c7
    COLOR_DARK_BLUE = RGBColor(3, 105, 161)  # Dark Blue #0369a1
    COLOR_TEAL = RGBColor(13, 148, 136)      # Teal #0d9488
    COLOR_GREEN = RGBColor(5, 150, 105)      # Emerald #059669
    COLOR_LIGHT_GREEN = RGBColor(240, 253, 244) # #f0fdf4
    COLOR_BORDER_GREEN = RGBColor(167, 243, 208) # #a7f3d0
    COLOR_PURPLE = RGBColor(107, 33, 168)    # Purple #6b21a8
    COLOR_LIGHT_PURPLE = RGBColor(250, 245, 255) # #faf5ff
    COLOR_BORDER = RGBColor(226, 232, 240)   # Border #e2e8f0

    def add_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG
        bg.line.fill.background()
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text=""):
        # Tag pill
        tag_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.5), Inches(2.8), Inches(0.38))
        tag_box.fill.solid()
        tag_box.fill.fore_color.rgb = RGBColor(224, 242, 254)
        tag_box.line.color.rgb = RGBColor(186, 230, 253)
        tf = tag_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = tag_text
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_DARK_BLUE
        p.alignment = PP_ALIGN.CENTER

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.95), Inches(11.7), Inches(0.65))
        tf = title_box.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_text
        p.font.size = Pt(24)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY

        # Subtitle
        if subtitle_text:
            sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.55), Inches(11.7), Inches(0.45))
            tf = sub_box.text_frame
            tf.word_wrap = True
            p = tf.paragraphs[0]
            p.text = subtitle_text
            p.font.size = Pt(13)
            p.font.color.rgb = COLOR_SECONDARY

    # ==========================================
    # SLIDE 1: Title & Academic Profile
    # ==========================================
    slide1 = prs.slides.add_slide(blank_layout)
    add_background(slide1)

    # Top Tag
    tag = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(0.8), Inches(3.2), Inches(0.4))
    tag.fill.solid()
    tag.fill.fore_color.rgb = RGBColor(224, 242, 254)
    tag.line.color.rgb = RGBColor(186, 230, 253)
    p = tag.text_frame.paragraphs[0]
    p.text = "EXECUTIVE RESEARCH BRIEF"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_DARK_BLUE
    p.alignment = PP_ALIGN.CENTER

    # Name Title
    name_box = slide1.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(8.5), Inches(0.9))
    p = name_box.text_frame.paragraphs[0]
    p.text = "Dr. Puntita Sae-Jia"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    # Position & Affiliation
    pos_box = slide1.shapes.add_textbox(Inches(0.8), Inches(2.25), Inches(8.5), Inches(0.8))
    tf = pos_box.text_frame
    p1 = tf.paragraphs[0]
    p1.text = "Lecturer in Mathematics Education"
    p1.font.size = Pt(18)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_BLUE

    p2 = tf.add_paragraph()
    p2.text = "School of Science, Walailak University • Ph.D. in Mathematics"
    p2.font.size = Pt(14)
    p2.font.color.rgb = COLOR_SECONDARY

    # Specialization Chips
    chips = ["Convex Bilevel Optimization", "Split Variational Inclusions", "Machine Learning & AI", "Health Data Analytics"]
    left_pos = Inches(0.8)
    for chip in chips:
        c_box = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, Inches(3.2), Inches(2.1), Inches(0.35))
        c_box.fill.solid()
        c_box.fill.fore_color.rgb = RGBColor(241, 245, 249)
        c_box.line.color.rgb = COLOR_BORDER
        p = c_box.text_frame.paragraphs[0]
        p.text = chip
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_SECONDARY
        p.alignment = PP_ALIGN.CENTER
        left_pos += Inches(2.2)

    # 3 Stat Metric Cards
    metrics = [
        ("PUBLICATIONS", "6", "Peer-Reviewed (Q1 Tier)"),
        ("H-INDEX", "3", "Scopus / Web of Science"),
        ("CITATIONS", "15", "International Citations")
    ]
    card_w = Inches(2.6)
    card_h = Inches(2.2)
    start_x = Inches(0.8)
    y_pos = Inches(4.0)

    for i, (label, val, desc) in enumerate(metrics):
        card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, start_x + (i * Inches(2.85)), y_pos, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1.5)

        tf = card.text_frame
        tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.text = label
        p1.font.size = Pt(12)
        p1.font.bold = True
        p1.font.color.rgb = COLOR_SECONDARY
        p1.alignment = PP_ALIGN.CENTER

        p2 = tf.add_paragraph()
        p2.text = val
        p2.font.size = Pt(46)
        p2.font.bold = True
        p2.font.color.rgb = COLOR_BLUE
        p2.alignment = PP_ALIGN.CENTER

        p3 = tf.add_paragraph()
        p3.text = desc
        p3.font.size = Pt(10.5)
        p3.font.color.rgb = COLOR_SECONDARY
        p3.alignment = PP_ALIGN.CENTER

    # Right Card: Interactive Profile QR Code & Contact
    right_card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(1.35), Inches(2.7), Inches(4.85))
    right_card.fill.solid()
    right_card.fill.fore_color.rgb = COLOR_CARD
    right_card.line.color.rgb = COLOR_BORDER
    right_card.line.width = Pt(1.5)

    tf = right_card.text_frame
    p = tf.paragraphs[0]
    p.text = "Interactive Profile"
    p.font.size = Pt(14)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.alignment = PP_ALIGN.CENTER

    if os.path.exists("qrcode.png"):
        slide1.shapes.add_picture("qrcode.png", Inches(10.25), Inches(2.1), width=Inches(1.8), height=Inches(1.8))

    qr_sub = slide1.shapes.add_textbox(Inches(9.9), Inches(4.1), Inches(2.5), Inches(1.8))
    tf = qr_sub.text_frame
    tf.word_wrap = True
    p1 = tf.paragraphs[0]
    p1.text = "Scan to visit online portfolio\nand test live application."
    p1.font.size = Pt(11)
    p1.font.color.rgb = COLOR_SECONDARY
    p1.alignment = PP_ALIGN.CENTER

    p2 = tf.add_paragraph()
    p2.text = "\nEmail: puntita.sa@wu.ac.th"
    p2.font.size = Pt(11)
    p2.font.bold = True
    p2.font.color.rgb = COLOR_BLUE
    p2.alignment = PP_ALIGN.CENTER


    # ==========================================
    # SLIDE 2: Mathematical Problems (Bilevel & Split)
    # ==========================================
    slide2 = prs.slides.add_slide(blank_layout)
    add_background(slide2)
    add_header(
        slide2,
        "THEORETICAL FOUNDATION",
        "Convex Bilevel Optimization & Split Inclusions",
        "Published in Journal of Computational and Applied Mathematics (Volume 488, 117823, May 2026 • Q1 Tier)"
    )

    # Card 1: Bilevel Optimization Model
    bilevel_card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.7), Inches(4.5))
    bilevel_card.fill.solid()
    bilevel_card.fill.fore_color.rgb = COLOR_LIGHT_PURPLE
    bilevel_card.line.color.rgb = RGBColor(216, 180, 254)
    bilevel_card.line.width = Pt(1.5)

    tf = bilevel_card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Convex Bilevel Optimization Model"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_PURPLE

    p = tf.add_paragraph()
    p.text = "\nOuter-Level Problem:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    p = tf.add_paragraph()
    p.text = "min { φ(x)  such that  x ∈ Γ }"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_PURPLE

    p = tf.add_paragraph()
    p.text = "\nInner-Level Problem (Constraint Set Γ):"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    p = tf.add_paragraph()
    p.text = "argmin { f(x) + g(x)  over  x ∈ H }"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_PURPLE

    p = tf.add_paragraph()
    p.text = "\nKey Properties:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    p = tf.add_paragraph()
    p.text = "• φ: H → ℝ is strongly convex and differentiable (parameter σ > 0).\n• Solves hierarchical inverse decision and machine learning objectives.\n• Models high-dimensional regularized sparse recovery."
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_SECONDARY

    # Card 2: Split Variational Inclusion Problem (SVIP)
    svip_card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.2), Inches(5.7), Inches(4.5))
    svip_card.fill.solid()
    svip_card.fill.fore_color.rgb = RGBColor(240, 249, 255)
    svip_card.line.color.rgb = RGBColor(186, 230, 253)
    svip_card.line.width = Pt(1.5)

    tf = svip_card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "2. Split Variational Inclusion Problem (SVIP)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_DARK_BLUE

    p = tf.add_paragraph()
    p.text = "\nMathematical Formulation:"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    p = tf.add_paragraph()
    p.text = "Find x* ∈ H₁ such that:\n0 ∈ (A₁ + B₁)(x*)   and   0 ∈ (A₂ + B₂)(Lx*)"
    p.font.size = Pt(14.5)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE

    p = tf.add_paragraph()
    p.text = "\nOperator Characteristics:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    p = tf.add_paragraph()
    p.text = "• L: H₁ → H₂ is a bounded linear operator (e.g. system blur matrix).\n• A₁, A₂ are inverse-strongly monotone operators.\n• B₁, B₂ are maximal monotone operators (non-smooth regularization).\n• Eliminates costly precomputation of operator norm ‖L‖."
    p.font.size = Pt(11)
    p.font.color.rgb = COLOR_SECONDARY


    # ==========================================
    # SLIDE 3: Proposed Algorithm 8 (DIVFB)
    # ==========================================
    slide3 = prs.slides.add_slide(blank_layout)
    add_background(slide3)
    add_header(
        slide3,
        "CORE ALGORITHMIC INNOVATION",
        "Algorithm 8: Double Inertial Viscosity Forward-Backward Scheme",
        "A strongly convergent accelerated splitting framework for convex bilevel and split problems"
    )

    # Algorithm Academic Container Box
    algo_box = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(11.7), Inches(4.7))
    algo_box.fill.solid()
    algo_box.fill.fore_color.rgb = COLOR_CARD
    algo_box.line.color.rgb = COLOR_PRIMARY
    algo_box.line.width = Pt(2)

    tf = algo_box.text_frame
    tf.word_wrap = True
    
    # Title line
    p = tf.paragraphs[0]
    p.text = "Algorithm 8: Double Inertial Viscosity Forward-Backward Algorithm (DIVFB)"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    # Initialization
    p = tf.add_paragraph()
    p.text = "Initialization: Choose x₁, x₀, x₋₁ ∈ H, λₙ ∈ (0, 1/‖L‖²), {rₙ} ⊂ (0, β], {βₙ} ⊂ (0, 1). Take {ξₙ}, {μₙ} ⊂ (0, ∞) and {ρₙ} ⊂ (-∞, 0)."
    p.font.size = Pt(11.5)
    p.font.color.rgb = COLOR_SECONDARY

    # Iterative Steps
    p = tf.add_paragraph()
    p.text = "\nIterative Steps: For n ≥ 1, compute xₙ₊₁ via:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    steps = [
        ("Step 1 (Inertial Steps):", "θₙ = min { μₙ,  ξₙ / ‖xₙ - xₙ₋₁‖ }  if xₙ ≠ xₙ₋₁ (else μₙ);     δₙ = max { ρₙ,  -ξₙ / ‖xₙ₋₁ - xₙ₋₂‖ }  if xₙ₋₁ ≠ xₙ₋₂ (else ρₙ)"),
        ("Step 2 (Double Inertial Step):", "wₙ = xₙ + θₙ(xₙ - xₙ₋₁) + δₙ(xₙ₋₁ - xₙ₋₂)"),
        ("Step 3 (Forward-Backward Resolvent):", "yₙ = J_{rₙ}^{A₁, B₁} [ wₙ - λₙ L* (I - J_{rₙ}^{A₂, B₂}) L wₙ ]"),
        ("Step 4 (Second Splitting Stage):", "zₙ = J_{rₙ}^{A₁, B₁} [ yₙ - λₙ L* (I - J_{rₙ}^{A₂, B₂}) L yₙ ]"),
        ("Step 5 (Viscosity Approximation):", "xₙ₊₁ = βₙ F(xₙ) + (1 - βₙ) zₙ")
    ]

    for title, formula in steps:
        p = tf.add_paragraph()
        p.text = f"• {title}  {formula}"
        p.font.size = Pt(11)
        p.font.color.rgb = COLOR_DARK_BLUE

    # Theorem Box inside
    p = tf.add_paragraph()
    p.text = "\nTHEORETICAL CONVERGENCE THEOREM:"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_GREEN

    p = tf.add_paragraph()
    p.text = "Under standard control conditions, the sequence {xₙ} generated by Algorithm 8 is mathematically proven to converge STRONGLY to a solution of the convex bilevel and split variational inclusion problem."
    p.font.size = Pt(11.5)
    p.font.bold = True
    p.font.color.rgb = RGBColor(6, 95, 70)


    # ==========================================
    # SLIDE 4: Clinical Impact & Image Restoration
    # ==========================================
    slide4 = prs.slides.add_slide(blank_layout)
    add_background(slide4)
    add_header(
        slide4,
        "REAL-WORLD MEDICAL IMPACT",
        "Clinical Dataset Classification & Image Restoration",
        "Empirical evaluation proving algorithmic superiority over benchmark first-order methods"
    )

    # Card 1: Hypertension Dataset
    card_hyp = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(5.7), Inches(4.7))
    card_hyp.fill.solid()
    card_hyp.fill.fore_color.rgb = COLOR_LIGHT_GREEN
    card_hyp.line.color.rgb = COLOR_BORDER_GREEN
    card_hyp.line.width = Pt(1.5)

    tf = card_hyp.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "1. Hypertension Clinical Dataset"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_GREEN

    p = tf.add_paragraph()
    p.text = "Sriphat Hospital, Chiang Mai (6,108 cases)\n"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_SECONDARY

    # Big Accuracy Box
    stat_box1 = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.3), Inches(3.2), Inches(4.7), Inches(1.5))
    stat_box1.fill.solid()
    stat_box1.fill.fore_color.rgb = COLOR_CARD
    stat_box1.line.color.rgb = COLOR_BORDER_GREEN
    stat_box1.line.width = Pt(1.5)

    tf1 = stat_box1.text_frame
    p = tf1.paragraphs[0]
    p.text = "TEST ACCURACY (TABLE 11)"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_SECONDARY
    p.alignment = PP_ALIGN.CENTER

    p = tf1.add_paragraph()
    p.text = "88.03%"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY
    p.alignment = PP_ALIGN.CENTER

    desc_hyp = slide4.shapes.add_textbox(Inches(1.1), Inches(4.9), Inches(5.1), Inches(1.8))
    tf = desc_hyp.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Key Findings & Superiority:\n• Achieved 88.03% test accuracy (Table 11).\n• Evaluated across multiple comprehensive metrics (Precision, Recall, and F1-Score).\n• Exhibited superior diagnostic stability and noise robustness compared to existing BiG-SAM baselines."
    p.font.size = Pt(11.5)
    p.font.color.rgb = COLOR_SECONDARY

    # Card 2: Medical Image Deblurring
    card_img = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(2.2), Inches(5.7), Inches(4.7))
    card_img.fill.solid()
    card_img.fill.fore_color.rgb = RGBColor(240, 249, 255)
    card_img.line.color.rgb = RGBColor(186, 230, 253)
    card_img.line.width = Pt(1.5)

    tf = card_img.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "2. Medical Image Restoration (Deblurring)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_DARK_BLUE

    p = tf.add_paragraph()
    p.text = "CT Scans, MRI, and Radiology Benchmarks\n"
    p.font.size = Pt(12)
    p.font.bold = True
    p.font.color.rgb = COLOR_SECONDARY

    # 2 Metrics: PSNR and SSIM
    psnr_box = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.2), Inches(3.2), Inches(2.3), Inches(1.1))
    psnr_box.fill.solid()
    psnr_box.fill.fore_color.rgb = COLOR_CARD
    psnr_box.line.color.rgb = RGBColor(186, 230, 253)
    tf = psnr_box.text_frame
    p = tf.paragraphs[0]
    p.text = "PSNR (TABLE 8)"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_SECONDARY
    p.alignment = PP_ALIGN.CENTER
    p = tf.add_paragraph()
    p.text = "26.1291"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE
    p.alignment = PP_ALIGN.CENTER

    ssim_box = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(9.8), Inches(3.2), Inches(2.3), Inches(1.1))
    ssim_box.fill.solid()
    ssim_box.fill.fore_color.rgb = COLOR_CARD
    ssim_box.line.color.rgb = RGBColor(186, 230, 253)
    tf = ssim_box.text_frame
    p = tf.paragraphs[0]
    p.text = "SSIM (TABLE 8)"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_SECONDARY
    p.alignment = PP_ALIGN.CENTER
    p = tf.add_paragraph()
    p.text = "0.8806"
    p.font.size = Pt(22)
    p.font.bold = True
    p.font.color.rgb = COLOR_TEAL
    p.alignment = PP_ALIGN.CENTER

    # Before & After Images
    if os.path.exists("blurred.jpeg"):
        slide4.shapes.add_picture("blurred.jpeg", Inches(7.4), Inches(4.5), width=Inches(1.8), height=Inches(1.8))
        b_label = slide4.shapes.add_textbox(Inches(7.4), Inches(6.35), Inches(1.8), Inches(0.4))
        p = b_label.text_frame.paragraphs[0]
        p.text = "Blurred Input"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = RGBColor(153, 27, 27)
        p.alignment = PP_ALIGN.CENTER

    # Arrow
    arrow_box = slide4.shapes.add_textbox(Inches(9.25), Inches(5.1), Inches(0.8), Inches(0.6))
    p = arrow_box.text_frame.paragraphs[0]
    p.text = "➔"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = COLOR_BLUE
    p.alignment = PP_ALIGN.CENTER

    if os.path.exists("Algorithm9.png"):
        slide4.shapes.add_picture("Algorithm9.png", Inches(10.1), Inches(4.5), width=Inches(1.8), height=Inches(1.8))
        r_label = slide4.shapes.add_textbox(Inches(10.1), Inches(6.35), Inches(1.8), Inches(0.4))
        p = r_label.text_frame.paragraphs[0]
        p.text = "Restored (Algo 9)"
        p.font.size = Pt(10)
        p.font.bold = True
        p.font.color.rgb = COLOR_GREEN
        p.alignment = PP_ALIGN.CENTER


    # ==========================================
    # SLIDE 5: Translation & Hypertension Web App
    # ==========================================
    slide5 = prs.slides.add_slide(blank_layout)
    add_background(slide5)
    add_header(
        slide5,
        "HEALTHCARE DIGITAL TRANSLATION",
        "Hypertension Predictor Web Application",
        "Translating mathematical modeling and machine learning into operational diagnostic software"
    )

    # Left Column: Web App Overview & Features
    app_card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(2.2), Inches(6.0), Inches(4.7))
    app_card.fill.solid()
    app_card.fill.fore_color.rgb = COLOR_CARD
    app_card.line.color.rgb = COLOR_BORDER
    app_card.line.width = Pt(1.5)

    tf = app_card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Software Innovation & Public Health Screening"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY

    features = [
        ("Clinical Decision Support:", "Predicts hypertension risk levels in seconds based on patient vitals and health indicators."),
        ("Intellectual Property:", "Registered copyright application pending for predictive diagnostic algorithm."),
        ("Community Integration:", "Field-tested with Village Health Volunteers (VHVs) in northern public health programs."),
        ("Edge Computing Ready:", "100% on-device client processing ensuring strict medical patient data privacy."),
        ("Live Deployment:", "https://hypertension-webapp-indol.vercel.app")
    ]

    for title, desc in features:
        p = tf.add_paragraph()
        p.text = f"\n• {title} {desc}"
        p.font.size = Pt(11.5)
        p.font.color.rgb = COLOR_SECONDARY

    # Right Column: Leadership & Institutional Value
    exec_card = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.1), Inches(2.2), Inches(5.4), Inches(4.7))
    exec_card.fill.solid()
    exec_card.fill.fore_color.rgb = COLOR_LIGHT_GREEN
    exec_card.line.color.rgb = COLOR_BORDER_GREEN
    exec_card.line.width = Pt(1.5)

    tf = exec_card.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = "Strategic Value for University Leadership"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_GREEN

    takeaways = [
        ("Academic Excellence:", "Demonstrates Walailak University's high-caliber research capacity in international Q1 journals."),
        ("Interdisciplinary Synergy:", "Bridges pure mathematics, data science, and clinical medicine to tackle National Health priorities (NCDs)."),
        ("Grant & Innovation Potential:", "Strong pipeline for commercialization, national research funding (TSRI / NRCT), and health technology patents."),
        ("Educational Leadership:", "Empowering mathematics students with applied coding, optimization, and AI skills for the modern workforce.")
    ]

    for title, desc in takeaways:
        p = tf.add_paragraph()
        p.text = f"\n✓ {title} {desc}"
        p.font.size = Pt(12)
        p.font.color.rgb = RGBColor(6, 95, 70)

    # Save presentation
    output_filename = "Executive_Presentation_Puntita.pptx"
    prs.save(output_filename)
    print(f"Presentation saved successfully as '{output_filename}'.")

if __name__ == "__main__":
    create_deck()
