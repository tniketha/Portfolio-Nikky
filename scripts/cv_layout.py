"""Readable internship resume with linked certificates. All text remains selectable."""
import json
from datetime import date
from pathlib import Path
from urllib.parse import quote
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Flowable, HRFlowable, KeepTogether, PageBreak, Paragraph, SimpleDocTemplate, Spacer


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
    body = ParagraphStyle('Body', fontName='Helvetica', fontSize=11, leading=15.5,
                          textColor=colors.HexColor('#171717'), spaceAfter=3)
    styles = {
        'body': body,
        'name': ParagraphStyle('Name', parent=body, fontName='Helvetica-Bold', fontSize=22,
                               leading=26, alignment=TA_CENTER, spaceAfter=4),
        'role': ParagraphStyle('Role', parent=body, fontSize=11, leading=15.5,
                               alignment=TA_CENTER, spaceAfter=5),
        'contact': ParagraphStyle('Contact', parent=body, fontSize=9.5, leading=13,
                                  alignment=TA_CENTER, spaceAfter=2),
        'heading': ParagraphStyle('Heading', parent=body, fontName='Helvetica-Bold',
                                  fontSize=11, leading=15.5, spaceBefore=9, spaceAfter=3,
                                  keepWithNext=True),
        'meta': ParagraphStyle('Meta', parent=body, fontSize=10.5, leading=14.5,
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
    text('<b>Languages:</b> JavaScript, SQL, Python, Java, C')
    text('<b>Frontend:</b> React, Next.js, React Native, Expo, HTML, CSS, Tailwind CSS')
    text('<b>Backend &amp; databases:</b> Node.js, Express, PostgreSQL (pg), MongoDB driver')
    text('<b>Tools &amp; practices:</b> Git, GitHub, REST APIs, transactions, unit and integration testing')

    section('TECHNICAL PROJECTS')
    story.append(AlignedLine('<b>ShopFlow</b> | Retail web application', 'Sole developer', body))
    text('JavaScript, Next.js, React, Tailwind CSS, Express, PostgreSQL, SQL | '
         '<link href="https://github.com/tniketha/ShopFlow">github.com/tniketha/ShopFlow</link>', 'meta')
    bullet('Built a responsive Next.js workspace connecting product management, supplier purchases, '
           'cash checkout, stock totals, and sales history through Express REST APIs.')
    bullet('Used parameterized SQL, serializable transactions, product row locks, and request keys '
           'to prevent overselling and duplicate purchases or sales on retry.')
    bullet('Enforced store isolation and role permissions; used integer LKR cents and saved product-price '
           'snapshots to preserve accurate sale records.')
    bullet('Added PostgreSQL integration tests for concurrent checkout, repeated requests, insufficient stock, '
           'transaction rollback, store boundaries, and SQL migrations.')
    story.append(Spacer(1, 7))
    story.append(AlignedLine('<b>Smart Attendance</b> | Web and mobile application', 'Sole developer', body))
    text('JavaScript, React Native, Expo, Express, MongoDB | '
         '<link href="https://github.com/tniketha/SmartAttendance">github.com/tniketha/SmartAttendance</link>', 'meta')
    bullet('Built JavaScript student and lecturer screens with React Native and Expo, backed by Express for '
           'module-based class creation, QR check-in, and semester attendance tracking.')
    bullet('Validated QR tokens, active classes, and enrollment timing; used unique attendance records '
           'and direct MongoDB driver transactions to prevent duplicates and coordinate check-in with closure.')
    bullet('Recorded missing students as absent when classes close; calculated completed-class statistics '
           'and provided filtered attendance history and lecturer CSV exports.')
    bullet('Added API integration tests for role restrictions, invalid QR codes, duplicate check-ins, '
           'class closure, expiry, semester reports, and logout token revocation.')

    certificates = json.loads((root / 'src/certificates.json').read_text(encoding='utf-8'))
    story.append(PageBreak())
    text('<b>NIKETHA THAVANESWARAN</b> | Certificates &amp; participation', 'meta')
    text('Click an underlined certificate title to view the original document.', 'meta')
    for category, heading in [
        ('Course completion', 'COURSE COMPLETION CERTIFICATES'),
        ('Competition participation', 'PROGRAMMING COMPETITION PARTICIPATION'),
        ('Professional development', 'PROFESSIONAL DEVELOPMENT'),
    ]:
        section(heading)
        for certificate in certificates:
            if certificate['category'] != category:
                continue
            path = root / 'public/certificates' / certificate['file']
            if not path.is_file():
                raise FileNotFoundError(path)
            url = 'https://tniketha.github.io/Portfolio-Nikky/certificates/' + quote(certificate['file'])
            title = escape(certificate['title'].replace('\u2019', "'"))
            issued = date.fromisoformat(certificate['date']).strftime('%d %b %Y')
            details = escape(certificate['issuer'])
            if certificate.get('credentialId'):
                details += ' | Credential ID: ' + escape(certificate['credentialId'])
            if certificate.get('team'):
                details += ' | Team: ' + escape(certificate['team'])
            story.append(KeepTogether([
                AlignedLine(f'<link href="{url}" color="#174a75"><u><b>{title}</b></u></link>', issued, body),
                Paragraph(details, styles['meta']),
                Spacer(1, 7),
            ]))

    section('COMMUNITY INVOLVEMENT')
    text('<b>AIESEC:</b> Member.', 'meta')
    text('<b>IEEE:</b> Member.', 'meta')
    text('<b>Zero Plastic, University of Vavuniya:</b> Member.', 'meta')

    if reference:
        section('REFERENCE')
        text('<b>' + escape(reference['name']) + '</b> | ' + escape(reference['role']))
        text(escape(reference['qualifications']), 'meta')
        phone = escape(reference['phone'])
        email_address = escape(reference['email'])
        text(f'{phone} | {email_address}')

    def page_footer(canvas, document):
        canvas.saveState()
        canvas.setFont('Helvetica', 8)
        canvas.setFillColor(colors.HexColor('#666666'))
        canvas.drawString(44, 20, 'Niketha Thavaneswaran | Software Engineering & Full-stack Internships')
        canvas.drawRightString(A4[0] - 44, 20, f'Page {document.page}')
        canvas.restoreState()

    folder = 'output/pdf' if private_reference else 'public'
    output = root / folder / 'Niketha-Thavaneswaran-CV.pdf'
    output.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output), pagesize=A4, leftMargin=44, rightMargin=44,
                            topMargin=34, bottomMargin=34,
                            title='Niketha Thavaneswaran - Software Engineering Internship CV',
                            author='tniketha', subject='Software engineering and full-stack development internships')
    doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)
    print(f'Created CV: {output}')
