# rogaircon.co.za

Under-construction holding page for Rog Aircon. Plain static HTML/CSS, no build step.

## Deploy (cPanel Git Version Control, zacp103.webway.host)

1. Push to GitHub (`main`).
2. cPanel → Git Version Control → Manage → Pull or Deploy → **Update from Remote** → **Deploy HEAD Commit**.

`.cpanel.yml` copies the site into `~/public_html/`. If rogaircon.co.za is an
addon domain on the account, change `DEPLOYPATH` to that domain's docroot.
Bump `styles.css?v=` in `index.html` whenever the CSS changes.
