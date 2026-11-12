"""
Generates a complete, professional Cybersecurity Solutions Lead CV in PDF format
for testing and uploading into the Viraya Interview AI Bot application.
"""
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable, KeepTogether
)

def build_pdf(filename="cybersecurity_cv.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    # Custom styles
    primary_color = colors.HexColor("#0F294A")  # Deep Navy
    secondary_color = colors.HexColor("#1E40AF") # Blue Accent
    dark_neutral = colors.HexColor("#1E293B")    # Slate 800
    subtle_neutral = colors.HexColor("#475569")  # Slate 600
    border_color = colors.HexColor("#CBD5E1")    # Slate 300

    name_style = ParagraphStyle(
        "CandidateName",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        textColor=primary_color,
        alignment=0
    )

    title_style = ParagraphStyle(
        "CandidateTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=15,
        textColor=secondary_color,
        alignment=0
    )

    contact_style = ParagraphStyle(
        "ContactInfo",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=subtle_neutral,
        alignment=0
    )

    section_heading = ParagraphStyle(
        "SectionHeading",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        textColor=primary_color,
        spaceBefore=8,
        spaceAfter=3,
        keepWithNext=True
    )

    job_title_style = ParagraphStyle(
        "JobTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=9.5,
        leading=12.5,
        textColor=dark_neutral
    )

    job_meta_style = ParagraphStyle(
        "JobMeta",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=8.5,
        leading=11.5,
        textColor=subtle_neutral
    )

    body_style = ParagraphStyle(
        "BodyDark",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=12,
        textColor=dark_neutral,
        spaceAfter=3
    )

    bullet_style = ParagraphStyle(
        "BulletText",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=8.5,
        leading=11.5,
        textColor=dark_neutral,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=2.5
    )

    story = []

    # 1. Header (Name, Title, Contact)
    story.append(Paragraph("MATHAN KUMAR G", name_style))
    story.append(Paragraph("CYBERSECURITY SOLUTIONS LEAD &bull; TECHNICAL DELIVERY &amp; PRESALES", title_style))
    story.append(Spacer(1, 3))
    
    contact_text = (
        "<b>Email:</b> mathanmsecit@gmail.com &nbsp;|&nbsp; "
        "<b>Phone:</b> +91 98765 43210 &nbsp;|&nbsp; "
        "<b>Location:</b> Bangalore, India &nbsp;|&nbsp; "
        "<b>LinkedIn:</b> linkedin.com/in/mathankumar-sec &nbsp;|&nbsp; "
        "<b>GitHub:</b> github.com/mathankumar-cyber"
    )
    story.append(Paragraph(contact_text, contact_style))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=primary_color, spaceBefore=2, spaceAfter=6))

    # 2. Executive Summary
    story.append(Paragraph("EXECUTIVE SUMMARY", section_heading))
    summary_text = (
        "High-impact, hands-on <b>Cybersecurity Solutions Lead</b> with <b>6+ years of specialized experience</b> in "
        "Technical Delivery, Vulnerability Assessment &amp; Penetration Testing (VAPT), Cloud Security Architecture, and Presales Engineering. "
        "Proven expertise across the complete security engagement lifecycle: conducting discovery calls with prospective client CTOs/CISOs, "
        "architecting tailored scopes of work (SOWs) and effort estimations, delivering live technical proof-of-concept demonstrations, "
        "and leading cross-functional delivery teams to uncover high-severity vulnerabilities. Deep technical mastery in web application, "
        "REST API, network, and multi-cloud security (AWS/Azure) coupled with the commercial ability to translate complex attack vectors "
        "into clear business risks and pragmatic remediation roadmaps."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=border_color, spaceBefore=4, spaceAfter=6))

    # 3. Core Competencies & Technical Skills (Table format)
    story.append(Paragraph("CORE COMPETENCIES &amp; TECHNICAL SKILLS", section_heading))
    
    skills_data = [
        [
            Paragraph("<b>Offensive Security &amp; VAPT:</b>", body_style),
            Paragraph("Web Application VAPT (OWASP Top 10), REST API Security (OWASP API Top 10), Network Penetration Testing, Cloud Security Reviews, Red Teaming, Phishing Simulation Programs.", body_style)
        ],
        [
            Paragraph("<b>Security Toolset:</b>", body_style),
            Paragraph("Burp Suite Professional, Nmap, Nessus Professional, OpenVAS, Metasploit Framework, Wireshark, Postman, Nuclei, OWASP ZAP, SQLmap, Kali Linux.", body_style)
        ],
        [
            Paragraph("<b>Cloud &amp; Infrastructure:</b>", body_style),
            Paragraph("AWS Security (IAM, GuardDuty, CloudTrail, S3 bucket policy review, Security Hub), Azure Defender, Docker &amp; Kubernetes container security baselines.", body_style)
        ],
        [
            Paragraph("<b>Governance &amp; Frameworks:</b>", body_style),
            Paragraph("OWASP, ISO/IEC 27001:2022, NIST Cybersecurity Framework (CSF), CIS Critical Security Controls v8, CVSS v3.1 Severity Scoring, SOC 2 Type II audit readiness.", body_style)
        ],
        [
            Paragraph("<b>Presales &amp; Solutions:</b>", body_style),
            Paragraph("Client Discovery Consultations, Scope of Work (SOW) Authoring, Effort Estimation &amp; Pricing Models, Technical Proof-of-Concepts (PoCs), Handling Client Objections.", body_style)
        ],
        [
            Paragraph("<b>Automation &amp; Scripting:</b>", body_style),
            Paragraph("Python, Bash, PowerShell, REST API integrations, custom vulnerability reporting pipelines, and AI-assisted security workflow automation.", body_style)
        ],
    ]
    skills_table = Table(skills_data, colWidths=[150, 390])
    skills_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(skills_table)
    story.append(HRFlowable(width="100%", thickness=0.5, color=border_color, spaceBefore=4, spaceAfter=6))

    # 4. Professional Experience
    story.append(Paragraph("PROFESSIONAL EXPERIENCE", section_heading))

    # Job 1
    j1_header = [
        [
            Paragraph("<b>Cybersecurity Solutions Lead (Technical Delivery &amp; Presales)</b>", job_title_style),
            Paragraph("<b>Nov 2022 – Present</b>", ParagraphStyle("RightDate", parent=job_meta_style, alignment=2))
        ],
        [
            Paragraph("ThreatShield Cyber Solutions &bull; Bangalore, India", job_meta_style),
            Paragraph("Full-time", ParagraphStyle("RightType", parent=job_meta_style, alignment=2))
        ]
    ]
    t1 = Table(j1_header, colWidths=[380, 160])
    t1.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t1)
    story.append(Spacer(1, 2))

    j1_bullets = [
        "<b>Delivery Leadership:</b> Directed and executed 45+ end-to-end VAPT engagements across web applications, mobile APIs, and cloud environments for fintech, banking, and SaaS enterprise clients.",
        "<b>Presales &amp; Deal Closure:</b> Partnered with enterprise account executives on 30+ discovery calls, leading technical scoping and objection handling; achieved a 65% PoC-to-commercial contract conversion rate resulting in $1.4M+ ARR.",
        "<b>Vulnerability Triage &amp; Remediation:</b> Uncovered critical vulnerabilities including Broken Object Level Authorization (BOLA), unauthenticated Remote Code Execution (RCE), and authentication bypasses; authored remediation roadmaps prioritized by CVSS and business impact.",
        "<b>Cloud Security Reviews:</b> Led comprehensive AWS and Azure security posture reviews, auditing IAM policies, public storage exposures, and network security groups to achieve regulatory compliance.",
        "<b>Service Offering Development:</b> Productized cybersecurity service packages for API Penetration Testing, Phishing Simulation Campaigns, and ISO 27001 Pre-Audit Readiness, creating repeatable delivery playbooks."
    ]
    for b in j1_bullets:
        story.append(Paragraph(f"&bull; {b}", bullet_style))
    story.append(Spacer(1, 4))

    # Job 2
    j2_header = [
        [
            Paragraph("<b>Senior Security Assessment Consultant</b>", job_title_style),
            Paragraph("<b>Aug 2020 – Oct 2022</b>", ParagraphStyle("RightDate", parent=job_meta_style, alignment=2))
        ],
        [
            Paragraph("CyberMatrix Defense Technologies &bull; Hyderabad, India", job_meta_style),
            Paragraph("Full-time", ParagraphStyle("RightType", parent=job_meta_style, alignment=2))
        ]
    ]
    t2 = Table(j2_header, colWidths=[380, 160])
    t2.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t2)
    story.append(Spacer(1, 2))

    j2_bullets = [
        "<b>Penetration Testing:</b> Executed manual and automated security testing on 70+ applications using Burp Suite Pro, OWASP ZAP, and custom Python scripts, preventing critical data breach exposures prior to product launches.",
        "<b>Network &amp; Infrastructure Audits:</b> Conducted external and internal network vulnerability assessments using Nessus, OpenVAS, and Nmap across 2,000+ IP ranges and hybrid corporate infrastructure.",
        "<b>Client Reporting &amp; Executive Briefings:</b> Drafted high-clarity technical vulnerability reports and presented executive summaries to client management, demonstrating business risk and practical mitigation steps.",
        "<b>Delivery Automation:</b> Built a custom Python automation tool that aggregated Nessus XML and Burp Suite scanner results, slashing vulnerability triage and report generation turnaround by 40%."
    ]
    for b in j2_bullets:
        story.append(Paragraph(f"&bull; {b}", bullet_style))
    story.append(Spacer(1, 4))

    # Job 3
    j3_header = [
        [
            Paragraph("<b>Cybersecurity Analyst</b>", job_title_style),
            Paragraph("<b>June 2018 – July 2020</b>", ParagraphStyle("RightDate", parent=job_meta_style, alignment=2))
        ],
        [
            Paragraph("Infosys Cyber Defense Center &bull; Chennai, India", job_meta_style),
            Paragraph("Full-time", ParagraphStyle("RightType", parent=job_meta_style, alignment=2))
        ]
    ]
    t3 = Table(j3_header, colWidths=[380, 160])
    t3.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('PADDING', (0,0), (-1,-1), 0),
        ('BOTTOMPADDING', (0,0), (-1,-1), 1),
    ]))
    story.append(t3)
    story.append(Spacer(1, 2))

    j3_bullets = [
        "Monitored multi-tenant SIEM systems and endpoint detection tools; triaged real-time security alerts and coordinated incident containment workflows.",
        "Conducted quarterly vulnerability scans, baseline compliance assessments, and patch management verification for Linux and Windows server environments.",
        "Assisted in deploying simulated employee phishing awareness campaigns, analyzing user click rates, and facilitating targeted remediation training."
    ]
    for b in j3_bullets:
        story.append(Paragraph(f"&bull; {b}", bullet_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=border_color, spaceBefore=4, spaceAfter=6))

    # 5. Key Projects & Engagements
    story.append(Paragraph("KEY PROJECT ACHIEVEMENTS &amp; ENGAGEMENTS", section_heading))
    projects = [
        "<b>Enterprise Fintech Core Banking API Security Engagement (2024):</b> Led presales scoping and technical delivery for a major payment aggregator. Identified a critical Broken Object Level Authorization (BOLA) vulnerability that allowed horizontal account balance queries. Produced verified remediation guidelines and secured an ongoing quarterly testing retainer.",
        "<b>Multi-Cloud Infrastructure Posture Audit (2023):</b> Evaluated a fast-growing healthcare platform's AWS/Azure environment against CIS Benchmarks. Uncovered 3 publicly accessible S3 storage buckets containing sensitive test payloads and over-permissive IAM roles, facilitating seamless ISO 27001 readiness.",
        "<b>Automated Vulnerability Orchestration Dashboard (Python / Flask / Nessus API):</b> Created an internal delivery automation tool that ingests Nessus and Burp Suite outputs, deduplicates findings, calculates adjusted CVSS v3 risk scores, and generates branded client reports in under 3 minutes."
    ]
    for p in projects:
        story.append(Paragraph(f"&bull; {p}", bullet_style))
    story.append(HRFlowable(width="100%", thickness=0.5, color=border_color, spaceBefore=4, spaceAfter=6))

    # 6. Certifications & Education
    story.append(Paragraph("PROFESSIONAL CERTIFICATIONS &amp; EDUCATION", section_heading))
    
    cert_edu_data = [
        [
            Paragraph("<b>Certifications:</b>", body_style),
            Paragraph(
                "&bull; <b>OSCP</b> - Offensive Security Certified Professional (OffSec)<br/>"
                "&bull; <b>CEH</b> - Certified Ethical Hacker (EC-Council)<br/>"
                "&bull; <b>AWS Certified Security – Specialty</b> (Amazon Web Services)<br/>"
                "&bull; <b>ISO/IEC 27001:2022 Lead Auditor</b> (CQI &amp; IRCA)",
                body_style
            )
        ],
        [
            Paragraph("<b>Education:</b>", body_style),
            Paragraph(
                "<b>Bachelor of Engineering (B.E.) in Information Technology</b><br/>"
                "Anna University, Chennai &bull; First Class with Distinction (2014 – 2018)",
                body_style
            )
        ]
    ]
    cert_edu_table = Table(cert_edu_data, colWidths=[120, 420])
    cert_edu_table.setStyle(TableStyle([
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 0),
        ('RIGHTPADDING', (0,0), (-1,-1), 0),
    ]))
    story.append(cert_edu_table)

    doc.build(story)
    print(f"Successfully generated {filename} ({os.path.getsize(filename)} bytes)")

if __name__ == "__main__":
    build_pdf("cybersecurity_cv.pdf")
    build_pdf("cv.pdf")
