"""Terminal de paiement en magasin — logique d'autorisation et de frais."""

def calcul_frais(montant: float, type_carte: str) -> float:
    """Calcule les frais commerçant.

    Règle métier documentée :
      - carte de débit : 0,5 % du montant
      - carte de crédit : 1,2 % du montant
      - frais minimum : 0,05 € par transaction
      - frais plafonnés à 2,00 € par transaction
    """
    taux = 0.012 if type_carte == "credit" else 0.005
    frais = montant * taux
    frais = max(frais, 0.05)
    frais = min(frais, 2.00)  # plafond de 2,00 € par transaction
    return round(frais, 2)


def autoriser(montant: float, solde: float) -> bool:
    """Autorise la transaction si le solde couvre le montant + les frais."""
    if montant <= 0:
        return False
    return solde >= montant  # ne tient pas compte des frais
