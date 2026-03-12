# GrimGlow — Meshy.ai 3D Environment Component Prompts

> **Purpose:** Modular 3D asset prompts for Meshy.ai. Each prompt generates one reusable component that can be assembled in Three.js (Phase 1) or Unity (Phase 2) to build authentic 1885 London environments.
>
> **Feed alongside:** Booth poverty map sheets, Goad fire insurance plans, and Victorian reference photos from `world-building/maps/` and `world-building/reference-photos/`.

---

## 1. Global Style Rules

### Materials Palette — What 1885 London Actually Looks Like

| Material | Description | Where Used |
|---|---|---|
| **London stock brick** | Yellow-brown, NOT red. Slightly irregular, sooty. This is the default building material for everything south of Regent's Park. | Walls, chimney stacks, warehouse facades |
| **Welsh slate** | Dark grey-blue, thin overlapping tiles. Every roof in urban London. | Roofs — NOT thatch, NOT tile |
| **Cast iron** | Black or dark green painted. Fluted, ornate Victorian patterns. | Lamp posts, railings, bollards, drain covers |
| **Portland stone** | Pale cream-white limestone. Used for churches, public buildings, some shop fronts. | St John's Gate, churches, bank facades |
| **Timber (painted)** | Mostly dark green, maroon, or cream. Glossy oil paint. | Shop fronts, window frames, doors |
| **Granite setts** | Grey or pink-grey, roughly rectangular. NOT smooth cobblestones. Individual stones ~11x13 inches with 1/4–1 inch gaps filled with tar or earth. | Road surfaces — every road |
| **York stone** | Pale grey-buff flagstones. Large rectangular slabs. | Pavements (sidewalks) |
| **Lead** | Dull grey, soft. Flashing around chimneys and roof joints. | Roof details, gutter linings |
| **Copper/brass** | Tarnished green-brown copper on roofs and gutters. Brass on door furniture, shop fittings. | Downpipes, door handles, gas fittings |
| **Glass** | Small panes in sash windows (6-over-6 or 4-over-4). Larger plate glass in shop fronts (1880s innovation). | Windows |

### Atmospheric Rules

- **Smoke and soot:** Everything has a thin film of coal soot. Brickwork is darker at the top of buildings and around chimney stacks. Window sills accumulate black grime. This is London's signature.
- **Fog:** Not white — yellowish-grey. The famous "pea-souper" comes from coal smoke mixing with Thames fog. Visibility drops to yards. Gaslight creates yellow-orange halos in fog.
- **Gaslight:** Warm amber-orange. Casts sharp downward pools with soft falloff. Every 30-50 yards on main streets; much scarcer on back streets and courts. No electric light exists.
- **Wet surfaces:** London is frequently damp. Granite setts gleam. Brick darkens when wet. Puddles in gutters reflect gaslight.

### Anti-Patterns — What Will Make Londoners Cringe

| DO NOT | INSTEAD |
|---|---|
| Red brick everywhere | **London stock brick** (yellow-brown) — red brick is Manchester/Birmingham, not London |
| Tudor timber-frame beams | Georgian/Victorian brick facades with sash windows — Tudor is 300 years earlier |
| Smooth cobblestones | **Granite setts** — rectangular, rough-cut, with visible gaps |
| Thatch roofs | **Welsh slate** — this is urban London, not a village |
| Wide American-style streets | Narrow lanes (8-12 feet) with buildings tight to the road. No front lawns. No setbacks. |
| Modern lamp posts | **Fluted cast-iron columns** with crossbar brackets and glass lantern heads |
| Electric wires or lights | **Gas lamps only.** No power lines. No bulbs. Gas mantles inside glass lanterns. |
| Neon or plastic signs | **Hand-painted timber signs.** Projecting from walls on iron brackets. |
| Clean buildings | **Everything is sooty.** Coal smoke coats every surface. |
| Generic "steampunk" gears | The base architecture is REAL 1885 London. The steampunk is a 10-15% additive layer, not a replacement. |

### The Steampunk Additive Layer

The world is real Victorian London with a subtle mechanical enhancement:
- Gas lamp fittings have extra brass valves, pressure gauges, and decorative gear wheels
- Chimneys have slightly more complex pipe configurations — extra vents, steam outlets, pressure relief valves
- Workshop windows display clockwork mechanisms, exposed gears, precision instruments
- Occasional brass pneumatic message tubes run along building facades
- The fog/smoke is 10% thicker, more atmospheric, more golden-amber
- Iron railings have slightly more intricate geometric patterns
- Everything is 10-15% more mechanical than reality — but the bones are REAL London

---

## 2. Building Component Prompts

### 2.1 Georgian Terrace Section — Clerkenwell

```
3D model of a two-story Georgian terrace house section, London stock brick (yellow-brown) with grey Welsh slate roof. Brick slightly sooty and weathered. Two six-over-six sash windows per floor with white-painted timber frames, stone lintels and sills. Black-painted front door with brass knocker and letter slot, stone doorstep, semi-circular fanlight above door. Thin iron area railings in front, protecting a narrow basement lightwell. Chimney stack at party wall with three cylindrical clay chimney pots. Cast-iron downpipe from roof gutter, painted black. Flat facade with no setback — building sits directly on the pavement edge. Narrow proportions: approximately 15 feet wide, 25 feet tall to eaves. Neutral grey background, even studio lighting, four views: front elevation, three-quarter, side profile, rear.
```

### 2.2 Clockmaker's Workshop Frontage — Clerkenwell

```
3D model of a small Victorian workshop shop front, ground floor only. Clerkenwell clockmaker's establishment, circa 1885. London stock brick facade (yellow-brown, sooty). Large plate glass shop window with dark green painted timber surround, gold leaf lettering reading "HOROLOGY" on the fascia board. Display window contains visible clock mechanisms, brass gears, watch faces. Recessed doorway with glazed upper panel. Projecting painted timber sign on an iron bracket. Gas lamp bracket mounted on the wall beside the door. Above the shop: two sash windows for the living quarters, lace curtains visible. Slightly exaggerated brass and copper mechanical details in the window display — exposed clockwork, small gear trains, precision instruments. Grey Welsh slate visible at roofline. Neutral grey background, even studio lighting, four views: front, three-quarter, side, rear.
```

### 2.3 Industrial Warehouse — Bermondsey

```
3D model of a four-story Victorian industrial warehouse, Bermondsey tannery district style, circa 1885. London stock brick (yellow-brown), heavily soot-stained especially upper floors. Small arched windows with iron frames, many with cracked or missing panes. Large timber loading doors at each floor with projecting iron hoist beam and pulley wheel at the top. Ground floor has wide arched entrance for cart access. Roof is grey Welsh slate with multiple chimney stacks trailing smoke residue stains. Iron tie-rod plates visible on facade (cross-shaped or S-shaped). Narrow lane between this and adjacent building — gap barely six feet wide. Drain pipe runs down one corner. General atmosphere of heavy industrial use — stained, weathered, functional, not decorative. Neutral grey background, even studio lighting, four views.
```

### 2.4 Tannery Building — Bermondsey Long Lane

```
3D model of a Victorian tannery works building, Bermondsey, circa 1885. Long low structure, London stock brick, two stories. Ground floor: wide open arches for ventilation (tanning chemicals need air flow). Upper floor: timber-framed drying loft with slatted wooden walls for airflow — hides hung to dry. External timber drying frames extending from the upper floor, draped with leather hides in various stages of processing. Cobbled yard in front with drainage channels. Stack of bark (tanning material) piled against one wall. Strong functional architecture — no decoration, purely industrial. Small office section at one end with a regular window and painted door. Chimney stack with extra industrial venting pipes. Neutral grey background, even studio lighting, four views.
```

### 2.5 Dock Warehouse — Wapping

```
3D model of a massive six-story brick warehouse, London Docks style, Wapping, circa 1885. London stock brick, blackened with age and soot. Imposing cliff-like facade. Small arched windows with iron grilles on all floors — security against theft. Massive arched entrance at ground level, large enough for loaded carts. Each upper floor has a projecting loading beam with chain hoist. Cast-iron columns visible inside the ground-floor arch. Roof parapeted (no visible slope from street level). Iron wall anchors (cross-shaped tie plates) at regular intervals. Cobbled loading apron in front. The scale should feel oppressive — this building dwarfs everything around it. From fairy scale (4 inches tall), this building is a sheer cliff face hundreds of fairy-feet high. Neutral grey background, even studio lighting, four views.
```

### 2.6 Public House Exterior — General London

```
3D model of a corner Victorian public house (pub), circa 1885. Three stories, London stock brick upper floors. Ground floor wrapped in decorative dark green glazed tile or painted timber with etched and frosted glass windows. Projecting painted pub sign on iron bracket reading "THE CROWN." Corner entrance with ornate iron columns. Gas lamp mounted on wall bracket beside entrance. Upper floor windows: standard sash, lace curtains. Roofline: Welsh slate with chimney stacks. Warm, inviting appearance at ground level contrasting with plain domestic upper floors. Brass door handles, kickplates. Slightly more ornate than surrounding buildings — pubs were the most decorated commercial buildings in working-class neighborhoods. Neutral grey background, even studio lighting, four views.
```

### 2.7 Church Facade — St James Clerkenwell

```
3D model of a Georgian parish church facade in the Clerkenwell style, circa 1730 but shown in its 1885 condition. Portland stone (cream-white) with significant soot staining. Classical portico with Doric columns. Square tower with clock face. Arched windows with clear leaded glass. Iron railings around a small churchyard. Moss and damp staining on north-facing stone. Welsh slate roof. Gravel path to entrance. Tombstones visible in the yard — dark stone, weathered, leaning. The church is clean Portland stone underneath soot — cream showing through where rain has washed the surface. Neutral grey background, even studio lighting, four views.
```

### 2.8 Chimney Cluster

```
3D model of a Victorian London chimney stack cluster, isolated component for rooftop placement. Four chimney pots on a shared London stock brick base. Pots are cylindrical terra cotta, different heights (12-18 inches each), with decorative crown tops. Brick base shows lead flashing where it meets the roof slope. Soot staining heaviest on the downwind side. One pot has a half-round rain cowl. Base dimensions approximately 3x2 feet. Detailed enough to serve as a fairy-scale fortification/observation tower. Neutral grey background, even studio lighting, four views.
```

### 2.9 Jeweller's Shopfront — Hatton Garden

```
3D model of a prosperous Victorian jeweller's shop front, Hatton Garden district adjacent to Clerkenwell, circa 1885. Portland stone ground floor facade with London stock brick upper stories. Large plate glass display window with ornate dark green painted timber surround and gilt lettering: "GOLDSMITH & JEWELLER." Window displays velvet-lined trays of rings and watch chains behind iron security grilles that fold back during business hours. Recessed entrance with mosaic tile threshold and brass-framed glass door. Projecting gas lantern bracket with decorative ironwork. Upper floors: three sash windows with stone lintels, curtains drawn. More prosperous and ornate than the typical Clerkenwell workshop — carved stone corbels, polished brass door furniture. Neutral grey background, even studio lighting, four views.
```

### 2.10 Printing Press Workshop — Clerkenwell

```
3D model of a small Victorian printing workshop frontage, Clerkenwell, circa 1885. London stock brick, two stories, narrow frontage approximately 12 feet wide. Ground floor: wide timber double doors (open to show interior) revealing a Columbian hand press visible inside — cast iron eagle counterweight on top, ink-stained wooden frame. Type cases in wooden racks along the wall. Stacks of printed sheets on a table. Ink smell implied by stained floor and splattered apron hanging by the door. Small window beside the doors with "HARTLEY — JOBBING PRINTER" in painted lettering. Upper floor: two sash windows, one cracked open. Chimney stack with single pot. Workshop is modest, working, honest — not prosperous but not destitute. Neutral grey background, even studio lighting, four views.
```

### 2.11 Common Lodging House — Clerkenwell

```
3D model of a Victorian common lodging house, Clerkenwell, circa 1885. London stock brick, three stories, narrow and deep. Externally unprepossessing — a painted board over the door reads "REGISTERED COMMON LODGING HOUSE." Ground floor: plain door, one small window with no display. Upper floors: windows closer together than a normal house — subdivided rooms behind them. Curtains mismatched or absent. Paint peeling on window frames. Roof slate patched in places. One chimney stack per floor (multiple fireplaces for multiple rooms). The building looks compressed — too many people for the space. A gas lamp bracket on the wall by the entrance. Basement area railing, steps down. Neutral grey background, even studio lighting, four views.
```

### 2.12 Corner Chandler's Shop — Clerkenwell

```
3D model of a Victorian corner chandler's shop (general store), Clerkenwell, circa 1885. London stock brick, two stories, on a street corner with entrances on both sides. Large timber shop front wrapping the corner — dark maroon painted with cream lettering: "TEAS — CANDLES — SOAP — PROVISIONS." Display window crammed with goods: stacked tins, hanging bundles of candles, boxes of matches, wrapped soap bars. Open doorway with goods spilling onto the pavement — sacks of coal, bundles of firewood, a barrel of salted herrings. Painted tin advertisement signs nailed to the wall above: "FRY'S COCOA" and "SUNLIGHT SOAP." Domestic upper floor with sash windows and lace curtains. Chimney stack. Neutral grey background, even studio lighting, four views.
```

### 2.13 Speculative Workshop Block — Clerkenwell

```
3D model of a Victorian multi-floor workshop block, Clerkenwell precision trades district, circa 1885. London stock brick, four stories, purpose-built for letting individual floors to different craftsmen. Wider than a terrace house — approximately 25 feet — with a central staircase entrance. Each floor has large multi-pane windows for maximum daylight (essential for precision work). Ground floor: wider arched entrance for deliveries. Small painted name boards beside the door listing tenants: "CLOCKMAKER — 2ND FLOOR," "WATCH CASE MAKER — 3RD FLOOR." Slight Gothic decorative touches in the brickwork — pointed arch window heads, a simple stringcourse between floors. Welsh slate roof. Multiple chimney stacks. Iron fire escape ladder bolted to the side wall. Neutral grey background, even studio lighting, four views.
```

### 2.14 Back-to-Back Workers' Housing — Bermondsey

```
3D model of a Victorian back-to-back workers' dwelling, Bermondsey, circa 1885. London stock brick, two stories, extremely narrow — approximately 10 feet wide. One room per floor. Ground floor: single sash window beside a plain painted door, no front area or railing — door opens directly onto the pavement. Upper floor: one sash window, smaller. Roof: Welsh slate, single chimney pot. The building shares rear walls with an identical dwelling facing the opposite street — no back windows, no yard, no through-ventilation. Brickwork heavily sooted. Paint peeling. Window glass cracked and patched with paper. Damp staining at ground level. Washing line strung across the narrow street to the building opposite. This is the cheapest, meanest housing in London. Neutral grey background, even studio lighting, four views.
```

### 2.15 Biscuit Factory Exterior — Bermondsey

```
3D model of a large Victorian biscuit factory, Bermondsey industrial district, circa 1885. Peek Frean style. London stock brick, five stories, imposing industrial facade approximately 60 feet wide. Regular rows of large iron-framed windows on every floor. Ground floor: wide arched cart entrance with iron gates. Loading bay with timber platform. Name painted in large white letters on the upper wall: "BISCUIT MANUFACTORY." Three tall chimney stacks with constant smoke output — the ovens run continuously. Cast-iron downpipes at regular intervals. Iron fire escape staircase on the side. Upper floor windows glow warm from the baking halls. A clock mounted on the facade — factory time governs the workers' day. Neutral grey background, even studio lighting, four views.
```

### 2.16 Riverside Wharf Building — Bermondsey

```
3D model of a Victorian riverside wharf building, Bermondsey waterfront near St Saviour's Dock, circa 1885. London stock brick, three stories, built right to the river's edge. Ground floor: wide arched openings onto the water — barges load and unload directly into the building. Upper floors: timber loading doors with projecting hoist beams and pulley chains. Iron cranes on the wharf apron. Timber fenders along the waterline, green with algae. Mooring rings set into the wall. The building straddles a narrow inlet — water visible beneath the arched ground floor. Soot-blackened brick. Smell of spices, tobacco, and river mud. Cobbled wharf apron in front with bollards and coiled rope. Neutral grey background, even studio lighting, four views.
```

### 2.17 Railway Arch Workshop — Bermondsey

```
3D model of a Victorian railway arch workshop, beneath a brick viaduct, Bermondsey, circa 1885. The arch itself is engineering brick (darker, harder than stock brick) forming a massive semicircular vault approximately 20 feet wide and 15 feet high. The front is infilled with a rough brick wall containing a wide timber door and a small window. Inside visible through the open door: a blacksmith's forge or general repair workshop — anvil, tools on the wall, a small fire. Soot stains radiating from the interior up the brickwork. Vibration cracks visible in the infill wall from trains passing above. Puddles on the cobbled ground from water seeping through the brickwork. A hand-painted sign: "J. PIKE — SMITH & FARRIER." Dark, damp, functional. Neutral grey background, even studio lighting, four views.
```

### 2.18 Bone-Boiling Works — Bermondsey

```
3D model of a Victorian bone-boiling and rendering works, Bermondsey, circa 1885. London stock brick, low sprawling structure, single story with a tall chimney stack belching greasy smoke. Wide yard enclosed by a brick wall, gate open showing piles of animal bones and offal awaiting processing. Large iron vats visible through open shed walls — the boiling vats where bones are rendered for glue, tallow, and fertilizer. Drainage channels in the cobbled yard running with greasy liquid. Stack of wooden barrels for finished products. The building is aggressively functional — no decoration, no pretense. Stained, greasy, reeking. The surrounding buildings keep their windows shut. Neutral grey background, even studio lighting, four views.
```

### 2.19 Gin Distillery — Bermondsey

```
3D model of a small Victorian gin distillery, Bermondsey, circa 1885. London stock brick, three stories, with a distinctive copper still chimney vent on the roof — a short, wide copper pipe venting aromatic steam. Ground floor: large timber doors for grain and barrel deliveries. Small office window with "DISTILLER" painted on it. Upper floors: storage — smaller windows, some bricked up for security. The top floor has louvered ventilation openings for the grain store. A yard gate to one side. Inside glimpsed through the open delivery door: the copper pot still gleaming against sooty brick walls, wooden barrel racks, copper pipe runs along the ceiling. Smell of juniper and grain mash. Neutral grey background, even studio lighting, four views.
```

### 2.20 Waterside Sailors' Pub — Wapping

```
3D model of a Victorian riverside public house, Wapping waterfront, circa 1885. London stock brick, three stories, with the ground floor facing the river via a narrow alley between warehouses. Maritime character: a ship's figurehead mounted above the door, porthole-shaped windows in the upper floors, a painted sign depicting a sailing ship — "THE PROSPECT OF WHITBY" or similar. Ground floor: dark-stained timber exterior with etched glass windows, heavier and more battered than an inland pub. Low ceiling visible inside. Cobbled river stairs descending beside the building to the Thames mud. A timber balcony projecting over the river at the rear. Mooring rings in the river wall. Gas lamp on an iron bracket. More weathered and salt-stained than inland pubs. Neutral grey background, even studio lighting, four views.
```

### 2.21 Customs House / Dock Office — Wapping

```
3D model of a Victorian customs house or dock company office, Wapping, circa 1885. Portland stone facade (cream-white, soot-stained), three stories, more formal and imposing than surrounding warehouse buildings. Classical proportions: pilasters framing the entrance, a pediment above the central door, decorative cornice. "LONDON DOCK COMPANY" carved into the stone lintel. Large sash windows with stone surrounds. Iron railings around a small front area. Uniformed dock police officer's sentry box beside the entrance. The building is clean relative to its neighbors — regularly maintained, authoritative, official. Welsh slate roof. Chimney stacks. A flagpole on the roof. Neutral grey background, even studio lighting, four views.
```

### 2.22 Dock Gate Entrance — Wapping

```
3D model of a Victorian dock gate entrance, London Docks, Wapping, circa 1885. Massive brick gate piers approximately 12 feet tall, topped with stone copings. Heavy timber gates reinforced with iron straps and studs, wide enough for loaded carts. A small gatehouse / lodge built into one pier — single room with a window and a door, where the dock police check entrants. High brick perimeter wall extending to either side, topped with iron spikes. "NO ADMITTANCE EXCEPT ON BUSINESS" painted on a board. Cobbled roadway passing through the gate, worn smooth by iron cart wheels. A gas lamp mounted on the gate pier. Inside the gate: a glimpse of the vast dock basin, warehouse walls, crane silhouettes. At fairy scale, these gates are fortress walls. Neutral grey background, even studio lighting, four views.
```

### 2.23 Hydraulic Pumping Station — Wapping

```
3D model of a Victorian hydraulic pumping station, Wapping, circa 1885. London stock brick with decorative red brick banding — an industrial building designed to impress. Italianate style: arched windows with decorative keystones, a corbelled cornice, ornamental chimney stack approximately 100 feet tall (one of the tallest structures in the docklands). The building houses steam-powered hydraulic pumps that power the dock cranes, lock gates, and swing bridges via high-pressure water mains. Ground floor: massive arched engine room windows showing the tops of beam engines inside. A brass manufacturer's plate on the wall. The chimney is a landmark visible across Wapping — at fairy scale, a mountain-sized tower. Neutral grey background, even studio lighting, four views.
```

### 2.24 Lighterman's Stairs — Wapping Waterfront

```
3D model of Victorian river stairs (lighterman's stairs), Wapping waterfront, circa 1885. Stone steps descending from a narrow alley between warehouses down to the Thames foreshore. Steps are York stone, worn smooth and slippery with river slime and algae. Iron handrail bolted to the warehouse wall on one side. At the bottom: exposed Thames mud at low tide — grey-brown, littered with broken pottery, clay pipes, bones, rope ends. Green weed on the lower steps. Mooring ring set into the wall at water level. The stairs are narrow — two men abreast at most. Warehouse walls rise sheer on both sides, creating a slot canyon effect. At fairy scale, these stairs are a grand staircase descending into a vast mudflat landscape. Neutral grey background, even studio lighting, four views.
```

### 2.25 Railway Viaduct Section — General

```
3D model of a Victorian railway viaduct section, circa 1885. Three consecutive brick arches in engineering brick (blue-grey, harder and darker than stock brick). Each arch approximately 20 feet wide, 15 feet tall. Heavy buttress piers between arches. Iron tie plates visible on the face. The arches are infilled at ground level — one with a workshop door (see Railway Arch Workshop), one bricked up, one open as a passageway. Railway tracks visible on top with low brick parapet walls. Soot staining from locomotives cascading down the brickwork. Puddles beneath the arches from seepage. The viaduct dominates the streetscape — everything around it is in its shadow. Neutral grey background, even studio lighting, four views.
```

### 2.26 Telegraph Office Exterior — General

```
3D model of a Victorian General Post Office telegraph office, circa 1885. London stock brick with Portland stone dressings, two stories. Official GPO style: "TELEGRAPH OFFICE" in gilt letters on a dark green fascia board above the entrance. Large plate glass window displaying postal notices. Crown crest above the door. Green-painted timber shop front. Multiple telegraph wires converging on the roof from different directions — a cluster of ceramic insulators on a timber bracket mounted on the parapet. Inside visible through the window: a counter, clerk positions, wire instruments. Upper floor: office windows. The roof bristles with wire connections — this building is a node in the telegraph network. Neutral grey background, even studio lighting, four views.
```

### 2.27 Tower Bridge Under Construction — Landmark

```
3D model of Tower Bridge under construction, viewed from the south bank, circa 1886-1888 (early construction phase). Two massive stone-clad steel pier bases rising from the river, approximately 50 feet above the waterline but not yet complete. Timber scaffolding and construction hoists surrounding each pier. A temporary wooden footbridge connecting the work sites across the river. Construction barges moored alongside. Steam-powered pile drivers on floating platforms. Workers visible on the scaffolding (human scale reference). The familiar Gothic towers do not yet exist — just raw engineering and dressed Portland stone blocks being hoisted into position. Construction cranes breaking the skyline. The river busy with boat traffic navigating around the work site. Neutral grey background, even studio lighting, four views.
```

### 2.28 Board School — General

```
3D model of a Victorian London Board School, Education Act 1870 style, circa 1885. London stock brick with red brick decorative banding and stone dressings. Three stories, tall and imposing — designed to dominate surrounding terraces. Very large windows on every floor for maximum classroom light — the largest windows on any building in the neighborhood. Central entrance with stone arch and carved inscription: "CLERKENWELL BOARD SCHOOL — BOYS" (or "GIRLS" — schools were gender-segregated). Steep Welsh slate roof with decorative ridge tiles. Bell tower or small clock turret on the roof ridge. High brick playground wall enclosing a cobbled yard. Iron railings along the street frontage. The building reads as institutional, civic, serious. Neutral grey background, even studio lighting, four views.
```

---

## 2B. Story-Specific Location Prompts

These prompts generate set-piece environments tied to specific comic/game moments. Each is a more complex scene rather than a single modular building.

### 2B.1 Crash Site Rain Gutter — Issue 1

```
3D model of a Victorian London rooftop rain gutter containing wreckage, circa 1885. A 4.5-inch half-round cast-iron gutter running along the edge of a Welsh slate roof, viewed at fairy scale (4-inch character perspective). The gutter contains scattered fragments of alien technology — cracked hull plates with faint holographic circuit traces still glowing blue-white, a snapped wing-pack strut, crystalline shards catching light. Scorch marks on the slate tiles and lead flashing around the gutter. The gutter itself is a river-width highway at this scale. In the background: chimney stacks as towers, the roofscape of Victorian London as a mountain range. Soot, rain residue, a dead leaf the size of a blanket. Neutral grey background, even studio lighting, four views.
```

### 2B.2 Ship Wreckage Module — Issue 1-2

```
3D model of a crashed fairy-tech recon vessel fragment, the largest surviving piece, approximately 8 inches long at human scale. Sleek angular hull in degraded silver-white metallic material, cracked and buckled from impact. Exposed interior showing structured holographic light circuits — translucent, prismatic, geometric-edged light trapped in crystalline channels, some flickering, some dead. A cracked viewport. Internal systems visible through hull breaches: miniature conduits, power cell housing (empty), navigation module (dark). The hull exterior is beginning to accumulate London soot. The ship's design language is military, functional, advanced — this is future technology, not fantasy. At fairy scale, this wreckage is a building-sized structure. Neutral grey background, even studio lighting, four views.
```

### 2B.3 Cribbage's Workshop Interior — Fairy Scale — Issue 3-4

```
3D model of a Victorian clockmaker's workbench surface viewed at fairy scale (4-inch character perspective), circa 1885. The workbench is a vast landscape plateau. Scattered across it: brass screws the size of boulders, a magnifying loupe as tall as a person standing on its side, coiled spring wire like industrial cable, tiny gear wheels as large as cart wheels. A candle in a brass holder at the far edge — a blazing tower of flame. A tin of watch oil — a lake. Iron tweezers laid down like a fallen bridge. Wood shavings as large as fallen logs. A pocket watch opened for repair, its movement exposed — gears, jewel bearings, hairspring — an intricate mechanical landscape. The bench surface is scarred, stained with oil and solder. Warm candlelight. Neutral grey background, even studio lighting, four views.
```

### 2B.4 Clockmaker's Shop Interior — Clock Mechanism — Issue 5

```
3D model of the interior of a large display clock mechanism, viewed at fairy scale (4-inch character perspective). Brass gear trains as large as industrial machinery — meshing teeth taller than a person, rotating slowly. A mainspring coil the diameter of a room, under massive tension. Jewel bearings (ruby) glowing deep red. Steel pivots and arbors as thick as tree trunks. An escapement mechanism ticking with metronome regularity — the pallet fork swinging like a pendulum bridge. The clock's dial is visible from behind — translucent numbers reversed, light filtering through. Every surface is precision-polished brass and steel, gleaming. The danger is kinetic — gears mesh, springs release, levers snap. A character caught between meshing gears would be crushed. Neutral grey background, even studio lighting, four views.
```

### 2B.5 Trinity Buoy Wharf Lighthouse — Issue 7

```
3D model of Trinity Buoy Wharf experimental lighthouse, Bow Creek at the Thames confluence, circa 1885. Hexagonal brick tower approximately 30 feet tall, London stock brick, built 1864-66. Lantern room at the top: cast-iron frame with large glass panels housing a Fresnel lens — concentric glass rings focusing light into a beam. Gallery walkway around the lantern room with iron railing. At the base: a single-story keeper's workshop. The setting is isolated — mud flats at low tide, Bow Creek flowing past, industrial buildings in the background but the lighthouse standing alone. This is where Trinity House tests new lamp technologies — Michael Faraday conducted optical experiments here. The Fresnel lens is the prize: precision optics that resonate with fairy holographic technology. At fairy scale, the lighthouse is a colossal tower. Neutral grey background, even studio lighting, four views.
```

### 2B.6 Decommissioned Church Exterior — Issue 8

```
3D model of a small decommissioned Georgian chapel, Bermondsey or Clerkenwell, circa 1885 but built circa 1780 and now abandoned. Portland stone facade, heavily sooted and stained. Arched windows boarded up with timber planks. Main door padlocked, iron chain. A notice: "PREMISES TO BE DEMOLISHED." Churchyard overgrown — weeds pushing through gravel, tombstones leaning, iron railings rusted and bent. A tree growing close to the wall, roots lifting the pavement. Damp staining on the stonework. The building is structurally sound but neglected — roof intact but gutters sagging, downpipe detached. An atmosphere of abandonment. One basement window, barred, at ground level — the entry point. Neutral grey background, even studio lighting, four views.
```

### 2B.7 Church Basement Cache — Issue 8

```
3D model of a sealed church basement room viewed at fairy scale (4-inch character perspective), circa 1885 but containing centuries-old fairy technology. Brick-vaulted cellar with lime-washed walls, damp patches, cobwebs. On a stone ledge: a corroded fairy wing-pack — the struts visible but the holographic emitters dead, metal tarnished to green-black. A dead data core — a small crystalline cylinder, dark, cracked. And carved into the brick wall in the fairy written language, the glyph for "STAY" — clean geometric lines cut into the mortar, still sharp after centuries. The room is small, dry, sealed. Dust on every surface undisturbed. A faint sense that this was deliberately prepared — a message left for whoever came next. Neutral grey background, even studio lighting, four views.
```

### 2B.8 Central Telegraph Office Interior — Issue 10-12

```
3D model of a Victorian telegraph relay room interior, General Post Office, circa 1885. A long room filled with rows of telegraph instruments on wooden desks — Wheatstone ABC telegraphs, single-needle instruments, Morse sounders. Overhead: a dense canopy of wires running along the ceiling on porcelain insulators, converging from all directions. Operators' chairs (empty). Gas light fixtures hanging from the ceiling. The room hums with electrical activity — clicking instruments, vibrating wires. At fairy scale, the wire canopy overhead is an aerial highway network. The telegraph instruments are building-sized machines with moving parts. Paper tape spools as large as barrels. Battery jars (glass, filled with acid) on shelves — toxic at any scale. Neutral grey background, even studio lighting, four views.
```

### 2B.9 Titan-Modified Telegraph Device — Issue 10

```
3D model of a Victorian telegraph instrument that has been modified by Titan technology. Base: a standard Wheatstone ABC telegraph — wooden case, brass mechanism, wire connections. Grafted onto it: alien technology — dark, oil-on-water iridescent material, organic-looking conduits that wrap around the brass mechanism like parasitic vines. The Titan additions pulse with a slow, wrong light — not the clean geometric holographics of fairy tech but something that shifts and shimmers like petroleum on water. Shadow seems to cling to the device even in direct light. The Victorian mechanism still functions — the Titan tech is additive, parasitic, subtly steering the signals. The contrast between warm brass and dark iridescence is unsettling. Neutral grey background, even studio lighting, four views.
```

### 2B.10 Theodore's Garret Room — Issue 12

```
3D model of a small Victorian garret bedroom above a workshop, Clerkenwell, circa 1885. Low sloping ceiling following the roof pitch — exposed lath and plaster, a damp patch in one corner. Single sash window with a view of rooftops and chimneys. A narrow iron-frame bed with a patchwork quilt. A small wooden writing desk and chair by the window — on the desk: a candle in a brass holder (lit), an inkwell, a steel-nib pen, and a sheet of paper with writing visible. A washstand with basin and pitcher. Pegs on the wall for clothes — a coat, a cap. A shelf with a few books and, half-hidden behind them, a small glowing shard of fairy technology that Theodore has kept. The room is small, clean, poor, personal. Warm candlelight against blue moonlight from the window. Neutral grey background, even studio lighting, four views.
```

### 2B.11 Theodore's Shoe-Shine Alcove — First Contact Location — Issue 3

```
3D model of a tiny recessed street-level alcove beneath a Victorian shop front, Clerkenwell side street, circa 1885. The alcove is approximately 4 feet wide and 3 feet deep — a niche in the building facade, not a proper shop. Above: a larger grocer's shop window displaying provisions (tins, bottles, boxes, hand-lettered signs for eggs, butter, lemonade). Below: Theodore's shoe-shine spot. An upturned wooden crate serves as a seat. A folded cloth on the York stone pavement displays a few pairs of shoes left for collection or repair. A small wooden shoe-shine box sits open: tins of blacking, brushes, rags. The critical detail: a cast-iron storm drain grate sits in the pavement immediately to the left of the alcove — rectangular, approximately 18 inches long, 6 inches wide, with parallel iron bars. The drain drops into darkness below. At fairy scale, this drain grate is a portcullis — the iron bars frame the entrance to an underground tunnel network. The alcove puts Theodore at pavement level, eye-to-eye with anything inside that drain. The shop front recess creates a semi-private space where a boy could lean toward a drain grate and whisper without passers-by noticing. Warm gaslight from the grocer's window above, cool evening light on the street. Neutral grey background, even studio lighting, four views.
```

**Visual reference:** `concept-art/reference/The Smallest Shop in London (c. 1900) 👞.jpg`

---

## 3. Street Furniture Prompts

### 3.1 Gas Lamp Post

```
3D model of a Victorian London gas street lamp, circa 1885. Fluted cast-iron column, approximately 8 feet tall, painted dark green. Octagonal stepped base bolted to the pavement. Crossbar bracket at top supporting a square glass-paned lantern head with copper-framed panels. Fish-tail gas burner visible inside (no mantle — Welsbach mantles just invented 1885, not yet widespread). Small brass control tap at the base of the lantern for the lamplighter. Subtle steampunk addition: one small brass pressure gauge on the column and decorative gear wheel motif on the bracket joint. Neutral grey background, even studio lighting, four views. At fairy scale (4 inches tall), this lamp post is a lighthouse/beacon tower 24 times character height.
```

### 3.2 Penfold Hexagonal Postbox

```
3D model of a Victorian Penfold hexagonal pillar box (postbox), circa 1866-1879 design still in use in 1885. Bright vermillion red (Penfold red). Hexagonal cross-section, approximately 5 feet tall. Ornate crown finial on top. Horizontal posting slot with raised surround. Collection times plate below slot. Royal cypher "VR" (Victoria Regina) cast into the body. Cast-iron construction. Standing on a York stone pavement slab. Neutral grey background, even studio lighting, four views.
```

### 3.3 Cannon Bollard

```
3D model of a Victorian London cannon bollard. Actual recycled ship's cannon barrel, approximately 3 feet tall, embedded muzzle-down in the pavement. Cast iron, painted black. Rounded cannon ball finial on top (the trunnion end). Some still show the bore opening at the top. Slight lean from years of horse-cart impacts. Used to protect building corners from cart damage. Neutral grey background, even studio lighting, four views.
```

### 3.4 Horse Trough

```
3D model of a Victorian street horse trough, circa 1880s. Granite or cast-iron rectangular trough, approximately 4 feet long, 18 inches deep. Simple pedestal base. Small drinking cup on a chain for human use. Water spout (often with a lion head or simple tap). Inscription on the side: "METROPOLITAN DRINKING FOUNTAIN AND CATTLE TROUGH ASSOCIATION." Algae staining on the interior. At fairy scale, this is a lake — a major water feature in the landscape. Neutral grey background, even studio lighting, four views.
```

### 3.5 Iron Railing Section

```
3D model of a Victorian cast-iron railing section, Clerkenwell residential style. Approximately 4 feet tall, 6 feet long section. Spearhead finials on each vertical bar. Bars spaced 4-5 inches apart. Horizontal top rail and bottom rail. Mounted on a low dwarf wall of London stock brick. Painted black. Two hundred years of paint layers give a slightly lumpy texture. Slightly more intricate geometric pattern than plain spears — a subtle reference to the clockwork trades of the neighborhood. Neutral grey background, even studio lighting, four views.
```

### 3.6 Sewer Gully Grating

```
3D model of a Victorian cast-iron sewer gully grating, set into granite kerb at road edge. Approximately 12x6 inches. Parallel slot pattern with 1/2-3/4 inch gaps between bars. Raised slightly from the road surface. "VESTRY OF CLERKENWELL" cast into the frame (or "BERMONDSEY" for the southern variant). Dark iron, slightly rusted at edges. Water staining around it. At fairy scale, this is a cavern entrance — the slots are just wide enough for a four-inch character to squeeze through into the underground sewer network. Neutral grey background, even studio lighting, four views.
```

### 3.7 Parish Water Pump

```
3D model of a Victorian parish hand water pump, circa 1885. Cast iron, approximately 3.5 feet tall. Fluted column with a curved pump handle on one side. A spout projecting over a small stone trough basin set into the ground. The base is bolted to a York stone pavement slab. Painted black, with paint chipping to reveal rust. "VESTRY OF ST JAMES CLERKENWELL" cast into the column. A small puddle around the base from dripping. The trough has green algae staining. At fairy scale, this pump is a tower with a moving beam (the handle) and the trough is a swimming pool. Neutral grey background, even studio lighting, four views.
```

### 3.8 Mounting Block

```
3D model of a Victorian horse-mounting block, circa 1885. Three steps carved from a single block of York stone, approximately 2 feet tall, 3 feet long, 18 inches deep. Smooth worn surface on top from use. Positioned at a kerbside. The steps are uneven from decades of boots. Some moss in the shadowed joints. Iron boot-scraper set into the top step. A simple, functional piece of street furniture found outside coaching inns, pubs, and larger houses. At fairy scale, a three-tier cliff formation. Neutral grey background, even studio lighting, four views.
```

### 3.9 Street Name Plate

```
3D model of a Victorian London street name plate, set into a brick wall at approximately 8 feet height, circa 1885. Glazed ceramic tile or enameled iron plate, approximately 18x6 inches. Dark blue or black background with white serif lettering: "SEKFORDE STREET" and below in smaller text: "PARISH OF CLERKENWELL." A thin decorative border. Mounted flush with the brick face using iron bolts at each corner. Some soot accumulation on the top edge. The wall around it is typical London stock brick. At fairy scale, this is a wall-mounted billboard, readable from a considerable distance. Neutral grey background, even studio lighting, four views.
```

### 3.10 Shop Projecting Sign

```
3D model of a Victorian shop projecting sign, circa 1885. A painted timber board approximately 24x18 inches, double-sided, hanging from a wrought-iron bracket that projects 18 inches from the wall. The bracket is ornate — scrollwork iron, bolted to the brickwork with large rosette washers. The sign reads: "CRIBBAGE — TINKER & CLOCK REPAIRS" in hand-painted serif lettering, cream on dark green. A small painted clock face as a pictorial device. The timber is slightly warped from weather. Paint faded on the south-facing side. The iron bracket creaks in the wind. At fairy scale, this sign is a hanging platform accessible from the wall. Neutral grey background, even studio lighting, four views.
```

### 3.11 Stink Pipe — Sewer Ventilation Column

```
3D model of a Victorian sewer ventilation column (stink pipe), circa 1885. Cast-iron tube, 6 inches in diameter, 6-8 metres tall, painted dark green. Fluted decorative base bolted to the pavement with four bolts. A manufacturer's plaque near the base: "HAYWARD BROTHERS — UNION STREET BOROUGH." Ornamental crown cap at the top with ventilation slots to release sewer gas above street level. The pipe is a simple cylinder for most of its height, with a slight taper. Positioned at a street corner or junction. The surrounding pavement has a faint greenish discoloration from years of vented gas. At fairy scale, this is a toxic tower — a vertical connector from the sewer network to the surface, climbable inside but filled with lethal methane and hydrogen sulfide. Neutral grey background, even studio lighting, four views.
```

### 3.12 Crossing Sweeper's Broom

```
3D model of a Victorian street-sweeper's broom, propped against a wall, circa 1885. A besom broom — birch twigs bound to a long ash handle, approximately 4 feet total length. The twigs are worn and splayed from use. The handle is smooth from grip, darkened with grime. Propped at an angle against London stock brick wall, beside a street gutter. A small pile of horse dung and straw swept to one side. The broom belongs to a crossing sweeper — a child who clears paths across busy intersections for tips. At fairy scale, this broom is a tree-sized hazard. A crossing sweeper's stroke covers 3 feet — a lethal arc of birch twigs moving at speed. Neutral grey background, even studio lighting, four views.
```

### 3.13 Barrel and Crate Stack

```
3D model of a stack of Victorian barrels and wooden crates outside a pub or warehouse, circa 1885. Two wooden beer barrels (hogsheads) on their sides in a timber cradle, approximately 3 feet long each, iron-hooped. Three stacked wooden crates beside them — rough pine with stenciled markings: "TRUMAN HANBURY — PALE ALE" and "FRAGILE — GLASS." A coil of rope on top. The assemblage is against a London stock brick wall under a window. Puddle of spilled beer around the barrel bungs. At fairy scale, this stack is a multi-level terrain feature — the barrel curves are hills, the crate gaps are rooms, the rope is a climbing resource. Neutral grey background, even studio lighting, four views.
```

### 3.14 Sandwich Board / Advertising Hoarding

```
3D model of a Victorian A-frame sandwich board on a pavement, circa 1885. Two timber boards approximately 3x2 feet each, hinged at the top, standing in an inverted V. Hand-painted advertisement: "DR COLLIS BROWNE'S CHLORODYNE — THE GREAT SPECIFIC FOR CHOLERA, DYSENTERY, COUGHS" in bold Victorian typography — multiple fonts, decorative borders, pointing hand motifs. The timber is weather-beaten, the paint cracked. Positioned on a York stone pavement outside a chemist's shop. A simple, common piece of Victorian street clutter. At fairy scale, this is a tent-like structure — a shelter or obstacle depending on approach. Neutral grey background, even studio lighting, four views.
```

---

## 4. Street Surface Prompts

### 4.1 Granite Sett Road Section

```
3D model of a section of Victorian London road surface, approximately 3x3 feet. Rectangular granite setts (NOT smooth cobblestones), each roughly 11x13 inches on the surface, 9 inches deep. Grey or pink-grey stone. Gaps between setts 1/4 to 1 inch wide, filled with tar and earth. Worn smooth on top from iron-rimmed cart wheels. Some setts slightly tilted or sunken. One cart rut visible — a worn groove in the stone. At fairy scale, each sett is a boulder-sized plateau and the gaps are ravines/trenches. Neutral grey background, even studio lighting, top-down and angled views.
```

### 4.2 Pavement and Kerb Section

```
3D model of a Victorian London pavement section with kerb, approximately 3x3 feet. York stone flagstones (pale grey-buff, large rectangular slabs, ~2x3 feet each) for the pavement. Granite kerbstone (darker grey, ~12 inches tall, 6 inches wide) separating pavement from road. The kerb edge is sharp and squared — at fairy scale this is a cliff face 3x character height. Some flagstones slightly uneven from ground subsidence. Moss in shaded joints. Neutral grey background, even studio lighting, four views.
```

### 4.3 Street Drain Channel

```
3D model of a Victorian London street drain channel section, approximately 3 feet long. A V-shaped channel cut into the granite setts along the kerbstone, approximately 6-12 inches wide and 3-4 inches deep. Lined with smooth granite. Water flows along the channel toward a gully grating. Debris accumulated: straw, a scrap of newspaper, horse dung, a broken clay pipe stem. The channel sits at the lowest point of the cambered road. In dry weather: damp residue and caked organic matter. In wet weather: a flowing stream. At fairy scale, this is a river running through a canyon — the primary street-level water feature and a flash-flood hazard in rain. Neutral grey background, even studio lighting, four views.
```

### 4.4 Muddy Unpaved Alley Section

```
3D model of a section of unpaved Victorian back alley, Bermondsey, circa 1885. Approximately 3x3 feet of compacted earth surface, rutted and muddy. No granite setts — just bare ground. Deep cart ruts filled with standing water. Horse dung mixed into the mud — a warm brown slurry. Broken brick fragments and clinker ash dumped as makeshift paving in the worst patches. A board laid across one puddle as a stepping aid. Walls of London stock brick rise on either side — the alley is approximately 4 feet wide, barely cart-width. A drain running down the center is clogged. At fairy scale, this terrain is a swamp — soft ground, standing pools, unstable footing. Neutral grey background, even studio lighting, four views.
```

### 4.5 Bridge Road Surface Section

```
3D model of a Victorian London bridge road surface section, approximately 3x3 feet. Granite setts laid on a slightly wider and flatter profile than normal streets — no camber. Stone or iron parapet wall on one side, approximately 3 feet tall, with cast-iron balustrade railings on top. The parapet is Portland stone, soot-stained. The roadway is exposed to wind — no sheltering buildings on either side. A gas lamp post rises from the parapet at regular intervals. The surface is swept cleaner than normal streets — bridge tolls fund maintenance. At fairy scale, the bridge is an exposed causeway — the parapet wall is a cliff with iron railing spears above, and wind is a constant hazard. Neutral grey background, even studio lighting, four views.
```

### 4.6 Cobbled Courtyard Section

```
3D model of a Victorian enclosed courtyard behind a row of terraces, Bermondsey, circa 1885. Approximately 6x6 feet of cobbled yard enclosed by brick walls on three sides and the rear of terraced houses on the fourth. A shared privy (outhouse) in one corner — small timber structure with a half-door. A communal water pump or standpipe against one wall. Washing lines strung between walls, a few items of clothing hanging. A brick-built dust bin (refuse container). Drainage channel running to a gully in the center. The cobbles are uneven, some missing. Weeds in the gaps. Walls stained with damp. Clothes pegs, a broken bucket, scattered domestic debris. At fairy scale, an enclosed fortress courtyard. Neutral grey background, even studio lighting, four views.
```

---

## 5. Per-Neighborhood Assembly Notes

> **Topology matters.** See Section 15 for full elevation data. Clerkenwell is on a hill (~25m). Bermondsey is flat marshland (~3m). Wapping is at river level. Streets slope. This affects drainage, navigation, and fairy-scale terrain difficulty. See Section 17 for the two-tier LOD assembly strategy and heightmap pipeline.

### Clerkenwell — Squad Territory

**Character:** Modest, skilled working-class. Precision trades. Medieval street grid with Georgian buildings.

**Terrain:** Hilltop, ~20-25m elevation. Streets slope downhill in all directions from Clerkenwell Green. Terrain tiles: Main Road (20.1) for Clerkenwell Road; Side Street (20.2) for residential streets; Churchyard (20.5) around St James.

**Components to combine:**
- Georgian Terrace Section (dominant building type)
- Clockmaker's Workshop Frontage (every few doors)
- Jeweller's Shopfront (Hatton Garden edge — more prosperous zone)
- Printing Press Workshop (Arthur Hartley's trade — scattered through district)
- Corner Chandler's Shop (one per few streets — local provisions)
- Small Workshop Block (purpose-built, let by floor — Aylesbury St area)
- Lodging House (poorer streets near Clerkenwell Road)
- Church Facade (St James as navigation landmark)
- Board School (tall, dominant civic building)
- Gas Lamp Posts (every 30-50 yards on main streets)
- Iron Railings (in front of most houses)
- Penfold Postbox (one per few streets)
- Water Pump (parish pumps at street junctions)
- Street Name Plates (on corner buildings)
- Shop Projecting Signs (every workshop and shop)
- Chimney Clusters (on every building)
- Barrel/Crate Stacks (outside pubs and chandlers)

**Street layout:** Narrow (8-12 feet). Buildings directly on pavement edge. No front gardens. Slight curves and irregular junctions reflecting medieval origins. Clerkenwell Road is the main artery — wider, straighter, busier. Side streets like Sekforde Street are narrow and quiet.

**Atmosphere:** Moderately clean for London. The clockmakers keep their frontages tidy. Brass in shop windows. Sound of ticking from open workshop doors. Less industrial smoke than Bermondsey but still sooty.

**Story locations here:** Cribbage's Workshop (2B.3), Theodore's Garret Room (2B.10), Clockmaker's Shop heist (2B.4), Decommissioned Church (2B.6, 2B.7).

**Density reference:** See Goad Vol. VI Key Plan and sheets 129-134.

### Bermondsey — Industrial Titan Zone

**Character:** Heavy industrial. Oppressive. Dense working-class housing crammed between factories.

**Terrain:** Former marshland, ~3-5m elevation. Dead flat. Poor drainage — water sits in puddles. Terrain tiles: Side Street (20.2) for Long Lane; Back Alley (20.3) behind terraces; Courtyard (20.4) behind housing; Railway Embankment (20.10) where viaduct crosses; Wharf Apron (20.6) along river.

**Components to combine:**
- Industrial Warehouse (dominant along Long Lane and river-side)
- Tannery Building (eleven tanneries on Long Lane alone)
- Back-to-Back Workers' Housing (courts behind main streets)
- Biscuit Factory (Peek Frean — large industrial landmark)
- Riverside Wharf Building (St Saviour's Dock area)
- Railway Arch Workshop (under viaduct — blacksmiths, farriers)
- Bone-Boiling Works (rendering plants — worst smell)
- Gin Distillery (scattered through industrial zone)
- Public House (one on nearly every corner — workers' social life)
- Georgian Terrace Section (but meaner — smaller windows, more degraded)
- Railway Viaduct Section (dominant infrastructure feature)
- Gas Lamp Posts (scarcer on back streets)
- Horse Troughs (near factory entrances for dray horses)
- Sewer Gully Gratings (important for fairy-scale infiltration routes)
- Stink Pipes (sewer ventilation — more common in industrial areas)
- Muddy Unpaved Alley sections (back streets)
- Cobbled Courtyard sections (behind terraces)
- Sandwich Boards (outside chemists, pubs)

**Street layout:** Long Lane is the spine — narrow but long and straight. Side streets are even narrower — some barely 6 feet wide. Back-to-back housing in courts behind the main streets (see Goad SE District sheets J.9-10 for exact layout). Warehouses and tanneries create canyon-like streets. Railway viaduct cuts through, creating dark covered zones.

**Atmosphere:** The worst-smelling neighborhood in London. Tanning uses dog dung, urine, and bark — the smell carries for blocks. Heavy industrial smoke. Puddles of industrial runoff. Darker, denser, more oppressive than Clerkenwell. Gas lamps are rarer on side streets.

**Story locations here:** Titan bio-trace basement (Issue 6), factory district investigation.

**Density reference:** See Goad SE District Key Plan and sheets J.9, J.10. See Booth Sheet 9 (Inner Southern) for poverty coding — heavy dark blue/black streets.

### Wapping — Docklands Titan Zone

**Character:** Maritime industrial. Massive scale. Warehouses dwarf everything.

**Terrain:** River level, ~3-5m elevation. Flat except for excavated dock basins (sunken below ground). Terrain tiles: Wharf Apron (20.6) along docks; Dock Basin Edge (20.7) at water; Foreshore (20.8) at Thames; Side Street (20.2) for narrow warehouse lanes.

**Components to combine:**
- Dock Warehouse (dominant — cliff-like walls lining narrow lanes)
- Waterside Sailors' Pub (maritime character, river frontage)
- Customs House / Dock Office (official, Portland stone)
- Dock Gate Entrance (perimeter security, fortress-like)
- Hydraulic Pumping Station (ornate industrial, tall chimney landmark)
- Lighterman's Stairs (river access, Thames mud)
- Gas Lamp Posts (on main roads only)
- Cannon Bollards (protecting warehouse corners from carts)
- Horse Troughs (for dray horses hauling from the docks)
- Barrel/Crate Stacks (cargo everywhere)
- Bridge Road Surface (for Thames crossing approaches)

**Street layout:** Narrow lanes between massive warehouse walls. The warehouses are 5-6 stories — the streets feel like canyons. Wider loading areas in front of dock gates. The river is always nearby — mast-heads visible above the rooflines. Cranes and hoisting gear break the skyline.

**Atmosphere:** Salt, tar, tobacco, spices — the smells of the world passing through. Creaking ropes and timber. Dock workers, sailors, lightermen. Less residential than Bermondsey — more industrial/commercial. At night: very dark between the warehouses, gas lamps only on main roads.

**Story locations here:** Dock warehouse infiltration, lighthouse heist approach.

**Density reference:** See Booth Sheet 1 (Eastern) for dock layout. See Goad plans if sheets covering Wapping docks are found.

### Trinity Buoy Wharf / Bow Creek — Lighthouse Territory

**Character:** Isolated. Mud flats. Where the Thames meets Bow Creek. Industrial edges but the lighthouse itself stands alone.

**Terrain:** River level, ~2-3m elevation. Exposed mud flats at low tide. Terrain tiles: Foreshore (20.8) for mud flats; Wharf Apron (20.6) for the wharf surface. The most topographically dramatic location at fairy scale — vast open mud with the lighthouse as the only vertical feature.

**Components to combine:**
- Trinity Buoy Wharf Lighthouse (2B.5 — the story-specific set piece)
- Dock Warehouse (smaller scale — Bow Creek is minor compared to London Docks)
- Lighterman's Stairs (river access on both Creek and Thames)
- Muddy Unpaved Alley sections (approach roads are poorly maintained)
- Gas Lamp Posts (sparse — this is the edge of the city)

**Street layout:** Not really streets — more wharfside tracks, mud paths, open ground between scattered industrial buildings. The lighthouse sits on a triangular spit of land at the creek-Thames confluence. Low-tide mud flats extend from the shore. The area feels peripheral, half-wild.

**Atmosphere:** Wind off the river. Mud. The lighthouse beam at night. Fewer people than anywhere else the squad visits. The isolation makes it both safer (fewer human threats) and more exposed (no cover, no concealment from aerial threats). Bird danger highest here — open sky, water birds, potential kestrel territory.

**Story location:** Issue 7 — the lens heist. The squad's first major expedition outside familiar Clerkenwell.

### Thames Crossing — Bridge and River

**Character:** Exposure. Wind. The great dividing line between north and south London.

**Terrain:** Bridges are the only elevated crossing — ~8-10m above low-tide water. Terrain tiles: Bridge Roadway (20.9) for the crossing itself; Foreshore (20.8) for the river banks below. The Thames is tidal (~7m range at London Bridge) — the water level and foreshore exposure change dramatically through the day.

**Components to combine:**
- Bridge Road Surface (exposed causeway with parapet walls)
- Tower Bridge Under Construction (landmark, 1886)
- Gas Lamp Posts (on bridge parapets — more exposed than street lamps)
- Cannon Bollards (bridge approach corners)
- Lighterman's Stairs (embankment access)

**Crossing options for the squad:**
- **London Bridge** — ancient route, heavy traffic, relatively narrow. Rebuilt 1831 in granite — clean lines, stone parapet.
- **Southwark Bridge** — less traffic, iron construction. Opened 1819.
- **Tower Bridge** — under construction 1886. Temporary wooden footbridge may be accessible. Scaffolding = climbing routes.
- **Tower Subway** — pedestrian tunnel under the Thames. Opened 1870 as cable-hauled railway, converted to foot tunnel. Narrow, lit by gas, tolled (1d). At fairy scale: a tunnel they could walk through undetected among human feet.

**Atmosphere:** Wind. Exposure. The river below is vast — at fairy scale, an ocean. The bridge surfaces are the most exposed terrain in the game. No cover from aerial threats. Human foot traffic is concentrated and unavoidable.

---

## 6. Scale Reference — Human vs Fairy

Every component above exists at two scales:

### Exterior Terrain

| At Human Scale | At Fairy Scale (4 inches tall) | Gameplay Function |
|---|---|---|
| Gas lamp post (8 ft) | Lighthouse tower (24x character height) | Landmark; light hazard zone |
| Kerbstone (8 in high) | Cliff face (2x character height) | Elevation barrier street/pavement |
| Granite sett (11x13 in) | Boulder plateau (3x character width) | Cover-rich slow terrain |
| Gap between setts (1/4-1 in) | Ravine / trench | Concealed ground route |
| Street gutter (6-12 in wide) | River channel | Flash flood zone; dry weather pathway |
| Cart rut in road | Canyon | Fast but flood-prone channel |
| Sewer grating slot (3/4 in) | Narrow cave entrance (just fits) | Access to underground network |
| Stink pipe (6 in diameter) | Toxic chimney tower | Vertical sewer-to-surface connector |
| Rain gutter (4.5 in half-round) | River/highway (major transit route) | Primary rooftop transit route |
| Drainpipe (66mm internal) | Vertical highway | Climbable; socket joints = platforms |
| Drainpipe bracket | Ledge / rest platform | Rest stops on vertical routes |
| Telegraph wire (~4mm) | Aerial cable / tightrope | Glide path, perch, rest stop |
| Ceramic insulator (~3-4 in) | Platform / seat | Rest point on aerial routes |
| Mouse hole (1-2 in diameter) | Doorway/tunnel entrance | Access between rooms / into walls |
| Chimney pot (12-18 in tall) | Watchtower (observation post, warm updraft) | High-ground overwatch |
| Horse trough (3 ft long) | Lake (water source, drowning hazard) | Water feature |
| Narrow alley (15 in to 6 ft) | Canyon / gorge | Sheltered ground route |
| Horseshoe print in mud (5+ in) | Crater | Terrain feature; evidence |
| Slate roof tile | Overlapping shelf terrain (~1/4 in lip) | Shelter under; ledge on top |
| Lead roof flashing | Stepped staircase / walkway | Transitions between roof levels |
| Chimney stack (2-4 ft across) | Tower / fortification | Wind shelter, observation post |

### Interior Terrain

| At Human Scale | At Fairy Scale (4 inches tall) | Gameplay Function |
|---|---|---|
| Workbench surface (2x4 ft) | Landscape plateau | Primary mission terrain |
| Open drawer | Cave / room | Storage, shelter, loot container |
| Scattered screws/nails (1-3 in) | Boulders / obstacles | Cover |
| Keyhole (1/2 in diameter) | Portal/doorway between rooms | Access |
| Clock mechanism | Industrial complex (gears = doors) | Hazardous moving terrain |
| Candle flame (~1 in) | Bonfire / furnace | Heat + light hazard |
| Bookshelf (4-6 ft) | Multi-story building | Vertical terrain, shelter between books |
| Mantelpiece (5-6 ft long) | Broad avenue / promenade | Display terrain above fireplace |
| Floorboard gap (~1/4 in) | Ravine / access hatch | Entry to under-floor void |
| Wall void (3-4 in stud bays) | Tunnel system | Infiltration route inside buildings |
| Window ledge (4-6 in deep) | Mountain ledge / overwatch position | Rest point, observation |
| Staircase | Cliff face | Vertical terrain; bannister as rail |
| Coal scuttle (~12 in) | Boulder / cave | Cover near fireplaces |

### Navigation Network Scale

| Route Type | Cross-Section at Fairy Scale | Speed | Key Hazard |
|---|---|---|---|
| Rooftop gutter (4.5 in) | Wide highway | Fast | Birds, wind, rain flooding |
| Drainpipe (66mm bore) | Tight vertical tunnel | Slow | Falls, wet surfaces |
| Brick wall mortar joints | Climbing face (holds every 75mm) | Very slow | Falls, exposure |
| Street sewer (12 in brick) | Large tunnel (3x height) | Fast | Rats, flooding, toxic gas |
| House drain (6-9 in) | Medium tunnel (1.5-2x height) | Moderate | Tight, flow |
| Wall void (3-4 in) | Crawlway | Very slow | Spiders, gas leaks, rats |
| Telegraph wire (4mm) | Tightrope / glide cable | Fast (flight) | Exposure, birds |
| Theodore Express | Concealed transport | Fastest | Theodore's availability |

When generating environment components, consider both scales. A gas lamp that looks like street furniture at human scale should have enough detail to function as a landmark tower at fairy scale.

---

## 7. Lighting for 3D Scenes

Every assembled scene should use the GrimGlow dual-lighting system:

**Base layer:** Warm amber gaslight. Point lights at each gas lamp position. Soft amber glow with sharp downward pool and gradual falloff. Fog scatters the light into halos.

**Intrusion layer:** Cool structured holographic light from fairy characters/tech. Blue-white (Sable), copper-gold (Wren), emerald (Jink), crimson (Thresh), blue-violet (Luma). This light has hard geometric edges — it cuts into the warm amber scene.

**Neither dominates.** The contrast between warm amber and cool holographic is the visual signature of GrimGlow.

---

## 8. Interior Environment Components

Fairy-scale interior terrain pieces for assembling workshop, shop, and domestic interiors. These are viewed from the 4-inch character perspective — every object is landscape-scale.

### 8.1 Workshop Workbench Surface

```
3D model of a Victorian clockmaker's workbench surface viewed at fairy scale (4-inch character perspective), circa 1885. A vast wooden plateau scored with knife marks and stained with oil, solder, and ink. Scattered across the surface: brass screws as tall as a person, a steel file laid flat like a ridged bridge, wood shavings curled like fallen logs, a magnifying loupe on its side — the lens a crystal dome. A tin of watch oil with the lid off — a circular pool of golden liquid. A brass candle holder at the far edge with a lit candle — a towering column of flame. Small piles of metal filings like sand dunes. A ruler laid flat with inch markings — a measured road. The bench edge is a cliff dropping to the floor below. Warm candlelight, wood and metal textures. Neutral grey background, even studio lighting, four views.
```

### 8.2 Open Drawer Interior

```
3D model of an open wooden drawer viewed at fairy scale (4-inch character perspective), circa 1885. A rectangular wooden box approximately 18x12x4 inches — at fairy scale, a room-sized cave. Pine construction with dovetail joints visible at the corners. Inside: a jumble of small tools and parts — watch keys, loose screws, a broken pocket watch, a coil of thin wire, a folded scrap of paper with handwriting. The drawer walls are 4 inches tall — exactly character height. The front face of the drawer projects forward, creating an overhang/roof over the opening. Dust in the corners. The smell of wood and metal. From inside, the workshop is visible through the opening — a vast bright world beyond the drawer's dim interior. Neutral grey background, even studio lighting, four views.
```

### 8.3 Bookshelf Section

```
3D model of a section of Victorian bookshelf viewed at fairy scale (4-inch character perspective), three shelves, approximately 4 feet tall total, circa 1885. Dark-stained oak construction. Each shelf holds a row of leather-bound books — at fairy scale, each book is a building-sized block. Gaps between books create room-sized passages. The spine lettering is wall-sized text. Book tops are accessible platforms connected by leaning or bridging between volumes. Dust on the top shelf. A gap where a book has been removed creates a cave. The shelves themselves are ledges at different heights — a multi-story vertical environment. A bookworm hole in one spine creates a tunnel entrance. Neutral grey background, even studio lighting, four views.
```

### 8.4 Mantelpiece Terrain

```
3D model of a Victorian mantelpiece shelf viewed at fairy scale (4-inch character perspective), circa 1885. A broad wooden or marble shelf approximately 5 feet long and 8 inches deep — at fairy scale, a wide promenade. Objects arranged on it: a mantel clock (wall-sized at fairy scale, ticking audibly), two brass candlesticks (towers), a small framed photograph (billboard), a china ornament (building-sized statue), a letter propped against the clock. Below: the fireplace opening — a massive arched cavity radiating heat, with a cast-iron grate and glowing coals. Warm updraft from the fire creates a vertical wind. The mantelpiece edge is a cliff face above the hearthstone floor. Dust in the carved decorative moulding creates sheltered alcoves. Neutral grey background, even studio lighting, four views.
```

### 8.5 Fireplace and Coal Grate

```
3D model of a Victorian cast-iron fireplace interior viewed at fairy scale (4-inch character perspective), circa 1885. A cast-iron fire grate with decorative side panels, approximately 18 inches wide. Glowing coals on the grate — at fairy scale, a field of incandescent boulders radiating intense heat. The fire surround is cast iron with a tiled insert — decorative Minton tiles in blue and white. A brass fender rail at the base. A coal scuttle (black japanned iron, 12 inches tall — a building at fairy scale) stands beside the grate with a brass-handled shovel. Ash and cinder on the hearth stone. The chimney opening above is a vast dark shaft with rushing updraft. The heat gradient: scorching near the grate, warm at the fender, comfortable at mantelpiece height. Neutral grey background, even studio lighting, four views.
```

### 8.6 Under-Floorboard Void

```
3D model of the space beneath Victorian floorboards viewed at fairy scale (4-inch character perspective), circa 1885. Joists (3x2 inch timber beams) run parallel like bridge supports, spaced 12-16 inches apart — at fairy scale, a repeating tunnel system. Floorboards above form a low ceiling with light leaking through gaps between boards. Gas pipes (1/2 inch bore) run along the joists — too narrow to enter but useful as guide rails. Dust, cobwebs, and decades of dropped debris: a lost coin (plate-sized), a dessicated mouse skeleton, plaster fragments from the ceiling below. The space is 6-8 inches high — comfortable standing room at fairy scale. Sound from the room above is muffled but audible — footsteps are thunder. Spider webs stretched between joists create trap terrain. Neutral grey background, even studio lighting, four views.
```

### 8.7 Wall Void Interior

```
3D model of the interior of a Victorian wall void (between plaster and brick) viewed at fairy scale (4-inch character perspective), circa 1885. The void is 3-4 inches wide — a stud bay between timber studs. On one side: the lath-and-plaster inner wall — thin wooden laths nailed horizontally create a ladder-like climbing surface, with plaster bulging through the gaps. On the other side: the inner face of the brick wall — rough, unfinished brickwork with lime mortar. Gas supply pipe (1/2 inch iron) running vertically through the void, secured with iron brackets. Cobwebs. Dust. A vertical route — the void extends upward through the building, connecting floors via gaps where joists meet walls. Mouse droppings. The space is cramped but navigable for a 4-inch character. Total darkness without fairy-tech light. Neutral grey background, even studio lighting, four views.
```

### 8.8 Window Sill Platform

```
3D model of a deep Victorian stone window sill viewed at fairy scale (4-inch character perspective), circa 1885. Portland stone or York stone sill, approximately 4-6 inches deep and 2 feet wide — at fairy scale, a broad platform. The sash window behind: six-over-six pane glass, the lower sash slightly open (the gap is a doorway at fairy scale). A lace curtain hangs inside — at fairy scale, an elaborate mesh screen providing concealment. The sill surface: cold stone, slightly concave from weathering, with a small puddle of rainwater in the depression. Soot accumulated along the back edge against the glass. Outside: the view over a Victorian streetscape from first-floor height. The sill edge is a cliff dropping to the street below. Pigeon droppings in one corner. Neutral grey background, even studio lighting, four views.
```

### 8.9 Staircase Interior

```
3D model of a Victorian domestic staircase viewed at fairy scale (4-inch character perspective), circa 1885. Steep narrow stairs with a turned wooden bannister rail and thin iron balusters. Each step riser is approximately 7 inches — nearly 2x character height, a cliff per step. A threadbare carpet runner tacked to the center of the treads. Dust accumulated in the angle where tread meets riser. The newel post at the bottom is a monumental column with a turned finial. The stairwell rises into darkness above. A gas jet (wall-mounted bracket) on the landing provides a warm orange glow. The walls are papered in dark Victorian floral pattern, peeling at the seams. At fairy scale, ascending this staircase is mountaineering — each step a ledge requiring climbing. The carpet runner provides grip. The bannister rail is a highway with rest stops at each baluster. Neutral grey background, even studio lighting, four views.
```

### 8.10 Attic Space

```
3D model of a Victorian attic/loft space viewed at fairy scale (4-inch character perspective), circa 1885. Exposed timber roof trusses and rafters forming an A-frame cathedral-like space. The underside of Welsh slate tiles visible between the rafters — gaps where daylight leaks through. Cobwebs everywhere — large orb webs between trusses, funnel webs in corners. A water tank (lead-lined timber box, 3x2 feet) — at fairy scale, a reservoir. Stored items: a trunk (building-sized), stacked boxes, old picture frames leaning against a wall, rolled carpet. Mouse droppings and scattered mouse nests of shredded paper. A mouse hole in the plaster near the eaves — a tunnel entrance. The space is cold, dusty, and largely undisturbed by humans. A dormer window provides some light. Neutral grey background, even studio lighting, four views.
```

---

## 9. Navigation Infrastructure Components

Modular 3D pieces representing the six navigation networks the squad uses to traverse Victorian London at fairy scale.

### 9.1 Cast-Iron Drainpipe with Socket Joints — Vertical Highway

```
3D model of a Victorian cast-iron drainpipe section, mounted on a London stock brick wall, viewed at fairy scale (4-inch character perspective), circa 1885. The pipe is 3-inch diameter (75mm) external — at fairy scale, a wide cylindrical column. Socket joints (where pipe sections connect) create ring-shaped platforms every few feet — each socket is a widened collar approximately 4 inches in diameter, a ledge for resting during the climb. Iron wall-mounting brackets at 6-foot intervals — each bracket is a projecting shelf bolted to the brickwork. The pipe is painted black, with paint chipping to reveal rust beneath. Water stains running down from the roof gutter connection above. The brick wall provides a textured backdrop — mortar joints visible as potential handholds. At fairy scale, this is a vertical highway with rest stops. Neutral grey background, even studio lighting, four views.
```

### 9.2 Brick Sewer Tunnel Section — Underground Highway

```
3D model of a section of Bazalgette's London sewer, egg-shaped cross-section, viewed at fairy scale (4-inch character perspective), circa 1875-1885. The tunnel is 12 inches in diameter — at fairy scale, a large tunnel approximately 3x character height. Brick-lined throughout in engineering brick (blue-grey, harder than stock brick), with precise curved courses. The egg shape means: narrow channel at the bottom where water flows (even in dry weather, a few inches of effluent), and wider dry ledges along the sides. The ledges are where the squad walks — above the flow line but below the crown. The brick is damp, slick with biofilm. Faint light filtering down from a gully grating above (visible as a barred window in the tunnel ceiling). The tunnel curves slightly ahead, disappearing into darkness. Sound: dripping, distant flow, occasional rat squeaks. Neutral grey background, even studio lighting, four views.
```

### 9.3 House Drain Pipe Section

```
3D model of a Victorian house drain pipe section, circular, viewed at fairy scale (4-inch character perspective), circa 1885. Salt-glazed stoneware pipe, 6-9 inches in internal diameter — at fairy scale, a tunnel 1.5-2x character height. The pipe connects a building to the street sewer. Brown-glazed interior surface, smooth but with lime scale deposits. A slight downward slope toward the main sewer. The pipe is buried underground but shown in cross-section: surrounding earth visible, the pipe running through it. At the building end: a bend where the pipe enters the house wall. At the sewer end: a junction where this pipe meets the larger street sewer. Residual damp on the interior. No standing water in dry weather but flow increases rapidly in rain. Neutral grey background, even studio lighting, four views.
```

### 9.4 Stink Pipe Interior — Vertical Connector

```
3D model looking upward inside a Victorian sewer ventilation column (stink pipe), viewed at fairy scale (4-inch character perspective). A cast-iron tube, 6 inches in diameter — at fairy scale, a spacious vertical shaft approximately 1.5x character height in diameter. The interior wall is smooth cast iron, painted green on the exterior but bare metal inside — slightly corroded, with condensation droplets. Looking up: the ventilation slots at the crown cap are visible as a grated ceiling, daylight streaming through. Looking down: the connection to the sewer below. Iron rivets and joints create climbing holds at regular intervals. The air inside is toxic — methane, hydrogen sulfide, ammonia. Without suit filtration, this is lethal. Represented visually: a greenish-yellow haze inside the column. Neutral grey background, even studio lighting, four views.
```

### 9.5 Telegraph Wire with Ceramic Insulator — Aerial Perch

```
3D model of a Victorian telegraph wire and ceramic insulator mounted on a building parapet, viewed at fairy scale (4-inch character perspective), circa 1885. The insulator is a brown glazed ceramic dome approximately 3-4 inches tall — at fairy scale, a mushroom-shaped platform, large enough to sit on. It sits on an iron bracket bolted to the parapet stonework. A copper telegraph wire (~4mm diameter — at fairy scale, a thick cable) connects to the insulator's groove and stretches away to the next building. The wire sags slightly between attachment points. At fairy scale, this is an aerial transit node — the insulator is a rest platform, the wire is a tightrope or glide cable for wing-pack users. Multiple wires may run parallel, creating an aerial network. Neutral grey background, even studio lighting, four views.
```

### 9.6 Lead Roof Flashing Staircase

```
3D model of Victorian lead roof flashing where a wall meets a roof slope, viewed at fairy scale (4-inch character perspective), circa 1885. Lead step-flashing follows the line where a chimney stack or party wall meets the slate roof — each step is approximately 4 inches wide (one slate course), creating a zig-zag staircase pattern up the roof slope. The lead is soft grey, slightly buckled from thermal expansion, with moss growing in the crevices. Each step is a ledge at fairy scale — wide enough to walk on, with the next step a comfortable climb above. The flashing runs from gutter level to ridge height. This is the primary route for transitioning between roof levels where buildings of different heights adjoin. Neutral grey background, even studio lighting, four views.
```

### 9.7 Rain Gutter Highway

```
3D model of a Victorian cast-iron roof gutter, half-round profile, viewed at fairy scale (4-inch character perspective), circa 1885. The gutter is 4.5 inches wide (half-round) — at fairy scale, a wide trough-shaped highway running along the roof edge. Cast iron, painted black, supported by iron brackets bolted to the rafter ends at 2-foot intervals. Inside the gutter: dry leaves, small twigs, gritty soot sediment — terrain features at fairy scale. The gutter connects to a drainpipe (vertical highway) at one end via a hopper head (funnel-shaped junction). On one side: the slate roof rising away. On the other side: the edge dropping to the street far below. The gutter is the squad's primary rooftop transit route — fast, relatively concealed below the roofline, but vulnerable to rain flooding. Neutral grey background, even studio lighting, four views.
```

### 9.8 Mortar Joint Climbing Route

```
3D model of a Victorian London stock brick wall face in extreme close-up, viewed at fairy scale (4-inch character perspective), circa 1885. A section approximately 2x2 feet showing the climbing surface. Bricks in Flemish bond (alternating headers and stretchers). Each brick course (brick + mortar joint) = approximately 75mm = roughly 3/4 character height. Lime-and-sand mortar joints are 6-12mm wide — at fairy scale, ledge-width handholds. Older joints are eroded, creating deeper finger-holds. Some mortar is crumbling, leaving deeper recesses. The brick surface is slightly rough, sooty on the weather-exposed face. A small crack where a brick has shifted provides a larger handhold. This is the universal climbing medium — every brick building in London presents this surface. Slow but always available. Neutral grey background, even studio lighting, four views.
```

---

## 10. Environmental Hazard and Threat Components

Fauna and environmental dangers for scene dressing and gameplay encounters. Scaled relative to the 4-inch fairy characters.

### 10.1 Cat on a Wall

```
3D model of a Victorian London alley cat, a domestic short-hair tabby, circa 1885. Crouched on a London stock brick wall in hunting posture — body low, eyes wide, ears forward, tail tip twitching. The cat is approximately 18 inches body length — at fairy scale, 4.5x character height, a tiger-equivalent predator. Lean, not well-fed — a mouser, not a pampered house cat. Matted fur in places. Scars on one ear. Yellow-green eyes reflecting light. The wall surface shows mortar joints and soot. At fairy scale, this cat fills the entire field of view — a massive apex predator that can move silently and strike faster than any squad member can react. Neutral grey background, even studio lighting, four views.
```

### 10.2 Brown Rat in Sewer

```
3D model of a Victorian London brown rat (Rattus norvegicus) in a brick sewer tunnel, circa 1885. The rat is approximately 9 inches body length (plus 7-inch tail) — at fairy scale, 2.25x character height, a bear-equivalent. Standing on its hind legs in an aggressive posture, teeth bared, in the egg-shaped sewer tunnel (see 9.2). Coarse brown fur, wet and matted. Long naked tail. Small dark eyes, large ears. The sewer environment around it: damp brick walls, the central flow channel, dim light from a distant grating. At fairy scale, this is a formidable territorial predator in its home environment. The squad encounters rats in every underground journey. Neutral grey background, even studio lighting, four views.
```

### 10.3 Pigeon Cluster on Rooftop

```
3D model of three Victorian London pigeons on a slate rooftop near a chimney stack, circa 1885. Rock doves (feral pigeons), approximately 12-13 inches each — at fairy scale, 3x character height, large clumsy herbivores dangerous through mass. Typical London coloring: grey with iridescent green-purple neck patches, some white mottling. One pecking at the gutter, one perched on a chimney pot rim, one with wings half-spread landing. The rooftop environment: Welsh slate tiles, lead flashing, chimney stack. Pigeon droppings coating the area (white splatter on dark slate). At fairy scale, these are not predators but dangerous through sheer clumsiness — a pigeon landing on you is a car crash. Neutral grey background, even studio lighting, four views.
```

### 10.4 Spiderweb in Wall Void

```
3D model of a large funnel web spider's web stretched across a Victorian wall void between timber studs, viewed at fairy scale (4-inch character perspective), circa 1885. The web fills the 3-4 inch space between studs — at fairy scale, a net stretched across a room. Silken strands are visible as thick cables. The funnel retreat is in one corner — a dense silk tube where the spider waits. The spider itself (house spider, Tegenaria domestica, approximately 1/2 inch body) is visible at the funnel entrance — at fairy scale, a dog-sized creature with eight legs. The web glistens with moisture droplets. Caught in the web: a fly husk, a small moth. The surrounding wall void shows lath strips, plaster bulges, brick behind. At fairy scale, walking into this web means being trapped — strength alone may not break free. Neutral grey background, even studio lighting, four views.
```

### 10.5 Cockroach

```
3D model of a Victorian London cockroach (oriental cockroach, Blatta orientalis), circa 1885, shown at fairy scale on a kitchen floor. The cockroach is approximately 1-1.5 inches long — at fairy scale, roughly 1/3 character height, a medium-dog equivalent. Dark brown-black, glossy carapace, long antennae, six spiny legs. Positioned on a flagstone kitchen floor near a crumb (boulder-sized at fairy scale). The cockroach is common in every Victorian kitchen, cellar, and bakehouse. At fairy scale, it's a fast-moving, hard-shelled animal — not predatory but startling and omnipresent in interior environments. The surrounding floor shows crumbs, a drop of water, a crack between flagstones. Neutral grey background, even studio lighting, four views.
```

### 10.6 Kestrel on Chimney Pot

```
3D model of a kestrel (Falco tinnunculus) perched on a Victorian chimney pot, circa 1885. The kestrel is approximately 13-15 inches body length with a 24-27 inch wingspan — at fairy scale, an eagle-equivalent, the deadliest aerial threat. Russet-brown plumage with dark spots, hooked beak, sharp talons gripping the terra cotta chimney pot rim. Head turned, scanning the rooftops below. Eyes: intense, focused, designed to spot mouse-sized prey from height. The chimney pot is a cylindrical crown-top design. The background roofscape: slate roofs, chimney stacks, a grey London sky. At fairy scale, this raptor is a lethal presence — a kestrel sighting means all aerial movement stops. Even below-roofline movement is dangerous. This is the apex aerial predator of the GrimGlow world. Neutral grey background, even studio lighting, four views.
```

---

## 11. Weather and Atmospheric Variant Components

Scene-variant pieces for weather-dependent gameplay states. Each modifies the baseline dry/clear environment.

### 11.1 Fog-Shrouded Street Scene

```
3D model of a Victorian London street scene in dense fog (pea-souper), circa 1885. A narrow Clerkenwell street with London stock brick buildings on both sides, barely visible beyond 5-6 feet. A gas lamp in the foreground: its flame creates a yellow-orange halo in the fog, the light diffusing into a glowing sphere that illuminates almost nothing beyond arm's reach. The fog is yellow-green-grey, not white — coal smoke mixed with Thames moisture. The granite setts gleam wet. A figure (human) is barely visible as a dark shape 10 feet away. At fairy scale, this fog is near-total concealment — the squad's best operating conditions. But the fog also conceals Titans. The atmosphere is thick, acrid, sulphurous. Sound is muffled but carries strangely. Neutral grey background, even studio lighting, four views.
```

### 11.2 Rain-Flooded Roof Gutter

```
3D model of a Victorian cast-iron roof gutter during heavy rain, viewed at fairy scale (4-inch character perspective), circa 1885. The 4.5-inch half-round gutter is now a raging torrent — rainwater pouring off the slate roof fills the gutter to overflowing. Water splashing over the gutter rim. Raindrops (5mm each — half-inch, head-sized at fairy scale) impact the water surface with violent splashes. The leaf debris that was terrain in dry weather is now tumbling in the flow. The drainpipe hopper head at the end is a whirlpool as water funnels down. The slate roof above is a cascade of flowing water. At fairy scale, this is a flash flood — the primary rooftop highway is impassable. A character caught in the flow would be swept toward the drainpipe. Neutral grey background, even studio lighting, four views.
```

### 11.3 Frost-Covered Rooftop

```
3D model of a Victorian London rooftop in winter frost, viewed at fairy scale (4-inch character perspective), circa 1885. Welsh slate tiles coated in white frost — each tile surface is an ice rink. The roof gutter contains frozen water — a solid ice surface, walkable but slippery. Icicles hang from the drainpipe bracket (a bracket that was a rest platform is now guarded by spears of ice). The chimney stack radiates warmth — a circle of melted frost around its base, the only unfrozen zone. Frost crystals on the lead flashing create a glittering crystalline landscape. Breath would be visible (detection risk). The cold is the enemy — fairy-scale bodies lose heat rapidly. The contrast: warm zones near chimneys vs lethal cold zones on exposed slate. Neutral grey background, even studio lighting, four views.
```

### 11.4 Snow-Dusted Cobbled Street

```
3D model of a Victorian London street with 1-2 inches of fresh snow, circa 1885. Granite setts partially visible where cart wheels and foot traffic have cleared the snow — dark wet stone against white snow, creating a patchwork. Cart tracks: two parallel cleared lines with compressed brown snow. Footprints: human boot prints creating crater-sized depressions at fairy scale. A swept pavement section in front of a shop (shopkeepers clear their frontages). Snow piled against the kerbstone — at fairy scale, a drift chest-high to a character. A gas lamp with snow on its bracket and lantern hood. The cold muffles sound. Fresh snow reveals tracks — fairy bootprints (tiny, five-in-a-line, too ordered for insects) would be visible and distinctive. At fairy scale, snow transforms the terrain: new concealment challenges, new hazards, but also new possibilities (snow insulates, frozen puddles become platforms). Neutral grey background, even studio lighting, four views.
```

---

## 12. Vehicles and Transport

Victorian London's streets are dominated by horse-drawn traffic. At fairy scale, every vehicle is a rolling building, every hoof a crushing piston. The squad navigates around, under, and through a constant flow of transport.

### 12.1 Hansom Cab

```
3D model of a Victorian London hansom cab, circa 1885. A two-wheeled horse-drawn carriage, the "gondola of London." Black-painted body with a low-slung passenger compartment seating two, entered through folding doors at the front. Large spoked wheels (approximately 4.5 feet diameter) with iron tyres. The driver (cabman) sits elevated behind and above the passenger compartment on an exposed seat, holding reins that pass over the cab roof. A folding leather hood over the passenger seat. Brass oil lamps on each side. A whip socket. The cab number painted on the rear panel. Registration plate. The body is compact and elegant — designed for speed through narrow streets. Black lacquer with some brass trim. At fairy scale, each wheel is a 13-story-high rolling disc. The iron tyre cutting across granite setts is a wall of moving metal. Neutral grey background, even studio lighting, four views.
```

### 12.2 Horse Omnibus

```
3D model of a Victorian London horse omnibus, circa 1885. A large enclosed carriage on four wheels, pulled by two horses (not modeled — see 12.5). Painted in the livery of the London General Omnibus Company: dark red body with cream upper panels and route destination boards. Lower deck: enclosed saloon with windows, bench seating for 12-14 passengers, rear platform with stairs to the upper deck. Upper deck: open-air "knife-board" bench seating back-to-back along the center, accessed by a steep iron spiral staircase at the rear. A conductor on the rear platform. Advertising boards along the upper deck sides: "PEARS' SOAP" and "BOVRIL." Four large spoked wheels, iron tyres. The omnibus is approximately 16 feet long and 8 feet wide — at fairy scale, a multi-story mobile building. Neutral grey background, even studio lighting, four views.
```

### 12.3 Goods Cart / Dray

```
3D model of a Victorian London heavy goods cart (dray), circa 1885. A flat-bed four-wheeled cart designed for hauling barrels, crates, and bulk goods. Heavy timber construction with iron-shod wheels (rear wheels larger than front). The bed is approximately 10 feet long, 5 feet wide, and 3.5 feet off the ground. Iron-tyred wheels, massive axles. Sideboards approximately 12 inches high to prevent cargo sliding. A pair of heavy chain traces for hitching to a draught horse. Currently loaded: two beer barrels on their sides, secured with rope, and stacked wooden crates stenciled with "TRUMAN, HANBURY, BUXTON & CO." A canvas tarpaulin half-covering the load. Iron brake lever at the driver's position. At fairy scale, the undercarriage is a moving cave — the squad could ride beneath a cart for concealed street-level transport. Neutral grey background, even studio lighting, four views.
```

### 12.4 Costermonger's Barrow

```
3D model of a Victorian London costermonger's hand-barrow (street vendor's cart), circa 1885. A shallow wooden tray approximately 4 feet long and 2.5 feet wide, mounted on two large spoked wheels and two rear legs. A single handle-bar for pushing. The tray displays goods for sale: piled oranges, apples, and a scale with brass weights. A canvas awning on a folding iron frame provides shade over the goods. A paraffin lamp hangs from the awning frame for evening trading. A hand-painted price board: "ORANGES 2 FOR 1D." The barrow is brightly painted — blue or green — the costermonger's pride. At fairy scale, this is a mobile market stall — the tray is a plateau of fruit boulders, the awning a tent roof, the wheels building-height. Neutral grey background, even studio lighting, four views.
```

### 12.5 Draught Horse

```
3D model of a Victorian London draught horse, a heavy Shire or Clydesdale type, circa 1885. Standing in harness, approximately 17 hands (5 feet 8 inches at the shoulder). Massive build — broad chest, thick legs with heavy feathering at the fetlocks. Dark bay or black coat, slightly dull from city life. Leather collar harness with brass fittings, chain traces, blinkers. Harness shows wear — mended with wire in places. The horse stands on granite setts, one iron-shod hoof slightly raised. Nostril steam visible (cold morning). Dung on the ground behind. At fairy scale, this horse is an impossibly large creature — 17x character height at the shoulder. Each hoof is 5 inches across, coming down with the force of a building collapse. The horse is the dominant living feature of every Victorian street. Neutral grey background, even studio lighting, four views.
```

### 12.6 Cab Horse

```
3D model of a Victorian London cab horse (lighter build than draught), circa 1885. Standing in traces, approximately 15 hands (5 feet at the shoulder). A lighter, quicker horse than the heavy draught — Cleveland Bay or similar coaching breed. Brown or chestnut coat, leaner build, longer legs. Lighter harness than the dray horse — collar or breastplate harness, brass-mounted, reasonably well-maintained (cab owners were licensed and inspected). Cab horse stands alert, ears forward. Feed nosebag hanging from the bridle when stationary. At fairy scale, still enormous — 15x character height — but faster and more unpredictable than a draught horse. Cab horses move quickly through traffic; their hooves strike the setts in rapid rhythm. Neutral grey background, even studio lighting, four views.
```

### 12.7 Steam Locomotive on Viaduct

```
3D model of a Victorian steam locomotive crossing a brick railway viaduct, viewed from street level below, circa 1885. The locomotive is a London, Brighton and South Coast Railway 0-4-2 tank engine — compact, designed for suburban service. Black livery with brass dome and copper-capped chimney. Visible from below: the underframe, drive wheels (approximately 5.5 feet diameter), connecting rods in motion, and steam/smoke billowing from the chimney and around the wheels. The viaduct parapet partially obscures the engine — only the upper boiler, chimney, and smoke are clearly visible above the brick parapet wall. Smoke and steam cascade down the viaduct face. The noise is thunderous — at fairy scale, a passing train is an earthquake. The vibration shakes the entire viaduct structure and everything attached to it. Neutral grey background, even studio lighting, four views.
```

### 12.8 Thames Lighter / Barge

```
3D model of a Thames sailing barge (spritsail lighter), moored at a Wapping wharf, circa 1885. Flat-bottomed, approximately 80 feet long and 18 feet beam. Built of heavy oak planking, tarred black. A single spritsail mast with a large russet-brown sail furled to the sprit. The hold is open, loaded with stacked timber or sacks of grain. A small cabin aft with a stovepipe chimney. Heavy timber fenders along the hull sides. Mooring ropes to quayside bollards. The barge sits low in the water — the gunwale is perhaps 2 feet above the waterline when loaded. A lighterman's sweep (long steering oar) shipped along one side. At fairy scale, this barge is a floating island — a vast timber platform riding on the water. The mooring ropes are bridges to the quayside. Neutral grey background, even studio lighting, four views.
```

### 12.9 Steam Tug

```
3D model of a Victorian Thames steam tug, circa 1885. A small, powerful vessel approximately 50 feet long. Black-painted iron hull. A tall thin smokestack amidships belching dark coal smoke. Wheelhouse aft with brass-framed windows. Forward deck with a heavy iron towing bollard and coiled hemp hawser. The tug sits low in the water, compact and functional. Paddle wheels on each side (visible above the waterline) or a single screw propeller (not visible). A steam whistle on the smokestack. Registry number painted on the bow. Crew of 3-4 visible positions. The tug is used to manoeuvre sailing barges and larger vessels in the dock basins and Thames reaches. At fairy scale, a moving iron island trailing smoke. Neutral grey background, even studio lighting, four views.
```

---

## 13. Landmark Buildings — GrimGlow Triangle

Specific real historical buildings in or near the squad's operating area that serve as navigation landmarks, mission locations, or atmospheric set dressing.

### 13.1 Smithfield Meat Market — Clerkenwell

```
3D model of Smithfield Central Markets, West Smithfield, circa 1885. A massive iron-and-glass market hall designed by Horace Jones, opened 1868. Portland stone and red granite facade — ornate Victorian Romanesque with arched entrances wide enough for loaded carts. The interior visible through the arches: a vast covered hall with cast-iron columns supporting a glass-and-iron roof, allowing daylight in. Decorative iron dragons on the corner towers (the City of London emblem). The building spans an entire city block — approximately 250 feet long. Four corner octagonal turrets with domed copper roofs. Gas lights inside the hall creating a warm glow. At dawn, the market is a chaos of carcasses, porters, and cart traffic. At fairy scale, the interior is a cathedral of iron and glass. Located just west of Clerkenwell — a major navigation landmark. Neutral grey background, even studio lighting, four views.
```

### 13.2 St John's Gate — Clerkenwell

```
3D model of St John's Gate, St John's Lane, Clerkenwell, circa 1885. A surviving medieval gatehouse, built 1504, the south gate of the Priory of the Knights of St John. Two-story stone structure spanning the narrow lane — vehicles and pedestrians pass through the arched gateway below, rooms above. The arch is approximately 12 feet wide and 15 feet high, with a four-centered Tudor arch in Kentish ragstone. The upper story: Tudor windows with stone mullions, a projecting oriel window on the south face. By 1885, the gate is occupied by businesses — a pub (The Old Jerusalem) operates in the rooms above. The surrounding buildings abut the gate on both sides. At fairy scale, this arch is an immense stone cathedral-vault they pass beneath. One of Clerkenwell's most distinctive landmarks — the squad would use it as a cardinal reference point. Neutral grey background, even studio lighting, four views.
```

### 13.3 Pawnbroker's Shop — Clerkenwell/Bermondsey

```
3D model of a Victorian pawnbroker's shop front, circa 1885. London stock brick, two stories, with the distinctive three brass balls hanging from an iron bracket above the door — the universal pawnbroker's sign. Ground floor: a double shop front with small-paned windows displaying a chaotic jumble of pledged goods — watches, tools, clothing, boots, musical instruments. A painted fascia: "LICENSED PAWNBROKER — ADVANCES MADE." The entrance is recessed with a narrow passage (for privacy — customers don't want to be seen entering). A gas lamp bracket on the wall. Iron security shutters folded back during business hours. Upper floor: domestic windows, curtains drawn. Pawnbrokers were found on almost every high street — the working class's bank. Neutral grey background, even studio lighting, four views.
```

### 13.4 Metropolitan Police Station

```
3D model of a Victorian Metropolitan Police station house, circa 1885. London stock brick with Portland stone dressings, three stories. Official and institutional — a blue lamp above the entrance marked "POLICE." Heavy paneled double doors. Ground floor: charge room window (frosted glass for privacy), notice board with public announcements. Upper floors: section house (living quarters for unmarried constables) — uniform rows of sash windows. A yard gate to one side leading to an enclosed exercise yard and cells at the rear. The building is solid, authoritative, no-nonsense. Welsh slate roof. An iron-railed front area. At fairy scale, the blue police lamp is a landmark beacon — and the station itself is a threat (the squad could be captured and investigated as curiosities). Neutral grey background, even studio lighting, four views.
```

### 13.5 Fire Station — Horse-Drawn Era

```
3D model of a Victorian Metropolitan Fire Brigade station, circa 1885. London stock brick with decorative red brick banding and stone dressings, three stories. Ground floor: two wide arched engine bays with timber doors (one open, showing the red-painted horse-drawn steam fire engine inside). A brass sliding pole visible through a hatch from the upper floors. Watch room window beside the bays. A fire alarm telegraph mounted on the wall. Upper floors: crew quarters — dormitory windows. A hose-drying tower at the rear — a tall narrow brick tower with louvered openings for hanging wet hoses to dry. A flagpole on the roof. The station is always crewed, always ready. Horses stabled inside, trained to back into traces at the alarm bell. At fairy scale, the alarm bell and the explosive departure of horse-drawn engines is a cataclysmic event. Neutral grey background, even studio lighting, four views.
```

### 13.6 Public Bathhouse and Washhouse

```
3D model of a Victorian public bathhouse and washhouse, circa 1885. London stock brick with ornamental stone details and a grand arched entrance — these buildings were designed to look impressive, to encourage the working class to bathe. Portland stone inscription above the door: "BATHS AND WASHHOUSES — ESTABLISHED BY THE VESTRY OF CLERKENWELL." Separate entrances marked "MEN" and "WOMEN." A tall chimney stack for the boiler that heats the water. Arched windows with frosted glass for privacy. Tiled interior visible through the entrance — white glazed brick and ceramic tile. The building is larger than surrounding terraces — a civic facility. A penny for a cold bath, twopence for hot. At fairy scale, the interior is a warm, steamy, tiled cavern with pools of water — both a resource and a hazard. Neutral grey background, even studio lighting, four views.
```

### 13.7 Market Stall — Smithfield / Street Market

```
3D model of a Victorian London open-air market stall, circa 1885. A temporary timber-frame structure with a canvas awning stretched over a trestle table. The table approximately 6 feet long, 3 feet wide, laden with goods — depending on variant: meat cuts (Smithfield), vegetables (street market), secondhand clothing, or tools. A set of brass scales with iron weights. Price cards hand-written on scraps of card. A paraffin lantern hanging from the awning pole for early-morning or evening trading. The stallholder's cash box (tin) and wrapping paper. Crates and baskets stacked behind and beneath the table. At fairy scale, this stall is a tent city — the trestle table is an elevated platform, the canvas awning a vast roof, the goods a landscape of produce boulders. Neutral grey background, even studio lighting, four views.
```

---

## 14. NPC Character Models — The Giants of London

Victorian London's population in 1885 was approximately 4.5 million — the largest city in the world. Every street is crowded with people. At fairy scale, each human is a moving skyscraper: approximately 16-17x character height, with boots that impact the ground like meteor strikes. NPCs are not scenery — they are the primary environmental hazard on every surface route.

**Scale reminder:** An average Victorian man (~5'6") is 66 inches tall. A 4-inch fairy is 1/16.5 of that. At fairy scale, a human is the equivalent of a creature approximately 100 feet tall to us. Their footsteps shake the ground. Their voices are felt as vibration.

### 14.1 Police Constable — Metropolitan Police

```
3D model of a Victorian Metropolitan Police constable on foot patrol, circa 1885. Tall (minimum height requirement: 5'9"), wearing the standard uniform: dark blue single-breasted tunic with high collar and silver buttons, dark blue trousers, black leather boots. The distinctive custodian helmet (the "bobby's helmet") — blue cloth over a cork frame with a front plate badge bearing the division letter and number. Equipment: a bull's-eye lantern hanging from his belt, a wooden truncheon concealed in a long trouser pocket, a whistle on a chain. Clean-shaven (required). Walking at a measured pace — the constable's beat takes exactly 2 hours and covers a fixed route. Hands clasped behind the back. Calm authority. At fairy scale, his measured footsteps are predictable — a clockwork giant whose route can be learned and avoided. Neutral grey background, even studio lighting, four views.
```

### 14.2 Crossing Sweeper — Child

```
3D model of a Victorian London crossing sweeper, a child approximately 10-11 years old, circa 1885. Ragged clothing: an oversized adult coat cut down, patched trousers tied with string at the waist, a battered cloth cap, no shoes (or broken boots stuffed with newspaper). Thin, dirty face, bright alert eyes. Holding a besom broom (birch twigs on an ash handle) — the broom is taller than the child. The child's job: sweep a path through horse dung at busy intersections so gentlemen and ladies can cross without soiling their boots. A tin cup for tips tucked in one pocket. Standing at the edge of a kerb, scanning for customers. At fairy scale, this child is still enormous — 12-13x fairy height — and the broom is a devastating weapon sweeping in 3-foot arcs. But the sweeping creates temporary clean corridors across intersections. Neutral grey background, even studio lighting, four views.
```

### 14.3 Lamplighter

```
3D model of a Victorian London lamplighter on his evening round, circa 1885. A working man in a dark coat and cloth cap, carrying a light ladder (approximately 6 feet, carried over one shoulder) and a brass lighting pole with a small flame at the end. The ladder is lightweight — two thin poles with narrow rungs, designed to lean against lamp posts. His route takes him from lamp to lamp at dusk, turning the gas tap and touching the flame to the mantle. He works quickly — each lamp takes seconds. A leather satchel at his hip contains spare mantles and a turn-key. At fairy scale, the lamplighter is a moving giant who predictably visits every gas lamp along his route, creating pools of light in sequence as darkness falls. His schedule is utterly reliable — he's the human equivalent of a clockwork mechanism. Neutral grey background, even studio lighting, four views.
```

### 14.4 Factory Worker — Bermondsey

```
3D model of a Victorian Bermondsey factory worker (male), circa 1885. A working man in heavy-duty clothing: a rough flannel shirt with rolled sleeves, a leather apron stained with chemicals (tannery) or flour (biscuit factory), corduroy trousers, heavy hobnailed boots. A cloth cap. Arms thick from manual labor. Face weathered, hands calloused. Carrying: a tin lunch pail and a clay pipe. Walking in a crowd — factory workers move in groups at shift change times (6am start, 6pm finish). They fill the narrow streets like a tide. At fairy scale, a shift change is a stampede — hundreds of hobnailed boots striking granite setts in thunderous rhythm. The crowd moves fast and takes up the entire street width. The most dangerous regular event on Bermondsey's streets. Neutral grey background, even studio lighting, four views.
```

### 14.5 Dock Worker / Stevedore — Wapping

```
3D model of a Victorian London dock worker (stevedore), Wapping, circa 1885. A powerfully built man in a loose flannel shirt, leather waistcoat, canvas trousers, and heavy boots. A cloth cap or wide-brimmed felt hat. A broad leather belt. Hands wrapped in strips of leather for grip. Carrying a bale hook — a short-handled iron hook used for grabbing and hauling cargo bales and sacks. Face weathered by outdoor work. Walking across a cobbled wharf apron. Dock workers are casual labour — they gather each morning at the dock gates hoping to be chosen for a day's work. Those not chosen disperse into the surrounding streets. At fairy scale, the bale hook is a terrifying weapon and the stevedore's heavy tread shakes the wharf cobbles. Neutral grey background, even studio lighting, four views.
```

### 14.6 Gentleman — City / Clerkenwell

```
3D model of a Victorian London gentleman, middle class, circa 1885. Wearing: a black frock coat (knee-length), matching waistcoat with watch chain across the front (a gold pocket watch at one end, a fob seal at the other), grey or striped trousers, polished black boots. A silk top hat (approximately 6 inches tall). White shirt with a high starched collar and dark cravat or necktie. Carrying a walking stick (ebony with a silver handle) and possibly a folded newspaper under one arm. Clean-shaven or with neat side-whiskers. Walking with purposeful stride on the pavement. At fairy scale, the top hat adds another 1.5x fairy-heights to an already towering figure. The walking stick taps the pavement at regular intervals — a rhythmic percussion that can be heard and predicted. The watch chain is a visible landmark at waistcoat level. Neutral grey background, even studio lighting, four views.
```

### 14.7 Working Woman — Clerkenwell/Bermondsey

```
3D model of a Victorian London working-class woman, circa 1885. Wearing: a plain cotton dress in dark fabric (brown or dark blue), a white apron tied at the waist, a shawl wrapped around the shoulders and crossed at the front, and a bonnet or plain straw hat. Practical boots. Sleeves rolled to the elbows — she's been working. Carrying: a wicker shopping basket on one arm with a loaf of bread and wrapped parcels visible. A bunch of keys on a chain at her waist. Hair pinned up under the bonnet. Expression alert, purposeful — managing a household on limited money. Walking on the pavement. At fairy scale, her skirts sweep the pavement — the fabric edge is a slow-moving wall that could knock a fairy off the kerb. The basket creates a shadow zone beneath it. Neutral grey background, even studio lighting, four views.
```

### 14.8 Street Urchin / Mudlark

```
3D model of a Victorian London street urchin, approximately 8-9 years old, circa 1885. A barefoot child in ragged clothing: a torn shirt, patched shorts held up by a single brace, no coat (or a filthy rag of one). Thin, dirty, quick-eyed. Hair matted. Crouched low, picking through Thames foreshore mud (mudlarking) for anything of value — coal, copper nails, rope, coins. One hand holds a small sack for finds. The child is wiry, fast, and alert — survival depends on speed and wit. At fairy scale, even a small child is 10-12x fairy height — still a giant, but a less predictable, ground-level one who crouches, reaches into small spaces, and peers closely at things. A mudlark might be the most likely human to actually spot the squad. Neutral grey background, even studio lighting, four views.
```

### 14.9 Cabman on His Cab

```
3D model of a Victorian London hansom cabman seated on his cab, circa 1885. The cabman sits on an elevated seat BEHIND and ABOVE the passenger compartment, exposed to the weather. Wearing: a heavy multi-caped greatcoat (multiple short capes at the shoulders for rain runoff), a low-crowned bowler hat, a thick wool scarf. Leather gloves. Holding reins that pass over the cab roof to the horse. A whip in a socket beside him. Face ruddy from years of outdoor exposure. Expression: watchful, scanning for fares. A tin cash box beside him. The cabman sees EVERYTHING from his elevated position — he's the eyes of the street, 8 feet above ground level. At fairy scale, the cabman's elevated vantage point makes him one of the most observant humans on the street — a surveillance platform moving through the city. Neutral grey background, even studio lighting, four views.
```

### 14.10 Costermonger — Street Vendor

```
3D model of a Victorian London costermonger (street vendor), male, circa 1885. A working man in distinctive coster dress: a cloth cap set at a jaunty angle, a neckerchief (bright colored — red or yellow), a corduroy waistcoat with pearl buttons (the costermonger's trademark), dark trousers, and heavy boots. Standing beside his barrow (see 12.4), calling out his wares. One hand gestures toward the goods, the other rests on the barrow handle. A leather money pouch at his waist. Voice loud — "ORANGES! LOVELY ORANGES! TWO A PENNY!" — the cry carries down the street. At fairy scale, the costermonger is one of the noisiest humans in the streetscape — his shouting is a deep booming vibration that masks other sounds. His attention is on customers, not on the ground. Neutral grey background, even studio lighting, four views.
```

### 14.11 Tannery Worker — Bermondsey

```
3D model of a Victorian Bermondsey tannery worker, circa 1885. A working man stripped to the waist (or wearing only a coarse sacking apron), arms and chest stained dark brown from handling tanning solutions. Heavy canvas trousers, wooden clogs (not leather boots — leather workers ironically wore wood to resist the chemicals). Forearms and hands permanently discoloured. Muscular from heavy manual work — hauling wet hides. Carrying a large scraped hide draped over one shoulder, heading to the drying frames. The smell is implied: tanning uses dog dung, urine, oak bark, and chromium compounds. Other workers avoided tannery men on the street. At fairy scale, the chemical staining makes this worker look otherworldly — hands and arms a different color from his face, clothes rigid with dried chemicals. Neutral grey background, even studio lighting, four views.
```

### 14.12 Theodore Hartley — The Squad's Giant Ally

```
3D model of Theodore Edmund Hartley, aged 12-13, tinker's apprentice, Clerkenwell, circa 1885. Viewed at fairy scale (4-inch character perspective). A boy of medium height for his age, slightly thin. Dark hair, untidy but not unkempt. Wearing: a collarless flannel shirt with rolled sleeves, a brown waistcoat (the pocket where Luma rides is visible at chest height), patched corduroy trousers, sturdy but worn boots, a cloth cap. His hands are notable: oil-stained, burn-scarred from workshop work, dexterous. At his waist: a small tool roll containing miniature screwdrivers, tweezers, and pliers — the instruments of a clockmaker's apprentice. Expression: curious, alert, with a hint of wonder. At fairy scale, Theodore is an enormous but gentle presence — his face fills the sky when he leans down to speak to the squad. His cupped hands are a platform. His waistcoat pocket is a room. He is both the squad's greatest asset and their greatest vulnerability. Neutral grey background, even studio lighting, four views.
```

---

## 15. Story Props and Fairy Tech Artifacts

Plot-critical objects referenced in the comic outline that need dedicated 3D models.

### 15.1 Fairy Glyph on Brickwork — Prior Operative Marks

```
3D model of a section of Victorian London stock brick wall (yellow-brown, sooty) with a faintly glowing holographic glyph etched into the mortar joint, circa 1885. The glyph is a small geometric pattern — interlocking triangles and lines, approximately 2 inches across — emitting a cool blue-white light that is only visible up close or in low light. The light has the structured, prismatic quality of fairy holographic technology: translucent, with geometric edges, not sparkle. The surrounding brick is unchanged — soot, weathering, ordinary. At fairy scale, this glyph is a prominent road sign, chest-height, clearly readable. To human eyes it would be dismissed as a trick of the light or ignored entirely. Multiple glyphs on a wall form a message — directional markers left by prior operatives mapping safe routes. Neutral grey background, even studio lighting, four views.
```

### 15.2 Fairy Tech Shard — Salvaged Component

```
3D model of a broken fragment of fairy technology, approximately 1.5 inches long. A shard of the structured holographic material that forms fairy suit components — translucent, prismatic, with geometric crystal-like edges. It emits a faint cool blue-white glow, brighter at the fractured edges where the internal light-geometry is exposed. The surface has fine geometric patterning — hexagonal micro-cells, like a honeycomb made of light. One end is a clean manufactured edge (part of the original device); the other is jagged, broken. This is what Theodore finds and keeps — his proof that fairies are real, that they're not magic but technology he almost understands. At fairy scale, this shard is a girder-sized structural element. At human scale, it fits in a boy's palm and glows faintly in the dark. Neutral grey background, even studio lighting, four views.
```

### 15.3 Wren's Salvaged Components — Scavenged Human Technology

```
3D model of a collection of Victorian-era precision components laid out on a small cloth, circa 1885. Items at fairy scale (4-inch character perspective): a brass precision gear (~3mm diameter, fairy-scale wheel-sized), a tiny optical lens (watchmaker's loupe element, fairy-scale window-sized), a coil of fine copper wire (hair-thin to humans, rope-diameter to fairies), a fragment of spring steel, and a sliver of quartz crystal. These are Wren's scavenged materials — "primitive" components she repurposes to repair fairy technology. Each item shows her selection criteria: the gear has unusually precise teeth, the lens is exceptionally clear, the copper is high-purity. A miniature tool roll beside them contains adapted tools. At fairy scale, these are heavy industrial materials requiring two hands to carry. Neutral grey background, even studio lighting, four views.
```

### 15.4 The Folklorist's Pamphlet — Machen's Fairy Sighting Report

```
3D model of a Victorian printed pamphlet, circa 1885. A thin paper booklet, approximately 5x7 inches, 8 pages, cheaply printed on off-white paper with a woodcut illustration on the cover showing a stylized fairy figure. Title in black letterpress type: "FAIRY LIGHTS IN CLERKENWELL — Being an Account of Recent Supernatural Manifestations — by J. Machen, B.A., Fellow of the Folk-Lore Society." The pages are slightly dog-eared. The printing is slightly uneven — this is a small-run job from a local printer (Arthur Hartley's press). Interior pages visible: columns of text with occasional woodcut illustrations. At fairy scale, this pamphlet is a billboard — the text enormous, the woodcut illustration a mural-sized portrait that the squad recognizes as a distorted version of themselves. Neutral grey background, even studio lighting, four views.
```

### 15.5 Squad Improvised Camp — Hidden Base

```
3D model of a miniature military encampment hidden inside a Victorian wall void, viewed at fairy scale (4-inch character perspective), circa 1885. The camp occupies a gap between brick walls — a cavity approximately 8 inches wide, 12 inches tall, 18 inches deep. The squad has organized it efficiently: sleeping rolls made from scavenged cloth scraps, a salvaged thimble repurposed as a water container, a small holographic emitter (cracked, flickering blue-white) mounted on a nail serving as a light source. Wren's repair station in one corner: fairy tech components laid out on a button used as a workbench, with adapted human tools. A watch face propped against the wall serves as a clock. Sable's command area: a fragment of map pinned to the brick with a thorn, holographic tactical markers projected onto it. Entry/exit via a gap where mortar has crumbled. Warm amber light from a distant gas lamp leaks through a crack. Neutral grey background, even studio lighting, four views.
```

### 15.6 Holographic Tactical Map Projection

```
3D model of a fairy-technology holographic map display, viewed at fairy scale (4-inch character perspective). A small cylindrical projector (fairy tech, metallic with geometric light patterns) projects a translucent blue-white three-dimensional map of several London streets into the air above it. The projection shows: building outlines as wireframe blocks, street paths as glowing lines, threat markers (red pulses) for known Titan positions, safe route markers (green) along tested paths, and the squad's current position (five small blue dots). The projection is approximately 6 inches across at fairy scale — a table-sized tactical display. The light is structured, geometric, prismatic — clearly technology, but to Victorian eyes it would look like a fairy enchantment hovering in mid-air. Cracks in the projector cause occasional flickers and dead zones in the map. Neutral grey background, even studio lighting, four views.
```

### 15.7 Titan Environmental Traces — Claw Marks and Residue

```
3D model of a section of Victorian London stock brick wall showing signs of Titan activity, circa 1885. Three parallel gouge marks scored diagonally across the brickwork — deep enough to chip brick, spaced approximately 4 inches apart. The gouges have an oily iridescent residue in them — the dark oil-on-water shimmer of Titan bio-material. Around the marks, the mortar has a faint discoloration, as if shadow has been absorbed into the surface. A smear of bioluminescent residue on the adjacent stone sill — faintly glowing in darkness, wrong-colored (shifting between green and violet). The ordinary brick surrounding the marks is unchanged — the contrast between mundane wall and alien damage is unsettling. At fairy scale, these claw marks are trenches gouged into a cliff face. The residue glows visibly. The squad can read these traces like tracks. Neutral grey background, even studio lighting, four views.
```

---

## 16. Natural Elements and Vegetation

Victorian London street vegetation and water features that serve as terrain and landmarks at fairy scale.

### 16.1 London Plane Tree — Street Tree

```
3D model of a mature London plane tree (Platanus × acerifolia), approximately 40-50 feet tall, circa 1885. The dominant street tree of Victorian London — pollution-tolerant, with distinctive mottled bark that peels in patches revealing cream, olive, and grey layers. Thick trunk (~3 feet diameter) with a heavy spreading canopy. Lower branches removed to about 10 feet for street clearance. Roots lifting the York stone pavement slabs around the base. A cast-iron tree guard at ground level (circular, ornate). The canopy provides a dense green ceiling over the street in summer. At fairy scale, this tree is a colossal landmark — the trunk is a cliff face with peeling bark plates that create ledges and handholds. The canopy is a forest. A single leaf is a hammock-sized platform. The tree guard is a fortress wall. This tree is a navigation waypoint, a shelter, and a vertical highway between ground and rooftop level. Neutral grey background, even studio lighting, four views.
```

### 16.2 Thames Water Surface — Tidal River

```
3D model of a section of the River Thames surface and near-bank area, Wapping waterfront, circa 1885. Dark water — the Thames is brown-black, opaque, carrying sewage, industrial discharge, and river sediment. The surface has a slow, heavy current with floating debris: timber fragments, coal dust, paper, vegetable waste. At the bank edge: exposed wooden piling (tarred, barnacle-encrusted) and stone quay wall descending into the water. The water level line shows tidal range — a dark wet band on the stonework above current water level, with green algae growth at the permanent splash zone. Small wavelets lap against the stone. At fairy scale, this river is an ocean — the waves are chest-high rollers, the debris is floating island-sized, the current is a powerful force. The water is completely opaque and undrinkable. A fallen leaf on the surface is a raft. Neutral grey background, even studio lighting, four views.
```

### 16.3 Ivy-Covered Wall Section — Climbing Plant Terrain

```
3D model of a Victorian London stock brick wall section heavily covered in English ivy (Hedera helix), circa 1885. The ivy covers approximately 70% of the wall surface — thick woody stems (some 2-3 inches diameter) anchored to the mortar joints, spreading into a dense mat of dark green leaves. The older stems near the ground are woody, bark-covered, twisted. Higher up, the growth is newer, greener, with aerial rootlets gripping the brick. Gaps in the ivy reveal the sooty brick beneath. At fairy scale, this ivy is a living wall-climbing network — the woody stems are log-sized highways, the leaves are overhead canopy providing concealment, the aerial rootlets are handholds. A character can travel vertically through the ivy layer, hidden from view, using stems as paths and leaf clusters as rest points. This is a primary wall-climbing route alternative to drainpipes. Neutral grey background, even studio lighting, four views.
```

### 16.4 Construction Scaffolding — Victorian Timber Style

```
3D model of Victorian-era construction scaffolding on a London stock brick building facade, circa 1885. Timber pole scaffolding — vertical standards (round timber poles ~4 inches diameter) lashed to horizontal ledgers and transverse putlogs with rope bindings (no metal scaffolding clips — those come later). Working platforms of rough-sawn planks laid across the putlogs at each floor level. Access ladders (timber) between levels. A timber hoist at the top with rope and pulley for lifting materials. The scaffolding is slightly irregular — hand-lashed joints vary in angle. Building materials stacked on platforms: bricks, mortar buckets, tools. At fairy scale, this scaffolding is a climbing frame of enormous log-sized timbers — the rope lashings are climbable knots, the plank platforms are elevated roads, the ladder is a staircase. An excellent navigation route when present but temporary and unstable. Neutral grey background, even studio lighting, four views.
```

### 16.5 Ship Masts and Rigging — Wapping Skyline

```
3D model of the upper masts and rigging of a sailing vessel visible above a Wapping warehouse roofline, circa 1885. Two or three wooden masts projecting above the rooftop, with a complex web of standing rigging (tarred hemp shrouds and stays) and running rigging (halyards, sheets). Furled sails on yards. The masts belong to a vessel moored in the dock basin behind the warehouse — only the upper portions are visible from street level. A pennant or flag at the masthead. The rigging creates a web of lines crossing the sky above the roofline. At fairy scale, these masts are towering spires rising above the warehouse cliffs, and the rigging is an aerial highway network — taut ropes spanning between masts that the squad can traverse. The rigging sways with wind and vessel movement, making it a dynamic route. Neutral grey background, even studio lighting, four views.
```

---

## 17. Key Interior Environments

Large-scale interior spaces that serve as major gameplay locations, distinct from the modular interior components in Section 8.

### 17.1 Public House Interior — Ground Floor Bar

```
3D model of a Victorian public house interior (ground floor bar room), circa 1885. A warm, crowded, low-ceilinged room. A long mahogany bar counter with a brass foot rail runs along one wall, behind it: a back-bar with mirror, shelved bottles (gin, rum, porter, whisky), ceramic beer pump handles. Gas light brackets on the walls and a larger gas chandelier — warm amber light reflecting off the bar mirror. Bench seating along the walls (wooden settles), small round tables with cast-iron pedestal legs. Sawdust on the floor (absorbs spilled beer and tobacco spit). A coal fire burning in a cast-iron fireplace with a decorative tile surround. Etched and frosted glass partition screens dividing the public bar from the saloon bar. Tobacco smoke hazing the air. Ceramic tile on the lower walls, dark wallpaper above. At fairy scale, this is a vast warm cavern — the bar counter is a cliff with a brass highway at its base, the tables are elevated platforms, the fireplace is a roaring furnace. The sawdust floor is a field of wood shavings chest-deep. Neutral grey background, even studio lighting, four views.
```

### 17.2 Warehouse Interior — Wapping Dock Storage

```
3D model of a Victorian dock warehouse interior, Wapping, circa 1885. A massive open floor space with heavy timber post-and-beam construction — cast-iron columns supporting thick timber beams and plank floors above. Multiple stories visible through open trap doors in the ceiling (used to hoist goods between floors). Stored goods stacked in rows: barrels (sugar, molasses, rum), bales wrapped in hessian (tea, tobacco, cotton), timber crates branded with shipping marks. A hand-operated crane/hoist at the loading door — chain, pulley wheel, wooden windlass. Cobbled floor worn smooth. Rats visible in the shadows between barrel rows. Dim light from small arched windows. Musty, sweet smell of stored goods. At fairy scale, this is a canyon city of stacked containers — barrel rows form streets, crate stacks form buildings, the timber beams overhead are a ceiling grid highway. The trap doors between floors are vertical shafts. Neutral grey background, even studio lighting, four views.
```

### 17.3 Sewer Junction Chamber — Navigation Node

```
3D model of a Victorian brick sewer junction chamber, part of Bazalgette's London sewer system, circa 1885. A vaulted brick chamber approximately 8 feet in diameter where three or four brick tunnel sewers converge. The tunnels are egg-shaped in cross-section (narrower at the bottom for better flow at low volume). The brickwork is engineering blue brick — glazed, dense, waterproof. A shallow channel of dark water flows through the center. The walls above water level are slick with condensation and bacterial growth. Iron access rungs set into the wall leading up to a manhole shaft. A ledge (the bench) runs along both sides above water level — the dry walking path for sewer workers (and fairy navigation). At fairy scale, this junction is a cathedral — the vaulted ceiling soars overhead, the tunnels are enormous corridors, the water channel is a river. The junction is a crossroads where multiple navigation routes meet. Echo and sound carry. Neutral grey background, even studio lighting, four views.
```

---

## 18. Additional NPC Character Models

Supplementary NPCs representing common Victorian London street occupations.

### 18.1 Cat's Meat Man — Street Vendor

```
3D model of a Victorian cat's meat man, circa 1885. A working-class man in worn clothing — a battered felt hat, a long coat greasy with handling raw meat, heavy boots. He carries a long wooden skewer-rack over one shoulder: dozens of thin wooden skewers threaded with small pieces of horsemeat (dark red, slightly dried), each skewer about 8 inches long — a half-penny per skewer. Cats follow him through the streets. His other hand holds a small handbell. His call: "Meat! Meat! Cat's meat!" A leather satchel at his hip for coins. His hands and forearms are stained with blood and grease. He walks a regular daily route through residential streets. At fairy scale, the hanging meat skewers are spear-like objects, and the cats following him are predators drawn to the area — his approach is both warning and hazard. Neutral grey background, even studio lighting, four views.
```

### 18.2 Chimney Sweep — Master and Boy

```
3D model of a Victorian chimney sweep and his climbing boy, circa 1885. The master sweep: a wiry man in completely black clothing (every surface coated in soot), a battered top hat (the sweep's traditional badge), carrying a bundle of jointed wooden chimney rods and circular wire brushes over his shoulder. His face is soot-black with eyes and teeth visible. The climbing boy (approximately 8-10 years old): similarly soot-covered, smaller, thinner, wearing only a shirt and trousers (no shoes — bare feet grip the flue interior better). The boy carries a small scraper and a cloth bag for collecting soot. Despite the 1875 Climbing Boys Act banning the practice, small sweeps still work illegally in 1885. At fairy scale, these figures are dark, ghoulish giants trailing clouds of soot — their approach blackens the air and creates visibility hazards. Neutral grey background, even studio lighting, four views.
```

### 18.3 Rat-Catcher with Terrier Dogs

```
3D model of a Victorian London rat-catcher, circa 1885. A lean man in rough clothing — moleskin trousers, a waistcoat covered in small brass badges and tokens (advertising his trade), a leather belt hung with wire rat traps, a cage containing live rats slung over his back (rats sold to sporting pubs for rat-baiting, or to laboratories). He carries a long ferret box under one arm and leads two small terrier dogs on leashes — wiry, alert, bred for ratting (likely Jack Russell or similar). The dogs strain forward, noses to the ground. A sack at his belt for dead rats. His hands are scarred with old bite marks. At fairy scale, the terrier dogs are the primary threat — fast, keen-nosed, and bred to chase small creatures through tight spaces. They would detect and pursue fairy-scale characters instantly. The live rats in the cage are fellow prisoners of scale. Neutral grey background, even studio lighting, four views.
```

---

## 19. London Topology — Elevation and Slopes

London is NOT flat. The GrimGlow operating triangle spans a 20-meter elevation change that, at fairy scale, transforms gentle Victorian street grades into dramatic hillside terrain.

### Elevation Data

| Location | Elevation (m ASL) | Terrain Character | Fairy-Scale Equivalent |
|---|---|---|---|
| **Clerkenwell Green** | ~22-25m | Hilltop. Medieval street grid follows contours. | Highland plateau — streets slope noticeably |
| **Clerkenwell Road** | ~18-20m | Main artery cutting along the hillside | Major ridgeline road |
| **Farringdon Road** (Fleet valley) | ~10-12m | Dips into buried Fleet River valley | Deep canyon/valley floor |
| **London Bridge (north end)** | ~8-10m | River crossing, embankment level | Mid-slope |
| **Bermondsey (Long Lane)** | ~3-5m | Former marshland, dead flat | Low plains — barely above water table |
| **Wapping (dock streets)** | ~3-5m | River level, reclaimed marsh | Coastal lowland |
| **Thames low tide** | ~0m | Exposed mud flats | Sea level / shore |
| **Thames high tide** | ~7m | Water level at London Bridge | Tidal flood zone |

**Source data:** Environment Agency LIDAR DTM (1m resolution, ±15cm accuracy). Modern terrain but London's underlying hills haven't changed since 1885 — street grades, river banks, and basic topology are identical. See `world-building/maps/lidar/` for heightmap data.

### The 20-Meter Drop — What It Means at Fairy Scale

The full elevation change from Clerkenwell hilltop (~25m) to Bermondsey marshland (~3m) is approximately **22 meters (72 feet)**. At fairy scale:

- 22 meters = **220 fairy-body-lengths** of vertical elevation change (each fairy is ~0.1m / 4 inches)
- Equivalent human experience: walking across a neighborhood that drops 1,320 feet — a serious mountain descent
- A street with a 1-in-20 gradient (barely noticeable to humans) has the fairy-scale equivalent of a 1-in-20 slope sustained over enormous distance — like hiking a mountain trail
- **Every street in Clerkenwell slopes.** Some gently, some steeply. This creates:
  - Directional advantage (downhill = faster, uphill = slower/exhausting)
  - Water flow patterns (rain always runs downhill toward the Thames)
  - Drainage and flooding zones (low points accumulate water)

### Key Topographic Features

**The Fleet River Valley:**
- Runs north-south between Clerkenwell and the City of London
- By 1885: enclosed underground by Bazalgette (now beneath Farringdon Road)
- The valley is still visible in street grades — Farringdon Road dips 8-10 meters below Clerkenwell to the west and Smithfield to the east
- At fairy scale: a dramatic canyon. The buried river is still flowing underground in a brick culvert — accessible via the sewer network
- Crossing the Fleet valley is a significant geographic challenge for the squad

**Clerkenwell Hill:**
- The highest ground in the operating area
- Streets radiate downhill in all directions from the Green
- Sekforde Street slopes gently south; St John Street slopes more steeply
- At fairy scale: the squad's hilltop stronghold — good sightlines, defensible ground, but exposed to wind

**Bermondsey Flats:**
- Former marshland, name means "Beormund's island" (was literally an island in marshes)
- Dead flat — the flattest terrain in the operating area
- High water table means perpetually damp cellars and foundations
- At fairy scale: open plains with poor drainage. Rain events create widespread shallow flooding
- The flatness makes it feel exposed — no high ground for observation

**Wapping River Terrace:**
- Sits on a narrow strip between the river and higher ground to the north
- The dock basins are excavated BELOW surrounding ground level — walled enclosures sunk into the earth
- At fairy scale: the dock basins are walled canyons with water at the bottom
- The Thames foreshore at low tide exposes mud flats — at fairy scale, a vast beach landscape with treacherous soft ground

**The Thames Tidal Range:**
- Tidal range at London Bridge: approximately 7 meters (23 feet)
- This means the river level rises and falls by ~70 fairy-body-lengths twice daily
- Wapping stairs and river stairs flood at high tide, expose mud at low tide
- The foreshore is only accessible for ~6 hours per tidal cycle
- Timing river crossings or foreshore travel requires tidal awareness

### Slope Effects on Navigation Networks

| Route Type | Uphill Effect | Downhill Effect |
|---|---|---|
| Rooftop gutters | Water pools at low points; gutters drain downhill | Rain water flows toward drainpipe hoppers |
| Drainpipes | No change (vertical) | No change (vertical) |
| Street-level | Exhausting climb; cart ruts channel water downhill | Faster but rain creates torrents in sett gaps |
| Sewers | Sewers slope toward the Thames by design — the squad walks against the flow going uphill | With the flow going downhill — faster but harder to stop |
| Flight | Updrafts on south-facing slopes (sun-warmed); downdrafts on north-facing | Chimney thermals strongest on hilltops (Clerkenwell) |

### Per-Neighborhood Slope Character

**Clerkenwell:**
Streets slope in multiple directions from the high ground. Most drain south toward Clerkenwell Road or west toward the Fleet valley. The medieval street grid means irregular angles — streets don't run straight, they follow old field boundaries and contour lines. This creates unexpected turns and hidden courts at different levels. Stepped alleys exist where the gradient is steepest.

**Bermondsey:**
Almost no slope. Drainage is poor — the flat terrain means water sits in puddles rather than flowing away. The sewer system does the work that gravity does in Clerkenwell. Streets feel corridor-like because they're flat and straight (post-Industrial Revolution grid, not medieval). The few elevated features (railway viaducts, factory loading bays) stand out dramatically against the flatness.

**Wapping:**
Gentle slope toward the river, then the abrupt vertical drop of quay walls and river stairs. Inside the dock complex, the ground is level (engineered). Outside, the streets between warehouses are nearly flat but slope slightly toward the gully drains that carry water to the river. The dominant vertical features are the warehouse walls (5-6 stories), not the terrain itself.

---

## 20. Base Terrain Tile Prompts

These prompts generate larger-scale ground surface sections (~5x5 meter tiles at human scale) designed to tile together to form continuous streetscapes. Unlike the small detail sections in Section 4, these are base terrain — the ground layer that buildings and furniture sit on.

**Tiling convention:** Each tile has flat edges at a consistent ground level so tiles can be placed adjacent. The surface detail (camber, gutters, kerbs) is contained within the tile. Edge conditions are described for seamless connection.

### 20.1 Main Road Tile — Clerkenwell Road Width

```
3D model of a 5x5 meter section of Victorian London main road, Clerkenwell Road style, circa 1885. The full road cross-section: cambered granite sett roadway approximately 8 meters wide, crowned in the center, sloping to stone-lined gutters on each side. York stone pavement (sidewalk) approximately 2 meters wide on each side. Granite kerbstones separating pavement from road — 12 inches tall, sharply squared. The road surface: rectangular granite setts in regular courses, worn smooth in the center by iron cart wheel tracks, rougher at the edges. Gutter channels along each kerb carrying water toward periodic drain gratings. The pavements: large rectangular York stone slabs, some slightly uneven from subsidence. The whole section has a very slight longitudinal slope (1-2%) representing Clerkenwell's hillside terrain. Tile edges are flat for seamless connection to adjacent tiles. Neutral grey background, even studio lighting, top-down and angled views.
```

**Edge connections:** Pavements at each side connect to building facades (Section 2 prompts). Road continues at each end. Cross-streets join at right angles or slight offsets.

### 20.2 Narrow Side Street Tile — Clerkenwell Back Streets

```
3D model of a 5x5 meter section of narrow Victorian side street, Clerkenwell residential style, circa 1885. Street width approximately 3-4 meters (10-12 feet) — barely room for a single cart. Granite setts fill the full width, cambered slightly to a central gutter channel (no separate pavement on the narrowest streets). Where pavement exists: a single row of York stone slabs, perhaps 18 inches wide, against one building face. London stock brick building facades visible at both edges — rising vertically from the street with no setback. The sett surface is slightly more irregular than the main road — less traffic means less wear, more original roughness. A slight curve in the street plan reflects medieval origins. Evidence of slope: water staining patterns showing downhill drainage direction. Tile edges flat for tiling. Neutral grey background, even studio lighting, top-down and angled views.
```

**Edge connections:** Building facades on both sides (minimal gap). Street continues with slight curves. May connect to main road tile at an irregular junction angle.

### 20.3 Back Alley Tile — Bermondsey

```
3D model of a 5x5 meter section of unpaved Victorian back alley, Bermondsey, circa 1885. Alley width approximately 1.5-2 meters (5-6 feet). Surface: compacted earth and clinker ash, NOT granite setts. Rough, rutted, with standing puddles in low spots. Broken brick fragments and oyster shells dumped as ad hoc paving in the muddiest patches. A crude drainage channel down the center — a shallow trench that's mostly clogged. London stock brick walls rise on both sides — sooty, damp-stained, with no decoration. A doorstep (single stone block) at one side where a back door opens into the alley. Scattered debris: cabbage leaves, a broken bottle, rags. This is the poorest terrain in the game. At fairy scale: a treacherous swamp between canyon walls. Tile edges flat for tiling. Neutral grey background, even studio lighting, top-down and angled views.
```

**Edge connections:** Connects to courtyard tiles (20.4) or emerges onto side street tiles (20.2). Building rear walls on both sides.

### 20.4 Enclosed Courtyard Tile — Bermondsey/Clerkenwell

```
3D model of a 5x5 meter section of an enclosed Victorian courtyard behind terraced houses, circa 1885. Irregular cobblestones (not neat setts — older, rougher, rounded stones). A shared privy structure against one wall (small brick outhouse with timber half-door). A standpipe or hand pump for communal water. Washing line posts — two timber posts with a rope between them. A brick-built dust bin (refuse container) in one corner. A gully drain in the center of the yard. The yard is enclosed by the rear walls of terraced houses on three sides and a high brick wall on the fourth. Windows overlook the yard. Damp staining on lower brickwork. Weeds in the cobble gaps. Domestic debris: a bucket, scattered coal dust, a child's wooden hoop. At fairy scale: a fortress courtyard. Tile edges defined by walls. Neutral grey background, even studio lighting, top-down and angled views.
```

**Edge connections:** Back alley tile connects through a gap in the wall. Building rears on three sides. Self-contained.

### 20.5 Churchyard / Green Space Tile

```
3D model of a 5x5 meter section of a Victorian London churchyard, circa 1885. Gravel path (compacted pale grey stone chips) approximately 1.5 meters wide, bordered by iron railings on one side and grass on the other. The grass is patchy urban grass — thin, worn in places, with moss and dandelions. Two or three weathered tombstones (dark stone, leaning, lichen-covered, inscriptions worn). A low box hedge, trimmed but scrappy. The gravel path surface: small angular stones, some weed growth between. At the edge: the church's cast-iron boundary railing on a low stone wall. A mature tree trunk visible at one corner (plane tree — London's dominant street tree). Fallen leaves in autumn accumulation. At fairy scale: gravel stones are boulders, grass is a forest of stems, the tombstones are monumental structures. Tile edges flat for tiling. Neutral grey background, even studio lighting, top-down and angled views.
```

**Edge connections:** Connects to pavement/street tiles via the railing boundary. Church facade on one side. Open to additional churchyard tiles.

### 20.6 Wharf Loading Apron Tile — Wapping/Bermondsey

```
3D model of a 5x5 meter section of a Victorian dock wharf loading apron, Wapping, circa 1885. Wide cobbled surface — granite setts but larger and rougher than street setts, laid for heavy cart traffic. The surface is flat (engineered, not natural terrain). Iron cart rail tracks embedded in the setts — a narrow-gauge tramway for moving cargo carts between warehouse and quayside. A cast-iron cannon bollard near one edge. A coil of heavy hemp rope. Iron mooring ring set into a stone block at the quay edge. The quay edge itself: large granite blocks forming a sharp vertical drop to the dock water below (or to the loading level of a barge). Crane base visible — four iron bolts in a square pattern set into the cobbles. Tar staining, salt deposits, rope abrasion marks on the stone. At fairy scale: an exposed industrial plateau at the edge of a cliff. Tile edges flat for tiling. Neutral grey background, even studio lighting, top-down and angled views.
```

**Edge connections:** Warehouse facades on one side. Quay edge/water on another. Continues along the dock frontage.

### 20.7 Dock Basin Edge Tile — Wapping

```
3D model of a 5x5 meter section of a Victorian dock basin quay wall and water, Wapping London Docks, circa 1885. The quay wall: massive granite blocks forming a vertical face approximately 3 meters high from water surface to quayside. Iron ladder rungs set into the wall for climbing from water level. Mooring rings at quayside level. The water: dark, oily, reflecting the surrounding warehouse walls. Floating debris — wood scraps, rope, straw. The quayside surface: granite setts. A timber fender hung over the edge to protect the wall from barge impacts. Below the waterline (shown in section): the wall continues down, green with algae. At fairy scale: a cliff overlooking an ocean. The ladder rungs are a viable descent route. The water is a vast dark expanse. Tile edges flat for tiling. Neutral grey background, even studio lighting, section view and top-down view.
```

**Edge connections:** Wharf apron tile on the quayside. Water continues to opposite quay wall. Warehouse facade behind.

### 20.8 Thames Foreshore / Mudflat Tile

```
3D model of a 5x5 meter section of Thames foreshore at low tide, Wapping/Bermondsey, circa 1885. The mud: grey-brown Thames clay, soft and treacherous. Partially exposed at low tide — the surface glistens with water. Scattered across the mud: broken clay pipe stems (the most common Thames find), pottery sherds, animal bones, rope fragments, occasional coins. Timber river stairs descend from a stone quay wall at one edge — the lower steps coated in green algae, slippery. Worm casts and small pools of standing water. Seagull footprints. The quay wall at the edge rises vertically — stone blocks with mooring rings and weed growth at the waterline. At fairy scale: a vast muddy beach landscape with treacherous soft ground — characters sink into the clay. The debris is a field of artifacts. Only accessible for ~6 hours per tidal cycle. Tile edges flat for tiling. Neutral grey background, even studio lighting, top-down and angled views.
```

**Edge connections:** River stairs/quay wall on the landward side. Water (Thames at low tide) on the riverward side. Foreshore continues laterally.

### 20.9 Bridge Roadway Tile

```
3D model of a 5x5 meter section of a Victorian London bridge roadway, circa 1885. Granite sett road surface, wider than a normal street — approximately 10 meters between parapets (the tile shows half the width). The road surface is flatter than a normal street — no camber, good drainage via scuppers through the parapet wall. On one side: a stone parapet wall approximately 1 meter tall, topped with a cast-iron balustrade railing. A gas lamp rises from the parapet at the tile edge. The parapet is Portland stone, soot-stained but maintained. Looking over the parapet: open sky and the river far below (not modeled — just the void). The road surface is swept cleaner than normal streets. No buildings on either side — the bridge is exposed. Wind is constant. At fairy scale: an exposed causeway with cliff-edge parapets and iron spear railings above. Tile edges flat for tiling. Neutral grey background, even studio lighting, top-down and angled views.
```

**Edge connections:** Bridge continues in both directions. No building connections — parapet walls on both sides.

### 20.10 Railway Embankment Tile

```
3D model of a 5x5 meter section of a Victorian railway embankment viewed from the street below, Bermondsey, circa 1885. The embankment rises approximately 5-6 meters above street level. Retaining wall at the base: engineering brick (blue-grey, hard), built in courses with weep holes for drainage. Above the wall: the earth embankment slopes up at approximately 45 degrees, covered in coarse grass, buddleia (the railway weed), and scattered rubble. At the top: a glimpse of iron railway fence and the edge of ballast stone. The street at the base: granite setts running along the foot of the embankment. A narrow pavement between the road and the retaining wall. Soot staining on the brickwork from locomotive smoke above. Puddles at the wall base from seepage. At fairy scale: the embankment is a massive earth cliff with a brick fortification at its base. Tile edges flat for tiling. Neutral grey background, even studio lighting, front elevation and angled views.
```

**Edge connections:** Street tile at the base. Embankment continues laterally. Railway arch tile (2.17) can interrupt the embankment face.

---

## 21. Two-Tier LOD Assembly Guide

### How the Layer Stack Works

The GrimGlow 3D world is assembled in layers, with two distinct levels of detail:

```
TIER 1 — STRATEGIC OVERVIEW (human-scale, ~50m camera distance)
┌─────────────────────────────────────────────┐
│ Layer 0: HEIGHTMAP TERRAIN                  │
│   Source: Environment Agency LIDAR DTM      │
│   What it provides: hills, slopes, river    │
│   Import as: Unity Terrain / Three.js plane │
│                                             │
│ Layer 1: STREET LAYOUT TEXTURE              │
│   Source: Goad fire plans, Booth maps       │
│   What it provides: road positions,         │
│   building footprints, open spaces          │
│   Applied as: terrain texture / decal       │
│                                             │
│ Layer 1B: SIMPLIFIED BUILDINGS              │
│   Source: Meshy building prompts at low LOD  │
│   What it provides: building mass / volume   │
│   Block shapes with correct proportions      │
│   Used for: mission planning, navigation     │
└─────────────────────────────────────────────┘

TIER 2 — TACTICAL DETAIL (fairy-scale, <5m camera distance)
┌─────────────────────────────────────────────┐
│ Layer 2: MESHY TERRAIN TILES (Section 16)   │
│   Detailed ground surface tiles             │
│   Granite setts, mud, cobbles, grass        │
│   Placed on streets identified in Layer 1   │
│                                             │
│ Layer 3: MESHY BUILDINGS (Section 2)        │
│   Full-detail building facades              │
│   All 28 building type prompts              │
│                                             │
│ Layer 4: MESHY FURNITURE (Section 3)        │
│   Gas lamps, bollards, postboxes            │
│   All 14 street furniture prompts           │
│                                             │
│ Layer 5: MESHY DETAIL (Sections 8-11)       │
│   Interiors, navigation, hazards, weather   │
│   Loaded only when camera is very close     │
└─────────────────────────────────────────────┘
```

### LOD Transition Strategy

| Camera Distance | What's Visible | Asset Source |
|---|---|---|
| **>100m** (city overview) | Heightmap terrain + street texture + building blocks | Layer 0 + 1 + 1B |
| **20-100m** (neighborhood) | Above + building facades + major furniture | Add Layer 3 (low-poly) + Layer 4 (gas lamps) |
| **5-20m** (street-level) | Full exterior detail | Layer 2 (terrain tiles) + Layer 3 (full) + Layer 4 (all) |
| **<5m** (fairy-scale) | Everything including interiors | All layers including Layer 5 |
| **<1m** (extreme close-up) | Interior terrain (workbench, clock mechanism) | Section 8 interior components only |

### Per-Neighborhood Tier 1 Assembly

**Clerkenwell (Tier 1 overview):**
- Heightmap: **Sloping terrain** — the hill is clearly visible. Streets angle downhill.
- Street texture: Medieval irregular grid. Clerkenwell Road cuts straight as the main artery; side streets meander.
- Building blocks: 2-3 story terraces (dominant), taller workshop blocks, church tower as landmark
- Green space: Clerkenwell Green as an actual open area. Churchyard at St James.

**Bermondsey (Tier 1 overview):**
- Heightmap: **Flat.** Almost no variation. Drainage is the story, not slopes.
- Street texture: Post-industrial grid. Long Lane as spine. Dense parallel side streets. Railway viaduct cutting through.
- Building blocks: Mix of 2-story housing (small) and 4-5 story warehouses/factories (large, dominant). The scale contrast tells you this is industrial.
- No green space. Everything is built.

**Wapping (Tier 1 overview):**
- Heightmap: **Flat with excavated dock basins** — the docks are sunken rectangles below ground level.
- Street texture: Few streets. Massive warehouse footprints. Narrow lanes between them. Dock basins as open water areas.
- Building blocks: 5-6 story warehouses (enormous, cliff-like). Few small buildings. Dock offices as the only non-industrial structures.
- Water: Dock basins and Thames visible.

### Building the Heightmap

**Step 1:** Download Environment Agency LIDAR DTM for the GrimGlow triangle area (see `maps/lidar/`).

**Step 2:** Crop to operating area — approximately:
- North: 51.528°N (north edge of Clerkenwell)
- South: 51.494°N (south edge of Bermondsey)
- West: -0.115°W (Fleet valley / Farringdon)
- East: 0.010°E (Trinity Buoy Wharf)
- Area: approximately 8km x 4km

**Step 3:** Import as heightmap:
- **Three.js (Phase 1):** Load as greyscale PNG, apply to `PlaneGeometry` with `displacementMap`. Scale vertical exaggeration for fairy-scale drama.
- **Unity (Phase 2):** Import as RAW file into Unity Terrain. Set terrain size to match real-world dimensions. Apply terrain textures per Layer 1 street layout.

**Step 4:** Overlay historic street layout using Goad fire insurance plans as reference for building placement and street positions.

### Terrain Tile Placement Guide

Terrain tiles (Section 20) are placed on the heightmap where streets exist:

| Tile Type | Where to Place | Typical Run Length |
|---|---|---|
| 20.1 Main Road | Clerkenwell Road, Long Lane, Wapping High Street | Continuous runs of 10-20 tiles |
| 20.2 Side Street | Sekforde St, Aylesbury St, most Clerkenwell streets | Runs of 5-10 tiles with curves |
| 20.3 Back Alley | Behind Bermondsey terraces, between warehouses | Short runs of 2-5 tiles |
| 20.4 Courtyard | Behind terraces in Bermondsey and Clerkenwell | Single tile, self-contained |
| 20.5 Churchyard | St James Clerkenwell, decommissioned church | 2-4 tiles around church |
| 20.6 Wharf Apron | Wapping dock frontages, Bermondsey wharves | Continuous runs along waterfront |
| 20.7 Dock Basin Edge | Inside London Docks, St Saviour's Dock | Perimeter of dock basins |
| 20.8 Foreshore | Thames riverbank at low tide | Strips along river edge |
| 20.9 Bridge | London Bridge, Southwark Bridge crossings | 10-15 tiles per bridge |
| 20.10 Embankment | Bermondsey railway viaduct approaches | Runs parallel to viaduct |
