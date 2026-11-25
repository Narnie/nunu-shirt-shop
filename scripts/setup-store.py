#!/usr/bin/env python3
"""Provision store content via the Shopify Admin API.

Creates the About page (template suffix `about`) and adds it to the
main navigation menu. Idempotent: safe to re-run.

Reads credentials from .env:
  SHOPIFY_CLIENT_ID, SHOPIFY_CLIENT_SECRET, SHOPIFY_STORE
"""

import json
import os
import sys
import urllib.request

API_VERSION = "2025-10"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_env():
    env = {}
    with open(os.path.join(REPO_ROOT, ".env")) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k] = v
    missing = {"SHOPIFY_CLIENT_ID", "SHOPIFY_CLIENT_SECRET", "SHOPIFY_STORE"} - env.keys()
    if missing:
        sys.exit(f"Missing in .env: {', '.join(sorted(missing))}")
    return env


def post(url, payload, token=None):
    headers = {"Content-Type": "application/json"}
    if token:
        headers["X-Shopify-Access-Token"] = token
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers=headers, method="POST"
    )
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read())


def mint_token(store, client_id, client_secret):
    url = f"https://{store}.myshopify.com/admin/oauth/access_token"
    resp = post(
        url,
        {
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials",
        },
    )
    if "access_token" not in resp:
        sys.exit(f"Token exchange failed: {resp}")
    return resp["access_token"]


def gql(store, token, query, variables=None):
    url = f"https://{store}.myshopify.com/admin/api/{API_VERSION}/graphql.json"
    resp = post(url, {"query": query, "variables": variables or {}}, token)
    if "errors" in resp:
        sys.exit(f"GraphQL errors: {resp['errors']}")
    return resp["data"]


def ensure_about_page(store, token):
    data = gql(
        store,
        token,
        """{ pages(first: 50) { nodes { id title handle } } }""",
    )
    for p in data["pages"]["nodes"]:
        if p["handle"] == "about":
            print(f"About page exists: {p['id']}")
            return p["id"]

    data = gql(
        store,
        token,
        """
        mutation pageCreate($page: PageCreateInput!) {
          pageCreate(page: $page) {
            page { id title handle }
            userErrors { field message }
          }
        }
        """,
        {"page": {"title": "About", "templateSuffix": "about", "isPublished": True}},
    )
    errs = data["pageCreate"]["userErrors"]
    if errs:
        sys.exit(f"pageCreate errors: {errs}")
    page = data["pageCreate"]["page"]
    print(f"Created About page: {page['id']}")
    return page["id"]


def ensure_menu_item(store, token, page_id):
    data = gql(
        store,
        token,
        """
        { menus(first: 20) { nodes { id handle title items { id title type url resourceId } } } }
        """,
    )
    menu = next((m for m in data["menus"]["nodes"] if m["handle"] == "main-menu"), None)
    if not menu:
        sys.exit("No menu with handle 'main-menu' found")

    existing = menu["items"]
    if any(i["title"].lower() == "about" for i in existing):
        print("About already in main menu")
        return

    items = [
        {k: v for k, v in i.items() if v is not None}
        for i in existing
    ]
    items.append({"title": "About", "type": "PAGE", "resourceId": page_id})

    data = gql(
        store,
        token,
        """
        mutation menuUpdate($id: ID!, $title: String!, $items: [MenuItemUpdateInput!]!) {
          menuUpdate(id: $id, title: $title, items: $items) {
            menu { id items { id title } }
            userErrors { field message }
          }
        }
        """,
        {"id": menu["id"], "title": menu["title"], "items": items},
    )
    errs = data["menuUpdate"]["userErrors"]
    if errs:
        sys.exit(f"menuUpdate errors: {errs}")
    titles = [i["title"] for i in data["menuUpdate"]["menu"]["items"]]
    print(f"Menu now: {' · '.join(titles)}")


def main():
    env = load_env()
    token = mint_token(
        env["SHOPIFY_STORE"], env["SHOPIFY_CLIENT_ID"], env["SHOPIFY_CLIENT_SECRET"]
    )
    print("Token minted")
    page_id = ensure_about_page(env["SHOPIFY_STORE"], token)
    ensure_menu_item(env["SHOPIFY_STORE"], token, page_id)


if __name__ == "__main__":
    main()
