# s-chem-u1: free-model run

- Book: `books/common/s-chem/s-chem-u1.html`
- Status: ok
- Model calls so far: 26 (87,713 tokens in, 199,770 out), 6.8 minutes

## Checker

```
s-chem-u1.html: 9 chapters, 12764 words, 10 figures, 148 KB
OK
```

## For the reviewer

- nothing flagged

## Reviewer notes (after any revision)

- ch 1 [low] Section 1, photoelectric effect: The threshold frequency ν₀ is used but never connected to the work function, so a student cannot see that φ = hν₀ and that ν₀ = φ/h.
- ch 1 [low] Section 1, first sentence: 'A black body absorbs and emits all wavelengths' can be read as saying it emits every wavelength equally; that is not the Planck spectrum.
- ch 1 [low] Section 2, de Broglie paragraph: 'of atomic size' is vague; a student cannot tell what number to remember.
- ch 1 [low] Figure caption: The caption gives Δp = 0.5/Δx 'in scaled units' but never says which constant was set to 1, so it does not visually match Δx Δp ≥ ħ/2.
- ch 1 [low] Worked example 1: The relation Δx Δp ≥ ħ/2 is stated for position and momentum of a particle; applying it to a photon to get a 'position uncertainty' is an order-of-magnitude estimate only, and the answer 3.2 × 10⁻⁵ m is far larger than the 400 nm wavelength, which a student may find odd.
- ch 1 [low] Beyond: 'the Heisenberg microscope' is named without any explanation, and it is not part of the chapter.
- ch 2 [low] Section 1: The sentence 'This is why a confined particle cannot have any energy' literally reads as 'the particle has zero energy', which contradicts E₁ > 0 stated in Section 2.
- ch 2 [low] Section 1, Born rule: Probability density is called 'probability per unit volume' inside a one-dimensional problem, and the normalisation is written with dV, so the 1D student may be confused about which measure to use.
- ch 2 [low] Section 1, boundary conditions: The list 'single-valued, continuous and finite' omits the continuity of the first derivative, which is the standard condition (except at an infinite step).
- ch 2 [low] Figure: The y-axis is labelled E_n, but the plotted values are 1 to 36, i.e. n² times E₁, not joules. A student may read the numbers as energies in J.
- ch 2 [low] Lead: 'its energies are quantised as n²' is unclear phrasing; n is not yet defined and 'quantised as n²' is loose.
- ch 3 [low] Section 3, periodic trends: The sentence 'Electron affinity becomes more negative' assumes the enthalpy sign convention, but many first-year Indian textbooks define electron affinity as the energy released (a positive number). A student using that convention will read this as the opposite trend.
- ch 3 [low] Worked example 1, dry run output: The output field shows two bare numbers, '8.8' and '2.2', with no labels, so the reader cannot tell which is S and which is Zeff, and cannot see the units are elementary charge.
- ch 3 [low] Figure and Section 3: Spelling switches between 'ionisation' in the text and 'Ionization energy' in the figure label and the aria text.
- ch 4 [low] Section 1, paragraph on σ and π orbitals: The phrase 'has a nodal plane along that line' is ambiguous: a student may read it as a plane perpendicular to the internuclear line. The nodal plane of a π MO contains the internuclear line.
- ch 4 [low] Section 2, table: The column is headed 'Valence configuration', but the H2 and He2 rows show σ1s² and σ1s² σ*1s², which are 1s orbitals, not valence 2s/2p orbitals like the rows below. The mixed use can confuse the reader about what 'valence' means in the table.
- ch 4 [low] Quiz Q1 answer: The answer writes N_b and N_a with underscores, but the chapter defines the terms with subscripts (N<sub>b</sub>, N<sub>a</sub>). Plain underscore notation is not standard and looks like a typo on a phone screen.
- ch 5 [high] quiz Q7: The question and answer assume diamond melts and that molten diamond can be tested for conductivity. Diamond does not melt at ordinary pressure — it converts to graphite and sublimes above roughly 3900 K — and liquid carbon is itself an electrical conductor, so 'diamond does not conduct when molten' is a false statement, not a teaching simplification.
- ch 5 [low] section 1: Hydrogen bonding is described only through the O–H···O example; the term itself is never defined, so a student cannot state what a hydrogen bond is in the exam.
- ch 5 [low] section 2: 'For a stable contact, anions touch each other and the cation sits in the hole between them' describes only the limiting case at the lower edge of each range, but reads as if anions always touch in every stable ionic solid.
- ch 5 [low] section 3: The cross-reference is plain text ('See Unit 6'), so it will not behave as a link in the book.
- ch 6 [low] Exam traps, trap 1: The trap says not to count CO as 'CO2+'. No standard convention treats CO as a 2+ ligand, and on a phone screen 'CO2+' reads like CO₂⁺ (carbon dioxide cation), so the warning confuses more than it warns. The real ligand where the neutral/ionic choice bites is NO (NO+ = 2e, NO = 3e).
- ch 6 [low] Exam traps, halide trap: The neutral-ligand instruction is incomplete. Counting each halide as one electron and lowering the metal oxidation state does not by itself give the same total for a charged complex: in [FeCl6]3− the ionic count is 5 + 12 = 17, but the stated method gives 8 + 6 = 14. The charge on the complex must also be added.
- ch 6 [low] Section 2, 18-electron rule: The relation d = group number − x is presented as if it holds only for first-row metals. It holds for all transition metals (Pt2+, group 10, gives d8), so the restriction can mislead a student working on 4d and 5d complexes later in the chapter.
- ch 7 [high] Lead paragraph: The lead says "This splitting is called crystal field theory". The splitting is not the theory; the splitting is a physical effect, and crystal field theory is the electrostatic model that explains it. A student would carry away a wrong definition of the theory itself.
- ch 7 [high] Section 3, paragraph comparing high spin and low spin: The comparison sign has been lost/corrupted in two places: "If Δo o > P" and "Low spin wins when −1.6Δo + P o". As printed the condition cannot be read, and the second statement does not say what CFSE it is being compared with.
- ch 7 [high] Quiz Q4 answer: Same corrupted inequality: "Low spin is favoured when −1.6Δo + P o, which simplifies to Δo > P." The missing comparison makes the derivation unreadable and the jump to Δo > P unjustified.
- ch 7 [high] Section 2, square planar paragraph: The orbital order given for square planar, dz² > dxy > dxz, dyz, contradicts the standard textbook order. For a square planar d⁸ complex the in-plane dxy is raised above dz²; the usual order is dx²−y² > dxy > dz² > dxz = dyz.
- ch 8 [high] Worked example 1, step 3: For d5 low spin, t2g holds only 5 electrons. That is two pairs plus one unpaired electron, not 'three pairs' (three pairs would be six electrons). The sentence contradicts its own conclusion n = 1.
- ch 8 [low] Lead: The symbol Δo appears in the lead before it is defined, which is the first thing a phone reader sees.
- ch 9 [low] Figure (sets spec): The figure caption promises hard acids and bases on one side and soft acids and bases on the other, but the 'Hard' set contains only cations (H+, Mg2+, Al3+) and the 'Soft' set mixes cations (Ag+, Hg2+) with an anion (I−). A student can read the soft set as 'soft acids' and be confused about whether I− is an acid.
- ch 9 [low] Beyond: Pb2+ is called a soft metal, but in the standard Pearson classification Pb2+ is borderline, not soft. Chelation therapy for lead in fact uses hard O donors (EDTA) as well as soft S donors, which contradicts the sentence as written.
