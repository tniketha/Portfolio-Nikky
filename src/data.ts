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
  author: "tniketha";
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
    title: "Smart Attendance",
    subtitle: "From a class QR code to a clear attendance record.",
    category: "Education · Web & mobile",
    type: "FULL-STACK ATTENDANCE APPLICATION",
    kind: "attendance",
    author: "tniketha",
    stack: [
      "JavaScript",
      "React Native",
      "Expo",
      "Node.js",
      "Express",
      "MongoDB",
    ],
    description:
      "A university attendance application for students and lecturers. Lecturers start module-based classes and display a QR code; students check in and review their semester attendance.",
    problem:
      "Manual class registers take time and make semester follow-up difficult. I connected student check-in, lecturer class management, and attendance reporting through a shared interface and API.",
    highlights: [
      "Class QR check-in",
      "Student & lecturer workflows",
      "Semester summaries & CSV",
    ],
    features: [
      "Sign in with an email or institutional ID, with separate student and lecturer screens",
      "Select a semester and module, set the class duration, and display its QR code",
      "Record present or late attendance with enrollment validation and one check-in per student per class",
      "Refresh the class attendance list and close the class to mark missing enrolled students absent",
      "View semester attendance statistics, filtered history, and enrolled modules",
      "Review lecturer module reports and export attendance as CSV",
    ],
    decisions: [
      {
        title: "Check attendance on the server.",
        description:
          "The Express API verifies the QR token, active class, enrollment timing, and duplicate records. Direct MongoDB queries use a unique student/class index and transactions to coordinate check-in with class closure.",
      },
      {
        title: "Count completed classes consistently.",
        description:
          "Closing or expiring a class records absences for missing enrolled students. Semester percentages count present and late records across completed classes, excluding active ones.",
      },
    ],
    architecture: [
      {
        name: "React Native + Expo",
        role: "Shared student and lecturer interface",
      },
      {
        name: "Express",
        role: "REST API, sign-in & attendance rules",
      },
      {
        name: "MongoDB driver",
        role: "Direct queries, unique indexes & transactions",
      },
    ],
    screenshots: [
      {
        file: "lecturer-dashboard-desktop.jpg",
        label: "Lecturer",
        alt: "Smart Attendance lecturer dashboard with semester modules and class controls",
        caption:
          "Lecturer dashboard · Choose a semester and module to start a class.",
      },
      {
        file: "session-qr-desktop.jpg",
        label: "Class QR",
        alt: "Smart Attendance active class displaying its QR code",
        caption: "Class QR · Enrolled students scan while the class is active.",
      },
      {
        file: "session-attendance-desktop.jpg",
        label: "Attendance",
        alt: "Smart Attendance class list with present and late demo students and a refresh button",
        caption:
          "Class attendance · Refresh the list to review student check-ins.",
      },
      {
        file: "lecturer-reports-desktop.jpg",
        label: "Reports",
        alt: "Smart Attendance lecturer module attendance report",
        caption: "Module reports · Review attendance and export CSV records.",
      },
      {
        file: "student-dashboard-mobile.jpg",
        label: "Student",
        alt: "Smart Attendance student dashboard at a mobile web width",
        caption:
          "Student dashboard · Semester modules and attendance at a glance.",
      },
      {
        file: "student-attendance-mobile.jpg",
        label: "Summary",
        alt: "Smart Attendance My Attendance semester statistics on mobile web",
        caption: "My Attendance · Semester statistics from completed classes.",
      },
      {
        file: "student-history-mobile.jpg",
        label: "History",
        alt: "Smart Attendance filtered student attendance history",
        caption:
          "Attendance history · Review records with semester and module filters.",
      },
      {
        file: "student-modules-mobile.jpg",
        label: "Modules",
        alt: "Smart Attendance student enrolled modules by semester",
        caption: "My modules · Browse enrolled semester modules.",
      },
      {
        file: "sign-in-mobile.jpg",
        label: "Sign in",
        alt: "Smart Attendance mobile web sign-in screen",
        caption: "Sign in · Use an email or institutional ID.",
      },
    ],
    scope:
      "An undergraduate demonstration built with React Native and Expo, with web, Android, and iOS development targets. These are current browser captures using fictional university records. QR check-in is available only during an active class and does not prove physical presence.",
    repository: "https://github.com/tniketha/SmartAttendance",
  },
  {
    title: "ShopFlow",
    subtitle: "Add products. Receive stock. Complete a cash sale.",
    category: "Retail · Responsive web",
    type: "FULL-STACK INVENTORY & CASH SALES",
    kind: "shopflow",
    author: "tniketha",
    stack: [
      "JavaScript",
      "Next.js",
      "React",
      "Tailwind CSS",
      "Node.js",
      "Express",
      "PostgreSQL",
      "SQL",
    ],
    description:
      "An inventory and cash-sales workspace for a small shop. Manage products and suppliers, receive purchases, complete cash checkout, and review saved sales in one responsive application.",
    problem:
      "Receiving stock and selling products must update the same inventory reliably. I built a clear product-to-purchase-to-sale workflow, with consistent stock records and accurate LKR amounts.",
    highlights: [
      "Products & supplier purchases",
      "Cash checkout & stock checks",
      "Overview & sales history",
    ],
    features: [
      "Overview with today’s sales, transaction count, product count, units in stock, and recent sales",
      "Search, add, edit, and archive products; manage categories and display product photos",
      "Manage suppliers and receive purchases at a stated unit cost to increase stock",
      "Choose products, enter whole-unit quantities and cash received, and save a sale",
      "View saved sale numbers, dates, and totals in sales history",
      "Session-based store isolation and owner/manager/cashier permissions enforced by the API",
      "Numbered SQL migrations with checksums and database constraints for stock and money",
    ],
    decisions: [
      {
        title: "Save stock and transactions together.",
        description:
          "Parameterized SQL through pg saves purchases or sales alongside stock changes in serializable transactions. Checkout locks product rows in a consistent order and checks stock; request keys prevent duplicate records on retry.",
      },
      {
        title: "Preserve accurate sale amounts.",
        description:
          "Prices use integer LKR cents, with decimal input parsed as text. Completed sales retain the product names and prices used at checkout, even when the catalogue changes.",
      },
      {
        title: "Keep database changes traceable.",
        description:
          "Numbered SQL migrations record checksums and skip previously applied files. Database constraints protect stock, money, and store relationships; migration tests check that existing store records are preserved.",
      },
    ],
    architecture: [
      {
        name: "Next.js + React",
        role: "Responsive forms and store screens",
      },
      {
        name: "Node.js + Express",
        role: "REST API, sessions & input checks",
      },
      {
        name: "PostgreSQL + pg",
        role: "Parameterized SQL, transactions & migrations",
      },
    ],
    screenshots: [
      {
        file: "01-dashboard-desktop.jpg",
        label: "Overview",
        alt: "ShopFlow Ceylon Corner overview with daily sales, stock totals and recent sales",
        caption:
          "Overview · Today’s sales, transactions, products, stock, and recent sales.",
      },
      {
        file: "02-inventory-desktop.jpg",
        label: "Inventory",
        alt: "ShopFlow current product inventory with photos, prices and stock",
        caption:
          "Inventory · Search and manage products, categories, and stock.",
      },
      {
        file: "05-purchases-desktop.jpg",
        label: "Purchases",
        alt: "ShopFlow supplier purchase screen for receiving product stock",
        caption: "Purchases · Receive supplier stock at a stated unit cost.",
      },
      {
        file: "03-pos-desktop.jpg",
        label: "Checkout",
        alt: "ShopFlow current cash checkout with products and basket",
        caption:
          "Point of sale · Select products, quantities, and cash received.",
      },
      {
        file: "06-sales-desktop.jpg",
        label: "Sales history",
        alt: "ShopFlow saved sales history with sale numbers, dates and totals",
        caption: "Sales history · Review saved cash transactions.",
      },
      {
        file: "08-dashboard-mobile.jpg",
        label: "Mobile overview",
        alt: "ShopFlow overview at a phone-sized browser width",
        caption:
          "Mobile overview · The same store totals in a responsive layout.",
      },
      {
        file: "09-pos-mobile.jpg",
        label: "Mobile checkout",
        alt: "ShopFlow cash checkout at a phone-sized browser width",
        caption:
          "Mobile checkout · Build and save a cash sale on a narrow screen.",
      },
      {
        file: "07-login-desktop.jpg",
        label: "Sign in",
        alt: "ShopFlow current sign-in screen with empty credential fields",
        caption: "Sign in · Access the store workspace with your account.",
      },
    ],
    scope:
      "A local full-stack project supporting cash payments and whole-unit stock. Screenshots show fictional Ceylon Corner store records. The source includes fresh-database setup helpers and unit and PostgreSQL integration tests.",
    repository: "https://github.com/tniketha/ShopFlow",
  },
];

export const email = "tn.niketha@gmail.com";
export const linkedin = "https://www.linkedin.com/in/niketha-thavaneswaran/";
