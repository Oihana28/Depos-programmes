def concentration_CO2(annee):
    """
    Renvoie la concentration estimée de CO₂ en ppm pour une année donnée.
    """
    if 1838 <= annee <= 1972:
        return 0.294 * annee - 262
    elif annee < 1838:
        return 278  # valeur moyenne avant l'ère industrielle
    else:
        return 1.9 * annee - 3430  # modèle linéaire post-1952


def concentration_CO2_altitude(altitude):
    """
    Renvoie la proportion estimée de CO₂ en ppm pour une altitude donnée.
    """
    if 0 <= altitude <= 60:
        return 380   # valeur à basse altitude
    elif altitude > 132:
        return 0  #valeur à haute altitude
    else: 
        return -5.26 * altitude + 736 #valeur avec la fonction affine
    

def coef_augmentation(concentration): 
    ref = concentration_CO2(2000) #année de référence du graphique des altitudes 
    coef = (concentration /ref)   
    return coef    

def augmentation_altitude(coef, altitude):
    prop_altitude = concentration_CO2_altitude(altitude) #proportion de CO2 à une altitude donnée en 2000
    prop_annee = prop_altitude * coef
    return prop_annee





