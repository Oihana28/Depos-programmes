def concentration_CH4(annee):
    """
    Renvoie la concentration estimée de CH4 en ppm pour une année donnée.
    """
    if annee <=1786 :
        return 675
    
    else:
        return  5.07 * annee - 8.38 *( 10**3)  # modèle linéaire post-1952
    
def concentration_CH4_altitude(altitude):
    """
    Renvoie la proportion estimée de CH4 en ppm pour une altitude donnée.
    """
    if  altitude < 9:
        return 1800   # valeur à basse altitude en ppb
    
    elif  9 <= altitude <= 45:
        return   -45.2 * altitude + 2190 #valeur à haute altitude
    else: 
        return 100  #valeur avec la fonction affine
    
def coef_augmentation(concentration): 
    ref = concentration_CH4(2020) #année de référence du graphique des altitudes 
    coef = (concentration /ref)   
    return coef    

def augmentation_altitude(coef, altitude):
    prop_altitude = concentration_CH4_altitude(altitude) #proportion de CH4 à une altitude donnée en 2020
    prop_annee = prop_altitude * coef
    return prop_annee

prop = concentration_CH4(2000) #essai du programme pour l'année 2000
c=coef_augmentation(prop)
print (concentration_CH4_altitude(20))
print (augmentation_altitude(c,20))
