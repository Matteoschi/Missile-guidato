import pandas as pd
import os
import sys

# Configurazione

PERCORSO_CSV = r"C:\Users\Utente\Documents\coding\Fisica-v3-main\missile guidato\missile guidato\scatola_nera.csv"  # Modifica se il file è altrove
SOGLIA_IMPATTO = 10.0  

def analizza_volo():
    # 1. Trova il file
    file_path = PERCORSO_CSV
    if not os.path.exists(file_path):
        # Prova a cercarlo nella cartella corrente se non lo trova nella sottocartella
        file_path = "scatola_nera.csv"
        if not os.path.exists(file_path):
            print(f"\n[ERRORE] File '{PERCORSO_CSV}' o 'scatola_nera.csv' non trovato.")
            input("Premi INVIO per uscire...")
            return

    print(f"[INFO] Analisi del file: {file_path}...")

    try:
        # Legge il CSV gestendo il formato "Excel Italiano" (separatore ; e decimali ,)
        df = pd.read_csv(file_path, sep=';', decimal=',', encoding='latin1')
    except Exception as e:
        print(f"\n[ERRORE] Impossibile leggere il CSV: {e}")
        return

    # 2. Calcola Statistiche
    try:
        min_distanza = df['Distanza'].min()
        idx_min_dist = df['Distanza'].idxmin()
        tempo_impatto = df['Tempo'].iloc[idx_min_dist]
        
        tempo_totale = df['Tempo'].iloc[-1]
        quota_finale = df['Missile_Z'].iloc[-1]
        
        max_speed = df['Vel_Totale'].max()
        max_mach = df['Mach'].max()
        max_temperature = df['Temp_Ristagno_K'].max()
        max_thrust = df['Spinta_Motore_N'].max()
        thrust=df['Spinta_Base_N'].max()
        max_g = (df['guide_force m/s^2'].max()) / 9.81
        max_cl = df['Cl_Attuale'].max()
        fuel_rimanente = df['Fuel_kg'].iloc[-1]
        max_temperature_skin = df['Temp_Skin_K'].max()
        
        # Analisi Stati di Sicurezza
        if 'stato sicurezza' in df.columns:
            # Conta quante volte appare ogni stato
            counts = df['stato sicurezza'].value_counts()
            totale_step = len(df)
        else:
            counts = None

    except KeyError as e:
        print(f"\n[ERRORE] Colonna mancante nel CSV: {e}")
        print("Assicurati che il CSV sia stato generato dall'ultima versione del simulatore.")
        return

    # 3. Determina Esito
    esito = "MANCATO (Overshoot/Esaurimento)"
    colore = "\033[91m" # Rosso
    
    if min_distanza < SOGLIA_IMPATTO:
        esito = f"SUCCESSO (Target Colpito a {tempo_impatto:.2f}s)"
        colore = "\033[92m" # Verde
    elif quota_finale <= 0.1:
        esito = "FALLIMENTO (Schianto al suolo)"
        colore = "\033[91m"

    reset_colore = "\033[0m"

    # 4. Stampa Report
    print("\n" + "="*50)
    print(f"          REPORT RAPIDO VOLO")
    print("="*50)
    print(f"ESITO:             {colore}{esito}{reset_colore}")
    print(f"Tempo Totale:      {tempo_totale:.2f} s")
    print("-" * 50)
    print(f"Prestazioni Picco:")
    print(f" - Min Distanza:   {min_distanza:.2f} m")
    print(f" - Max Velocità:   Mach {max_mach:.2f} = {max_speed:.2f} m/s")
    print(f" - Max Temp Rist.: {max_temperature:.2f} K = {max_temperature - 273.15:.2f} °C")
    print(f" - Max Temp Skin:  {max_temperature_skin:.2f} K = {max_temperature_skin - 273.15:.2f} °C")
    print(f" - Max Spinta:     {max_thrust:.2f} N , Bonus spinta Max= {max_thrust - thrust:.2f} N")
    print(f" - Max G-Load:     {max_g:.2f} G")
    print(f" - Max Lift (Cl):  {max_cl:.4f}")
    
    print(f" - Fuel Rimasto:   {fuel_rimanente:.2f} kg")
    print("-" * 50)
    
    if counts is not None:
        print("DIAGNOSTICA SICUREZZA (Cause problemi):")
        for stato, count in counts.items():
            perc = (count / totale_step) * 100
            nome_stato = str(stato).strip()
            
            # Colora gli errori gravi in rosso
            warn = ""
            if "LOST" in nome_stato or "STALL" in nome_stato or "DANGER" in nome_stato:
                warn = " <!>"
            
            print(f" - {nome_stato:<20}: {count:4d} passi ({perc:5.1f}%){warn}")
    else:
        print("Nessun dato diagnostico trovato.")
        
    print("="*50)
    input("\nPremi INVIO per chiudere...")

if __name__ == "__main__":
    analizza_volo()