class Personnage:
    def __init__(self, _id=None, nom="", ATK=0, DEF=0, PV=0):
        self.id = _id
        self.nom = nom
        self.ATK = ATK
        self.DEF = DEF
        self.PV = PV

    @staticmethod
    def from_dict(data):
        return Personnage(
            _id=data.get("_id"),
            nom=data["nom"],
            ATK=data["ATK"],
            DEF=data["DEF"],
            PV=data["PV"]
        )

class Monstre:
    def __init__(self, _id=None, nom="", ATK=0, DEF=0, PV=0):
        self.id = _id
        self.nom = nom
        self.ATK = ATK
        self.DEF = DEF
        self.PV = PV

    @staticmethod
    def from_dict(data):
        return Monstre(
            _id=data.get("_id"),
            nom=data["nom"],
            ATK=data["ATK"],
            DEF=data["DEF"],
            PV=data["PV"]
        )
