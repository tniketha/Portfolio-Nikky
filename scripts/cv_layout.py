"""One-page CV with linked certificates and a plain-text reference."""
import json
from datetime import date
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Flowable, HRFlowable, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


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


def build_cv(root: Path, private_reference=None):
    reference_file = root / 'src/cv-reference.json'
    reference = private_reference or (
        json.loads(reference_file.read_text(encoding='utf-8')) if reference_file.is_file() else None
    )
    body = ParagraphStyle('Body', fontName='Helvetica', fontSize=10.5, leading=13,
                          textColor=colors.HexColor('#171717'), spaceAfter=2)
    styles = {
        'body': body,
        'name': ParagraphStyle('Name', parent=body, fontName='Helvetica-Bold', fontSize=22,
                               leading=26, alignment=TA_CENTER, spaceAfter=3),
        'role': ParagraphStyle('Role', parent=body, alignment=TA_CENTER, spaceAfter=3),
        'contact': ParagraphStyle('Contact', parent=body, fontSize=9.5, leading=12,
                                  alignment=TA_CENTER, spaceAfter=1),
        'heading': ParagraphStyle('Heading', parent=body, fontName='Helvetica-Bold',
                                  spaceBefore=7, spaceAfter=2, keepWithNext=True),
        'meta': ParagraphStyle('Meta', parent=body, fontSize=9.5, leading=12,
                               textColor=colors.HexColor('#444444'), spaceAfter=2),
        'certificate': ParagraphStyle('Certificate', parent=body, fontSize=9.5, leading=11.5,
                                      spaceAfter=0),
        'bullet': ParagraphStyle('Bullet', parent=body, leftIndent=10, bulletIndent=0,
                                 spaceAfter=2),
    }
    story = []

    def text(value, style='body'):
        story.append(Paragraph(value, styles[style]))

    def section(title):
        text(title, 'heading')
        story.append(HRFlowable(width='100%', thickness=.4,
                                color=colors.HexColor('#999999'), spaceAfter=4))

    def bullet(value):
        story.append(Paragraph(value, styles['bullet'], bulletText='-'))

    text('NIKETHA THAVANESWARAN', 'name')
    text('Computer Science Undergraduate', 'role')
    text('Jaffna, Sri Lanka | <link href="mailto:tn.niketha@gmail.com">tn.niketha@gmail.com</link>', 'contact')
    text('<link href="https://github.com/tniketha">github.com/tniketha</link> | '
         '<link href="https://www.linkedin.com/in/niketha-thavaneswaran/">LinkedIn: niketha-thavaneswaran</link> | '
         '<link href="https://tniketha.github.io/Portfolio-Nikky/">Portfolio</link>', 'contact')

    section('PROFILE')
    text('Final-year Computer Science undergraduate with hands-on experience building web and mobile '
         'applications using JavaScript, React, Node.js, and databases. Interested in practical problem-solving '
         'and creating clear, reliable user workflows.')

    section('EDUCATION')
    story.append(AlignedLine('<b>University of Vavuniya</b>', '<b>2023-2027</b>', body))
    text('B.Sc. (Hons) Computer Science | Final year')

    section('TECHNICAL SKILLS')
    text('<b>Languages:</b> JavaScript, SQL, Python, Java, C')
    text('<b>Frontend:</b> React, Next.js, React Native, Expo, HTML, CSS, Tailwind CSS')
    text('<b>Backend &amp; databases:</b> Node.js, Express, PostgreSQL, MongoDB')
    text('<b>Tools:</b> Git, GitHub, REST APIs')

    section('PROJECTS')
    story.append(AlignedLine('<b>ShopFlow</b> | Inventory and cash sales', 'Sole developer', body))
    text('JavaScript, Next.js, React, Express, PostgreSQL | '
         '<link href="https://github.com/tniketha/ShopFlow">github.com/tniketha/ShopFlow</link>', 'meta')
    bullet('Built a shop application to manage products and suppliers, receive stock, complete cash sales, '
           'and view sales history.')
    bullet('Receiving a purchase increases stock; checkout checks availability, records the sale, '
           'and reduces stock while keeping the original product names and prices.')
    story.append(Spacer(1, 4))
    story.append(AlignedLine('<b>Smart Attendance</b> | QR attendance application', 'Sole developer', body))
    text('JavaScript, React Native, Expo, Express, MongoDB | '
         '<link href="https://github.com/tniketha/SmartAttendance">github.com/tniketha/SmartAttendance</link>', 'meta')
    bullet('Built student and lecturer workflows: lecturers start a module-based class and display a QR code; '
           'enrolled students scan it to record present or late attendance.')
    bullet('Prevents duplicate check-ins, records missing students as absent when a class closes, '
           'and provides semester summaries, attendance history, and lecturer CSV exports.')

    section('CERTIFICATES &amp; PARTICIPATION')
    certificates = json.loads((root / 'src/certificates.json').read_text(encoding='utf-8'))
    cells = []
    for certificate in certificates:
        path = root / 'public/certificates' / certificate['file']
        if not path.is_file():
            raise FileNotFoundError(path)
        url = 'https://tniketha.github.io/Portfolio-Nikky/certificates/' + quote(certificate['file'])
        title = escape(certificate['title'].replace(chr(0x2019), "'"))
        issued = date.fromisoformat(certificate['date']).strftime('%b %Y')
        if certificate['category'] == 'Competition participation':
            details = 'IEEE | Participation | ' + issued
        elif certificate['category'] == 'Professional development':
            details = 'AIESEC, University of Peradeniya | ' + issued
        else:
            details = escape(certificate['issuer']) + ' | ' + issued
        cells.append(Paragraph(
            f'<link href="{url}" color="#174a75"><u><b>{title}</b></u></link><br/>{details}',
            styles['certificate']))
    # Read each column from top to bottom; each certificate keeps its own document link.
    middle = (len(cells) + 1) // 2
    rows = [[cells[i], cells[i + middle] if i + middle < len(cells) else ''] for i in range(middle)]
    table = Table(rows, colWidths=[(A4[0] - 92) / 2] * 2, hAlign='LEFT')
    table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (0, -1), 0),
        ('LEFTPADDING', (1, 0), (1, -1), 14),
        ('RIGHTPADDING', (0, 0), (0, -1), 14),
        ('RIGHTPADDING', (1, 0), (1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 2),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(table)

    section('COMMUNITY INVOLVEMENT')
    text('AIESEC - Member | IEEE - Member | Zero Plastic, University of Vavuniya - Member', 'meta')

    if reference:
        section('REFERENCE')
        text('<b>' + escape(reference['name']) + '</b> | ' + escape(reference['role']))
        text(escape(reference['phone']), 'meta')
        text(escape(reference['email']), 'meta')

    folder = 'output/pdf' if private_reference else 'public'
    output = root / folder / 'Niketha-Thavaneswaran-CV.pdf'
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=40, rightMargin=40,
                            topMargin=28, bottomMargin=28,
                            title='Niketha Thavaneswaran - Curriculum Vitae',
                            author='tniketha', subject='Computer Science curriculum vitae')
    doc.build(story)
    print(f'Created CV: {output}')
