[![AppleHome](https://storage.googleapis.com/ning_picture/mainlogo.png)](http://www.jumpen.me/)
# [Übungen](https://max.book118.com/html/2015/0329/13938158.shtm)
# Aussagenlogik
### Definition der logischen Grundbegriffe
1. Erfüllbarkeit
2. Allgemeingültigkeit
3. M |= A
4. Boolesche Funtion f_a einer Formel A

### Definition der verschiedenen Normalformen
1. Disjunktive Normalform
2. Konjunktive Normalform
3. Negationsnormalform
4. Kurze konjunktive Normalform
5. Shannon Normalform
6. Reduzierte Shannongraphen

### Graigscher Interpolationssatz
### Einfache aussagenlogische Tautologie erkennen
### Gegebene Formeln in Normalformen transformieren
### Shannongraphen zu Boolesche Funktionen konstruieren und umgekehrt
### SAT soler DPLL
### Für einfache Formeln mit Hilfe des DPLL Erfüllbarkeit bzw. Unerfüllbarkeit feststellen.
### Einfache Anwendungen durch aussagenlogische Formeln formalisieren können

# Prädikatenlogik
### Definition der Formeln und der Strukturen für PK1
### Substitution
### Den Begriff Unifikation kennen und berechnen
### Die logischen Grundbegriffe
### Einfache semantische Tautologien
### Einfache Sachverhalte in PL1 formalisieren
### Definition der verschiedenen Normalformen
### Gegebene Formeln in Normalformen transformieren
### Die Aussage des Substitutionslemmas kennen
### ???? Den Satz von Herband kennen

# Beweistheorie
### Die Ziele der Beweistheorie verstehen
### Grundidee des Hilbertkalkül verstehen
**Axiom**
- Ax1 $$A \to (B \to A)$$ &nbsp;&nbsp; (Abschwächung)
- Ax2 $$(A \to (B \to C)) \to ((A \to B) \to (A \to C))$$ &nbsp;&nbsp; (Verteilung von $$\to$$)
- Ax3 $$(\neg A \to \neg B) \to (B \to A)$$
- Ax4 $$\forall{x} A \to \{x/t\}(A) \space\space\space\space wobei \space\space\{x/t\} \space\space kollisionsfrei\space\space für\space\space A$$
- Ax5 $$\forall{x} (A \to B) \to (A \to  \forall{x} B) \space\space wobei\space x \notin Frei(A)$$
- Gl1 $$x \doteq x$$
- Gl2 $$x \doteq y \to y \doteq x$$
- Gl3 $$x \doteq y \to (y \doteq z \to x \doteq z)$$
- Gl4
- Gl5
**Regeln**
- Mp: $$\frac {A,\space A \to B}{B}$$
- Gen: $$\frac{A}{\forall{x} A}$$

**Lemma**
- Komposition mittels Modus ponens
$$M_1 \vdash_H A, M_2 \vdash_{H_0} A \to B \Rightarrow M_1 \cup M_2 \vdash _H B$$
- Deduktionstheom
$$M \vdash_H A \to B \Leftrightarrow M \cup \{A\} \vdash_H B$$

### Resolutionskalkül, Tableaukalkül kennen

**Resolutionsregel Die aussagenlogische Resolutionregel**
- $$\frac {C_1 \cup \{P\}, \space C_2 \{\neg P\}}{C_1 \cup C_2} \space \space C_1 \cup C_2 \space \space heisst \space\space Resolvente$$

**Resolutionsregel Die prädikatenlogische Resolutionregel**
- $$\frac {C_1 \cup K_1 \space \space C_2 \cup K_2}{\mu(C_1 \cup C_2)} \space \space \space \mu$$ ist allgemeinster Unifikator von $$K_1 \cup \sim K_2$$

**Tableau Vorbemerkung**
$$M \models A \Leftrightarrow M \cup \{ \neg A\} \vdash _\bm{T_0} \bm{0}$$
**Definition Tableau(Typen von Vorzeichenformeln)**
- $$Typ \space \epsilon:\space 0P, 1P\space für P \in \Sigma$$
- $$Typ \space \alpha: \space 0\neg B, 1\neg B, 1(B\land C), 0(B \lor C), 0(B \to C)$$
- $$Typ \space \beta: \space 0(B \land C), 1(B \lor C), 1(B \to C)$$

**Lemma**

### Beweisidee für den Korrektheits- und Vollständigkeitsbeweis des aussagenlogischen Resolutionskalkül kennen
### Beweisidee für den Korrektheits- und Vollständigkeitsbeweis des Tableaukalküls kennen
### Für kleine Beispiele Ableitungen im Resolutionskalkül und Tableaukalkül, für Aussagen- und Prädikatenlogik, finden können
### Aussagenlogische Tableauregeln aus Wahrheitstafeln konstruieren

# PEANO ARITHMETIK
### Grundidee der Peano Arithmetik kennen
### Entscheidbarkeitsresultate zur Peano Arithmetik kennen.

# JML
### Grundlegende Konzepte von JML kennen
### Einfache JML Spezifikationen lesen und erklären können
### einfache Spezifikationen in JML formalisieren können

# Reduktionssysteme
### Wichtigsten Eigenschaften von Reduktionssystemen und die Zusammenhänge zwischen ihnen kennen
### Gerichtete Termersetzungssystem kennen und kleine Beispiel rechnen können

# Modale Logik
### Definition von Syntax und Semantik(Kripke Strukturen)
### Allgemeingültige Formeln erkennen können, auch für Allgemeingültigkeit relativ zu Kripke Strukturen mit Einschränkungen und die Zugänglichheitsrelation R.
### Für einfache Eigenschaften von R charakterisierende Formeln finden

# LTL 
### LTL-Formeln lesen können
### Einfache temporale Eigenschaften in LTL formalisieren
### Zusammenhang zwischen LTL und Büchi Automaten kennen
### Konzept der LTL Modellprüfung kennen
