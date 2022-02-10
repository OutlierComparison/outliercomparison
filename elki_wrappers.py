


  java -jar elki.jar KDDCLIApplication \
    -dbc.in mouse.csv \
    -algorithm clustering.kmeans.KMedoidsEM \
    -kmeans.k $k \
    -resulthandler ResultWriter -out.gzip \
    -out output/k-$k 

