def concentration_CH4(annee):
    """
    Renvoie la concentration estimée de CH4 en ppm pour une année donnée.
    """
    if annee <=1786 :
        return 675
    
    else:
        return  5.07 * annee - 8.38 *( 10**3)  # modèle linéaire post-1952
    
print (concentration_CH4(1953))