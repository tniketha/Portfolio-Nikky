export const projects = [
 {
  title: 'Smart Attendance',
  subtitle: 'A simpler way to manage classroom attendance.',
  category: 'Full-stack application',
  type: 'WEB & MOBILE APPLICATION',
  stack: ['TypeScript', 'React Native', 'Expo', 'Node.js', 'Express', 'MongoDB', 'Prisma', 'Socket.IO'],
  description: 'A classroom attendance application for students, lecturers, and administrators. Students check in with rotating QR codes, while lecturers manage sessions, follow live attendance, and review correction requests.',
  features: [
   'Signed, rotating QR codes with expiry and duplicate check-in prevention',
   'Location checks for attendance sessions when enabled',
   'Separate student, lecturer, and administrator workflows',
   'Live lecturer rosters, student history, and attendance analytics',
   'Correction requests with lecturer review and audit records',
   'CSV attendance reports and light, dark, and system themes'
  ],
  kind: 'attendance',
  repository: 'https://github.com/tniketha/SmartAttendance'
 }
];
export type Project = typeof projects[number];
export const email='nikkytamilneshan@gmail.com';

export const linkedin='https://www.linkedin.com/in/niketha-thavaneswaran/';
