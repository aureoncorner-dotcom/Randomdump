# Appendix B v0.3 — Paths, closure and mixing

## 1. Three separate questions

Formal sector increments say which subgroup might be generated. Full-state reachability asks whether enabled paths exist from the declared starting state. Mixing asks whether the actual chain explores its target distribution adequately on the measured time scale. An answer to one does not supply the other two.

For a concrete counterexample take states A, B, C, D with q labels 00, 10, 00, 01, and only bidirectional edges A↔B and C↔D. Across the graph the increment labels span both binary directions. Starting at A, only q=00 and q=10 are accessible. A successful rank check over global labels cannot repair a disconnected state graph. Conversely, the explicitly declared cube of eight labels with enabled unit-axis flips is connected; this checks that finite action, not a physical kernel.

## 2. Addressed cocycles

Every path record declares whether one step is a proposal, accepted elementary operator, completed worm, macro-sweep or retained measurement. At that address,
\[
\eta_k=q_{k+1}-q_k\pmod2,\qquad
c(m,n)=\sum_{k=m}^{n-1}\eta_k=q_n-q_m\pmod2.
\]
The identity follows by telescoping. It says nothing about how much internal motion was hidden by the address. Keep \(\Delta W\) on the source-free domain: an even increment has zero \(\eta\), and opposite signed increments cancel. Rejected proposals retain identity events. Bootstrap joins are not trajectory events.

## 3. Universal versus stationary closure

For a complete finite full-state kernel P and label map \(\pi\), strong closure requires
\[
\sum_{z:\pi(z)=b}P(x,z)=\sum_{z:\pi(z)=b}P(y,z)
\quad\text{whenever }\pi(x)=\pi(y),\text{ for every }b.
\]
The finite checker uses exact rational entries and returns a differing pair as a witness. Its result names the supplied domain. A sample of matching contexts yields only `SAMPLE_CONSISTENT`; missing coverage yields `UNRESOLVED`. When no autonomous law is claimed, use a separate `NOT_CLAIMED` record.

The included kernel is
\[
P=\begin{pmatrix}1/10&1/10&4/5\\2/5&2/5&1/5\\1/4&1/4&1/2\end{pmatrix},
\qquad \pi=(A,A,B).
\]
States 0 and 1 have next-A probabilities 1/5 and 4/5, so strong closure fails. Nevertheless \(\mu=(1/4,1/4,1/2)\) is stationary. The first two columns are identical, so conditional on observing A after a transition, its two hidden states have equal probability regardless of the preceding history. At stationarity the initial conditional law also has that property. From that equal mixture, next-A probability is 1/2; from B it is also 1/2. Therefore the stationary A/B process is independent fair draws. The tests separately enumerate all length-five words. Failure of universal closure does not exclude this stationary weak closure.

This example is not the original FH-REF-1 physical-mixture example and does not transfer its conclusions to another kernel. Both remain scoped to their own definitions.

## 4. Work stopping changes the question

Draw independent fair bits, charging one unit of work for 0 and two for 1. Stop on reaching at least two units. The terminal bit is 1 if the first draw is 1 (probability 1/2), or if the first is 0 and the second 1 (probability 1/4). Hence the endpoint law is \((1/4,3/4)\), despite each draw being fair.

This exact finite example shows why an accepted-work stopping schedule needs its own stationarity proof. It does not demonstrate bias in the unexecuted worm sampler. A fixed number of target-preserving steps is a sufficient alternative when their hypotheses hold. State-dependent stopping, selection and retention rules must be included in the kernel being validated.

## 5. Required empirical records

Keep topology, formal paths, observed accessibility, stationarity, mixing, scale admissibility and physical interpretation in distinct fields. Use the inherited effective round trips, multi-chain diagnostics and rare-sector alternatives in [the protocol](02_Simulation_Protocol_v0.6_Consolidated.md). The lattice fixtures supply no empirical values for them. Axis and placement equivalence needs declared tolerances and simultaneous intervals; paired resampling preserves their covariance. A non-significant difference test alone is insufficient.
