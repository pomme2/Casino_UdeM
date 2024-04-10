## Nom du Projet: Casino UdeM projet 2024

### Description:
Ce projet est une application web Flask qui interagit avec une base de données SQL Server. Il fournit des fonctionnalités pour gérer les tables et exécuter des requêtes SQL. L'application nécessite l'installation de Flask et de pyodbc. De plus, SQL Server Management Studio doit être configuré pour activer tous les ports pour SQL Server.

### Installation:
1. Assurez-vous que Python est installé sur votre système.
2. Installez Flask en utilisant pip :
    ```
    pip install flask
    ```
3. Installez pyodbc en utilisant pip :
    ```
    pip install pyodbc
    ```
4. Configurez SQL Server Management Studio pour activer tous les ports pour SQL Server.

### Utilisation:
1. Exécutez Tables.py pour créer les tables nécessaires dans la base de données SQL Server :
    ```
    python Tables.py
    ```
2. Exécutez requetes.py pour effectuer les opérations de base de données requises :
    ```
    python requetes.py
    ```
3. Lancez app.py pour démarrer l'application Flask :
    ```
    python app.py
    ```
4. Accédez à l'application Flask en suivant le lien fourni dans la console.

### Note Importante:
- Assurez-vous que l'instance SQL Server est nommée "projdb" comme mentionné dans le code de l'application.
- Les fichiers HTML ne sont pas dynamiques ; ils sont servis via app.py.

### Fichiers:
1. Tables.py - Script Python pour créer les tables nécessaires dans la base de données.
2. requetes.py - Script Python pour effectuer des opérations de base de données.
3. app.py - Application web Flask.
4. Autres fichiers HTML - Fichiers HTML statiques servis par l'application Flask.

### Contributeurs:
- [Carlos ED, Lucky, Tarek,Antoine, Aragorn]
