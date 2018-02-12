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
>> Für jede Attributeinschränkung a0 in h=<a0, ..., an>
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
### 5.2 ID3 
### 5.3 Overfitting
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
### Der K-NN Algorithmus
### Case-Based Reasoning: Motivation und Vorstellung
### Der Case-Based Reasoning Zyklus
### Beispiel für den Einsatz von CBR
### Bewertung von CBR

## Evolutionäre Algorithmen
### Vorkenntnis
### Nomenklatur
### Der Grundalgorithmus
### Repräsentation von Nachkommen
### Mutation
### Rekombination
### Beispiel
### Selektion
### Populationsmodelle
### Maximumsuche(s. Berthold)
### Populationsmitglieder
### Selektionmethoden
### Evolution
### Beispiel: Travelling Saleman-Problem
### Anwendungsbeispiel
#### Mischung von Kaffeesorten
#### Cybermotten
### Genetische Programmierung
### Beispiel
#### Ameise
### Steuerung in der Robotik
#### Snakeboot
#### künstliche Ontogenese
#### Gebobots

