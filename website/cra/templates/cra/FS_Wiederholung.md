<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
![](https://storage.googleapis.com/ning_picture/grun.png)
# [Übungen](https://max.book118.com/html/2015/0329/13938158.shtm)
# 1. Aussagenlogik
### 1.1 Definition der logischen Grundbegriffe
1. Erfüllbarkeit
2. Allgemeingültigkeit
3. M |= A
4. Boolesche Funtion $$f_a$$ einer Formel A

### 1.2 Definition der verschiedenen Normalformen
1. Disjunktive Normalform
$$(A_1\land A_2\land A_3) \lor (A_4\land A_5\land A_6)...$$
2. Konjunktive Normalform
$$(A_1 \lor A_2 \lor A_3) \land (A_4 \lor A_5\lor A_6)...$$
3. Negationsnormalform
$$\neg P_1$$
4. Kurze konjunktive Normalform
$$(\neg Q \lor (L_1 \space op\space L_2)) \land (Q \lor \neg (L_1 \space op\space L_2))$$
5. Shannon Normalform
$$sh(P_1, P_2, P_3)\leftrightarrow(\neg P_1\land P_2)\lor(P_1\land P_3)$$
6. Reduzierte Shannongraphen

### 1.3 Graigscher Interpolationssatz
> Zu je zwei aussagenlogischen Formeln A, B, so daß $$A\rightarrow B$$ eine Tautologie ist, existiert eine Interpolante

### 1.4 Einfache aussagenlogische Tautologie erkennen
> Tautologie ist der einfachste logische Schluß. Wenn man A schon weiß, so kann man, sozusagen in 0 Schritten, daraus A ableiten.
> Tautologie spiegelt eine wichtige Voraussetzung für die Aussagenlogik, wie wir sie in diesem Text präsentieren
> Tautologie ist letzten Endes eine Konsequenz aus der Festlegung der Wahrheitstafel für die Implikation $$\rightarrow$$
### 1.5 Gegebene Formeln in Normalformen transformieren
> $$A\leftrightarrow(B\leftrightarrow C)
> \leftrightarrow(A\land \neg B \land \neg C)\lor (\neg A\land\neg B\land C)\lor (\neg A\land\neg C\land B)$$

### 1.6 Shannongraphen zu Boolesche Funktionen konstruieren und umgekehrt
>![](https://storage.googleapis.com/ning_picture/shannonbf.png)
### 1.7 SAT soler DPLL
1. Einerkausel auswählen wenn es gibt
2. Literal auswählen wenn es gibt keine Einerklausel

### 1.8 Für einfache Formeln mit Hilfe des DPLL Erfüllbarkeit bzw. Unerfüllbarkeit feststellen.
>![](https://storage.googleapis.com/ning_picture/DPLL.png)
### 1.9 Einfache Anwendungen durch aussagenlogische Formeln formalisieren können
_________________________________________________________________________________________________________
# 2. Prädikatenlogik
### 2.1 Definition der Formeln und der Strukturen für PK1
1. Logische Zeichen
2. Signatur Tripel $$\Sigma=(F_\Sigma, P_\Sigma, \alpha_\Sigma)$$
3. Terme
4. Atomare Formeln
5. Formeln
6. Gebundene und freie Variable  
Beispiel: $$\forall x(p_0(x, y)\rightarrow\forall z(\exists y\space p_1(y, z) \lor \forall x\space p_2(f(x), x)))$$
treten x und z nur gebunden auf, y tritt frei und gebunden auf.

### 2.2 Substitution
Beispiel:
> Für $$\sigma = \{x/f(x, y), y/g(x)\} \space gilt\space \sigma(f(x, y)= f(f(x, y), g(x))$$
> Für $$\mu = \{x/c, y/d\} \space gilt\space \mu(\exists y\space p(x, y)) = \exists y\space p(c, y)$$
> Für $$\sigma_1 = \{x/f(x, x)\}\space gilt\space \sigma_1(\forall y\space p(x, y)) = \forall y\space p(f(x, x), y)$$
> Für $$\mu_1 = \{x/y\}\space gilt\space \mu_1(\forall y\space p(x, y)) = \forall y\space p(y, y)$$
### 2.3 Den Begriff Unifikation kennen und berechnen
Beispiel
> $$\{f(g(a, x), g(y, b)), f(z, g(v, w)), f(g(x, a), g(v, b))\}$$ wird unifiziert durch $$\{x/a, y/v, z/g(a, a), w/b\}$$

### 2.4 Die logischen Grundbegriffe
1. Substitutionslemma für Terme
2. Substitutionslemma für Formeln
3. Hoare-Kalkül
4. Modell
5. Folgerbarkeit
6. $$A\in For_\Sigma$$ ohne freie Variablen heißt
    - allgemeingültig gdw $$\models A$$
    - erfüllbar gdw $$\neg A$$ ist nicht allgemeingültig
### 2.5 Einfache semantische Tautologien
> $$A \in For_\Sigma$$ ohne freie Variablen heißt Tautologie, wenn es eine endliche aussagenlogische Signatur

### 2.6 Einfache Sachverhalte in PL1 formalisieren
> ...

### 2.7 Definition der verschiedenen Normalformen
1. negationsnormalform
Jedes Negationszeichen in A vor einer atomaren Teilformel steht.
2. Pränexe Normalform
$$Q_1x_1...Q_nx_n B$$
$$\forall y(\forall x\forall y\space p(x,y)\rightarrow\space \exists x\space r(x, y)) \Leftrightarrow \space \forall y \exists x \exists z \exists u\space (p(x, z)\rightarrow r(u, y))$$
3. Skolem-Normalform
Allquantoren im Präfix mit quantorenfreiem B und Matrix in KNF
Beispiel: 
    - Gegeben: $$\forall x(\exists y(p(y)) \land\exists z(q(x, z))$$
    - Pränex Normalform: $$\forall x\exists y\exists z(p(y)\land q(x, z))$$
    - Skolem Normalform: $$\forall x(p(f_1(x))\land q(x, f_2(x)))$$
### 2.8 Gegebene Formeln in Normalformen transformieren
> ...
### 2.9 Die Aussage des Substitutionslemmas kennen
1. Substitutionslemma für Terme
$$val_{D,\beta}(\sigma(t)) = val_{D, \beta'}(t)$$ wobei $$\beta'(x) = val_{D, \beta}(\sigma(x))$$
2. Substitutionslemma für Formeln
Gleich wie Term

### 2.10 ???? Den Satz von Herband kennen
> ...
_________________________________________________________________________________________________________

# 3. Beweistheorie
### 3.1 Die Ziele der Beweistheorie verstehen
> ...
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
1. Gilt $$M \vdash_{\bf{R}} \Box$$, dann ist M nicht erfüllbar
2. Ist M nicht erfüllbar, dann folgt $$M \vdash_{\bf{R}} \Box$$
3. Beweis
    - Beliebige klauselmenge M für alle $$n\geq 0$$ wenn $$R^n(M)$$ erfüllbar ist, dann ist auch $$R^{n+1}(M)$$ erfüllbar

### 3.6 Beweisidee für den Korrektheits- und Vollständigkeitsbeweis des Tableaukalküls kennen
1. Korrektheitslemma
2. Vollständigkeitslemma

### 3.7 Für kleine Beispiele Ableitungen im Resolutionskalkül und Tableaukalkül, für Aussagen- und Prädikatenlogik, finden können
> ...

### 3.8 Aussagenlogische Tableauregeln aus Wahrheitstafeln konstruieren
|$$1(A  \land B)$$|$$0(A\land B)$$|
|---|----|
|$$1A$$|$$0A\|0B$$|
|$$1B$$|
___________________________________________________________________________________________________________

# 4. PEANO ARITHMETIK
### 4.1 Grundidee der Peano Arithmetik kennen
> Peano Arithmetik

Axiom
### 4.2 Entscheidbarkeitsresultate zur Peano Arithmetik kennen.
> ...
___________________________________________________________________________________________________________

# 5. JML
### 5.1 Grundlegende Konzepte von JML kennen
1. Anfangsfall
2. Iterationsschritt
3. Anwendungsfall
4. Keyword
    - public normal_behaviour
    - requiers
    - assignable 
    - ensures
    - invariant
    - nullable
    - non_null
    - loop_invariant
    - decreases
    - \result
    - \forall
    - \nothing
    - \forall
    - \exists
    - \sum
    - \product
    - \max
    - \min

### 5.2 Einfache JML Spezifikationen lesen und erklären können
> ...

### 5.3 einfache Spezifikationen in JML formalisieren können
> ...
___________________________________________________________________________________________________________

# 6. Reduktionssysteme
### 6.1 Wichtigsten Eigenschaften von Reduktionssystemen und die Zusammenhänge zwischen ihnen kennen
> Ein **Reduktionssystem** $$(D, \succ)$$ besteht aus einer nichtleeren Menge D und einer beliebigen, binären Relation $$\succ$$ auf D
1. Notation
    - $$\rightarrow$$ die reflexive, transitive Hülle von $$\succ$$
    - $$\frac{+}{\to}$$ transitiv
    - $$\leftrightarrow$$ reflexiv, transitiv, symmetrisch
2. **lokal konfluent:** Am End zu die gleiche Gleichung

### 6.2 Gerichtete Termersetzungssystem kennen und kleine Beispiel rechnen können
> Ist E eine endliche Menge von Gleichungen über der Signatur $$\Sigma$$, dann nennen wir das Reduktionssystem($$Term_\Sigma, \to E$$) ein Termersetzungssystem

Beispiel1:
$$0\land x = 0 \space\space\space\space 1\land x = x$$
$$x\land 0 = 0 \space\space\space\space x\land 1 = x$$
$$0 \lor x = x \space\space\space\space 1 \lor x = 1$$
$$x \lor 0 = x \space\space\space\space x \lor 1 = 1$$
Für jeden variablenfreien Booleschen Term t filt $$t\to _E 0 \space oder\space t\to_E 1$$

Beispiel2:
1. $$0+x = x$$
2. $$(x+y)+z = x+ (y+z)$$
3. $$i(x) + x = 0$$
$$\Rightarrow$$ Der Term $$(i(x) + x) +z$$ mit 3 zu $$0+z$$ und weiter zu $$z$$ mit 1, mit 2 zu $$i(x) + (x+z)$$, diese eine Normalform und nicht weiter reduzierbar. nicht zu z reduzieren lassen. Deswegen $$E_G$$ ist also nicht lokal konfluent
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



### 7.2 Allgemeingültige Formeln erkennen können, auch für Allgemeingültigkeit relativ zu Kripke Strukturen mit Einschränkungen und die Zugänglichheitsrelation R.
1. A allgemeingültig $$\Leftrightarrow\space\space\space val_{\kappa, s}(A) = W$$ für alle $$\kappa = (S, R, I)$$ und alle $$s \in S$$
2. A erfüllbar $$\Leftrightarrow$$ es gibt eine $$\kappa$$ und ein $$s\in S\space mit \space val_{\kappa, s}(A) = W$$ 

### 7.3 Für einfache Eigenschaften von R charakterisierende Formeln finden

**Charakterisierungen**
1. $$\Box A \rightarrow A$$ reflexive Kripke-Rahmen
2. $$\Box A \rightarrow\Box\Box A$$ transitive
3. $$A \rightarrow \Box\Diamond A$$ symmetrische
4. $$\Box\Box A \rightarrow \Box A$$ dichte
5. $$\Diamond A\rightarrow \Box A$$ partielle
6. $$\Box A \rightarrow\Diamond A$$ endlose
____________________________________________________________________________________________________________

# 8. LTL 
### 8.1 LTL-Formeln lesen können
> ...

### 8.2 Einfache temporale Eigenschaften in LTL formalisieren
1. $$\xi \models p$$
2. $$\xi \models op(A, B)$$
3. $$\xi \models \Box A$$ gdw forall
4. $$\xi \models \Diamond A$$ gdw exists
5. $$\xi \models AUB$$ gdw until
6. $$\xi \models X A\space gdw\space\xi_1=A$$ 

### 8.3 Zusammenhang zwischen LTL und Büchi Automaten kennen
> LTL zu BA and BA zu LTL transformieren

### 8.4 Konzept der LTL Modellprüfung kennen
> Alle mögliche Aussagen mit LTL Omega-Struktur
_____________________________________________________________________________________________________________

[![AppleHome](https://storage.googleapis.com/ning_picture/mainlogo.png)](http://www.jumpen.me/)
