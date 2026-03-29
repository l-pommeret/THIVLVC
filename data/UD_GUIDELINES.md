# OFFICIAL LATIN UD GUIDELINES (Comprehensive v2)

This document provides definitive Universal Dependencies (UD) annotation guidelines for Latin, harmonized across major treebanks (ITTB, Perseus, PROIEL, UDante, CIRCSE).

---

## 1. TOKENIZATION & WORD SEGMENTATION

### Enclitics (-que, -ve, -ne)
*   **Rule**: Enclitics must be split into separate tokens.
*   **Example**: `arma virumque` -> `arma`, `virum`, `que`.
*   **Attachment**: The enclitic (usually `CCONJ`) attaches to the word it is appended to using the `cc` relation (or `cc:preconj`).

---

## 2. CORE ARGUMENTS & NOMINALS

### [nsubj](https://universaldependencies.org/u/dep/nsubj.html) / [nsubj:pass](https://universaldependencies.org/u/dep/nsubj-pass.html)

#### **nsubj**
A nominal subject (nsubj) is a nominal which is the syntactic subject and the proto-agent of a clause.
That is, it is in the position that passes typical grammatical test for subjecthood, and this argument is the more agentive,
the do-er, or the proto-agent of the clause. This nominal may be headed by a noun, 
or it may be a pronoun or relative pronoun or, in ellipsis contexts, other things such as an adjective.

New from v2: The nsubj relation is also used for the nominal subject of a passive verb or verb group, even
though the subject is then not typically the proto-agent argument due to valency changing operations. For languages
that have a grammaticalized passive transformation, it is strongly recommended to use the subtype nsubj:pass in 
such cases. If the subject is of a copular clause whose predicate is itself a clause, nsubj:outer may be used.

The governor of the nsubj relation might not always be a verb: when
the verb is a copular verb, the root of the clause is the complement
of the copular verb, which can be an adjective or noun, including a noun marked by a preposition,
as in the examples below.

The nsubj role is only applied to semantic arguments of a predicate.
When there is an empty argument in a grammatical subject position (sometimes called a pleonastic or expletive),
it is labeled as expl. If there is then a displaced subject
in the clause, as in the English existential there construction, it will be labeled as nsubj.)

(Source: https://universaldependencies.org/u/dep/nsubj.html)

#### **nsubj:pass**
A passive nominal subject is a noun phrase which is the syntactic
subject of a passive clause.

Reflexive passive (the meaning is “This will be solved tomorrow.”)

(Source: https://universaldependencies.org/u/dep/nsubj-pass.html)

#### **nsubj**
A nominal subject (nsubj) is a nominal which is the syntactic subject and the proto-agent of a clause.
That is, it is in the position that passes typical grammatical test for subjecthood, and this argument is the more agentive,
the do-er, or the proto-agent of the clause. This nominal may be headed by a noun, 
or it may be a pronoun or relative pronoun or, in ellipsis contexts, other things such as an adjective.

New from v2: The nsubj relation is also used for the nominal subject of a passive verb or verb group, even
though the subject is then not typically the proto-agent argument due to valency changing operations. For languages
that have a grammaticalized passive transformation, it is strongly recommended to use the subtype nsubj:pass in 
such cases. If the subject is of a copular clause whose predicate is itself a clause, nsubj:outer may be used.

The governor of the nsubj relation might not always be a verb: when
the verb is a copular verb, the root of the clause is the complement
of the copular verb, which can be an adjective or noun, including a noun marked by a preposition,
as in the examples below.

The nsubj role is only applied to semantic arguments of a predicate.
When there is an empty argument in a grammatical subject position (sometimes called a pleonastic or expletive),
it is labeled as expl. If there is then a displaced subject
in the clause, as in the English existential there construction, it will be labeled as nsubj.)

(Source: https://universaldependencies.org/u/dep/nsubj.html)

#### **nsubj:pass**
A passive nominal subject is a noun phrase which is the syntactic
subject of a passive clause.

Reflexive passive (the meaning is “This will be solved tomorrow.”)

(Source: https://universaldependencies.org/u/dep/nsubj-pass.html)

#### **nsubj**
A nominal subject (nsubj) is a nominal which is the syntactic subject and the proto-agent of a clause.
That is, it is in the position that passes typical grammatical test for subjecthood, and this argument is the more agentive,
the do-er, or the proto-agent of the clause. This nominal may be headed by a noun, 
or it may be a pronoun or relative pronoun or, in ellipsis contexts, other things such as an adjective.

New from v2: The nsubj relation is also used for the nominal subject of a passive verb or verb group, even
though the subject is then not typically the proto-agent argument due to valency changing operations. For languages
that have a grammaticalized passive transformation, it is strongly recommended to use the subtype nsubj:pass in 
such cases. If the subject is of a copular clause whose predicate is itself a clause, nsubj:outer may be used.

The governor of the nsubj relation might not always be a verb: when
the verb is a copular verb, the root of the clause is the complement
of the copular verb, which can be an adjective or noun, including a noun marked by a preposition,
as in the examples below.

The nsubj role is only applied to semantic arguments of a predicate.
When there is an empty argument in a grammatical subject position (sometimes called a pleonastic or expletive),
it is labeled as expl. If there is then a displaced subject
in the clause, as in the English existential there construction, it will be labeled as nsubj.)

(Source: https://universaldependencies.org/u/dep/nsubj.html)

#### **nsubj:pass**
A passive nominal subject is a noun phrase which is the syntactic
subject of a passive clause.

Reflexive passive (the meaning is “This will be solved tomorrow.”)

(Source: https://universaldependencies.org/u/dep/nsubj-pass.html)

#### **nsubj**
A nominal subject (nsubj) is a nominal which is the syntactic subject and the proto-agent of a clause.
That is, it is in the position that passes typical grammatical test for subjecthood, and this argument is the more agentive,
the do-er, or the proto-agent of the clause. This nominal may be headed by a noun, 
or it may be a pronoun or relative pronoun or, in ellipsis contexts, other things such as an adjective.

New from v2: The nsubj relation is also used for the nominal subject of a passive verb or verb group, even
though the subject is then not typically the proto-agent argument due to valency changing operations. For languages
that have a grammaticalized passive transformation, it is strongly recommended to use the subtype nsubj:pass in 
such cases. If the subject is of a copular clause whose predicate is itself a clause, nsubj:outer may be used.

The governor of the nsubj relation might not always be a verb: when
the verb is a copular verb, the root of the clause is the complement
of the copular verb, which can be an adjective or noun, including a noun marked by a preposition,
as in the examples below.

The nsubj role is only applied to semantic arguments of a predicate.
When there is an empty argument in a grammatical subject position (sometimes called a pleonastic or expletive),
it is labeled as expl. If there is then a displaced subject
in the clause, as in the English existential there construction, it will be labeled as nsubj.)

(Source: https://universaldependencies.org/u/dep/nsubj.html)

### [obj](https://universaldependencies.org/u/dep/obj.html) vs [obl:arg](https://universaldependencies.org/u/dep/obl-arg.html)

#### **obj**
The object of a verb is the second most core argument of a verb after the subject.
Typically, it is the noun phrase that denotes the entity acted upon or which undergoes a change of state or motion (the proto-patient).

In languages distinguishing morphological cases, the
object will often be marked by the accusative case. If a verb dictates
another case (dative, genitive…), the fundamental question is whether
such cases qualify as core in the given language. Often these cases
are oblique, regardless of the presence or absence of an adposition.
Consequently they cannot use the obj relation and must use obl,
even if the traditional grammar calls such dependents “objects”.

If there are two or more objects, one of them should be obj and the
others should be iobj. In such cases it is necessary to decide what
is the most directly affected object (patient).
If there is just one object, it should likely be obj 
unless it is morphosyntactically more similar to clear cases 
of iobj in the language than it is to prototypical patient arguments.

There is further discussion of the two kinds of object at iobj.
If possible, language-specific documentation should be available to help identify the primary (or direct) object.

(Source: https://universaldependencies.org/u/dep/obj.html)

#### **obl:arg**
The relation obl:arg is used for oblique arguments and distinguishes them from
adjuncts, which use the plain obl relation. It is thus possible to preserve
the notion of object as it is defined in the traditional grammar of some
languages, where it essentially follows the distinction between arguments and
adjuncts (which is otherwise not reflected in the main UD relation types — see the
discussion here).
A Czech example:

Arguments are selected by the predicate. Their coding (preposition and
morphological case) is determined by the predicate; within the set of
arguments of this predicate, the coding maps the argument to a particular
semantic role.
In contrast, the semantics of an adjunct is relatively independent of the
predicate, and typical adjuncts (such as specifications of time, location,
manner or instrument) can combine with a large number of different predicates.

Hence in the above example, the preposition na “on” and the accusative case of
the noun instinkt “instinct” are selected by the verb spoléhat “to rely”.
Other verbs may also select the same preposition and case but the meaning will
be different: for instance, myslet na někoho “to think of someone.”
Finally, the preposition na itself has an adessive or allative meaning
(see the corresponding values of the Case feature).
This meaning is suppressed when the preposition is selected by a predicate but
it is more recognizable in adjuncts. In the following example, the preposition
combines with a noun phrase in the locative case and marks a locational modifier:

(Source: https://universaldependencies.org/u/dep/obl-arg.html)

#### **obj**
The object of a verb is the second most core argument of a verb after the subject.
Typically, it is the noun phrase that denotes the entity acted upon or which undergoes a change of state or motion (the proto-patient).

In languages distinguishing morphological cases, the
object will often be marked by the accusative case. If a verb dictates
another case (dative, genitive…), the fundamental question is whether
such cases qualify as core in the given language. Often these cases
are oblique, regardless of the presence or absence of an adposition.
Consequently they cannot use the obj relation and must use obl,
even if the traditional grammar calls such dependents “objects”.

If there are two or more objects, one of them should be obj and the
others should be iobj. In such cases it is necessary to decide what
is the most directly affected object (patient).
If there is just one object, it should likely be obj 
unless it is morphosyntactically more similar to clear cases 
of iobj in the language than it is to prototypical patient arguments.

There is further discussion of the two kinds of object at iobj.
If possible, language-specific documentation should be available to help identify the primary (or direct) object.

(Source: https://universaldependencies.org/u/dep/obj.html)

#### **obl:arg**
The relation obl:arg is used for oblique arguments and distinguishes them from
adjuncts, which use the plain obl relation. It is thus possible to preserve
the notion of object as it is defined in the traditional grammar of some
languages, where it essentially follows the distinction between arguments and
adjuncts (which is otherwise not reflected in the main UD relation types — see the
discussion here).
A Czech example:

Arguments are selected by the predicate. Their coding (preposition and
morphological case) is determined by the predicate; within the set of
arguments of this predicate, the coding maps the argument to a particular
semantic role.
In contrast, the semantics of an adjunct is relatively independent of the
predicate, and typical adjuncts (such as specifications of time, location,
manner or instrument) can combine with a large number of different predicates.

Hence in the above example, the preposition na “on” and the accusative case of
the noun instinkt “instinct” are selected by the verb spoléhat “to rely”.
Other verbs may also select the same preposition and case but the meaning will
be different: for instance, myslet na někoho “to think of someone.”
Finally, the preposition na itself has an adessive or allative meaning
(see the corresponding values of the Case feature).
This meaning is suppressed when the preposition is selected by a predicate but
it is more recognizable in adjuncts. In the following example, the preposition
combines with a noun phrase in the locative case and marks a locational modifier:

(Source: https://universaldependencies.org/u/dep/obl-arg.html)

#### **obj**
The object of a verb is the second most core argument of a verb after the subject.
Typically, it is the noun phrase that denotes the entity acted upon or which undergoes a change of state or motion (the proto-patient).

In languages distinguishing morphological cases, the
object will often be marked by the accusative case. If a verb dictates
another case (dative, genitive…), the fundamental question is whether
such cases qualify as core in the given language. Often these cases
are oblique, regardless of the presence or absence of an adposition.
Consequently they cannot use the obj relation and must use obl,
even if the traditional grammar calls such dependents “objects”.

If there are two or more objects, one of them should be obj and the
others should be iobj. In such cases it is necessary to decide what
is the most directly affected object (patient).
If there is just one object, it should likely be obj 
unless it is morphosyntactically more similar to clear cases 
of iobj in the language than it is to prototypical patient arguments.

There is further discussion of the two kinds of object at iobj.
If possible, language-specific documentation should be available to help identify the primary (or direct) object.

(Source: https://universaldependencies.org/u/dep/obj.html)

#### **obl:arg**
The relation obl:arg is used for oblique arguments and distinguishes them from
adjuncts, which use the plain obl relation. It is thus possible to preserve
the notion of object as it is defined in the traditional grammar of some
languages, where it essentially follows the distinction between arguments and
adjuncts (which is otherwise not reflected in the main UD relation types — see the
discussion here).
A Czech example:

Arguments are selected by the predicate. Their coding (preposition and
morphological case) is determined by the predicate; within the set of
arguments of this predicate, the coding maps the argument to a particular
semantic role.
In contrast, the semantics of an adjunct is relatively independent of the
predicate, and typical adjuncts (such as specifications of time, location,
manner or instrument) can combine with a large number of different predicates.

Hence in the above example, the preposition na “on” and the accusative case of
the noun instinkt “instinct” are selected by the verb spoléhat “to rely”.
Other verbs may also select the same preposition and case but the meaning will
be different: for instance, myslet na někoho “to think of someone.”
Finally, the preposition na itself has an adessive or allative meaning
(see the corresponding values of the Case feature).
This meaning is suppressed when the preposition is selected by a predicate but
it is more recognizable in adjuncts. In the following example, the preposition
combines with a noun phrase in the locative case and marks a locational modifier:

(Source: https://universaldependencies.org/u/dep/obl-arg.html)

#### **obj**
The object of a verb is the second most core argument of a verb after the subject.
Typically, it is the noun phrase that denotes the entity acted upon or which undergoes a change of state or motion (the proto-patient).

In languages distinguishing morphological cases, the
object will often be marked by the accusative case. If a verb dictates
another case (dative, genitive…), the fundamental question is whether
such cases qualify as core in the given language. Often these cases
are oblique, regardless of the presence or absence of an adposition.
Consequently they cannot use the obj relation and must use obl,
even if the traditional grammar calls such dependents “objects”.

If there are two or more objects, one of them should be obj and the
others should be iobj. In such cases it is necessary to decide what
is the most directly affected object (patient).
If there is just one object, it should likely be obj 
unless it is morphosyntactically more similar to clear cases 
of iobj in the language than it is to prototypical patient arguments.

There is further discussion of the two kinds of object at iobj.
If possible, language-specific documentation should be available to help identify the primary (or direct) object.

(Source: https://universaldependencies.org/u/dep/obj.html)

### [iobj](https://universaldependencies.org/u/dep/iobj.html)

#### **iobj**
In UD, the indirect object of a verb is any nominal phrase that is a core
argument of the verb but is not its subject or (direct) object.
The prototypical example is the recipient of ditransitive verbs of
exchange:

However, many languages allow other semantic roles as additional objects. The most common case is allowing benefactives, but some languages allow other roles. Examples include instruments, such as in the Kinyarwanda example below, or comitatives. At the other extreme, some languages lack all indirect objects.

In languages distinguishing morphological cases, the recipient will often be marked by the dative case.
However, the iobj relation can be used only for a core argument. The morphological dative may signal a core argument
in some languages (such as Basque) but in many others it is just oblique (like the English preposition to). For
instance, in many Indo-European languages, the recipient should be attached as obl and not iobj, regardless
of the traditional grammar which may label it as “indirect object”.

In the following Czech example, the verb takes two objects. Both are nouns in the accusative case, which is rather
unusual—for most other verbs, one of the arguments would be in the dative and would thus be treated as oblique in UD.
However, a bare accusative signals a core object and a verb with one nominative and two accusatives is ditransitive
in UD. One of the accusatives is direct object (patient), the other is indirect (recipient). It is parallel to how
the English translation would be annotated (where there is no morphological case marking) and also to verbs of giving
in English (consider a similar sentence, he gave my daughter a class of maths).

Predicates in Basque can cross-reference (by morphological agreement on the auxiliary verb) up to three arguments
in different morphological cases: ergative, absolutive, and dative. The morphological cross-reference is a strong
indicator that all three are core arguments. Therefore, if all three are present, we have a double-object situation
and the dative argument will be iobj (while the ergative argument will be nsubj and the absolutive obj).
Even if the absolutive argument is omitted for a verb which licenses three arguments, the dative argument is still
iobj.

Nevertheless, Basque has also a class of verbs that license only two core arguments, one ergative and
one dative. Here the ergative has the A function and the dative the P function (Zúñiga and Fernández 2014),
meaning that the dative is obj rather than iobj, as in “The teacher has looked angrily at the students.”

Another class of transitive verbs in Basque license one dative and one absolutive argument. Here the
dative has the A function and the absolutive the P function, meaning that the dative is nsubj and
the absolutive is obj, as in “The boy likes the soup very much.”

In Tagalog, core arguments are marked by the prepositions ang and ng (or by corresponding inflection
of personal pronouns), while oblique dependents are typically marked by the preposition sa (sometimes
glossed as the dative). Giving somebody something is a (mono)transitive predicate.

However, locative dependents can be topicalized if the verb morphology signals
the “locative voice”. Then the locative noun phrase switches to nominative,
it becomes a core argument, while the original two core arguments keep core
coding, too. Therefore we have a ditransitive clause with three core arguments,
even for verbs that are not associated with ditransitives in other languages:

In Plains Cree (Wolvengrey 2011), transitive verbs cross-reference subjects and animate objects but not
inanimate objects. With a verb of giving, the theme is typically inanimate while the recipient is
typically animate. Assuming that nsubj and obj are reserved for the two core arguments
cross-referenced by the verb, the theme has to be iobj (if it is a core argument at all; otherwise
it would have to be obl; but real oblique nominals in Plains Cree take a locative case affix,
which is not present here).

In the above example, the verb stem used is for animate objects, while
masinahikan “book” is inanimate. That is a proof that the 3rd person singular
cross-reference on the verb does not refer to the book but to an animate
recipient that is not overtly represented in the sentence.

If the language has a prototypical iobj (occurring in a double object construction with obj),
then morphosyntactic criteria need to be established for when a sole object is obj and when it is iobj.1
Depending on the language, potential reasons to consider a sole object in a clause as an iobj include:

For example, in English, the verb teach may occur with obj, iobj, or both:

However, not all verbs license two objects (or an object plus ccomp), in which case the sole object should be plain obj even if it has recipient-like semantics:

(Source: https://universaldependencies.org/u/dep/iobj.html)

#### **iobj**
In UD, the indirect object of a verb is any nominal phrase that is a core
argument of the verb but is not its subject or (direct) object.
The prototypical example is the recipient of ditransitive verbs of
exchange:

However, many languages allow other semantic roles as additional objects. The most common case is allowing benefactives, but some languages allow other roles. Examples include instruments, such as in the Kinyarwanda example below, or comitatives. At the other extreme, some languages lack all indirect objects.

In languages distinguishing morphological cases, the recipient will often be marked by the dative case.
However, the iobj relation can be used only for a core argument. The morphological dative may signal a core argument
in some languages (such as Basque) but in many others it is just oblique (like the English preposition to). For
instance, in many Indo-European languages, the recipient should be attached as obl and not iobj, regardless
of the traditional grammar which may label it as “indirect object”.

In the following Czech example, the verb takes two objects. Both are nouns in the accusative case, which is rather
unusual—for most other verbs, one of the arguments would be in the dative and would thus be treated as oblique in UD.
However, a bare accusative signals a core object and a verb with one nominative and two accusatives is ditransitive
in UD. One of the accusatives is direct object (patient), the other is indirect (recipient). It is parallel to how
the English translation would be annotated (where there is no morphological case marking) and also to verbs of giving
in English (consider a similar sentence, he gave my daughter a class of maths).

Predicates in Basque can cross-reference (by morphological agreement on the auxiliary verb) up to three arguments
in different morphological cases: ergative, absolutive, and dative. The morphological cross-reference is a strong
indicator that all three are core arguments. Therefore, if all three are present, we have a double-object situation
and the dative argument will be iobj (while the ergative argument will be nsubj and the absolutive obj).
Even if the absolutive argument is omitted for a verb which licenses three arguments, the dative argument is still
iobj.

Nevertheless, Basque has also a class of verbs that license only two core arguments, one ergative and
one dative. Here the ergative has the A function and the dative the P function (Zúñiga and Fernández 2014),
meaning that the dative is obj rather than iobj, as in “The teacher has looked angrily at the students.”

Another class of transitive verbs in Basque license one dative and one absolutive argument. Here the
dative has the A function and the absolutive the P function, meaning that the dative is nsubj and
the absolutive is obj, as in “The boy likes the soup very much.”

In Tagalog, core arguments are marked by the prepositions ang and ng (or by corresponding inflection
of personal pronouns), while oblique dependents are typically marked by the preposition sa (sometimes
glossed as the dative). Giving somebody something is a (mono)transitive predicate.

However, locative dependents can be topicalized if the verb morphology signals
the “locative voice”. Then the locative noun phrase switches to nominative,
it becomes a core argument, while the original two core arguments keep core
coding, too. Therefore we have a ditransitive clause with three core arguments,
even for verbs that are not associated with ditransitives in other languages:

In Plains Cree (Wolvengrey 2011), transitive verbs cross-reference subjects and animate objects but not
inanimate objects. With a verb of giving, the theme is typically inanimate while the recipient is
typically animate. Assuming that nsubj and obj are reserved for the two core arguments
cross-referenced by the verb, the theme has to be iobj (if it is a core argument at all; otherwise
it would have to be obl; but real oblique nominals in Plains Cree take a locative case affix,
which is not present here).

In the above example, the verb stem used is for animate objects, while
masinahikan “book” is inanimate. That is a proof that the 3rd person singular
cross-reference on the verb does not refer to the book but to an animate
recipient that is not overtly represented in the sentence.

If the language has a prototypical iobj (occurring in a double object construction with obj),
then morphosyntactic criteria need to be established for when a sole object is obj and when it is iobj.1
Depending on the language, potential reasons to consider a sole object in a clause as an iobj include:

For example, in English, the verb teach may occur with obj, iobj, or both:

However, not all verbs license two objects (or an object plus ccomp), in which case the sole object should be plain obj even if it has recipient-like semantics:

(Source: https://universaldependencies.org/u/dep/iobj.html)

#### **iobj**
In UD, the indirect object of a verb is any nominal phrase that is a core
argument of the verb but is not its subject or (direct) object.
The prototypical example is the recipient of ditransitive verbs of
exchange:

However, many languages allow other semantic roles as additional objects. The most common case is allowing benefactives, but some languages allow other roles. Examples include instruments, such as in the Kinyarwanda example below, or comitatives. At the other extreme, some languages lack all indirect objects.

In languages distinguishing morphological cases, the recipient will often be marked by the dative case.
However, the iobj relation can be used only for a core argument. The morphological dative may signal a core argument
in some languages (such as Basque) but in many others it is just oblique (like the English preposition to). For
instance, in many Indo-European languages, the recipient should be attached as obl and not iobj, regardless
of the traditional grammar which may label it as “indirect object”.

In the following Czech example, the verb takes two objects. Both are nouns in the accusative case, which is rather
unusual—for most other verbs, one of the arguments would be in the dative and would thus be treated as oblique in UD.
However, a bare accusative signals a core object and a verb with one nominative and two accusatives is ditransitive
in UD. One of the accusatives is direct object (patient), the other is indirect (recipient). It is parallel to how
the English translation would be annotated (where there is no morphological case marking) and also to verbs of giving
in English (consider a similar sentence, he gave my daughter a class of maths).

Predicates in Basque can cross-reference (by morphological agreement on the auxiliary verb) up to three arguments
in different morphological cases: ergative, absolutive, and dative. The morphological cross-reference is a strong
indicator that all three are core arguments. Therefore, if all three are present, we have a double-object situation
and the dative argument will be iobj (while the ergative argument will be nsubj and the absolutive obj).
Even if the absolutive argument is omitted for a verb which licenses three arguments, the dative argument is still
iobj.

Nevertheless, Basque has also a class of verbs that license only two core arguments, one ergative and
one dative. Here the ergative has the A function and the dative the P function (Zúñiga and Fernández 2014),
meaning that the dative is obj rather than iobj, as in “The teacher has looked angrily at the students.”

Another class of transitive verbs in Basque license one dative and one absolutive argument. Here the
dative has the A function and the absolutive the P function, meaning that the dative is nsubj and
the absolutive is obj, as in “The boy likes the soup very much.”

In Tagalog, core arguments are marked by the prepositions ang and ng (or by corresponding inflection
of personal pronouns), while oblique dependents are typically marked by the preposition sa (sometimes
glossed as the dative). Giving somebody something is a (mono)transitive predicate.

However, locative dependents can be topicalized if the verb morphology signals
the “locative voice”. Then the locative noun phrase switches to nominative,
it becomes a core argument, while the original two core arguments keep core
coding, too. Therefore we have a ditransitive clause with three core arguments,
even for verbs that are not associated with ditransitives in other languages:

In Plains Cree (Wolvengrey 2011), transitive verbs cross-reference subjects and animate objects but not
inanimate objects. With a verb of giving, the theme is typically inanimate while the recipient is
typically animate. Assuming that nsubj and obj are reserved for the two core arguments
cross-referenced by the verb, the theme has to be iobj (if it is a core argument at all; otherwise
it would have to be obl; but real oblique nominals in Plains Cree take a locative case affix,
which is not present here).

In the above example, the verb stem used is for animate objects, while
masinahikan “book” is inanimate. That is a proof that the 3rd person singular
cross-reference on the verb does not refer to the book but to an animate
recipient that is not overtly represented in the sentence.

If the language has a prototypical iobj (occurring in a double object construction with obj),
then morphosyntactic criteria need to be established for when a sole object is obj and when it is iobj.1
Depending on the language, potential reasons to consider a sole object in a clause as an iobj include:

For example, in English, the verb teach may occur with obj, iobj, or both:

However, not all verbs license two objects (or an object plus ccomp), in which case the sole object should be plain obj even if it has recipient-like semantics:

(Source: https://universaldependencies.org/u/dep/iobj.html)

#### **iobj**
In UD, the indirect object of a verb is any nominal phrase that is a core
argument of the verb but is not its subject or (direct) object.
The prototypical example is the recipient of ditransitive verbs of
exchange:

However, many languages allow other semantic roles as additional objects. The most common case is allowing benefactives, but some languages allow other roles. Examples include instruments, such as in the Kinyarwanda example below, or comitatives. At the other extreme, some languages lack all indirect objects.

In languages distinguishing morphological cases, the recipient will often be marked by the dative case.
However, the iobj relation can be used only for a core argument. The morphological dative may signal a core argument
in some languages (such as Basque) but in many others it is just oblique (like the English preposition to). For
instance, in many Indo-European languages, the recipient should be attached as obl and not iobj, regardless
of the traditional grammar which may label it as “indirect object”.

In the following Czech example, the verb takes two objects. Both are nouns in the accusative case, which is rather
unusual—for most other verbs, one of the arguments would be in the dative and would thus be treated as oblique in UD.
However, a bare accusative signals a core object and a verb with one nominative and two accusatives is ditransitive
in UD. One of the accusatives is direct object (patient), the other is indirect (recipient). It is parallel to how
the English translation would be annotated (where there is no morphological case marking) and also to verbs of giving
in English (consider a similar sentence, he gave my daughter a class of maths).

Predicates in Basque can cross-reference (by morphological agreement on the auxiliary verb) up to three arguments
in different morphological cases: ergative, absolutive, and dative. The morphological cross-reference is a strong
indicator that all three are core arguments. Therefore, if all three are present, we have a double-object situation
and the dative argument will be iobj (while the ergative argument will be nsubj and the absolutive obj).
Even if the absolutive argument is omitted for a verb which licenses three arguments, the dative argument is still
iobj.

Nevertheless, Basque has also a class of verbs that license only two core arguments, one ergative and
one dative. Here the ergative has the A function and the dative the P function (Zúñiga and Fernández 2014),
meaning that the dative is obj rather than iobj, as in “The teacher has looked angrily at the students.”

Another class of transitive verbs in Basque license one dative and one absolutive argument. Here the
dative has the A function and the absolutive the P function, meaning that the dative is nsubj and
the absolutive is obj, as in “The boy likes the soup very much.”

In Tagalog, core arguments are marked by the prepositions ang and ng (or by corresponding inflection
of personal pronouns), while oblique dependents are typically marked by the preposition sa (sometimes
glossed as the dative). Giving somebody something is a (mono)transitive predicate.

However, locative dependents can be topicalized if the verb morphology signals
the “locative voice”. Then the locative noun phrase switches to nominative,
it becomes a core argument, while the original two core arguments keep core
coding, too. Therefore we have a ditransitive clause with three core arguments,
even for verbs that are not associated with ditransitives in other languages:

In Plains Cree (Wolvengrey 2011), transitive verbs cross-reference subjects and animate objects but not
inanimate objects. With a verb of giving, the theme is typically inanimate while the recipient is
typically animate. Assuming that nsubj and obj are reserved for the two core arguments
cross-referenced by the verb, the theme has to be iobj (if it is a core argument at all; otherwise
it would have to be obl; but real oblique nominals in Plains Cree take a locative case affix,
which is not present here).

In the above example, the verb stem used is for animate objects, while
masinahikan “book” is inanimate. That is a proof that the 3rd person singular
cross-reference on the verb does not refer to the book but to an animate
recipient that is not overtly represented in the sentence.

If the language has a prototypical iobj (occurring in a double object construction with obj),
then morphosyntactic criteria need to be established for when a sole object is obj and when it is iobj.1
Depending on the language, potential reasons to consider a sole object in a clause as an iobj include:

For example, in English, the verb teach may occur with obj, iobj, or both:

However, not all verbs license two objects (or an object plus ccomp), in which case the sole object should be plain obj even if it has recipient-like semantics:

(Source: https://universaldependencies.org/u/dep/iobj.html)

---

## 3. AUXILIARIES & COPULA

### [cop](https://universaldependencies.org/u/dep/cop.html) vs [aux](https://universaldependencies.org/u/dep/aux.html)

#### **cop**
A cop (copula) is the relation of a function word used to link a subject to a nonverbal predicate, including the expression of identity predication (e.g. sentences like “Kim is the President”).
It is often a verb but nonverbal (pronominal) copulas are also frequent in the world’s languages.
Verbal copulas are tagged AUX, not VERB. Pronominal copulas are tagged PRON or DET.

The cop relation
should only be used for pure copulas that add at most TAME categories to the meaning of the predicate,
which means that most languages have at most one copula, and only when the nonverbal predicate is treated
as the head of the clause.

As a concrete example, in many European languages the equivalent of the English verb to be is the only word that can appear with the cop relation. In Spanish and related languages, both ser and estar can be copulas. In Czech and related languages, both být and bývat are copulas (because they are morphological variants of the same lexeme, and the reason they have two lemmas is that aspect-related morphology is treated as derivational in these languages). In contrast, the equivalents of to become are not copulas despite the fact that traditional grammar may label them as such. Existential to be can be copula only if it is the same verb as in equivalence clauses (John is a teacher). If a language uses two different verbs, then the existential one is not a copula. Some more discussion of the topic is archived here.

The copula be is not treated as the head of a clause, but rather the nonverbal predicate, as exemplified above.

Such an analysis is motivated by the fact that many languages often or always lack an overt copula in such
constructions, as in the the following Russian and Hebrew examples:

In informal English, this may also arise.

This analysis is adopted also when the predicate is a prepositional phrase, provided that the same copula
(or absence thereof) is used here, in which case the nominal part of the
prepositional phrase is the head of the clause.

If the copula is accompanied by other verbal auxiliaries for tense, aspect, etc., then they are also given a flat structure, and taken as dependents of the lexical predicate:

The motivation for this choice is that this structure is parallel to the flat structure which we give to auxiliary verbs accompanying verbs. In particular, in languages such as English, it is often very difficult to decide whether to regard a participle as a verb or an adjective.  Perhaps the following sentence is such a case:

While a part of speech (and associated deprel: cop vs. aux) has to be decided in such cases, it would be unfortunate if the choice of part of speech also changed the dependency structure. Note, however, that the exact distribution of the copula construction is subject to language-specific variation.

Finally, the cop may mark a predicate clause, i.e., a full clause serving as the predicate within an outer copular clause. 
In such cases, nsubj:outer or csubj:outer can be used to distinguish the outer subject:

(Source: https://universaldependencies.org/u/dep/cop.html)

#### **aux**
An aux (auxiliary) of a clause is a function word associated with a verbal predicate that expresses categories such as tense, mood, aspect, voice or evidentiality. It is often a verb (which may have non-auxiliary uses as well) but many languages have nonverbal TAME markers and these are also treated as instances of aux.

New from v2: Auxiliaries used to construct the passive voice are now also labeled aux, although we strongly encourage the use of the subtype aux:pass in languages that have a grammaticalized (periphrastic) passive.

(Source: https://universaldependencies.org/u/dep/aux_.html)

#### **cop**
A cop (copula) is the relation of a function word used to link a subject to a nonverbal predicate, including the expression of identity predication (e.g. sentences like “Kim is the President”).
It is often a verb but nonverbal (pronominal) copulas are also frequent in the world’s languages.
Verbal copulas are tagged AUX, not VERB. Pronominal copulas are tagged PRON or DET.

The cop relation
should only be used for pure copulas that add at most TAME categories to the meaning of the predicate,
which means that most languages have at most one copula, and only when the nonverbal predicate is treated
as the head of the clause.

As a concrete example, in many European languages the equivalent of the English verb to be is the only word that can appear with the cop relation. In Spanish and related languages, both ser and estar can be copulas. In Czech and related languages, both být and bývat are copulas (because they are morphological variants of the same lexeme, and the reason they have two lemmas is that aspect-related morphology is treated as derivational in these languages). In contrast, the equivalents of to become are not copulas despite the fact that traditional grammar may label them as such. Existential to be can be copula only if it is the same verb as in equivalence clauses (John is a teacher). If a language uses two different verbs, then the existential one is not a copula. Some more discussion of the topic is archived here.

The copula be is not treated as the head of a clause, but rather the nonverbal predicate, as exemplified above.

Such an analysis is motivated by the fact that many languages often or always lack an overt copula in such
constructions, as in the the following Russian and Hebrew examples:

In informal English, this may also arise.

This analysis is adopted also when the predicate is a prepositional phrase, provided that the same copula
(or absence thereof) is used here, in which case the nominal part of the
prepositional phrase is the head of the clause.

If the copula is accompanied by other verbal auxiliaries for tense, aspect, etc., then they are also given a flat structure, and taken as dependents of the lexical predicate:

The motivation for this choice is that this structure is parallel to the flat structure which we give to auxiliary verbs accompanying verbs. In particular, in languages such as English, it is often very difficult to decide whether to regard a participle as a verb or an adjective.  Perhaps the following sentence is such a case:

While a part of speech (and associated deprel: cop vs. aux) has to be decided in such cases, it would be unfortunate if the choice of part of speech also changed the dependency structure. Note, however, that the exact distribution of the copula construction is subject to language-specific variation.

Finally, the cop may mark a predicate clause, i.e., a full clause serving as the predicate within an outer copular clause. 
In such cases, nsubj:outer or csubj:outer can be used to distinguish the outer subject:

(Source: https://universaldependencies.org/u/dep/cop.html)

#### **aux**
An aux (auxiliary) of a clause is a function word associated with a verbal predicate that expresses categories such as tense, mood, aspect, voice or evidentiality. It is often a verb (which may have non-auxiliary uses as well) but many languages have nonverbal TAME markers and these are also treated as instances of aux.

New from v2: Auxiliaries used to construct the passive voice are now also labeled aux, although we strongly encourage the use of the subtype aux:pass in languages that have a grammaticalized (periphrastic) passive.

(Source: https://universaldependencies.org/u/dep/aux_.html)

#### **cop**
A cop (copula) is the relation of a function word used to link a subject to a nonverbal predicate, including the expression of identity predication (e.g. sentences like “Kim is the President”).
It is often a verb but nonverbal (pronominal) copulas are also frequent in the world’s languages.
Verbal copulas are tagged AUX, not VERB. Pronominal copulas are tagged PRON or DET.

The cop relation
should only be used for pure copulas that add at most TAME categories to the meaning of the predicate,
which means that most languages have at most one copula, and only when the nonverbal predicate is treated
as the head of the clause.

As a concrete example, in many European languages the equivalent of the English verb to be is the only word that can appear with the cop relation. In Spanish and related languages, both ser and estar can be copulas. In Czech and related languages, both být and bývat are copulas (because they are morphological variants of the same lexeme, and the reason they have two lemmas is that aspect-related morphology is treated as derivational in these languages). In contrast, the equivalents of to become are not copulas despite the fact that traditional grammar may label them as such. Existential to be can be copula only if it is the same verb as in equivalence clauses (John is a teacher). If a language uses two different verbs, then the existential one is not a copula. Some more discussion of the topic is archived here.

The copula be is not treated as the head of a clause, but rather the nonverbal predicate, as exemplified above.

Such an analysis is motivated by the fact that many languages often or always lack an overt copula in such
constructions, as in the the following Russian and Hebrew examples:

In informal English, this may also arise.

This analysis is adopted also when the predicate is a prepositional phrase, provided that the same copula
(or absence thereof) is used here, in which case the nominal part of the
prepositional phrase is the head of the clause.

If the copula is accompanied by other verbal auxiliaries for tense, aspect, etc., then they are also given a flat structure, and taken as dependents of the lexical predicate:

The motivation for this choice is that this structure is parallel to the flat structure which we give to auxiliary verbs accompanying verbs. In particular, in languages such as English, it is often very difficult to decide whether to regard a participle as a verb or an adjective.  Perhaps the following sentence is such a case:

While a part of speech (and associated deprel: cop vs. aux) has to be decided in such cases, it would be unfortunate if the choice of part of speech also changed the dependency structure. Note, however, that the exact distribution of the copula construction is subject to language-specific variation.

Finally, the cop may mark a predicate clause, i.e., a full clause serving as the predicate within an outer copular clause. 
In such cases, nsubj:outer or csubj:outer can be used to distinguish the outer subject:

(Source: https://universaldependencies.org/u/dep/cop.html)

#### **aux**
An aux (auxiliary) of a clause is a function word associated with a verbal predicate that expresses categories such as tense, mood, aspect, voice or evidentiality. It is often a verb (which may have non-auxiliary uses as well) but many languages have nonverbal TAME markers and these are also treated as instances of aux.

New from v2: Auxiliaries used to construct the passive voice are now also labeled aux, although we strongly encourage the use of the subtype aux:pass in languages that have a grammaticalized (periphrastic) passive.

(Source: https://universaldependencies.org/u/dep/aux_.html)

#### **cop**
A cop (copula) is the relation of a function word used to link a subject to a nonverbal predicate, including the expression of identity predication (e.g. sentences like “Kim is the President”).
It is often a verb but nonverbal (pronominal) copulas are also frequent in the world’s languages.
Verbal copulas are tagged AUX, not VERB. Pronominal copulas are tagged PRON or DET.

The cop relation
should only be used for pure copulas that add at most TAME categories to the meaning of the predicate,
which means that most languages have at most one copula, and only when the nonverbal predicate is treated
as the head of the clause.

As a concrete example, in many European languages the equivalent of the English verb to be is the only word that can appear with the cop relation. In Spanish and related languages, both ser and estar can be copulas. In Czech and related languages, both být and bývat are copulas (because they are morphological variants of the same lexeme, and the reason they have two lemmas is that aspect-related morphology is treated as derivational in these languages). In contrast, the equivalents of to become are not copulas despite the fact that traditional grammar may label them as such. Existential to be can be copula only if it is the same verb as in equivalence clauses (John is a teacher). If a language uses two different verbs, then the existential one is not a copula. Some more discussion of the topic is archived here.

The copula be is not treated as the head of a clause, but rather the nonverbal predicate, as exemplified above.

Such an analysis is motivated by the fact that many languages often or always lack an overt copula in such
constructions, as in the the following Russian and Hebrew examples:

In informal English, this may also arise.

This analysis is adopted also when the predicate is a prepositional phrase, provided that the same copula
(or absence thereof) is used here, in which case the nominal part of the
prepositional phrase is the head of the clause.

If the copula is accompanied by other verbal auxiliaries for tense, aspect, etc., then they are also given a flat structure, and taken as dependents of the lexical predicate:

The motivation for this choice is that this structure is parallel to the flat structure which we give to auxiliary verbs accompanying verbs. In particular, in languages such as English, it is often very difficult to decide whether to regard a participle as a verb or an adjective.  Perhaps the following sentence is such a case:

While a part of speech (and associated deprel: cop vs. aux) has to be decided in such cases, it would be unfortunate if the choice of part of speech also changed the dependency structure. Note, however, that the exact distribution of the copula construction is subject to language-specific variation.

Finally, the cop may mark a predicate clause, i.e., a full clause serving as the predicate within an outer copular clause. 
In such cases, nsubj:outer or csubj:outer can be used to distinguish the outer subject:

(Source: https://universaldependencies.org/u/dep/cop.html)

---

## 4. CLAUSAL STRUCTURES

### [advcl](https://universaldependencies.org/u/dep/advcl.html) & [advcl:abs](https://universaldependencies.org/u/dep/advcl.html)

#### **advcl**
An adverbial clause modifier is a clause which modifies a verb or other predicate (adjective, etc.),
as a modifier not as a core complement. This includes things such as a temporal clause, consequence, conditional clause, purpose
clause, etc. The dependent must be clausal (or else it is an advmod) and the dependent is the main predicate of the clause.

(Source: https://universaldependencies.org/u/dep/advcl.html)

#### **advcl:abs**
*   **Ablative Absolute**: Use the subtype `advcl:abs` (or `advcl`). The participle is the head of the absolute clause and attaches to the main predicate.
*   **Subordinate Clauses**: Clauses introduced by *cum, ut, quia, si*.

#### **advcl**
An adverbial clause modifier is a clause which modifies a verb or other predicate (adjective, etc.),
as a modifier not as a core complement. This includes things such as a temporal clause, consequence, conditional clause, purpose
clause, etc. The dependent must be clausal (or else it is an advmod) and the dependent is the main predicate of the clause.

(Source: https://universaldependencies.org/u/dep/advcl.html)

#### **advcl:abs**
*   **Ablative Absolute**: Use the subtype `advcl:abs` (or `advcl`). The participle is the head of the absolute clause and attaches to the main predicate.
*   **Subordinate Clauses**: Clauses introduced by *cum, ut, quia, si*.

#### **advcl**
An adverbial clause modifier is a clause which modifies a verb or other predicate (adjective, etc.),
as a modifier not as a core complement. This includes things such as a temporal clause, consequence, conditional clause, purpose
clause, etc. The dependent must be clausal (or else it is an advmod) and the dependent is the main predicate of the clause.

(Source: https://universaldependencies.org/u/dep/advcl.html)

#### **advcl:abs**
*   **Ablative Absolute**: Use the subtype `advcl:abs` (or `advcl`). The participle is the head of the absolute clause and attaches to the main predicate.
*   **Subordinate Clauses**: Clauses introduced by *cum, ut, quia, si*.

#### **advcl**
An adverbial clause modifier is a clause which modifies a verb or other predicate (adjective, etc.),
as a modifier not as a core complement. This includes things such as a temporal clause, consequence, conditional clause, purpose
clause, etc. The dependent must be clausal (or else it is an advmod) and the dependent is the main predicate of the clause.

(Source: https://universaldependencies.org/u/dep/advcl.html)

### [acl:relcl](https://universaldependencies.org/u/dep/acl-relcl.html)

#### **acl:relcl**
A relative clause modifier of a nominal is a clause that modifies the nominal,
whereas the nominal is coreferential with a constituent inside the relative
clause (here the constituent may be realized as a relative pronoun, another
relative word, or it may not be overtly realized at all). The acl:relcl
relation points from the head of the modified nominal to the head of the
relative clause.

Depending on language, it may be required that relative clauses are finite.
For example, English non-finite clauses are traditionally not termed relative;
therefore, the girl that was born today is a relative clause because
it is finite, while the girl born today is non-finite (the participle
is not accompanied by a finite auxiliary) and it uses the plain acl
relation. In other languages however, the distinction between finite and
non-finite clauses may not exist or may not be used as a criterion for relative
clauses.

(Source: https://universaldependencies.org/u/dep/acl-relcl.html)

#### **acl:relcl**
A relative clause modifier of a nominal is a clause that modifies the nominal,
whereas the nominal is coreferential with a constituent inside the relative
clause (here the constituent may be realized as a relative pronoun, another
relative word, or it may not be overtly realized at all). The acl:relcl
relation points from the head of the modified nominal to the head of the
relative clause.

Depending on language, it may be required that relative clauses are finite.
For example, English non-finite clauses are traditionally not termed relative;
therefore, the girl that was born today is a relative clause because
it is finite, while the girl born today is non-finite (the participle
is not accompanied by a finite auxiliary) and it uses the plain acl
relation. In other languages however, the distinction between finite and
non-finite clauses may not exist or may not be used as a criterion for relative
clauses.

(Source: https://universaldependencies.org/u/dep/acl-relcl.html)

#### **acl:relcl**
A relative clause modifier of a nominal is a clause that modifies the nominal,
whereas the nominal is coreferential with a constituent inside the relative
clause (here the constituent may be realized as a relative pronoun, another
relative word, or it may not be overtly realized at all). The acl:relcl
relation points from the head of the modified nominal to the head of the
relative clause.

Depending on language, it may be required that relative clauses are finite.
For example, English non-finite clauses are traditionally not termed relative;
therefore, the girl that was born today is a relative clause because
it is finite, while the girl born today is non-finite (the participle
is not accompanied by a finite auxiliary) and it uses the plain acl
relation. In other languages however, the distinction between finite and
non-finite clauses may not exist or may not be used as a criterion for relative
clauses.

(Source: https://universaldependencies.org/u/dep/acl-relcl.html)

#### **acl:relcl**
A relative clause modifier of a nominal is a clause that modifies the nominal,
whereas the nominal is coreferential with a constituent inside the relative
clause (here the constituent may be realized as a relative pronoun, another
relative word, or it may not be overtly realized at all). The acl:relcl
relation points from the head of the modified nominal to the head of the
relative clause.

Depending on language, it may be required that relative clauses are finite.
For example, English non-finite clauses are traditionally not termed relative;
therefore, the girl that was born today is a relative clause because
it is finite, while the girl born today is non-finite (the participle
is not accompanied by a finite auxiliary) and it uses the plain acl
relation. In other languages however, the distinction between finite and
non-finite clauses may not exist or may not be used as a criterion for relative
clauses.

(Source: https://universaldependencies.org/u/dep/acl-relcl.html)

---

## 5. COORDINATION & ORPHANS

### [conj](https://universaldependencies.org/u/dep/conj.html) & [cc](https://universaldependencies.org/u/dep/cc.html)

#### **conj**
A conjunct is the relation between two elements connected by a
coordinating conjunction, such as and, or, etc. Coordinate structures 
are in principle symmetrical, but the first conjunction is by convention 
treated as the parent (or “technical head”) of all subsequent coordinated clauses 
via the conj relation.

Coordinated clauses are treated the same way as coordination of other constituent types:

Coordination may be asyndetic, which means that the coordinating conjunction is omitted.
Commas or other punctuation symbols will delimit the conjuncts in the typical case.
Asyndetic coordination may be more frequent in some languages, while in others,
conjunction will appear between every two conjuncts (John and Mary and Bill).

Unlike elements may be related by conj as a result of ellipsis.
In the following examples, the first element is a main clause while the second has the form of a modifier.
We understand there to be ellipsis of the main predicate (but [we can visit] only after…):

(Source: https://universaldependencies.org/u/dep/conj.html)

#### **cc**
A cc is the relation between a conjunct and
an associated coordinating conjunction.

A coordinating conjunction may also appear at the beginning of a
sentence. This is also attached as cc, even though the sentence lacks
multiple conjuncts joined with a conj relation.

(Source: https://universaldependencies.org/u/dep/cc.html)

#### **conj**
A conjunct is the relation between two elements connected by a
coordinating conjunction, such as and, or, etc. Coordinate structures 
are in principle symmetrical, but the first conjunction is by convention 
treated as the parent (or “technical head”) of all subsequent coordinated clauses 
via the conj relation.

Coordinated clauses are treated the same way as coordination of other constituent types:

Coordination may be asyndetic, which means that the coordinating conjunction is omitted.
Commas or other punctuation symbols will delimit the conjuncts in the typical case.
Asyndetic coordination may be more frequent in some languages, while in others,
conjunction will appear between every two conjuncts (John and Mary and Bill).

Unlike elements may be related by conj as a result of ellipsis.
In the following examples, the first element is a main clause while the second has the form of a modifier.
We understand there to be ellipsis of the main predicate (but [we can visit] only after…):

(Source: https://universaldependencies.org/u/dep/conj.html)

#### **cc**
A cc is the relation between a conjunct and
an associated coordinating conjunction.

A coordinating conjunction may also appear at the beginning of a
sentence. This is also attached as cc, even though the sentence lacks
multiple conjuncts joined with a conj relation.

(Source: https://universaldependencies.org/u/dep/cc.html)

#### **conj**
A conjunct is the relation between two elements connected by a
coordinating conjunction, such as and, or, etc. Coordinate structures 
are in principle symmetrical, but the first conjunction is by convention 
treated as the parent (or “technical head”) of all subsequent coordinated clauses 
via the conj relation.

Coordinated clauses are treated the same way as coordination of other constituent types:

Coordination may be asyndetic, which means that the coordinating conjunction is omitted.
Commas or other punctuation symbols will delimit the conjuncts in the typical case.
Asyndetic coordination may be more frequent in some languages, while in others,
conjunction will appear between every two conjuncts (John and Mary and Bill).

Unlike elements may be related by conj as a result of ellipsis.
In the following examples, the first element is a main clause while the second has the form of a modifier.
We understand there to be ellipsis of the main predicate (but [we can visit] only after…):

(Source: https://universaldependencies.org/u/dep/conj.html)

#### **cc**
A cc is the relation between a conjunct and
an associated coordinating conjunction.

A coordinating conjunction may also appear at the beginning of a
sentence. This is also attached as cc, even though the sentence lacks
multiple conjuncts joined with a conj relation.

(Source: https://universaldependencies.org/u/dep/cc.html)

#### **conj**
A conjunct is the relation between two elements connected by a
coordinating conjunction, such as and, or, etc. Coordinate structures 
are in principle symmetrical, but the first conjunction is by convention 
treated as the parent (or “technical head”) of all subsequent coordinated clauses 
via the conj relation.

Coordinated clauses are treated the same way as coordination of other constituent types:

Coordination may be asyndetic, which means that the coordinating conjunction is omitted.
Commas or other punctuation symbols will delimit the conjuncts in the typical case.
Asyndetic coordination may be more frequent in some languages, while in others,
conjunction will appear between every two conjuncts (John and Mary and Bill).

Unlike elements may be related by conj as a result of ellipsis.
In the following examples, the first element is a main clause while the second has the form of a modifier.
We understand there to be ellipsis of the main predicate (but [we can visit] only after…):

(Source: https://universaldependencies.org/u/dep/conj.html)

### [orphan](https://universaldependencies.org/u/dep/orphan.html)

#### **orphan**
The ‘orphan’ relation is used in cases of head ellipsis where simple promotion would result in an unnatural 
and misleading dependency relation. The typical case is predicate ellipsis where one of the core arguments
has to be promoted to clausal head.

In this example, the subject Peter is promoted to the head position in the second conjunct. Attaching
the object bronze to the subject is necessary to preserve the integrity of the clause, but using the
standard relation obj would be misleading because bronze is not the object of Peter. Therefore,
the orphan relation is used to indicate that this is a non-standard attachment. By contrast, the coordinating
conjunction and performs essentially the same function as in the non-elliptical case and therefore retains
its normal relation cc.

See further discussion of ellipsis.

(Source: https://universaldependencies.org/u/dep/orphan.html)

#### **orphan**
The ‘orphan’ relation is used in cases of head ellipsis where simple promotion would result in an unnatural 
and misleading dependency relation. The typical case is predicate ellipsis where one of the core arguments
has to be promoted to clausal head.

In this example, the subject Peter is promoted to the head position in the second conjunct. Attaching
the object bronze to the subject is necessary to preserve the integrity of the clause, but using the
standard relation obj would be misleading because bronze is not the object of Peter. Therefore,
the orphan relation is used to indicate that this is a non-standard attachment. By contrast, the coordinating
conjunction and performs essentially the same function as in the non-elliptical case and therefore retains
its normal relation cc.

See further discussion of ellipsis.

(Source: https://universaldependencies.org/u/dep/orphan.html)

#### **orphan**
The ‘orphan’ relation is used in cases of head ellipsis where simple promotion would result in an unnatural 
and misleading dependency relation. The typical case is predicate ellipsis where one of the core arguments
has to be promoted to clausal head.

In this example, the subject Peter is promoted to the head position in the second conjunct. Attaching
the object bronze to the subject is necessary to preserve the integrity of the clause, but using the
standard relation obj would be misleading because bronze is not the object of Peter. Therefore,
the orphan relation is used to indicate that this is a non-standard attachment. By contrast, the coordinating
conjunction and performs essentially the same function as in the non-elliptical case and therefore retains
its normal relation cc.

See further discussion of ellipsis.

(Source: https://universaldependencies.org/u/dep/orphan.html)

#### **orphan**
The ‘orphan’ relation is used in cases of head ellipsis where simple promotion would result in an unnatural 
and misleading dependency relation. The typical case is predicate ellipsis where one of the core arguments
has to be promoted to clausal head.

In this example, the subject Peter is promoted to the head position in the second conjunct. Attaching
the object bronze to the subject is necessary to preserve the integrity of the clause, but using the
standard relation obj would be misleading because bronze is not the object of Peter. Therefore,
the orphan relation is used to indicate that this is a non-standard attachment. By contrast, the coordinating
conjunction and performs essentially the same function as in the non-elliptical case and therefore retains
its normal relation cc.

See further discussion of ellipsis.

(Source: https://universaldependencies.org/u/dep/orphan.html)

---

## 6. LATIN-SPECIFIC SUBTYPES

| Relation | Description |
| :--- | :--- |
| `nsubj:pass` | Subject of a passive verb |
| `aux:pass` | Auxiliary for passive periphrastic |
| `advcl:abs` | Ablative Absolute construction |
| `obl:arg` | Selected oblique argument (Dative/Ablative/Prep) |
| `obl:lmod` | Locative modifier (spatial) |
| `obl:tmod` | Temporal modifier |

---

## 7. PUNCTUATION RULES
*   **Delimiters**: Commas, colons, and semi-colons attach to the head of the clause/phrase they delimit (usually a VERB).
---

## 8. NOMINAL MODIFIERS

### [nmod](https://universaldependencies.org/u/dep/nmod.html)

#### **nmod**
The nmod relation is used for nominal dependents of another noun or noun phrase and functionally corresponds to
an attribute, or genitive complement.

New from v2: The nmod relation was previously used also for nominal dependents of verbs, adjectives, and adverbs. These are now covered by the new obl relation.

In conjunction with the case relation, nmod provides a uniform analysis for the possessive alternation (with the option of a subtype like nmod:poss to distinguish non-adpositional case):

(Source: https://universaldependencies.org/u/dep/nmod.html)

#### **nmod**
The nmod relation is used for nominal dependents of another noun or noun phrase and functionally corresponds to
an attribute, or genitive complement.

New from v2: The nmod relation was previously used also for nominal dependents of verbs, adjectives, and adverbs. These are now covered by the new obl relation.

In conjunction with the case relation, nmod provides a uniform analysis for the possessive alternation (with the option of a subtype like nmod:poss to distinguish non-adpositional case):

(Source: https://universaldependencies.org/u/dep/nmod.html)

#### **nmod**
The nmod relation is used for nominal dependents of another noun or noun phrase and functionally corresponds to
an attribute, or genitive complement.

New from v2: The nmod relation was previously used also for nominal dependents of verbs, adjectives, and adverbs. These are now covered by the new obl relation.

In conjunction with the case relation, nmod provides a uniform analysis for the possessive alternation (with the option of a subtype like nmod:poss to distinguish non-adpositional case):

(Source: https://universaldependencies.org/u/dep/nmod.html)

#### **nmod**
The nmod relation is used for nominal dependents of another noun or noun phrase and functionally corresponds to
an attribute, or genitive complement.

New from v2: The nmod relation was previously used also for nominal dependents of verbs, adjectives, and adverbs. These are now covered by the new obl relation.

In conjunction with the case relation, nmod provides a uniform analysis for the possessive alternation (with the option of a subtype like nmod:poss to distinguish non-adpositional case):

(Source: https://universaldependencies.org/u/dep/nmod.html)

### [amod](https://universaldependencies.org/u/dep/amod.html)

#### **amod**
An adjectival modifier of a noun (or pronoun) is any adjectival phrase that serves
to modify the noun (or pronoun). The relation applies whether the meaning of the noun 
is modified in a compositional way (e.g., large house) or an idiomatic way (hot dogs).

An amod dependent may have its own modifiers (e.g., very large house) but the dependent should not be a clause. If it is a clause, then acl should be used.

(Source: https://universaldependencies.org/u/dep/amod.html)

#### **amod**
An adjectival modifier of a noun (or pronoun) is any adjectival phrase that serves
to modify the noun (or pronoun). The relation applies whether the meaning of the noun 
is modified in a compositional way (e.g., large house) or an idiomatic way (hot dogs).

An amod dependent may have its own modifiers (e.g., very large house) but the dependent should not be a clause. If it is a clause, then acl should be used.

(Source: https://universaldependencies.org/u/dep/amod.html)

#### **amod**
An adjectival modifier of a noun (or pronoun) is any adjectival phrase that serves
to modify the noun (or pronoun). The relation applies whether the meaning of the noun 
is modified in a compositional way (e.g., large house) or an idiomatic way (hot dogs).

An amod dependent may have its own modifiers (e.g., very large house) but the dependent should not be a clause. If it is a clause, then acl should be used.

(Source: https://universaldependencies.org/u/dep/amod.html)

#### **amod**
An adjectival modifier of a noun (or pronoun) is any adjectival phrase that serves
to modify the noun (or pronoun). The relation applies whether the meaning of the noun 
is modified in a compositional way (e.g., large house) or an idiomatic way (hot dogs).

An amod dependent may have its own modifiers (e.g., very large house) but the dependent should not be a clause. If it is a clause, then acl should be used.

(Source: https://universaldependencies.org/u/dep/amod.html)

### [case](https://universaldependencies.org/u/dep/case.html) & [det](https://universaldependencies.org/u/dep/det.html)

#### **case**
The case relation is used for any case-marking element which is treated as a separate syntactic word (including prepositions, postpositions, and clitic case markers). Case-marking elements are treated as dependents of the noun they attach to or introduce. (Thus, contrary to SD, UD abandons treating a preposition as a mediator between a modified word and its object.) The case relation aims at providing a more uniform analysis of nominal elements, prepositions and case in morphologically rich languages: a nominal in an oblique case will receive the same dependency structure as a nominal introduced by an adposition.

When case markers are morphemes, they are not divided off the noun as a separate case dependent,
but the noun as a whole is analyzed as obl (if dependent on a predicate) or nmod (if dependent on noun).
To overtly mark case,
POS tags and
features
are included in the representation as shown below on a Russian example
(put your mouse pointer over the words to see additional morphosyntactic features).

This treatment provides parallelism between different constructions
across and within languages. A good result is that we now have greater
parallelism between prepositional phrases and subordinate clauses,
which are often introduced by a preposition in some languages (but note that 
the relation should be mark in those cases):

We also obtain parallel constructions for

Another advantage of this new analysis is that it provides a treatment
of prepositional phrases that are predicative complements of “be” that is consistent with the treatment of nominal predicative
complements:

When prepositions are stacked (that is, there is a sequence of prepositions), there are two possible analyses. If the sequence is a frozen combination with a specific meaning, then the best analysis is as fixed. An English example of this is out of:

However, if various combinations of prepositions can be used to express different meaning combinations or nuances, then  each preposition is independently analyzed as a case dependent. Examples of this in English include up beside (which can alternate with down beside or up near) or except during which can alternate with as during or except after:

(Source: https://universaldependencies.org/u/dep/case.html)

#### **det**
The relation determiner (det) holds between a nominal head and its
determiner. Most commonly, a word of POS DET will have the relation det and vice versa. The known exceptions at present are:

(Source: https://universaldependencies.org/u/dep/det.html)

#### **case**
The case relation is used for any case-marking element which is treated as a separate syntactic word (including prepositions, postpositions, and clitic case markers). Case-marking elements are treated as dependents of the noun they attach to or introduce. (Thus, contrary to SD, UD abandons treating a preposition as a mediator between a modified word and its object.) The case relation aims at providing a more uniform analysis of nominal elements, prepositions and case in morphologically rich languages: a nominal in an oblique case will receive the same dependency structure as a nominal introduced by an adposition.

When case markers are morphemes, they are not divided off the noun as a separate case dependent,
but the noun as a whole is analyzed as obl (if dependent on a predicate) or nmod (if dependent on noun).
To overtly mark case,
POS tags and
features
are included in the representation as shown below on a Russian example
(put your mouse pointer over the words to see additional morphosyntactic features).

This treatment provides parallelism between different constructions
across and within languages. A good result is that we now have greater
parallelism between prepositional phrases and subordinate clauses,
which are often introduced by a preposition in some languages (but note that 
the relation should be mark in those cases):

We also obtain parallel constructions for

Another advantage of this new analysis is that it provides a treatment
of prepositional phrases that are predicative complements of “be” that is consistent with the treatment of nominal predicative
complements:

When prepositions are stacked (that is, there is a sequence of prepositions), there are two possible analyses. If the sequence is a frozen combination with a specific meaning, then the best analysis is as fixed. An English example of this is out of:

However, if various combinations of prepositions can be used to express different meaning combinations or nuances, then  each preposition is independently analyzed as a case dependent. Examples of this in English include up beside (which can alternate with down beside or up near) or except during which can alternate with as during or except after:

(Source: https://universaldependencies.org/u/dep/case.html)

#### **det**
The relation determiner (det) holds between a nominal head and its
determiner. Most commonly, a word of POS DET will have the relation det and vice versa. The known exceptions at present are:

(Source: https://universaldependencies.org/u/dep/det.html)

#### **case**
The case relation is used for any case-marking element which is treated as a separate syntactic word (including prepositions, postpositions, and clitic case markers). Case-marking elements are treated as dependents of the noun they attach to or introduce. (Thus, contrary to SD, UD abandons treating a preposition as a mediator between a modified word and its object.) The case relation aims at providing a more uniform analysis of nominal elements, prepositions and case in morphologically rich languages: a nominal in an oblique case will receive the same dependency structure as a nominal introduced by an adposition.

When case markers are morphemes, they are not divided off the noun as a separate case dependent,
but the noun as a whole is analyzed as obl (if dependent on a predicate) or nmod (if dependent on noun).
To overtly mark case,
POS tags and
features
are included in the representation as shown below on a Russian example
(put your mouse pointer over the words to see additional morphosyntactic features).

This treatment provides parallelism between different constructions
across and within languages. A good result is that we now have greater
parallelism between prepositional phrases and subordinate clauses,
which are often introduced by a preposition in some languages (but note that 
the relation should be mark in those cases):

We also obtain parallel constructions for

Another advantage of this new analysis is that it provides a treatment
of prepositional phrases that are predicative complements of “be” that is consistent with the treatment of nominal predicative
complements:

When prepositions are stacked (that is, there is a sequence of prepositions), there are two possible analyses. If the sequence is a frozen combination with a specific meaning, then the best analysis is as fixed. An English example of this is out of:

However, if various combinations of prepositions can be used to express different meaning combinations or nuances, then  each preposition is independently analyzed as a case dependent. Examples of this in English include up beside (which can alternate with down beside or up near) or except during which can alternate with as during or except after:

(Source: https://universaldependencies.org/u/dep/case.html)

#### **det**
The relation determiner (det) holds between a nominal head and its
determiner. Most commonly, a word of POS DET will have the relation det and vice versa. The known exceptions at present are:

(Source: https://universaldependencies.org/u/dep/det.html)

#### **case**
The case relation is used for any case-marking element which is treated as a separate syntactic word (including prepositions, postpositions, and clitic case markers). Case-marking elements are treated as dependents of the noun they attach to or introduce. (Thus, contrary to SD, UD abandons treating a preposition as a mediator between a modified word and its object.) The case relation aims at providing a more uniform analysis of nominal elements, prepositions and case in morphologically rich languages: a nominal in an oblique case will receive the same dependency structure as a nominal introduced by an adposition.

When case markers are morphemes, they are not divided off the noun as a separate case dependent,
but the noun as a whole is analyzed as obl (if dependent on a predicate) or nmod (if dependent on noun).
To overtly mark case,
POS tags and
features
are included in the representation as shown below on a Russian example
(put your mouse pointer over the words to see additional morphosyntactic features).

This treatment provides parallelism between different constructions
across and within languages. A good result is that we now have greater
parallelism between prepositional phrases and subordinate clauses,
which are often introduced by a preposition in some languages (but note that 
the relation should be mark in those cases):

We also obtain parallel constructions for

Another advantage of this new analysis is that it provides a treatment
of prepositional phrases that are predicative complements of “be” that is consistent with the treatment of nominal predicative
complements:

When prepositions are stacked (that is, there is a sequence of prepositions), there are two possible analyses. If the sequence is a frozen combination with a specific meaning, then the best analysis is as fixed. An English example of this is out of:

However, if various combinations of prepositions can be used to express different meaning combinations or nuances, then  each preposition is independently analyzed as a case dependent. Examples of this in English include up beside (which can alternate with down beside or up near) or except during which can alternate with as during or except after:

(Source: https://universaldependencies.org/u/dep/case.html)

---

## 9. STRUCTURAL ATTACHMENT PRINCIPLES [HEAD]

When evaluating disagreements regarding the **HEAD** (attachment index), consider these priority rules:

1. **Dependency vs. Coordination**: In coordination, all items should ideally attach to the first element (`conj`). Disagreements often arise when a system incorrectly attaches a second conjunct to the main verb instead of the first conjunct.
2. **Verb Clusters**: Auxiliaries and Copulas (`aux`, `cop`) always depend on the lexical predicate (Noun, Adjective, or Participle). The lexical predicate is the head.
3. **Prepositional Phrases**: The preposition (`case`) depends on the noun. The noun depends on the predicate.
4. **Apposition vs. Modifiers**: Appositions (`appos`) attach to the noun they specify. Nominal modifiers (`nmod`) also attach to the noun.
5. **Evaluating Changes**: If the systems agree on the relation (`deprel`) but disagree on the `HEAD`, verify which attachment better reflects the semantic scope of the modifier.

> [!NOTE]
> If a system proposes a head that creates a cycle or leaves a fragment disconnected from the `root`, it is likely incorrect.
