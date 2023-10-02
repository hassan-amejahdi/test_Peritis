Partie SQL hors ligne:

Pour calculer l ID de la session de chaque événement en utilisant BigQuery
 et en prenant en compte une durée d'inactivité de session d'une minute,
 vous pouvez utiliser la fonction d'analyse LAG pour comparer les horodatages
 des événements successifs et attribuer un nouvel ID de session lorsque la durée
 d' inactivité est supérieure à une minute.
 Voici le code SQL nécessaire pour obtenir le résultat attendu :
 
 WITH EventsWithSession AS (
  SELECT
    event_id,
    created_ts,
    SUM(session_start) OVER (ORDER BY created_ts) AS session_id
  FROM (
    SELECT
      event_id,
      created_ts,
      IFNULL(TIMESTAMP_DIFF(created_ts, LAG(created_ts) OVER (ORDER BY created_ts), SECOND) > 60, TRUE) AS session_start
    FROM
      YourTable
  )
)

SELECT
  event_id,
  created_ts,
  session_id
FROM
  EventsWithSession
ORDER BY
  created_ts;

Voici comment cela fonctionne :

Dans la sous-requête (EventsWithSession), nous utilisons la fonction LAG
 pour comparer les horodatages successifs des événements
 et calculer si la durée depuis le dernier événement
 est supérieure à 60 secondes (1 minute). Si oui, nous marquons 
 l'événement actuel comme le début d'une nouvelle session.

Ensuite, nous utilisons SUM(session_start) OVER (ORDER BY created_ts) 
pour attribuer un ID de session cumulatif en fonction des marqueurs de début 
de session.

Enfin, nous sélectionnons les informations pertinentes, y compris l'ID de session,
 pour obtenir le résultat attendu.

Ce code SQL attribuera un ID de session à chaque événement en prenant en compte
 une durée d'inactivité de session d'une minute.