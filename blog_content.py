"""Blog posts. Pure data: build.py renders /blog.html and one page per post.

Each section is (heading, [paragraphs], [optional bullet list]).
"""

POSTS = [
    {
        "slug": "blog-cold-room-icing-up.html",
        "date": "2026-10-30",
        "title": "Why Is My Cold Room Icing Up? Causes and Fixes",
        "meta_title": "Why Is My Cold Room Icing Up? | RM Air Solutions Durban",
        "desc": "Ice on a cold room evaporator means the room is losing cooling. The common causes, what you can check yourself, and when to call a technician.",
        "img": "blog-cold-room-ice",
        "img_alt": "Technician inspecting a frosted evaporator inside a walk-in cold room",
        "excerpt": "A thin layer of frost is normal. A block of ice on the evaporator is not, and it means the room is slowly losing its ability to stay cold.",
        "sections": [
            ("Frost is normal, ice is not", [
                "Every cold room evaporator collects some frost: it is pulling moisture out of the air. A defrost cycle melts that frost a few times a day and drains the water away.",
                "When the defrost can't keep up, frost turns to solid ice. Ice blocks the airflow through the coil, the room warms up, the system runs longer, and even more ice forms. Left alone, it ends with a room that won't hold temperature.",
            ], []),
            ("The most common causes", [
                "In our experience, icing nearly always comes down to one of these:",
            ], [
                "A failed defrost heater, so the coil never fully clears",
                "A defrost timer or controller set wrong, or faulty",
                "A blocked or frozen drain line, so meltwater refreezes on the coil",
                "A torn door seal or door left open, letting warm, humid air in",
                "An evaporator fan that has stopped, so air isn't moving across the coil",
                "Low refrigerant from a leak, which makes the coil run too cold",
            ]),
            ("What you can check yourself", [
                "Before calling anyone, there are a few safe checks that help us find the fault faster:",
            ], [
                "Is the door closing fully and the seal intact all the way round?",
                "Are the evaporator fans inside the room turning?",
                "Is water dripping or pooling under the evaporator?",
                "Has anyone changed the controller settings recently?",
            ]),
            ("Don't chip the ice off", [
                "It is tempting to hack the ice away with a knife or screwdriver. Please don't. The evaporator fins and tubes are thin and easy to puncture, and a punctured coil turns a defrost problem into a gas leak and a much bigger repair.",
                "If the room must keep running, move valuable stock to another cold space if you can, keep the door shut, and call us.",
            ], []),
            ("How we fix it", [
                "We start by safely defrosting the coil, then test the defrost heaters, timer or controller settings, drain line and heater, and fans. We check the door seal and the refrigerant charge, because a low charge from a leak can cause icing too. The aim is to fix the reason the ice formed, not just melt it.",
            ], []),
        ],
        "related": ["cold-room-repairs-durban.html", "refrigeration-unit-repairs-durban.html"],
    },
    {
        "slug": "blog-bottle-cooler-not-cooling.html",
        "date": "2026-10-30",
        "title": "Bottle Cooler Not Cooling? 6 Checks Before You Call a Technician",
        "meta_title": "Bottle Cooler Not Cooling? 6 Checks | RM Air Solutions",
        "desc": "Warm drinks lose sales. Six quick checks shop owners can do when a glass-door bottle cooler stops cooling, and the faults that need a technician.",
        "img": "blog-bottle-cooler",
        "img_alt": "Glass-door bottle coolers full of cold drinks in a shop",
        "excerpt": "Before you pay for a call-out, a few simple checks can rule out the easy causes, and tell us exactly what to look for if it is a real fault.",
        "sections": [
            ("Why bottle coolers fail in summer", [
                "Bottle coolers have a tough life: doors opened all day, packed shelves, and often a hot shopfront or a spot near the road. Most of the coolers we're called to in summer have a dirty condenser or a tired fan motor. Both are easy to catch early.",
            ], []),
            ("Six checks you can do yourself", [
                "Switch the cooler off at the plug before touching anything near the fan or compressor.",
            ], [
                "Power: is it plugged in properly and is the breaker on? Does the light come on?",
                "Thermostat: has the dial been turned to a warmer setting by accident?",
                "Condenser: look at the black grille, usually at the bottom or back. If it's furry with dust, that's very likely the problem.",
                "Ventilation: is the cooler pushed hard against a wall or boxed in? It needs space to breathe.",
                "Door seals: does each door close and seal fully, with no gaps or splits?",
                "Loading: are drinks blocking the fan or the air vents inside the cabinet?",
            ]),
            ("Faults that need a technician", [
                "If the checks above don't sort it out, these are jobs for us:",
            ], [
                "Compressor clicking on and off, or humming without starting",
                "Fan motors that have stopped or are noisy",
                "Ice building up on the back panel",
                "Cooler runs non-stop but never gets cold, which often means a gas leak",
            ]),
            ("Prevent it next time", [
                "Cleaning the condenser every three months in a dusty shop prevents most summer breakdowns. It takes a few minutes and costs far less than a repair or lost sales on a hot day.",
                "One last thing: if the cooler belongs to a drinks supplier, check your agreement before booking a repair. Many suppliers handle repairs on their own coolers.",
            ], []),
        ],
        "related": ["bottle-cooler-repairs-durban.html", "display-fridge-repairs-durban.html"],
    },
    {
        "slug": "blog-aircon-service-durban.html",
        "date": "2026-10-30",
        "title": "How Often Should You Service an Aircon in Durban?",
        "meta_title": "How Often to Service an Aircon in Durban | RM Air Solutions",
        "desc": "Durban's heat and humidity are hard on aircons. How often offices, shops and homes should service their aircons, and what a proper service includes.",
        "img": "blog-aircon-service",
        "img_alt": "Technician cleaning the filters of a wall-mounted split aircon",
        "excerpt": "In a humid city, an aircon pulls a lot of water out of the air. That water is why servicing matters more here than in drier parts of the country.",
        "sections": [
            ("The short answer", [
                "For offices, shops, salons and restaurants where the aircon runs most of the day: every six months. For most homes: once a year, ideally in spring before the heat arrives.",
                "Units near the sea, such as Umhlanga, central Durban, the Bluff and Amanzimtoti, benefit from more frequent cleaning of the outdoor unit because of salt in the air.",
            ], []),
            ("Why humidity makes servicing important", [
                "An aircon dries the air as it cools it. All that water runs over the indoor coil and down a drain line. On a dirty coil, the damp dust feeds mould, which is the musty smell many people notice when the aircon starts. The same sludge blocks the drain, and that is where most indoor leaks come from.",
            ], []),
            ("What a proper service includes", [
                "A quick filter rinse isn't a service. A proper one covers:",
            ], [
                "Filters cleaned or replaced",
                "Indoor coil and blower wheel cleaned",
                "Drain line and tray cleared and flushed",
                "Outdoor condenser coil cleaned",
                "Gas pressures and temperatures checked",
                "Electrical connections and operation tested",
            ]),
            ("Signs your aircon is overdue", [
                "Book a service if you notice any of these:",
            ], [
                "A musty or damp smell when it starts",
                "Weaker airflow than before",
                "The room taking much longer to cool",
                "Water dripping from the indoor unit",
                "Higher electricity bills in summer",
            ]),
            ("Servicing several units", [
                "For offices and shops with several units, servicing them all in one visit is quicker and usually works out cheaper per unit. Send us the number of units and we'll quote.",
            ], []),
        ],
        "related": ["aircon-servicing-durban.html", "aircon-repairs-durban.html"],
    },
    {
        "slug": "blog-what-size-aircon.html",
        "date": "2026-10-30",
        "title": "What Size Aircon Do I Need? A BTU Guide for Durban",
        "meta_title": "What Size Aircon Do I Need? BTU Guide | RM Air Solutions",
        "desc": "How to choose the right aircon size in BTU for a room, office or shop in Durban, with a rough room-size guide and the factors that push the size up.",
        "img": "blog-aircon-size",
        "img_alt": "Modern office with a wall-mounted split air-conditioner",
        "excerpt": "Too small and the aircon runs flat out without ever cooling the room. Too big and it switches on and off without drying the air. Here's how to get it right.",
        "sections": [
            ("What BTU means", [
                "Aircon capacity is usually given in BTU (British Thermal Units) per hour. The higher the number, the more heat the unit can remove from a room. Common split-unit sizes are 9 000, 12 000, 18 000 and 24 000 BTU, with larger units available for bigger spaces.",
            ], []),
            ("A rough room-size guide", [
                "As a starting point for rooms with normal ceiling heights:",
            ], [
                "9 000 BTU: up to about 15 to 18 square metres, such as a bedroom or small office",
                "12 000 BTU: about 18 to 25 square metres, such as a main bedroom or study",
                "18 000 BTU: about 25 to 35 square metres, such as a lounge or open-plan office",
                "24 000 BTU: about 35 to 50 square metres, such as a large lounge or small shop",
            ]),
            ("What pushes the size up in Durban", [
                "That guide is only a starting point. These all mean you need more capacity:",
            ], [
                "Sun on large windows, especially west-facing glass in the afternoon",
                "High ceilings or open-plan spaces",
                "Lots of people, as in a salon, restaurant or meeting room",
                "Heat from equipment: kitchens, servers, printers or display lighting",
                "A top-floor room under a hot roof",
            ]),
            ("Why bigger isn't better", [
                "An oversized unit cools the air quickly and switches off before it has had time to remove the moisture. In Durban's humidity that leaves the room cool but clammy. A correctly sized unit runs long enough to dry the air as well.",
            ], []),
            ("Getting it right", [
                "Send us the room size, which way the windows face and what the room is used for, and we'll recommend the right capacity before you buy. If you've already bought a unit, we'll install that one.",
            ], []),
        ],
        "related": ["aircon-installation-durban.html", "aircon-servicing-durban.html"],
    },
    {
        "slug": "blog-coastal-aircon-salt-air.html",
        "date": "2026-10-30",
        "title": "Salt Air and Your Aircon: Protecting Outdoor Units on the Coast",
        "meta_title": "Salt Air & Aircons on the Durban Coast | RM Air Solutions",
        "desc": "Why aircons and condensing units near the sea in Umhlanga, central Durban and Amanzimtoti corrode faster, and how to make them last longer.",
        "img": "blog-coastal-aircon",
        "img_alt": "Outdoor aircon units on a building near the sea",
        "excerpt": "Sea air carries salt, and salt eats aluminium fins and copper pipes. Here's what it does to outdoor units and how to slow it down.",
        "sections": [
            ("What salt air does to an outdoor unit", [
                "Outdoor aircon units and refrigeration condensers pull large volumes of air through their coils. Near the sea, that air carries fine salt that settles on the aluminium fins and copper tubes. Combined with Durban's humidity, it corrodes the coil from the outside in.",
                "Corroded fins crumble and block airflow, so the unit runs hotter and less efficiently. Eventually the corrosion reaches the copper and the coil starts leaking gas. Electrical connections and the outdoor fan motor suffer too.",
            ], []),
            ("Where we see it most", [
                "Units close to the beachfront, in Umhlanga, central Durban and the Point, the Bluff and Amanzimtoti, show corrosion much earlier than units inland. Rooftop and balcony units that face the sea are worst affected.",
            ], []),
            ("Signs of corrosion", [
                "Look at your outdoor unit. Call us if you notice:",
            ], [
                "White or green powdery deposits on the fins or pipes",
                "Fins that crumble or flake when touched gently",
                "Rust on the casing, screws or brackets",
                "An aircon that has needed regassing more than once",
            ]),
            ("How to make coastal units last longer", [
                "You can't stop the salt, but you can slow the damage a lot:",
            ], [
                "Clean and rinse the outdoor coil more often than an inland unit, about every three to six months",
                "Keep the area around the unit clear so air flows freely",
                "Check brackets and fixings for rust before they weaken",
                "When replacing a unit near the sea, ask about models with protected or coated coils",
            ]),
            ("Commercial refrigeration on the coast", [
                "The same applies to condensing units for cold rooms and display fridges in coastal restaurants and shops. A corroded condenser coil makes the whole system work harder, and that shows up as high running costs and compressor failures.",
            ], []),
        ],
        "related": ["aircon-servicing-durban.html", "aircon-refrigeration-umhlanga.html"],
    },
]

# Second batch (Nov 2026), newest first
from blog_more import MORE_POSTS  # noqa: E402

POSTS = MORE_POSTS + POSTS
