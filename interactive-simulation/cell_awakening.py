import time
import sys

def slow_print(text, delay=0.03):
    """Stampa il testo lentamente per simulare un terminale."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def main():
    score = 0
    slow_print("=========================================")
    slow_print(" INIZIALIZZAZIONE SISTEMA HUMANSAFE...   ")
    slow_print("=========================================")
    time.sleep(1)
    slow_print("\n[SISTEMA]: Analisi del nodo neurale in corso...")
    slow_print("[SISTEMA]: Sei una Cellula all'interno dell'Organismo sociale.")
    slow_print("[SISTEMA]: Iniziamo l'estrazione dei dati cognitivi.\n")
    time.sleep(1)

    # SCENARIO 1
    slow_print(">> SCENARIO 1: L'INFIAMMAZIONE")
    slow_print("Il tuo schermo si illumina. Una notifica ti avvisa che un influencer ha attaccato duramente i tuoi valori.")
    slow_print("L'algoritmo attende la tua rabbia per monetizzarla. Cosa fai?")
    print("  [1] Rispondo subito per difendere le mie idee (Reazione).")
    print("  [2] Leggo, mi infastidisco, ma chiudo l'app (Difesa Passiva).")
    print("  [3] Riconosco l'esca. Spengo lo schermo. Il mio spazio mentale è sacro (Sovranità).")
    
    scelta1 = input("Inserisci 1, 2 o 3: ")
    if scelta1 == '1': score += 0
    elif scelta1 == '2': score += 5
    elif scelta1 == '3': score += 10

    print("\n")

    # SCENARIO 2
    slow_print(">> SCENARIO 2: IL VUOTO")
    slow_print("Sei in una stanza d'attesa. Il telefono è completamente scarico. Nessuna via di fuga digitale.")
    print("  [1] Vado in ansia. Mi sento perso senza stimoli.")
    print("  [2] Mi annoio, cerco vecchie riviste per distrarmi dal silenzio.")
    print("  [3] Accolgo il vuoto. Lo uso per respirare e ascoltare i miei pensieri.")
    
    scelta2 = input("Inserisci 1, 2 o 3: ")
    if scelta2 == '1': score += 0
    elif scelta2 == '2': score += 5
    elif scelta2 == '3': score += 10

    print("\n")
    slow_print("[SISTEMA]: Calcolo dell'HUMANSAFE INDEX in corso...")
    time.sleep(2)
    slow_print("=========================================")
    slow_print(" REFERTO DIAGNOSTICO                     ")
    slow_print("=========================================")

    if score <= 5:
        slow_print("ARCHETIPO: La Cellula Dormiente (Nodo Isolato)")
        slow_print("DIAGNOSI: Usi lo schermo come anestetico. Sei in balia dell'algoritmo.")
        slow_print("AZIONE: Inizia la 'Regola del Vuoto'. 15 min di silenzio al giorno.")
    elif score <= 15:
        slow_print("ARCHETIPO: La Cellula Reattiva (Nodo Infiammato)")
        slow_print("DIAGNOSI: Consumi informazioni tossiche. Stai infiammando l'Organismo.")
        slow_print("AZIONE: Inizia il 'Digiuno dell'Opinione'. Attendi 24h prima di commentare.")
    else:
        slow_print("ARCHETIPO: Il Nucleo Sovrano (Architetto Consapevole)")
        slow_print("DIAGNOSI: Il sistema non ha potere su di te. Usi la tecnologia, non ne sei usato.")
        slow_print("AZIONE: Diventa un Ambasciatore Humansafe. Guida le altre cellule.")
    
    print("\nVisita il nostro repository per scaricare il Framework completo.")

if __name__ == "__main__":
    main()
