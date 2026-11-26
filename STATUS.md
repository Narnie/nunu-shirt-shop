# NARNIE & NUNU — setup status

Last updated: 2026-11-25

## Done

- **Repo**: `Narnie/nunu-shirt-shop` — Dawn-based Shopify theme
- **Branches**: `main` (stable) and `dev` (scratch) — both GitHub-connected as
  draft themes in Shopify; **`dev` is currently the published theme**
- **Storefront**: live but private (password page on). Domain:
  `narnienunu.myshopify.com`
- **Store name**: `NARNIE & NUNU` set in admin
- **Look**: gallery-minimal — Jost type, quiet header wordmark, stencil-dog
  hero, "Designed by Narnie, starring Nunu" tagline, "See the prints" CTA,
  eco announcement bar
- **Sections**: custom `nunu-hero.liquid` (image picker falls back to stencil
  asset); `assets/nunu-mark.png` square head-crop for favicon/footer use
- **About page**: created via API with `about` template; nav = Home · Catalog ·
  Contact · About
- **Automation**: `scripts/setup-store.py` — idempotent store provisioning via
  Admin API (client-credentials in `.env`, gitignored)
- **CI**: `theme-check.yml` runs `shopify theme check` on pushes to main/dev
- **Brand assets**: `brand/` has source logos/SVGs

## Left — store ops (admin-side)

- [ ] **Gelato app** — install in Shopify, create first product
      (organic blank: Stanley/Stella or Econscious; see README tier list)
- [ ] **Payments** — activate Shopify Payments; toggle PayPal
- [ ] **Shipping** — review rates vs Gelato's per-product shipping costs
- [ ] **Plan** — pick Shopify plan to drop the storefront password
- [ ] **Custom domain** — `narnienunu.art` / `narnienunu.com` appeared
      unregistered (verify at checkout); connect in admin after buying
- [ ] **Store email** — see notes below
- [ ] **Test prints** — see notes below
- [ ] **Instagram business** — see notes below

## Left — theme-side (repo)

- [ ] Footer pass (stock Dawn still; add nunu-mark + brand line)
- [ ] Favicon — upload `nunu-mark.png` in Theme settings
- [ ] Real hero/logo image once brand art is final (picker overrides stencil)
- [ ] About page photo of Nunu (image slot is ready)
- [ ] Merge `dev` → `main`, republish `main` as live, return `dev` to scratch
- [ ] Optional: sustainability strip / values section below hero

## Notes on open questions

### Store email

Shopify doesn't host email. Options:

- **Free-ish**: domain registrar forwarding (e.g. `hello@narnienunu.art` → your
  personal inbox) + Gmail "Send mail as" for replies. Cheapest, slightly hacky.
- **Zoho Mail** — has a legit free/very cheap tier for custom-domain email.
- **Google Workspace** — ~$6/mo, most polished (Gmail on your domain).
- Needs the custom domain first, so order: domain → email.

### Test prints

In the Gelato dashboard you can place **sample orders** (discounted cost).
Order 1–2 before launch — the stencil is high-contrast B/W, the things to
check are print sharpness on fabric, ink density (pure black can print
charcoal-ish on DTG), and whether white-on-dark garments need underbase.
Also sanity-check the print size on the mockup vs reality.

### PayPal / business details privacy

- **Shopify Payments** legal name/address is KYC-only — never customer-facing.
- **PayPal**: buyers see your *business name* and business email at checkout.
  Your address/phone aren't shown on standard card transactions, but CAN
  appear on invoices/payment-request receipts. If your PayPal account is
  still an individual type, your **personal name may show** — set/upgrade the
  business name to `NARNIE & NUNU`.
- Biggest exposure point is usually the **return/shipping address** — POD
  dodges this entirely: Gelato ships from their facility, your home address
  never reaches customers.
- If still uncomfortable later: a registered agent/virtual mailbox address is
  the standard fix, but likely unnecessary at this scale.
- Also worth verifying domain WHOIS privacy when registering the domain
  (usually on by default).

### Instagram business + agent access

- Setup: IG business account → link a Facebook Page in **Meta Business
  Suite** (required for API/scheduling access).
- "Agent access" options, easiest first:
  1. **Me drafting, you posting** — content calendar, captions, image picks.
     Zero setup.
  2. **Meta Business Suite People access** — needs a real human FB profile;
     can't add a bot directly.
  3. **API publishing** — Meta app + IG Graph API content publishing; needs
     business account + FB page link + permissions review. Real project,
     doable but a lift.
- Recommend starting with option 1 while the store is built; revisit API
  once there's product content worth scheduling.
