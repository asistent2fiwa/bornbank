# 🐷 Børnebank

Et digitalt lommepenge-system til familier. Hjælp børn med at lære om økonomi og ejerskab.

## 🌟 Funktioner

### For forældre
- **Opret familie** - Start din egen familie-bane
- **Tilføj børn** - Tilføj børn med navn, fødselsdag og lommepenge
- **Transaktioner** - Tilføj indtægter og udgifter
- **Automatisk lommepenge** - Tilskrives hver fredag kl. 15
- **Rente** - Valgfri rente på opsparing (måned/kvartal/år)
- **Deling** - Del adgang med anden forælder via QR-kode eller link

### For børn
- **Saldo** - Altid opdateret saldo
- **Transaktioner** - Se seneste bevægelser
- **Read-only** - Kan ikke ændre data (sikker)

## 📱 Installation

### PWA (Anbefalet)
1. Åbn https://asistent2fiwa.github.io/bornbank/ i din browser
2. **iOS:** Tryk på Del → "Tilføj til hjemmeskærm"
3. **Android:** Tryk på menu → "Installer app"

### Browser
 Fungerer i alle moderne browsere:
- Chrome
- Safari  
- Firefox
- Edge

## 🔒 Sikkerhed

- **Kun fornavne** - Ingen persondata gemmes
- **URL-tokens** - Deling sker via unikke koder (ikke passwords)
- **LocalStorage** - Data gemmes lokalt på enheden
- **Supabase** - Cloud-synkronisering mellem forældre (valgfrit)

## 🛠️ Teknologi

- **Frontend:** HTML, CSS (Tailwind), JavaScript
- **Database:** Supabase (PostgreSQL)
- **Hosting:** GitHub Pages

## 📊 Datastruktur

```
Family
├── id (unik kode)
├── parent_token (delings-kode)
└── data
    ├── children[]
    │   ├── id
    │   ├── name
    │   ├── birth
    │   ├── age
    │   ├── piece (monopoly-brik)
    │   ├── allowance (lommepenge/uge)
    │   ├── saldo
    │   └── transactions[]
    │       ├── date
    │       ├── amount
    │       └── desc
    └── interest
        ├── enabled
        ├── rate
        ├── freq (1=måned, 3=kvartal, 12=år)
        └── lastInterest
```

## 🤝 Bidrag

Feedback er velkommen! Tryk på griseikonet i appen for at sende ris eller ros.

## 📝 License

MIT License

---

*Lavet med ❤️ til familier der vil lære børn om penge*
