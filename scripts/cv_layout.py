"""Readable, single-column internship resume. All text remains selectable."""
import json
from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Flowable, HRFlowable, Paragraph, SimpleDocTemplate, Spacer


class AlignedLine(Flowable):
    """One reading-order line with consistent left and right edges."""

    def __init__(self, left, right, style):
        super().__init__()
        self.left = Paragraph(left, style)
        self.right = Paragraph(right, ParagraphStyle('Right', parent=style, alignment=2))
        self.keepWithNext = True

    def wrap(self, width, height):
        self.width = width
        self.right_width = min(155, width * .34)
        self.left_width = width - self.right_width - 10
        _, left_height = self.left.wrap(self.left_width, height)
        _, right_height = self.right.wrap(self.right_width, height)
        self.height = max(left_height, right_height)
        return self.width, self.height

    def draw(self):
        self.left.drawOn(self.canv, 0, 0)
        self.right.drawOn(self.canv, self.width - self.right_width, 0)


def build_cv(root: Path):
    body = ParagraphStyle('Body', fontName='Helvetica', fontSize=10.5, leading=14,
                          textColor=colors.HexColor('#171717'), spaceAfter=3)
    styles = {
        'body': body,
        'name': ParagraphStyle('Name', parent=body, fontName='Helvetica-Bold', fontSize=22,
                               leading=26, alignment=TA_CENTER, spaceAfter=4),
        'role': ParagraphStyle('Role', parent=body, fontSize=10.5, leading=14,
                               alignment=TA_CENTER, spaceAfter=5),
        'contact': ParagraphStyle('Contact', parent=body, fontSize=9.5, leading=13,
                                  alignment=TA_CENTER, spaceAfter=2),
        'heading': ParagraphStyle('Heading', parent=body, fontName='Helvetica-Bold',
                                  fontSize=10.5, leading=14, spaceBefore=9, spaceAfter=3,
                                  keepWithNext=True),
        'meta': ParagraphStyle('Meta', parent=body, fontSize=10, leading=13,
                               textColor=colors.HexColor('#444444'), spaceAfter=3),
        'bullet': ParagraphStyle('Bullet', parent=body, leftIndent=11, bulletIndent=0,
                                 spaceAfter=3),
    }
    story = []

    def text(value, style='body'):
        story.append(Paragraph(value, styles[style]))

    def section(title):
        text(title, 'heading')
        story.append(HRFlowable(width='100%', thickness=.45,
                                color=colors.HexColor('#777777'), spaceAfter=6))

    def bullet(value):
        story.append(Paragraph(value, styles['bullet'], bulletText='-'))

    text('NIKETHA THAVANESWARAN', 'name')
    text('Final-year Computer Science Undergraduate | Software Engineering &amp; Full-stack Internships', 'role')
    text('Jaffna, Sri Lanka | <link href="mailto:tn.niketha@gmail.com">tn.niketha@gmail.com</link>', 'contact')
    text('<link href="https://github.com/tniketha">github.com/tniketha</link> | '
         '<link href="https://www.linkedin.com/in/niketha-thavaneswaran/">LinkedIn: niketha-thavaneswaran</link> | '
         '<link href="https://tniketha.github.io/Portfolio-Nikky/">Portfolio</link>', 'contact')

    section('EDUCATION')
    story.append(AlignedLine('<b>University of Vavuniya</b>', 'Sri Lanka', body))
    story.append(AlignedLine('B.Sc. (Hons) Computer Science', '<b>Expected June 2027</b>', body))
    text('Final year | Relevant coursework: Data Structures and Algorithms, Database Management Systems, '
         'Computer Architecture, Human-Computer Interaction.', 'meta')

    section('TECHNICAL SKILLS')
    text('<b>Languages:</b> TypeScript, JavaScript, SQL, Python, Java, C')
    text('<b>Frontend:</b> React, Next.js, React Native, Expo, HTML, CSS, Tailwind CSS')
    text('<b>Backend &amp; databases:</b> Node.js, Express, Fastify, Prisma, PostgreSQL, MongoDB')
    text('<b>Tools &amp; practices:</b> Git, GitHub, REST APIs, transactions, unit and integration testing')

    section('TECHNICAL PROJECTS')
    story.append(AlignedLine('<b>ShopFlow</b> | Retail web application', 'Sole developer', body))
    text('Next.js, React, TypeScript, Tailwind CSS, Fastify, PostgreSQL, Prisma | '
         '<link href="https://github.com/tniketha/ShopFlow">github.com/tniketha/ShopFlow</link>', 'meta')
    bullet('Built a responsive Next.js workspace connecting product management, supplier purchases, '
           'cash checkout, stock totals, and sales history through Fastify REST APIs.')
    bullet('Used serializable PostgreSQL transactions, conditional stock updates, and request keys '
           'to prevent overselling and duplicate purchases or sales on retry.')
    bullet('Enforced store isolation and role permissions; used integer LKR cents and saved product-price '
           'snapshots to preserve accurate sale records.')
    bullet('Added PostgreSQL integration tests for concurrent checkout, repeated requests, insufficient stock, '
           'transaction rollback, and access across store boundaries.')
    story.append(Spacer(1, 7))
    story.append(AlignedLine('<b>Smart Attendance</b> | Web and mobile application', 'Sole developer', body))
    text('React Native, Expo, TypeScript, Express, MongoDB, Prisma | '
         '<link href="https://github.com/tniketha/SmartAttendance">github.com/tniketha/SmartAttendance</link>', 'meta')
    bullet('Built React Native and Expo student and lecturer screens backed by an Express API for '
           'module-based class creation, QR check-in, and semester attendance tracking.')
    bullet('Validated QR tokens, active classes, and enrollment timing; used unique attendance records '
           'and MongoDB transactions to prevent duplicates and coordinate check-in with class closure.')
    bullet('Recorded missing students as absent when classes close; calculated completed-class statistics '
           'and provided filtered attendance history and lecturer CSV exports.')
    bullet('Added API integration tests for role restrictions, invalid QR codes, duplicate check-ins, '
           'class closure, expiry, semester reports, and logout token revocation.')

    certificates = json.loads((root / 'src/certificates.json').read_text(encoding='utf-8'))
    section('SELECTED COURSES')
    courses = [c['title'] for c in certificates
               if c['category'] == 'Course completion' and c['title'] in ('C Intermediate', 'SQL Intermediate')]
    text('<b>Sololearn | Feb 2026:</b> ' + '; '.join(escape(c) for c in courses) + '.', 'meta')

    section('COMPETITIONS &amp; ACTIVITIES')
    text('<b>IEEE IEEEXtreme:</b> 19.0 (Oct 2025), team DigitalVanguard; '
         '18.0 (Oct 2024), team TheChiefs. Programming competition participant.', 'meta')
    text("<b>AIESEC:</b> Member. <b>Trailblazers '24:</b> Professional development participant, "
         'AIESEC in University of Peradeniya (Dec 2024).', 'meta')

    output = root / 'public/Niketha-Thavaneswaran-CV.pdf'
    doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=44, rightMargin=44,
                            topMargin=34, bottomMargin=34,
                            title='Niketha Thavaneswaran - Software Engineering Internship CV',
                            author='tniketha', subject='Software engineering and full-stack development internships')
    doc.build(story)
    print(f'Created CV: {output}')
