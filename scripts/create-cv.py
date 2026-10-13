"""Build the monochrome CV using the portfolio's shared certificate records."""
import json
from datetime import date
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parents[1]
certificates = json.loads((ROOT / 'src/certificates.json').read_text(encoding='utf-8'))
styles = getSampleStyleSheet()
for name, font, size, leading, after in [
    ('NameCV', 'Helvetica-Bold', 21, 25, 3),
    ('RoleCV', 'Helvetica', 10, 14, 3),
    ('MetaCV', 'Helvetica', 9, 13, 7),
    ('SectionCV', 'Helvetica-Bold', 10, 13, 5),
    ('BodyCV', 'Helvetica', 10.5, 14, 5),
    ('ProjectCV', 'Helvetica', 10.5, 14, 5),
    ('CertificateCV', 'Helvetica', 10.5, 14, 3),
]:
    styles.add(ParagraphStyle(name=name, fontName=font, fontSize=size, leading=leading,
        textColor=black, spaceAfter=after, spaceBefore=8 if name=='SectionCV' else 0,
        keepWithNext=name=='SectionCV'))
story=[]
def p(text, style='BodyCV'):
    story.append(Paragraph(text, styles[style]))
def section(title):
    p(title, 'SectionCV')

p('NIKETHA THAVANESWARAN', 'NameCV')
p('Computer Science Undergraduate', 'RoleCV')
p('Jaffna, Sri Lanka | <link href="mailto:nikkytamilneshan@gmail.com">nikkytamilneshan@gmail.com</link><br/>'
  '<link href="https://github.com/tniketha">github.com/tniketha</link> | '
  '<link href="https://tniketha.github.io/Portfolio-Nikky/">tniketha.github.io/Portfolio-Nikky</link>', 'MetaCV')
story.append(HRFlowable(width='100%', thickness=0.6, color=black))
section('PROFILE')
p('Computer Science undergraduate with interests in software development, machine learning, and data analysis. '
  'Developed Smart Attendance, a classroom attendance application using React Native, Expo, TypeScript, and an Express API. Seeking internship and collaborative project opportunities.')
section('EDUCATION')
p('<b>B.Sc. (Hons) Computer Science</b> | Current undergraduate<br/>University of Vavuniya, Sri Lanka')
p('<b>Relevant coursework:</b> Data Structures and Algorithms, Machine Learning, Artificial Intelligence, Database Management Systems, Computer Architecture, Bioinformatics, and Human-Computer Interaction.')
section('TECHNICAL SKILLS')
p('<b>Languages:</b> TypeScript, Python, Java, C, HTML, CSS, PHP, SQL, MIPS and 8086 Assembly<br/>'
  '<b>Data &amp; ML:</b> Pandas, NumPy, Matplotlib, Scikit-learn; data cleaning and visualization<br/>'
  '<b>Application development:</b> React Native, Expo, Node.js, Express, Prisma, Socket.IO<br/><b>Databases &amp; tools:</b> MongoDB, MySQL, Git, GitHub, VS Code, Jupyter Notebook, Google Colab, Android Studio')
section('PROJECT')
p('<b>Smart Attendance</b> | Web &amp; mobile application', 'ProjectCV')
p('TypeScript, React Native, Expo, Node.js, Express, MongoDB, Prisma, Socket.IO', 'ProjectCV')
p('Developed student, lecturer, and administrator workflows for classroom attendance management.', 'ProjectCV')
p('Implemented signed, rotating QR check-ins with expiry, duplicate prevention, and optional session location checks.', 'ProjectCV')
p('Added live lecturer rosters, student attendance history and analytics, correction requests, and CSV reports.', 'ProjectCV')
p('<link href="https://github.com/tniketha/SmartAttendance">github.com/tniketha/SmartAttendance</link>', 'ProjectCV')
section('COURSES &amp; CERTIFICATES')
for c in certificates:
    if c['category'] == 'Course completion':
        earned = date.fromisoformat(c['date']).strftime('%b %Y')
        p(f"<b>{escape(c['title'])}</b> | {escape(c['issuer'])} | {earned}", 'CertificateCV')
section('COMPETITIONS &amp; ACTIVITIES')
for c in certificates:
    earned = date.fromisoformat(c['date']).strftime('%b %Y')
    if c['category'] == 'Competition participation':
        p(f"<b>{escape(c['title'])}</b> | IEEE | {earned}<br/>Programming competition participant; team {escape(c['team'])}.", 'CertificateCV')
    elif c['category'] == 'Professional development':
        p(f"<b>Trailblazers '24</b> | {escape(c['issuer'])} | {earned}<br/>Participant in personal and professional development activities.", 'CertificateCV')
p('<b>AIESEC:</b> Member', 'CertificateCV')
output=ROOT / 'public/Niketha-Thavaneswaran-CV.pdf'
doc=SimpleDocTemplate(str(output), pagesize=A4, rightMargin=43, leftMargin=43,
    topMargin=32, bottomMargin=32, title='Niketha Thavaneswaran - CV', author='tniketha')
doc.build(story)
print(f'Created CV: {output}')
