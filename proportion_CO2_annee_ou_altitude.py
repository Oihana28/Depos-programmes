
# fonction pour une année donnée 
def concentration_CO2_annee(annee):
    if 1838 <= annee <= 1972:
        return 0.294 * annee - 262
    elif annee < 1952:
        return 278  # valeur moyenne avant l'ère industrielle
    else:
        return 1.9 * annee - 3430  # modèle linéaire post-1952
    


# fonction pour une altitude donnée 
def concentration_CO2_altitude(altitude):
  
    if 0 <= altitude <= 60:
        return 380
    elif altitude > 132:
        return 0  # valeur à haute altitude
    else:
        return -5.26 * altitude + 736 #via l'équation de la fonction affine 
    
