import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="Børnebank", page_icon="🐷")

st.title("🐷 Børnebank")

# Sheet URL from user
sheet_url = st.text_input("Google Sheet URL", placeholder="https://docs.google.com/spreadsheets/d/...")

if sheet_url:
    try:
        # Convert to CSV export URL
        if "/edit" in sheet_url:
            sheet_id = sheet_url.split("/d/")[1].split("/")[0]
            csv_url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
        else:
            csv_url = sheet_url
        
        # Try to read children sheet
        children_df = pd.read_csv(csv_url)
        
        st.success("✅ Sheet fundet!")
        
        # Show children
        st.header("👶 Børn")
        
        for idx, row in children_df.iterrows():
            st.metric(row['Navn'], f"{row['Saldo']} kr")
        
        # Add new transaction
        st.header("➕ Ny transaktion")
        
        col1, col2 = st.columns(2)
        with col1:
            child_name = st.selectbox("Vælg barn", children_df['Navn'].tolist())
        with col2:
            amount = st.number_input("Beløb", min_value=-1000, max_value=1000, step=10)
        
        trans_type = st.selectbox("Type", ["Lommepenge", "Bonus", "Fratræk", "Andet"])
        
        if st.button("Tilføj transaktion"):
            st.info("💡 For at tilføje transaktioner, rediger Google Sheet direkte!")
            st.info("Denne prototype viser data - redigering kræver Google Sheets API setup")
            
    except Exception as e:
        st.error(f"Fejl: {e}")
        st.info("💡 Tip: Gå til Google Sheet → Fil → Del → Publikér til internettet → CSV")
else:
    st.info("👆 Indtast din Google Sheet URL for at starte!")
    
    st.markdown("---")
    st.markdown("### Sådan opretter du en Google Sheet:")
    st.markdown("""
    1. Opret nyt regneark i Google Sheets
    2. Omdøb første ark til "Børn" med kolonner: Navn, Saldo
    3. Opret andet ark til "Transaktioner" med: Dato, Barn, Type, Beløb
    4. Gå til **Fil → Del → Publikér til internettet**
    5. Vælg **Hele dokumentet** og **Comma-separated values (.csv)**
    6. Kopier linket og indsæt her!
    """)
