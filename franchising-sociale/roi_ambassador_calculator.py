def calcola_distribuzione_fondi(prezzo_pianta, quantita_vendute, costo_ingrosso_singolo):
    """
    Calcola in totale trasparenza la distribuzione dei fondi 
    generati dalla campagna territoriale "Radici Umane".
    """
    # 1. Calcolo del ricavo totale e dei costi vivi
    ricavo_totale = prezzo_pianta * quantita_vendute
    costi_totali = costo_ingrosso_singolo * quantita_vendute
    margine_netto = ricavo_totale - costi_totali

    # 2. Modello Peace Business (Distribuzione Etica 50/50)
    # Il 50% va all'Ambasciatore per il suo lavoro e la sua dignità
    compenso_ambasciatore = margine_netto * 0.50
    # Il 50% va all'ecosistema Humansafe (APS) per aprire i centri e gestire la tech
    fondo_humansafe = margine_netto * 0.50

    return {
        "Ricavo Totale": ricavo_totale,
        "Costi Vivi (Piante/Vasi)": costi_totali,
        "Margine Netto Generato": margine_netto,
        "Compenso Ambasciatore": compenso_ambasciatore,
        "Fondo Ecosistema Humansafe": fondo_humansafe
    }

# --- SIMULAZIONE DELLA GIORNATA DI UN AMBASCIATORE ---
if __name__ == "__main__":
    print("=== SIMULATORE PEACE BUSINESS: RADICI UMANE ===")
    
    # Esempio: L'ambasciatore distribuisce 20 piante a 15€ l'una. Costo all'ingrosso 4€.
    risultato = calcola_distribuzione_fondi(prezzo_pianta=15, quantita_vendute=20, costo_ingrosso_singolo=4)
    
    print(f"Piante distribuite: 20")
    print(f"Ricavo Totale: € {risultato['Ricavo Totale']:.2f}")
    print(f"Costi Vivi (Materiale): € {risultato['Costi Vivi (Piante/Vasi)']:.2f}")
    print("-" * 40)
    print(f"MARGINE NETTO: € {risultato['Margine Netto Generato']:.2f}")
    print("-" * 40)
    print(f"💰 Compenso Ambasciatore (Dignità): € {risultato['Compenso Ambasciatore']:.2f}")
    print(f"🏛️ Fondo Humansafe APS (Strutture): € {risultato['Fondo Ecosistema Humansafe']:.2f}")
    print("\n[SISTEMA]: Modello economico sostenibile. Il Peace Business è attivo.")
