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

## Launch details still needed

- Actual application screenshots and confirmation of released capabilities.
- A verified early-access collection endpoint or contact address.
- Final commercial pricing, billing and refund rules.
- Verified legal operator, business address, privacy and grievance channels.
- Finalized application policies based on actual data flows.

Current policy pages describe this website and identify outstanding prelaunch details without inventing them. All app capabilities and concept previews are clearly labelled.

## Validation and hosting status

JavaScript syntax checks pass. All generated page asset and route references resolve locally. All four supplied animation JSON files parse correctly.

Local HTTP preview was blocked by the environment's socket permissions. Site source publication was blocked by DNS resolution for the source Git host. Browser layout QA and deployment are therefore unverified. The retained Site identity is in `.openai/hosting.json`; reuse it when publishing rather than registering a second Site.
