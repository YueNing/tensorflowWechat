# 1. Aussagenlogik: Syntax und Semantik
## 1.1 Syntax der Aussagenlogik
	- Zeichen
1. Logische Zeichen: in jeder Aussagenlogik vorzukommen, wie 1, 0, nicht, und, oder, wenn...dann, genau dann...wenn(beiderseitige Implikation) 
2. Signatur: Sigma, von Fall zu Fall davon abzuweichen und andere Signaturen zu vereinbaren.
3. Eine bestimmte aussagenlogische Sprache entsteht erst durch die Festleung einer Signatur
4. Suffix "0" in For0sigma bedeutet, dass wir in der Aussagenlogik befinden.
5. Schachtelungstiefe von Formeln
6. Komplexitätsmaße:
	- L(A) = Anzahl der Atomvorkommen in A
	- Op(A) = Anzahl de Vorkommen von **und** oder **oder** in A
	- für jede Formel A, die nur die Operatoren **und** oder **oder** enthält, die Gleichung gilt L(A) = Op(A) + 1

## 1.2 Semantik der Aussagenlogik
### 1.2.1 Boolesche Funktionen
### 1.2.2 Basen
Eine Menge KOp von aussagenlogischen Konstanten und Operatoren, so daß für jede Boolesche Funktion eine Formel A existiert, die nur mit Konstanten und Operatoren aus KOp aufgebaut ist ,und fa = f erfüllt, nennt man eine(aussagenlogische) Basis.
- Basen: {nicht, und} weitere Basis ist {0, implikation}
### 1.2.3 Logisches Schließen
M |= A: Man nennt die allgemeingültigen Formeln auch Tautologien. Erst in der Prädikatenlogik werden beiden Begriffe differieren.
- Logische Äquivalenz: A und B heißen logisch äquivalent, in Symbolen A drei strichen B für alle Interpretationen I gilt vali(A) drei Strichen vali(B)
- Erzetungslemma
### 1.2.4 Tautologien
### 2.3.5 Interpolanten
- Craigsches Interpolationslemman: Zu je zwei aussagenlogischen Formeln A,B, so daß A-> B eine Tautologie ist, existiert eine Interpolante.
A[1] oder A[0] die aussagenlogischen Variable, die in A aber nicht in B vorkommen.

## 1.3 Normalformen
### 1.3.1 Disjunktive und konjunktive Normalform
### 1.3.2 Primimplikanten
- eine Konjuntion von Literalen
- so daß P-> C eine Tautologie ist, und
- für jede Teilkonjunktion P' von P ist P' -> C keine Tautologie
### 1.3.3 Kurze Konjunktive Normalform
### 1.3.4 Shannon Formeln
- Jedem nichtterminalen Knoten v ist eine natürliche Zahl index(v) zugeordnent.
- Von jedem nichtterminalen Knoten v gehen zwei Kanten aus. Eine davon ist mit F, die andere mit W gekennzeichnet.
- Jedem terminalen Knoten v ist eine der Zahlen F oder W zugeordnet, bezeichnet mit wert(v).
- Ist der nichtterminale Knoten w ein unmittelbarer Nachfolger von v, dann gilt index(v) < index(w)
- Es gibt genau einen Wurzelknoten.
**Wegen der vierten Forderung ist jeder sh-Graph zyklenfrei**

# 2. Aussagenlogik: Erfüllbarkeitstest
## 2.1 DPLL
**einzige Variable auszuwählen, wenn es gibt. Sonst, wählen eine Variable mit P und nicht P , weiter die Fallunterscheidung zu machen.**
## 2.2 Horn-Formeln
**Markierungsalgorithmus**

# 3. Prädikatenlogik
### 3.1 Syntax der Prädikatenlogik
1. **Terme und Formeln**:
2. **Gebundene und freie Variable**
3. **Unifikation**
4. **Unifikationsalgorithmus**
5. **Literatur**
[Prädikatenlogik](https://wenku.baidu.com/view/0bfc1e302b160b4e777fcf24.html)

### 3.2 Semantik der Prädikatenlogik
1. **Interpretation**
2. **Allegemeingültigkeit**

### 3.3 Normalformen
1. **Skolem-Normalform**

# 4. Beweistheorie
## 4.1 Beispiel
**Kann mein Bruder wäre mein Schawager**
## 4.2
 
# Logik
[Logik](https://wenku.baidu.com/view/59e21590284ac850ad024253.html)
[-| Logik](https://wenku.baidu.com/view/7181e50e581b6bd97f19ea77.html)
