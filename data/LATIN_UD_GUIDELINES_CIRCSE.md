# OFFICIAL LATIN UD GUIDELINES (With Latin Specifications)

This document groups the Universal Dependencies (UD) annotation guidelines for Latin, with specific details pertinent to the **UD_Latin** treebanks.

---

## 1. TOKENIZATION & WORD SEGMENTATION

### Enclitics (-que, -ve, -ne)
*   **Rule**: Enclitics must be split into separate tokens.
*   **Example**: `arma virumque` -> `arma`, `virum`, `que`.
*   **Attachment**: The enclitic (usually `CCONJ`) attaches to the word it is appended to using the `cc` relation (or `cc:preconj`).

---

## 2. CORE ARGUMENTS & VALENCY

### [nsubj](https://universaldependencies.org/u/dep/nsubj.html)
A nominal subject (nsubj) is a nominal which is the syntactic subject and the proto-agent of a clause.
*   **nsubj**: Standard nominal subject.
*   **nsubj:pass**: Used for the subject of a passive verb. *Latin heavily uses this subtype for clarity.*

### [obj](https://universaldependencies.org/u/dep/obj.html) vs [obl:arg](https://universaldependencies.org/u/dep/obl-arg.html)

#### **obj**
The object of a verb is the second most core argument of a verb after the subject (traditionally Accusative).

#### **obl:arg** (Selected Argument)
The relation `obl:arg` is used for **oblique arguments selected by the valency** of the predicate. This distinguishes them from adjuncts.
*   **Latin Specifics**: 
    *   Verbs taking Dative arguments (*parcere*, *imperare*, *nuber*): Use `obl:arg`.
    *   Verbs taking Ablative arguments (*frui*, *uti*, *egeo*): Use `obl:arg`.
    *   Prepositional arguments required by the verb: Use `obl:arg`.
    *   **Contrast**: If the oblique is an optional adjunct (manner, time, instrument), use generic `obl` (or `obl:lmod`).

### [obl](https://universaldependencies.org/u/dep/obl.html) (Adjuncts & Modifiers)
The `obl` relation is used for oblique nominals that are NOT core arguments.

*   **obl:lmod** (Location Modifier): **Latin specific**. Used for any oblique indicating **location** or **direction** (spatial).
    *   *ad Troiam* -> `obl:lmod`
    *   *in recessu* -> `obl:lmod`
*   **obl:tmod** (Temporal Modifier): Used for temporal expressions.
*   **obl:agent** (Passive Agent): Used for the agent in a passive construction (usually *a/ab* + Ablative).
*   **obl**: Generic oblique for manner, instrument, cause, etc.

---

## 3. AUXILIARIES & COPULA

### [cop](https://universaldependencies.org/u/dep/cop.html) vs [aux](https://universaldependencies.org/u/dep/aux.html)
*   **cop**: Used for the copula *sum* (to be) in non-verbal predicates.
*   **aux**: Used for TAME markers.
*   **aux:pass**: Used for the auxiliary *sum* in periphrastic passive constructions (*amatus est*).

---

## 4. CLAUSAL STRUCTURES

### [advcl](https://universaldependencies.org/u/dep/advcl.html)
An adverbial clause modifier.
*   **advcl:abs** (Ablative Absolute): Latin specifically marks Ablative Absolutes with this subtype. The head is the participle.
*   **advcl:pred** (Predicative / Secondary Predication): Latin uses this for participles or adjectives that agree with a nominal but describe a state simultaneous with the main action (e.g., *Sedens digerit* "Sitting, he arranges").

### [acl](https://universaldependencies.org/u/dep/acl.html) vs [amod](https://universaldependencies.org/u/dep/amod.html)
*   **amod**: Simple adjectives or participles functioning purely as attributes (*nigrantes comae*).
*   **acl**: Participles with strong verbal force, arguments, or dependents. **Latin prefers `acl`** in ambiguous cases characteristic of poetic language.

---

## 5. COORDINATION & ELLIPSIS

### [conj](https://universaldependencies.org/u/dep/conj.html)
Connects conjuncts. The first element is the head.

### [orphan](https://universaldependencies.org/u/dep/orphan.html)
Used in cases of **Head Ellipsis (Gapping)**.
*   **Scenario**: The main predicate is elided in a coordinated clause.
*   **Resolution**: One core argument (Subject > Object) is promoted to head the gapped clause.
*   **Relation**: The promoted head attaches to the antecedent clause head via `conj`.
*   **Orphans**: All other dependents of the elided predicate attach to the promoted head via `orphan`.
*   **Example**: *Aditur illo Gnosius Minos foro, Rhadamanthus illo [aditur]...*
    *   *Rhadamanthus* (promoted Subject) -> `conj` -> *aditur*
    *   *illo* -> `orphan` -> *Rhadamanthus*

---

## 6. NOMINAL MODIFIERS

### [nmod](https://universaldependencies.org/u/dep/nmod.html)
Nominal modifier (Genitive).

### [appos](https://universaldependencies.org/u/dep/appos.html)
Apposition (renaming the noun).

### [case](https://universaldependencies.org/u/dep/case.html)
Prepositions attach to their Noun head.

---

## 7. LATIN-SPECIFIC SUBTYPE SUMMARY (GLOSSARY)

| Relation | Description |
| :--- | :--- |
| `nsubj:pass` | Subject of a passive verb |
| `aux:pass` | Auxiliary for passive periphrastic |
| `advcl:abs` | Ablative Absolute construction |
| `advcl:pred` | Secondary predication |
| `obl:arg` | Selected oblique argument (valency-bound) |
| `obl:lmod` | Locative modifier (spatial) |
| `obl:tmod` | Temporal modifier |
| `obl:agent` | Passive agent |
| `conj:expl` | Explicative coordination |

---

## 8. STRUCTURAL ATTACHMENT PRINCIPLES

1. **Dependency vs. Coordination**: In coordination, all items should ideally attach to the first element (`conj`).
2. **Verb Clusters**: Auxiliaries and Copulas (`aux`, `cop`) always depend on the lexical predicate.
3. **Prepositional Phrases**: The preposition (`case`) depends on the noun. The noun depends on the predicate.
