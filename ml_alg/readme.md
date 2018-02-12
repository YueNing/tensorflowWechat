# ML 1

## Einführung
### Allgemeine Information
### Einführung und Überblick
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
### Literaturhinweise

## Induktives Lernen
### Induktion & Deduktion
- **Induktion**: Prozess des plausiblen Schließens vom Speziellen zum Allgemeinen
	- Basis: große Anzahl zutreffender Fälle
		![gailvgongshi]()
- **Deduktion**: Modus Ponens 
	![]()
- Vergleich:
	|      Induktion      |     Deduktion      |
	|:-------------------:|:------------------:|
	| Wahrheitserweiternd | Wahrheitserhaltend |
	| Macht Lebewesen     | Logischer Schluss  |
	| überlebensfähig     | Korrektheit        |
	| Plausibilität       |                    |
- Induktive Lernhypothese:
Jede Hypothse, die die Zielfuntion über einer genügend großen Menge von Trainingsbeispielen gut genug approximiert, wird die Zielfuntion auch über unbekannten Beispielen gut approximieren.	     
### Konzeptlernen als Suche im Hypothesenraum
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
#### Suche vom Allgemeinen zum Speziellen
1. Ausgangspunkt ist allgemeinste Hypothese <?, ...., ?>
2. Negative Beispiele: Spezialisierung
3. Positive Beispiele: werden nicht betrachtet
#### Suche vom Speziellen zum Allgemeinen
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
 
#### Paralleles Anwenden beider methoden => Version Space
Der Versionsraum VSH,D bezüglich des Hypothesenraums H und der Menge von Trainingsbeispielen D ist die Untermenge der Hypothesen von H, die mit den Trainingsbeispielen in D konistent ist.
##### Versionraum(Version Space) / Gandidate-Elimination-Algorithmen
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
### Notwendigkeit von Vorzugskriterien(Bias)
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

## Unüberwachtes Lerenen
### Motivation & Einführung
### K-means Clustering
### Hierarchisches Clustering
### Begriffliche Ballungen & COBWEB
### Ausblick

## Lerntheorie, Algorithmenunabhängige Verfahren
### PAC
### Modell
### Lernmaschine
### VC-Dimension

## Entscheidungsbäume
### Motivation
### ID3 
### Overfitting
### Erweiterungen
### C4.5
### ID5R
### Random-Forests
### Zusammenfassung

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

