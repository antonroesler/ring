from ring.db.places import Place, Places
from ring.db.species import Species, BirdSpecies
from ring.db.rings import Ring, Rings
from ring.db.sighting import Sighting, Sightings

places = [
    Place(name="Ostpark, Frankfurt", lon=8.702778, lat=50.116667),
    Place(name="Grüneburkpark, Frankfurt", lon=8.666667, lat=50.116667),
    Place(name="Riedberg, Frankfurt", lon=8.683333, lat=50.166667),
    Place(name="Günthersburgpark, Frankfurt", lon=8.7, lat=50.133333),
    Place(name="Niddapark, Frankfurt", lon=8.666667, lat=50.133333),
    Place(name="Huthpark, Frankfurt", lon=8.683333, lat=50.116667),
    Place(name="Galluspark, Frankfurt", lon=8.65, lat=50.116667),
    Place(name="Enkheimer Ried, Frankfurt", lon=8.733333, lat=50.133333),
    Place(name="Mainufer, Frankfurt", lon=8.683333, lat=50.1),
    Place(name="Hafenpark, Frankfurt", lon=8.7, lat=50.1),
    Place(name="Bad Vilbel", lon=8.733333, lat=50.183333),
    Place(name="Feldberg", lon=8.483333, lat=50.233333),
]

species = [
    BirdSpecies(name="Graugans", scientific_name="Anser anser"),
    BirdSpecies(name="Nilgans", scientific_name="Alopochen aegyptiaca"),
    BirdSpecies(name="Kanadagans", scientific_name="Branta canadensis"),
    BirdSpecies(name="Brandgans", scientific_name="Tadorna tadorna"),
    BirdSpecies(name="Gänsesäger", scientific_name="Mergus merganser"),
    BirdSpecies(name="Haubentaucher", scientific_name="Podiceps cristatus"),
    BirdSpecies(name="Kormoran", scientific_name="Phalacrocorax carbo"),
    BirdSpecies(name="Silberreiher", scientific_name="Ardea alba"),
    BirdSpecies(name="Graureiher", scientific_name="Ardea cinerea"),
    BirdSpecies(name="Höckerschwan", scientific_name="Cygnus olor"),
    BirdSpecies(name="Stockente", scientific_name="Anas platyrhynchos"),
    BirdSpecies(name="Mandarinente", scientific_name="Aix galericulata"),
    BirdSpecies(name="Knäkente", scientific_name="Anas querquedula"),
    BirdSpecies(name="Löffelente", scientific_name="Anas clypeata"),
    BirdSpecies(name="Krickente", scientific_name="Anas crecca"),
    BirdSpecies(name="Blaumeise", scientific_name="Cyanistes caeruleus"),
    BirdSpecies(name="Kohlmeise", scientific_name="Parus major"),
    BirdSpecies(name="Amsel", scientific_name="Turdus merula"),
    BirdSpecies(name="Rotkehlchen", scientific_name="Erithacus rubecula"),
    BirdSpecies(name="Buchfink", scientific_name="Fringilla coelebs"),
    BirdSpecies(name="Grünfink", scientific_name="Chloris chloris"),
    BirdSpecies(name="Goldammer", scientific_name="Emberiza citrinella"),
    BirdSpecies(name="Star", scientific_name="Sturnus vulgaris"),
    BirdSpecies(name="Elster", scientific_name="Pica pica"),
    BirdSpecies(name="Rabe", scientific_name="Corvus corax"),
    BirdSpecies(name="Silbermöwe", scientific_name="Larus argentatus"),
    BirdSpecies(name="Lachmöwe", scientific_name="Larus ridibundus"),
    BirdSpecies(name="Sturmmöwe", scientific_name="Larus canus"),
    BirdSpecies(name="Heringsmöwe", scientific_name="Larus fuscus"),
    BirdSpecies(name="Mantelmöwe", scientific_name="Larus marinus"),
]

rings = [
    Ring(num="DEWAG 1234", species="Graugans"),
    Ring(num="DEWAG 1235", species="Graugans"),
    Ring(num="DEWAG 1236", species="Graugans"),
    Ring(num="DEWAG 1237", species="Graugans"),
    Ring(num="DEWAG 1238", species="Graugans"),
    Ring(num="DEWAG 1239", species="Graugans"),
    Ring(num="DEWAG 1240", species="Graugans"),
    Ring(num="DEWAG 1241", species="Graugans"),
    Ring(num="DEWAG 1242", species="Graugans"),
    Ring(num="CY0032", species="Heringsmöwe"),
    Ring(num="CY0033", species="Heringsmöwe"),
    Ring(num="A1234", species="Lachmöwe"),
    Ring(num="A1235", species="Lachmöwe"),
    Ring(num="A1236", species="Lachmöwe"),
    Ring(num="A1237", species="Lachmöwe"),
    Ring(num="A1238", species="Lachmöwe"),
    Ring(num="A1239", species="Lachmöwe"),
    Ring(num="DEX000947362", species="Kanadagans"),
    Ring(num="DEX000947363", species="Kanadagans"),
    Ring(num="DEX000947364", species="Kanadagans"),
    Ring(num="DEX000947365", species="Kanadagans"),
    Ring(num="DEX000947366", species="Kanadagans"),
    Ring(num="DEX000947367", species="Kanadagans"),
    Ring(num="DEX000947368", species="Kanadagans"),
    Ring(num="DEX000947369", species="Kanadagans"),
    Ring(num="DEX000947370", species="Kanadagans"),
    Ring(num="DEX000947371", species="Kanadagans"),
    Ring(num="DEX000947372", species="Kanadagans"),
    Ring(num="DEX000947373", species="Kanadagans"),
    Ring(num="DEX000947374", species="Kanadagans"),
    Ring(num="DEX000947375", species="Kanadagans"),
    Ring(num="DEX000947376", species="Kanadagans"),
]

sightings = [
    Sighting(
        place="Ostpark, Frankfurt",
        ring="DEWAG 1234",
        year=2021,
        month=5,
        day=1,
        hour=8,
        minute=0,
    ),
    Sighting(
        place="Ostpark, Frankfurt",
        ring="DEWAG 1235",
        year=2021,
        month=5,
        day=1,
        hour=8,
        minute=0,
    ),
    Sighting(
        place="Ostpark, Frankfurt",
        ring="DEWAG 1236",
        year=2021,
        month=5,
        day=1,
        hour=8,
        minute=0,
    ),
    Sighting(
        place="Grüneburkpark, Frankfurt",
        ring="DEWAG 1237",
        year=2021,
        month=5,
        day=1,
        hour=8,
        minute=0,
    ),
    Sighting(
        place="Grüneburkpark, Frankfurt",
        ring="DEWAG 1237",
        year=2021,
        month=6,
        day=1,
        hour=18,
        minute=0,
    ),
]


for p in Places Places.insert()