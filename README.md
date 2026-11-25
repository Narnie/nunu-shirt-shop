# nunu-shirt-shop

Storefront theme for the **NARNIE & NUNU** art shop — print-on-demand apparel
featuring Nunu the smooth collie, fulfilled by [Gelato](https://gelato.com).

## Architecture

- **Shopify** — store engine. Handles checkout, payments, taxes, shipping,
  order emails. No custom backend.
- **Gelato app for Shopify** — print-on-demand fulfillment. Products are
  designed in Gelato, synced to Shopify, and orders auto-route to Gelato for
  printing and shipping.
- **This repo** — the Shopify theme (based on [Dawn](https://github.com/Shopify/dawn),
  Shopify's reference Online Store 2.0 theme). Customization is done in the
  theme editor and in the Liquid/JSON files here.

## Workflow

1. Install the Shopify CLI: `npm install -g @shopify/cli @shopify/theme`
2. `shopify theme dev --store <your-store>.myshopify.com` — live-reload local dev
3. `shopify theme push` — upload to the store as an unpublished theme, or wire
   **Shopify → Online Store → Themes → Add theme → Connect from GitHub** so
   pushes to `main` deploy automatically.
4. `shopify theme check` — lint the theme before committing (config in
   `.theme-check.yml`).

## Brand

`brand/` holds source brand assets (NARNIE mosaic logos, SVGs). The web-ready
logo is `assets/nunu-logo.png`; assign it via
**Theme editor → Theme settings → Logo** (and favicon) — the image pickers read
from store media, so upload the logo there once.

## Products — sustainable garment picks

In the Gelato catalog, prefer these blanks when creating products
(from most to least sustainable). Certifications listed are what to cite on
product pages:

| Tier | Brand | Notes |
|------|-------|-------|
| Best | Stanley/Stella | 100% GOTS organic cotton / recycled, Fair Wear, PETA-vegan |
| Best | Econscious | Organic cotton blanks, GOTS/OCS, budget-friendly |
| Best | Allmade | Carbonfree® certified, Repreve + organic cotton tri-blends, fair-wage Haiti factories |
| Good | Bella+Canvas | WRAP, Fair Labor, bluesign dye house, solar-powered cutting (3001 = classic POD tee) |
| Good | AS Colour | BCI member, OEKO-TEX, published supply chain |
| OK   | B&C | Fair Wear member; use its organic/recycled lines |
| OK   | District Re-Tee | 100% recycled, no re-dye (Re-Tee/Re-Fleece lines only) |
| OK   | Comfort Colors | Garment-dyed durability; Gildan-owned |

Avoid building claims on: Gildan, Fruit of the Loom, Jerzees, Champion,
Just Cool, Cotton Heritage.

**Caveat:** Gelato may substitute an equivalent garment per region — prefer
products whose listed alternatives are all in the top two tiers, and market
the print-on-demand story itself (made-to-order, local production, no
unsold stock).
