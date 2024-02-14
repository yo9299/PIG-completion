== problems, results, organization

For any two real numbers $a, b in RR$, we define the _closed interval_ (_open interval_) of endpoints $a$ and $b$ as the set $[a, b] := {x in RR | a <= x <= b}$ (the set $(a, b) := {x in RR | a < x < b}$, and the two _semi-open intervals_ $[a, b)$ and $(a, b]$. The interval is _integer_ if $a,b in NN$. Two _intervals intersect_ if they contain a same point of $RR$. Where $I$ is an interval, then $a_I$ ($b_I$) denotes the left (the right) endpoint of $I$.

In much literature, the terms _multiset_ and _family_ are used interchangeabily when dealing with sets in which a same object (or identical objects) may apper multiple times as an element of the set. The _multiplicity_ of an object is the number of its occurrences as a member of the family.
A family of intervals $cal(I)$ can be used to represent the graph $G_cal(I)$ having node set $V(G) = cal(I)$ and edge set $E(G)$ comprising those pairs of intervals in $V(G)$ that intersect. Any graph $G=(V,E)$ that can be represented in this way is called an _interval graph_. It is well-kown and easy to show that for every interval graph $G$ there exists a family of _closed intervals_ $cal(I)$ such that $G=G_cal(I)$. It can also be assumed that all intervals in $cal(I)$ are integer.
An interval graph $G=(V,E)$ is called _proper_ if it contains no induced $K_(1,3)$.
A family of intervals $cal(I)$ is called _proper_ if for every two intersecting intervals $I,J in cal(I)$ we have that $I$ contains at least one endpoint of $J$ and $J$ contains at least one endpoint of $I$. Clearly, $G_cal(I)$ is proper whenever the interval family $cal(I)$ is proper. The converse is also true.

*Fact:* Every proper interval graph $G$ admits a proper interval representation by closed and integer intervals.

_proof:_ Let $cal(I)$ be any family of closed and integer intervals such that $G=G_cal(I)$.
Start from any family of closed and integer intervals $cal(I)$ and if an interval $[a,b] in cal(I)$ can be replaced by the smaller interval $[a+1,b]$ (or $[a,b-1]$) without affecting $G_cal(I)$, then perform this replacement.
Keep on shrinking the intervals in $cal(I)$ as long as possible. Clearly this is a finite process and, where $cal(I)'$ is the current interval family at any step, the process respects the following invariants: 1. $G_(cal(I)')=G_cal(I)$, 2. every interval in $cal(I)'$ is closed and integer.
Notice that, when the process has come to an end, then $cal(I)'$ is proper since on one side $G_(cal(I)')$ contains no induced $K_(1,3)$ and on the other $cal(I)'$ contains both an interval $[x,a]$ and an interval $[b,y]$ for every $[a,b] in cal(I)'$.
QED

The event-set at time $t$ for a family of closed intervals $cal(I)$ is the set of those intervals in $cal(I)$ that have either the form $[t,t']$ with $t'>=t$ or the form $[t',t]$ with $t'<=t$; this is actually a multiset for when $t'=t$ we have a double insertion of the same interval. The _log_ of $cal(I)$ is the ordered sequence of all the non-empty event-sets for $cal(I)$ as we observe them when $t$ moves from left to right. Note that two families $cal(I)_1$ and $cal(I)_2$ have the same log whenever they are both obtained from a same starting family $cal(I)$ by conducting up to termination the shrinking procedure described in the proof here above. This unique log $"sign (cal(I))"$ is called the signature of $cal(I)$.

*Example:* if $cal(I) = {I_1,I_2,I_3,I_4,I_6,I_4,I_7}$ with $I_1=[0,4]$, $I_2=[1,5]$, $I_3=[2,13]$, $I_4=[6,10]$, $I_5=[7,11]$, I_6=[8,8], I_7=[9,9], then $"sign (cal(I))" = {I_1,I_2}, {I_3}, {I_1,I_2}, {I_4,I_5}, {I_1,I_2}, {I_6,I_6}, {I_7,I_7}, {I_3,I_4,I_5}$.

An interval graph is called _rigid_ if all its interval representations have the same signature (possibly after total reversal of the order of the list). I would expect that this notion of rigidity for interval graphs has been studied and fully characterized for interval graph (as it has been for othes classes like planar graphs). If not, it would be worth working it out and offering it as of added value, otherwise we better refer to what known and avoid introducing our own silly notations. (We might find convenient making use of it in the points indicated more below.)

An _extension_ of an interval graph $G=(V,E)$ is any interval graph $G=(V,E')$ with $E' supset E$. The extension is called _proper_ if $G=(V,E')$ is a proper interval graph.

*Problem [`Min_Interval-to-Proper-Iterval-Graph-Completion`]:*
   Given in input an interval graph $G=(V,E)$, find a proper extension $G=(V,E')$ of $G$ with $|E'|$ as small as possible.

An _extension_ of a family of closed intervals $cal(I)$ is a pair $(cal(I)',f)$ where $cal(I)'$ is a family of closed intervals and $f:cal(I) -> cal(I)'$ is a bijection such that $I subset.eq f(I)$ for every $I in cal(I)$. The extension is called _proper_ if $cal(I)'$ is a proper family of closed intervals.

*Problem [`Min_Interval-to-Proper-Iterval-Family-Completion`]:*
   Given in input a family of closed intervals $cal(I)$, find a proper extension $cal(I)'$ of $cal(I)$ with $|E(G_(cal(I)'))|$ as small as possible.

We are working at organizing a proof that Problem `Min_Interval-to-Proper-Iterval-Family-Completion` is NP-hard.
In fact, we believe that from here we should also obtain a downhill proof that Problem `Min_Interval-to-Proper-Iterval-Graph-Completion` is NP-hard as well.
The way we could possibly like to frame this out would be:

+ introduce this dynamic notion of rigidity for interval families: A family of closed intervals $cal(I)$ is called _rigid_ if for every proper extension $G'$ of $G_cal(I)$ there exists an extension $cal(I)'$ of $cal(I)$ such that $G'=G_(cal(I)')$.

+ prove that $cal(I)$ is dynamically rigid if and only if $G_cal(I)$ is rigid.

+ prove that Problem `Min_Interval-to-Proper-Iterval-Family-Completion` is NP-hard even when restricted to dynamically rigid input (by observing that our reduction always yields interval families $cal(I)$ such that $G_cal(I)$ is rigid and application of 2.).

Not only we are still quite wavy on how our proof of the NP-hardness of Problem `Min_Interval-to-Proper-Iterval-Family-Completion` might possibly be also read as a proof of the NP-hardness of Problem `Min_Interval-to-Proper-Iterval-Graph-Completion` but it is clear that we would grately benefit, both in effort and final quality of our contribution and its proper exposition, from a better awareness of what already done in the literature concerning steps 1 and 2 hypothesized here above and the notions of rigidity, log, and signature. Again, it is most likely that these notions and issues have been already investigated and polished out in the literature (if not, this could be a good occasion to spend and throw out such a study that would certainly find even other applications, e.g., in the study of isomorphism checking and retrival for these classes of graphs).
Clearly, it is most wise to start from and adhere to what is already known. Also for this reason, I would see best Virginia on this front since she is the one among us three with more background and commitment into this topic area.

== the NP-hardness proof

=== preliminary results

The following one allows us to use weighted (i.e., with multiplicities) families of intervals.

*Fact:* For every family of closed intervals $cal(I)$ there always exist an optimal solution $(cal(I)',f)$ to the `Min_Interval-to-Proper-Iterval-Family-Completion` Problem such that for any two intervals $I,J in cal(I)$ with $a_I=a_J$ and $b_I=b_J$ then $a_(f(I))=a_(f(J))$ and $b_(f(I))=b_(f(J))$ also holds.

_proof:_
Let $I,J in cal(I)$ with $a_I=a_J$ and $b_I=b_J$ and assume we have a solution where $a_(f(I))!=a_(f(J))$ (respectively $b_(f(I))!=b_(f(J))$).
Let $c_I, c_J$ be the respective costs of paid by $I$ and $J$ (i.e. the number of intervals they intersect).
If $c_I = c_J$, we have an equivalent solution where $a_(f(I))=a_(f(J))$ (respectively $b_(f(I))=b_(f(J))$)
If $c_I != c_J$, we can make the interval with the higher cost equal to the one with lower cost, thus lowering the total cost and having that $a_(f(I))=a_(f(J))$ (respectively $b_(f(I))=b_(f(J))$).
QED

*Fact:* For every family of closed intervals $cal(I)$ there always exist an optimal solution $(cal(I)',f)$ to the `Min_Interval-to-Proper-Iterval-Family-Completion` Problem such that every interval in $cal(I)'$ is contained in some interval of $cal(I)$. (In particular, the maximal intervals in $cal(I)$ are left unenlarged.)

_proof:_
// TODO: Fix this
// For any family of closed intervals $cal(I)$, being proper is equivalent to saying that each interval $I in cal(I)$
// should contain at least one extremity of all the intervals it intersects.
// Suppose we have an interval $J' in cal(I)'$ (corresponding to an interval $J in cal(I)$) such that $#sym.exists.not I in cal(I) | J' in I$.
// Look a the intersection between $J$ and $cal(I)$:
// - If $J$ intersects only itself, then there is no reason to change the interval, so $J = J'$.
// - If $J$ intersects other intervals, let $L, R$ be respectively the leftmost beginning and rightmost ending intervals intersecting with $J$.
//   We would have that $cal(I)'$ $a_J < a_L$ and $b_R < b_L$, but for the above definition of proper interval is enough that
//   $a_J = a_L$ and $b_R = b_L$, since $L$ and $R$ are proper and enlarging $J'$ more can only increase the cost and


QED


*Fact:* For every family of closed intervals $cal(I)$ there always exist an optimal solution $(cal(I)',f)$ to the `Min_Interval-to-Proper-Iterval-Family-Completion` Problem such that for every interval $I' in cal(I)'$ either $a_(I') = a_(f^(-1)(I'))$ or there exists a maximal interval $J in cal(I)$ such that $a_(I') = a_J$. (And the symmetric holds for the other endpoint of $I'$.

_proof:_
I do not think a proof will be needed.




*Fact:* For every family of closed and integer intervals $cal(I)$ there always exist an optimal solution $(cal(I)',f)$ to the `Min_Interval-to-Proper-Iterval-Family-Completion` Problem such that every interval in $cal(I)'$ is closed and integer and for any two intervals $I,J in cal(I)$ with $a_I=a_J$ and $b_I=b_J$ then $a_(f(I))=a_(f(J))$ and $b_(f(I))=b_(f(J))$ also holds.

_proof:_
It should appear to be just a corollary of the above.



== the problem we reduce from

Let $D=(V,A)$ be a directed graph, and $S subset.eq V$.
Then $delta^+(S) := {(u,v)in A | u in S, v in.not S}$ is called the _dicut_ in $D$ of _out-shore_ $S$ (and _in-shore_ $V without S$).


*Problem [`Max_Dicut`]:*
   Given in input a directed graph $D=(V,A)$, find an $S subset.eq V$ maximiziong $|delta^+(S)|$.

The NP-hardness of max dicut follows from the observation that the
well-known undirected version of max dicut — the maximum cut problem
(max cut), which is on the original Karp’s list of NP-complete problems —
reduces to max dicut by substituting each edge for two oppositely oriented
arcs.

== the reduction

Assume given an instance of the `Max_Dicut` Problem in decision form,
that is, a directed graph $D=(V,A)$ and a number $delta in NN$. We are asked to decide whether there exists an $S subset.eq V$ such that $|delta^+(S)| >= delta$. Let $n:=|V|$, $m:=|A|$, and assume the nodes in $V$ are labelled by the naturals $0, ..., n-1$.
Let $A={a_0, ..., a_(m-1)}$ with $a_j=(u_j,v_j)$ for every $j=0,...,m-1$.
In order to represent this instance, we define a family of closed and integer intervals $cal(I)_D$.
This family of intervals is organized in four subfamilies that play distinct roles in the reduction:

/ the rulers: these $8 m n$ intervals have length $L:=2n$ and multiplicities of the highest order.
  For every $r in {0,1}$, $v in V$, $g in {0,1,2,3}$, and $j=0,...,m-1$, the ruler $R_(j,g,v,r) = [r + 2(v + n (g + 4 j)),  r + 2(v + n (g + 4 j)) + L]$ is also indexed as $R_(8 n j + 2 n g + 2 v + r)$. We see rulers as organized in $4 m$ stages of $2 n = L$ consecutive rulers each: ruler $R_(r, v, g, j)$ is of stage $g + m j$. Some rulers have a _discounted multiplicity_ of $M_3 := (4 m n + 1)^3$ but most rulers have the _full multiplicity_ of $M_3 + 2$. We will specify which rulers have discounted multiplicity only when defining the last subfamily of intervals (i.e., the cars).

/ the lorries: these $4 m n$ intervals have length $L-2$ and multiplicity $M_2 := (4 m n + 1)^2$.
  For every $v in V$, $g in {0,1,2,3}$, and $j=0, ..., m$ we have a lorry $L_(j,g,v) = [1 + 2(v + n (g + 4 j)),  2(v + n (g + 4 j )) + L - 1]$.

/ the walls: these $2 n$ intervals have multiplicity $M_1 := (4 m n + 1)$.
  For every $v in V$ we place a left wall $W^L_v = [2 v - L, 2 v]$ and a right wall $W^R_i = [2 v + 8 m n, 2 v + 8 m n + L]$.

/ the cars (the digraph encoding subfamily) and the discounted rulers: these $2 m$ intervals of length $0$ and multiplicity $1$ are actually the only intervals whose layout depends on $A(D)$ (all previous subfamilies are fully determined once $m$ and $n$ are fixed, except for which rulers have multiplicity only $M_3$). For every arc $a_j=(u_j,v_j) in A(D)$, define the group $g_(j,v_j) := 2$ and $"stage"_(j,v_j) := 4 j + g_(j,v_j)$ parameters, and consider these two cases: \
  *Case 1 ($u_j < v_j$):* define the parameters $g_(j,u_j) = 2$ and $"stage"_(j,u_j) := "stage"_(j,v_j)$. \
  *Case 2 ($u_j > v_j$):* define the parameter $g_(j,u_j) = 1$ and $"stage"_(j,u_j) := "stage"_(j,v_j) - 1$. \
  We hope the placement of the two cars $C_(j,u_j) = ["stage"_(j,u_j) L + 3 u_j, "stage"_(j,u_j) L + 3 u_j]$ and $C_(j,v_j) = ["stage"_(j,v_j) L + 3 v_j, "stage"_(j,v_j) L + 3 v_j]$ to be more transparent in terms of these descriptive parameter.
  In both cases $p_u < p_v <= L - 2$, where $p_u$ ($p_v$) is the only point in $C_(j,u_j)$ (in $C_(j,v_j)$). In the first case $p_u$ and $p_v$ are the left endpoints of rulers of a same stage, in the second case the ruler for $p_u$ is of the previous stage. We now specify the $4$ rulers that get discounted multiplicity to finalize the encoding of the arc $a_j$: where ${p_x,p_y}:={p_u,p_v}$ with $p_x < p_y$, the ruler with right endpoint in $p_x$, the ruler with right endpoint in $p_x - L + 1$, the ruler with left endpoint in $p_y$, the ruler with left endpoint in $p_y + L - 1$.

Clearly, the instance $cal(I)_D$ can be constructed in polynomial time from any reasonable encoding for $D$.

(Andrea, check out the description of the reduction, and fill in the proofs and arguments below.)

*Fact:* Any enlargemet of all cars to length $L-1$ closed integer intervals is a feasible solution.

_proof:_
Andrea, dry/coincise and sharp.
QED

Define a canonical solution to be a solution as in the above fact.

*Fact:* Every feasible solution comprising only closed integer intervals "contains (=intervals inclusions after bijection)" a canonical solution.

_proof:_
Andrea, dry/coincise and sharp.
QED

Given a canonical solution $cal(I')$, let $E^c(cal(I'))$ the set of those edges of $G_(cal(I'))$ which have two cars as endpoints and let $G^(overline(c))_(cal(I')) := G_(cal(I')) without E^c(cal(I'))$.

*Fact:* $|E(G^(overline(c))_(cal(I')))| = $CONSTANT_TOT for every canonical solution $cal(I')$.

_proof:_
Andrea, dry/coincise and sharp. It is likely that you will have to specify the CONSTANT_TOT number but see what is most supportive and less pain for the reader.
QED


*Fact [Easy Lemma]:* Let $D=(V,A)$ be a directed graph, and $S subset.eq V$. Then the `Min_Interval-to-Proper-Iterval-Family-Completion` instance $cal(I)_D$ admits a canonical solution $cal(I)'$ such that $|E( G_(cal(I)') )| <=$ CONSTANT_TOT $+ m - |delta^+(S)|$ arcs.

_proof:_
Andrea, dry, plain, and supporting.
QED



*Fact [Hard Lemma]:*
Let $D=(V,A)$ be a directed graph, and $cal(I)'$ be a canonical solution for the `Min_Interval-to-Proper-Iterval-Family-Completion` instance $cal(I)_D$. Then there exists an $S subset.eq V$ with $|delta^+(S)| >= $ CONSTANT_TOT $ + m - |E( G_(cal(I)') )|$.

_proof:_
Andrea, even just only a first structuring and identification of the main arguments/challenges.
QED

