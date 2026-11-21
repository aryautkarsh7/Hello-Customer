import { existsSync, readFileSync } from 'node:fs';

const routes = [
  '',
  'about',
  'acceptable-use',
  'contact',
  'cookie-policy',
  'data-deletion',
  'disclaimer',
  'faq',
  'features',
  'grievance',
  'how-it-works',
  'pricing',
  'privacy-policy',
  'refund-policy',
  'terms',
];

const pages = new Map(
  routes.map((route) => {
    const path = route ? `dist/${route}/index.html` : 'dist/index.html';
    if (!existsSync(path)) throw new Error(`Missing generated route: /${route}`);
    return [route, readFileSync(path, 'utf8')];
  }),
);

const allPages = [...pages.values()].join('\n');
const stalePhrases = [
  /pricing to be announced/i,
  /prices? (?:are |being )?finalized/i,
  /contact details? (?:have |has )?not been supplied/i,
  /privacy contact (?:information )?(?:has |is )?not/i,
  /no support inbox configured/i,
  /refund terms? (?:are |being )?finalized/i,
  /trial length (?:is )?not confirmed/i,
  /launch pricing to be announced/i,
];

for (const phrase of stalePhrases) {
  if (phrase.test(allPages)) throw new Error(`Outdated public copy found: ${phrase}`);
}

const required = [
  ['', ['₹399/month', 'one-month free trial']],
  ['contact', ['SaralKaro', 'mailto:support.hellocustomer@saralkaro.app', 'tel:+918102309095']],
  ['privacy-policy', ['Privacy contact', 'support.hellocustomer@saralkaro.app']],
  ['terms', ['₹399 per month', 'one-month trial', 'WhatsApp messaging charges are separate']],
  ['refund-policy', ['five calendar days', 'no campaign has been run', 'statutory rights remain unaffected']],
  ['data-deletion', ['Data Deletion Request', 'support.hellocustomer@saralkaro.app']],
  ['grievance', ['F311, Tulsiani Easy In Homes', 'responsible grievance contact']],
  ['pricing', ['₹399/month', 'ONE MONTH FREE TRIAL']],
  ['faq', ['₹399 per month', 'one-month free trial']],
];

for (const [route, phrases] of required) {
  const html = pages.get(route);
  for (const phrase of phrases) {
    if (!html.includes(phrase)) throw new Error(`Missing "${phrase}" on /${route}`);
  }
}

const footerMarker = 'Udyam No: UDYAM-HR-05-0188662';
for (const [route, html] of pages) {
  if (!html.includes(footerMarker)) throw new Error(`Shared footer missing on /${route}`);
}

console.log(`Verified ${routes.length} generated routes and confirmed public information.`);
