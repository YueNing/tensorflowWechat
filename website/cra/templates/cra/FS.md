# Begriffe
- syntaktisch:
- Term: In der Mathematik ist ein Term sinnvoller Ausdruck, der Zahlen, Variable, Symbole für mathematische Verknüpfungen und Klammern enthalten kann. Terme sind die syntaktisch korrekt gebildeten Wörter oder Wortgruppen in der Formalen Sprache der Mathematik
- logische Zeichen wie Aussagenlogik () 1 0 -> neu in Prädikatenlogik , Allquantor, Existenzquantor
- Signatur: In der mathematischen Logik besteht eine Signatur aus der Menge der Symbole
- Atomare Formeln: Wenn t1 und t2 Terme sind, dann ist t1 = t2 eine Formel. Wenn R ein n-stelliges Relationssymbol und t1,... tn Terme sind, dann ist R(t1,...,tn) eine Formel.
- Formeln: induktiv definiert 
- Substitutionen: Als Substitution bezeichnet man in der Logik allgemein die Erzetzung eines Ausdrucks durch einen anderen. schreiben wir wie {x1/s1,...,xm/sm}  u heisst Grundsubstitution
- Kollisionsfreie Substitutionen: Eine Substitution u heisst kollisionsfrei für eine Formel A, wenn für jede Variable z und jede Stelle freien Auftretens von z in A gilt: Diese Stelle liegt nicht im Wirkungsbereich eines Qauntors all x oder existiert x, wo x eine Variable in u(z) ist.
- Komposition von Subtitutionen
- Unifikation: Unifikation ist eine Methode zur Vereinheitlichung prädikatenlogischer Ausdrücke. Zwei Ausdrücke werden unifiziert, indem ihre Variablen so durch geeignete Terme ersetzt werden, dass die resultierenden Ausdrücke gleich sind. Die Unifikation hat insbesondere in der Computerlogik und Computerlinguistik eine größere Bedeutung erlangt.
- Mächtigkeit: In der Mathematik verwendet man den aus der Mengenlehre von Georg Cantor stammenden Begriff der Mächtigkeit oder Kardinalität, um den für endliche Mengen verwendeten Begriff der "Anzahl der Elemente einer Menge" auf unendliche Mengen zu verallgemeinenrn. Für endliche Mengen ist die Mächtigkeit gleich der Anzahl der Elemente der Menge, das ist eine natürliche Zahl einschlißlich der Null. Für unendliche Mengen benötigt man etwas Vorarbeit, um ihre Mächtigkeiten zu charakterisieren. wie Doppelkreuz # u(T) = 1 oder |u(T)| = 1
- Interpretation: 
- Koinzidenzlemma
- Negationsnormalform: Jedes Negationszeichen in A vor einer atomaren Teilformel steht.
- Pränexe Normalform: B ist eine quantorenfrei Formel. Man nennt B auch die Matrix von A.
- Matrix in Logik: In der prädikatenlogik ist die Matrix einer Formel F diejenige Formel, die man durch Streichen sämtlicher Quantoren aus F erhält. Der Begrif wird vor allem im Zusammenhang mit der Pränexform verwendet, bei der sämtliche Quantoren am Anfang der Formel stehen.
- Skolem Normalform
- These: bezeichnet eine beweisende Behauptung oder einen Leitsatz
- Axiome: Innerhalb einer formalisierbaren Theorie ist eine These ein Satz, der bewiesen werden soll. Ein Axiom ist ein Satz, der nicht in der Theorie bewiesen soll, sondern beweislog vorausgesetzt wird.
- Regeln: 
- Hilbertkalkül: axiomatische Kalkül für die klassische Aussagenlogik oder die Prädikatenlogik erster Stufe, das heißt Kalkühle, in denen sich Theoreme und Argumente der Aussagenlogik oder der Prädikatenlogik erster Stufe herleiten lassen.
- Komposition mittels Modus ponens
- Deduktionstheom
- Resolutionskalkül: Die Resolution ist ein Verfahren der formalen Logik, um eine logische Formel auf Gültigkeit zu testen.
- Resolutionsregel: Die aussagenlogische Resolutionsregel ist die Regel, eine Modifikation des modus ponens. Es ist nämlich auch die Erweiterung von MP.


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
3. Substitutionslemma für Terme
4. Hoare Kalkül
5. Modell
6. Folgerbarkeit
7. Ersetzungstheorem

### 3.3 Normalformen
1. **Skolem-Normalform**
- geschlossen ist
- die Gestalt hat nur Allquantoren im Präfix, mit quantorenfreiem B
- Die Matrix B in KNF ist.

# 4. Beweistheorie
## 4.1 Beispiel
**Kann mein Bruder wäre mein Schawager**
## 4.2 Hilbertkalkül
## 4.3 Resolutionskalkül
## 4.4 Aussagenlogische Tableaukalkül
## 4.5 Prädikatenlogischer Tableaukalkül
## 4.6 Sequenzenkalkül

# 5. Gleichheitslogik
## 5.1 Reduktionssysteme
## 5.2 Termersetzungssysteme

# 6. Die Spezifikationssprache JML
# 7. Modale Aussagenlogik
# 8. Temporale Logik
## 8.1 Lineare Temporale Logik(LTL)
# 9. Modellprüfung
## 9.1 Büchi Automaten und LTL 
 
# Logik
[Logik](https://wenku.baidu.com/view/59e21590284ac850ad024253.html)
[-| Logik](https://wenku.baidu.com/view/7181e50e581b6bd97f19ea77.html)
