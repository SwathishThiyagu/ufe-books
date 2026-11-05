# c-xr-u5: free-model run

- Book: `books/cse/c-xr/c-xr-u5.html`
- Status: ok
- Model calls so far: 25 (80,602 tokens in, 172,602 out), 6.9 minutes

## Checker

```
c-xr-u5.html: 8 chapters, 14302 words, 9 figures, 148 KB
OK
```

## For the reviewer

- chapter 3: the figure cannot be drawn: tree is too wide (8 leaves); use fewer leaves or shorter labels
- chapter 3: the figure could not be drawn; a plain box diagram stands in for it

## Reviewer notes (after any revision)

- ch 1 [low] Section 3, design rules: The sentence 'set gain so small hand motions make large object motions only when needed' is ambiguous. It mixes up two opposite needs: coarse travel (where you want amplification) and fine placement (where you want a small, 1:1 or reduced mapping). A student can read it either way.
- ch 1 [low] Quiz Q7: The answer lists 'a lower gain' as a way to reduce fatigue. A lower gain means more hand travel for the same object movement, so it increases arm movement and fatigue. This also contradicts the design rule in Section 3 that asks for amplification when large object motion is needed.
- ch 1 [low] Section 2, ray-casting formula: q is described as 'the closest point on the ray', but q = p + t u with t = (c − p)·u is the closest point on the infinite line. When t < 0 the closest point on the actual ray is p, not q. The selection test t ≥ 0 hides this, but the definition as written is loose.
- ch 2 [low] Section 2, layout bullet: 'short decision points' is unclear and mixes up the idea: it is the number and complexity of decision points that matter, not their length.
- ch 2 [low] Section 3, matching paragraph: 'Keep one aid per decision point' is ambiguous; a reader may think only one sign may exist in the whole world.
- ch 2 [low] Section 1, first paragraph: 'The user moves through the scene, while objects stay fixed' is contradicted later by world scaling, where the world appears to shrink or grow around a nearly stationary user.
- ch 2 [low] Exam traps, user-centred versus environment-centred aids: Signs are listed as user-centred aids here, but signs are physically placed in the world, so some syllabi call them environment-centred; the chapter does not warn of this split.
- ch 3 [low] Exam traps, trap 2: The clause "even if both use a hand gesture" contradicts the example itself: rotating the bolt may use a pinch, but saying "next step" is a voice command. A student can read this as saying both commands are given by hand, which muddles the point that the channel does not decide the class.
- ch 3 [low] Lead and Section 1: "Some syllabi call this command and control" appears twice word for word, once in the lead and again at the end of Section 1. It reads as a copy-paste slip.
- ch 4 [low] Section 3, OpenSceneGraph sentence: State set is listed as a node type, but in OpenSceneGraph osg::StateSet is not a node. It is a state attribute container attached to a node's drawables or to a group; the node types are Group, Transform (MatrixTransform/PositionAttitudeTransform) and Geode.
- ch 4 [low] Lead and Section 1, definition of scene graph: The chapter says a scene graph is a tree only. Most toolkits (OpenSceneGraph and most engines) let one node be shared by several parents, so the structure is really a directed acyclic graph, and that sharing is how instancing is done. A student who reads only 'tree' will not recognise a shared subtree.
- ch 4 [low] Quiz Q3: The answer suggests a child cannot get its world transform without depth-first order, but a breadth-first walk level by level also knows every parent transform before its children. Depth-first is chosen because a stack naturally pushes and pops transforms and render state on the way down and back up.
- ch 4 [low] Section 2, formula term list: T_T is described as 'the transform of T, M's parent'. In a deeper tree that is ambiguous: what multiplies p_local is the accumulated transform from the root down to T, not T's own local transform. The example is correct only because the root is identity and T has a single translation.
- ch 5 [high] Beyond: URP, HDRP, Lumen and Nanite are grouped as 'render pipelines'. URP and HDRP are Unity render pipelines, but Lumen is Unreal's global illumination system and Nanite is its virtualised geometry system; neither is a render pipeline. A student will mislabel them in a viva.
- ch 5 [low] Section 3, workflow paragraph: Says both engines target VR headsets and phones 'through OpenXR'. OpenXR is the cross-vendor API mainly for VR/MR headsets; phone AR is normally built with ARCore or ARKit, not OpenXR.
- ch 5 [low] Section 1, final sentences: Chapter 5.4 is named in plain text but not given as a chapter link, so a phone reader cannot jump to the scene graph chapter.
- ch 5 [low] Quiz Q4 answer: The answer writes 'ceiling(60 ÷ 15)' while the formula and all other answers use ceil(); the inconsistent name may make students think it is a different function.
- ch 6 [low] section 3, code block: The [shown output] block after the script is empty. A student sees a blank output panel and cannot tell whether the script prints anything.
- ch 6 [low] section 2: 'The engine detects contacts in FixedUpdate' is inaccurate about the order. FixedUpdate runs first, then the physics simulation step, and the collision and trigger callbacks come after the simulation in that same fixed cycle. A student may think contact detection happens inside their FixedUpdate code.
- ch 6 [low] section 1, raycast sentence: 'Physics.Raycast(origin, direction, out hit, distance, layerMask) returns the first hit' is misleading. The method returns a bool (true if something was hit); the hit details are written into the out parameter hit.
- ch 6 [low] section 1 and quiz Q4: Trigger callbacks need a Rigidbody on at least one of the two objects. The chapter never states this, so a student whose trigger silently does nothing has no clue why.
- ch 6 [low] figure spec: The figure shows the message 'move object' from Script to Display, but section 2 says the physics engine updates positions. The two descriptions of who moves the object disagree.
- ch 6 [low] section 1, cross-reference: The pointer 'see 3D manipulation and travel' is plain text, so it does not work as a chapter link on a phone.
- ch 7 [high] Section 2, emergency stop definition: It says an emergency stop is a control that 'pauses the app and lifts the display'. Software cannot lift the display; a button, voice command or gesture cannot physically move the headset. A student will read this as a mechanical action and be confused about what the stop actually does.
- ch 7 [low] Section 2, safety boundary: 'Guardian boundary' is one vendor's product name used as if it were the general term. Some syllabi use chaperone boundary or safety boundary, and readers meeting the generic idea for the first time may think only one brand has it.
- ch 8 [low] Section 1, Feedback guideline: The sentence 'Delay above about 100 ms starts to feel disconnected' is fine for a button or menu response, but in a head-tracked VR scene the tolerance is far smaller. Motion-to-photon latency of a few tens of milliseconds already causes visible lag. As written, a student may conclude that 100 ms of tracking lag is acceptable in a headset.
- ch 8 [low] Section 2 and Worked example 1 / figure: Section 2 says 'Half the users see A first, half see B first', which means the same users test both designs (within-subjects). The worked example then says the designs are 'tested by 20 users each' and the figure labels the rows 'A users' and 'B users', which reads as two separate groups of 20 (between-subjects, 40 people). The two descriptions do not match and the denominator of 20 becomes ambiguous.
- ch 8 [low] Figure (success and error counts table): The table has no column headings, so only the first number in each row is explained by the caption and the aria text. The values 4, 34, 2 and 37 (non-completers and correct attempts) are left undefined.
- ch 8 [low] Section 3, NASA-TLX bullet: NASA-TLX is described as having 'mental, physical and time demands'. The standard instrument has six subscales: mental demand, physical demand, temporal demand, performance, effort and frustration. Naming three may lead students to think these are the only ones.
