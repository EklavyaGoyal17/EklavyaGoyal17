<!-- ═══════════════════════════ HEADER ═══════════════════════════ -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,45:0e7490,100:7c3aed&height=220&section=header&text=Eklavya%20Goyal&fontSize=64&fontColor=ffffff&fontAlignY=36&desc=I%20build%20systems%20that%20stay%20correct%20when%20things%20go%20wrong&descSize=18&descAlignY=58&animation=fadeIn" width="100%" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&pause=900&color=22D3EE&center=true&vCenter=true&width=760&lines=Incoming+SWE+Intern+%40+American+Express+(Summer+2027);Ledgers+that+never+lose+a+rupee+under+races;Permission+systems+for+autonomous+AI+agents;Bluetooth+mesh+SOS+for+when+the+towers+go+dark;B.Tech+CSE+%40+VIT+Vellore+%C2%B7+CGPA+9.69" alt="Typing SVG" />
  </a>
</p>

<p align="center">
  <a href="https://eklavyagoyal17.github.io/"><img src="https://img.shields.io/badge/Portfolio-0e7490?style=for-the-badge&logo=googlechrome&logoColor=white" /></a>
  <a href="https://www.linkedin.com/in/eklavya-goyal-9b2aa0309"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" /></a>
  <a href="https://leetcode.com/u/eklavya_goyal/"><img src="https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=black" /></a>
  <a href="mailto:eklavyagoyal108@gmail.com"><img src="https://img.shields.io/badge/Email-7c3aed?style=for-the-badge&logo=gmail&logoColor=white" /></a>
  <img src="https://komarev.com/ghpvc/?username=EklavyaGoyal17&style=for-the-badge&color=0e7490&label=PROFILE+VIEWS" />
</p>

---

### `$ whoami`

```go
type Engineer struct {
    Name      string
    Now       []string
    Obsessed  []string
    Principle string
}

var eklavya = Engineer{
    Name: "Eklavya Goyal · B.Tech CSE @ VIT Vellore ('28)",
    Now: []string{
        "Incoming SWE Intern @ American Express — Summer 2027",
        "Building AEGIS: authorization that lives outside the model",
        "Taking HaalChaal (AI check-in calls for parents) to its first pilot",
    },
    Obsessed:  []string{"concurrency", "idempotency", "failure modes", "audit trails"},
    Principle: "If a number is on the dashboard, a run you can inspect produced it.",
}
```

---

### 🛰️ Flagship systems

<table>
<tr>
<td width="50%" valign="top">

#### 🛡️ [AEGIS](https://github.com/EklavyaGoyal17/AEGIS)
**The permission system for AI agents.** An agent may *ask* to act; AEGIS decides — independently of the model. Fail-closed policy engine (`DENY > REQUIRE_APPROVAL > ALLOW`), digest-bound human approvals, a gateway that executes **exactly once**, and a hash-chained append-only audit log.

`TypeScript` `Fastify` `Next.js` `PostgreSQL` `Ed25519` `OpenAPI 3.1`

</td>
<td width="50%" valign="top">

#### 💸 [LedgerCore](https://github.com/EklavyaGoyal17/LedgerCore)
**A transaction-safe double-entry ledger.** Built around the failures that actually happen: a response lost after commit, two requests racing for the same funds, a broker down after a transfer. Durable idempotent replay, transactional outbox → Kafka, independent reconciliation.

`Java 21` `Spring Boot` `PostgreSQL` `Kafka` `Redis` `OpenTelemetry`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🔬 [FORGE](https://github.com/EklavyaGoyal17/Forge)
**A lab for watching code misbehave.** Every experiment runs in its own sandboxed JVM. An interleaving explorer enumerates *every* schedule to find the race; a liveness explorer finds livelock and starvation. Coordinated-omission-corrected load testing, JFR, JMH, and honest bootstrap statistics.

`Java` `JFR` `JMH` `Testcontainers` `React` `Docker`

</td>
<td width="50%" valign="top">

#### 📞 [HaalChaal](https://github.com/EklavyaGoyal17/haalchaal)
**An AI that calls your parents every day.** In their own language, on an ordinary phone — checks wellbeing and medicines, remembers earlier calls, and WhatsApps the family a summary, with instant alerts when something sounds wrong. Pre-pilot with Indian families.

`Go` `PostgreSQL` `Voice AI` `Claude` `WhatsApp Cloud API`

</td>
</tr>
<tr>
<td width="50%" valign="top">

#### 🚨 [MeshSOS](https://github.com/EklavyaGoyal17/MeshSOS)
**SOS when the towers go dark.** A BLE mesh that relays compact distress payloads phone-to-phone, multi-hop, with no SIM or internet — plus offline maps, a "Good Samaritan" radar, and a UI in 7 Indian languages.

`Java` `Android` `Bluetooth LE` `OSMDroid` `Firebase`

</td>
<td width="50%" valign="top">

#### 🛺 [Vapi Hustle](https://github.com/EklavyaGoyal17/Game)
**An open-world game on ~200 km² of real streets.** Vapi & Daman rebuilt in the browser: 9,241 streets, 94,700 buildings, bullet trains on the viaduct. New data pipeline, map, missions and characters on the Madras Hustle engine. Plays with a PS controller.

`JavaScript` `Three.js` `OpenStreetMap / Overture data`

</td>
</tr>
</table>

<details>
<summary><b>📂 More builds (click to expand)</b></summary>
<br/>

| Project | What it is | Stack |
|---|---|---|
| [ATLAS](https://github.com/EklavyaGoyal17/ATLAS) | Local engineering lab: synthetic payment workflows, incident recipes with traces, Java code intelligence, cited evidence assistant | Java · Spring · React · Postgres |
| [LifeLine](https://github.com/EklavyaGoyal17/DBMS-Project) | Blood bank system — donor eligibility → TTI screening → FEFO allocation → vein-to-vein audit trail | Oracle 21c · PL/SQL · Node.js |
| [SmartCity IAQ Node](https://github.com/EklavyaGoyal17/SmartCity-IAQ-Node) | IoT air-quality proxy via occupancy sensing, closed-loop ventilation relay | Arduino · Node.js · React |
| [Aequitas](https://github.com/EklavyaGoyal17/aequitas) | Research ledger benchmarking OCC / 2PL / SSI / adaptive CC under skewed load (conference paper) | Go · TLA+ · Python |
| [Lab-PC Fit Checker](https://github.com/EklavyaGoyal17/Cisco-Lab-PC-Software-Fit-Checker) | Matches software profiles to lab machines by OS, RAM and tool versions | Java |

</details>

---

### 🧰 Toolbox

<p align="center">
  <img src="https://skillicons.dev/icons?i=java,go,ts,py,cpp,js&perline=6" /><br/>
  <img src="https://skillicons.dev/icons?i=spring,nodejs,nextjs,react,tailwind,threejs,androidstudio&perline=7" /><br/>
  <img src="https://skillicons.dev/icons?i=postgres,redis,kafka,firebase,docker,githubactions,linux,git&perline=8" />
</p>

---

### 📊 Telemetry

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=EklavyaGoyal17&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=EklavyaGoyal17&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" />
</p>
<p align="center">
  <img height="165" src="https://streak-stats.demolab.com?user=EklavyaGoyal17&theme=tokyonight&hide_border=true" />
  <img height="165" src="https://leetcard.jacoblin.cool/eklavya_goyal?theme=dark&font=JetBrains%20Mono&ext=heatmap" />
</p>

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/EklavyaGoyal17/EklavyaGoyal17/output/github-contribution-grid-snake-dark.svg" />
    <img alt="contribution snake" src="https://raw.githubusercontent.com/EklavyaGoyal17/EklavyaGoyal17/output/github-contribution-grid-snake.svg" />
  </picture>
</p>

---

### 🧠 How I think about software

```text
1. Correctness first. A fast ledger that loses money is a fast bug.
2. Make failure boring. Retries, replays, crashes — design for them on day one.
3. Authority lives outside the model. Never trust the thing you're guarding.
4. Show the evidence. Tests, traces and audit logs over adjectives.
```

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:7c3aed,55:0e7490,100:0d1117&height=110&section=footer" width="100%" />
</p>
