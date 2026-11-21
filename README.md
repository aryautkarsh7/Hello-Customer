# Hello Customer

A responsive 15-page prelaunch website, based on the supplied Hello Customer brand kit and Brand & Website Content Brief.

## Run

No installation or external dependencies are required. With Node and Python available:

```sh
npm run build
npm run dev
```

Open http://localhost:4173. To check JavaScript syntax, run `npm run check`.

`dist/` is the deployable static website. `build.mjs` generates the pages; shared presentation and browser interactions are in `dist/styles.css` and `dist/app.js`. The `assets/branding/` tree is copied from the supplied kit. Brand vectors and their original Lottie scale keyframes are rendered locally without a third-party animation runtime.

## Included

Home, Features, How It Works, Pricing, About, Contact, FAQ, Privacy, Terms, Refund & Cancellation, Cookies, Acceptable Use, Data Deletion, Grievance and Disclaimer.

Interactive business tabs support arrow keys, Home and End. The sample message editor has 12 fixed samples and copy controls. The modal supports Escape and returns focus. The contact form validates entries, prepares a message locally and lets visitors copy it for sharing with SaralKaro. Nothing is submitted or stored by the form. No payment, account creation, real AI generation or WhatsApp delivery is implemented by this marketing site.

## Confirmed public information

The site publishes the owner-confirmed SaralKaro business identity and contact details, ₹399 monthly software subscription, one-month trial, five-day conditional refund policy, cancellation explanation and Udyam number. Hello Customer remains under development, so the site uses early-access language and clearly labels unavailable integrations and planned AI functionality.

The contact form prepares an enquiry locally and offers the verified support email; it does not transmit or store form data. A delivery backend is still required before the form can truthfully show a submitted confirmation.

## Validation and hosting status

Run `npm run build` and `npm run check` before deployment. `dist/` remains generated output and is not committed in the parent monorepo.
