from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name='NameCV',fontName='Helvetica-Bold',fontSize=23,leading=28,textColor=HexColor('#243943'),spaceAfter=5))
styles.add(ParagraphStyle(name='RoleCV',fontName='Helvetica',fontSize=11,leading=15,textColor=HexColor('#8c713d'),spaceAfter=8))
styles.add(ParagraphStyle(name='MetaCV',fontName='Helvetica',fontSize=9,leading=14,textColor=HexColor('#52616a'),spaceAfter=11))
styles.add(ParagraphStyle(name='SectionCV',fontName='Helvetica-Bold',fontSize=10,leading=14,textColor=HexColor('#8c713d'),spaceBefore=15,spaceAfter=6))
styles.add(ParagraphStyle(name='BodyCV',fontName='Helvetica',fontSize=9.5,leading=14,textColor=HexColor('#343c40'),spaceAfter=6))
styles.add(ParagraphStyle(name='ProjectCV',fontName='Helvetica',fontSize=9.3,leading=13,textColor=HexColor('#343c40'),spaceAfter=7))
story=[]
def p(text, style='BodyCV'): story.append(Paragraph(text,styles[style]))
p('NIKETHA THAVANESWARAN','NameCV')
p('COMPUTER SCIENCE UNDERGRADUATE','RoleCV')
p('Jaffna, Sri Lanka  |  <link href="mailto:nikkytamilneshan@gmail.com">nikkytamilneshan@gmail.com</link><br/><link href="https://github.com/tniketha">github.com/tniketha</link>','MetaCV')
story.append(HRFlowable(width='100%',thickness=1,color=HexColor('#baa374')))
p('PROFILE','SectionCV')
p('Computer Science undergraduate at the University of Vavuniya with interests in software development, machine learning, data analysis, and web development. Enjoys solving programming problems, learning new technologies, and applying computing knowledge to real-world problems. Seeking internship and collaborative project opportunities.')
p('EDUCATION','SectionCV')
p('<b>B.Sc. (Hons) Computer Science</b> | Current undergraduate<br/>University of Vavuniya, Sri Lanka<br/>Faculty of Applied Science, Department of Physical Science')
p('<b>Relevant coursework:</b> Programming, Data Structures and Algorithms, Machine Learning, Artificial Intelligence, Computer Architecture, Database Management Systems, System Analysis and Design, Human-Computer Interaction, Computer Graphics, Bioinformatics, Parallel Computing.')
p('TECHNICAL SKILLS','SectionCV')
p('<b>Languages &amp; web:</b> Python, Java, HTML, CSS, PHP, MIPS Assembly, 8086 Assembly<br/><b>Data &amp; ML:</b> Pandas, NumPy, Matplotlib, Scikit-learn, data cleaning, visualization, classification, model evaluation<br/><b>Databases:</b> MySQL, SQL, database design, ER/EER diagrams, normalization, CRUD operations<br/><b>Tools:</b> VS Code, Jupyter Notebook, Google Colab, Git, GitHub, Laragon, Android Studio<br/><b>Computing:</b> Computer architecture, system analysis and design, Microsoft MPI, CUDA concepts')
p('PROJECTS &amp; EXPLORATIONS','SectionCV')
p('<b>Python DNA Sequence Analyzer</b> | Python, Pandas, Matplotlib<br/>Reads DNA sequences, calculates sequence length and GC content, counts bases, exports results to CSV, and creates visualizations.','ProjectCV')
p('<b>Bioinformatics Data Visualization</b> | Python, Pandas, NumPy, Matplotlib<br/>Loads, cleans, and explores biological datasets through category counts, disease-status analysis, bar charts, and basic statistical interpretation.','ProjectCV')
p('<b>Candidate Elimination Implementation</b> | Python<br/>Explores concept learning with specific and general boundary calculation, positive and negative example processing, and version-space representation.','ProjectCV')
p('<b>MIPS Assembly String Processing</b> | MIPS Assembly<br/>Programs for reading and comparing strings, calculating string length, character processing, loops, and branching.','ProjectCV')
p('<b>Digital Attendance Management System - Concept</b> | HTML, CSS, PHP, MySQL<br/>An attendance-management concept where lecturers select present students and remaining students are automatically marked absent.','ProjectCV')
p('ACTIVITIES &amp; STRENGTHS','SectionCV')
p('<b>IEEEXtreme 18.0 &amp; 19.0:</b> Programming competition participant<br/><b>AIESEC:</b> Member<br/><b>Strengths:</b> Problem solving, analytical thinking, teamwork, communication, self-learning, adaptability, and technical documentation.')
doc=SimpleDocTemplate('public/Niketha-Thavaneswaran-CV.pdf',pagesize=A4,rightMargin=42,leftMargin=42,topMargin=35,bottomMargin=35,title='Niketha Thavaneswaran - CV',author='Niketha Thavaneswaran')
doc.build(story)
print('Created portfolio CV')
