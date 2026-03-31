# 🐷 Børnebank

Et digitalt lommepenge-system til familier. Hjælp børn med at lære om økonomi og ejerskab - uden at børnene behøver deres egen bankkonto.

## 🌟 Hvad er Børnebank?

Børnebank er **ikke en rigtig bank** - det er et værktøj til at styre børnenes lommepenge:

- **Forældrene** har pengene i deres egen bank (som altid)
- **Børnene** får en "virtuel" saldo i appen de kan se
- I får overført penge når der er behov (til fødselsdage, behov, etc.)

Det er en mellemting mellem kontanter og en rigtig bankkonto - perfekt til børn der er for små til eget Visakort.

## 🌟 Funktioner

### For forældre
- **Opret familie** - Start din egen familie-konto
- **Tilføj børn** - Tilføj børn med navn, fødselsdag og lommepenge
- **Transaktioner** - Registrer hvad børnene får ind (pligter, gaver) og ud (legetøj, sodavand, etc.)
- **Automatisk lommepenge** - Tilskrives hver fredag kl. 15
- **Rente** - Valgfri rente på opsparing (lærer børnene om renters rente)
- **Deling** - Del adgang med anden forælder via QR-kode eller link

### For børn
- **Saldo** - Altid opdateret oversigt over "deres" penge
- **Transaktioner** - Se seneste bevægelser (hvad fik jeg ind? hvad brugte jeg?)
- **Read-only** - Kan ikke ændre data (sikker)

## 📱 Installation

### PWA (Anbefalet)
1. Åbn https://asistent2fiwa.github.io/bornbank/ i din browser
2. **iOS:** Tryk på Del → "Tilføj til hjemmeskærm"
3. **Android:** Tryk på menu → "Installer app"

### Browser
Fungerer i alle moderne browsere:
- Chrome, Safari, Firefox, Edge

## 🔒 Sikkerhed & GDPR

**Hvad gemmes:**
- Fornavn (på barnet)
- Fødselsdag (for at beregne alder)
- Lommepenge-beløb og transaktioner

**GDPR:**
- Der gemmes **ingen** cpr-numre, adresser, telefonnumre eller andre personlige data
- Data opbevares lokalt på enheden og valgfrit i Supabase (krypteret forbindelse)
- Du kan altid slette alle data ved at slette appen/cachen

**Juridisk:** Da vi kun behandler fornavn og fødselsdag (ikke fødselsnummer), er der ingen GDPR-registrering nødvendig.

## 🛠️ Teknologi

- **Frontend:** HTML, CSS (Tailwind), JavaScript
- **Database:** Supabase (PostgreSQL) - valgfri cloud-synkring
- **Hosting:** GitHub Pages

## 📊 Datastruktur

```
Familie
├── id (unik kode)
├── parent_token (delings-kode)
└── data
    ├── children[]
    │   ├── id
    │   ├── name (fornavn)
    │   ├── birth (dd-mm-åååå)
    │   ├── age (beregnet)
    │   ├── piece (monopoly-brik)
    │   ├── allowance (lommepenge/uge)
    │   ├── saldo (nuværende balance)
    │   └── transactions[]
    │       ├── date
    │       ├── amount (beløb)
    │       └── desc (beskrivelse)
    └── interest
        ├── enabled
        ├── rate (rente %)
        ├── freq (1=måned, 3=kvartal, 12=år)
        └── lastInterest
```

## 🎨 Temaer

Appen har 6 temaer som kan vælges via knappen i bunden af appen:

| Tema | Baggrund | Tekst | Accent |
|------|----------|-------|--------|
| ☀️ **Lys (Light)** | `#f9fafb` | `#111827` | Grøn/Rød knapper |
| 🌙 **Mørk (Dark)** | `#0f0f14` | `#ffffff` | Grøn/Rød knapper |
| 🩵 **Blå (Blue)** | `#0c1929` | `#e0f2fe` | Grøn/Rød knapper |
| 🟢 **Natur (Nature)** | `#f0fdf4` | `#14532d` | Grøn/Rød knapper |
| 🧁 **Soft** | `#faf8f5` | `#374151` | Ocean/Sunset |
| 🍯 **Honning (Honey)** | Gradient `#F5C842→#996600` | `#3D2000` | Transparente bobler |

**Honning-temaet** har desuden en glas-effekt med halvtransparente bobler i baggrunden.

---

## 🤝 Bidrag

Feedback er velkommen! Tryk på griseikonet i appen for at sende ris eller ros.

---

*Lavet med ❤️ til familier der vil lære børn om penge*

**Licens:** MIT License
