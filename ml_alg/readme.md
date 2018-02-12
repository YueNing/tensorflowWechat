# ML 1

## 1. Einführung
### 1.1 Allgemeine Information
### 1.2 Einführung und Überblick
- Charakterisierte Intelligenz: Testen von Intelligenz Turing Test und Gegenbeispiel(Chinese room) eindeutige Definition nicht möglich
- Loebner Preis
	- x Tester glauben lassen, sie hätten sich tatsächlich mit einem Menschen unterhalten
	- Chatbots: **Jabberwock**
	- 2010/11 Suzette/Rosette von Bruce Wilcox
	- 2013 Mitsuku
- Lernen
- Maschinelles Lernen
	- Forschungsrichtungen des ML
		1. Praxisorientiert: Aufgabenorientierte, problemlösende Systeme, Wissenserwerb und Lösungshypothese finden
		2. Entscheidungstheoretische Ansätze: Diskriminierungsfuntionen aus einer Menge von Trainingsbeispielen ??????????
		3. Theorieorientiert: 
			- Problemcharakteristik -> Methoden
			- Lernbarkeit analysieren
			- Komplexitätsabschätzungen
		4. Koginitionsorientiert: Konstruktion kognitiver Modelle oft angelehnt an menschliche oder tierische Lerneprozesses
		5. Evolutionäres lernen: Ursprung -> Neurophysiologische, biologische und psychologische Forschung -> Systeme die sich nach Umgebung anpassen
	- Historie
		1. Beginn und früher Enthusiasmus(1955-1968)
		2. Depression(1969-1976)
		3. Renaissance(1976 bis 1986)
		4. Maturität - Reife(1986 bis ...)
			- Lerntheorie, Erweiterungen der Basisalgorithmen
				- Neuronale Netze & SVM
				- Reinforcement Learning
				- Genetische Algorithmen
				- Deep Learning
			- Problemlösearchitekturen
				- Kombination induktiver und deduktiver Verfahren
				- Kombination symbolischer und subsymbolischer Verfahren
				- Überwachtes, Unüverwachtes, aktives Lernen
		5. ML als aktuelles Forschungsgebiet(...heute)
			- Personenerkennung, -identifikation
			- Gesten- und Aktivitätserkennung
			- Blickrichtungserkennung
			- Kognitive Automobile und Fahrerassistenz
			- Objekterkennung Klassifikation
			- Umgebungserkennung
			- Situatives Entscheiden
			- Skill Lernen
- Komponenten eines lernenden Systems
![liuchengtu]()
### 1.3 Literaturhinweise

## 2. Induktives Lernen
### 2.1 Induktion & Deduktion
- **Induktion**: Prozess des plausiblen Schließens vom Speziellen zum Allgemeinen
	- Basis: große Anzahl zutreffender Fälle
		![gailvgongshi]()
- **Deduktion**: Modus Ponens 
	![]()
- Vergleich:
<table>
<tr><td>Induktion</td><td>Deduktion</td></tr>
<tr><td>Wahrheitserewiternd</td><td>Wahrheitserhaltend</td></tr>
<tr><td>Macht Lebenwesen</td><td>Logischer Schluss</td></tr>
<tr><td>Überlebensfähig</td><td>Korrektheit</td></tr>
<tr><td>Plausibilität</td><td>Korrektheit</td></tr>
</table>
- Induktive Lernhypothese:
Jede Hypothse, die die Zielfuntion über einer genügend großen Menge von Trainingsbeispielen gut genug approximiert, wird die Zielfuntion auch über unbekannten Beispielen gut approximieren.	     
### 2.2 Konzeptlernen als Suche im Hypothesenraum
<p> Konzept beschribt Untermenge von Objekten oder Ereignissen definiert auf größerer menge, und Bool'sche Funktion definiert über größerer Menge </p>

1. Gegeben: Beispiele, die als Mitglieder oder Nichtmitglieder eines konzepts gekennzeichnet sind
2. Gesucht: Automatischer Schluss auf die Definition des zugrundeliegenden Konzepts
3. Definition Konzeptlernen: Schließen auf eine Boolean-wertige Funktion aus Trainingsbeispielen ihres Inputs und Outputs
4. Beispiel: Das Wetter

**Konsistenz**: Keine negativen Beispiel werden positiv klassifiziert
**Vollständigkeit**: Alle positiven Beispiele werden als postiv klassifiziert.
- vollständig aber nicht konsistenz: alle positiven Beispiele als postiv klassifiziert, aber es gibt negative Beispiele als positive klassifiziert werden
- konsistenz, aber nicht vollständig: keine negativen Beispiele als postiv klassifiziert, aber nicht alle positiven Beispiele als postive klassifiziert werden, das bedeutet, es einige positiven Beispiele gibt, die als negativ klassifiziert werden.
- konsistent und vollständig: keien negativen Beispiele als positiv klassifiziert und alle positiven Beispiele als positiv klassifiziert werden.
![shuomingtu]()
#### 2.2.1 Suche vom Allgemeinen zum Speziellen
1. Ausgangspunkt ist allgemeinste Hypothese <?, ...., ?>
2. Negative Beispiele: Spezialisierung
3. Positive Beispiele: werden nicht betrachtet
#### 2.2.2 Suche vom Speziellen zum Allgemeinen
1. Ausgangspunkt ist speziellste Hypothese<#, ..., #>
2. Positive Beispiele: (minimale) Verallgemeinerung
3. Negative Beispiele: werden nicht betrachtet 

Preseude Code
> Initialisiere h mit der spezifischsten Hypothese in H <#, ...., #>
> Für jedes positive Trainingsbeispiel x
>> Für jede Attributeinschränkung a0 in h
>>> wenn ai von x erfüllt wird
>>>> Dann tue nichts

>>> Sonst:
>>>> Ersetze ai durch die nächstallgemeinere Einschränkung, die durch x erfüllt wird

> Gib die Hypothes aus

4. Beurteilung 1
	- Wichtiges Prinzip im Konzeptlernen
	- Für Hypothesenräume, die durch Konjunktion von Attributeinschränkungen beschrieben sind garantiert das Verfahren die spezifischste Hypothese, die mit den positiven Trainingsbeispielen vereinba ist
	- Endhypothese ist auch mit negativen Trainingsbeispielen konsistent Solange die Trainingsbeispiele korrekt sind und die Zielhypothese in H enthalten ist.
 
#### 2.2.3 Paralleles Anwenden beider methoden => Version Space
Der Versionsraum VSH,D bezüglich des Hypothesenraums H und der Menge von Trainingsbeispielen D ist die Untermenge der Hypothesen von H, die mit den Trainingsbeispielen in D konistent ist.
##### 2.2.3.1 Versionraum(Version Space) / Gandidate-Elimination-Algorithmen
- Lernen ist inkrementell
- Gespeichert werden: S und G
- S- Und A- Hypothesen
	- negatives Beispiel
		1. Lösche aus S
		2. Spezialisiere G, und sie allgeminer als eine Hypothese in S bleiben
		3. Lösche aus G alle hypothesen, die spezifischer als eine andere Hypothese aus G sind
	- positves Beispiel
		1. Lösche aus G, die mit p inkonsistenten Hypothesen
		2. Verallgemeinere S, sie spezifischer als eine Hypothese in G
		3. Lösche aus S alle Hypothesen, die allgemeiner als eine andere Hypothese aus S sind
- Beurteilung
	- S=G
		- Voraussetzung: Beispiele konsistent, korrekte Hypothese in Hypothesenraum enthalten
		- Probleme: feherbehaftet Trainingsdaten(Rausch)!, Zielkonzept nicht von Hypothesenrepräsentation abgedeckt **????????????**, mögliche Erweiterung:disjunktive Begriffe
### 2.3 Notwendigkeit von Vorzugskriterien(Bias)
Induktives Lernen erfordert Vorannahmen(inductive bias)
Je strenger die Vorannahmen, also mehr unbekannte Beispiele können klassifiziert werden!!!!!!!!
- Mögliche Vorzugskriterien
	- Verständlichkeit
	- Klassifikationsgenauigkeit
	- Messaufwand für die verwendeten Deskriptoren
	- Berechnungs- und Speicheraufwand für die Hypothese
- Hypothesenraumbias
	- h gehöre zu einem beschränkten Raum von hypothesen
		- logische Konjunktionen
		- lineare Schwellwertfunktionen
		- Geraden, Polynome, ...etc
		- 3 NN (Nearest Neighbour)
- Präferenzbias
- Problem
	- keine Funtion h, die konsistent mit allen Trainingsbeispielen ist, y.B wegen verauschter Trainingsdaten.
	- Unterschiedlische Ansätze möglich unterschiedliche Lösungen
	- Anpassen des Hypothesenraumbias: Overfitting!
	- Anpassen des Präferenzbias: Misklassifikation muss in Kauf genommen werden

## 3. Unüberwachtes Lerenen
### 3.1 Motivation & Einführung
1. Sammeln und Klassifizieren von Trainingsdaten kann sehr aufwändig sein wie Spracherkennung
2. Engineering z.B: Merkmalsberechnung der Daten kann sehr aufwendig sein
3. Data Mining
4. Sich verändernde Charakteristika von Mustern
5. Finden von neuen Eigenschaften
6. Erste Erkenntnisse üver Struktur von Daten
<p>Grundidee</p>
- Ausnutzen von Ähnlichkeiten in Trainingsdaten, um 
	- die Klassen / Ballungen zu ershließen
	- oder um die wesentlichen Charakteristika = Merkmale
- Analogie zum menschlichen Lernen:
	- Schüler lernt graduell
### 3.2 K-means Clustering
1. Sehr elementar aber populär
2. Klassifiziert eine Datenmenge in eine a-priori vorgegeben Anzahl von Ballungen
3. Grundidee:
	- Definieren eines Mittelpunkts für jeden Cluster
	- Iterative Anpassung / Verbesserung
	- Optimalitätskriterium: Minimierung der Abstände aller Datenpunkte von ihrem Ballungsmittelpunkt
<p>k-means-Clustering Formal</p>
1. Gegeben:
	- Menge X von unklassifizierten Trainingsbeispielen mit jeweils d Attributen:
	- Anzahl der gesuchen Ballungen k
2. Gesucht:
	- Einteilung der Trainingsmenge in Ballungen mit Zentren c unter Minimierung von k 

3. Algorithmenbeschreibungen:
	- Plaziere K Punkte c im d-dimensionalen Raum als initiale mittelpunkte der Ballungen
	- Bis sich die c nicht mehr ändern:
4. K-means-Clustering Bewerutng
	- Resultate hängen stark von der initialen Belegung de c ab
		- Evtl. werden suboptimale Lösungen gefunden 
	- Resulate hängen von der verwendeten Metrik |x - c| ab
		- in hochdimensionalen Repräsentationen sind allle Daten unähnlich -> schwer Cluster zu finden
	- Resultate hängen von der korrekten Wahl von k ab 
		- Keine fundierten theoretischen Lösugnen
		- Ergibt sich k aus der Domäne
		- Overfitting!!!!
5. Fuzzy k means Clustering mit
	- normale K-means: jeder Datenpunkt in genau einem Cluster
	- Abschwächung: jeder Datenpunkt x hat eine abgestufte / "unscharfe" Zugehörigkeit zu jedem Cluster X
		- p(X | x): Wahrscheinlichkeitsmaß für die Zugehörigkeit
		- p(X | x) ~ 0: Datenpunkt weit von Cluster entfernt
		- p ist normiert über die Ballungen X
		- Neuberechung der X  durch Adaption von c unter Beachtung der unscharfen Zugehörigkeit aller Datenpunkte und von p für jedes x
	- Problem: Laufzeit = O(kn) je Iteration
**Induktiv**
### 3.3 Hierarchisches Clustering
1. K-means: "flache" Datenbeschreibung
2. Ballungen können Sub-ballungen und Sub-sub-ballungen haben
3. Idee:
	- Iteratives Vereinen von (Sub-) Clustern zu größeren Clustern
4. AHC Distanz: Nearest Neighbor
**Induktiv**
### 3.4 Begriffliche Ballungen & COBWEB
Bei klassischen Ballungsverfahren:
	- Definiton der Änhlichkeit auf der Basis einer meist numerischen Änhlichkeitsfunktion
<p>COBWEB Lernen durch inkrementelles Aufbauen und Anpassen eines Strukturbaums</p>
1. Jede Verzweigung innerhalb des Baumes steht für eine Einteilung der Unterbäume in verschiedene Kategorien
2. Blätter sind die speziellsten Begriffe(Kategorien)
3. Es werden nominale Attributwerte gestattet

<p>Der COBWEB-Algorithmus</p>
1. Eingabe: 
	- Aktueller Knoten N in der Konzepthierarchie
	- Ein Unklassfifiziertes Attribute-Werte-paar
2. Ausgabe:
	- Konzepthierarchie, die die Instaz I klassifiziert 
3. Top-level call: COBWEB(TOP-node)
4. Variablen:
	- C, P, Q, R: Knoten in der Hierarchie
	- W, X, Y, Z: Category-Utility Werte


### 3.5 Ausblick

## 4. Lerntheorie, Algorithmenunabhängige Verfahren
### 4.1 PAC
### 4.2 Modell
### 4.3 Lernmaschine
### 4.4 VC-Dimension

## 5. Entscheidungsbäume
### 5.1 Motivation
1. Instanzen lassen sich als Attribut-Wert Paare beschreiben
2. Zielfunktion besitzt diskrete Ausgabewerte
3. Disjunkte Hypothesen erforderlich
4. Beispieldaten sind möglichweise verrauscht
5. Beispieldaten enthalten evtl. fehlende Attributwerte
### 5.2 ID3 
1. Top Down Aufbau von EB
	- A <- Das beste Enscheidungsattribut für den nächsten Knoten: 
		- Cross Entropy
		- Informationsgewinn Gewinn(S, A) = Entropie(S) - all Sv / S entropy(Sv)
	- Weise A als Entscheidungsattribut für den nächsten Knoten zu 
	- Füge für jeden möglichen Wert von A einen Nachfolgeknoten ein
### 5.3 Overfitting
1. Basisverfahren:
	- Jeder Zweig wächst solange, bis die Trainingsbeispiele perfekt klassifiziert werden
	- Dies basiert auf dem statistisch approximierten Inforamtionsgewinn
> Dies kann zu Problemen führen, wenn
	- die Daten verrauscht sind
	- die Beispiel nicht repräsentativ sind  potentiell mehr Fehler
2. Vermeidung von Overfitting
	- Frühzeitiges Stoppen des Baumwachstums
	- Nachträgliches "Prunen" des Baumes(in der Proxis erfolgreicher) ?????????????
### 5.4 Erweiterungen
### 5.5 C4.5
### 5.6 ID5R
### 5.7 Random-Forests
### 5.8 Zusammenfassung

## SVM Stützvektor Methoden, Support Vector Mehtod, Kernel Methoden
### Lineare Support Vektor Methode
### Architektur
### Optimierungen
### Erweiterungen

## Neuronale Netze
### Der Menschen(Vorkenntnis)
### Frühe Realisierung: Perzeption
### Multi layer Feedforward Neural Network
#### Motivation
#### Aufbau des MLNN
#### Aufbau des RBF Netzes
#### Probleme / Optimierung

## Reinforcement learning
### Problemstellung MDP
### Lernziel: maximale Bewertung
#### Q 
### Problemstellung in RL
### Strategielernen (Policy Learning)
### Anwendungsbeispiel

## Hidden Markov Modell
### Motivation
### Diskreter Markov Prozess
### Hidden Markov Modelle
### Die 3 grundlegenden Probleme
### Lösungen der Probleme
### Anwendungsbeispiele

## Lernen nach Bayes
### Motivation
### Theorem von Bayes
### MAP-/ML-Hypothesen
### Optimaler Bayes-Klassifikator
### Naiver Bayes-Klassifikator
### Beispiel:Klassifikatin von Texten
### Bayes'sche Netze
### Der EM-Algorithmus
### Zusammenfassung

## Instanzbasiertes Lernen
### Einführung in das Instanzen-basierte Lernen
Lazy learning vs. Eager learnign (faules Lernen  -- fleißiges Lernen)
1. Instanzen-basiertes Lernen: "Delayed / Lazy Learning"
2. Lernen = (einfaches) Abspeichern der Trainingsbeispiele
3. Weniger Rechenzeit während des Trainings, dafür mehr bei Anfragen zur Klassifikation
4. Unterschiedliche Hypothesen / Lokale Approximation der Zielfuntion für jede Anfrage
5. "Fleißig" Lernalgorithmen mit dem gleichen Hypothesenraum sind eingeschränkter
6. Bildet für jede neue Anfrage eine andere Annährung an die Zielfunktion
	- Lokale Approximation der Targetfuntion
	- Komplexere symbolische Repräsentationen für Instanzen
7. Generalisierungsentscheidung wird bis zu einer konkrete Suchanfrage aufgeschoben
8. Neue Instanzen werden analog zu ähnlichen Instanzen klassifiziert
9. Instanzenbasiertes Lernen: Beurteilung:
	- Komplexe Targetfunktionen können modelliert werden
	- Inforamtion aus den Trainingsbeispielen geht nicht verloren
	- Evtl. komplexe Berechnungen bei Klassifizierung neuer Instanzen
	- Schwierigkeit: Welche Instanzen sind sich ähnlich?
> Problem irrelevanter Eigenschaften
### Der K-NN Algorithmus
1. Instanzen x = <> korrespondieren mit Punkten im n-dimensionalen Raum
2. Nachbarschaftsbeziehungen sind durch die Euklidische Distanz:
	d(x,z ) = sqrt
3. Lernen einer Funtion f: R n-di -> V aus einer Menge von Trainingsbeispielen <x, c(x)>
4. V endliche (diskrete) Menge
5. Trainingsalgorithmus:
	- für jedes Trainingsbeispiel<> mit c aus V:
		- Füge das Trainingsbeispielen zu der Liste training_examples hinzu
	- Klassifiaktionsalgorithmus: Anfrage xq
		- x1, ... xk seien die k Instanzen von training_examples, die am nächsten zu xq liegen
		- Ergebnis f(xq) <- arg max delta(v, c(xi))
6. 5-NN Klassifikation: xq negativ
7. 1-NN Klassifikation: xq positiv
8. Normalisierung der Eingabevektoren oft sinvoll
	- Verzerrung bei stark ungliechen Eingabedimensionen
9. Abstandsgewichteter K-NN Algorithmus
	- Nahe Nachbaren gehen genauso stark in die Klassifikation
### Case-Based Reasoning: Motivation und Vorstellung
**Analogien**
1. allgemeines abstraktes Framework
2. kein direkt anwendbarer Algorihmus
3. Wiederverwendung alter Fälle
4. Such nach Lösungen ähnlicher Probleme
### Der Case-Based Reasoning Zyklus
1. Aufgabe: Finde ähnliche Fälle
2. Ähnlichkeitsmaß
	- Euklidische Distanz
	- Syntaktische Ähnlichkeiten
	- Semantische Ähnlichkeiten
3. Organisation der Fallbasis
	- Lineare Liste
	- Baumstruktur
	- Graphen, Netze, Indexstrukturen
	- Datenbanken
4. Indizierung: Problem
	- Auswahl der Indizes
5. Wiederverwendung
	- Lösungsadaption
	- Eingesetzte Methoden
		- Benutzerinteraktion
		- Regelbasiertes Schließen
		- Modellbasiertes Schließen
		- Planer
6. Anpassen / Überarbeiten / Revise
	- Überprüfung, Verbesserung der Lösung
	- Evaluierung der Lösung
		- Überprüfung durch Simulation
		- Überprüfung in realer Welt
	- Verbessern bzw. Reparieren der Lösung
		- Fehler erkennen und erklären
		- Beseitigen unter Berücksichtigung der Fehlererklärungen
	- Potentiell iterativ!!!
7. Zurückbehalten
	- Bewahrung der gamachten Erfahrung
	- Was wird gelernt?
		- Neue Erfahrung 
		- Alten Fall generalisieren
		- Neue Merkmale (Indizes)
		- Organisation der Fallbasis (Effizienz)
	- Methoden
		- Auswendiglernen(Speichern neuer Fälle)
		- Induktive / Deduktive Lernverfahren
### Beispiel für den Einsatz von CBR
1. CLAVIER
	- Zusammenstellung von Teilepaletten für einen Vulkanisierungofen
	- Durchlauf: Suche nach "ähnlichster" bekannter Zusammenstellung
	- Adaption durch Ersetzen möglichst weniger Elemente
2. Kognitive Automobile
	- Ziel: Entwicklung autonomer Fahrzeuge
		- Wahrnehmung der Umwelt
		- Versthen aktueller Situationen
		- Auswahl und Ausführung von Verhalten
	- Szenen repräsentiert mittels Beschreiungslogik
	- KogniMobil: Fallbasis
		- Fall
		- Vererbungshierarchie zwischen Fällen (DAG)
		- Fälle enthalten Verweise auf zeitlich nachfolgende Fälle(abhängi von gewählten Verhalten)
### Bewertung von CBR
#### **Vorteil**
1. Konzeptuell einfach, aber trotzdem können komplexe Entscheidungsgranzen gebildet werden
2. Kann mit relativ wenig Information arbeiten
3. Analogie zu menschlichem Problemlösen
4. Lernen ist einfach (one shot learning)
5. Günstig für mit Regeln schlecht erfassbare Probleme
#### **Probleme**
1. Gedächtniskosten
2. Klassifikation kann lange dauern
3. Hängt start von Repräsentation ab
4. Problematisch bei komplexen Repräsentationen
5. Problematisch: Irrelevante Eigenschaften

## Evolutionäre Algorithmen
### Vorkenntnis
1. Biologisches Evolutionsmodell nach Darwin: Selektion = Treibende Kraft der Evolution
2. Man kann die natürliche Selektion genauso gut in Formeln packen, wie es mit natürlichen Neuronalen Netzen geht
3. Technische: Evolution als Optimierung komplexer, künstlicher Systeme
### Nomenklatur
1. Individuum : <= eine mögliche Lösung, Hypothese
2. Population und Generation <= Lösungs- bzw. Hypothesenmenge
3. Erzeugen von Nachkommen <= Generierung neuer Hypothesen
	- Rekombination und Mutation
4. Veränderter Nachfolger, Kind, Nachkommene <= neue Hypothese
5. Fitness(-funktion) <= Hypothesengüte, zu optimierendes Kriterium
6. Selektion des Besten <= Auswahl der Hypothesen, welche die beste Problemlösung erzeugen
### Der Grundalgorithmus
![Evoulutionäre Al]()
### Repräsentation von Nachkommen
1. Wissen wird meistens strukturiert repräsentiert
2. Kodieren durch Gene
	- k-Alphabet(k=2: Binärcodierung) -> Genetische Algorihmen
	- Reelle Zahlen, Vektoren -> Evolutionäre Strategien
	- baumartige Strukturen -> Genetisches Programmieren
#### Generierung von Nachkommmen 
1. Erfolgt durch s.g. genetische Operatoren
2. Zwei Strategien:
	- Exploration ---- Exploitation
	- Erforschen des Hypothesenraumes ---- Lokale Optimierung
3. Vergleich
	- Je stärker und zufälliger Änderungen sind, um so geringer ist die Wahrscheinlichkeit, bessere nachkomen zu erzeugen
	- Bei lokalen Verbesserungsmethoden ist die Gefahr der lokalen Minima gegeben
	- Explorationsgrad muss gemäß der aktuellen Fitness der Generation ausgewählt werden(z.B.: anfangs hoch dann fallend)	
### Mutation
1. Der Nachkomme stammt von einem Elternteil ab
2. Mutation einzelner Gene
3. Konzepte:
	- Alle Bits einer Sequenz werden unabhängig voneinander mit einer bestimmten Wahrscheinlichkeit invertiert
	- Für eine bestimmte(oder zufällige) Anzahl von Bits werden die Indizes zufällig ausgewählt
	- stochastisch bei kontinuierlicher Repräsentation:
4. Mutationsoperator bei Sequenzen
	- Herausnehmen einer Teilsequenz und Einfügen an anderer Stelle
	- Invertiertes Einfügen der Teilsequenz
	- Spezielle Mutationsoperatoren -> anwendungsspezifisch
### Rekombination
1. Eigenschaften von zwei oder mehreren Eltern sollen gemischt werden
	- Diskrete Rekombination
	- Intermediäre Rekombination(kontinuierliche Repräsentation)
2. Crossover: aus 2 Eltern -> 2 Nachkommen
	- Single-point crossover
	- Two-point crossover 
	- Uniform crossover
### Selektion
1. 2 Arten der Selektion
	- der Eltern für jeweilige Erzeugung von Nachkommen
	- der Population für die nächste Iteration
2. Probleme:
	- Genetische Drift: Individuen vermehren sich zufällig mehr als andere
	- crowding, Ausreißerproblem: "Fitte" Indiduen und ähnliche Nachkommen dominieren die Population
> Entwicklung der Individuen wird verlangsamt 
> Vielfalt der Population wird eingeschränkt
### Populationsmodelle
1. Inselmodell(lokal)
	- die Evolution läuft weitgehend getrennt, nur manchmal werden Individuen ausgetauscht
2. Nachbarschaftsmodell(nahe Umgebung)
	- Nachkommen dürfen nur von Individuen erzeugt werden, die in ihrer Nachbarschaft die beste Fitness besitzen
3. Eine einfache Menge(global)
	- die global Besten entwickeln sich rasch weiter, andere Entwicklunglinien werden unterdrückt
### Maximumsuche(s. Berthold)
1. Finde Maximum einer Funktion:
	- 3 Populationsgruppen, je 20 Individuen(schwarz, grau, weiß)
	- Individuum: binäre Kodierung(12bit)der x,y Positon
	- Operatoren: Mutation / Inversion, 1-point Crossover
	- Initiale Verteilung, Gene
### Populationsmitglieder
1. Populationsgröße:
	- Soll sie konstant bleiben ? u
	- Wie viele neu erzeugte Nachkommen? lambda
	- wie viele Eltern sollen verwendet werden? p
	- wie werden diese bestimmt?
2. Mitgliederselektion:
	- stochastisch ausgewählt -> die besten u Individuen
	- u, lamda Strategie: bessere Exploration
	- u + lamda: Exploitation, günstig bei gut berechenbaren Fitnessfunktionen
3. Ersetzungsregel für Mitglieder:
	- Nachkommen ersetzten alle Eltern(Generationen - Modus)
	- Nachkommen ersetzten einen Teil der Eltern
	- Nachkommen ersetzten Eltern, die ihnen am ähnlichsten sind
	- Geographische Ersetzung
	- Bestes Individuum überlebt(Elitist - Modus)
4. Daumenregel
	- Das beste Viertel der Population sollte drei Viertel der Nachkommen erzeugen
### Selektionmethoden
1. Fitness basierte Selektion
	Px = fx / all fx genau Px = lamda / u * fx / all fx
	- px: Wahrscheinlichkeit der Auswahl von Individuum x
	- lamda: Anzahl von Nachkommen
	- u: Populationsgröße
	- f: Fitness Funktion
> abhängig vom Wert der Fitnessfunktion
> Problem wenn y.B im Laufe der Evolution nur noch geringe Änderungen in fx und damit in px

2. Rang basierte Selektion 
px =  g(r(x)) / all g(r(x))
	- px: Wahrscheinlichkeit der Auswahl von Individuum x
	- rx: ranking von x in der aktuellen Population gemäß Fitness - Funtion
	- g: mit der Güte des Ranges monoton steigende Funtion größer 0
		- Exponentiell: gx := a -x
		- Hyperbolisch: gx := x -a
		- Die besten K: 
> weniger anhängig von dem Betrag der Fitness
> bessere Anpassung von Exploration / Eploitation durch g

3. Turnier Selektion (tournament selection)
	- wähle für jedes zu erzeugende Individuum n (=2) Individuen
	- belohne davon, das ge,äß der Fitness beste Individuum
	- wähle Individuen mit höchster Bewertung
> wenig anhängig von dem Betrag der Fitness

4. Wahl der Selektionmethode
	- oft anwendungsspezifisch
### Evolution
1. Lamarksche Evolution
	- Individuen ändern sich (lernen) nach der Erzeugung
	- Genotyp(alle Gene) wird verändert und anschließend vererbt
2. Baldwinsche Evolution
	- Individuen ändern sich nach der Erzeugung
	- Genotyp bleibt unverändert
3. Hybride Verfahren
	- es gibt veränderbare und fixe Phänotypen
	- Anwendung: Suche nach ooptimalen neuronalen Netzen
### Beispiel: Travelling Saleman-Problem
1. Finde einene Pfad
	- jeder Ort wird genau einaml besucht
	- der zurückgelegte Weg ist minimal
2. Lösung: Evolutionsstrategie
3. Anwendungsbeispiel: 
	- Flugplanoptimierung
	- Mischung von Kaffeesorten: Markenkaffee sollte immer gleich schmecken, obwohl es immer wieder zu unterschiedlichen Mischverhältnissen kommt. Überliches Vorgehen:Experten mischen solange, bis die Mischung den gewünschten Geschmack hat.
		- Fitnessfunciton: Mensch - Geschmackstester
		- Test der Evolutionsstrategie
		- Vorteil: Auch Kosten und andere Optimierungskriterien können einbezogen werden
		- Anwendungsgebiete: Mischprodukte wie Kako, Tee, Whisky, Kompositionen wie Fliesenglasuren, Farbtöne etc, Kriminalistik: Persionen identifizieren
	- Cybermotten
### Genetische Programmierung
1. Ziel: Erzeugung optimierter Programme
	- Individuen sind Programme
	- Repräsentation z.B als Baum
	- Selektion, Mutation und Rekombination auf Baumstrukturen
	- Fitness: Programmtest auf einer Menge von Testdaten
2. Rekombination als Austausch von Teilbäumen
3. Beispiel 1: 
	- pick and place das Wort zu erzeugen
	- Fitness: Test auf 166 Startkonfigurationen
	- Ergebnis: die beste Programmierung  EQ((DU(MT CS) (NOT CS)))
4. Beispiel 2 Ameise:
	- Ziel: Programm(Steuerung) einer Ameise, s.d. mit Start von (10, 17) das gesamte Futter, wegoptimal gesammelt wird
	- Funtionen:
### Steuerung in der Robotik
#### Snakeboot
#### künstliche Ontogenese
#### Gebobots

