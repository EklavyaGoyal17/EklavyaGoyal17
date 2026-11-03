#!/usr/bin/env python3
"""Self-hosted GitHub telemetry cards for the profile README.
Draws dist/telemetry.svg (stats + streak + languages) and dist/pulse.svg
(contribution grid with a beacon sweep). No third-party services, no deps."""
import json, os, sys, urllib.request, datetime as dt
from collections import defaultdict

LOGIN = os.environ.get("GH_LOGIN", "EklavyaGoyal17")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
OUT = os.environ.get("OUT_DIR", "dist")

N="#07090C"; H="#0D1116"; H2="#131921"; R="#1D252F"; R2="#2A3440"
I="#E9ECEF"; D="#8F9AA7"; F="#5C6876"; B="#FFB547"
SANS="'Bricolage Grotesque','Segoe UI',Inter,'Helvetica Neue',Arial,sans-serif"
MONO="'Geist Mono',ui-monospace,SFMono-Regular,Menlo,Consolas,'Liberation Mono',monospace"
LEVEL={"NONE":0,"FIRST_QUARTILE":1,"SECOND_QUARTILE":2,"THIRD_QUARTILE":3,"FOURTH_QUARTILE":4}
CELL=["#131921","#4d3612","#86591a","#c4862a","#FFB547"]
SHADES=["#FFB547","#E39A36","#BF7F2B","#996522","#734C1A","#4F3514"]

def gql(query, variables):
    req = urllib.request.Request("https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {TOKEN}", "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if "errors" in body: sys.exit(f"GraphQL error: {body['errors']}")
    return body["data"]

MAIN = """query($login:String!){ user(login:$login){
  createdAt followers{totalCount}
  repositories(ownerAffiliations:OWNER,isFork:false,privacy:PUBLIC,first:100){ totalCount
    nodes{ stargazerCount languages(first:10,orderBy:{field:SIZE,direction:DESC}){ edges{ size node{name} } } } }
  contributionsCollection{ totalCommitContributions restrictedContributionsCount
    totalPullRequestContributions totalIssueContributions totalRepositoriesWithContributedCommits
    contributionCalendar{ totalContributions weeks{ contributionDays{ date contributionCount contributionLevel } } } } } }"""
YEAR = """query($login:String!,$from:DateTime!,$to:DateTime!){ user(login:$login){
  contributionsCollection(from:$from,to:$to){ contributionCalendar{ totalContributions
    weeks{ contributionDays{ date contributionCount } } } } } }"""

def fetch():
    u = gql(MAIN, {"login": LOGIN})["user"]
    created = dt.date.fromisoformat(u["createdAt"][:10]); today = dt.date.today()
    alldays = {}; alltotal = 0
    for y in range(created.year, today.year + 1):
        f = dt.datetime(y,1,1); t = min(dt.datetime(y,12,31,23,59,59), dt.datetime.combine(today, dt.time(23,59,59)))
        c = gql(YEAR, {"login": LOGIN, "from": f.isoformat()+"Z", "to": t.isoformat()+"Z"})["user"]["contributionsCollection"]["contributionCalendar"]
        alltotal += c["totalContributions"]
        for w in c["weeks"]:
            for d in w["contributionDays"]: alldays[d["date"]] = d["contributionCount"]
    return u, alldays, alltotal

def streaks(days):
    ds = sorted(days); longest = run = 0; prev = None
    for k in ds:
        d = dt.date.fromisoformat(k)
        if days[k] > 0:
            run = run + 1 if prev and (d - prev).days == 1 and days[prev.isoformat()] > 0 else 1
            longest = max(longest, run)
        prev = d
    cur = 0; d = dt.date.fromisoformat(ds[-1])
    if days.get(d.isoformat(), 0) == 0: d -= dt.timedelta(days=1)   # today not over yet
    while days.get(d.isoformat(), 0) > 0: cur += 1; d -= dt.timedelta(days=1)
    return cur, longest

def esc(s): return str(s).replace("&","&amp;").replace("<","&lt;").replace(">","&gt;")
def fmt(n): return f"{n/1000:.1f}k" if n >= 10000 else f"{n:,}"

def telemetry_svg(u, days, alltotal):
    cc = u["contributionsCollection"]; cal = cc["contributionCalendar"]
    repos = u["repositories"]; stars = sum(n["stargazerCount"] for n in repos["nodes"])
    langs = defaultdict(int)
    for n in repos["nodes"]:
        for e in n["languages"]["edges"]: langs[e["node"]["name"]] += e["size"]
    top = sorted(langs.items(), key=lambda x: -x[1]); total = sum(langs.values()) or 1
    if len(top) > 6: top = top[:5] + [("Other", sum(v for _, v in top[5:]))]
    cur, longest = streaks(days)
    active = sum(1 for w in cal["weeks"] for d in w["contributionDays"] if d["contributionCount"] > 0)
    W, Hh = 1280, 300
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" role="img" aria-label="GitHub telemetry: {cal["totalContributions"]} contributions in the last year, current streak {cur} days">',
         f'<style>.ring{{fill:none;stroke:{B};transform-origin:770px 132px;animation:p 3s ease-out infinite;opacity:0}}.r2{{animation-delay:1.5s}}@keyframes p{{0%{{transform:scale(.3);opacity:.7}}100%{{transform:scale(1.25);opacity:0}}}}'
         f'.bar{{transform-origin:left;animation:g 1.2s cubic-bezier(.2,.7,.2,1) both}}@keyframes g{{from{{transform:scaleX(0)}}}}</style>',
         f'<rect x=".5" y=".5" width="{W-1}" height="{Hh-1}" rx="16" fill="{H}" stroke="{R}"/>',
         f'<line x1="600" y1="32" x2="600" y2="{Hh-32}" stroke="{R}"/><line x1="940" y1="32" x2="940" y2="{Hh-32}" stroke="{R}"/>']
    # --- left: numbers
    s.append(f'<text x="40" y="52" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{F}">ACTIVITY · LAST 12 MONTHS</text>')
    cells = [(fmt(cal["totalContributions"]), "contributions"),
             (fmt(cc["totalCommitContributions"] + cc["restrictedContributionsCount"]), "commits"),
             (fmt(cc["totalPullRequestContributions"]), "pull requests"),
             (fmt(repos["totalCount"]), "public repos"),
             (fmt(active), "active days"),
             (fmt(cc.get("totalRepositoriesWithContributedCommits", 0)), "repos committed to")]
    for k, (v, l) in enumerate(cells):
        x = 40 + (k % 3) * 180; y = 122 + (k // 3) * 100
        s.append(f'<text x="{x}" y="{y}" font-family="{SANS}" font-size="44" font-weight="800" letter-spacing="-1" fill="{B if k==0 else I}">{esc(v)}</text>')
        s.append(f'<text x="{x+2}" y="{y+26}" font-family="{MONO}" font-size="12" letter-spacing="1" fill="{D}">{esc(l.upper())}</text>')
    # --- middle: streak beacon
    s.append(f'<text x="636" y="52" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{F}">STREAK</text>')
    s.append(f'<circle class="ring" cx="770" cy="132" r="62"/><circle class="ring r2" cx="770" cy="132" r="62"/>')
    s.append(f'<circle cx="770" cy="132" r="54" fill="{H2}" stroke="{B}" stroke-opacity=".55" stroke-width="2"/>')
    s.append(f'<text x="770" y="146" text-anchor="middle" font-family="{SANS}" font-size="44" font-weight="800" fill="{B}">{cur}</text>')
    s.append(f'<text x="770" y="220" text-anchor="middle" font-family="{MONO}" font-size="12" letter-spacing="1.5" fill="{I}">CURRENT · DAYS</text>')
    s.append(f'<text x="770" y="252" text-anchor="middle" font-family="{MONO}" font-size="12" letter-spacing="1" fill="{D}">longest  <tspan fill="{B}">{longest}</tspan>  days</text>')
    # --- right: languages
    s.append(f'<text x="976" y="52" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{F}">LANGUAGES · BY BYTES</text>')
    x = 976; bw = 264
    s.append(f'<clipPath id="bc"><rect x="976" y="74" width="{bw}" height="12" rx="6"/></clipPath><g clip-path="url(#bc)" class="bar">')
    for k, (n, v) in enumerate(top):
        w = bw * v / total; s.append(f'<rect x="{x:.1f}" y="74" width="{w+0.6:.1f}" height="12" fill="{SHADES[k]}"/>'); x += w
    s.append('</g>')
    for k, (n, v) in enumerate(top):
        y = 122 + k * 27
        s.append(f'<circle cx="982" cy="{y-4}" r="5" fill="{SHADES[k]}"/>')
        s.append(f'<text x="996" y="{y}" font-family="{SANS}" font-size="15" fill="{I}">{esc(n)}</text>')
        s.append(f'<text x="1240" y="{y}" text-anchor="end" font-family="{MONO}" font-size="13" fill="{D}">{100*v/total:.1f}%</text>')
    s.append('</svg>')
    return "".join(s)

def pulse_svg(u):
    weeks = u["contributionsCollection"]["contributionCalendar"]["weeks"]
    total = u["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    cs, gap, x0, y0 = 17, 5, 70, 74
    cols = len(weeks); W = 1280; Hh = y0 + 7 * (cs + gap) + 50
    rects, clip, months = [], [], []; last_m = None
    for c, w in enumerate(weeks):
        x = x0 + c * (cs + gap)
        for d in w["contributionDays"]:
            r = dt.date.fromisoformat(d["date"]).weekday(); r = (r + 1) % 7   # Sunday first
            y = y0 + r * (cs + gap); lv = LEVEL.get(d["contributionLevel"], 0)
            glow = f' filter="url(#gl)"' if lv >= 3 else ""
            rects.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" rx="4" fill="{CELL[lv]}"{glow}><title>{d["contributionCount"]} on {d["date"]}</title></rect>')
            clip.append(f'<rect x="{x}" y="{y}" width="{cs}" height="{cs}" rx="4"/>')
        m = dt.date.fromisoformat(w["contributionDays"][0]["date"]).strftime("%b")
        if m != last_m and c < cols - 2:
            months.append(f'<text x="{x}" y="{y0-14}" font-family="{MONO}" font-size="12" fill="{F}">{m}</text>'); last_m = m
    gx1 = x0 + cols * (cs + gap)
    days_lbl = "".join(f'<text x="{x0-14}" y="{y0 + r*(cs+gap) + 13}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{F}">{t}</text>' for r, t in ((1,"Mon"),(3,"Wed"),(5,"Fri")))
    legend = "".join(f'<rect x="{1120 + k*22}" y="{Hh-34}" width="15" height="15" rx="4" fill="{CELL[k]}"/>' for k in range(5))
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{Hh}" viewBox="0 0 {W} {Hh}" role="img" aria-label="{total} contributions in the last year">
<style>.sweep{{animation:sw 6s cubic-bezier(.45,0,.55,1) infinite}}@keyframes sw{{from{{transform:translateX(-260px)}}to{{transform:translateX({gx1}px)}}}}</style>
<defs>
<linearGradient id="beam" x1="0" x2="1"><stop offset="0" stop-color="{B}" stop-opacity="0"/><stop offset=".8" stop-color="{B}" stop-opacity=".38"/><stop offset="1" stop-color="{B}" stop-opacity=".9"/></linearGradient>
<clipPath id="cells">{"".join(clip)}</clipPath>
<filter id="gl" x="-60%" y="-60%" width="220%" height="220%"><feGaussianBlur stdDeviation="2.4" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
</defs>
<rect x=".5" y=".5" width="{W-1}" height="{Hh-1}" rx="16" fill="{H}" stroke="{R}"/>
<text x="40" y="36" font-family="{MONO}" font-size="12" letter-spacing="2" fill="{F}">CONTRIBUTION MESH</text>
<text x="{W-40}" y="36" text-anchor="end" font-family="{SANS}" font-size="16" font-weight="700" fill="{I}"><tspan fill="{B}">{total:,}</tspan> contributions in the last year</text>
{"".join(months)}{days_lbl}{"".join(rects)}
<g clip-path="url(#cells)"><rect class="sweep" x="0" y="{y0}" width="260" height="{7*(cs+gap)}" fill="url(#beam)"/></g>
<text x="1110" y="{Hh-22}" text-anchor="end" font-family="{MONO}" font-size="11" fill="{F}">less</text>{legend}
<text x="1234" y="{Hh-22}" font-family="{MONO}" font-size="11" fill="{F}">more</text>
<text x="40" y="{Hh-22}" font-family="{MONO}" font-size="11" letter-spacing="1" fill="{F}">updated {dt.date.today().isoformat()} · self-hosted, no third-party cards</text>
</svg>'''

if __name__ == "__main__":
    if os.environ.get("MOCK"): u, days, alltotal = json.load(open(os.environ["MOCK"]))
    else: u, days, alltotal = fetch()
    os.makedirs(OUT, exist_ok=True)
    open(f"{OUT}/telemetry.svg", "w").write(telemetry_svg(u, days, alltotal))
    open(f"{OUT}/pulse.svg", "w").write(pulse_svg(u))
    print("wrote telemetry.svg and pulse.svg")
