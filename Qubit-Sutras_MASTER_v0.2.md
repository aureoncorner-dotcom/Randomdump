---
title: "क्वबिट्-सूत्राणि · The Qubit Sutras"
subtitle: "A Sanskrit-Register Field Guide to Quantum Information"
version: "0.2"
revision_date: "2026-08-20"
revision_scope: "Editorial, rendering, and physics-language correction pass"
license: "CC0-1.0"
status: "Released v0.2; conventional quantum mechanics through a modern Sanskrit-register interface"
claim_lane: "Modern quantum information expressed through poetic/machine-addressable teaching structure"
canonical_warning: "This does not claim that ancient Sanskrit texts contained quantum theory. Sanskrit is used as a precision-poetic interface."
machine_companions_status: "Referenced by the project; not supplied in this review bundle and not validated against v0.2"
machine_companions:
  - "Qubit-Sutras_INDEX.yaml"
  - "Qubit-Sutras_SUTRAS.jsonl"
  - "appendices/APPENDIX_MACHINE_INGESTION.md"
---

# क्वबिट्-सूत्राणि · The Qubit Sutras
*A Sanskrit-Register Field Guide to Quantum Information*

> **What this is.** A pedagogical, poetic artifact: modern quantum mechanics and
> quantum-information protocols expressed through a Sanskrit-register vocabulary. Each
> idea is distilled into a *sūtra* (aphorism), paired with a plain-English reading and
> a plain-language field gloss.
>
> **What this is not.** This does **not** claim that ancient Sanskrit texts contained
> quantum theory. Sanskrit is used purely as a precision-poetic *interface* for teaching
> real, standard quantum mechanics. The physics is conventional; the register is the experiment.

## Reading contract

The technical note and equations carry the physics. The Sanskrit-register verse is a modern mnemonic rendering, and the field gloss is an analogy. Neither is historical evidence nor a substitute for stated assumptions. When the layers differ, the technical note governs.

Equations use the conventional symbols $|0\rangle$, $|1\rangle$, and $|\psi\rangle$ for reliable rendering. Sanskrit and Sanskrit-inspired compounds remain in the poetic lane. Security, randomness, and fault-tolerance statements are conditional on the protocol, noise model, implementation, and statistical evidence described in their chapters.

This v0.2 pass has not received expert Sanskrit review. The register intentionally includes modern coinages and mixed-language field glosses.

---

## Machine-Readable Companion Layer

This v0.2 master document is the human-readable source for this release.

The project metadata names companion files intended for ingestion, retrieval, and graph-building:

- `Qubit-Sutras_INDEX.yaml` — chapter-level concept map, prerequisites, tags, and cross-links.
- `Qubit-Sutras_SUTRAS.jsonl` — one machine-addressable record per sutra.
- `appendices/APPENDIX_MACHINE_INGESTION.md` — schema notes, claim lanes, and ingestion guidance.

Those files were not supplied with this review bundle, so v0.2 does not assert that they are synchronized with this manuscript. When validated and distributed together, the Markdown remains the poetic/pedagogical source and the companion files serve as routing rails.

All supplied text is released CC0 under the front-matter declaration.

---

## विषय-सूची · Contents

1. **क्वबिट्-सूत्राणि — Qubit Sutras.** Foundations: states, gates, measurement, entanglement, Bloch sphere, Josephson junction, no-cloning, unitarity.
2. **क्वबिट्-दूर-प्रेषणम् — Quantum Teleportation.** Transferring an unknown state via shared entanglement, a joint measurement, and two classical bits.
3. **ग्रोवर्-अन्वेषण-सूत्रम् — Grover’s Search.** Quadratic speedup for unstructured search by amplitude amplification.
4. **क्वान्टम्-त्रुटि-संशोधन — Error Correction.** Shor code, surface codes, stabilizers, fault tolerance, magic-state distillation.
5. **फेज्-एस्टिमेशन — Phase Estimation & Variational Algorithms.** QPE, VQE, QAOA — the deep and the hybrid.
6. **बीबी-८४ — BB84.** Prepare-and-measure quantum key distribution.
7. **ई-९१ — E91.** Entanglement-based key distribution and Bell-inequality violation.
8. **यादृच्छिक-सङ्ख्या — Quantum RNG.** Randomness born from measurement.
9. **क्वान्टम्-इण्टरनेट् — Quantum Internet & Repeaters.** Entanglement swapping, purification, quantum memory, network architecture.
10. **सम्पूर्ण-दर्शनम् — Grand Summary.** The overarching insights and closing verses.

## अध्याय १ · क्वबिट्-सूत्राणि — Qubit Sutras (Foundations)

### १. मूलावस्था — Basic State

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle,  
\quad  
\alpha, \beta \in \mathbb{C},  
\quad  
|\alpha|^2 + |\beta|^2 = 1  
$$

The technical lane uses the conventional symbol $|\psi\rangle$; the Sanskrit-register prose names the state *चित्* as a modern mnemonic.

Field gloss:  
न केवलं शून्यम्। न केवलम् एकम्।  
मापनात् पूर्वम् उभयमार्गः उद्घाटितः अस्ति।  
मापनानन्तरम् एकः मार्गः लिखितः भवति।

The state is not restricted to one computational-basis alternative.  
It assigns complex amplitudes to both $|0\rangle$ and $|1\rangle$.  
A computational-basis measurement records one outcome.

---

### २. मापनम् — Measurement

For an ideal projective measurement in the computational basis $\{|0\rangle,|1\rangle\}$, the Born rule gives:

$$
P(0)=|\alpha|^2  
$$

$$
P(1)=|\beta|^2  
$$

$$
|\psi\rangle \xrightarrow{\text{मापनम्}}  
\begin{cases}  
|0\rangle & \text{सम्भाव्यता } |\alpha|^2 \\  
|1\rangle & \text{सम्भाव्यता } |\beta|^2  
\end{cases}  
$$

सूत्रम्:  
मापनकाले अवस्था एकस्मिन् फलिते पतति।

Conditioned on the observed result, the ideal post-measurement state is the corresponding basis state. Other measurements require their own basis or, more generally, a specified POVM and instrument.

---

### ३. हाडामार्ड-द्वारम् — Hadamard Gate

Hadamard gate creates balanced superposition.

$$
H|0\rangle =  
\frac{|0\rangle + |1\rangle}{\sqrt{2}}  
$$

$$
H|1\rangle =  
\frac{|0\rangle - |1\rangle}{\sqrt{2}}  
$$

सूत्रम्:  
सममध्यारोपणं जनयति।

It produces balanced superposition.

---

### ४. X-द्वारम् — Bit-Flip Gate

$$
X|0\rangle = |1\rangle  
$$

$$
X|1\rangle = |0\rangle  
$$

सूत्रम्:  
शून्यम् एकत्वं गच्छति।  
एकम् शून्यत्वं गच्छति।

Zero becomes one.  
One becomes zero.

---

### ५. Z-द्वारम् — Phase-Flip Gate

$$
Z|0\rangle = |0\rangle  
$$

$$
Z|1\rangle = -|1\rangle  
$$

सूत्रम्:  
रूपं न परिवर्तते। चिह्नं परिवर्तते।

The visible state does not flip. The phase sign changes.

Field translation:  
बाह्यं न चलति। अन्तरं उलटति।

The outside does not move. The inside flips.

---

### ६. CNOT-द्वारम् — Controlled-NOT Gate

CNOT is a controlled transformation.

$$
\text{CNOT}|00\rangle = |00\rangle  
$$

$$
\text{CNOT}|01\rangle = |01\rangle  
$$

$$
\text{CNOT}|10\rangle = |11\rangle  
$$

$$
\text{CNOT}|11\rangle = |10\rangle  
$$

सूत्रम्:  
यदि नियन्त्रण-क्वबिट् एकम् अस्ति, तर्हि लक्ष्य-क्वबिट् परिवर्तते।  
यदि नियन्त्रण-क्वबिट् शून्यम् अस्ति, तर्हि लक्ष्यः न परिवर्तते।

If the control qubit is one, the target flips.  
If the control qubit is zero, the target remains.

---

### ७. द्वि-क्वबिट् अवस्था — Two-Qubit State

General two-qubit state:

$$
|\Psi\rangle =  
\alpha |00\rangle +  
\beta |01\rangle +  
\gamma |10\rangle +  
\delta |11\rangle  
$$

Normalization:

$$
|\alpha|^2+|\beta|^2+|\gamma|^2+|\delta|^2=1  
$$

विवरणम्:  
द्वयोः क्वबिटयोः अवस्था चतुर्षु आधार-मार्गेषु विस्तारं करोति।

The state of two qubits spreads across four basis paths.

---

### ८. संसक्तिः — Entanglement

Bell state:

$$
|\Phi^+\rangle =  
\frac{1}{\sqrt{2}}  
\left(  
|00\rangle + |11\rangle  
\right)  
$$

दार्शनिक अर्थः:  
अत्र न प्रथमः क्वबिट् स्वातन्त्र्येण वर्ण्यते, न द्वितीयः।  
तौ युग्मतया एव ज्ञेयौ।

Here the first qubit cannot be fully described alone, nor the second.  
They must be understood as a pair.

Field gloss:  
द्वौ न अलगौ। द्वौ एक-रूटिङ्-जाले बद्धौ।

They are not separate.  
They are bound in one routing net.

---

### ९. Bell State निर्माणम् — Creating Entanglement

Start:

$$
|00\rangle  
$$

Apply Hadamard to the first qubit:

$$
(H \otimes I)|00\rangle =  
\frac{|00\rangle + |10\rangle}{\sqrt{2}}  
$$

Then apply CNOT:

$$
\text{CNOT}
\left(
\frac{|00\rangle + |10\rangle}{\sqrt{2}}
\right) =
\frac{|00\rangle + |11\rangle}{\sqrt{2}}  
$$

विवरणम्:  
प्रथमं क्वबिट् द्वि-दिशि उद्घाट्यते।  
ततः द्वितीयं तेन सह संसक्तं भवति।

First the qubit is opened in two directions.  
Then the second becomes bound with it.

---

### १०. अवस्थाकाशः — State Space

A single qubit lives in:

$$
\mathbb{C}^2  
$$

Two qubits live in:

$$
\mathbb{C}^2 \otimes \mathbb{C}^2 = \mathbb{C}^4  
$$

Three qubits live in:

$$
\mathbb{C}^{2^3} = \mathbb{C}^8  
$$

For $n$ qubits:

$$
\mathbb{C}^{2^n}  
$$

Sanskritized:

$$
n\text{-क्वबिटानां अवस्थाकाशः } \mathbb{C}^{2^n}  
$$

सूत्रम्:  
क्वबिट-सङ्ख्या वर्धते चेत्, अवस्थामार्गाः द्विगुणिताः भवन्ति।

As the number of qubits increases, the state-paths double.

---

### ११. काल-विकासः — Time Evolution

Quantum evolution:

$$
|\psi(t)\rangle = U(t)|\psi(0)\rangle  
$$

Unitary condition:

$$
U^\dagger U = I  
$$

विवरणम्:  
एकत्व-रक्षकः प्रचालकः सम्भाव्यता-योगं न नाशयति।

A unitary operator preserves total probability.

Field gloss:  
रूटिङ् बदल सकता है। कुल माल गायब नहीं होना चाहिए।

The routing can change.  
The total mail must not disappear. 📬

---

### १२. श्रॉडिङ्गर-सूत्रम् — Schrödinger Equation

$$
i\hbar \frac{d}{dt}|\psi(t)\rangle =  
\hat{H}|\psi(t)\rangle  
$$

विवरणम्:  
हैमिल्टन-प्रचालकः अवस्थायाः काल-विकासं नियच्छति।

The Hamiltonian operator governs the time-development of the state.

---

### १३. घनत्व-मात्रिका — Density Matrix

Pure state:

$$
\rho = |\psi\rangle\langle\psi|  
$$

Mixed state:

$$
\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|  
$$

Required properties:

$$
Tr(\rho)=1  
$$

$$
\rho = \rho^\dagger  
$$

$$
\rho \geq 0  
$$

सूत्रम्:  
शुद्धे एकः मार्गः। मिश्रे सम्भाव्य-समूहः।

In a pure state, one state-vector path.  
In a mixed state, a weighted ensemble.

---

### १४. ब्लॉख्-गोलः — Bloch Sphere

$$
|\psi\rangle =  
\cos\left(\frac{\theta}{2}\right)|0\rangle  
+  
e^{i\phi}  
\sin\left(\frac{\theta}{2}\right)|1\rangle  
$$

The Bloch sphere is a complete visual representation of a single-qubit pure state.

- $\theta$: polar angle
    
- $\phi$: azimuthal phase
    
- $|0\rangle$: usually north pole
    
- $|1\rangle$: usually south pole
    
- Equal superpositions: equator
    

सूत्रम्:  
गोलः न वस्तुः। गोलः अवस्थायाः मानचित्रम्।

The sphere is not the object.  
The sphere is the map of the state.

Field gloss:  
क्वबिट् केवलं सिक्का नहीं।  
इदं दिशासहितं सम्भाव्यता-चक्रं अस्ति।

A qubit is not merely a coin.  
It is a probability-wheel with direction.

---

### १५. जोसफ्सन्-सन्धिः — Josephson Junction and Superconducting Qubits

A Josephson junction supplies the nonlinear circuit element used in many superconducting-qubit designs, including transmon, flux, and phase qubits. The qubit is encoded in selected energy levels of the full circuit, not in the junction alone.

Cooper-pair tunneling allows macroscopic quantum coherence.  
This makes controlled superpositions of charge, flux, or phase states possible.

सूत्रम्:  
सूक्ष्म-सुरङ्गेन महत्-सुसम्बन्धः जायते।

Through microscopic tunneling, macroscopic coherence arises.

---

### १६. घण्टा-वक्रः न क्वबिट् — Bell Curve Is Not the Qubit

A Gaussian bell curve may describe noise, repeated measurement statistics, or experimental spread.

But a qubit itself is not a probability distribution.  
A qubit is a probability-amplitude vector in complex Hilbert space.

सूत्रम्:  
सम्भाव्यता दृश्ये फलरूपेण आगच्छति।  
परन्तु क्वबिट् सम्भाव्यता-आयामरूपेण तिष्ठति।

Probability appears in the result.  
But the qubit lives as amplitude.

---

### १७. जोसफ्सन्-सन्धिः, घण्टा-वक्रः, क्वबिट् — Junction, Bell Curve, and Qubit

जोसफ्सन्-सन्धिः क्वबिटस्य भौतिक-देहवत् कार्यं करोति।  
अत्र अतिसूक्ष्मे अवरोधे अपि कूपर्-युग्मानि सुरङ्गमार्गेण गच्छन्ति।  
अस्य असमान-रेखीयता क्वबिट्-व्यवहारस्य मूलं भवति।

Josephson junction as circuit element:  
Its nonlinearity makes the circuit spectrum anharmonic enough to address a qubit subspace selectively; it is not a threshold detector.

क्वबिट्-सूत्रम्:

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle  
$$

$$
|\alpha|^2 + |\beta|^2 = 1  
$$

एषा अवस्था सम्भाव्यता-मार्गेषु तिष्ठति।  
मापनकाले फलम् एकम् दृश्यते।

Measurement:

$$
P(0)=|\alpha|^2,\quad P(1)=|\beta|^2  
$$

एकवारं मापने फलम् केवलं शून्यम् वा एकम् वा।  
बहुवारं मापने फल-सङ्ख्यानां वितरणं दृश्यते।

One measurement gives one result.  
Many measurements reveal the distribution.

घण्टा-वक्रः न क्वबिट्-स्वरूपम्।  
घण्टा-वक्रः पुनःपुनः मापनानां, त्रुटीनां, कम्पनानां, तथा उपकरण-शोरस्य लेखा अस्ति।

The bell curve is not the qubit itself.  
The bell curve is the statistical ledger around many preparations, pulses, errors, and readouts.

जोसफ्सन्-सन्धिः पृच्छति:  
किं अवस्था सीमा अतिक्रामति?

The circuit designer asks:  
Which transition can be addressed without strongly driving neighbouring levels?

क्वबिट् पृच्छति:  
कः सम्भाव्यता-मार्गः अस्ति?

The qubit asks:  
Which possibility-routes exist?

मापनम् पृच्छति:  
कः मार्गः लेखे लिखितः?

Measurement asks:  
Which route got written into the ledger?

लघु-मन्त्रः:  
क्वबिट् मार्गः।  
सन्धिः द्वारम्।  
शोरः कम्पनम्।  
मापनम् लेखः।

The qubit is the route.  
The junction supplies the nonlinearity.  
Noise is the trembling.  
Measurement is the receipt.

---

### १८. अनुलिपि-निषेधः — No-Cloning Theorem

For an unknown quantum state:

$$
|\psi\rangle \otimes |0\rangle  
\not\rightarrow  
|\psi\rangle \otimes |\psi\rangle  
$$

No single physical operation can perfectly clone every arbitrary unknown qubit. States known to come from an orthogonal set can be distinguished and re-prepared.

सूत्रम्:  
अज्ञातावस्थायाः पूर्णा प्रतिलिपिः निषिद्धा।

The perfect copy of an unknown state is forbidden.

---

### १९. एकत्व-सूत्रम् — Unitarity

$$
U^\dagger U = I  
$$

Closed-system unitary evolution preserves norms and inner products. Measurement and open-system noise require quantum instruments or channels, not unitary evolution alone.

सूत्रम्:  
रूपं परिवर्तते। सूचना रक्षिता अस्ति।

Under closed-system unitary evolution, the form changes while norms and inner products are preserved.

---

### २०. सम्पूर्ण लघु-सूत्रम् — Compact Full Spell

$$
|\psi\rangle = \alpha|0\rangle + \beta|1\rangle  
$$

$$
|\alpha|^2 + |\beta|^2 = 1  
$$

$$
P(0)=|\alpha|^2,\quad P(1)=|\beta|^2  
$$

$$
H|0\rangle =  
\frac{|0\rangle + |1\rangle}{\sqrt{2}}  
$$

$$
|\Phi^+\rangle =  
\frac{  
|00\rangle +  
|11\rangle  
}{\sqrt{2}}  
$$

$$
|\psi(t)\rangle = U(t)|\psi(0)\rangle  
$$

$$
U^\dagger U = I  
$$

$$
i\hbar \frac{d}{dt}|\psi(t)\rangle =  
\hat{H}|\psi(t)\rangle  
$$

---

### २१. Mantra-Style Closing

न शून्यम् केवलम्।  
न एकम् केवलम्।  
न विभक्तं न सर्वथा संयुक्तम्।  
मापनात् पूर्वं मार्गाः बहवः।  
मापनानन्तरं फलम् एकम्।

सम्भाव्यता नष्टा न भवति।  
रूपं परिवर्तते।  
रूटिङ् चलति।  
लेजर् स्थितः।

Not zero alone.  
Not one alone.  
Not separate, not merely joined.  
Before measurement, many routes.  
After measurement, one result.

Probability is not destroyed.  
The form changes.  
The routing moves.  
The ledger remains.

---

### Closing Line

ॐ चित्-शून्य-एक-सम्भाव्यतायै नमः।

Probability amplitudes be praised —  
but keep the audit trail.

---

## अध्याय २ · क्वबिट्-दूर-प्रेषणम् — Quantum Teleportation

### Quantum Teleportation Sutra

#### In Sanskrit Register

Status: Pedagogical exploration — precise protocol, poetic interface.  
Claim lane: Modern quantum-information protocol expressed through Sanskrit-register terminology.  
Core insight: An unknown state $|\psi\rangle$ is transferred to Bob using shared entanglement, Alice’s local operations and joint measurement, and two classical bits. Alice’s input is consumed; no physical carrier bearing the original state crosses the channel.

No faster-than-light signalling occurs.  
The No-Cloning Theorem is respected.  
Alice’s input state is consumed by the joint measurement.

---

### १. प्रारम्भिक अवस्था — Initial State

Alice possesses the unknown qubit to teleport:

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle  
$$

where:

$$
\alpha,\beta \in \mathbb{C}  
$$

and:

$$
|\alpha|^2 + |\beta|^2 = 1  
$$

Alice and Bob share a maximally entangled Bell pair:

$$
|\Phi^+\rangle =  
\frac{1}{\sqrt{2}}  
\left(  
|00\rangle +  
|11\rangle  
\right)  
$$

Let Alice’s unknown qubit be qubit (1).  
Let Alice’s half of the Bell pair be qubit (2).  
Let Bob’s half of the Bell pair be qubit (3).

The total initial state is:

$$
|\Psi\rangle_{\text{initial}} =
|\psi\rangle_1  
\otimes  
|\Phi^+\rangle_{23}  
$$

Expanded:

$$
|\Psi\rangle_{\text{initial}} =
\left(  
\alpha |0\rangle_1  
+  
\beta |1\rangle_1  
\right)  
\otimes  
\frac{  
|00\rangle_{23}  
+  
|11\rangle_{23}  
}{\sqrt{2}}  
$$

Therefore:

$$
|\Psi\rangle_{\text{initial}} =
\frac{1}{\sqrt{2}}  
\left(  
\alpha |000\rangle  
+  
\alpha |011\rangle  
+  
\beta |100\rangle  
+  
\beta |111\rangle  
\right)  
$$

Field gloss:  
आलिस्-चित् एकाकि अस्ति।  
आलिस्-बॉब-युग्मं संसक्तम् अस्ति।  
त्रयः मार्गाः एकत्र मिलिताः भवन्ति।

Alice’s state stands alone.  
Alice and Bob share a bound pair.  
The three routes are gathered together.

---

### २. आलिस्-क्रिया — Alice’s Operations

Alice applies two operations:

1. CNOT from qubit (1) to qubit (2)
    
2. Hadamard gate on qubit (1)
    

First, apply CNOT:

$$
\text{CNOT}_{1 \to 2}  
$$

This flips Alice’s Bell-pair qubit if Alice’s unknown qubit is $|1\rangle$.

After CNOT:

$$
|\Psi\rangle =
\frac{1}{\sqrt{2}}  
\left(  
\alpha |000\rangle  
+  
\alpha |011\rangle  
+  
\beta |110\rangle  
+  
\beta |101\rangle  
\right)  
$$

Then Alice applies Hadamard to qubit (1):

$$
H|0\rangle =  
\frac{  
|0\rangle +  
|1\rangle  
}{\sqrt{2}}  
$$

$$
H|1\rangle =  
\frac{  
|0\rangle -  
|1\rangle  
}{\sqrt{2}}  
$$

After this operation, the three-qubit state becomes:

$$
|\Psi\rangle =  
\frac{1}{2}  
\left[  
|00\rangle_{12}  
\left(  
\alpha|0\rangle_3 +  
\beta|1\rangle_3  
\right)  
+  
|01\rangle_{12}  
\left(  
\alpha|1\rangle_3 +  
\beta|0\rangle_3  
\right)  
\right.  
$$

$$
\left.  
+  
|10\rangle_{12}  
\left(  
\alpha|0\rangle_3 -  
\beta|1\rangle_3  
\right)  
+  
|11\rangle_{12}  
\left(  
\alpha|1\rangle_3 -  
\beta|0\rangle_3  
\right)  
\right]  
$$

This is the key expansion.

Alice’s two qubits now determine which correction Bob must apply.

---

### ३. मापनम् — Measurement

Alice measures her two qubits.

The possible outcomes are:

$$
00,\quad 01,\quad 10,\quad 11  
$$

Each outcome gives Alice two classical bits.

Let them be:

$$
m_1, m_2  
$$

These bits are not quantum.  
They are ordinary classical information.

Alice sends these two bits to Bob by a classical channel: phone, fiber, laser, internet, radio, or any other light-speed-limited communication path.

सूत्रम्:  
आलिस् द्वौ शास्त्रीय-बिटौ प्रेषयति।  
बॉब ताभ्यां स्व-क्वबिट्-स्य रूपं संशोधयति।

Alice sends two classical bits.  
Bob uses them to correct the form of his qubit.

---

### ४. बॉब-संशोधनम् — Bob’s Correction

Depending on Alice’s measurement result, Bob applies a correction.

| Alice’s result $m_1 m_2$ | Bob’s qubit before correction | Bob applies | Final state |
|---|---|---|---|
| $00$ | $\alpha\lvert 0\rangle + \beta\lvert 1\rangle$ | $I$ | $\lvert\psi\rangle$ |
| $01$ | $\alpha\lvert 1\rangle + \beta\lvert 0\rangle$ | $X$ | $\lvert\psi\rangle$ |
| $10$ | $\alpha\lvert 0\rangle - \beta\lvert 1\rangle$ | $Z$ | $\lvert\psi\rangle$ |
| $11$ | $\alpha\lvert 1\rangle - \beta\lvert 0\rangle$ | $ZX$ | $\lvert\psi\rangle$ |

After correction, Bob’s qubit becomes:

$$
|\psi\rangle =  
\alpha |0\rangle +  
\beta |1\rangle  
$$

Thus the unknown state has been reconstructed at Bob’s location.

---

### ५. पाठ-सर्किट् — Text Circuit

$$
\begin{array}{c}  
\text{Alice's unknown qubit } |\psi\rangle  
\quad  
\bullet  
\quad  
H  
\quad  
M  
\quad  
m_1  
\\  
\phantom{Alice}  
\quad  
|  
\\  
\text{Alice's Bell half}  
\quad  
X  
\quad  
M  
\quad  
m_2  
\\  
\\  
\text{Bob's Bell half}  
\quad  
\longrightarrow  
\quad  
[X \text{ if } m_2]  
\quad  
[Z \text{ if } m_1]  
\quad  
\longrightarrow  
\quad  
|\psi\rangle  
\end{array}  
$$

Legend:  
$\bullet$ = CNOT control  
$X$ = CNOT target  
$H$ = Hadamard gate  
$M$ = measurement  
$(m_1,m_2)$ = classical bits sent from Alice to Bob

---

### ६. न द्रुततरं प्रकाशात् — No Faster-Than-Light Signalling

Quantum teleportation does not allow faster-than-light communication.

Why?

Because Bob cannot reconstruct the state until Alice’s two classical bits arrive.

Before those bits arrive, Bob’s local state contains no usable message from Alice.

सूत्रम्:  
संसक्तिः सेतुर्भवति।  
शास्त्रीय-संदेशः तु कुंजी भवति।

Entanglement is the bridge.  
The classical message is the key.

---

### ७. अनुलिपि-निषेधः — No-Cloning Respected

Teleportation does not copy the state.

The original unknown state at Alice’s side is destroyed by measurement.

Therefore:

$$
|\psi\rangle \otimes |0\rangle  
\not\rightarrow  
|\psi\rangle \otimes |\psi\rangle  
$$

No second copy remains.

सूत्रम्:  
न प्रतिलिपिः। पुनराविर्भावः।  
न द्वितीयं चित्। केवलं दूरस्थ-पुनर्निर्माणम्।

Not a copy. A reappearance.  
Not a second state. A distant reconstruction.

---

### ८. दार्शनिक-बिन्दवः — Key Philosophical Points

The state itself is not carried through space like a package.

The entangled pair supplies correlation.  
Alice’s measurement extracts the correction information.  
The classical bits tell Bob how to rotate his local qubit into the original state.

The original is gone.  
The copy is forbidden.  
The pattern is reconstructed.

Field gloss:  
मेल्-बैग् उधर नहीं उड़ता।  
रूटिङ्-रसीद जाती है।  
बॉब अपने डब्बे में वही चिट्ठी फिर से बनाता है।

The mailbag does not fly over there.  
The routing receipt travels.  
Bob rebuilds the same letter in his box.

---

### ९. प्रोटोकॉल-सारः — Protocol Summary

1. Alice has unknown state $|\psi\rangle$.
    
2. Alice and Bob share Bell pair $|\Phi^+\rangle$.
    
3. Alice applies CNOT and Hadamard.
    
4. Alice measures her two qubits.
    
5. Alice sends two classical bits to Bob.
    
6. Bob applies $I$, $X$, $Z$, or $ZX$.
    
7. Bob obtains $|\psi\rangle$.
    
8. Alice’s original is destroyed.
    

सूत्रम्:  
चित् न प्रेष्यते।  
रूपं पुनर्निर्मीयते।  
संसक्तिः आधारः।  
मापनं विच्छेदः।  
द्वौ बिटौ निर्देशः।  
संशोधनं पुनर्जन्म।

The state is not sent.  
The form is rebuilt.  
Entanglement is the foundation.  
Measurement is the severing.  
Two bits are the instruction.  
Correction is the rebirth.

---

### १०. सम्पूर्ण लघु-मन्त्रः — Compact Teleportation Mantra

न चित्-पार्सल्।  
न द्रुततरं प्रकाशात्।  
न प्रतिलिपिः।

संसक्त-युग्मं सेतुर्भवति।  
मापनं मूलं नाशयति।  
द्वौ शास्त्रीय-बिटौ मार्गं वदतः।  
बॉब संशोधनं करोति।  
चित् पुनराविर्भवति।

$$
U^\dagger U = I  
$$

एकत्वं रक्षितम्।  
सम्भाव्यता-आयामाः संरक्षिताः।  
लेजर् स्थितः।

Not a state-parcel.  
Not faster than light.  
Not a copy.

The entangled pair becomes the bridge.  
Measurement destroys the original.  
Two classical bits describe the route.  
Bob performs the correction.  
The state reappears.

Unitarity is guarded.  
In the ideal protocol, Bob’s corrected state matches Alice’s original input state.  
The ledger remains.

---

### Closing Line

ॐ चित्-दूर-संक्रमणाय नमः।

Probability amplitudes do not fly as parcels.  
They reappear through correlation, correction, and receipt.

---

## अध्याय ३ · ग्रोवर्-अन्वेषण-सूत्रम् — Grover’s Search Algorithm

### Grover’s Search Algorithm Sutra

#### In Sanskrit Register

Status: Quantum advantage for unstructured search — pedagogical continuation of the क्वबिट्-सूत्राणि collection.  
Claim lane: Modern quantum algorithm expressed through Sanskrit-register terminology.  
Core promise: Given an unstructured search space of $N=2^n$ items with one marked solution, classical search uses $(N+1)/2$ oracle queries on average for a uniformly located target and up to $N$ in the worst case. Grover search uses $O(\sqrt{N})$ oracle queries.

This is a quadratic speedup.

---

### १. समस्या — The Search Problem

Let there be $N=2^n$ possible items.

Exactly one item is marked as the solution:

$$
|\omega\rangle  
$$

A classical search checks items one by one.  
On average, it needs:

$$
\frac{N+1}{2}  
$$

queries.

Grover’s algorithm uses quantum amplitude amplification and needs about:

$$
\frac{\pi}{4}\sqrt{N}  
$$

queries.

सूत्रम्:  
असंरचिते कोशे एकः चिह्नितः मार्गः अस्ति।  
शास्त्रीय-अन्वेषणं क्रमशः पश्यति।  
क्वान्टम्-अन्वेषणं आयामान् नर्तयति।

In an unstructured storehouse, one route is marked.  
Classical search checks one by one.  
Quantum search makes the amplitudes dance.

---

### २. प्रारम्भिक अवस्था — Initial State

Start with $n$ qubits in the all-zero state:

$$
|0\rangle^{\otimes n} =
|0\cdots 0\rangle  
$$

Apply Hadamard gates to all qubits:

$$
H^{\otimes n}|0\cdots 0\rangle  
$$

This creates the uniform superposition:

$$
|s\rangle =
H^{\otimes n}|0\cdots0\rangle =
\frac{1}{\sqrt{N}}  
\sum_{x=0}^{N-1}|x\rangle  
$$

Every possible item has equal amplitude.

सूत्रम्:  
सर्वे मार्गाः समभावेन उद्घाटिताः भवन्ति।

All routes are opened evenly.

Field gloss:  
सारा मेल्-रूट एक साथ मेज़ पर खुल गया।  
अभी कोई लिफ़ाफ़ा चुना नहीं गया — सब सम्भाव्य हैं।

The whole mail route is spread on the table at once.  
No envelope has been chosen yet — all are possible.

---

### ३. ओरेकल् — The Oracle / Marker

The oracle is a black-box unitary operation that recognizes the marked state.

It acts as:

$$
O|\omega\rangle = -|\omega\rangle  
$$

and for all non-solution states:

$$
O|x\rangle = |x\rangle  
\quad  
\text{when}  
\quad  
x \neq \omega  
$$

Equivalently:

$$
O|x\rangle =  
\begin{cases}  
-|x\rangle & \text{if } x=\omega \\  
|x\rangle & \text{if } x\neq\omega  
\end{cases}  
$$

The oracle does not directly announce the answer.  
It flips the phase of the marked state.

सूत्रम्:  
ओरेकल् उत्तरं न घोषयति।  
केवलं चिह्नित-मार्गस्य चिह्नं उलटति।

The oracle does not shout the answer.  
It only flips the sign of the marked route.

Field gloss:  
सही लिफ़ाफ़े पर अदृश्य उलटा-चिह्न लग गया।  
बाहर से कुछ नहीं दिखता।  
अन्दर से रूट बदल गया।

The correct envelope gets an invisible reversed mark.  
Outside, nothing obvious appears.  
Inside, the route has changed.

---

### ४. प्रसारण-प्रचालकः — Diffusion Operator

After the oracle flips the marked state’s phase, Grover applies the diffusion operator:

$$
D = 2|s\rangle\langle s| - I  
$$

This reflects the state about the average amplitude.

The diffusion operator increases the amplitude of the marked state and decreases the amplitudes of the unmarked states.

सूत्रम्:  
औसत-आयामे प्रतिबिम्बनं भवति।  
चिह्नित-मार्गस्य आयामः वर्धते।  
अन्येषां आयामाः हीयन्ते।

Reflection occurs about the average amplitude.  
The marked route’s amplitude grows.  
The others shrink.

Field gloss:  
पहले सही रूट पर उलटा निशान लगा।  
फिर पूरी मेज़ औसत के चारों ओर पलटी।  
अब सही लिफ़ाफ़ा थोड़ा ऊँचा दिखने लगा।

First the correct route gets flipped.  
Then the whole table reflects around the average.  
Now the correct envelope rises a little higher.

---

### ५. ग्रोवर्-चक्रम् — Grover Iteration

One Grover iteration is:

$$
G = DO  
$$

That is:

1. Oracle phase flip
    
2. Diffusion reflection
    

So:

$$
G = \left(2|s\rangle\langle s| - I\right)O  
$$

Each iteration amplifies the marked state’s probability amplitude.

सूत्रम्:  
ओरेकल् चिह्नं उलटति।  
प्रसारणः आयामं वर्धयति।  
चक्रम् लक्ष्यं निकटतरं करोति।

The oracle flips the sign.  
Diffusion amplifies the amplitude.  
Each cycle moves closer to the target.

---

### ६. ज्यामितीय-दर्शनम् — Geometric View

Grover’s algorithm can be seen in a two-dimensional plane.

This plane is spanned by:

$$
|\omega\rangle  
$$

the marked solution, and:

$$
|\alpha\rangle  
$$

the uniform superposition of all non-solutions.

Define:

$$
|\alpha\rangle =  
\frac{1}{\sqrt{N-1}}  
\sum_{x\neq \omega}|x\rangle  
$$

The starting state can be written as:

$$
|s\rangle =  
\cos\theta|\alpha\rangle  
+  
\sin\theta|\omega\rangle  
$$

where:

$$
\sin\theta = \frac{1}{\sqrt{N}}  
$$

The oracle reflects across the non-solution axis.  
The diffusion operator reflects across the starting state $|s\rangle$.  
Two reflections create a rotation.

Each Grover iteration rotates the state vector toward the marked solution by approximately:

$$
2\theta  
$$

सूत्रम्:  
द्वे प्रतिबिम्बने घूर्णनं जनयतः।  
घूर्णनं चित्-वेक्टरं समाधान-दिशि नयति।

Two reflections produce a rotation.  
The rotation carries the state-vector toward the solution.

Field gloss:  
यह खोज नहीं — दिशा-संशोधन है।  
हर चक्कर में सुई समाधान की तरफ़ मुड़ती है।

This is not ordinary searching — it is direction-correction.  
Each cycle turns the needle toward the answer.

---

### ७. आवर्तन-सङ्ख्या — Number of Iterations

After $k$ Grover iterations, the state is approximately:

$$
G^k|s\rangle =
\cos((2k+1)\theta)|\alpha\rangle  
+  
\sin((2k+1)\theta)|\omega\rangle  
$$

We want the marked-state amplitude to be near $1$:

$$
\sin((2k+1)\theta) \approx 1  
$$

This occurs when:

$$
(2k+1)\theta \approx \frac{\pi}{2}  
$$

Therefore:

$$
k \approx \frac{\pi}{4\theta}  
$$

Since:

$$
\theta \approx \frac{1}{\sqrt{N}}  
$$

the optimal number of iterations is:

$$
k \approx \frac{\pi}{4}\sqrt{N}  
$$

सूत्रम्:  
न अत्यल्पं चक्रम्।  
न अतिचक्रम्।  
समये स्थितं घूर्णनं फलाय भवति।

Not too few cycles.  
Not too many cycles.  
A correctly timed rotation produces the result.

Important note:  
If Grover iterations continue too long, the state rotates past the solution and the success probability falls again.

Field gloss:  
लक्ष्य तक घुमाओ।  
लक्ष्य के पार मत घुमाओ।  
वरना सही लिफ़ाफ़ा फिर नीचे चला जाएगा।

Rotate toward the target.  
Do not rotate past the target.  
Otherwise the correct envelope sinks again.

---

### ८. मापनम् — Measurement

After the optimal number of Grover iterations, measure the register.

The probability of obtaining the marked state is close to $1$:

$$
P(\omega) \approx 1  
$$

The final measurement collapses the quantum state to a classical answer:

$$
|\omega\rangle  
$$

सूत्रम्:  
आयामः पूर्वं वर्धितः।  
मापनम् अन्ते फलम् लिखति।

The amplitude is amplified first.  
Measurement writes the result at the end.

---

### ९. सम्बन्धः पूर्व-सूत्रैः — Relation to Earlier Sutras

Grover’s algorithm uses earlier quantum principles:

Hadamard gates create the initial superposition:

$$
H^{\otimes n}|0\cdots0\rangle = |s\rangle  
$$

The oracle uses phase flip:

$$
|\omega\rangle \mapsto -|\omega\rangle  
$$

The diffusion operator uses interference:

$$
D = 2|s\rangle\langle s| - I  
$$

Measurement extracts the final classical answer.

सूत्रम्:  
अध्यारोपणं सर्वमार्गान् उद्घाटयति।  
चिह्न-परिवर्तनं लक्ष्यं गुप्ततया सूचयति।  
व्यतिकरणं लक्ष्य-आयामं वर्धयति।  
मापनं फलम् लिखति।

Superposition opens all paths.  
Phase-flip secretly marks the target.  
Interference amplifies the target amplitude.  
Measurement writes the result.

---

### १०. न प्रतिलिपिः, न जादू — Not Copying, Not Magic

Grover’s algorithm does not inspect all answers and copy the right one.

It does not violate the No-Cloning Theorem.

It does not allow faster-than-light signalling.

It works by amplitude amplification: increasing the probability of the marked solution through carefully arranged interference.

सूत्रम्:  
न सर्वज्ञता।  
न प्रतिलिपिः।  
न जादू।  
केवलं आयाम-वर्धनम्।

Not omniscience.  
Not copying.  
Not magic.  
Only amplitude amplification.

---

### ११. लघु उदाहरणम् — Small Example

Suppose:

$$
N = 4  
$$

Then:

$$
\sqrt{N}=2  
$$

Classically, a uniformly located target requires on average:

$$
\frac{N+1}{2}=2.5  
$$

queries on average.

For this small instance, use the exact Grover angle rather than the asymptotic estimate:

$$
\theta=\arcsin\left(\frac{1}{\sqrt{4}}\right)=\frac{\pi}{6}.
$$

After one Grover iteration the marked-state angle is $3\theta=\pi/2$, so the ideal success probability is $1$.

For large $N$, the advantage becomes much more important.

Example:

$$
N = 1,000,000  
$$

Classical average search:

$$
500,000  
$$

Grover search:

$$
\frac{\pi}{4}\sqrt{1,000,000}  
\approx 785  
$$

Field gloss:  
पुरानी डाक में आधा शहर खंगालना पड़ता।  
ग्रोवर में शहर मुड़कर सही गली की तरफ़ इशारा करता है।

In old mail search, you may check half the city.  
In Grover search, the city folds toward the right street.

---

### १२. बहु-समाधान-स्थिति — Multiple Marked Solutions

If there are $M$ marked solutions instead of one, the speed becomes:

$$
O\left(\sqrt{\frac{N}{M}}\right)  
$$

The starting angle changes:

$$
\sin\theta = \sqrt{\frac{M}{N}}  
$$

If $M$ is unknown, the algorithm needs modifications, such as variable iteration counts or amplitude estimation.

सूत्रम्:  
यदि लक्ष्याणि बहूनि, चक्राणि न्यूनानि।  
यदि लक्ष्य-सङ्ख्या अज्ञाता, समयः परीक्षितव्यः।

If there are many targets, fewer cycles are needed.  
If the number of targets is unknown, the timing must be tested.

---

### १३. उपयोगाः — Uses

Grover’s algorithm is useful as a general amplitude-amplification primitive.

It can speed up unstructured search, brute-force-style checking, constraint satisfaction, and subroutines inside larger quantum algorithms.

But it gives a quadratic query-complexity speedup, not an exponential one. Building the oracle, loading data, and error-correcting the circuit can dominate an end-to-end application.

सूत्रम्:  
ग्रोवर् मार्गं संक्षिपति।  
सर्वथा जगत् न उलटति।

Grover shortens the path.  
It does not overturn the whole world.

---

### १४. प्रोटोकॉल-सारः — Protocol Summary

1. Prepare $n$ qubits in $|0\rangle^{\otimes n}$.
    
2. Apply Hadamard gates to create uniform superposition.
    
3. Use the oracle to phase-flip the marked state.
    
4. Apply the diffusion operator to amplify the marked amplitude.
    
5. Repeat approximately $\frac{\pi}{4}\sqrt{N}$ times.
    
6. Measure.
    
7. Obtain the marked solution with high probability.
    

सूत्रम्:  
सर्व-मार्गान् उद्घाटय।  
चिह्नित-मार्गस्य चिह्नम् उलट।  
औसत-आयामे प्रतिबिम्बनं कुरु।  
चक्रं पुनः पुनः कुरु।  
मापनं कृत्वा लक्ष्यं प्राप्नुहि।

Open all routes.  
Flip the sign of the marked route.  
Reflect about the average amplitude.  
Repeat the cycle.  
Measure and obtain the target.

---

### १५. सम्पूर्ण लघु-मन्त्रः — Compact Grover Mantra

सर्व-मार्गान् उद्घाटय।  
चिह्नित-मार्गस्य चिह्नम् उलट।  
औसत-आयामे प्रतिबिम्बनं कुरु।  
आयामं वर्धय।  
अलक्ष्य-मार्गान् क्षीणय।  
समये मापनं कुरु।

$$
k \approx \frac{\pi}{4}\sqrt{N}  
$$

$$
G = DO  
$$

$$
D = 2|s\rangle\langle s| - I  
$$

व्यतिकरणम् विजयते।  
लेजर् स्थितः।

Open all routes.  
Flip the sign of the marked route.  
Reflect around the average amplitude.  
Amplify the target.  
Diminish the non-targets.  
Measure at the right time.

Interference wins.  
The ledger remains.

---

### Closing Line

ॐ ग्रोवर्-अन्वेषणाय नमः।

Quadratic speedup be praised —  
the search space folds toward the marked route.

---

## अध्याय ४ · क्वान्टम्-त्रुटि-संशोधन-सूत्रम् — Quantum Error Correction (Shor & Surface Codes)

### Quantum Error Correction Sutra

#### Surface Code & Shor Code

#### In Sanskrit Register

Status: Protecting fragile quantum information — essential for scalable quantum computing.  
Claim lane: Modern quantum error correction expressed through Sanskrit-register terminology.  
Core insight: Physical qubits are noisy and fragile. Logical qubits survive by spreading information across many physical qubits, measuring error syndromes, and correcting errors without directly measuring or destroying the encoded quantum state.

---

### १. किमर्थम् आवश्यकम्? — Why Error Correction Is Needed

A qubit is fragile.

Errors arise from interaction with the environment, imperfect gates, heat, vibration, control noise, and unwanted coupling.

Common error types include:

$$
X  
$$

bit-flip error,

$$
Z  
$$

phase-flip error,

$$
Y = iXZ  
$$

combined bit-and-phase error,

as well as amplitude damping, dephasing, leakage, and measurement error.

Classical repetition codes protect classical bits by copying them.  
But quantum states cannot simply be copied, because of the No-Cloning Theorem:

$$
|\psi\rangle \otimes |0\rangle  
\not\rightarrow  
|\psi\rangle \otimes |\psi\rangle  
$$

Therefore, quantum error correction cannot be simple copying.

It must use:

1. Redundant encoding
    
2. Ancilla qubits
    
3. Syndrome measurement
    
4. Classical decoding
    
5. Corrective operations
    

सूत्रम्:  
क्वबिट् मृदुः अस्ति।  
शोरः तं कम्पयति।  
प्रतिलिपिः निषिद्धा।  
सिन्ड्रोम-मापनं मार्गं दर्शयति।

The qubit is soft.  
Noise shakes it.  
Copying is forbidden.  
Syndrome measurement shows the route.

---

### २. सिन्ड्रोम-मापनम् — Syndrome Measurement

The key trick is to detect the error without measuring the logical quantum information itself.

A syndrome is an error-signature.

It tells us what kind of error happened and where, without revealing the encoded state.

सूत्रम्:  
दोषं पश्य।  
चित् न पश्य।  
लक्षणं मापय।  
तार्किक-अवस्थां मा भिन्दि।

See the defect.  
Do not look at the state.  
Measure the symptom.  
Do not break the logical state.

Field gloss:  
लिफ़ाफ़े का पता मत पढ़।  
बस देख कि कोना मुड़ा है या टिकट उलटा है।  
चिट्ठी बची रहे — यही खेल है।

Do not read the letter.  
Only check whether the corner is bent or the stamp is upside down.  
The message must survive — that is the game.

---

### ३. शोर्-कोडः — Shor Code

The Shor code encodes one logical qubit into nine physical qubits.

It protects against an arbitrary single-qubit error.

A general logical qubit is:

$$
|\psi_L\rangle =  
\alpha |0_L\rangle +  
\beta |1_L\rangle  
$$

The Shor code uses two layers of protection:

1. Phase-flip protection
    
2. Bit-flip protection
    

Logical states may be written as:

$$
|0_L\rangle =  
\frac{1}{\sqrt{8}}  
\left(  
|000\rangle + |111\rangle  
\right)^{\otimes 3}  
$$

$$
|1_L\rangle =  
\frac{1}{\sqrt{8}}  
\left(  
|000\rangle - |111\rangle  
\right)^{\otimes 3}  
$$

These states distribute the logical information across nine physical qubits.

A single local error damages only part of the encoded structure, and syndrome measurements identify how to repair it.

सूत्रम्:  
एकं तार्किक-क्वबिट् नवभिः भौतिक-क्वबिटैः रक्षितम्।  
दोषः स्थानीयः भवति।  
चित् विस्तीर्णा भवति।  
सिन्ड्रोमः चिकित्सकः भवति।

One logical qubit is protected by nine physical qubits.  
The error is local.  
The state is spread out.  
The syndrome becomes the physician.

---

### ४. शोर्-कोड्-संशोधन-क्रमः — Shor Code Correction Steps

The correction process is:

1. Measure stabilizer syndromes using ancilla qubits.
    
2. Detect bit-flip errors through $Z$-type parity checks.
    
3. Detect phase-flip errors through $X$-type parity checks.
    
4. Use the syndrome pattern to identify the error.
    
5. Apply the corrective Pauli operation.
    

For example:

$$
X  
$$

corrects a bit-flip error,

$$
Z  
$$

corrects a phase-flip error,

and

$$
Y  
$$

corresponds to both bit and phase flip.

The Shor code can correct any single-qubit error because arbitrary single-qubit errors can be decomposed into Pauli-error components.

सूत्रम्:  
X-दोषः दृश्यते।  
Z-दोषः दृश्यते।  
Y-दोषः द्विरूपः।  
पॉली-संशोधनं पुनः समत्वं करोति।

The $X$-error is seen.  
The $Z$-error is seen.  
The $Y$-error has two forms.  
Pauli correction restores balance.

Field gloss:  
एक क्वबिट् फिसला।  
पूरी टोली नहीं टूटी।  
सिन्ड्रोम बोला: “यहीं सुधारो।”  
लेजर् बच गया।

One qubit slipped.  
The whole crew did not break.  
The syndrome said: “Fix it here.”  
The ledger survived.

---

### ५. स्थिरकाः — Stabilizers

Quantum error-correcting codes are often described using stabilizers.

A stabilizer is an operator that leaves the valid code state unchanged.

If:

$$
S|\psi_L\rangle = |\psi_L\rangle  
$$

then $S$ stabilizes the logical state.

If measurement of a stabilizer gives an unexpected sign, such as:

$$
-1  
$$

then an error has occurred.

सूत्रम्:  
स्थिरकः पृच्छति — “अवस्था यथावत् अस्ति वा?”  
उत्तरं सम्यक् चेत् शान्तिः।  
उत्तरं विपरीतम् चेत् दोषः।

The stabilizer asks: “Is the state still as it should be?”  
If the answer is correct, there is peace.  
If the answer flips, there is an error.

---

### ६. सर्फेस्-कोडः — Surface Code

The surface code is a leading architecture for fault-tolerant quantum computing.

It encodes logical qubits into a two-dimensional lattice of many physical qubits.

The lattice contains:

1. Data qubits
    
2. Measurement qubits
    
3. $X$-type stabilizers
    
4. $Z$-type stabilizers
    

Errors create syndrome patterns on the lattice.

The correction problem becomes a classical decoding problem: infer the most likely error chain from the observed syndrome pattern.

सूत्रम्:  
द्वि-आयामी-जाले चित् गुप्तम्।  
स्थानीय-मापनैः दोष-चिह्नानि दृश्यन्ते।  
तार्किक-अवस्था दूरस्थ-रूपेण रक्षिता।

In a two-dimensional net, the state is hidden.  
Local measurements reveal error marks.  
The logical state is protected non-locally.

Field gloss:  
चित् अब अकेले घर में नहीं रहता।  
पूरा मोहल्ला उसका सुरक्षा-जाल है।  
गलती गली में दिखती है; संदेश शहर में बचता है।

The state no longer lives alone in one house.  
The whole neighborhood becomes its security net.  
The mistake appears in the street; the message survives in the city.

---

### ७. सर्फेस्-कोड्-स्थिरकाः — Surface Code Stabilizers

Surface code checks are local parity checks.

A $Z$-type stabilizer detects bit-flip-like errors:

$$
Z \otimes Z \otimes Z \otimes Z  
$$

An $X$-type stabilizer detects phase-flip-like errors:

$$
X \otimes X \otimes X \otimes X  
$$

In practice, measurement qubits interact with nearby data qubits, gather parity information, and are then measured.

The logical information is not directly measured.

Only syndrome information is extracted.

सूत्रम्:  
निकट-क्वबिटानां समता मीयते।  
दोषलक्षणं लभ्यते।  
चित् रहस्यं न उद्घाट्यते।

The parity of nearby qubits is measured.  
The error symptom is obtained.  
The secret of the state is not revealed.

---

### ८. दोष-श्रृंखला — Error Chains

In the surface code, errors often appear as chains on the lattice.

The endpoints of these chains create syndrome events.

A decoder tries to infer the most likely chain that caused the observed endpoints.

One common decoding method is minimum-weight perfect matching.

सूत्रम्:  
दोषः रेखामार्गेण चरति।  
अन्तबिन्दवः लक्षणानि भवन्ति।  
विवेचकः न्यूनतम-भार-मार्गं चिनोति।

The error travels as a line.  
The endpoints become symptoms.  
The decoder chooses the least-weight path.

Field gloss:  
बिल्ली ने डाक-घर में पंजे के निशान छोड़े।  
तुम हर पंजा नहीं देखते।  
बस निशान जोड़कर समझते हो — बिल्ली किधर गई।

The cat left pawprints in the post office.  
You do not see every step.  
You connect the marks and infer where the cat went.

---

### ९. सीमा-सिद्धान्तः — Threshold Theorem

The threshold idea is central to fault-tolerant quantum computing.

If the physical error rate is below a threshold value,

$$
p < p_{\text{threshold}}  
$$

then increasing the code size can make the logical error rate much smaller.

For the surface code, this threshold is often roughly around the percent level, depending on the exact noise model, hardware, and decoding method.

सूत्रम्:  
यदि भौतिक-दोषः सीमातः अधः अस्ति,  
तर्हि कोड्-विस्तारः तार्किक-दोषं क्षीणयति।

If the physical error rate is below threshold,  
then expanding the code suppresses logical error.

Field gloss:  
यदि बारिश बहुत पागल नहीं है,  
तो बड़ा छाता काम करता है।  
छाता बढ़ाओ; चिट्ठी सूखी रहती है।

If the rain is not too insane,  
a bigger umbrella works.  
Make the umbrella larger; the letter stays dry.

---

### १०. तार्किक-क्वबिट् — Logical Qubit

A logical qubit is not a single physical object.

It is an encoded state distributed across many physical qubits.

Physical qubits fail often.  
Logical qubits are designed to fail rarely.

$$
|\psi_L\rangle =  
\alpha |0_L\rangle +  
\beta |1_L\rangle  
$$

सूत्रम्:  
भौतिक-क्वबिट् कम्पते।  
तार्किक-क्वबिट् समुदायेन तिष्ठति।

The physical qubit trembles.  
The logical qubit stands through community.

Field gloss:  
एक बंदा गिरा तो रास्ता बंद नहीं।  
पूरा मोहल्ला रूट पकड़े हुए है।

If one guy falls, the route is not closed.  
The whole neighborhood is holding the route.

---

### ११. फॉल्ट्-टॉलरन्स् — Fault Tolerance

Fault-tolerant computation means the computer can continue operating even while errors occur.

This requires:

1. Error-corrected memory
    
2. Fault-tolerant gates
    
3. Repeated syndrome extraction
    
4. Decoding
    
5. State preparation
    
6. Measurement protection
    

Some logical gates can be implemented transversally.  
Others require special methods, such as magic-state distillation.

सूत्रम्:  
दोषाः आगच्छन्ति।  
गणना न निवर्तते।  
रक्षा निरन्तरा भवति।

Errors come.  
Computation does not stop.  
Protection continues.

---

### १२. मैजिक्-स्टेट्-डिस्टिलेशनम् — Magic State Distillation

Many protected operations are Clifford operations.

But universal quantum computation also needs non-Clifford gates, such as the $T$ gate.

These are often supplied through magic states.

Noisy magic states are purified through distillation.

$$
\text{noisy magic states}  
\longrightarrow  
\text{fewer cleaner magic states}  
$$

सूत्रम्:  
अशुद्ध-विशेषावस्थाः संगृह्यन्ते।  
संस्कारैः स्वच्छतराः भवन्ति।  
ततः सार्वत्रिक-गणना सम्पूर्णा भवति।

Noisy special states are gathered.  
Through refinement, cleaner ones arise.  
Then universal computation becomes complete.

Field gloss:  
कच्ची जादू-टिकटें आती हैं।  
कई मिलाकर एक साफ़ टिकट बनती है।  
तभी गेट खुलता है।

Raw magic tickets arrive.  
Many are combined into one clean ticket.  
Then the gate opens.

---

### १३. सम्बन्धः पूर्व-सूत्रैः — Relation to Earlier Sutras

Quantum error correction connects the previous sutras.

Teleportation can use encoded qubits for reliable transfer.

Grover’s algorithm benefits from protected coherent states.

Shor’s factoring algorithm requires fault-tolerant logical qubits at useful scale.

Density matrices describe decoherence and mixed states when noise enters.

Syndrome measurement protects information without fully revealing it.

सूत्रम्:  
दूर-प्रेषणं रक्षणं इच्छति।  
अन्वेषणं दीर्घ-चित् इच्छति।  
कारक-विभाजनं विशाल-कोड् इच्छति।  
घनत्व-मात्रिका शोरस्य लेखा ददाति।

Teleportation wants protection.  
Search wants long-lived coherence.  
Factoring wants large codes.  
The density matrix gives the ledger of noise.

---

### १४. सामान्य-सिद्धान्ताः — General Principles

Quantum error correction depends on four ideas:

1. Encode one logical state into many physical qubits.
    
2. Measure stabilizers to obtain error syndromes.
    
3. Decode the syndrome using classical computation.
    
4. Correct the inferred error while preserving the logical state.
    

सूत्रम्:  
विस्तारः रक्षा।  
सिन्ड्रोमः सूचना।  
विवेचनं निर्णयः।  
संशोधनं पुनर्स्थापनम्।

Encoding is protection.  
Syndrome is information.  
Decoding is decision.  
Correction is restoration.

---

### १५. लघु-मन्त्रः — Error Correction Mantra

त्रुटिः आगच्छति।  
सिन्ड्रोमं मापय।  
तार्किक-अवस्थां मा स्पृश।  
दोष-लक्षणं पठ।  
पॉली-संशोधनं कुरु।

यदि:

$$
p < p_{\text{threshold}}  
$$

तर्हि:

$$
\text{logical error} \rightarrow \text{smaller with code distance}  
$$

शोरः कम्पति।  
कोड् रक्षति।  
व्यतिकरणं जीवति।  
लेजर् स्थितः।

Error comes.  
Measure the syndrome.  
Do not touch the logical state.  
Read the error symptom.  
Apply Pauli correction.

If the error rate is below threshold,  
logical error becomes smaller with code distance.

Noise trembles.  
The code protects.  
Interference lives.  
The ledger remains.

---

### Closing Line

ॐ क्वान्टम्-त्रुटि-रक्षणाय नमः।

Fragile amplitudes are protected by redundancy, syndrome, decoding, and topology.

---

## अध्याय ५ · क्वान्टम्-फेज्-एस्टिमेशन-सूत्रम् — Phase Estimation & Variational Algorithms

### Quantum Phase Estimation & Variational Algorithms Sutra

#### In Sanskrit Register

Status: From exact quantum primitives to practical hybrid algorithms — continuation of क्वबिट्-सूत्राणि.  
Claim lane: Modern quantum algorithms expressed through Sanskrit-register terminology.  
Core insight: Quantum Phase Estimation estimates an eigenphase of a unitary. Variational quantum algorithms combine parameterized quantum circuits with classical optimization to seek approximate solutions; practical advantage remains problem- and hardware-dependent.

---

### १. क्वान्टम्-फेज्-एस्टिमेशनम् — Quantum Phase Estimation

Quantum Phase Estimation, or QPE, estimates the phase associated with an eigenvalue of a unitary operator.

Suppose a unitary operator $U$ has an eigenvector $|\psi\rangle$:

$$
U|\psi\rangle = e^{2\pi i \phi}|\psi\rangle  
$$

where:

$$
0 \leq \phi < 1  
$$

The goal of QPE is to estimate:

$$
\phi  
$$

the hidden phase.

सूत्रम्:  
यूनिटरी-प्रचालकः चित्-वेक्टरं घूर्णयति।  
फेज् तस्य गुप्त-कोणः।  
क्वान्टम्-फेज्-एस्टिमेशनं तं कोणं मापयति।

A unitary operator rotates the state-vector.  
The phase is its hidden angle.  
Quantum Phase Estimation measures that angle.

---

### २. किमर्थम् महत्त्वपूर्णम्? — Why QPE Matters

Quantum Phase Estimation is a core subroutine in several major quantum algorithms.

It appears in:

1. Shor’s algorithm, where order-finding can be expressed through phase estimation
    
2. Quantum simulation
    
3. Hamiltonian eigenvalue estimation
    
4. Quantum chemistry
    
5. Quantum linear systems
    
6. Fault-tolerant quantum algorithms
    

QPE is powerful, but it usually requires deep circuits and high-quality error-corrected qubits.

सूत्रम्:  
फेज् ज्ञाते, क्रमः ज्ञायते।  
क्रमे ज्ञाते, कारकाः ज्ञायन्ते।  
एवं शोर्-अल्गोरिद्मस्य हृदयम् उद्घाटते।

When the phase is known, the period can be known.  
When the period is known, factors can be found.  
Thus the heart of Shor’s algorithm opens.

---

### ३. QPE-प्रोटोकॉलः — QPE Protocol

QPE uses two registers.

The first register has $t$ ancilla qubits for precision:

$$
|0\rangle^{\otimes t}  
$$

The second register contains an eigenvector of $U$:

$$
|\psi\rangle  
$$

The initial state is:

$$
|0\rangle^{\otimes t}|\psi\rangle  
$$

Apply Hadamard gates to the first register:

$$
H^{\otimes t}|0\rangle^{\otimes t} =
\frac{1}{\sqrt{2^t}}  
\sum_{k=0}^{2^t-1}|k\rangle  
$$

So the full state becomes:

$$
\frac{1}{\sqrt{2^t}}  
\sum_{k=0}^{2^t-1}|k\rangle|\psi\rangle  
$$

Now apply controlled powers of $U$:

$$
U^k  
$$

This gives:

$$
\frac{1}{\sqrt{2^t}}  
\sum_{k=0}^{2^t-1}|k\rangle U^k|\psi\rangle  
$$

Since:

$$
U|\psi\rangle = e^{2\pi i\phi}|\psi\rangle  
$$

we have:

$$
U^k|\psi\rangle =  
e^{2\pi i k\phi}|\psi\rangle  
$$

Therefore:

$$
\frac{1}{\sqrt{2^t}}  
\sum_{k=0}^{2^t-1}  
e^{2\pi i k\phi}  
|k\rangle|\psi\rangle  
$$

The phase has now been written into the amplitudes of the first register.

Next, apply the inverse Quantum Fourier Transform:

$$
QFT^{-1}  
$$

to the first register.

Then measure the first register.

The measured bit string gives an estimate of:

$$
\phi  
$$

सूत्रम्:  
Hadamard सर्व-घातान् उद्घाटयति।  
Controlled-$U^k$ फेजं आयामेषु लिखति।  
$QFT^{-1}$ गुप्त-कोणं सङ्ख्यायां परिवर्तयति।  
मापनं फलम् लिखति।

Hadamard opens all powers.  
Controlled-$U^k$ writes the phase into amplitudes.  
The inverse QFT converts the hidden angle into a number.  
Measurement writes the result.

---

### ४. QPE-मानचित्रम् — QPE Map

The essence is:

$$
U|\psi\rangle = e^{2\pi i\phi}|\psi\rangle  
$$

then:

$$
\frac{1}{\sqrt{2^t}}
\sum_{k=0}^{2^t-1}|k\rangle U^k|\psi\rangle =
\frac{1}{\sqrt{2^t}}  
\sum_{k=0}^{2^t-1}  
e^{2\pi i k\phi}  
|k\rangle|\psi\rangle  
$$

and:

$$
QFT^{-1}  
$$

turns the phase pattern into a measurable estimate of $\phi$.

Field gloss:  
यूनिटरी के भीतर एक छिपा कोण है।  
QPE उसे सीधे नहीं पकड़ता।  
पहले कोण को तरंगों में लिखता है।  
फिर QFT से उसे संख्या में बदलता है।

There is a hidden angle inside the unitary.  
QPE does not grab it directly.  
First it writes the angle into waves.  
Then QFT turns it into a number.

---

### ५. वैरिएशनल्-क्वान्टम्-अल्गोरिद्माः — Variational Quantum Algorithms

Variational Quantum Algorithms, or VQAs, are hybrid quantum-classical algorithms.

They are especially important in the NISQ era: noisy intermediate-scale quantum devices.

Instead of requiring one huge, perfect, fault-tolerant quantum circuit, VQAs use a repeated loop:

1. Prepare a parameterized quantum state
    
2. Measure a cost function
    
3. Send the result to a classical optimizer
    
4. Update the parameters
    
5. Repeat
    

सूत्रम्:  
क्वान्टम्-यन्त्रं अवस्थां जनयति।  
शास्त्रीय-यन्त्रं मानं सुधारयति।  
उभयोः सहयोगेन न्यूनतमं खोज्यते।

The quantum machine prepares the state.  
The classical machine adjusts the parameters.  
Together, they search for the minimum.

---

### ६. VQE — Variational Quantum Eigensolver

The most famous VQA is the Variational Quantum Eigensolver, or VQE.

Its goal is to estimate the ground-state energy of a Hamiltonian:

$$
H  
$$

For example, $H$ may describe a molecule.

Prepare a parameterized quantum state:

$$
|\psi(\theta)\rangle  
$$

where $\theta$ is a set of tunable parameters.

Measure the expectation value:

$$
E(\theta) =
\langle \psi(\theta)|H|\psi(\theta)\rangle  
$$

The goal is to minimize:

$$
E(\theta)  
$$

So:

$$
E_{\mathrm{VQE}}
:=
\min_{\theta}
\langle \psi(\theta)|H|\psi(\theta)\rangle
\ge E_0
$$

Equality requires an ansatz capable of representing a ground state and successful optimization; sampling and hardware errors add further uncertainty. The quantum processor estimates $E(\theta)$, and the classical optimizer updates $\theta$.

सूत्रम्:  
अवस्था $|\psi(\theta)\rangle$ निर्मीयते।  
ऊर्जा $\langle H\rangle$ मीयते।  
$\theta$ पुनः पुनः संशोधितः भवति।  
न्यूनतम-ऊर्जा लक्ष्यं भवति।

The state $|\psi(\theta)\rangle$ is prepared.  
Energy $\langle H\rangle$ is measured.  
The parameters $\theta$ are updated again and again.  
The lowest energy is the target.

---

### ७. हैमिल्टनियन्-मापनम् — Measuring the Hamiltonian

In practice, the Hamiltonian is decomposed into Pauli strings:

$$
H = \sum_j c_j P_j  
$$

where each $P_j$ is a tensor product of Pauli operators:

$$
I,\quad X,\quad Y,\quad Z  
$$

Then:

$$
E(\theta) =
\sum_j c_j  
\langle \psi(\theta)|P_j|\psi(\theta)\rangle  
$$

Each Pauli term is measured on the quantum device.  
The weighted sum gives the energy estimate.

सूत्रम्:  
हैमिल्टनियनं पॉली-सूत्रेषु विभज।  
प्रत्येकं पदं मापय।  
भारित-योगेन ऊर्जा लभ्यते।

Split the Hamiltonian into Pauli strings.  
Measure each term.  
The weighted sum gives the energy.

Field gloss:  
पूरी इमारत एक बार में मत तौल।  
ईंट-ईंट का वजन लो।  
फिर कुल वजन जोड़ो।

Do not weigh the whole building at once.  
Weigh each brick.  
Then add the total.

---

### ८. आन्साट्ज् — Ansatz

The ansatz is the parameterized circuit used to prepare:

$$
|\psi(\theta)\rangle  
$$

Examples include:

1. Hardware-efficient ansatz
    
2. Chemistry-inspired ansatz
    
3. UCCSD-style ansatz
    
4. Problem-specific ansatz
    

A good ansatz explores useful states efficiently.  
A bad ansatz wastes parameters or becomes hard to train.

सूत्रम्:  
आन्साट्ज् मार्ग-परिवारः।  
सत्यम् तत्र निश्चयेन नास्ति।  
परन्तु समीपं गन्तुं मार्गः अस्ति।

The ansatz is a family of routes.  
The truth is not guaranteed to be inside it.  
But it may provide a path nearby.

---

### ९. क्लासिकल्-ऑप्टिमाइजर् — Classical Optimizer

The classical optimizer updates the parameters:

$$
\theta  
$$

It tries to reduce:

$$
E(\theta)  
$$

Possible optimizers include gradient descent, SPSA, COBYLA, Nelder-Mead, and other numerical methods.

The loop is:

$$
\theta  
\rightarrow  
|\psi(\theta)\rangle  
\rightarrow  
E(\theta)  
\rightarrow  
\theta'  
$$

सूत्रम्:  
मानं स्थापय।  
ऊर्जा मापय।  
दिशां सुधारय।  
पुनः प्रयत्नं कुरु।

Set the parameters.  
Measure the energy.  
Adjust the direction.  
Try again.

Field gloss:  
क्वान्टम् हिस्सा खाना पकाता है।  
क्लासिकल् हिस्सा चखकर मसाला बदलता है।  
फिर वही चक्र चलता है।

The quantum part cooks the dish.  
The classical part tastes it and changes the seasoning.  
Then the loop continues.

---

### १०. QAOA — Quantum Approximate Optimization Algorithm

Another major VQA is QAOA.

QAOA is used for combinatorial optimization problems.

It alternates between two kinds of operations:

1. Cost Hamiltonian evolution
    
2. Mixer Hamiltonian evolution
    

A common form is:

$$
|\gamma,\beta\rangle =
\prod_{j=1}^{p}  
e^{-i\beta_j H_M}  
e^{-i\gamma_j H_C}  
|s\rangle  
$$

where:

$$
H_C  
$$

encodes the problem cost, and:

$$
H_M  
$$

mixes the state between candidate solutions.

The parameters are:

$$
\gamma_j,\beta_j  
$$

The classical optimizer adjusts them.

सूत्रम्:  
समस्या-हैमिल्टनियनं दिशा ददाति।  
मिक्सर्-हैमिल्टनियनं मार्गान् चलायति।  
परामितयः फलम् सुधारयन्ति।

The cost Hamiltonian gives direction.  
The mixer Hamiltonian moves among routes.  
The parameters improve the result.

---

### ११. VQA-सामर्थ्यम् — Strengths of VQAs

Variational algorithms are attractive because they can use shallower circuits than QPE.

They are more compatible with noisy quantum hardware.

They allow hybrid workflows where the quantum processor handles state preparation and measurement, while the classical processor handles optimization.

सूत्रम्:  
दीर्घ-सर्किट् न आवश्यकम्।  
शोरयुक्ते यन्त्रे अपि प्रयोगः सम्भवः।  
क्वान्टम्-क्लासिकल्-सहयोगः मार्गं खोलति।

A deep circuit is not always required.  
Even noisy machines may be used.  
Quantum-classical cooperation opens the route.

---

### १२. VQA-दौर्बल्यानि — Limitations of VQAs

VQAs are not magic.

They can suffer from:

1. Barren plateaus
    
2. Vanishing gradients
    
3. Poor ansatz choice
    
4. Measurement overhead
    
5. Noise sensitivity
    
6. Local minima
    
7. Expensive optimization loops
    

A barren plateau occurs when gradients become extremely small, making training difficult.

सूत्रम्:  
परामिति-वनं विस्तीर्णम्।  
क्वचित् ढलानं न दृश्यते।  
ऑप्टिमाइजर् अन्धः भ्रमति।

The parameter forest is vast.  
Sometimes no slope is visible.  
The optimizer wanders blind.

Field gloss:  
तुम मसाला बदलते रहते हो।  
लेकिन जीभ को फर्क ही नहीं पड़ता।  
अब रसोई हँस रही है।

You keep changing the seasoning.  
But the tongue cannot tell the difference.  
Now the kitchen is laughing.

---

### १३. QPE बनाम VQA — Comparison

| Aspect | QPE | VQA / VQE |
|---|---|---|
|Main goal|Estimate eigenphase/eigenvalue|Minimize a cost or energy|
|Style|Mostly quantum|Hybrid quantum-classical|
|Circuit depth|Deep|Shallower|
|Hardware need|Usually fault-tolerant for high precision|Designed for shallower experiments; advantage not assured|
|Output|High-precision phase/eigenvalue|Approximate optimized value|
|Core tool|Controlled-$U^k$ and inverse QFT|Ansatz, measurement, optimizer|
|Example use|Shor’s algorithm, simulation|Chemistry, optimization|

सूत्रम्:  
QPE गुप्त-फेजं प्रकाशयति।  
VQA परामितीन् सुधारयति।  
एकः गहनः।  
अन्यः सहयोगात्मकः।

QPE reveals the hidden phase.  
VQA improves parameters.  
One is deep.  
The other is collaborative.

---

### १४. सम्बन्धः पूर्व-सूत्रैः — Relation to Earlier Sutras

QPE uses:

$$
U^\dagger U = I  
$$

unitarity,

$$
QFT^{-1}  
$$

Fourier structure,

and controlled unitary powers:

$$
U^k  
$$

VQA uses:

$$
|\psi(\theta)\rangle  
$$

parameterized states,

$$
\langle H\rangle  
$$

expectation values,

and repeated measurement.

QPE points toward Shor’s algorithm and fault-tolerant quantum computation.

VQA points toward NISQ-era experiments, chemistry, and optimization.

सूत्रम्:  
QPE फेजस्य लेखा पठति।  
VQA ऊर्जायाः लेखा न्यूनयति।  
उभे क्वान्टम्-मार्गौ।  
उभयोः लेखा भिन्ना।

QPE reads the ledger of phase.  
VQA lowers the ledger of energy.  
Both are quantum routes.  
Their receipts differ.

---

### १५. सम्पूर्ण लघु-मन्त्रः — Compact Mantra

फेज्-एस्टिमेशनम्:

$$
U|\psi\rangle = e^{2\pi i\phi}|\psi\rangle  
$$

$$
\text{Controlled-}U^k + QFT^{-1}  
\longrightarrow  
\phi  
$$

वैरिएशनल्-अल्गोरिद्मः:

$$
|\psi(\theta)\rangle  
$$

$$
E(\theta)=  
\langle \psi(\theta)|H|\psi(\theta)\rangle  
$$

$$
\theta \rightarrow \theta'  
$$

फेज् गुप्तः।  
QPE तं प्रकाशयति।

ऊर्जा माप्या।  
VQA तां न्यूनयति।

क्वान्टम् यन्त्रं मापयति।  
शास्त्रीय यन्त्रं सुधारयति।  
सहयोगेन फलम् आगच्छति।

The phase is hidden.  
QPE reveals it.

Energy is measured.  
VQA lowers it.

The quantum machine measures.  
The classical machine improves.  
Through cooperation, the result appears.

---

### Closing Line

ॐ क्वान्टम्-फेज्-वैरिएशनल्-सहयोगाय नमः।

Phases are estimated.  
Energies are variationally minimized.  
The quantum and classical ledgers shake hands.

---

## अध्याय ६ · बीबी-८४-सूत्रम् — Quantum Cryptography: BB84

### Quantum Cryptography — BB84 Protocol Sutra

#### In Sanskrit Register

Status: Secure key distribution using quantum principles — continuation of क्वबिट्-सूत्राणि.  
Claim lane: Modern quantum key distribution expressed through Sanskrit-register terminology.  
Core insight: Alice and Bob can generate a shared secret key by transmitting quantum states and comparing bases over an authenticated public classical channel. The observed error statistics bound what an adversary may know; noise can also cause errors, and the protocol may abort.

BB84 does not directly encrypt a message.  
It distributes a secret key.  
That key can then be used for secure communication.

---

### १. मूल-सिद्धान्ताः — Basic Principles

BB84 uses qubits, often represented by photon polarization states.

It uses two conjugate bases.

The rectilinear basis:

$$
+  
$$

contains:

$$
|0\rangle  
$$

and:

$$
|1\rangle  
$$

The diagonal basis:

$$
\times  
$$

contains:

$$
|+\rangle =  
\frac{|0\rangle + |1\rangle}{\sqrt{2}}  
$$

and:

$$
|-\rangle =  
\frac{|0\rangle - |1\rangle}{\sqrt{2}}  
$$

These bases are incompatible.

If a qubit is prepared in one basis and measured in the other, the result becomes random.

सूत्रम्:  
द्वौ आधारौ स्तः।  
एकः सीधा।  
अन्यः तिर्यक्।  
एकेन निर्मितं चित् अन्येन मीयते चेत् अनिश्चितता जायते।

There are two bases.  
One is straight.  
The other is diagonal.  
If a state prepared in one is measured in the other, uncertainty appears.

---

### २. सुरक्षा-बीजम् — Seed of Security

BB84 relies on two quantum facts:

1. Measurement can disturb an unknown quantum state.
    
2. An unknown quantum state cannot be copied perfectly.
    

The No-Cloning Theorem says:

$$
|\psi\rangle \otimes |0\rangle  
\not\rightarrow  
|\psi\rangle \otimes |\psi\rangle  
$$

Eve cannot simply copy each qubit, store the copy, and wait until Alice and Bob reveal their bases.

सूत्रम्:  
अज्ञातं चित् न प्रतिलिप्यते।  
मापनं स्पर्शः भवति।  
स्पर्शः चिह्नं त्यजति।

An unknown state cannot be copied.  
Measurement is a touch.  
Touch leaves a mark.

Field gloss:  
ईव लिफ़ाफ़ा खोलना चाहती है।  
पर क्वान्टम् लिफ़ाफ़ा खुलते ही मुड़ जाता है।  
अब आलिस् और बॉब देखते हैं — “किसने छुआ?”

Eve wants to open the envelope.  
An intercept-resend attack changes some statistics.  
Alice and Bob test whether the observed error rate is compatible with continuing securely.

---

### ३. आलिस्-तैयारी — Alice’s Preparation

Alice randomly chooses a classical bit:

$$
0 \quad \text{or} \quad 1  
$$

She also randomly chooses a basis:

$$
+ \quad \text{or} \quad \times  
$$
    

Then she prepares and sends the corresponding quantum state.

Example encoding:

| Alice’s bit | Alice’s basis | Sent state |
|---:|:---:|:---|
| 0 | $Z$ (`+`) | $\lvert 0\rangle$ |
| 1 | $Z$ (`+`) | $\lvert 1\rangle$ |
| 0 | $X$ (`×`) | $\lvert +\rangle$ |
| 1 | $X$ (`×`) | $\lvert -\rangle$ |

सूत्रम्:  
आलिस् यादृच्छिकं बिट् चिनोति।  
यादृच्छिकम् आधारं चिनोति।  
ततः क्वबिट् प्रेषयति।

Alice chooses a random bit.  
Alice chooses a random basis.  
Then she sends the qubit.

---

### ४. बॉब-मापनम् — Bob’s Measurement

For each incoming qubit, Bob randomly chooses a measurement basis:

$$
+ \quad \text{or} \quad \times  
$$
    

He measures and records the result.

If Bob chooses the same basis as Alice, he should obtain the same bit, assuming no noise or eavesdropping.

If Bob chooses the wrong basis, his result is random.

सूत्रम्:  
बॉब अपि आधारं यादृच्छिकतया चिनोति।  
समे आधारे सत्यं दृश्यते।  
भिन्ने आधारे फलम् अनिश्चितं भवति।

Bob also chooses a basis randomly.  
In the same basis, the truth is seen.  
In the wrong basis, the result becomes uncertain.

---

### ५. आधार-मेलनम् — Basis Reconciliation

After transmission, Alice and Bob communicate over an authenticated public classical channel.

They do not reveal the bit values.

They reveal only which bases they used.

Then they keep only the positions where their bases matched.

This process is called sifting.

Roughly half of the transmitted qubits survive the basis comparison.

These remaining bits form the raw key.

सूत्रम्:  
आधाराः सार्वजनिकतया कथ्यन्ते।  
बिट्-मूल्यानि न कथ्यन्ते।  
यत्र आधारौ समौ, तत्र बिट् रक्ष्यते।  
अन्यत्र त्यज्यते।

The bases are announced publicly.  
The bit values are not announced.  
Where the bases match, the bit is kept.  
Where they differ, it is discarded.

Field gloss:  
आलिस् और बॉब कहते हैं:  
“मैंने किस चश्मे से देखा?”  
पर वे यह नहीं कहते:  
“मैंने क्या देखा?”

Alice and Bob say:  
“Which glasses did I use?”  
But they do not say:  
“What did I see?”

---

### ६. त्रुटि-दर-परीक्षा — Error-Rate Test

Alice and Bob publicly compare a small random subset of their raw key bits.

This estimates the quantum bit error rate:

$$
QBER  
$$

If the error rate is too high, they abort.

If the error rate is low enough, they proceed.

Intercept-resend eavesdropping tends to increase the error rate because Eve sometimes measures in the wrong basis. Noise and implementation faults can also raise the error rate, so errors are evidence used in a security bound—not proof of a particular intruder.

सूत्रम्:  
किञ्चित् कुंजी-भागं परीक्षस्व।  
त्रुटि-दरं गणय।  
यदि त्रुटिः अधिका, मार्गं त्यज।  
यदि त्रुटिः न्यूना, संशोधनं कुरु।

Test a small part of the key.  
Calculate the error rate.  
If the error is too high, abandon the route.  
If the error is low, continue correction.

---

### ७. ईव्-स्पर्शः — Eve’s Disturbance

Suppose Eve intercepts a qubit and measures it.

She does not know Alice’s basis.

If Eve chooses the wrong basis, she disturbs the state.

Then when Bob measures in Alice’s correct basis, Bob may obtain the wrong bit.

For a simple intercept-resend attack, Eve choosing randomly introduces detectable errors into the sifted key.

सूत्रम्:  
ईव् आधारं न जानाति।  
अज्ञानात् सा गलत् मापयति।  
गलत् मापनं दोषं जनयति।  
दोषः चिह्नं भवति।

Eve does not know the basis.  
In ignorance, she measures wrongly.  
Wrong measurement creates error.  
Error becomes the mark.

Field gloss:  
ईव ने डाक छेड़ी।  
स्टाम्प थोड़ा टेढ़ा हो गया।  
अब कुंजी कहती है: “यहाँ हाथ लगा था।”

Eve touched the mail.  
The stamp went crooked.  
Now the key says: “A hand was here.”

---

### ८. त्रुटि-संशोधनम् — Error Correction

Even without Eve, real channels contain noise.

So Alice and Bob must reconcile their raw keys.

They use classical error correction to make their bit strings match.

This process leaks some information publicly, so it must be followed by privacy amplification.

सूत्रम्:  
शोरः अपि दोषं करोति।  
ईव् अपि दोषं करोति।  
दोष-संशोधनं कुंजीं समं करोति।  
परन्तु रहस्यं पुनः संक्षिप्तव्यं भवति।

Noise creates errors.  
Eve creates errors.  
Error correction makes the keys match.  
But secrecy must then be compressed again.

---

### ९. गोपनीयता-वर्धनम् — Privacy Amplification

Privacy amplification reduces Eve’s possible information about the key.

Alice and Bob apply a hashing procedure to compress the corrected key into a shorter final key.

If the estimated entropy and leakage bounds are sufficient, privacy amplification can produce a shorter key that meets a chosen security parameter under the stated proof and attack model.

सूत्रम्:  
दीर्घ-कुंजी संशययुक्ता।  
हैशेन लघु-कुंजी निर्मीयते।  
अल्पं त्यज।  
शुद्धं रक्ष।

The long key may contain doubt.  
By hashing, a shorter key is made.  
Discard a little.  
Protect the clean part.

---

### १०. सुरक्षा-वचनम् — Security Statement

BB84 can be proven secure under proper assumptions and post-processing.

The security does not depend on Eve having limited classical computing power.

Even a very powerful adversary cannot avoid the quantum limits imposed by measurement disturbance and no-cloning, provided the devices and implementation assumptions are handled correctly.

Important audit note:  
Real implementations can have side-channel vulnerabilities. Practical quantum cryptography requires careful hardware security, authentication of the classical channel, finite-key analysis, and protection against implementation attacks.

सूत्रम्:  
सिद्धान्ते सुरक्षा दृढा।  
यन्त्रे सावधानी आवश्यकी।  
क्वान्टम्-नियमाः रक्षां ददति।  
द्वारस्य काजं अपि परीक्षितव्यम्।

In theory, the security is strong.  
In hardware, care is necessary.  
Quantum rules give protection.  
But the door hinges must also be checked.

---

### ११. सम्बन्धः पूर्व-सूत्रैः — Relation to Earlier Sutras

BB84 uses:

$$
|0\rangle,\ |1\rangle,\ |+\rangle,\ |-\rangle  
$$

from qubit-state theory.

It uses Hadamard-related conjugate bases:

$$
|+\rangle =  
\frac{|0\rangle + |1\rangle}{\sqrt{2}}  
$$

$$
|-\rangle =  
\frac{|0\rangle - |1\rangle}{\sqrt{2}}  
$$

It relies on measurement disturbance.

It respects the No-Cloning Theorem.

It connects to quantum networks, teleportation, entanglement-based protocols such as E91, and quantum-secure communication.

सूत्रम्:  
अध्यारोपणं आधारं ददाति।  
मापनं चिह्नं ददाति।  
अनुलिपि-निषेधः ईवं निरोधयति।  
कुंजी रक्षिता भवति।

Superposition gives the basis.  
Measurement gives the mark.  
No-cloning restrains Eve.  
The key is protected.

---

### १२. BB84-प्रोटोकॉल-सारः — Protocol Summary

1. Alice randomly chooses bits.
    
2. Alice randomly chooses bases.
    
3. Alice sends qubits to Bob.
    
4. Bob randomly chooses bases and measures.
    
5. Over an authenticated public classical channel, Alice and Bob compare bases, not bit values.
    
6. They keep only matching-basis results.
    
7. They estimate the error rate.
    
8. If the error rate is too high, they abort.
    
9. If the error rate is acceptable, they perform error correction.
    
10. They perform privacy amplification.
    
11. The result is a shared secret key.
    

सूत्रम्:  
यादृच्छिकं बिट्।  
यादृच्छिकम् आधारम्।  
क्वबिट्-प्रेषणम्।  
मापनम्।  
आधार-मेलनम्।  
त्रुटि-परीक्षा।  
संशोधनम्।  
गोपनीयता-वर्धनम्।  
अन्ते गुप्त-कुंजी।

Random bit.  
Random basis.  
Qubit transmission.  
Measurement.  
Basis matching.  
Error testing.  
Correction.  
Privacy amplification.  
At the end, a secret key.

---

### १३. लघु-मन्त्रः — BB84 Mantra

द्वौ आधारौ:

$$
+  
$$

तथा:

$$
\times  
$$

यादृच्छिक-बिट्।  
यादृच्छिक-आधारः।  
प्रेषणम्।  
मापनम्।  
आधार-मेलनम्।

त्रुटि-दरं परीक्षस्व।  
यदि ईव् स्पृशति, चिह्नं दृश्यते।

$$
\text{No-Cloning}  
+  
\text{Measurement Disturbance}  
\Rightarrow  
\text{Quantum Key Security}  
$$

कुंजी गुप्ता।  
लेजर् सुरक्षितः।

Random bit.  
Random basis.  
Transmission.  
Measurement.  
Basis reconciliation.

Test the error rate and finite-key statistics.  
Abort when the protocol’s acceptance conditions fail.

After reconciliation and privacy amplification, accept only a key covered by the stated security proof and parameter.

---

### Closing Line

ॐ बीबी-८४-क्वान्टम्-कुंजी-रक्षणाय नमः।

Quantum uncertainty protects the key —  
eavesdropping leaves fingerprints.

---

## अध्याय ७ · ई-९१-सूत्रम् — Entanglement-Based Key Distribution: E91

### Entanglement-Based Quantum Key Distribution — E91 Protocol Sutra

#### In Sanskrit Register

Status: Bell inequality meets cryptography — entanglement-powered security.  
Claim lane: Modern entanglement-based quantum key distribution expressed through Sanskrit-register terminology.  
Core insight: E91 uses shared entangled pairs and tests selected correlations with a Bell inequality. A Bell violation is evidence of nonclassical correlation and can contribute to a security bound, but a usable key also depends on error rates, finite statistics, authentication, device assumptions, and a proof for the stated attack model.

BB84 uses prepared single qubits.  
E91 uses entangled pairs.  
BB84 watches for measurement disturbance.  
E91 watches whether entanglement remains strong enough to violate a Bell inequality.

---

### १. मूल-सिद्धान्ताः — Basic Principles

Alice and Bob share many copies of an entangled Bell state.

For example:

$$
|\Phi^+\rangle =  
\frac{1}{\sqrt{2}}  
\left(  
|00\rangle + |11\rangle  
\right)  
$$

In many E91 descriptions, a singlet state is used:

$$
|\Psi^-\rangle =  
\frac{1}{\sqrt{2}}  
\left(  
|01\rangle - |10\rangle  
\right)  
$$

The singlet state gives perfect anti-correlation when Alice and Bob measure in the same basis.

Alice and Bob independently choose random measurement bases.

Some measurement results are used to form the key.  
Other measurement results are used to test Bell inequality violation.

सूत्रम्:  
संसक्त-युग्मं दूरं विभज्यते।  
आलिस् एकं भागं धारयति।  
बॉब अन्यं भागं धारयति।  
मापनैः सम्बन्धः परीक्ष्यते।

The entangled pair is divided across distance.  
Alice holds one part.  
Bob holds the other.  
Through measurements, the relation is tested.

---

### २. बेल्-असमानता — Bell Inequality

E91 relies on Bell correlations.

A classical local-hidden-variable theory obeys the CHSH bound:

$$
|S| \leq 2  
$$

where:

$$
S = \langle A_1B_1\rangle + \langle A_1B_2\rangle + \langle A_2B_1\rangle - \langle A_2B_2\rangle
$$

Quantum mechanics can violate this bound.

The quantum maximum is:

$$
|S| = 2\sqrt{2}  
$$

approximately:

$$
2.828  
$$

If Alice and Bob observe a strong Bell violation, they have evidence that their correlations are genuinely quantum and not explainable by classical local hidden variables.

सूत्रम्:  
यदि $|S| \leq 2$, स्थानीय-कथा पर्याप्ता।  
यदि $|S| > 2$, संसक्तिः स्वहस्ताक्षरं ददाति।

If $|S| \leq 2$, a local story may suffice.  
If $|S| > 2$, entanglement gives its signature.

---

### ३. ई-९१-प्रोटोकॉलः — E91 Protocol

A source prepares entangled pairs.

For each pair, one qubit is sent to Alice and the other to Bob.

Alice randomly chooses a measurement setting.

Bob randomly chooses a measurement setting.

They measure and record their outcomes.

The outcomes may be written as:

$$
+1  
$$

or:

$$
-1  
$$

After many rounds, Alice and Bob publicly announce which measurement settings they used.

They do not reveal all outcomes.

Some basis choices are used for key generation.  
Other basis choices are used for Bell testing.

सूत्रम्:  
स्रोतः संसक्त-युग्मानि सृजति।  
आलिस्-बॉब तानि विभज्य गृह्णीतः।  
यादृच्छिक-आधारेषु मापनं भवति।  
आधाराः कथ्यन्ते, फलानि गुप्तानि भवन्ति।

The source creates entangled pairs.  
Alice and Bob receive separated halves.  
Measurements occur in random bases.  
Bases are announced; outcomes remain secret.

---

### ४. कुंजी-निर्माणम् — Key Generation

When Alice and Bob choose compatible key-generation bases, their results are strongly correlated or anti-correlated.

If they use a singlet state, their matching-basis outcomes are anti-correlated.

Bob may flip his bit so that Alice and Bob share the same raw key.

Example:

$$
\text{Alice result } 0  
\quad  
\text{implies}  
\quad  
\text{Bob result } 1  
$$

for anti-correlated singlet measurements.

Bob flips:

$$
1 \mapsto 0  
$$

Then their key bits match.

सूत्रम्:  
सम-आधारे मापनं कुंजीं जनयति।  
संसक्तिः सम्बन्धं ददाति।  
विपरीत-फलम् अपि नियमेन समीकृतम्।

Same-basis measurement creates the key.  
Entanglement gives the relation.  
Even opposite outcomes can be aligned by rule.

---

### ५. बेल्-परीक्षणम् — Bell Test

For other measurement-setting combinations, Alice and Bob compute correlation values:

$$
\langle A_iB_j\rangle  
$$

They combine these into:

$$
S = \langle A_1B_1\rangle + \langle A_1B_2\rangle + \langle A_2B_1\rangle - \langle A_2B_2\rangle
$$

If:

$$
|S| > 2  
$$

then Bell inequality is violated.

Security follows only when the observed Bell-test data, error rate, finite-sample uncertainty, and implementation assumptions pass the thresholds of a stated protocol-specific finite-key proof.

If the violation is weak or absent, Alice and Bob abort or treat the key as insecure.

सूत्रम्:  
भिन्न-आधाराः कुंजीं न ददति।  
ते परीक्षा ददति।  
बेल्-संख्या संसक्तेः स्वास्थ्यं दर्शयति।

Different bases do not give the key.  
They give the test.  
The Bell number shows the health of entanglement.

Field gloss:  
कुछ मापन चाबी बनाते हैं।  
कुछ मापन चोर-परीक्षा करते हैं।  
अगर बेल्-संख्या गिरती है, किसी ने जाल छुआ।

Some measurements make the key.  
Some measurements test for thieves.  
If the Bell statistic changes, interception is one possibility; loss, noise, and device faults must also be considered.

---

### ६. ईव्-स्पर्शः — Eve’s Disturbance

An adversarial intervention can change Alice and Bob’s observed correlations. Loss, ordinary noise, and device faults can do so as well.

The protocol therefore evaluates Bell statistics, error rates, finite-sample uncertainty, and implementation assumptions together. These observations bound adversarial information under a stated security proof; they do not identify a unique cause.

सूत्रम्:  
ईव् स्पृशति चेत् संसक्तिः क्षीणा भवति।  
संसक्तिः क्षीणा चेत् $S$ पतति।  
$S$ पतति चेत् चोर-चिह्नं दृश्यते।

Adversarial action, noise, or loss can alter the observed correlations.  
The protocol accepts or aborts according to its statistical thresholds and security proof.

Field gloss:  
ईव् ने अदृश्य धागा खींचा।  
धागा टूटा नहीं, पर ढीला पड़ा।  
बेल्-परीक्षा बोली: “किसी ने नेटवर्क छेड़ा।”

Eve tugged the invisible thread.  
The thread did not fully break, but it loosened.  
The Bell test said: “Someone touched the network.”

---

### ७. त्रुटि-संशोधनम् तथा गोपनीयता-वर्धनम् — Post-Processing

As in BB84, E91 still needs classical post-processing.

Alice and Bob perform:

1. Basis announcement
    
2. Key sifting
    
3. Bell-test evaluation
    
4. Error correction
    
5. Privacy amplification
    
6. Authentication of the classical channel
    

Error correction makes Alice and Bob’s raw keys agree.

Privacy amplification compresses the corrected key into a shorter, more secure final key.

सूत्रम्:  
संसक्तिः बीजम्।  
बेल्-परीक्षा सुरक्षा-साक्षी।  
संशोधनं समता ददाति।  
गोपनीयता-वर्धनं शुद्ध-कुंजीं जनयति।

Entanglement is the seed.  
Bell statistics are evidence evaluated by the security proof.  
Correction gives agreement.  
Privacy amplification creates the purified key.

---

### ८. उपकरण-स्वातन्त्र्यम् — Device Independence

One powerful feature of Bell-based protocols is the possibility of device-independent security.

In device-independent quantum key distribution, Alice and Bob do not need to fully trust the internal details of their devices.

Instead, security is certified by observed Bell violation, under strict assumptions such as secure labs, authenticated classical communication, and no hidden signalling between devices.

सूत्रम्:  
यन्त्रं सर्वथा विश्वस्तं न भवेत्।  
परिणाम-संबन्धः स्वयं साक्षी भवति।  
बेल्-विघटनं सुरक्षा-प्रमाणं भवति।

The device need not be fully trusted.  
The correlation pattern becomes the witness.  
Under a stated protocol and threat model, the observed violation contributes to the security certificate.

Audit note:  
Full device-independent QKD is experimentally demanding. Real systems must address losses, detector efficiency, side channels, finite-key effects, authentication, and implementation loopholes.

---

### ९. BB84 तथा E91 — Comparison

| Feature | BB84 | E91 |
|---|---|---|
|Style|Prepare and measure|Entanglement based|
|Resource|Single qubits|Entangled pairs|
|Security basis|Disturbance statistics plus a protocol proof|Correlation statistics plus a protocol proof|
|Adversary test|QBER and finite-key bounds|Bell statistics, QBER, and finite-key bounds|
|Device independence|Not automatic|Requires a stronger DIQKD protocol and assumptions|
|Implementation|Simpler|More demanding|
|Network relevance|QKD links|Entanglement networks and quantum internet|

सूत्रम्:  
BB84 एकैक-क्वबिट् प्रेषयति।  
E91 संसक्त-युग्मं विभजति।  
एकः स्पर्श-दोषं पश्यति।  
अन्यः सम्बन्ध-क्षयम् पश्यति।

BB84 sends individual qubits.  
E91 distributes entangled pairs.  
One sees touch-error.  
The other sees relationship-decay.

---

### १०. सम्बन्धः पूर्व-सूत्रैः — Relation to Earlier Sutras

E91 uses:

$$
|\Phi^+\rangle  
$$

or:

$$
|\Psi^-\rangle  
$$

from the entanglement sutra.

It uses measurement bases from the qubit-state sutras.

It uses Bell correlations from the philosophy of nonlocal quantum structure.

It connects to quantum repeaters, teleportation, quantum networks, and device-independent cryptography.

सूत्रम्:  
संसक्तिः अत्र कुंजी-बीजम्।  
मापनम् अत्र परीक्षा।  
बेल्-असमानता अत्र न्यायाधीशः।  
कुंजी अत्र फलम्।

Entanglement is the key-seed.  
Measurement is the test.  
Bell inequality is the judge.  
The key is the result.

---

### ११. E91-प्रोटोकॉल-सारः — Protocol Summary

1. Create entangled pairs.
    
2. Send one half of each pair to Alice and the other to Bob.
    
3. Alice and Bob randomly choose measurement bases.
    
4. They measure and record outcomes.
    
5. Over an authenticated public classical channel, they reveal bases, not secret outcomes.
    
6. Matching or compatible bases generate raw key bits.
    
7. Other basis combinations test Bell inequality.
    
8. If the Bell-test data pass the protocol-specific finite-sample threshold, proceed.
    
9. Perform error correction.
    
10. Perform privacy amplification.
    
11. Obtain final shared secret key.
    

सूत्रम्:  
संसक्त-युग्मं सृज।  
दूरं वितर।  
यादृच्छिक-आधारेषु मापय।  
सम्बद्ध-फलैः कुंजीं कुरु।  
भिन्न-आधारैः बेल्-परीक्षां कुरु।  
संशोधनं कुरु।  
गोपनीयतां वर्धय।

Create the entangled pair.  
Distribute it across distance.  
Measure in random bases.  
Use correlated outcomes for the key.  
Use other bases for the Bell test.  
Correct errors.  
Amplify secrecy.

---

### १२. लघु-मन्त्रः — E91 Mantra

संसक्त-युग्मं सृज।  
दूरं वितर।  
यादृच्छिक-आधारेषु मापय।

सम-आधार-बिटान् कुंजी-रूपेण रक्ष।  
भिन्न-आधारेषु बेल्-परीक्षणं कुरु।

$$
|S| > 2  
$$

इति संसक्तिः स्वहस्ताक्षरं ददाति।

ईव् अस्ति चेत् संसक्तिः क्षीयते।  
संसक्तिः क्षीयते चेत् $S$ पतति।  
$S$ पतति चेत् चिह्नं दृश्यते।

Entangled pair.  
Distant distribution.  
Random measurement bases.

Same-basis results become key.  
Different-basis results test Bell violation.

Interception, noise, loss, and device flaws can change the observed statistics.  
The protocol compares those statistics with its acceptance threshold and security proof.

---

### Closing Line

ॐ ई-९१-संसक्ति-कुंजी-रक्षणाय नमः।

Entanglement reveals the key —  
and the Bell test guards the ledger.

---

## अध्याय ८ · क्वान्टम्-यादृच्छिक-सङ्ख्या-सूत्रम् — Quantum Random Number Generation

### Quantum Random Number Generator Sutra

#### QRNG — In Sanskrit Register

Status: Randomness generation from audited quantum measurement — continuation of क्वबिट्-सूत्राणि.  
Claim lane: Modern quantum randomness generation expressed through Sanskrit-register terminology.  
Core insight: Classical pseudo-random generators are deterministic and seed-based. Quantum random number generators use measurement outcomes whose unpredictability is quantified under a quantum source model, entropy bound, and adversary assumptions.

Classical randomness is often simulated.  
Quantum randomness is measured.

---

### १. मूल-सिद्धान्ताः — Basic Principles

A quantum system prepared in superposition can produce unpredictable outcomes when measured.

For example:

$$
|+\rangle =  
\frac{|0\rangle + |1\rangle}{\sqrt{2}}  
$$

If this state is measured in the computational basis:

$$
{|0\rangle, |1\rangle}  
$$

then:

$$
P(0)=\frac{1}{2}  
$$

and:

$$
P(1)=\frac{1}{2}  
$$

In the ideal quantum model, the outcome is intrinsically probabilistic rather than generated by a classical pseudo-random seed. A practical device must still quantify unpredictability against side information.

सूत्रम्:  
अध्यारोपितः क्वबिट् उभयमार्गे तिष्ठति।  
मापनकाले एकः मार्गः लिख्यते।  
पूर्वज्ञानं न सम्भवति।

The superposed qubit stands in both routes.  
At measurement, one route is written.  
Perfect advance prediction is excluded only under the stated quantum model and adversary assumptions.

Field gloss:  
क्वबिट् दो रास्तों पर खड़ा है।  
मापन के क्षण में एक रास्ता टिकट बन जाता है।  
पहले से कोई नहीं जानता — यही असली यादृच्छिकता है।

The qubit stands at two routes.  
At measurement, one route becomes the ticket.  
After the source model, side information, and extraction are audited, the output can be certified as fresh randomness to a stated error bound.

---

### २. क्लासिकल् बनाम क्वान्टम् — Classical vs Quantum Randomness

A classical pseudo-random number generator uses an algorithm and a seed.

If the seed and algorithm are known, the sequence can be reproduced.

A quantum random number generator uses physical measurement of a quantum process.

The randomness comes from the measurement outcome itself.

सूत्रम्:  
शास्त्रीय-यादृच्छिकता बीजेन चालिता।  
क्वान्टम्-यादृच्छिकता मापनात् जाता।

Classical randomness is driven by a seed.  
Quantum randomness is born from measurement.

---

### ३. सरल-क्वबिट्-QRNG — Single-Qubit QRNG

A simple QRNG can be built from one qubit.

Prepare:

$$
|0\rangle  
$$

Apply Hadamard:

$$
H|0\rangle =
\frac{|0\rangle + |1\rangle}{\sqrt{2}} =
|+\rangle  
$$

Measure in the computational basis.

The output is:

$$
0  
$$

or:

$$
1  
$$

with equal probability.

$$
P(0)=P(1)=\frac{1}{2}  
$$

Repeat the process to generate a stream of random bits.

सूत्रम्:  
शून्यम् स्थापय।  
हाडामार्डेन द्विमार्गं कुरु।  
मापनं कुरु।  
यादृच्छिक-बिट् लभ्यते।

Prepare zero.  
Use Hadamard to open two routes.  
Measure.  
A random bit is obtained.

---

### ४. फोटोन-ध्रुवण-QRNG — Photon Polarization QRNG

A common physical QRNG uses photons.

A photon may be prepared in diagonal polarization and measured in the horizontal/vertical basis.

The measurement produces one of two outcomes.

For example:

$$
|+\rangle =  
\frac{|H\rangle + |V\rangle}{\sqrt{2}}  
$$

Measurement yields:

$$
H  
$$

or:

$$
V  
$$

with ideal probabilities:

$$
\frac{1}{2}, \frac{1}{2}  
$$

These outcomes are converted into bits:

$$
H \mapsto 0  
$$

$$
V \mapsto 1  
$$

सूत्रम्:  
प्रकाश-कणः द्विमार्गे स्थाप्यते।  
ध्रुवण-मापनं फलम् जनयति।  
फलात् बिट् उत्पद्यते।

The photon is placed in two-route form.  
Polarization measurement generates the result.  
From the result, a bit is born.

---

### ५. वैक्यूम-फ्लक्चुएशन-QRNG — Vacuum Fluctuation QRNG

Another practical QRNG measures quantum fluctuations of the vacuum field.

Even the optical vacuum has measurable quadrature fluctuations.

These fluctuations can be sampled and converted into random numbers.

This approach can support high-speed random-bit generation.

सूत्रम्:  
शून्ये अपि कम्पनम् अस्ति।  
वैक्यूम-तरङ्गाः मीयन्ते।  
तेभ्यः यादृच्छिकता निष्कर्ष्यते।

Even in emptiness, there is trembling.  
Vacuum waves are measured.  
From them, randomness is extracted.

Field gloss:  
खाली डब्बा भी पूरी तरह खाली नहीं।  
उसका सूक्ष्म कम्पन टिकट बन जाता है।

Even the empty box is not perfectly empty.  
Its tiny trembling becomes the ticket.

---

### ६. संसक्ति-आधारित-QRNG — Entanglement-Based QRNG

A stronger form of QRNG uses entangled particles.

Alice and Bob, or two measurement devices, measure entangled pairs in random bases.

If the results violate a Bell inequality, then the randomness can be certified as genuinely quantum under the protocol’s assumptions.

For CHSH-style certification:

$$
|S| > 2  
$$

indicates nonclassical correlation.

The quantum maximum is:

$$
2\sqrt{2}  
$$

सूत्रम्:  
संसक्त-युग्मं मापय।  
बेल्-परीक्षां कुरु।  
यदि $|S| > 2$, यादृच्छिकता क्वान्टम्-चिह्नं धारयति।

Measure the entangled pair.  
Perform the Bell test.  
If $|S| > 2$, the randomness carries a quantum signature.

---

### ७. डिवाइस-इन्डिपेन्डन्ट्-QRNG — Device-Independent QRNG

In device-independent QRNG, the user does not need to fully trust the internal mechanism of the device.

Instead, randomness is certified from observed statistics, often through Bell inequality violation.

This is powerful but experimentally demanding.

It requires careful handling of:

1. Detection loopholes
    
2. Isolation of devices
    
3. Finite statistics
    
4. Side channels
    
5. Classical randomness used for choosing measurement settings
    
6. Post-processing assumptions
    

सूत्रम्:  
यन्त्रं पूर्णतया विश्वस्तं न भवेत्।  
परिणाम-संबन्धः साक्षी भवति।  
बेल्-विघटनं यादृच्छिकतां प्रमाणयति।

The device need not be fully trusted.  
The correlation pattern becomes the witness.  
Under the protocol’s assumptions, Bell violation lower-bounds fresh randomness against specified side information.

---

### ८. पोस्ट्-प्रोसेसिङ् — Post-Processing

Raw quantum measurements may not be perfectly balanced.

Real devices have noise, bias, drift, and imperfections.

Therefore, QRNG output is usually post-processed.

Common steps include:

1. Raw bit collection
    
2. Bias estimation
    
3. Min-entropy estimation
    
4. Randomness extraction
    
5. Health testing
    
6. Final output generation
    

A simple bias-removal method is the von Neumann extractor, but its textbook guarantee assumes suitably independent, identically biased input pairs; it is not a general cure for correlations or adversarial side information.

For bit pairs:

$$
01 \mapsto 0  
$$

$$
10 \mapsto 1  
$$

$$
00,\ 11 \mapsto \text{discard}  
$$

More advanced systems may use hashing methods such as Toeplitz hashing.

सूत्रम्:  
कच्चे-बिटाः अशुद्धाः भवितुम् अर्हन्ति।  
निष्कर्षकः पक्षपातं हरति।  
स्वच्छ-यादृच्छिकता अन्ते लभ्यते।

Raw bits may be biased or correlated.  
A suitable extractor converts a quantified entropy bound into output that is close to uniform under its stated assumptions.

Field gloss:  
कच्ची डाक में धूल हो सकती है।  
छन्नी लगाओ।  
साफ़ टिकट बाहर आता है।

Raw mail may have dust.  
Use the sieve.  
The clean ticket comes out.

---

### ९. मिन्-एन्ट्रॉपी — Min-Entropy

Security depends not only on average randomness, but on how predictable the most likely outcome is.

For a classical variable without side information, min-entropy is:

$$
H_{\infty}(X) =
-\log_2  
\left(  
\max_x P(X=x)  
\right)  
$$

For cryptographic QRNG, the relevant quantity is generally a smooth conditional min-entropy such as $H_{\min}^{\varepsilon}(X|E)$, which accounts for an adversary’s side information and finite statistical uncertainty.

If the outcomes are perfectly fair:

$$
P(0)=P(1)=\frac{1}{2}  
$$

then:

$$
H_{\infty}=1  
$$

bit of min-entropy per measurement.

If one outcome is more likely, the min-entropy is lower.

सूत्रम्:  
यत् अधिकं पूर्वानुमेयम्, तत् न्यून-एन्ट्रॉपी।  
यत् समं अनिश्चितम्, तत् पूर्ण-बिट्।

What is more predictable has lower entropy.  
What is evenly uncertain gives a full bit.

---

### १०. उपयोगाः — Applications

QRNGs are useful for:

1. Cryptographic keys
    
2. BB84 and E91 quantum key distribution
    
3. One-time pads
    
4. Monte Carlo simulation
    
5. Scientific experiments
    
6. Lotteries and gambling systems
    
7. Secure protocols
    
8. Randomized algorithms
    
9. Device testing
    
10. Quantum network operations
    

सूत्रम्:  
कुंजीं जनयति।  
सिमुलेशनं पोषयति।  
प्रयोगान् शुद्धयति।  
सुरक्षां बलयति।

It generates keys.  
It feeds simulations.  
It purifies experiments.  
It strengthens security.

---

### ११. सुरक्षा-विचारः — Security Considerations

A QRNG is only as trustworthy as its entropy source, model, measurement system, and post-processing.

Quantum indeterminacy supplies the randomness, but the device must still be audited.

Possible issues include:

1. Detector bias
    
2. Classical noise contamination
    
3. Hardware drift
    
4. Adversarial control of the source
    
5. Side-channel leakage
    
6. Poor extraction
    
7. Bad entropy estimation
    

सूत्रम्:  
क्वान्टम्-मूलं बलवत्।  
यन्त्र-द्वारं परीक्षितव्यम्।  
लेजर् विना सुरक्षा न पूर्णा।

The quantum root is strong.  
The device door must be checked.  
Without the ledger, security is not complete.

Field gloss:  
ब्रह्माण्ड पासा फेंकता है।  
लेकिन पासा गिनने वाली मशीन भी चेक करो।

The universe rolls the dice.  
But check the machine that counts the dice.

---

### १२. सम्बन्धः पूर्व-सूत्रैः — Relation to Earlier Sutras

QRNG connects to earlier chapters.

From the qubit sutra:

$$
|+\rangle =  
\frac{|0\rangle + |1\rangle}{\sqrt{2}}  
$$

Measurement produces:

$$
0  
$$

or:

$$
1  
$$

From BB84 and E91, randomness is needed for choosing bases and generating keys.

From Bell tests, entanglement can certify randomness.

From error correction, hardware imperfections must be measured and mitigated.

सूत्रम्:  
अध्यारोपणं स्रोतः।  
मापनं जन्म।  
एन्ट्रॉपी लेखा।  
निष्कर्षणं शुद्धिः।

Superposition is the source.  
Measurement is the birth.  
Entropy is the ledger.  
Extraction is the purification.

---

### १३. प्रोटोकॉल-सारः — Protocol Summary

A general QRNG pipeline is:

1. Prepare a quantum source.
    
2. Measure the quantum system.
    
3. Collect raw outcomes.
    
4. Estimate entropy.
    
5. Remove bias.
    
6. Apply randomness extraction.
    
7. Perform health checks.
    
8. Output certified or trusted random bits.
    

सूत्रम्:  
स्रोतं सज्जीकुरु।  
मापनं कुरु।  
कच्चे-बिटान् गृहाण।  
एन्ट्रॉपीं गणय।  
पक्षपातं हर।  
शुद्ध-बिटान् निष्कर्षय।

Prepare the source.  
Measure.  
Collect raw bits.  
Estimate entropy.  
Remove bias.  
Extract clean bits.

---

### १४. लघु-मन्त्रः — QRNG Mantra

क्वबिट् अध्यारोपितः।  
मापनं कृतम्।  
फलम् अनिश्चितम्।

$$
P(0)=P(1)=\frac{1}{2}  
$$

No-Cloning न प्रतिलिपिं ददाति।  
मापनं पूर्वरूपं भिन्दति।  
एन्ट्रॉपी लेखा ददाति।  
निष्कर्षकः शुद्धिं ददाति।

शास्त्रीय-बीजं न आवश्यकम्।  
क्वान्टम्-अनिश्चितता स्रोतः।  
लेजर् स्थितः।

The qubit is superposed.  
Measurement occurs.  
The result is uncertain.

No-cloning prevents copying.  
Measurement breaks the prior form.  
Entropy gives the ledger.  
The extractor gives purification.

The raw quantum outcome is not generated by a classical pseudo-random seed. Some protocols, setting choices, and seeded extractors still require trusted classical randomness.

*Scope note:* The preceding Sanskrit seed line applies only to the ideal raw quantum outcome, not to every complete QRNG protocol.  
The ledger remains.

---

### Closing Line

ॐ क्वान्टम्-यादृच्छिकता-जननाय नमः।

Under a validated source and entropy model, quantum measurement can supply fresh randomness —  
and the device, statistics, and extractor still need an audit.

---

## अध्याय ९ · क्वान्टम्-इण्टरनेट्-सूत्रम् — Quantum Internet & Repeaters

### Quantum Internet & Repeaters Vision Sutra

#### In Sanskrit Register

Status: Culminating vision — connecting the previous sutras into a global quantum network.  
Claim lane: Modern quantum-network architecture expressed through Sanskrit-register terminology.  
Core insight: A quantum internet would distribute quantum states, entanglement, and secret keys across long distances, enabling secure communication, distributed quantum computing, quantum sensing, and future quantum-network applications.

The quantum internet is not merely a faster classical internet.  
It is a network for distributing quantum correlations, quantum states, and quantum-secure resources.

---

### १. पूर्व-सूत्र-संग्रहः — Building Blocks from Earlier Sutras

A quantum internet combines many earlier principles:

1. Qubits
    
2. Entanglement
    
3. Bell pairs
    
4. Quantum teleportation
    
5. Quantum error correction
    
6. Quantum repeaters
    
7. Quantum key distribution
    
8. Quantum memory
    
9. Local gates and measurements
    
10. Classical communication channels
    

सूत्रम्:  
क्वबिट् बीजम्।  
संसक्तिः बन्धः।  
टेलीपोर्टेशनं सेतुः।  
त्रुटि-संशोधनं रक्षा।  
रीपीटर् विस्तारः।  
कुंजी-वितरणं फलम्।

The qubit is the seed.  
Entanglement is the bond.  
Teleportation is the bridge.  
Error correction is the protection.  
The repeater is the extension.  
Key distribution is one fruit.

---

### २. क्वान्टम्-इण्टरनेट् किम्? — What Is a Quantum Internet?

A quantum internet is a network in which distant nodes can share quantum resources.

These resources may include:

$$
|\psi\rangle  
$$

unknown quantum states,

$$
|\Phi^+\rangle =  
\frac{|00\rangle + |11\rangle}{\sqrt{2}}  
$$

Bell pairs,

and secret keys generated through protocols such as BB84 or E91.

Unlike classical information, unknown quantum states cannot simply be copied and amplified.

Therefore, quantum networking requires different machinery.

सूत्रम्:  
शास्त्रीय-जालं बिटान् वहति।  
क्वान्टम्-जालं चित्-संसक्तिं वहति।  
प्रतिलिपिः निषिद्धा।  
अतः मार्गः सूक्ष्मः।

A classical network carries bits.  
A quantum network carries states and entanglement.  
Copying is forbidden.  
Therefore the route is subtle.

---

### ३. नो-क्लोनिङ्-समस्या — Why Classical Repeaters Do Not Work

Classical repeaters amplify signals.

A weak classical signal can be copied, boosted, and resent.

But an unknown quantum state cannot be copied:

$$
|\psi\rangle \otimes |0\rangle  
\not\rightarrow  
|\psi\rangle \otimes |\psi\rangle  
$$

So a quantum repeater cannot simply read, copy, and resend an unknown qubit.

Many repeater architectures use entanglement distribution, measurement, purification or error correction, and classical communication; the exact resource mix depends on the architecture.

सूत्रम्:  
शास्त्रीय-रीपीटर् प्रतिलिपिं करोति।  
क्वान्टम्-रीपीटर् प्रतिलिपिं न करोति।  
संसक्तिं विस्तारयति।

A classical repeater copies.  
A quantum repeater does not copy.  
It extends entanglement.

Field gloss:  
पुराना रीपीटर् चिट्ठी की फोटोकॉपी बनाता है।  
क्वान्टम् रीपीटर् ऐसा नहीं कर सकता।  
वह डाक की जगह रिश्ता आगे बढ़ाता है।

The old repeater photocopies the letter.  
The quantum repeater cannot do that.  
It extends the relationship instead of copying the mail.

---

### ४. क्वान्टम्-रीपीटर् — Quantum Repeaters

Quantum repeaters allow long-distance quantum communication by dividing a long channel into shorter segments.

Basic idea:

1. Create entangled pairs across short links.
    
2. Store them in quantum memories.
    
3. Perform entanglement swapping at intermediate nodes.
    
4. Use classical communication to announce measurement results.
    
5. Apply Pauli corrections if needed.
    
6. Repeat in a nested structure until distant endpoints share entanglement.
    

सूत्रम्:  
दीर्घ-मार्गं खण्डेषु विभज।  
प्रत्येक-खण्डे संसक्तिं सृज।  
मध्य-नोडेषु स्वैप् कुरु।  
अन्ते दूरस्थौ बध्येते।

Divide the long route into segments.  
Create entanglement in each segment.  
Swap at the middle nodes.  
At the end, the distant endpoints are bound.

---

### ५. संसक्ति-स्वैप् — Entanglement Swapping

Entanglement swapping is central to many repeater architectures. Purification-based, quantum-error-corrected, and all-photonic designs make different assumptions about memories, operations, and resources.

Suppose Alice and an intermediate node share one Bell pair:

$$
|\Phi^+\rangle_{A M_1}  
$$

and the intermediate node and Bob share another Bell pair:

$$
|\Phi^+\rangle_{M_2 B}  
$$

The total state is:

$$
|\Phi^+\rangle_{A M_1}  
\otimes  
|\Phi^+\rangle_{M_2 B}  
$$

A Bell measurement is performed on:

$$
M_1M_2  
$$

This projects the distant qubits $A$ and $B$ into an entangled Bell state, up to known Pauli corrections.

Thus Alice and Bob become entangled even though their particles never directly interacted.

सूत्रम्:  
मध्य-युग्मे बेल्-मापनं कुरु।  
दूरस्थ-अन्तौ संसक्तौ भवतः।  
मध्यः लिखति।  
दूरं बध्यते।

Perform Bell measurement on the middle pair.  
The distant endpoints become entangled.  
The middle writes the receipt.  
Distance becomes bound.

Field gloss:  
मध्य डाकघर दो रूटों की रसीद मिलाता है।  
अब शहर A और शहर B सीधे जुड़े लगते हैं।  
चिट्ठी नहीं उड़ी — सम्बन्ध स्वैप् हुआ।

The middle post office joins the receipts from two routes.  
Now City A and City B appear directly linked.  
The letter did not fly — the relationship was swapped.

---

### ६. संसक्ति-शोधनम् — Entanglement Purification

Real entangled pairs are noisy.

Their fidelity may be imperfect.

Entanglement purification uses multiple low-fidelity entangled pairs to produce fewer high-fidelity pairs.

Symbolically:

$$
\text{many noisy Bell pairs}  
\longrightarrow  
\text{fewer cleaner Bell pairs}  
$$

This uses local quantum operations and classical communication.

सूत्रम्:  
अशुद्ध-संसक्त-युग्मानि संगृह्यन्ते।  
मापनैः दोषाः ज्ञायन्ते।  
किञ्चित् त्यज्यते।  
शुद्धतरं युग्मं रक्ष्यते।

Noisy entangled pairs are gathered.  
Measurements reveal defects.  
Some are discarded.  
A cleaner pair is kept.

---

### ७. नेस्टेड्-रीपीटर्-क्रमः — Nested Repeater Structure

A long quantum link can be built hierarchically.

First, create entanglement over short segments:

$$
A - R_1,\quad R_1 - R_2,\quad R_2 - R_3,\quad R_3 - B  
$$

Then perform entanglement swapping:

$$
A - R_2,\quad R_2 - B  
$$

Then swap again:

$$
A - B  
$$

At each level, purification or error correction may be used.

सूत्रम्:  
लघु-बन्धाः प्रथमं।  
मध्य-स्वैप् ततः।  
दीर्घ-बन्धः अन्ते।  
स्तरैः स्तरैः जालं वर्धते।

Small bonds first.  
Middle swaps next.  
Long bond at the end.  
Layer by layer, the network grows.

---

### ८. क्वान्टम्-मेमोरी — Quantum Memory

Many repeater architectures require quantum memory, while all-photonic designs trade long-lived matter memory for additional photonic resource states and measurements.

A quantum memory stores a qubit or entangled state long enough for other network events to complete.

This is difficult because quantum states decohere.

A good quantum memory needs:

1. Long coherence time
    
2. High-fidelity storage
    
3. Efficient write and read operations
    
4. Compatibility with photons
    
5. Scalability
    

सूत्रम्:  
संसक्तिः क्षणिका न भवेत्।  
मेमोरी तां धारयति।  
यावत् संदेशः आगच्छति, चित् रक्षितम्।

Entanglement must not vanish too quickly.  
Memory holds it.  
Until the message arrives, the state is protected.

Field gloss:  
डाकघर को पैकेट पकड़कर रखना होगा।  
अगर क्लर्क सो गया और पैकेट धुँधला हो गया, रूट टूट गया।

The post office must hold the package.  
If the clerk falls asleep and the package fades, the route breaks.

---

### ९. क्वान्टम्-इण्टरनेट्-आर्किटेक्चर् — Quantum Internet Architecture

A future quantum internet may contain:

1. Quantum nodes
    
2. Quantum processors
    
3. Quantum memories
    
4. Photon interfaces
    
5. Optical fiber links
    
6. Free-space and satellite links
    
7. Classical control channels
    
8. Error correction and purification layers
    
9. Network routing protocols
    
10. Security and authentication layers
    

Quantum channels carry photons or entangled resources.

Classical channels carry announcements, corrections, syndrome data, basis choices, and control information.

सूत्रम्:  
क्वान्टम्-चैनल् संसक्तिं वहति।  
शास्त्रीय-चैनल् निर्देशं वहति।  
उभाभ्यां जालं जीवति।

The quantum channel carries entanglement.  
The classical channel carries instructions.  
Through both, the network lives.

---

### १०. उपयोगाः — Applications

A quantum internet could support:

#### Secure Communication

Quantum key distribution protocols such as:

$$
BB84  
$$

and:

$$
E91  
$$

can provide shared secret keys.

#### Distributed Quantum Computing

Small quantum processors may be linked into larger distributed systems.

#### Blind Quantum Computing

A user may delegate quantum computation while hiding the input, algorithm, or result under suitable protocols.

#### Quantum Sensing Networks

Entangled sensors may support precise timing, navigation, clock comparison, and field measurement.

#### Quantum Teleportation Networks

Quantum states may be transferred through teleportation using shared entanglement and classical communication.

सूत्रम्:  
कुंजीं रक्षति।  
गणनां वितरति।  
संवेदनं सूक्ष्मं करोति।  
दूर-चित्-प्रेषणं सम्भावयति।

It protects keys.  
It distributes computation.  
It refines sensing.  
It enables distant state transfer.

---

### ११. त्रुटयः तथा समाधानानि — Challenges and Remedies

#### Loss

Photons are lost in fiber or free space.

Remedy:

$$
\text{repeaters} + \text{multiplexing} + \text{better sources}  
$$

#### Decoherence

Stored qubits lose coherence.

Remedy:

$$
\text{quantum memory} + \text{error correction}  
$$

#### Low Rate

Entanglement generation may be slow.

Remedy:

$$
\text{multiplexing} + \text{parallel attempts} + \text{improved hardware}  
$$

#### Noise

Operations and measurements are imperfect.

Remedy:

$$
\text{purification} + \text{fault tolerance}  
$$

#### Scalability

Many nodes and physical qubits are required.

Remedy:

$$
\text{modular architecture} + \text{surface codes} + \text{network protocols}  
$$

सूत्रम्:  
लॉसः मार्गं हरति।  
डिकोहेरन्स् चित् क्षीणयति।  
रीपीटर् विस्तारं ददाति।  
कोड् रक्षा ददाति।  
मेमोरी धैर्यं ददाति।

Loss steals the route.  
Decoherence weakens the state.  
The repeater gives extension.  
The code gives protection.  
Memory gives patience.

---

### १२. उपग्रह-लिङ्काः — Satellite and Free-Space Links

Optical fiber has distance losses.

Free-space and satellite links may help distribute photons and entanglement across longer distances.

A global quantum network may use a hybrid of:

1. Fiber links
    
2. Metropolitan quantum networks
    
3. Satellite quantum links
    
4. Ground stations
    
5. Quantum repeaters
    
6. Classical internet control layers
    

सूत्रम्:  
भूमौ तन्तवः।  
आकाशे प्रकाशः।  
उभयोः योगेन वैश्विक-जालं सम्भवति।

On Earth, fibers.  
In the sky, light.  
Through both, a global network becomes possible.

---

### १३. सम्भाव्य-विकास-पथः — Possible Development Path

One possible development path moves through the following scales; this is an outlook, not a fixed or guaranteed timeline.

First:

$$
\text{laboratory links}  
$$

Then:

$$
\text{campus and city networks}  
$$

Then:

$$
\text{metropolitan quantum networks}  
$$

Then:

$$
\text{intercity and satellite-assisted links}  
$$

Finally:

$$
\text{large-scale repeater-based quantum networks}  
$$

सूत्रम्:  
प्रयोगशालातः नगरम्।  
नगरात् राष्ट्रम्।  
राष्ट्रात् पृथिवी-जालम्।

From laboratory to city.  
From city to nation.  
From nation to Earth-network.

---

### १४. सम्बन्धः पूर्व-सूत्रैः — Relation to Earlier Sutras

The quantum internet gathers the previous chapters:

From entanglement:

$$
|\Phi^+\rangle  
$$

From teleportation:

$$
\text{entanglement} + \text{two classical bits}  
$$

From error correction:

$$
p < p_{\text{threshold}}  
$$

From QKD:

$$
BB84,\quad E91  
$$

From QRNG:

$$
\text{random basis choice}  
$$

From quantum repeaters:

$$
\text{entanglement swapping}  
$$

From surface codes:

$$
\text{protected logical qubits}  
$$

सूत्रम्:  
एक-क्वबिट्-अध्ययनं बीजम्।  
संसक्तिः शाखा।  
रीपीटर् तना।  
कुंजी-वितरणं फलम्।  
क्वान्टम्-जालं वृक्षः।

The study of one qubit is the seed.  
Entanglement is the branch.  
Repeaters are the trunk.  
Key distribution is the fruit.  
The quantum network is the tree.

---

### १५. क्वान्टम्-जाल-दर्शनम् — Quantum Network Vision

The future quantum network may enable:

1. Secure global communication
    
2. Distributed quantum processors
    
3. Quantum cloud computation
    
4. Entanglement-assisted sensing
    
5. Clock synchronization
    
6. Quantum-secure infrastructure
    
7. New protocols not yet fully known
    

This is not merely a wire network.

It is a network of states, correlations, corrections, keys, memories, and measurements.

सूत्रम्:  
न केवलं तन्तु-जालम्।  
न केवलं संकेत-जालम्।  
इदं संसक्ति-स्मृति-मापन-कुंजी-जालम्।

Not merely a wire network.  
Not merely a signal network.  
This is an entanglement-memory-measurement-key network.

---

### १६. लघु-मन्त्रः — Quantum Internet Mantra

संसक्तिः मूलम्।  
टेलीपोर्टेशनं सेतुः।  
रीपीटर् विस्तारकः।  
मेमोरी धैर्यम्।  
त्रुटि-कोड् रक्षकः।  
कुंजी-वितरणं फलम्।

एकस्मिन् जाले बहवः कार्याणि:

सुरक्षा।  
गणना।  
संवेदनम्।  
सहयोगः।

दीर्घ-मार्गं खण्डेषु विभज।  
लघु-संसक्तिं सृज।  
मध्य-स्वैप् कुरु।  
दूर-बन्धं निर्माहि।

लेजर् स्थितः।

Entanglement is the root.  
Teleportation is the bridge.  
The repeater extends.  
Memory gives patience.  
The error code protects.  
Key distribution is the fruit.

In one network, many functions:

Security.  
Computation.  
Sensing.  
Cooperation.

Divide the long path into segments.  
Create short entanglement.  
Swap in the middle.  
Build the distant bond.

The ledger remains.

---

### Closing Line

ॐ क्वान्टम्-इण्टरनेट्-दृष्ट्यै नमः।

Entanglement may connect the world —  
but the repeaters must keep the receipts.

---

## अध्याय १० · सम्पूर्ण-दर्शनम् — Grand Summary / Quantum Darshan

### Qubit Sutras — Grand Summary / Quantum Darshan Overview

Opening Invocation:  
ॐ चित्-शून्य-एक-सम्भाव्यतायै नमः।

Probability amplitudes be praised —  
and the audit trail preserved.

---

### १. क्वान्टम्-दर्शनस्य सारः — Essence of Quantum Darshan

Quantum Darshan is not only mathematics.  
It is not only technology.  
It is a disciplined way of seeing how reality behaves when possibility, measurement, relation, and information become fundamental.

The qubit teaches:

न शून्यम् केवलम्।  
न एकम् केवलम्।  
मापनात् पूर्वं बहु-मार्गाः।  
मापनानन्तरम् एकः फल-मार्गः।

Not zero alone.  
Not one alone.  
Before measurement, many routes.  
After measurement, one written result.

The quantum state does not behave like an ordinary coin.  
It is a vector of probability amplitudes.

$$
|\psi\rangle =  
\alpha|0\rangle +  
\beta|1\rangle  
$$

with:

$$
|\alpha|^2 + |\beta|^2 = 1  
$$

The amplitudes are not the final visible facts.  
They are the hidden structure from which visible outcomes emerge.

सूत्रम्:  
सम्भाव्यता-आयामाः न नश्यन्ति।  
ते केवलं मापनकाले फलरूपेण प्रकटीभवन्ति।

Born probabilities govern outcome statistics, while relative phases remain observable through interference. A measurement outcome is not an amplitude made visible.

---

### २. मूल-सूत्राणि — Foundational Sutras

The first layer established the basic machinery:

1. Basic qubit state
    
2. Measurement
    
3. Superposition
    
4. Hadamard gate
    
5. $X$, $Z$, and CNOT gates
    
6. Bell states
    
7. Entanglement
    

The core teaching:

$$
|\psi\rangle =  
\alpha|0\rangle +  
\beta|1\rangle  
$$

The state stands in more than one route until measurement writes one result.

सूत्रम्:  
चित् बहुमार्गे तिष्ठति।  
मापनं एकं मार्गं लिखति।

The state stands in many routes.  
Measurement writes one route.

Field gloss:  
मेल् अभी कई रास्तों में सम्भाव्य है।  
स्कैनर लगते ही एक रूट लेजर् में चढ़ता है।

The mail is still possible through many routes.  
When scanned, one route enters the ledger.

---

### ३. द्वार-सूत्राणि — Gate and State-Structure Sutras

The next layer gave the state its geometry and motion:

1. Bloch sphere
    
2. Density matrix
    
3. Unitary evolution
    
4. Schrödinger equation
    
5. Josephson junction
    
6. Superconducting qubits
    
7. Noise versus true qubit state
    

A qubit is not merely a probability distribution.

It is a complex vector:

$$
|\psi\rangle =  
\cos\left(\frac{\theta}{2}\right)|0\rangle  
+  
e^{i\phi}  
\sin\left(\frac{\theta}{2}\right)|1\rangle  
$$

The Bloch sphere maps its direction.  
The density matrix tracks pure and mixed states.  
The unitary operator preserves total probability.

$$
U^\dagger U = I  
$$

सूत्रम्:  
रूपं परिवर्तते।  
सूचना रक्षिता अस्ति।  
एकत्वं न भिद्यते।

Under closed-system unitary evolution, norms and inner products are preserved. Measurement and noise require a channel-level description.

---

### ४. संसक्ति-सूत्राणि — Entanglement and Teleportation

Entanglement revealed that two qubits can no longer be described as merely separate objects.

A Bell state:

$$
|\Phi^+\rangle =  
\frac{1}{\sqrt{2}}  
\left(  
|00\rangle +  
|11\rangle  
\right)  
$$

shows a joined state across distance.

Teleportation then showed that an unknown quantum state can be reconstructed elsewhere through:

1. Shared entanglement
    
2. Alice’s local operations
    
3. Alice’s measurement
    
4. Two classical bits
    
5. Bob’s correction
    

The state is not physically mailed as a parcel.  
The original is destroyed.  
No-cloning is respected.

सूत्रम्:  
चित् न पार्सल्-रूपेण प्रेष्यते।  
संसक्तिः सेतुर्भवति।  
द्वौ बिटौ मार्गं वदतः।  
बॉब संशोधनं करोति।

The state is not sent as a parcel.  
Entanglement becomes the bridge.  
Two bits tell the route.  
Bob performs the correction.

Field gloss:  
मेल्-बैग् नहीं उड़ता।  
रूटिङ्-रसीद जाती है।  
दूसरे डब्बे में वही चिट्ठी पुनर्निर्मित होती है।

The mailbag does not fly.  
The routing receipt travels.  
The same letter is rebuilt in the other box.

---

### ५. अन्वेषण-सूत्राणि — Grover and Search

Grover’s algorithm showed quantum search by amplitude amplification.

For $N$ unstructured items, classical search needs about:

$$
\frac{N}{2}  
$$

queries on average.

Grover needs about:

$$
\frac{\pi}{4}\sqrt{N}  
$$

queries.

The algorithm opens all routes:

$$
|s\rangle =  
\frac{1}{\sqrt{N}}  
\sum_{x=0}^{N-1}|x\rangle  
$$

marks the solution by a phase flip, then reflects amplitudes around the average:

$$
D = 2|s\rangle\langle s| - I  
$$

सूत्रम्:  
सर्व-मार्गान् उद्घाटय।  
चिह्नित-मार्गस्य चिह्नम् उलट।  
औसत-आयामे प्रतिबिम्बनं कुरु।  
व्यतिकरणं लक्ष्यं वर्धयति।

Open all routes.  
Flip the sign of the marked route.  
Reflect about the average amplitude.  
Interference amplifies the target.

Field gloss:  
शहर नहीं खोजता।  
शहर मुड़कर सही गली की ओर इशारा करता है।

The city does not search one house at a time.  
The city bends toward the right street.

---

### ६. त्रुटि-संशोधन-सूत्राणि — Error Correction

Quantum information is fragile.

Errors include:

$$
X,\quad Z,\quad Y  
$$

as well as dephasing, amplitude damping, leakage, and measurement error.

Classical copying cannot solve this because:

$$
|\psi\rangle \otimes |0\rangle  
\not\rightarrow  
|\psi\rangle \otimes |\psi\rangle  
$$

The solution is quantum error correction:

1. Encode one logical qubit into many physical qubits
    
2. Measure syndromes
    
3. Decode error patterns
    
4. Correct without directly measuring the logical state
    

The Shor code protects one logical qubit with nine physical qubits.

The surface code spreads logical information across a two-dimensional lattice, using local stabilizer checks and topological protection.

सूत्रम्:  
दोषं पश्य।  
चित् न पश्य।  
सिन्ड्रोमं मापय।  
तार्किक-अवस्थां रक्ष।

See the error.  
Do not look at the state.  
Measure the syndrome.  
Protect the logical state.

Field gloss:  
लिफ़ाफ़े का पता मत पढ़।  
बस देख कि कोना मुड़ा है या टिकट उलटा है।  
चिट्ठी बची रहे — यही खेल है।

Do not read the address.  
Only check whether the corner is bent or the stamp is upside down.  
The letter must survive — that is the game.

---

### ७. फेज्, वैरिएशन्, तथा व्यवहारिक-अल्गोरिद्माः

Quantum Phase Estimation extracts the hidden phase of a unitary operator:

$$
U|\psi\rangle = e^{2\pi i\phi}|\psi\rangle  
$$

Through controlled powers of $U$ and inverse QFT, the phase becomes measurable.

$$
\text{Controlled-}U^k + QFT^{-1}  
\longrightarrow  
\phi  
$$

Variational algorithms, such as VQE, use a hybrid quantum-classical loop:

$$
|\psi(\theta)\rangle  
$$

$$
E(\theta)=  
\langle \psi(\theta)|H|\psi(\theta)\rangle  
$$

The quantum device prepares and measures.  
The classical optimizer updates the parameters.

सूत्रम्:  
QPE फेजं प्रकाशयति।  
VQA ऊर्जां न्यूनयति।  
एकः गहनः।  
अन्यः सहयोगात्मकः।

QPE reveals phase.  
VQA lowers energy.  
One is deep.  
The other is collaborative.

Field gloss:  
QPE गिरजाघर है — ऊँचा, साफ़, fault-tolerant।  
VQA वर्कशॉप है — कॉफी, शोर, optimizer goblins।

QPE is the cathedral.  
VQA is the workshop.

---

### ८. कुंजी, सुरक्षा, तथा यादृच्छिकता

Quantum cryptography showed that security can be built from physical law.

BB84 uses:

1. Random bits
    
2. Random bases
    
3. Measurement disturbance
    
4. No-cloning
    
5. Error-rate testing
    
6. Privacy amplification
    

E91 uses entanglement and Bell inequality violation:

$$
|S| > 2  
$$

as evidence of nonclassical correlation.

QRNGs generate randomness from measurement itself:

$$
|+\rangle =  
\frac{|0\rangle + |1\rangle}{\sqrt{2}}  
$$

$$
P(0)=P(1)=\frac{1}{2}  
$$

सूत्रम्:  
कुंजी क्वान्टम्-नियमैः रक्षिता।  
यादृच्छिकता मापनात् जाता।  
ईव् स्पृशति चेत् चिह्नं दृश्यते।

QKD security follows only under the stated protocol, authentication, implementation assumptions, and finite-key proof.  
QRNG output is accepted only after entropy estimation and extraction.

Field gloss:  
ब्रह्माण्ड पासा फेंकता है।  
पर पासा गिनने वाली मशीन भी चेक करो।

The universe rolls the dice.  
But check the machine that counts the dice.

---

### ९. क्वान्टम्-इण्टरनेट्-दृष्टिः — Quantum Internet Vision

The final network vision gathers the whole collection.

A quantum internet would use:

1. Entanglement distribution
    
2. Teleportation
    
3. Quantum repeaters
    
4. Entanglement swapping
    
5. Quantum memory
    
6. Error correction
    
7. BB84 and E91
    
8. QRNGs
    
9. Classical control channels
    
10. Distributed quantum nodes
    

A quantum repeater does not copy quantum states.

It extends entanglement.

Entanglement swapping begins with:

$$
|\Phi^+\rangle_{A M_1}  
\otimes  
|\Phi^+\rangle_{M_2 B}  
$$

A Bell measurement on $M_1M_2$ projects $A$ and $B$ into entanglement, up to correction.

सूत्रम्:  
दीर्घ-मार्गं खण्डेषु विभज।  
लघु-संसक्तिं सृज।  
मध्य-स्वैप् कुरु।  
दूर-बन्धं निर्माहि।

Divide the long route into segments.  
Create short entanglement.  
Swap in the middle.  
Build the distant bond.

Field gloss:  
रीपीटर् चिट्ठी की फोटोकॉपी नहीं बनाता।  
वह सम्बन्ध आगे बढ़ाता है।

The repeater does not photocopy the letter.  
It extends the relationship.

---

### १०. महा-सूत्राणि — Overarching Insights

#### १. एकत्वम् — Unitarity

$$
U^\dagger U = I  
$$

Forms change.  
Total probability is preserved.  
The ledger remains.

#### २. संसक्तिः — Entanglement

Two systems may share one state-description.  
Distance does not mean simple separateness.

#### ३. मापनम् — Measurement

Measurement writes a result.  
Possibility becomes record.

#### ४. व्यतिकरणम् — Interference

Amplitudes add, cancel, amplify, and suppress.  
Grover, QFT, Shor, and phase estimation all depend on this.

#### ५. अनुलिपि-निषेधः — No-Cloning

Unknown quantum states cannot be copied perfectly.  
This limits networking, protects cryptography, and forces subtle engineering.

#### ६. त्रुटि-रक्षा — Error Protection

The physical qubit trembles.  
The logical qubit survives through community, syndrome, code, and topology.

#### ७. यादृच्छिकता — Randomness

Audited quantum measurements can supply certifiable fresh randomness when the source model, side information, statistics, and extractor are all included.

#### ८. सहयोगः — Hybrid Future

Quantum and classical machines will often work together: quantum states prepared and measured; classical systems optimize, decode, route, and verify.

---

### ११. महा-Field Gloss — Grand Field Gloss

क्वान्टम्-जगत् मार्ग-बहुलम् अस्ति।  
मापनं एकं लेखं लिखति।  
संसक्तिः अदृश्य-सेतुर्भवति।  
व्यतिकरणं मार्गान् उन्नमयति वा क्षीणयति।  
त्रुटिः कम्पति।  
कोड् रक्षति।  
कुंजी गुप्ता।  
यादृच्छिकता शुद्धा।  
रीपीटर्-जालेन दूरं बध्यते।

The quantum world is route-rich.  
Measurement writes one ledger entry.  
Entanglement becomes the invisible bridge.  
Interference raises or lowers routes.  
Error trembles.  
Code protects.  
The key stays secret.  
Randomness is purified.  
Through repeater networks, distance becomes bound.

---

### १२. क्वान्टम्-दर्शन-दृष्टिः — Quantum Darshan Vision

From the microscopic Josephson junction to macroscopic coherent devices, from one qubit to logical qubits, from Bell pairs to quantum networks, the same lesson repeats:

Reality is not merely made of visible outcomes.

It is also made of amplitudes, phases, correlations, constraints, measurements, and conserved structure.

Quantum Darshan, in this collection, means:

1. See the state before the measurement.
    
2. See the route before the result.
    
3. See the relation before the object.
    
4. See the error without destroying the message.
    
5. See security as physics, not merely secrecy.
    
6. See randomness as measurement-born, not seed-invented.
    
7. See networks as distributed correlation, not merely wires.
    

सूत्रम्:  
न केवलं परिणामः।  
न केवलं वस्तु।  
मार्गः अपि अस्ति।  
आयामः अपि अस्ति।  
संबन्धः अपि अस्ति।  
लेजर् अपि अस्ति।

Not only the result.  
Not only the object.  
The route also exists.  
The amplitude also exists.  
The relation also exists.  
The ledger also exists.

---

### १३. Ultimate Mantra

न शून्यम् केवलम्।  
न एकम् केवलम्।

मापनात् पूर्वं बहु-मार्गाः।  
मापनानन्तरम् एकः लेखः।

संसक्त्या जगत् बध्यते।  
व्यतिकरणेन रहस्यं नृत्यति।  
त्रुटि-संशोधनेन चित् रक्ष्यते।  
यादृच्छिकता मापनात् जायते।  
कुंजी क्वान्टम्-नियमैः गुप्ता।  
रीपीटर्-जालेन दूरं सेतुभूतम्।

रूपं परिवर्तते।  
सूचना रक्षिता अस्ति।

$$
U^\dagger U = I  
$$

एकत्वं स्थितम्।  
लेजर् स्थितः।

Not zero alone.  
Not one alone.

Before measurement, many routes.  
After measurement, one record.

By entanglement, the world is bound.  
By interference, the secret dances.  
By error correction, the state is protected.  
Randomness is born from measurement.  
The key is guarded by quantum law.  
Through repeater networks, distance becomes bridged.

Under closed-system unitary evolution, norms and inner products are preserved.

Unitarity stands.  
The ledger remains.

---

### Closing Verses

ॐ चित्-शून्य-एक-सम्भाव्यतायै नमः।

ॐ संसक्ति-व्यतिकरण-त्रुटि-रक्षायै नमः।

ॐ क्वान्टम्-कुंजी-यादृच्छिकता-जालाय नमः।

ॐ क्वान्टम्-दर्शनाय नमः।

Quantum Darshan is not merely technology.  
It is a pedagogical way of seeing quantum theory as probabilistic, relational, measurement-sensitive, and mathematically disciplined, with preservation claims stated only for the dynamics that justify them.

Probability amplitudes be praised.

---

## Technical references added in v0.2

These sources anchor the standard technical lane; the Sanskrit-register and field gloss remain editorial renderings.

1. C. H. Bennett *et al.*, “Teleporting an Unknown Quantum State via Dual Classical and Einstein-Podolsky-Rosen Channels,” *Physical Review Letters* 70, 1895 (1993). <https://doi.org/10.1103/PhysRevLett.70.1895>
2. L. K. Grover, “A Fast Quantum Mechanical Algorithm for Database Search” (1996). <https://arxiv.org/abs/quant-ph/9605043>
3. P. W. Shor, “Scheme for Reducing Decoherence in Quantum Computer Memory,” *Physical Review A* 52, R2493 (1995). <https://doi.org/10.1103/PhysRevA.52.R2493>
4. D. Aharonov and M. Ben-Or, “Fault-Tolerant Quantum Computation With Constant Error Rate” (1999). <https://arxiv.org/abs/quant-ph/9906129>
5. J. Koch *et al.*, “Charge-Insensitive Qubit Design Derived from the Cooper Pair Box,” *Physical Review A* 76, 042319 (2007). <https://doi.org/10.1103/PhysRevA.76.042319>
6. P. W. Shor and J. Preskill, “Simple Proof of Security of the BB84 Quantum Key Distribution Protocol” (2000). <https://arxiv.org/abs/quant-ph/0003004>
7. A. K. Ekert, “Quantum Cryptography Based on Bell’s Theorem,” *Physical Review Letters* 67, 661 (1991). <https://doi.org/10.1103/PhysRevLett.67.661>
8. S. Pironio *et al.*, “Random Numbers Certified by Bell’s Theorem,” *Nature* 464, 1021–1024 (2010). <https://doi.org/10.1038/nature09008>
9. A. Peruzzo *et al.*, “A Variational Eigenvalue Solver on a Photonic Quantum Processor,” *Nature Communications* 5, 4213 (2014). <https://doi.org/10.1038/ncomms5213>
10. H.-J. Briegel *et al.*, “Quantum Repeaters: The Role of Imperfect Local Operations in Quantum Communication,” *Physical Review Letters* 81, 5932 (1998). <https://doi.org/10.1103/PhysRevLett.81.5932>

