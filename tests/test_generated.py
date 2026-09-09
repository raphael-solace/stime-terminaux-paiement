import pytest

# Tests generes automatiquement pour: PR #2 frais + controle de solde
# Regle: le controle de solde a l'autorisation inclut desormais les frais.

def autorise(solde, montant, frais):
    return solde >= montant + frais

def test_solde_suffisant_sans_frais():
    assert autorise(100, 50, 0) is True

def test_solde_insuffisant_a_cause_des_frais():
    assert autorise(50, 50, 2) is False

def test_cas_limite_solde_egal_montant_plus_frais():
    assert autorise(52, 50, 2) is True

def test_frais_nuls():
    assert autorise(50, 50, 0) is True

def test_insuffisant_d_un_centime():
    assert autorise(51.99, 50, 2) is False
