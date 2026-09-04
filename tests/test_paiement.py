from src.paiement import calcul_frais, autoriser

def test_frais_debit():
    assert calcul_frais(100.0, "debit") == 0.5

def test_frais_minimum():
    assert calcul_frais(1.0, "debit") == 0.05
