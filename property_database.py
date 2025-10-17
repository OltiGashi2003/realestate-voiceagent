"""
Property Database for Ingolstadt Real Estate
Based on LiveKit External API Pattern from official documentation
"""

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Property:
    """Represents a real estate property"""
    id: str
    type: str  # "Wohnung", "Haus", "Penthouse", "Reihenhaus"
    title: str
    district: str
    address: str
    price: int  # Monthly rent or purchase price
    size: int  # Square meters
    rooms: float
    bedrooms: int
    bathrooms: int
    available: bool
    listing_type: str  # "Miete" or "Kauf"
    features: List[str]
    description: str


# Sample properties in Ingolstadt
PROPERTIES: List[Property] = [
    # Apartments - Miete (Rental)
    Property(
        id="A001",
        type="Wohnung",
        title="Moderne 2-Zimmer-Wohnung in Zentrum",
        district="Zentrum",
        address="Ludwigstraße 45",
        price=850,
        size=65,
        rooms=2,
        bedrooms=1,
        bathrooms=1,
        available=True,
        listing_type="Miete",
        features=["Balkon", "Einbauküche", "Tiefgarage"],
        description="Helle Wohnung im Herzen von Ingolstadt mit Balkon und moderner Ausstattung."
    ),
    Property(
        id="A002",
        type="Wohnung",
        title="Geräumige 3-Zimmer-Wohnung mit Garten",
        district="Haunwöhr",
        address="Beethovenstraße 12",
        price=1100,
        size=85,
        rooms=3,
        bedrooms=2,
        bathrooms=1,
        available=True,
        listing_type="Miete",
        features=["Gartenzugang", "Einbauküche", "Stellplatz"],
        description="Familienfreundliche Wohnung mit direktem Gartenzugang in ruhiger Lage."
    ),
    Property(
        id="A003",
        type="Wohnung",
        title="1-Zimmer-Apartment für Singles",
        district="Nordwest",
        address="Am Stein 8",
        price=550,
        size=38,
        rooms=1,
        bedrooms=1,
        bathrooms=1,
        available=True,
        listing_type="Miete",
        features=["Möbliert", "Internet", "Waschmaschine"],
        description="Kompaktes, voll möbliertes Apartment - perfekt für Studenten oder Pendler."
    ),
    Property(
        id="A004",
        type="Wohnung",
        title="4-Zimmer-Wohnung mit 2 Balkonen",
        district="Südwest",
        address="Hollerstraße 23",
        price=1350,
        size=110,
        rooms=4,
        bedrooms=3,
        bathrooms=2,
        available=True,
        listing_type="Miete",
        features=["2 Balkone", "Einbauküche", "Tiefgarage", "Aufzug"],
        description="Großzügige Familienwohnung mit viel Platz und zwei Balkonen."
    ),
    Property(
        id="A005",
        type="Wohnung",
        title="Penthouse mit Dachterrasse",
        district="Zentrum",
        address="Theresienstraße 67",
        price=1850,
        size=120,
        rooms=3,
        bedrooms=2,
        bathrooms=2,
        available=True,
        listing_type="Miete",
        features=["Dachterrasse", "Luxusausstattung", "Tiefgarage", "Aufzug"],
        description="Exklusives Penthouse mit großer Dachterrasse und Premiumausstattung."
    ),
    
    # Apartments - Kauf (Purchase)
    Property(
        id="A006",
        type="Wohnung",
        title="Neubauwohnung 3-Zimmer",
        district="Oberhaunstadt",
        address="Münchener Straße 134",
        price=320000,
        size=78,
        rooms=3,
        bedrooms=2,
        bathrooms=1,
        available=True,
        listing_type="Kauf",
        features=["Neubau", "Balkon", "Einbauküche", "Fußbodenheizung"],
        description="Erstbezug! Moderne Neubauwohnung mit hochwertiger Ausstattung."
    ),
    Property(
        id="A007",
        type="Wohnung",
        title="2-Zimmer-Eigentumswohnung",
        district="Nordost",
        address="Goethestraße 89",
        price=195000,
        size=58,
        rooms=2,
        bedrooms=1,
        bathrooms=1,
        available=True,
        listing_type="Kauf",
        features=["Balkon", "Keller", "Stellplatz"],
        description="Gepflegte Eigentumswohnung als Kapitalanlage oder Eigennutzung."
    ),
    Property(
        id="A008",
        type="Wohnung",
        title="4-Zimmer-Maisonette-Wohnung",
        district="Haunwöhr",
        address="Schillerstraße 45",
        price=425000,
        size=135,
        rooms=4,
        bedrooms=3,
        bathrooms=2,
        available=True,
        listing_type="Kauf",
        features=["Maisonette", "2 Balkone", "Tiefgarage", "Kamin"],
        description="Einzigartige Maisonette-Wohnung auf zwei Ebenen mit Kamin."
    ),
    Property(
        id="A009",
        type="Wohnung",
        title="Barrierefreie 3-Zimmer-Wohnung",
        district="Südwest",
        address="Ringstraße 12",
        price=285000,
        size=82,
        rooms=3,
        bedrooms=2,
        bathrooms=1,
        available=False,
        listing_type="Kauf",
        features=["Barrierefrei", "Aufzug", "Balkon", "Tiefgarage"],
        description="Seniorengerechte Wohnung mit barrierefreiem Zugang und Aufzug."
    ),
    Property(
        id="A010",
        type="Wohnung",
        title="Luxus 3-Zimmer-Wohnung mit Parkblick",
        district="Zentrum",
        address="Am Glacis 3",
        price=475000,
        size=95,
        rooms=3,
        bedrooms=2,
        bathrooms=2,
        available=True,
        listing_type="Kauf",
        features=["Parkblick", "Luxusausstattung", "Balkon", "Tiefgarage"],
        description="Hochwertige Wohnung mit Blick auf den Glacispark."
    ),
    
    # Houses - Miete
    Property(
        id="H001",
        type="Haus",
        title="Einfamilienhaus mit Garten",
        district="Mailing",
        address="Gartenweg 34",
        price=1950,
        size=145,
        rooms=5,
        bedrooms=4,
        bathrooms=2,
        available=True,
        listing_type="Miete",
        features=["Garten", "Garage", "Keller", "Terrasse"],
        description="Freistehendes Einfamilienhaus mit großem Garten und Garage."
    ),
    Property(
        id="H002",
        type="Reihenhaus",
        title="Modernes Reihenhaus",
        district="Etting",
        address="Birkenweg 78",
        price=1450,
        size=120,
        rooms=4,
        bedrooms=3,
        bathrooms=2,
        available=True,
        listing_type="Miete",
        features=["Garten", "Carport", "Einbauküche"],
        description="Gepflegtes Reihenhaus in familienfreundlicher Nachbarschaft."
    ),
    
    # Houses - Kauf
    Property(
        id="H003",
        type="Haus",
        title="Traumhaus mit Pool",
        district="Friedrichshofen",
        address="Sonnenallee 45",
        price=725000,
        size=185,
        rooms=6,
        bedrooms=4,
        bathrooms=3,
        available=True,
        listing_type="Kauf",
        features=["Pool", "Sauna", "Garage", "Garten", "Smart Home"],
        description="Luxuriöses Einfamilienhaus mit Pool und Wellness-Bereich."
    ),
    Property(
        id="H004",
        type="Haus",
        title="Einfamilienhaus in ruhiger Lage",
        district="Mailing",
        address="Waldstraße 23",
        price=520000,
        size=140,
        rooms=5,
        bedrooms=3,
        bathrooms=2,
        available=True,
        listing_type="Kauf",
        features=["Garten", "Doppelgarage", "Keller", "Kamin"],
        description="Charmantes Einfamilienhaus mit großem Garten am Waldrand."
    ),
    Property(
        id="H005",
        type="Reihenhaus",
        title="Neubau Reihenhaus",
        district="Etting",
        address="Ahornweg 56",
        price=445000,
        size=125,
        rooms=4,
        bedrooms=3,
        bathrooms=2,
        available=True,
        listing_type="Kauf",
        features=["Neubau", "Garten", "Carport", "Fußbodenheizung"],
        description="Erstbezug! Modernes Reihenhaus mit energieeffizienter Ausstattung."
    ),
    
    # Additional Properties
    Property(
        id="A011",
        type="Wohnung",
        title="WG-geeignete 5-Zimmer-Wohnung",
        district="Nordwest",
        address="Studentenstraße 12",
        price=1600,
        size=125,
        rooms=5,
        bedrooms=4,
        bathrooms=2,
        available=True,
        listing_type="Miete",
        features=["WG-geeignet", "2 Balkone", "Keller"],
        description="Großzügige Wohnung ideal für Studenten-WG oder große Familie."
    ),
    Property(
        id="A012",
        type="Wohnung",
        title="3-Zimmer-Wohnung mit Blick auf die Donau",
        district="Nordost",
        address="Donaustraße 89",
        price=1150,
        size=90,
        rooms=3,
        bedrooms=2,
        bathrooms=1,
        available=True,
        listing_type="Miete",
        features=["Donau-Blick", "Balkon", "Einbauküche", "Stellplatz"],
        description="Schöne Wohnung mit traumhaftem Blick auf die Donau."
    ),
    Property(
        id="A013",
        type="Wohnung",
        title="Loft-Wohnung im Industriestil",
        district="Zentrum",
        address="Fabrikstraße 5",
        price=1250,
        size=95,
        rooms=2,
        bedrooms=1,
        bathrooms=1,
        available=True,
        listing_type="Miete",
        features=["Loft-Charakter", "Hohe Decken", "Einbauküche"],
        description="Stylische Loft-Wohnung in umgebautem Industriegebäude."
    ),
    Property(
        id="H006",
        type="Haus",
        title="Doppelhaushälfte",
        district="Oberhaunstadt",
        address="Lindenstraße 67",
        price=465000,
        size=130,
        rooms=5,
        bedrooms=3,
        bathrooms=2,
        available=True,
        listing_type="Kauf",
        features=["Garten", "Garage", "Keller", "Terrasse"],
        description="Gepflegte Doppelhaushälfte mit Garten und Garage."
    ),
    Property(
        id="A014",
        type="Penthouse",
        title="Luxus-Penthouse mit Panoramablick",
        district="Zentrum",
        address="Rathausplatz 1",
        price=895000,
        size=155,
        rooms=4,
        bedrooms=3,
        bathrooms=3,
        available=True,
        listing_type="Kauf",
        features=["360° Dachterrasse", "Luxusausstattung", "Tiefgarage", "Concierge"],
        description="Exklusives Penthouse in bester Innenstadtlage mit Rundumblick."
    ),
]


def search_properties(
    listing_type: Optional[str] = None,
    property_type: Optional[str] = None,
    district: Optional[str] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    min_rooms: Optional[float] = None,
    max_rooms: Optional[float] = None,
    min_size: Optional[int] = None,
    max_size: Optional[int] = None,
    available_only: bool = True,
) -> List[Property]:
    """
    Search properties based on criteria
    
    Args:
        listing_type: "Miete" or "Kauf"
        property_type: "Wohnung", "Haus", "Penthouse", "Reihenhaus"
        district: District name
        min_price: Minimum price
        max_price: Maximum price
        min_rooms: Minimum number of rooms
        max_rooms: Maximum number of rooms
        min_size: Minimum size in square meters
        max_size: Maximum size in square meters
        available_only: Only show available properties
    
    Returns:
        List of matching properties
    """
    results = PROPERTIES.copy()
    
    if available_only:
        results = [p for p in results if p.available]
    
    if listing_type:
        results = [p for p in results if p.listing_type.lower() == listing_type.lower()]
    
    if property_type:
        results = [p for p in results if p.type.lower() == property_type.lower()]
    
    if district:
        results = [p for p in results if p.district.lower() == district.lower()]
    
    if min_price is not None:
        results = [p for p in results if p.price >= min_price]
    
    if max_price is not None:
        results = [p for p in results if p.price <= max_price]
    
    if min_rooms is not None:
        results = [p for p in results if p.rooms >= min_rooms]
    
    if max_rooms is not None:
        results = [p for p in results if p.rooms <= max_rooms]
    
    if min_size is not None:
        results = [p for p in results if p.size >= min_size]
    
    if max_size is not None:
        results = [p for p in results if p.size <= max_size]
    
    return results


def get_property_by_id(property_id: str) -> Optional[Property]:
    """Get a specific property by its ID"""
    for prop in PROPERTIES:
        if prop.id == property_id:
            return prop
    return None


def get_districts() -> List[str]:
    """Get all unique districts"""
    return sorted(list(set(p.district for p in PROPERTIES)))


def get_property_types() -> List[str]:
    """Get all unique property types"""
    return sorted(list(set(p.type for p in PROPERTIES)))
