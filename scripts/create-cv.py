"""Build the one-page CV using verified project and shared certificate details."""
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
    ('MetaCV', 'Helvetica', 9, 12, 6),
    ('SectionCV', 'Helvetica-Bold', 10, 13, 5),
    ('BodyCV', 'Helvetica', 10.2, 13.5, 4),
    ('ProjectCV', 'Helvetica-Bold', 10.2, 13.5, 3),
    ('StackCV', 'Helvetica', 9.2, 12, 3),
    ('BulletCV', 'Helvetica', 10.2, 13.5, 3),
    ('CertificateCV', 'Helvetica', 9.5, 12.5, 3),
]:
    styles.add(ParagraphStyle(name=name, fontName=font, fontSize=size, leading=leading,
        textColor=black, spaceAfter=after, spaceBefore=8 if name=='SectionCV' else 0,
        leftIndent=9 if name=='BulletCV' else 0,
        firstLineIndent=-9 if name=='BulletCV' else 0,
        keepWithNext=name in {'SectionCV', 'ProjectCV', 'StackCV'}))
story=[]
def p(text, style='BodyCV'):
    story.append(Paragraph(text, styles[style]))
def section(title):
    p(title, 'SectionCV')

p('NIKETHA THAVANESWARAN', 'NameCV')
p('Computer Science Undergraduate | Full-stack Development', 'RoleCV')
p('Jaffna, Sri Lanka | <link href="mailto:tn.niketha@gmail.com">tn.niketha@gmail.com</link><br/>'
  '<link href="https://github.com/tniketha">github.com/tniketha</link> | '
  '<link href="https://tniketha.github.io/Portfolio-Nikky/">tniketha.github.io/Portfolio-Nikky</link><br/>'
  '<link href="https://www.linkedin.com/in/niketha-thavaneswaran/">linkedin.com/in/niketha-thavaneswaran</link>', 'MetaCV')
story.append(HRFlowable(width='100%', thickness=0.6, color=black))
section('PROFILE')
p('Computer Science undergraduate who has independently developed web and mobile applications, '
  'REST APIs, and database workflows through Smart Attendance and ShopFlow. '
  'Seeking a software engineering internship or junior developer opportunity, with interests in machine learning and data analysis.')
section('EDUCATION')
p('<b>B.Sc. (Hons) Computer Science</b> | Current undergraduate<br/>University of Vavuniya, Sri Lanka')
p('<b>Relevant coursework:</b> Data Structures and Algorithms, Database Management Systems, Machine Learning, Artificial Intelligence, Computer Architecture, Bioinformatics, and Human-Computer Interaction.')
section('TECHNICAL SKILLS')
p('<b>Languages:</b> TypeScript, Python, Java, C, SQL, HTML, CSS, PHP, MIPS and 8086 Assembly<br/>'
  '<b>Web &amp; mobile:</b> React, Next.js, React Native, Expo, Tailwind CSS<br/>'
  '<b>Backend &amp; data:</b> Node.js, Express, Fastify, Prisma, Socket.IO, PostgreSQL, MongoDB, MySQL<br/>'
  '<b>Data &amp; ML:</b> Pandas, NumPy, Matplotlib, Scikit-learn; data cleaning and visualization<br/>'
  '<b>Tools:</b> Git, GitHub, VS Code, Jupyter Notebook, Google Colab, Android Studio')
section('PROJECTS')
p('Smart Attendance | Web and mobile application | Sole developer', 'ProjectCV')
p('TypeScript, React Native, Expo, Express, MongoDB, Prisma, Socket.IO', 'StackCV')
p('- Built student, lecturer, and administrator workflows with signed, rotating QR check-ins, enrollment validation, duplicate prevention, and optional location checks.', 'BulletCV')
p('- Connected authenticated live rosters and polling recovery with semester-based insights, CSV reports, and audited attendance correction requests.', 'BulletCV')
p('<link href="https://github.com/tniketha/SmartAttendance">github.com/tniketha/SmartAttendance</link>', 'StackCV')
p('ShopFlow | Retail web application | Sole developer', 'ProjectCV')
p('TypeScript, Next.js, React, Tailwind CSS, Fastify, PostgreSQL, Prisma', 'StackCV')
p('- Developed inventory, purchasing, barcode-assisted cash checkout, partial refunds, PDF invoices, and sales reporting with owner, manager, and cashier permissions.', 'BulletCV')
p('- Used database transactions, stock checks, and duplicate-request protection to keep sales and inventory consistent; represented money in integer LKR cents for exact calculations.', 'BulletCV')
p('<link href="https://github.com/tniketha/ShopFlow">github.com/tniketha/ShopFlow</link>', 'StackCV')
section('COURSES &amp; CERTIFICATES')
courses = [c for c in certificates if c['category'] == 'Course completion']
course_text = '; '.join(f"{escape(c['title'])} ({date.fromisoformat(c['date']).strftime('%b %Y')})" for c in courses)
p(f'<b>Sololearn:</b> {course_text}.', 'CertificateCV')
section('COMPETITIONS &amp; ACTIVITIES')
competitions = sorted((c for c in certificates if c['category'] == 'Competition participation'), key=lambda c: c['date'], reverse=True)
competition_text = '; '.join(f"{escape(c['title'])} ({date.fromisoformat(c['date']).strftime('%b %Y')}), team {escape(c['team'])}" for c in competitions)
p(f'<b>IEEE programming competitions:</b> Participant in {competition_text}.', 'CertificateCV')
for c in certificates:
    if c['category'] == 'Professional development':
        earned = date.fromisoformat(c['date']).strftime('%b %Y')
        p(f"<b>Trailblazers '24:</b> {escape(c['issuer'])}, {earned}. Personal and professional development participant.", 'CertificateCV')
p('<b>AIESEC:</b> Member.', 'CertificateCV')
output=ROOT / 'public/Niketha-Thavaneswaran-CV.pdf'
doc=SimpleDocTemplate(str(output), pagesize=A4, rightMargin=43, leftMargin=43,
    topMargin=32, bottomMargin=32, title='Niketha Thavaneswaran - CV', author='tniketha')
doc.build(story)
print(f'Created CV: {output}')
