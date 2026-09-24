#!/usr/bin/env python3
"""Radar semanal: consulta las APIs publicas de Greenhouse/Lever/Ashby y hace diff.

Uso:  python check.py            # consulta, guarda snapshot, muestra diff
Lee las empresas de companies.csv y filtra los titulos por KEYWORDS (ajustalo a tu rol).
"""
import csv, json, re, sys, urllib.request
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
# Palabras clave del TITULO del puesto que te interesan. Ajustalas a tu perfil.
KEYWORDS = re.compile(r"data|scien|engineer|analyst|research", re.I)


def fetch(url):
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.load(r)
    except Exception as e:
        return {"_error": str(e)}


def jobs_for(ats, slug):
    if ats in ("greenhouse", "greenhouse-eu"):
        host = "boards-api.eu.greenhouse.io" if ats == "greenhouse-eu" else "boards-api.greenhouse.io"
        d = fetch(f"https://{host}/v1/boards/{slug}/jobs")
        if "_error" in d:
            return None, d["_error"]
        return [{"id": j["id"], "title": j["title"],
                 "location": j.get("location", {}).get("name", ""),
                 "url": j.get("absolute_url", "")} for j in d.get("jobs", [])], None
    if ats == "lever":
        d = fetch(f"https://api.lever.co/v0/postings/{slug}?mode=json")
        if isinstance(d, dict) and "_error" in d:
            return None, d["_error"]
        return [{"id": j["id"], "title": j["text"],
                 "location": j.get("categories", {}).get("location", ""),
                 "url": j.get("hostedUrl", "")} for j in d], None
    if ats == "ashby":
        d = fetch(f"https://api.ashbyhq.com/posting-api/job-board/{slug}")
        if "_error" in d:
            return None, d["_error"]
        return [{"id": j["id"], "title": j["title"],
                 "location": j.get("location", ""),
                 "url": j.get("jobUrl", "")} for j in d.get("jobs", [])], None
    return None, f"ats '{ats}' sin soporte (verificar a mano)"


def main():
    snap_file = HERE / "snapshot.json"
    prev = json.loads(snap_file.read_text(encoding="utf-8")) if snap_file.exists() else {}
    curr, errors = {}, []
    with open(HERE / "companies.csv", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            ats, slug, name = row["ats"].strip(), row["slug"].strip(), row["empresa"]
            if ats in ("verificar", "workday", ""):
                continue
            jobs, err = jobs_for(ats, slug)
            if err:
                errors.append(f"  {name}: {err}")
                continue
            curr[name] = {str(j["id"]): j for j in jobs if KEYWORDS.search(j["title"])}
    new = removed = 0
    for name, jobs in curr.items():
        p = prev.get(name, {})
        for jid, j in jobs.items():
            if jid not in p:
                print(f"[NUEVA] {name}: {j['title']} ({j['location']})")
                print(f"        {j['url']}")
                new += 1
        for jid, j in p.items():
            if jid not in jobs:
                print(f"[cerrada] {name}: {j['title']}")
                removed += 1
    snap_file.write_text(json.dumps(curr, indent=1, ensure_ascii=False), encoding="utf-8")
    total = sum(len(v) for v in curr.values())
    print(f"\n{date.today()} - {total} vacantes relevantes en {len(curr)} empresas | {new} nuevas | {removed} cerradas")
    if errors:
        print("Errores (revisar slug/ats en companies.csv):")
        print("\n".join(errors))


if __name__ == "__main__":
    main()
