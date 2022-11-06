import Lab2.bmi

def test_bmi_under_weight():
    height = 1.75
    weight = 30
    result = Lab2.bmi.calculate_bmi(height, weight)
    assert (result == -1)

def test_bmi_normal_weight():
    height = 1.75
    weight = 60
    result = Lab2.bmi.calculate_bmi(height, weight)
    assert (result == 0)

def test_bmi_over_weight():
    height = 1.75
    weight = 100
    result = Lab2.bmi.calculate_bmi(height, weight)
    assert (result == 1)

