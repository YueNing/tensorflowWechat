[![AppleHome](https://storage.googleapis.com/ning_picture/mainlogo.png)](http://www.jumpen.me/)
# [Übungen](https://max.book118.com/html/2015/0329/13938158.shtm)
# 1. Aussagenlogik
### 1.1 Definition der logischen Grundbegriffe
1. Erfüllbarkeit
2. Allgemeingültigkeit
3. M |= A
4. Boolesche Funtion f_a einer Formel A

### 1.2 Definition der verschiedenen Normalformen
1. Disjunktive Normalform
2. Konjunktive Normalform
3. Negationsnormalform
4. Kurze konjunktive Normalform
5. Shannon Normalform
6. Reduzierte Shannongraphen

### 1.3 Graigscher Interpolationssatz
### 1.4 Einfache aussagenlogische Tautologie erkennen
### 1.5 Gegebene Formeln in Normalformen transformieren
### 1.6 Shannongraphen zu Boolesche Funktionen konstruieren und umgekehrt
### 1.7 SAT soler DPLL
### 1.8 Für einfache Formeln mit Hilfe des DPLL Erfüllbarkeit bzw. Unerfüllbarkeit feststellen.
### 1.9 Einfache Anwendungen durch aussagenlogische Formeln formalisieren können
_________________________________________________________________________________________________________
# 2. Prädikatenlogik
### 2.1 Definition der Formeln und der Strukturen für PK1
### 2.2 Substitution
### 2.3 Den Begriff Unifikation kennen und berechnen
### 2.4 Die logischen Grundbegriffe
### 2.5 Einfache semantische Tautologien
### 2.6 Einfache Sachverhalte in PL1 formalisieren
### 2.7 Definition der verschiedenen Normalformen
### 2.8 Gegebene Formeln in Normalformen transformieren
### 2.9 Die Aussage des Substitutionslemmas kennen
### 2.10 ???? Den Satz von Herband kennen
_________________________________________________________________________________________________________
# 3. Beweistheorie
### 3.1 Die Ziele der Beweistheorie verstehen
### 3.2 Grundidee des Hilbertkalkül verstehen
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


### 3.3 Resolutionskalkül, Tableaukalkül kennen

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
Für eine Vorzeichenformel V gilt
- vom Typ $$\alpha: val_I(V) = W \Leftrightarrow val_I(V_1) = W \space und\space val_I(V_2) = W$$ 
- vom Typ $$\beta: Val_I(V) = W \Leftrightarrow val_I(V_1) = W\space oder \space val_I(V_2)=W$$

**Prädikatenlogischer Tableaukalkül**
- Typ $$\epsilon: 1A, 0A$$ für atomare Formeln A
- Typ $$\alpha$$ 
- Typ $$\beta$$
- Typ $$\gamma$$
- Typ $$\delta$$

**Zusammenfassung der Tableauregeln in Kurzform**
- $$\alpha$$-Regel &nbsp;&nbsp; $$\frac{V}{V_1}$$ für $$\alpha$$-Formeln V
- $$\beta$$-Regel &nbsp;&nbsp; $$\frac{V}{V_1|V_2}$$ für $$\beta$$-Formeln V
- $$\gamma$$-Regel &nbsp;&nbsp; $$\frac{V}{V_1(y)}$$ für $$\gamma$$-Regel V und jede Variable y, die auf dem Pfad noch nicht vorkommt
- $$\delta$$-Regel $$\frac{V}{V_1(f(x_1, ..., x_n)}$$ für $$\delta$$-Formeln V, wobei $$x_1, ..., x_n$$ alle freien Variablen in V sind und f ein neues n-stelliges Funktionssymbol
- Anfangsregel &nbsp;&nbsp; $$\frac{}{0A}$$ für die zu beweisende Formel A A ohne freie Variable
- V-Regel &nbsp;&nbsp; $$\frac{}{1B}$$ für jedes B $$\in M$$ B ohne freie Variable

### 3.4 Sequenzenkalkül
**Der aussagenlogische Kalkül**
| |  |
|:--:| :--: |
|axiom |impl-right
$$\frac{}{\Gamma,\space F\space \Rightarrow\space F, \space\Delta}$$|$$\frac{\Gamma,\space F\space\Rightarrow\space G,\space\Delta}{\Gamma\space\Rightarrow\space F\space\rightarrow\space G,\space\Delta}$$|
|0-left | and-left
$$\frac{}{\Gamma ,\space \bm{0}\space\Rightarrow\space \Delta}$$|$$\frac{\Gamma,\space F,\space G\space\Rightarrow\space\Delta}{\Gamma,\space F\land G\space\Rightarrow\space\Delta}$$|
|1-right | and–right
$$\frac{}{\Gamma\space\Rightarrow\space \bm{1},\space\Delta}$$|$$\frac{\Gamma,\space\Rightarrow\space F,\space\Delta\space\space\Gamma\space\Rightarrow G,\space\Delta}{\Gamma\space\Rightarrow\space F\land G,\space\Delta}$$|
|not-left | or-left
$$\frac{\Gamma,\space\Rightarrow\space F,\space \Delta}{\Gamma,\space\neg F\space\Rightarrow\space\Delta}$$|$$\frac{\Gamma,\space F\space\Rightarrow\space\Delta\space\space \Gamma,\space G\space\Rightarrow\space\Delta}{\Gamma,\space F\lor G\space\Rightarrow\space\Delta}$$|
|not-right | or-right
$$\frac{\Gamma,\space F\space\Rightarrow\space\Delta}{\Gamma\space\Rightarrow\space\neg F,\space\Delta}$$|$$\frac{\Gamma\space\Rightarrow\space F,\space G,\space\Delta}{\Gamma\space\Rightarrow\space F\lor G,\space\Delta}$$|
|impl-left
$$\frac{\Gamma\space\Rightarrow\space F,\space\Delta\space\space\Gamma,\space G\space\Rightarrow\space\Delta}{\Gamma,\space F\space\rightarrow\space G\space\Rightarrow\space\Delta}$$||

**Der prädikatenlogische Kalkül**
| |  |
|:--:| :--: |
|all-left|all-right|
|||
|all-right|ex-right|

**Sequenzenregeln für die Gleichheit**
| |  |
|:--:| :--: |
|identity|eq-subst-right|
|||
|symmetry-right|eq-subst-left|
|||
|symmetry-left||

### 3.5 Beweisidee für den Korrektheits- und Vollständigkeitsbeweis des aussagenlogischen Resolutionskalkül kennen
### 3.6 Beweisidee für den Korrektheits- und Vollständigkeitsbeweis des Tableaukalküls kennen
### 3.7 Für kleine Beispiele Ableitungen im Resolutionskalkül und Tableaukalkül, für Aussagen- und Prädikatenlogik, finden können
### 3.8 Aussagenlogische Tableauregeln aus Wahrheitstafeln konstruieren
___________________________________________________________________________________________________________
# 4. PEANO ARITHMETIK

### 4.1 Grundidee der Peano Arithmetik kennen
### 4.2 Entscheidbarkeitsresultate zur Peano Arithmetik kennen.
___________________________________________________________________________________________________________
# 5. JML
### 5.1 Grundlegende Konzepte von JML kennen
### 5.2 Einfache JML Spezifikationen lesen und erklären können
### 5.3 einfache Spezifikationen in JML formalisieren können
___________________________________________________________________________________________________________
# 6. Reduktionssysteme
### 6.1 Wichtigsten Eigenschaften von Reduktionssystemen und die Zusammenhänge zwischen ihnen kennen
### 6.2 Gerichtete Termersetzungssystem kennen und kleine Beispiel rechnen können
___________________________________________________________________________________________________________
# 7. Modale Logik
### 7.1 Definition von Syntax und Semantik(Kripke Strukturen)
**Lemma Allgemeingültige modale Formeln**
1. Jede aussagenlogische Tautologie ist eine allgemeingültige modale Formel
2. $$\Box(A\rightarrow B)\rightarrow(\Box A\rightarrow\Box B)$$
3. $$(\Box A\land \Box B)\leftrightarrow\Box(A\land B)$$
4. $$(\Box A \lor \Box B) \rightarrow \Box(A\lor B)$$
5. $$\Box A \leftrightarrow(\neg\Diamond\neg A)$$
6. $$\Diamond A \leftrightarrow(\neg\Box\neg A)$$
7. $$(\Diamond A\lor \Diamond B)\leftrightarrow\Diamond(A\lor B)$$
8. $$\Diamond(A\land B)\rightarrow(\Diamond A\land \Diamond B)$$
9. $$(\Box(A\rightarrow B)\land \Box(B\rightarrow A))\leftrightarrow\Box(A\leftrightarrow B)$$
10. $$\Box(A\rightarrow B)\rightarrow(\Diamond A\rightarrow\Diamond B)$$

**Lemma Relative Allgemeingültigkeit modaler Formeln**
1. In der Klasse aller reflexiven Kripke-Strukturen ist allgemeingültig:
$$\Box A\rightarrow A$$
2. In der Klasse aller transitiven Kripke-Strukturen ist allgemeingültig:
$$\Box A \rightarrow \Box\Box A$$
3. In der Klasse aller symmetrischen Kripke-Strukturen ist allgemeingültig:
$$A\rightarrow \Box\Diamond A$$
4. In der Klasse aller dichten Kripke-Strukturen ist allgemeingültig:
$$\Box\Box A \rightarrow \Box A$$
5. In der klasse aller partiell funtionalen Kripke-Strukturen ist allgemeingültig:
$$\Diamond A \rightarrow \Box A$$
6. In der Klasse aller endlosen Kripke-Struturen ist allgemeingültig:
$$\Box A \rightarrow \Diamond A$$

**Charakterisierungen**

### 7.2 Allgemeingültige Formeln erkennen können, auch für Allgemeingültigkeit relativ zu Kripke Strukturen mit Einschränkungen und die Zugänglichheitsrelation R.
### 7.3 Für einfache Eigenschaften von R charakterisierende Formeln finden
____________________________________________________________________________________________________________

# 8. LTL 
### 8.1 LTL-Formeln lesen können
### 8.2 Einfache temporale Eigenschaften in LTL formalisieren
### 8.3 Zusammenhang zwischen LTL und Büchi Automaten kennen
### 8.4 Konzept der LTL Modellprüfung kennen
_____________________________________________________________________________________________________________
