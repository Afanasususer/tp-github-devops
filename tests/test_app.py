from app import calculer_imc, convertir_temperature

def test_imc_normal():
    imc, cat = calculer_imc(70, 1.75)
    assert cat == "Poids normal"

def test_imc_surpoids():
    imc, cat = calculer_imc(90, 1.75)
    assert cat == "Surpoids"

def test_temp_celsius():
    val, unite = convertir_temperature(100, "C")
    assert val == 212.0 and unite == "F"

def test_temp_fahrenheit():
    val, unite = convertir_temperature(32, "F")
    assert val == 0.0 and unite == "C"
