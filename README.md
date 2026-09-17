# Simulatore 3-DOF di Dinamica del Volo Supersonico

Ambiente di simulazione a **3 Gradi di Libertà (3-DOF)** per lo studio semi-empirico non lineare della traiettoria di un intercettore a corto raggio, con modellazione fisica realistica di aerodinamica comprimibile, propulsione a massa variabile e legge di guida.

> 📄 Questo README è una sintesi generale. La repository contiene documenti dedicati con il dettaglio matematico e implementativo completo — vedi la sezione [Documentazione](#documentazione) qui sotto.

## Panoramica

Il simulatore rappresenta il vettore non come un punto materiale a massa costante, ma come un sistema dinamico soggetto a vincoli termodinamici, aerodinamici e propulsivi variabili nel tempo. Il modello integra tre domini fisici:

- **Aerodinamica comprimibile**: atmosfera standard ISA, effetti di compressibilità in regime transonico/supersonico, degradazione della portanza (stallo) e resistenza indotta.
- **Propulsione a massa variabile**: equazione del razzo estesa, con variazione dell'impulso specifico in funzione della contropressione atmosferica locale.
- **Guida e controllo**: legge di Navigazione Proporzionale (Pro-Nav), soggetta a saturazione strutturale (G-Limiter).

L'obiettivo è calcolare, istante per istante, il bilancio vettoriale delle forze (Spinta, Gravità, Portanza, Resistenza) per determinare l'inviluppo di volo operativo.

## Modelli fisici principali

- **Cinematica di ingaggio**: vettore linea di vista (LOS), range, versore di puntamento.
- **Massa dinamica**: consumo di propellente modulato dal fattore di parzializzazione della spinta (throttle), integrazione numerica della massa istantanea, fase balistica dopo il burn-out.
- **Navigazione Proporzionale**: velocità di chiusura (Vc), rateo di rotazione della LOS, comando di accelerazione laterale con costante di navigazione N.
- **Atmosfera ISA**: profilo di densità esponenziale, gradiente termico verticale, celerità del suono e numero di Mach, pressione dinamica.
- **Riscaldamento aerodinamico**: temperatura di ristagno e limitatore proattivo della spinta (soft limiter) per il controllo termico.
- **Propulsione**: spinta endoreattore con termine di pressione dipendente dalla quota (bonus di spinta nel vuoto).
- **Compressibilità e drag**: divergenza del coefficiente di resistenza in regime transonico/supersonico, resistenza parassita e d'onda.
- **Flight envelope protection**: limiti aerodinamici (CLmax dipendente da Mach) e strutturali (fattore di carico G), saturazione vettoriale del comando di accelerazione, mappatura dei codici di stato/diagnostica di volo.
- **Bilancio energetico**: resistenza indotta legata al coefficiente di portanza, coefficiente di resistenza totale (polare parabolica).
- **Dinamica del corpo rigido**: scomposizione ed equazione vettoriale del moto (spinta, drag, gravità, portanza/guida).
- **Integrazione numerica**: risoluzione delle equazioni del moto con metodo Runge-Kutta del 4° ordine (RK4).

## Documentazione

La repository include documenti di approfondimento separati da questo README:

| File | Contenuto |
|---|---|
| `Spiegazione.pdf` | Trattazione teorica completa: derivazione matematica di tutti i modelli fisici (cinematica, propulsione, atmosfera, drag, flight envelope, integrazione RK4) con formule ed equazioni |
| *(altri file del codice sorgente)* | Implementazione C/Python dei modelli descritti |

Per i dettagli matematici puntuali (formule, costanti, soglie, mappatura dei codici di stato) fare riferimento al documento tecnico piuttosto che al solo codice sorgente.

## Stato del progetto

- Modello fisico-matematico documentato nella sua interezza (versione documento: 27 gennaio 2026).
- Copre l'intera catena: cinematica → atmosfera → propulsione → aerodinamica → guida → integrazione numerica.

---

*Per domande su una sezione specifica del modello, consultare prima il documento tecnico corrispondente elencato sopra.*