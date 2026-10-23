export interface ProjectScreenshot {
 file: string;
 label: string;
 alt: string;
 caption: string;
}

export interface Project {
 title: string;
 subtitle: string;
 category: string;
 type: string;
 kind: string;
 author: 'tniketha';
 stack: string[];
 description: string;
 problem: string;
 highlights: string[];
 features: string[];
 decisions: { title: string; description: string }[];
 architecture: { name: string; role: string }[];
 screenshots: ProjectScreenshot[];
 scope: string;
 repository: string;
}

export const projects: Project[] = [
 {
  title: 'Smart Attendance',
  subtitle: 'From classroom check-in to a clear attendance record.',
  category: 'Education · Web & mobile',
  type: 'FULL-STACK ATTENDANCE APPLICATION',
  kind: 'attendance',
  author: 'tniketha',
  stack: ['TypeScript', 'React Native', 'Expo', 'Express', 'MongoDB', 'Prisma', 'Socket.IO'],
  description: 'A connected attendance workflow for students, lecturers, and administrators. Rotating QR check-ins feed live classroom rosters, while students track their progress and request reviewed corrections.',
  problem: 'Manual roll calls interrupt classes, and disconnected records make follow-up difficult. I built a shared application that connects check-in, session management, reporting, and corrections across three user roles.',
  highlights: ['Rotating QR check-in', 'Live lecturer rosters', 'Role-based access'],
  features: [
   'Signed, expiring QR codes with enrollment checks and duplicate prevention',
   'Optional session location checks and separate student, lecturer, and administrator workflows',
   'Live rosters, semester-based attendance insights, and CSV reports',
   'Lecturer-reviewed correction requests with an audit history',
   'Responsive layouts, light and dark themes, and shared web and mobile code'
  ],
  decisions: [
   { title: 'Validate beyond the QR code.', description: 'The API checks the account, enrollment, session state, and configured location rules before accepting attendance. Transactions protect check-ins when a lecturer closes a session at the same time.' },
   { title: 'Keep live views recoverable.', description: 'Authenticated Socket.IO updates keep lecturer rosters current, with polling recovery after a dropped connection. Approved corrections and their audit entries commit together.' }
  ],
  architecture: [
   { name: 'React Native + Expo', role: 'Shared client for web, Android & iOS' },
   { name: 'Express + Socket.IO', role: 'API, authorization & live updates' },
   { name: 'Prisma + MongoDB', role: 'Sessions, attendance & audit records' }
  ],
  screenshots: [
   { file: 'lecturer-dashboard-desktop.jpg', label: 'Lecturer', alt: 'Smart Attendance lecturer dashboard with an active Computer Architecture session', caption: 'Lecturer dashboard · Start sessions and follow attendance.' },
   { file: 'live-qr-desktop.jpg', label: 'Live QR', alt: 'Smart Attendance rotating QR screen for a temporary classroom session', caption: 'Live QR · A short-lived code connects students to the current session.' },
   { file: 'live-roster-desktop.jpg', label: 'Roster', alt: 'Smart Attendance live roster showing fictional present and late students', caption: 'Live roster · Check-ins appear in the lecturer’s session view.' },
   { file: 'student-dashboard-mobile.jpg', label: 'Student', alt: 'Smart Attendance student dashboard at a phone-sized browser width', caption: 'Student dashboard · Responsive web view with demo attendance records.' },
   { file: 'student-analytics-mobile.jpg', label: 'Insights', alt: 'Smart Attendance mobile web insights with a subject attendance breakdown', caption: 'Student insights · Explore attendance by subject and semester.' },
   { file: 'admin-dashboard-desktop.jpg', label: 'Admin', alt: 'Smart Attendance administrator dashboard with a demonstration audit entry', caption: 'Administration · System activity and an attendance correction audit trail.' }
  ],
  scope: 'Built for web, Android, and iOS with Expo. Screenshots show the responsive web app with fictional demo records. QR and location checks reduce misuse but cannot prove physical presence; native device acceptance and institutional deployment are separate steps.',
  repository: 'https://github.com/tniketha/SmartAttendance'
 },
 {
  title: 'ShopFlow',
  subtitle: 'Stock, sales, and the next step for a store.',
  category: 'Retail · Responsive web',
  type: 'FULL-STACK RETAIL WORKSPACE',
  kind: 'shopflow',
  author: 'tniketha',
  stack: ['TypeScript', 'Next.js', 'React', 'Tailwind CSS', 'Fastify', 'PostgreSQL', 'Prisma'],
  description: 'A retail workspace that brings inventory, purchasing, cash checkout, refunds, and reporting together. Built around clear store workflows, accurate LKR totals, and consistent stock records.',
  problem: 'Purchases, sales, and returns all affect the same stock. I built a workspace that connects those operations, gives each store role the right tools, and keeps financial and inventory records consistent.',
  highlights: ['Inventory & purchasing', 'Cash checkout & refunds', 'Sales insights & exports'],
  features: [
   'Product inventory, category filters, barcode lookup, favourites, and product photos',
   'Supplier purchases and receiving with stock movement records',
   'Cash checkout, PDF invoices, partial refunds, and stock restoration',
   'Sales insights, low-stock alerts, and CSV/PDF reports using Sri Lanka business dates',
   'CSV import with row-level validation and a preview before saving',
   'Server-enforced owner, manager, and cashier permissions with business-isolated data'
  ],
  decisions: [
   { title: 'Keep stock changes together.', description: 'Serializable PostgreSQL transactions commit checkout, purchase receipts, or refunds alongside their stock movements. Request keys protect successful operations from being recorded twice on retry.' },
   { title: 'Make money calculations explicit.', description: 'Amounts use integer LKR cents. Sales retain the original product and price snapshots, while refunds enforce returned-quantity limits and restore stock atomically.' }
  ],
  architecture: [
   { name: 'Next.js + React', role: 'Responsive store workspace' },
   { name: 'Fastify', role: 'REST API, sessions & permissions' },
   { name: 'Prisma + PostgreSQL', role: 'Transactions, stock & sales records' }
  ],
  screenshots: [
   { file: '01-dashboard-desktop.jpg', label: 'Overview', alt: 'ShopFlow store dashboard with sample sales insights and low-stock information', caption: 'Store overview · Sales trends, top products, and stock at a glance.' },
   { file: '03-pos-desktop.jpg', label: 'Checkout', alt: 'ShopFlow point of sale with photographed products and a two-item cash basket', caption: 'Point of sale · Product search, barcode entry, and a cash basket.' },
   { file: '02-inventory-desktop.jpg', label: 'Inventory', alt: 'ShopFlow inventory catalogue with product filters, prices, and stock levels', caption: 'Inventory · A filterable catalogue with clear prices and stock status.' },
   { file: '04-reports-desktop.jpg', label: 'Reports', alt: 'ShopFlow sales report with date filters and CSV and PDF export options', caption: 'Reports · Review sales and refunds for the selected business dates.' },
   { file: '12-csv-import-desktop.jpg', label: 'CSV import', alt: 'ShopFlow CSV import preview flagging an invalid decimal price', caption: 'CSV import · Review row-level validation before saving products.' },
   { file: '09-pos-mobile.jpg', label: 'Mobile', alt: 'ShopFlow point of sale at a phone-sized browser width', caption: 'Responsive checkout · The store workflow at a narrow web viewport.' }
  ],
  scope: 'A local full-stack project with cash payments and whole-unit inventory. Screenshots use fictional store data. The repository includes setup, tests, and deployment guidance; card payments and offline checkout are outside the current scope.',
  repository: 'https://github.com/tniketha/ShopFlow'
 }
];

export const email = 'tn.niketha@gmail.com';
export const linkedin = 'https://www.linkedin.com/in/niketha-thavaneswaran/';
