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
         'Machine Learning, Artificial Intelligence, Computer Architecture, Human-Computer Interaction.', 'meta')

    section('TECHNICAL SKILLS')
    text('<b>Languages:</b> TypeScript, Python, Java, C, SQL, JavaScript, HTML, CSS, PHP')
    text('<b>Frontend:</b> React, Next.js, React Native, Expo, Tailwind CSS')
    text('<b>Backend &amp; databases:</b> Node.js, Express, Fastify, Prisma, PostgreSQL, MongoDB, MySQL')
    text('<b>Tools &amp; practices:</b> Git, GitHub, REST APIs, role-based access, database transactions, integration testing')
    text('<b>Data &amp; machine learning:</b> Pandas, NumPy, Matplotlib, Scikit-learn, Jupyter Notebook')

    section('TECHNICAL PROJECTS')
    story.append(AlignedLine('<b>ShopFlow</b> | Retail web application', 'Sole developer', body))
    text('Next.js, React, TypeScript, Tailwind CSS, Fastify, PostgreSQL, Prisma | '
         '<link href="https://github.com/tniketha/ShopFlow">github.com/tniketha/ShopFlow</link>', 'meta')
    bullet('Built a responsive inventory and cash-sales application with product and category management, '
           'supplier purchases, cash checkout, an overview dashboard, and sales history.')
    bullet('Implemented Fastify REST APIs, PostgreSQL transactions, and owner, manager, and cashier permissions '
           'to keep stock updates consistent and isolate business data.')
    bullet('Protected retries with unique request keys and represented amounts in integer LKR cents '
           'to prevent duplicate transactions and monetary rounding errors.')
    story.append(Spacer(1, 7))
    story.append(AlignedLine('<b>Smart Attendance</b> | Web and mobile application', 'Sole developer', body))
    text('React Native, Expo, TypeScript, Express, MongoDB, Prisma | '
         '<link href="https://github.com/tniketha/SmartAttendance">github.com/tniketha/SmartAttendance</link>', 'meta')
    bullet('Built student and lecturer workflows with React Native and Expo, connecting semester modules, '
           'class QR check-in, and attendance history to an Express API.')
    bullet('Validated active-class QR tokens, enrollment timing, and duplicate check-ins on the server; '
           'used MongoDB transactions to coordinate check-in with class closure.')
    bullet('Implemented present, late, and absent records, lecturer-refreshed class lists, semester statistics, '
           'filtered student history, and module CSV exports.')

    certificates = json.loads((root / 'src/certificates.json').read_text(encoding='utf-8'))
    section('COURSES &amp; CERTIFICATES')
    courses = [c['title'] for c in certificates if c['category'] == 'Course completion']
    text('<b>Sololearn | Jan-Feb 2026:</b> ' + '; '.join(escape(c) for c in courses) + '.', 'meta')

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
