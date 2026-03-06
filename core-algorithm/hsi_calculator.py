def calcola_hsi(empatia_attiva, responsabilita_sovrana, distrazione_tossica):
    """
    Calcola l'Humansafe Index (HSI) di un individuo o di un team aziendale.
    I valori di input devono essere compresi tra 0 e 10.
    """
    # Controlli di sicurezza sui dati in ingresso
    for val in [empatia_attiva, responsabilita_sovrana, distrazione_tossica]:
        if val < 0 or val > 10:
            raise ValueError("I valori devono essere compresi tra 0 e 10.")

    # Moltiplicatore base
    beta = 5 
    
    # Formula algoritmica HSI
    # Aggiungiamo +1 al denominatore per evitare DivisionByZero
    hsi_grezzo = ((empatia_attiva + responsabilita_sovrana) / (distrazione_tossica + 1)) * beta * 10
    
    # Normalizziamo il risultato a un massimo di 100 (Cap)
    hsi_finale = min(100, round(hsi_grezzo))
    
    return hsi_finale

def genera_referto(hsi):
    if hsi <= 35:
        return "ZONA ROSSA: Rischio Burnout. Intossicazione digitale elevata."
    elif hsi <= 65:
        return "ZONA GRIGIA: Dispersione cognitiva. Necessario intervento di disintossicazione."
    else:
        return "ZONA VERDE: Nucleo Sovrano. Idoneo alla Certificazione Humansafe."

# --- TEST DEL SISTEMA ---
if __name__ == "__main__":
    print("=== HUMANSAFE INDEX CALCULATOR ===")
    
    # Esempio di un dipendente alienato (Bassa empatia, alta distrazione)
    dipendente_a = calcola_hsi(empatia_attiva=2, responsabilita_sovrana=3, distrazione_tossica=9)
    print(f"Test Dipendente A (Isolato): HSI = {dipendente_a}/100 -> {genera_referto(dipendente_a)}")
    
    # Esempio di un dipendente consapevole (Alta empatia, bassa distrazione)
    dipendente_b = calcola_hsi(empatia_attiva=9, responsabilita_sovrana=8, distrazione_tossica=2)
    print(f"Test Dipendente B (Sovrano): HSI = {dipendente_b}/100 -> {genera_referto(dipendente_b)}")
