# Share-Meal

A complete, buildless HTML/CSS/JavaScript landing website for an early-stage food-sharing project. No frontend framework, paid dependencies, backend, or remote resources are required to display the site.

## Preview locally

Open `index.html` directly, or run `python3 -m http.server 8000` from this folder and visit http://localhost:8000. On Windows, `py` may replace `python3`.

## Configure before publishing

Edit `site.config.json`:

- `siteUrl`: the final HTTPS URL, including the repository path, e.g. `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/`. This example is documentation, not a deployed address.
- `contactEmail`: leave empty until a real, approved project email is supplied.
- `repositoryUrl`: the supplied project URL; verify its availability.

Run `python3 scripts/configure.py`. It generates browser configuration, canonical/Open Graph URLs, robots.txt, sitemap.xml, and nested-path-safe 404 links. Run again whenever configuration changes. The base package intentionally does not invent a canonical hostname; its sitemap remains empty until configured. Use the final canonical URL before first deployment. If changing to another domain after configuring, start from the original 404.html or update its absolute paths as well.

## Publish free on GitHub Pages

1. Sign in to GitHub and create a **public** repository for this landing website. Using a separate repository avoids replacing application source. Do not upload private keys, Firebase service accounts, or other application secrets.
2. Set `siteUrl` to `https://YOUR-USERNAME.github.io/YOUR-REPOSITORY/` and run the configuration command above.
3. Upload this folder’s **contents**, with `index.html` at the repository root. Preserve assets subfolders. Include `.nojekyll`.
4. Open repository **Settings → Pages**. Under Build and deployment, select **Deploy from a branch**, then `main` and `/ (root)`, and Save.
5. Wait for the Pages deployment to finish. Open the URL GitHub displays. This package has not been deployed from this session.
6. Verify the home page, mobile menu, FAQ, screenshot images, privacy page, repository link, and a deliberately nonexistent nested path. Check the console and network panel for errors. Confirm canonical and Open Graph tags use the deployed URL.

No form service is needed. A configured email opens the visitor’s mail app. To add a form later, connect a real provider endpoint, implement clear success/failure handling, and update the privacy notice before collecting data.

## Custom domain later

Add your domain in GitHub Pages settings and follow GitHub’s displayed DNS verification instructions. Set the canonical HTTPS domain in site.config.json, regenerate metadata, update absolute 404 paths, and commit. Enable HTTPS once DNS/certificate setup completes. DNS values depend on your domain and provider; use GitHub’s current instructions.

## Files

- index.html: full landing page
- privacy.html / 404.html: supporting pages
- assets/css/styles.css: tokens, responsive layouts, reduced-motion rules
- assets/js/main.js: accessible menu, date, configured links, progressive reveal
- assets/js/config.js: generated from site.config.json
- assets/images/: supplied prototype screenshots, original SVG illustration/logo, PNG social card
- favicon.svg: reusable locally served mark
- scripts/configure.py: metadata generation with Python standard library
- VALIDATION.md: checks and remaining manual verification

## Content and status

The source repository could not be retrieved in this environment. No implementation was independently verified. Supplied screenshots establish interface appearance only. Prototype, planned, and interface labels are conservative, not assertions of operational functionality. The website does not take food requests or registrations. Public availability, registration status, team history, safety procedures, service areas, and contact email remain unverified.

The supplied reference logo informed the food-and-community direction. The website uses a new reusable bowl-and-leaves SVG mark. Hero illustration and social card were created for this deliverable. Confirm permission to publicly distribute the supplied screenshots, including names/avatars visible in them, before release. No external imagery or font dependencies are used.

## Accessibility and graceful behavior

Navigation is visible without JavaScript. With JavaScript, the mobile toggle exposes expanded state; Escape closes it and restores focus. FAQ uses native details/summary. The page includes a skip link, visible focus styles, semantic headings, descriptive image text, local fonts, and reduced-motion support. Reveal effects never hide content while waiting for JavaScript. Screen images have fixed aspect ratios and local assets.
